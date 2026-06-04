"""User-facing runner APIs for translation-only processing."""

import asyncio
import json
import re
from pathlib import Path

from core.schema import MetaData, Transcription
from core.utils import normalize_generated_text
from configs.config import Config
from llm.llm_model import LLM
from pipeline.prompts.utils import (
    build_messages_with_audio_placeholders,
    build_prompt_one_pass,
    build_prompt_translation_audio_assisted,
    build_prompt_translation_only,
)
from pipeline.providers.omni_translation_provider import OmniTranslationProvider
from pipeline.providers.raw_translation_provider import RawTranslationProvider
from pipeline.providers.retry_error_rendering import is_system_or_provider_error
from pipeline.schema import PipelineRecord
from pipeline.schema import (
    RawTranslationArtifact,
    StatusEnum,
    TaskStatus,
    TargetLanguageEntry,
    TranscriptArtifact,
)
from pipeline.runners.utils import (
    append_visualization,
    cache_output_path,
    is_finished_omni_translation_record,
    load_pipeline_records_by_uid,
    omni_translation_errors,
    TqdmBar,
    safe_shard_label,
    stage_output_path_from_input_cache,
    upsert_record,
    visualization_omni_translation_only,
    visualization_translation_only,
    visualized_path,
)


class TranslationOnlyRunner:
    """User-facing translation-only runner while scripts retain dataset-level control."""

    def __init__(
        self,
        llm: LLM,
        concurrency: int = 4,
        *,
        max_retries: int,
    ):
        self.llm = llm
        self.concurrency = concurrency
        self.max_retries = max_retries
        self._semaphore = asyncio.Semaphore(concurrency)
        self._file_lock = asyncio.Lock()
        self._tqdm_bar = TqdmBar()
        self._staged_translation_parser = RawTranslationProvider(
            llm=llm,
            system_prompt="",
            user_prompt_template="",
            max_retries=self.max_retries,
        )

    def reset_progress(
        self,
        *,
        show_tqdm_bar: bool,
        total: int | None,
        desc: str,
        initial: int = 0,
    ) -> None:
        self._tqdm_bar.reset(show_tqdm_bar=show_tqdm_bar, total=total, desc=desc, initial=initial)

    def close_progress(self) -> None:
        self._tqdm_bar.close()

    def is_finished_staged_translation_record(self, record: PipelineRecord) -> bool:
        if not record.target.languages:
            return False
        for code, target in record.target.languages.items():
            status = target.status.raw_translation
            if not target.artifacts.raw_translation.text:
                return False
            if status.status != StatusEnum.FINISHED:
                return False
        return True

    def _staged_translation_target_language_codes(self, record: PipelineRecord) -> list[str]:
        source_language = record.metadata.language
        transcript = record.source.artifacts.transcript
        if transcript is not None and transcript.language_code:
            source_language = transcript.language_code
        return [code for code in Config.language_codes if code != source_language]

    def _validate_staged_translation_prerequisite_record(self, prerequisite_record: PipelineRecord) -> list[str]:
        errors: list[str] = []
        transcript = prerequisite_record.source.artifacts.transcript
        if prerequisite_record.source.status.asr.status != StatusEnum.FINISHED:
            errors.append("Source ASR dependency is not finished")
        if transcript is None or not transcript.text:
            errors.append("Missing source transcript dependency")
        return errors

    def _build_failed_staged_translation_record(
        self,
        prerequisite_record: PipelineRecord,
        stage_label: str,
        errors: list[str],
    ) -> PipelineRecord:
        record = prerequisite_record.model_copy(deep=True)
        for code in self._staged_translation_target_language_codes(record):
            branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
            branch.status.raw_translation = TaskStatus(
                status=StatusEnum.FAILED,
                errors=[f"{stage_label}: {error}" for error in errors],
            )
        return record

    def staged_translation_record_status(self, record: PipelineRecord) -> str:
        if self.is_finished_staged_translation_record(record):
            return "finished"
        for branch in record.target.languages.values():
            if any(error.startswith("prerequisite_invalid:") for error in branch.status.raw_translation.errors):
                return "prerequisite_invalid"
        return "translation_failed"

    def _resolve_target_language_code(self, key: str) -> str:
        if not isinstance(key, str):
            return ""
        text = key.strip()
        if not text:
            return ""

        upper = text.upper()
        if upper in Config.language_codes:
            return upper

        lowered = text.lower()
        for name, code in Config.lang_name2code.items():
            if name.lower() == lowered:
                return code.upper()

        normalized = re.sub(r"[^a-zA-Z]", "", text).lower()
        for name, code in Config.lang_name2code.items():
            if re.sub(r"[^a-zA-Z]", "", name).lower() == normalized:
                return code.upper()

        return ""

    def _extract_staged_translation_payload(self, final_result: object) -> tuple[dict[str, str], list[str]]:
        if not isinstance(final_result, dict):
            return {}, ["Translation result is not a structured mapping"]

        payload = final_result.get("translation") if isinstance(final_result.get("translation"), dict) else final_result
        if not isinstance(payload, dict):
            return {}, ["Translation result is not a structured mapping"]

        translations: dict[str, str] = {}
        errors: list[str] = []
        for key, value in payload.items():
            if not isinstance(value, str):
                errors.append(f"Translation value for '{key}' is not a string")
                continue
            code = self._resolve_target_language_code(key)
            if not code:
                errors.append(f"Unrecognized target language key: {key}")
                continue
            translations[code] = value

        if not translations and not errors:
            errors.append("Translation result is not a structured mapping")
        return translations, errors

    def _resolve_audio_path_for_record(self, dataset_root: Path | None, record: PipelineRecord) -> Path | None:
        if dataset_root is None:
            return None
        if not record.metadata.file_name:
            return None
        source_language = record.metadata.language
        transcript = record.source.artifacts.transcript
        if transcript is not None and transcript.language_code:
            source_language = transcript.language_code
        return dataset_root / "audio" / source_language / record.metadata.file_name

    def _with_staged_translation_retry_feedback(
        self,
        messages: list[dict],
        errors: list[str],
    ) -> list[dict]:
        feedback = (
            "Previous output failed validation:\n"
            + "\n".join(f"- {error}" for error in errors)
            + "\n\nReturn a corrected answer for the same task. "
            "The content inside <result> must be one valid JSON object. "
            "Escape all double quotes inside JSON string values. "
            "Do not output markdown, code fences, or extra text outside <scratchpad> and <result>."
        )
        retry_messages: list[dict] = []
        for message in messages:
            copied = dict(message)
            if copied.get("role") == "user":
                content = copied.get("content")
                if isinstance(content, list):
                    copied["content"] = [{"type": "text", "text": feedback + "\n\n"}] + content
                elif isinstance(content, str):
                    copied["content"] = feedback + "\n\n" + content
            retry_messages.append(copied)
        return retry_messages

    async def _request_staged_translation_with_retries(
        self,
        *,
        messages: list[dict],
        target_lang_codes: list[str],
        max_tokens: int,
        temperature: float,
        top_p: float,
        extra_body: dict | None,
    ) -> tuple[object, str, dict[str, str], list[str]]:
        final_result: object = ""
        scratchpad = ""
        translations_by_code: dict[str, str] = {}
        attempt_errors: list[str] = []

        for n_retry in range(self.max_retries + 1):
            attempt_messages = messages
            if attempt_errors:
                attempt_messages = self._with_staged_translation_retry_feedback(messages, attempt_errors)

            response = await self.llm.chat(
                attempt_messages,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                extra_body=extra_body,
            )
            result_text, scratchpad = self._staged_translation_parser._parse_translation_response(response.content)

            json_errors: list[str] = []
            try:
                final_result = json.loads(result_text)
            except Exception as exc:
                final_result = result_text
                json_errors.append(
                    f"Invalid translation JSON on attempt {n_retry + 1}/{self.max_retries + 1}: {exc}"
                )

            translations_by_code, parse_errors = self._extract_staged_translation_payload(final_result)
            missing_errors = [
                f"Missing translation output for target language: {Config.lang_code2name.get(code, code)}"
                for code in target_lang_codes
                if code not in translations_by_code
            ]
            attempt_errors = json_errors + parse_errors + missing_errors
            if not attempt_errors:
                return final_result, scratchpad, translations_by_code, []
            if n_retry < self.max_retries:
                await asyncio.sleep(0.5 * (n_retry + 1))

        return final_result, scratchpad, translations_by_code, attempt_errors

    async def run_cache_shard(
        self,
        *,
        input_cache_base: Path,
        input_cache_path: Path,
        prerequisite_records: list[PipelineRecord],
        output_root: Path,
        max_current_tasks: int,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        enable_visualization: bool = False,
        enable_audio_assisted_translation: bool = False,
        dataset_root: Path | None = None,
    ) -> dict[str, int | str]:
        output_path = stage_output_path_from_input_cache(
            output_root,
            input_cache_base,
            input_cache_path,
            "translation",
        )
        shard_visualized_path = visualized_path(output_path, "translation")
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        pending_records = [
            record
            for record in prerequisite_records
            if record.uid not in existing_output_by_uid
            or self.staged_translation_record_status(existing_output_by_uid[record.uid]) != "finished"
        ]

        summary: dict[str, int | str] = {
            "output_label": safe_shard_label(output_path),
            "existing_finished": len(prerequisite_records) - len(pending_records),
            "pending": len(pending_records),
            "finished": 0,
            "translation_failed": 0,
            "prerequisite_invalid": 0,
        }

        pending_iter = iter(pending_records)
        active_tasks: dict[asyncio.Task, PipelineRecord] = {}

        def schedule_next() -> None:
            while len(active_tasks) < max_current_tasks:
                prerequisite_record = next(pending_iter, None)
                if prerequisite_record is None:
                    break
                task = asyncio.create_task(
                    self.run_cache_record(
                        prerequisite_record,
                        existing_record=existing_output_by_uid.get(prerequisite_record.uid),
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        extra_body=extra_body,
                        enable_audio_assisted_translation=enable_audio_assisted_translation,
                        dataset_root=dataset_root,
                    )
                )
                active_tasks[task] = prerequisite_record

        schedule_next()
        while active_tasks:
            done, _ = await asyncio.wait(active_tasks.keys(), return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                prerequisite_record = active_tasks.pop(task)
                try:
                    record, visualized = await task
                except Exception as e:
                    if not is_system_or_provider_error(e):
                        raise
                    record = self._build_failed_staged_translation_record(
                        prerequisite_record,
                        "provider_api_error",
                        [str(e)],
                    )
                    visualized = visualization_translation_only(
                        record.uid,
                        record.target.shared.translation_analysis,
                        {},
                        asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                        asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                        status="translation_failed",
                        errors=[f"provider_api_error: {e}"],
                    )
                existing_output_by_uid[prerequisite_record.uid] = record
                await upsert_record(
                    output_path=output_path,
                    record=record,
                    file_lock=self._file_lock,
                )
                if enable_visualization:
                    await append_visualization(
                        shard_visualized_path=shard_visualized_path,
                        visualized=visualized,
                        file_lock=self._file_lock,
                    )
                status = self.staged_translation_record_status(record)
                if status == "finished":
                    self._tqdm_bar.update("Translation-only", n_finished=1, n_failed=0)
                    summary["finished"] += 1
                else:
                    self._tqdm_bar.update("Translation-only", n_finished=0, n_failed=1)
                    errors = [
                        error
                        for branch in record.target.languages.values()
                        for error in branch.status.raw_translation.errors
                    ]
                    self._tqdm_bar.write_latest_error(errors[-1] if errors else None, uid=record.uid, error_name=status)
                    summary[status] += 1
            schedule_next()

        return summary

    async def run_cache_record(
        self,
        prerequisite_record: PipelineRecord,
        *,
        existing_record: PipelineRecord | None = None,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        enable_audio_assisted_translation: bool = False,
        dataset_root: Path | None = None,
    ) -> tuple[PipelineRecord, str]:
        if existing_record and self.is_finished_staged_translation_record(existing_record):
            return existing_record, visualization_translation_only(
                existing_record.uid,
                existing_record.target.shared.translation_analysis,
                {
                    code: branch.artifacts.raw_translation.text
                    for code, branch in sorted(existing_record.target.languages.items())
                    if branch.artifacts.raw_translation.text
                },
                asr_language_name=existing_record.source.artifacts.transcript.language_name if existing_record.source.artifacts.transcript else "",
                asr_text=existing_record.source.artifacts.transcript.text if existing_record.source.artifacts.transcript else "",
            )

        prerequisite_errors = self._validate_staged_translation_prerequisite_record(prerequisite_record)
        if prerequisite_errors:
            record = self._build_failed_staged_translation_record(
                prerequisite_record,
                "prerequisite_invalid",
                prerequisite_errors,
            )
            return record, visualization_translation_only(
                record.uid,
                record.target.shared.translation_analysis,
                {},
                asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                status="prerequisite_invalid",
                errors=[f"prerequisite_invalid: {error}" for error in prerequisite_errors],
            )

        source_record = existing_record or prerequisite_record
        record = source_record.model_copy(deep=True)
        async with self._semaphore:
            return await self._run_staged_translation_record(
                record,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                extra_body=extra_body,
                enable_audio_assisted_translation=enable_audio_assisted_translation,
                dataset_root=dataset_root,
            )

    async def _run_staged_translation_record(
        self,
        record: PipelineRecord,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        enable_audio_assisted_translation: bool = False,
        dataset_root: Path | None = None,
    ) -> tuple[PipelineRecord, str]:
        transcript = record.source.artifacts.transcript
        transcription = Transcription(
            uid=record.uid,
            language=(transcript.language_code if transcript and transcript.language_code else record.metadata.language),
            text=transcript.text if transcript else "",
            author=transcript.author if transcript else "",
        )

        author = self.llm.model_name
        if enable_audio_assisted_translation:
            audio_path = self._resolve_audio_path_for_record(dataset_root, record)
            if audio_path is None or not audio_path.exists():
                error = f"Audio-assisted translation requested but audio file is missing: {audio_path}"
                for code in self._staged_translation_target_language_codes(record):
                    branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
                    branch.status.raw_translation = TaskStatus(
                        status=StatusEnum.FAILED,
                        errors=[error],
                    )
                return record, visualization_translation_only(
                    record.uid,
                    record.target.shared.translation_analysis,
                    {},
                    asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                    asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                    status="translation_failed",
                    errors=[error],
                )
            system_prompt, user_prompt, target_lang_codes = build_prompt_translation_audio_assisted(
                transcription=transcription,
            )
            user_content = build_messages_with_audio_placeholders(user_prompt, str(audio_path))
            messages = [
                {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
                {"role": "user", "content": user_content},
            ]
        else:
            system_prompt, user_prompt, target_lang_codes = build_prompt_translation_only(
                transcription=transcription,
            )
            messages = [
                {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
            ]
        final_result, scratchpad, translations_by_code, parse_errors = await self._request_staged_translation_with_retries(
            messages=messages,
            target_lang_codes=target_lang_codes,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            extra_body=extra_body,
        )

        record.target.shared.translation_analysis = scratchpad

        for code in target_lang_codes:
            branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
            if code in translations_by_code:
                branch.artifacts.raw_translation = RawTranslationArtifact(
                    text=normalize_generated_text(translations_by_code[code], code),
                    author=author,
                )
                branch.status.raw_translation = TaskStatus(status=StatusEnum.FINISHED)
            else:
                errors = list(parse_errors)
                language_name = Config.lang_code2name.get(code, code)
                missing_error = f"Missing translation output for target language: {language_name}"
                if missing_error not in errors:
                    errors.append(missing_error)
                branch.status.raw_translation = TaskStatus(
                    status=StatusEnum.FAILED,
                    errors=errors,
                )

        return record, visualization_translation_only(
            record.uid,
            scratchpad,
            final_result,
            asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
            asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
            errors=[
                error
                for code in target_lang_codes
                for error in record.target.languages[code].status.raw_translation.errors
            ] or None,
        )

    async def run_omni_translation_shard(
        self,
        *,
        metadata_jsonl_path: Path,
        metadata_list: list[MetaData],
        dataset_root: Path,
        output_root: Path,
        max_current_tasks: int,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        enable_visualization: bool = False,
    ) -> dict[str, int | str]:
        output_path = cache_output_path(output_root, metadata_jsonl_path, "translation")
        shard_visualized_path = visualized_path(output_path, "translation")
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        pending_metadata_list = [
            meta
            for meta in metadata_list
            if not is_finished_omni_translation_record(
                existing_output_by_uid.get(meta.uid, PipelineRecord(uid=meta.uid, metadata=meta))
            )
        ]

        summary: dict[str, int | str] = {
            "output_label": safe_shard_label(output_path),
            "existing_finished": len(metadata_list) - len(pending_metadata_list),
            "pending": len(pending_metadata_list),
            "finished": 0,
            "failed": 0,
        }

        pending_iter = iter(pending_metadata_list)
        active_tasks: dict[asyncio.Task, MetaData] = {}

        def schedule_next() -> None:
            while len(active_tasks) < max_current_tasks:
                meta = next(pending_iter, None)
                if meta is None:
                    break
                task = asyncio.create_task(
                    self.run_omni_translation_record(
                        meta,
                        dataset_root,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        extra_body=extra_body,
                    )
                )
                active_tasks[task] = meta

        schedule_next()
        while active_tasks:
            done, _ = await asyncio.wait(active_tasks.keys(), return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                meta = active_tasks.pop(task)
                try:
                    record, visualized = await task
                except Exception as e:
                    if not is_system_or_provider_error(e):
                        raise
                    record = PipelineRecord(uid=meta.uid, metadata=meta)
                    record.source.status.asr = TaskStatus(
                        status=StatusEnum.FAILED,
                        errors=[f"provider_api_error: {e}"],
                    )
                    visualized = visualization_omni_translation_only(
                        uid=meta.uid,
                        scratchpad="",
                        final_result={},
                        asr_language_name="",
                        asr_text="",
                        errors=[f"provider_api_error: {e}"],
                    )
                existing_output_by_uid[meta.uid] = record
                await upsert_record(
                    output_path=output_path,
                    record=record,
                    file_lock=self._file_lock,
                )
                if enable_visualization:
                    await append_visualization(
                        shard_visualized_path=shard_visualized_path,
                        visualized=visualized,
                        file_lock=self._file_lock,
                    )
                if is_finished_omni_translation_record(record):
                    summary["finished"] += 1
                else:
                    summary["failed"] += 1
            schedule_next()

        return summary

    async def run_omni_translation_record(
        self,
        meta: MetaData,
        dataset_root: Path,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        extra_body: dict | None = None,
    ) -> tuple[PipelineRecord, str]:
        async with self._semaphore:
            audio_path = dataset_root / "audio" / meta.language / meta.file_name
            system_prompt, user_prompt, target_language_names = build_prompt_one_pass(meta)
            provider = OmniTranslationProvider(
                llm=self.llm,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                max_retries=self.max_retries,
            )
            record = PipelineRecord(uid=meta.uid, metadata=meta)
            record = await provider.provide(
                record=record,
                audio=str(audio_path),
                target_language_names=target_language_names,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                extra_body=extra_body,
            )
            latest_error = omni_translation_errors(record)[-1] if omni_translation_errors(record) else None
            if latest_error:
                self._tqdm_bar.update("Omni translation-only", n_finished=0, n_failed=1)
                self._tqdm_bar.write_latest_error(latest_error, uid=record.uid, error_name="omni_translation_failed")
            else:
                self._tqdm_bar.update("Omni translation-only", n_finished=1, n_failed=0)
            final_result = {
                "asr": {
                    "language_name": record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                    "language_code": record.source.artifacts.transcript.language_code if record.source.artifacts.transcript else "",
                    "text": record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                },
                "translation": {
                    code: target.artifacts.raw_translation.text
                    for code, target in sorted(record.target.languages.items())
                    if target.artifacts.raw_translation.text
                },
            }
            return record, visualization_omni_translation_only(
                uid=meta.uid,
                scratchpad=record.target.shared.translation_analysis,
                final_result=final_result,
                asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                errors=omni_translation_errors(record),
            )

    async def run_staged_translation_shard(
        self,
        *,
        transcription_jsonl_path: Path,
        transcription_list: list[Transcription],
        output_root: Path,
        max_current_tasks: int,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        enable_visualization: bool = False,
    ) -> dict[str, int | str]:
        output_path = cache_output_path(output_root, transcription_jsonl_path, "translation")
        shard_visualized_path = visualized_path(output_path, "translation")
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        pending_transcriptions = [
            transcription
            for transcription in transcription_list
            if not self.is_finished_staged_translation_record(
                existing_output_by_uid.get(
                    transcription.uid,
                    PipelineRecord(
                        uid=transcription.uid,
                        metadata=MetaData(
                            uid=transcription.uid,
                            file_name="",
                            duration=0.0,
                            sample_rate=0.0,
                            language=transcription.language,
                        ),
                    ),
                )
            )
        ]

        summary: dict[str, int | str] = {
            "output_label": safe_shard_label(output_path),
            "existing_finished": len(transcription_list) - len(pending_transcriptions),
            "pending": len(pending_transcriptions),
            "finished": 0,
            "failed": 0,
        }

        pending_iter = iter(pending_transcriptions)
        active_tasks: dict[asyncio.Task, Transcription] = {}

        def schedule_next() -> None:
            while len(active_tasks) < max_current_tasks:
                transcription = next(pending_iter, None)
                if transcription is None:
                    break
                task = asyncio.create_task(
                    self.run_staged_translation_record(
                        transcription,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        extra_body=extra_body,
                    )
                )
                active_tasks[task] = transcription

        schedule_next()
        while active_tasks:
            done, _ = await asyncio.wait(active_tasks.keys(), return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                transcription = active_tasks.pop(task)
                try:
                    record, visualized = await task
                except Exception as e:
                    if not is_system_or_provider_error(e):
                        raise
                    metadata = MetaData(
                        uid=transcription.uid,
                        file_name="",
                        duration=0.0,
                        sample_rate=0.0,
                        language=transcription.language,
                    )
                    record = PipelineRecord(uid=transcription.uid, metadata=metadata)
                    record.source.artifacts.transcript = TranscriptArtifact(
                        language_code=transcription.language,
                        language_name=Config.lang_code2name.get(transcription.language, transcription.language),
                        text=normalize_generated_text(transcription.text, transcription.language),
                        author=getattr(transcription, "author", ""),
                    )
                    record.source.status.asr = TaskStatus(status=StatusEnum.FINISHED)
                    record = self._build_failed_staged_translation_record(
                        record,
                        "provider_api_error",
                        [str(e)],
                    )
                    visualized = visualization_translation_only(
                        transcription.uid,
                        "",
                        {},
                        asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                        asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                        status="translation_failed",
                        errors=[f"provider_api_error: {e}"],
                    )
                existing_output_by_uid[transcription.uid] = record
                await upsert_record(
                    output_path=output_path,
                    record=record,
                    file_lock=self._file_lock,
                )
                if enable_visualization:
                    await append_visualization(
                        shard_visualized_path=shard_visualized_path,
                        visualized=visualized,
                        file_lock=self._file_lock,
                    )
                if self.is_finished_staged_translation_record(record):
                    summary["finished"] += 1
                else:
                    summary["failed"] += 1
            schedule_next()

        return summary

    async def run_staged_translation_record(
        self,
        transcription: Transcription,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        extra_body: dict | None = None,
    ) -> tuple[PipelineRecord, str]:
        async with self._semaphore:
            author = self.llm.model_name
            system_prompt, user_prompt, target_lang_codes = build_prompt_translation_only(
                transcription=transcription,
            )
            messages = [
                {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
            ]
            final_result, scratchpad, translations_by_code, parse_errors = await self._request_staged_translation_with_retries(
                messages=messages,
                target_lang_codes=target_lang_codes,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                extra_body=extra_body,
            )
            metadata = MetaData(
                uid=transcription.uid,
                file_name="",
                duration=0.0,
                sample_rate=0.0,
                language=transcription.language,
            )
            record = PipelineRecord(uid=transcription.uid, metadata=metadata)
            record.source.artifacts.transcript = TranscriptArtifact(
                language_code=transcription.language,
                language_name=Config.lang_code2name.get(transcription.language, transcription.language),
                text=normalize_generated_text(transcription.text, transcription.language),
                author=getattr(transcription, "author", ""),
            )
            record.source.status.asr = TaskStatus(status=StatusEnum.FINISHED)
            record.target.shared.translation_analysis = scratchpad

            for code in target_lang_codes:
                branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
                if code in translations_by_code:
                    branch.artifacts.raw_translation = RawTranslationArtifact(
                        text=normalize_generated_text(translations_by_code[code], code),
                        author=author,
                    )
                    branch.status.raw_translation = TaskStatus(status=StatusEnum.FINISHED)
                else:
                    errors = list(parse_errors)
                    language_name = Config.lang_code2name.get(code, code)
                    missing_error = f"Missing translation output for target language: {language_name}"
                    if missing_error not in errors:
                        errors.append(missing_error)
                    branch.status.raw_translation = TaskStatus(
                        status=StatusEnum.FAILED,
                        errors=errors,
                    )

            failed_codes = [
                code for code in target_lang_codes
                if record.target.languages[code].status.raw_translation.status != StatusEnum.FINISHED
            ]
            if failed_codes:
                self._tqdm_bar.update("Translation-only", n_finished=0, n_failed=1)
            else:
                self._tqdm_bar.update("Translation-only", n_finished=1, n_failed=0)
            return record, visualization_translation_only(
                transcription.uid,
                scratchpad,
                final_result,
                asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                errors=[
                    error
                    for code in target_lang_codes
                    for error in record.target.languages[code].status.raw_translation.errors
                ] or None,
            )


