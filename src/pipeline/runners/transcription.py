"""User-facing runner APIs for transcription tasks."""

import asyncio
import json
from pathlib import Path

from core.schema import MetaData
from pipeline.providers.asr_provider import ASRProvider
from pipeline.schema import PipelineRecord, StatusEnum, TaskStatus
from pipeline.runners.utils import (
    TqdmBar,
    load_pipeline_records_by_uid,
    safe_shard_label,
    stage_output_path_from_input_cache,
    upsert_record,
    upsert_record_and_visualization,
    visualized_path,
)


class TranscriptionRunner:
    """Public runner for source transcription generation."""

    def __init__(
        self,
        concurrency: int = 4,
        *,
        provider_max_retries: int,
        provider_name: str | None = None,
    ):
        self.concurrency = concurrency
        self.provider_max_retries = provider_max_retries
        self.provider_name = provider_name
        self._semaphore = asyncio.Semaphore(concurrency)
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

    def _is_finished_record(self, record: PipelineRecord) -> bool:
        transcript = record.source.artifacts.transcript
        return (
            transcript is not None
            and bool(transcript.text)
            and record.source.status.asr.status == StatusEnum.FINISHED
        )

    def record_status(self, record: PipelineRecord) -> str:
        if self._is_finished_record(record):
            return "finished"
        if any(error.startswith("prerequisite_invalid:") for error in record.source.status.asr.errors):
            return "prerequisite_invalid"
        return "asr_failed"

    async def run_cache_shard(
        self,
        *,
        input_cache_base: Path,
        input_cache_path: Path,
        prerequisite_records: list[PipelineRecord],
        output_root: Path,
        dataset_root: Path,
        asr_model,
        max_current_tasks: int,
        enable_visualization: bool = True,
    ) -> dict[str, int | str]:
        output_path = stage_output_path_from_input_cache(
            output_root,
            input_cache_base,
            input_cache_path,
            "asr",
        )
        shard_visualized_path = visualized_path(output_path, "transcription")
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
            "transcribed": 0,
            "asr_failed": 0,
            "prerequisite_invalid": 0,
        }

        pending_iter = iter(pending_records)
        active_tasks: dict[asyncio.Task, PipelineRecord] = {}
        file_lock = asyncio.Lock()

        def schedule_next() -> None:
            while len(active_tasks) < max_current_tasks:
                prerequisite_record = next(pending_iter, None)
                if prerequisite_record is None:
                    break
                task = asyncio.create_task(
                    self.run_cache_record(
                        prerequisite_record,
                        dataset_root=dataset_root,
                        asr_model=asr_model,
                        existing_record=existing_output_by_uid.get(prerequisite_record.uid),
                    )
                )
                active_tasks[task] = prerequisite_record

        schedule_next()
        while active_tasks:
            done, _ = await asyncio.wait(active_tasks.keys(), return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                prerequisite_record = active_tasks.pop(task)
                record = await task
                existing_output_by_uid[prerequisite_record.uid] = record
                status = self.record_status(record)
                if status == "finished":
                    transcript = record.source.artifacts.transcript
                    visualized = "\n".join([
                        f"=== {record.uid} ===",
                        "asr:",
                        transcript.text if transcript else "",
                        "",
                        "---",
                        "",
                    ])
                else:
                    visualized = "\n".join([
                        f"=== {record.uid} ===",
                        f"status: {status}",
                        "errors:",
                        json.dumps(record.source.status.asr.errors, ensure_ascii=False, indent=2),
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
                    summary["transcribed"] += 1
                else:
                    summary[status] += 1
            schedule_next()

        return summary

    async def run_cache_record(
        self,
        prerequisite_record: PipelineRecord,
        *,
        dataset_root: Path,
        asr_model,
        existing_record: PipelineRecord | None = None,
    ) -> PipelineRecord:
        if existing_record and self._is_finished_record(existing_record):
            return existing_record

        if self._is_finished_record(prerequisite_record):
            return prerequisite_record

        audio = str(dataset_root / "audio" / prerequisite_record.metadata.language / prerequisite_record.metadata.file_name)
        record = prerequisite_record.model_copy(deep=True)
        provided = await self.run_record(record.metadata, audio, asr_model)
        record.source.artifacts.transcript = provided.source.artifacts.transcript
        record.source.status.asr = provided.source.status.asr
        return record

    async def run_record(
        self,
        meta: MetaData,
        audio: str | bytes,
        asr_model,
    ) -> PipelineRecord:
        async with self._semaphore:
            try:
                provider_kwargs = {
                    "asr_model": asr_model,
                    "max_retries": self.provider_max_retries,
                }
                if self.provider_name is not None:
                    provider_kwargs["name"] = self.provider_name
                provider = ASRProvider(**provider_kwargs)
                record = PipelineRecord(uid=meta.uid, metadata=meta)
                record = await provider.provide(
                    record=record,
                    audio=audio,
                    language_code=meta.language,
                )
                latest_error = record.source.status.asr.errors[-1] if record.source.status.asr.errors else None
                if latest_error:
                    self._tqdm_bar.update("Transcription", n_finished=0, n_failed=1)
                    self._tqdm_bar.write_latest_error(latest_error, uid=record.uid, error_name="asr_failed")
                else:
                    self._tqdm_bar.update("Transcription", n_finished=1, n_failed=0)
                return record
            except Exception as e:
                self._tqdm_bar.update("Transcription", n_finished=0, n_failed=1)
                self._tqdm_bar.write_latest_error(e, uid=meta.uid)
                raise
