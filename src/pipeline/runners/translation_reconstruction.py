"""User-facing runner APIs for translation reconstruction."""

import asyncio
import json
from pathlib import Path

from core.schema import MetaData
from llm.llm_model import LLM
from pipeline.prompts.utils import build_prompt_translation_reconstruction
from pipeline.providers.translation_reconstruction_provider import (
    TranslationReconstructionProvider,
)
from pipeline.validators.reconstruction_validator import ReconstructionValidator
from pipeline.schema import (
    PipelineRecord,
    StatusEnum,
    TaskStatus,
)
from pipeline.runners.utils import TqdmBar, safe_shard_label, visualization_translation_reconstruction, visualized_path
from pipeline.runners.utils import (
    condense_pipeline_record_shard,
    load_pipeline_records_by_uid,
    reconstruction_output_path_from_input_cache,
    upsert_record,
    append_visualization,
)
from configs.config import Config
def _resolve_language_code(language: str) -> str:
    if not isinstance(language, str) or not language.strip():
        raise ValueError(f"Invalid language value: {language!r}")

    text = language.strip()
    upper = text.upper()
    if upper in Config.language_codes:
        return upper

    lowered = text.lower()
    for name, code in Config.lang_name2code.items():
        if name.lower() == lowered:
            return code.upper()

    raise ValueError(f"Unsupported language value: {language}")


def _resolve_language_name(language: str) -> str:
    code = _resolve_language_code(language)
    return Config.lang_code2name.get(code, code)


