"""User-facing runner APIs for forced-alignment tasks."""

import asyncio
import json
from pathlib import Path
from typing import Literal

from core.schema import MetaData
from core.utils import apply_mapping_groups
from pipeline.providers.qwen3_forced_alignment_provider import Qwen3ForcedAlignment
from pipeline.providers.whisperx_forced_alignment_provider import WhisperXForcedAlignment
from pipeline.schema import (
    AlignmentArtifact,
    PipelineRecord,
    StatusEnum,
    TaskStatus,
)
from pipeline.runners.utils import (
    TqdmBar,
    load_pipeline_records_by_uid,
    safe_shard_label,
    stage_output_path_from_input_cache,
    upsert_record,
    upsert_record_and_visualization,
    visualized_path,
)


class ForcedAlignmentRunner:
    """Public runner for source forced alignment."""

    @staticmethod
    def _validate_raw_alignment_token_timing(
        tokens,
        *,
        repair_overlap: bool = False,
        eps: float = 1e-8,
    ) -> None:
        for idx in range(len(tokens) - 1):
            left = tokens[idx]
            right = tokens[idx + 1]
            if left.end <= right.start + eps:
                continue
            if left.end >= right.end:
                raise ValueError(
                    "Forced-alignment validation error: raw token timing is causally invalid/non-repairable: "
                    f"token[{idx}]={left.word!r} start={left.start:.6f} end={left.end:.6f}, "
                    f"token[{idx + 1}]={right.word!r} start={right.start:.6f} end={right.end:.6f}"
                )
            if not repair_overlap:
                raise ValueError(
                    "Forced-alignment validation error: raw token timing is not monotonic/non-overlapping: "
                    f"token[{idx}]={left.word!r} start={left.start:.6f} end={left.end:.6f}, "
                    f"token[{idx + 1}]={right.word!r} start={right.start:.6f} end={right.end:.6f}; "
                    "repair_raw_token_timing_overlap is disabled"
                )
            right.start = left.end

    def __init__(self, concurrency: int = 4, *, repair_raw_token_timing_overlap: bool = False):
        self.concurrency = concurrency
        self.repair_raw_token_timing_overlap = repair_raw_token_timing_overlap
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

    def update_progress(self, *, n_finished: int = 0, n_failed: int = 0) -> None:
        self._tqdm_bar.update(
            "Forced alignment",
            n_finished=n_finished,
            n_failed=n_failed,
        )

    def _is_finished_record(self, record: PipelineRecord) -> bool:
        alignment = record.source.artifacts.alignment
        return (
            alignment is not None
            and bool(alignment.tokens)
            and record.source.status.forced_alignment.status == StatusEnum.FINISHED
        )

    def _validate_prerequisite_record(self, prerequisite_record: PipelineRecord) -> list[str]:
        errors: list[str] = []
        transcript = prerequisite_record.source.artifacts.transcript
        if transcript is None or not transcript.text:
            errors.append("Missing source transcript dependency")
        return errors

    def _build_failed_record(
        self,
        prerequisite_record: PipelineRecord,
        stage_label: str,
        errors: list[str],
    ) -> PipelineRecord:
        record = prerequisite_record.model_copy(deep=True)
        record.source.status.forced_alignment = TaskStatus(
            status=StatusEnum.FAILED,
            errors=[f"{stage_label}: {error}" for error in errors],
        )
        return record

    def record_status(self, record: PipelineRecord) -> str:
        if self._is_finished_record(record):
            return "finished"
        if any(error.startswith("prerequisite_invalid:") for error in record.source.status.forced_alignment.errors):
            return "prerequisite_invalid"
        return "alignment_failed"

    def _audio_path(self, dataset_root: Path, record: PipelineRecord) -> str:
        return str(dataset_root / "audio" / record.metadata.language / record.metadata.file_name)

    def _provider_kind(
        self,
        provider: Qwen3ForcedAlignment | WhisperXForcedAlignment,
    ) -> Literal["qwen3", "whisperx"]:
        if isinstance(provider, Qwen3ForcedAlignment):
            return "qwen3"
        if isinstance(provider, WhisperXForcedAlignment):
            return "whisperx"
        raise TypeError(f"Unsupported forced-alignment provider: {provider.__class__.__name__}")

    async def run_cache_shard(
        self,
        *,
        input_cache_base: Path,
        input_cache_path: Path,
        prerequisite_records: list[PipelineRecord],
        output_root: Path,
        dataset_root: Path,
        provider: Qwen3ForcedAlignment | WhisperXForcedAlignment,
        max_current_tasks: int,
        enable_visualization: bool = True,
    ) -> dict[str, int | str]:
        output_path = stage_output_path_from_input_cache(
            output_root,
            input_cache_base,
            input_cache_path,
            "forced_alignment",
        )
        shard_visualized_path = visualized_path(output_path, "forced_alignment")
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        pending_records = [
            record
            for record in prerequisite_records
            if record.uid not in existing_output_by_uid
            or self.record_status(existing_output_by_uid[record.uid]) != "finished"
        ]
        summary: dict[str, int | str] = {
            "output_label": safe_shard_label(output_path),
            "existing_finished": len(prerequisite_records) - len(pending_records),
            "pending": len(pending_records),
            "aligned": 0,
            "alignment_failed": 0,
            "prerequisite_invalid": 0,
        }

        batch_size = max(1, getattr(provider, "max_inference_batch_size", 1) or 1)
        file_lock = asyncio.Lock()

        execution_batch_size = batch_size if self._provider_kind(provider) == "qwen3" else max(1, max_current_tasks)
        for batch_start in range(0, len(pending_records), execution_batch_size):
            batch_records = pending_records[batch_start: batch_start + execution_batch_size]
            result_records = await self.run_cache_records(
                batch_records,
                dataset_root=dataset_root,
                provider=provider,
                existing_output_by_uid=existing_output_by_uid,
            )
            for prerequisite_record, record in zip(batch_records, result_records):
                existing_output_by_uid[prerequisite_record.uid] = record
                status = self.record_status(record)
                if status == "finished":
                    transcript = record.source.artifacts.transcript
                    alignment = record.source.artifacts.alignment
                    transcription_text = transcript.text if transcript else ""
                    aligned_words = []
                    if alignment:
                        aligned_words = apply_mapping_groups(
                            alignment.tokens,
                            alignment.words,
                            language=record.metadata.language,
                        )
                    visualized = "\n".join([
                        f"=== {record.uid} ===",
                        f"transcription: {transcription_text}",
                        "",
                        *[
                            f"word={word.word!r} start={word.start} end={word.end}"
                            for word in aligned_words
                        ],
                        "",
                        "---",
                        "",
                    ])
                else:
                    visualized = "\n".join([
                        f"=== {record.uid} ===",
                        f"status: {status}",
                        "errors:",
                        json.dumps(record.source.status.forced_alignment.errors, ensure_ascii=False, indent=2),
                        "",
                        "---",
                        "",
                    ])
                if enable_visualization:
                    await upsert_record_and_visualization(
                        output_path=output_path,
                        shard_visualized_path=shard_visualized_path,
                        record=record,
                        visualized=visualized,
                        file_lock=file_lock,
                    )
                else:
                    await upsert_record(
                        output_path=output_path,
                        record=record,
                        file_lock=file_lock,
                    )
                if status == "finished":
                    self.update_progress(n_finished=1, n_failed=0)
                    summary["aligned"] += 1
                else:
                    self.update_progress(n_finished=0, n_failed=1)
                    errors = record.source.status.forced_alignment.errors
                    self._tqdm_bar.write_latest_error(errors[-1] if errors else None, uid=record.uid, error_name=status)
                    summary[status] += 1
        return summary

    async def run_cache_shard_qwen3(
        self,
        *,
        input_cache_base: Path,
        input_cache_path: Path,
        prerequisite_records: list[PipelineRecord],
        output_root: Path,
        dataset_root: Path,
        provider: Qwen3ForcedAlignment,
        max_current_tasks: int,
        enable_visualization: bool = True,
    ) -> dict[str, int | str]:
        return await self.run_cache_shard(
            input_cache_base=input_cache_base,
            input_cache_path=input_cache_path,
            prerequisite_records=prerequisite_records,
            output_root=output_root,
            dataset_root=dataset_root,
            provider=provider,
            max_current_tasks=max_current_tasks,
            enable_visualization=enable_visualization,
        )

    async def run_cache_shard_whisperx(
        self,
        *,
        input_cache_base: Path,
        input_cache_path: Path,
        prerequisite_records: list[PipelineRecord],
        output_root: Path,
        dataset_root: Path,
        provider: WhisperXForcedAlignment,
        max_current_tasks: int,
        enable_visualization: bool = True,
    ) -> dict[str, int | str]:
        return await self.run_cache_shard(
            input_cache_base=input_cache_base,
            input_cache_path=input_cache_path,
            prerequisite_records=prerequisite_records,
            output_root=output_root,
            dataset_root=dataset_root,
            provider=provider,
            max_current_tasks=max_current_tasks,
            enable_visualization=enable_visualization,
        )

    async def run_cache_records(
        self,
        prerequisite_records: list[PipelineRecord],
        *,
        dataset_root: Path,
        provider: Qwen3ForcedAlignment | WhisperXForcedAlignment,
        existing_output_by_uid: dict[str, PipelineRecord] | None = None,
    ) -> list[PipelineRecord]:
        existing_output_by_uid = existing_output_by_uid or {}
        ready_results: list[PipelineRecord | None] = [None] * len(prerequisite_records)
        batch_records: list[PipelineRecord] = []
        batch_indices: list[int] = []
        audio_list: list[str] = []
        text_list: list[str] = []

        for idx, prerequisite_record in enumerate(prerequisite_records):
            existing_record = existing_output_by_uid.get(prerequisite_record.uid)
            if existing_record and self._is_finished_record(existing_record):
                ready_results[idx] = existing_record
                continue

            prerequisite_errors = self._validate_prerequisite_record(prerequisite_record)
            if prerequisite_errors:
                ready_results[idx] = self._build_failed_record(prerequisite_record, "prerequisite_invalid", prerequisite_errors)
                continue

            batch_indices.append(idx)
            batch_records.append(prerequisite_record.model_copy(deep=True))
            audio_list.append(self._audio_path(dataset_root, prerequisite_record))
            text_list.append(prerequisite_record.source.artifacts.transcript.text)

        if batch_records:
            aligned_records = await self._run_alignment_batch(
                records=batch_records,
                audio_list=audio_list,
                text_list=text_list,
                provider=provider,
                languages=[record.metadata.language for record in batch_records],
            )
            for idx, record in zip(batch_indices, aligned_records):
                ready_results[idx] = record

        return [record for record in ready_results if record is not None]

    async def run_cache_record(
        self,
        prerequisite_record: PipelineRecord,
        *,
        dataset_root: Path,
        provider: Qwen3ForcedAlignment | WhisperXForcedAlignment,
        existing_record: PipelineRecord | None = None,
    ) -> PipelineRecord:
        records = await self.run_cache_records(
            [prerequisite_record],
            dataset_root=dataset_root,
            provider=provider,
            existing_output_by_uid={prerequisite_record.uid: existing_record} if existing_record else None,
        )
        return records[0]

    async def run_record(
        self,
        record: PipelineRecord,
        *,
        audio: str | Path,
        text: str,
        provider: Qwen3ForcedAlignment | WhisperXForcedAlignment,
    ) -> PipelineRecord:
        try:
            record = await self._run_alignment(
                record=record,
                audio=audio,
                text=text,
                provider=provider,
                language=record.metadata.language,
            )
            latest_error = record.source.status.forced_alignment.errors[-1] if record.source.status.forced_alignment.errors else None
            if latest_error:
                self._tqdm_bar.update("Forced alignment", n_finished=0, n_failed=1)
                self._tqdm_bar.write_latest_error(latest_error, uid=record.uid, error_name="alignment_failed")
            else:
                self._tqdm_bar.update("Forced alignment", n_finished=1, n_failed=0)
            return record
        except Exception as e:
            self._tqdm_bar.update("Forced alignment", n_finished=0, n_failed=1)
            self._tqdm_bar.write_latest_error(e, uid=record.uid)
            raise

    async def run_qwen3_record(
        self,
        meta: MetaData,
        audio: str | Path,
        text: str,
        provider: Qwen3ForcedAlignment,
    ) -> PipelineRecord:
        record = PipelineRecord(uid=meta.uid, metadata=meta)
        return await self.run_record(record, audio=audio, text=text, provider=provider)

    async def run_whisperx_record(
        self,
        meta: MetaData,
        audio: str | Path,
        text: str,
        provider: WhisperXForcedAlignment,
    ) -> PipelineRecord:
        record = PipelineRecord(uid=meta.uid, metadata=meta)
        return await self.run_record(record, audio=audio, text=text, provider=provider)

    async def _run_alignment(
        self,
        record: PipelineRecord,
        audio: str | Path,
        text: str,
        provider: Qwen3ForcedAlignment | WhisperXForcedAlignment,
        language: str,
    ) -> PipelineRecord:
        return (
            await self._run_alignment_batch(
                records=[record],
                audio_list=[str(audio)],
                text_list=[text],
                provider=provider,
                languages=[language],
            )
        )[0]

    async def _run_alignment_batch(
        self,
        *,
        records: list[PipelineRecord],
        audio_list: list[str],
        text_list: list[str],
        provider: Qwen3ForcedAlignment | WhisperXForcedAlignment,
        languages: list[str],
    ) -> list[PipelineRecord]:
        for record in records:
            record.source.status.forced_alignment.status = StatusEnum.RUNNING
            record.source.status.forced_alignment.errors.clear()

        unique_languages = set(languages)
        if len(unique_languages) != 1:
            raise ValueError(
                "ForcedAlignmentRunner batch received multiple languages for one "
                f"forced-alignment provider: {sorted(unique_languages)}"
            )
        batch_language = languages[0]

        provider_kind = self._provider_kind(provider)
        if provider_kind == "qwen3":
            maybe_tokens_words = provider.align(audio=audio_list, text=text_list, language=batch_language)
            if hasattr(maybe_tokens_words, "__await__"):
                tokens_list, words_list = await maybe_tokens_words
            else:
                tokens_list, words_list = maybe_tokens_words
        else:
            tokens_list = []
            words_list = []
            for audio, text in zip(audio_list, text_list):
                maybe_tokens_words = provider.align(audio=audio, text=text)
                if hasattr(maybe_tokens_words, "__await__"):
                    tokens, words = await maybe_tokens_words
                else:
                    tokens, words = maybe_tokens_words
                tokens_list.append(tokens)
                words_list.append(words)

        for record, tokens, words in zip(records, tokens_list, words_list):
            try:
                self._validate_raw_alignment_token_timing(
                    tokens,
                    repair_overlap=self.repair_raw_token_timing_overlap,
                )
            except ValueError as exc:
                record.source.status.forced_alignment.status = StatusEnum.FAILED
                record.source.status.forced_alignment.errors = [str(exc)]
                continue

            record.source.artifacts.alignment = AlignmentArtifact(
                tokens=tokens,
                words=words,
                author=provider.model_name,
            )
            record.source.status.forced_alignment.status = StatusEnum.FINISHED

        return records