class TranslationReconstructionRunner:
    """Public runner for multi-language translation reconstruction."""

    def __init__(
        self,
        llm: LLM,
        concurrency: int = 4,
        *,
        max_retries: int,
        provider_name: str | None = None,
        reconstruction_validator_llm: LLM | None = None,
        reconstruction_validator_window_size: int = 1,
    ):
        self.llm = llm
        self.reconstruction_validator_llm = reconstruction_validator_llm or llm
        if reconstruction_validator_window_size < 1:
            raise ValueError("reconstruction_validator_window_size must be >= 1 pure window")
        self.reconstruction_validator_window_size = reconstruction_validator_window_size
        self.concurrency = concurrency
        self.max_retries = max_retries
        self.provider_name = provider_name
        self._semaphore = asyncio.Semaphore(concurrency)
        self._file_lock = asyncio.Lock()
        self._tqdm_bar = TqdmBar()

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

    def _target_language_codes_from_record(self, record: PipelineRecord) -> list[str]:
        return sorted(record.target.languages.keys())

    def _is_finished_target_branch(self, record: PipelineRecord, code: str) -> bool:
        target = record.target.languages.get(code)
        if target is None or not target.artifacts.reconstruction.text:
            return False
        return target.status.reconstruction.status == StatusEnum.FINISHED

    def _pending_target_language_codes(self, record: PipelineRecord) -> list[str]:
        return [
            code
            for code in self._prerequisite_target_language_codes(record)
            if not self._is_finished_target_branch(record, code)
        ]

    def _prerequisite_target_language_codes(self, record: PipelineRecord) -> list[str]:
        return sorted(
            code
            for code, target in record.target.languages.items()
            if target.artifacts.raw_translation.text
        )

    def _is_finished_record(self, record: PipelineRecord) -> bool:
        target_codes = self._target_language_codes_from_record(record)
        if not target_codes:
            return False
        for code in target_codes:
            if not self._is_finished_target_branch(record, code):
                return False
        return True

    def _build_failed_record(
        self,
        prerequisite_record: PipelineRecord,
        stage_label: str,
        errors: list[str],
        *,
        target_language_codes: list[str] | None = None,
    ) -> PipelineRecord:
        record = prerequisite_record.model_copy(deep=True)
        target_codes = target_language_codes or self._prerequisite_target_language_codes(record)
        for code in target_codes:
            record.target.languages[code].status.reconstruction = TaskStatus(
                status=StatusEnum.FAILED,
                errors=[f"{stage_label}: {error}" for error in errors],
            )
        return record

    def _validate_prerequisite_record(self, prerequisite_record: PipelineRecord) -> list[str]:
        errors: list[str] = []
        transcript = prerequisite_record.source.artifacts.transcript
        if transcript is None or not transcript.text:
            errors.append("Missing source transcript dependency")
        target_codes = self._prerequisite_target_language_codes(prerequisite_record)
        if not target_codes:
            errors.append("Missing raw translation dependencies")
        return errors

    def _has_failed_prerequisite_status(self, prerequisite_record: PipelineRecord) -> bool:
        if prerequisite_record.source.status.asr.status == StatusEnum.FAILED:
            return True

        for branch in prerequisite_record.target.languages.values():
            task_status = branch.status.raw_translation
            if task_status.status == StatusEnum.FAILED:
                return True

        return False

    def _is_reconstruction_candidate(self, prerequisite_record: PipelineRecord) -> bool:
        if self._has_failed_prerequisite_status(prerequisite_record):
            return False
        return not self._validate_prerequisite_record(prerequisite_record)

    def filter_reconstruction_candidates(
        self,
        prerequisite_records: list[PipelineRecord],
    ) -> tuple[list[PipelineRecord], dict[str, int]]:
        candidates: list[PipelineRecord] = []
        excluded_prerequisite_failed = 0
        excluded_prerequisite_invalid = 0

        for record in prerequisite_records:
            if self._has_failed_prerequisite_status(record):
                excluded_prerequisite_failed += 1
                continue
            if self._validate_prerequisite_record(record):
                excluded_prerequisite_invalid += 1
                continue
            candidates.append(record)

        return candidates, {
            "excluded_prerequisite_failed": excluded_prerequisite_failed,
            "excluded_prerequisite_invalid": excluded_prerequisite_invalid,
        }

    def branch_status(self, record: PipelineRecord, code: str) -> str:
        branch = record.target.languages.get(code)
        if branch is None:
            return "pending"
        task_status = branch.status.reconstruction
        if task_status.status == StatusEnum.FINISHED:
            return "finished"
        if any(error.startswith("prerequisite_failed:") for error in task_status.errors):
            return "prerequisite_failed"
        if any(error.startswith("prerequisite_invalid:") for error in task_status.errors):
            return "prerequisite_invalid"
        if task_status.status == StatusEnum.RUNNING:
            return "running"
        return "reconstruction_failed"

    def record_status(self, record: PipelineRecord) -> str:
        reconstruction_statuses = [
            record.target.languages[code].status.reconstruction
            for code in self._prerequisite_target_language_codes(record)
            if code in record.target.languages
        ]
        if reconstruction_statuses and all(status.status == StatusEnum.FINISHED for status in reconstruction_statuses):
            return "finished"
        all_errors = [error for status in reconstruction_statuses for error in status.errors]
        if any(error.startswith("prerequisite_failed:") for error in all_errors):
            return "prerequisite_failed"
        if any(error.startswith("prerequisite_invalid:") for error in all_errors):
            return "prerequisite_invalid"
        return "reconstruction_failed"

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
        top_k: int = 40,
        enable_thinking: bool,
        enable_visualization: bool = False,
    ) -> dict[str, int | str]:
        output_path = reconstruction_output_path_from_input_cache(output_root, input_cache_base, input_cache_path)
        shard_visualized_path = visualized_path(output_path, "translation_reconstruction")
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        candidate_records, candidate_stats = self.filter_reconstruction_candidates(prerequisite_records)
        candidate_units: list[tuple[PipelineRecord, str]] = []
        for record in candidate_records:
            existing_record = existing_output_by_uid.get(record.uid)
            if existing_record and self._is_finished_record(existing_record):
                continue
            source_record = existing_record or record
            for code in self._pending_target_language_codes(source_record):
                candidate_units.append((record, code))

        summary: dict[str, int | str] = {
            "output_label": safe_shard_label(output_path),
            "candidate_total": len(candidate_units),
            "existing_finished": sum(
                1
                for record in candidate_records
                for code in self._prerequisite_target_language_codes(existing_output_by_uid.get(record.uid, record))
                if record.uid in existing_output_by_uid
                and self.branch_status(existing_output_by_uid[record.uid], code) == "finished"
            ),
            "pending": len(candidate_units),
            "resumed_finished": sum(
                1
                for uid, record in existing_output_by_uid.items()
                if uid in {candidate.uid for candidate in candidate_records}
                and self.record_status(record) == "finished"
            ),
            "reconstructed": 0,
            "reconstruction_failed": 0,
            "excluded_prerequisite_failed": candidate_stats["excluded_prerequisite_failed"],
            "excluded_prerequisite_invalid": candidate_stats["excluded_prerequisite_invalid"],
        }
        all_stage_units_finished = summary["pending"] == 0

        pending_iter = iter(candidate_units)
        active_tasks: dict[asyncio.Task, tuple[PipelineRecord, str]] = {}

        def schedule_next() -> None:
            while len(active_tasks) < max_current_tasks:
                unit = next(pending_iter, None)
                if unit is None:
                    break
                prerequisite_record, target_language_code = unit
                task = asyncio.create_task(
                    self.run_cache_record(
                        prerequisite_record,
                        existing_record=existing_output_by_uid.get(prerequisite_record.uid),
                        target_language_code=target_language_code,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        top_k=top_k,
                        enable_thinking=enable_thinking,
                    )
                )
                active_tasks[task] = unit

        schedule_next()
        while active_tasks:
            done, _ = await asyncio.wait(active_tasks.keys(), return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                prerequisite_record, target_language_code = active_tasks.pop(task)
                record = await task
                existing_output_by_uid[prerequisite_record.uid] = record
                status = self.branch_status(record, target_language_code)
                if status == "finished":
                    debug_payload = record.get_debug_translation_reconstruction(target_language_code)
                    raw_translation = {
                        _resolve_language_name(target_language_code): record.target.languages[target_language_code].artifacts.raw_translation.text
                        if record.target.languages.get(target_language_code) and record.target.languages[target_language_code].artifacts.raw_translation.text else ""
                    }
                    reconstructed_translation = {
                        _resolve_language_name(target_language_code): debug_payload.get("result", "")
                    }
                    visualized = visualization_translation_reconstruction(
                        uid=record.uid,
                        scratchpad=debug_payload.get("scratchpad", ""),
                        asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                        asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                        raw_translation=raw_translation,
                        reconstructed_translation=reconstructed_translation,
                        shared_translation_analysis=record.target.shared.translation_analysis,
                        validator_scratchpad=debug_payload.get("validator_scratchpad", ""),
                        validator_result=debug_payload.get("validator_result", ""),
                        validator_order_risk=debug_payload.get("validator_order_risk", ""),
                        validator_source_tokens=debug_payload.get("validator_source_tokens", ""),
                        validator_source_windows=debug_payload.get("validator_source_windows", ""),
                        validator_feedback=debug_payload.get("validator_feedback", ""),
                    )
                else:
                    errors = list(record.target.languages[target_language_code].status.reconstruction.errors)
                    debug_payload = record.get_debug_translation_reconstruction(target_language_code)
                    raw_translation = {
                        _resolve_language_name(target_language_code): record.target.languages[target_language_code].artifacts.raw_translation.text
                        if record.target.languages.get(target_language_code) and record.target.languages[target_language_code].artifacts.raw_translation.text else ""
                    }
                    reconstructed_translation = {
                        _resolve_language_name(target_language_code): debug_payload.get("result", "")
                    }
                    visualized = visualization_translation_reconstruction(
                        uid=record.uid,
                        scratchpad=debug_payload.get("scratchpad", ""),
                        asr_language_name=record.source.artifacts.transcript.language_name if record.source.artifacts.transcript else "",
                        asr_text=record.source.artifacts.transcript.text if record.source.artifacts.transcript else "",
                        raw_translation=raw_translation,
                        reconstructed_translation=reconstructed_translation,
                        shared_translation_analysis=record.target.shared.translation_analysis,
                        validator_result=debug_payload.get("validator_result", ""),
                        validator_order_risk=debug_payload.get("validator_order_risk", ""),
                        validator_source_tokens=debug_payload.get("validator_source_tokens", ""),
                        validator_source_windows=debug_payload.get("validator_source_windows", ""),
                        validator_feedback=debug_payload.get("validator_feedback", ""),
                        errors=errors,
                    )
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
                if status == "finished":
                    self._tqdm_bar.update("Translation reconstruction", n_finished=1, n_failed=0)
                    summary["reconstructed"] += 1
                else:
                    self._tqdm_bar.update("Translation reconstruction", n_finished=0, n_failed=1)
                    self._tqdm_bar.write_latest_error(
                        errors[-1] if errors else None,
                        uid=record.uid,
                        error_name=status,
                    )
                    summary[status] += 1
            schedule_next()

        if summary["pending"] == summary["reconstructed"] + summary["reconstruction_failed"]:
            all_stage_units_finished = True

        if all_stage_units_finished:
            condensation_stats = condense_pipeline_record_shard(output_path=output_path)
            summary["condensed_rows_before"] = condensation_stats["rows_before"]
            summary["condensed_rows_after"] = condensation_stats["rows_after"]

        return summary

    async def run_cache_record(
        self,
        prerequisite_record: PipelineRecord,
        existing_record: PipelineRecord | None = None,
        target_language_code: str | None = None,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool,
    ) -> PipelineRecord:
        if existing_record and target_language_code and self._is_finished_target_branch(existing_record, target_language_code):
            return existing_record

        if self._has_failed_prerequisite_status(prerequisite_record):
            return self._build_failed_record(
                prerequisite_record,
                "prerequisite_failed",
                ["Upstream prerequisite status is failed"],
                target_language_codes=[target_language_code] if target_language_code else None,
            )

        prerequisite_errors = self._validate_prerequisite_record(prerequisite_record)
        if prerequisite_errors:
            return self._build_failed_record(
                prerequisite_record,
                "prerequisite_invalid",
                prerequisite_errors,
                target_language_codes=[target_language_code] if target_language_code else None,
            )

        record = (existing_record or prerequisite_record).model_copy(deep=True)

        record = await self.run_record(
            record,
            target_language_codes=[target_language_code] if target_language_code else None,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            enable_thinking=enable_thinking,
        )
        return record

    async def run_cache_records(
        self,
        prerequisite_records: list[PipelineRecord],
        existing_output_by_uid: dict[str, PipelineRecord] | None = None,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool,
    ) -> list[PipelineRecord]:
        existing_output_by_uid = existing_output_by_uid or {}
        return await asyncio.gather(
            *(
                self.run_cache_record(
                    prerequisite_record,
                    existing_record=existing_output_by_uid.get(prerequisite_record.uid),
                    target_language_code=None,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    enable_thinking=enable_thinking,
                )
                for prerequisite_record in prerequisite_records
            )
        )

    async def run_record(
        self,
        record: PipelineRecord,
        target_language_codes: list[str] | None = None,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool,
    ) -> PipelineRecord:
        async with self._semaphore:
            system_prompt, user_prompt, target_language_codes = build_prompt_translation_reconstruction(
                record=record,
                target_language_codes=target_language_codes,
            )
            provider_kwargs = {
                "llm": self.llm,
                "system_prompt": system_prompt,
                "user_prompt_template": user_prompt,
                "max_retries": self.max_retries,
                "reconstruction_validator": ReconstructionValidator(llm=self.reconstruction_validator_llm),
                "source_windows_per_validator_window": self.reconstruction_validator_window_size,
            }
            if self.provider_name is not None:
                provider_kwargs["name"] = self.provider_name
            provider = TranslationReconstructionProvider(**provider_kwargs)
            return await provider.provide(
                record=record,
                target_language_codes=target_language_codes,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                enable_thinking=enable_thinking,
            )