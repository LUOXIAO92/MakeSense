"""User-facing runner APIs for time pressure segmentation tasks."""

import asyncio
from pathlib import Path

from llm.llm_model import LLM
from pipeline.providers.time_pressure_segmentation_provider import TimePressureSegmentationProvider
from pipeline.schema import PipelineRecord, StatusEnum, TaskStatus
from pipeline.runners.utils import (
    TqdmBar,
    load_pipeline_records_by_uid,
    safe_shard_label,
    stage_output_path_from_input_cache,
    upsert_record,
    upsert_record_and_visualization,
    visualization_time_pressure_segmentation,
    visualized_path,
)


class TimePressureSegmentationRunner:
    """Public runner for source time pressure segmentation."""

    def __init__(
        self,
        llm: LLM,
        concurrency: int = 4,
        *,
        processor_max_retries: int,
        processor_name: str | None = None,
    ):
        self.llm = llm
        self.concurrency = concurrency
        self.processor_max_retries = processor_max_retries
        self.processor_name = processor_name
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
        segmentation = record.source.artifacts.time_pressure_segmentation
        return (
            segmentation is not None
            and bool(segmentation.sense_units.groups)
            and record.source.status.time_pressure_segmentation.status == StatusEnum.FINISHED
        )

    def _validate_prerequisite_record(self, prerequisite_record: PipelineRecord) -> list[str]:
        errors: list[str] = []
        transcript = prerequisite_record.source.artifacts.transcript
        alignment = prerequisite_record.source.artifacts.alignment
        if transcript is None or not transcript.text:
            errors.append("Missing source transcript dependency")
        if alignment is None or not alignment.tokens:
            errors.append("Missing source alignment dependency")
        return errors

    def _build_failed_record(
        self,
        prerequisite_record: PipelineRecord,
        stage_label: str,
        errors: list[str],
    ) -> PipelineRecord:
        record = prerequisite_record.model_copy(deep=True)
        record.source.status.time_pressure_segmentation = TaskStatus(
            status=StatusEnum.FAILED,
            errors=[f"{stage_label}: {error}" for error in errors],
        )
        return record

    def record_status(self, record: PipelineRecord) -> str:
        if self._is_finished_record(record):
            return "finished"
        if any(error.startswith("prerequisite_invalid:") for error in record.source.status.time_pressure_segmentation.errors):
            return "prerequisite_invalid"
        return "segmentation_failed"

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
        enable_thinking: bool = False,
        enable_visualization: bool = True,
    ) -> dict[str, int | str]:
        output_path = stage_output_path_from_input_cache(
            output_root,
            input_cache_base,
            input_cache_path,
            "time_pressure_segmentation",
        )
        shard_visualized_path = visualized_path(output_path, "time_pressure_segmentation")
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
            "segmented": 0,
            "segmentation_failed": 0,
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
                        existing_record=existing_output_by_uid.get(prerequisite_record.uid),
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        top_k=top_k,
                        enable_thinking=enable_thinking,
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
                visualized = visualization_time_pressure_segmentation(record)
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
                    summary["segmented"] += 1
                else:
                    summary[status] += 1
            schedule_next()

        return summary

    async def run_cache_records(
        self,
        prerequisite_records: list[PipelineRecord],
        existing_output_by_uid: dict[str, PipelineRecord] | None = None,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool = False,
    ) -> list[PipelineRecord]:
        existing_output_by_uid = existing_output_by_uid or {}
        return await asyncio.gather(
            *(
                self.run_cache_record(
                    prerequisite_record,
                    existing_record=existing_output_by_uid.get(prerequisite_record.uid),
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    enable_thinking=enable_thinking,
                )
                for prerequisite_record in prerequisite_records
            )
        )

    async def run_cache_record(
        self,
        prerequisite_record: PipelineRecord,
        existing_record: PipelineRecord | None = None,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool = False,
    ) -> PipelineRecord:
        if existing_record and self._is_finished_record(existing_record):
            return existing_record

        prerequisite_errors = self._validate_prerequisite_record(prerequisite_record)
        if prerequisite_errors:
            return self._build_failed_record(prerequisite_record, "prerequisite_invalid", prerequisite_errors)

        record = prerequisite_record.model_copy(deep=True)
        return await self.run_record(
            record,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            enable_thinking=enable_thinking,
        )

    async def run_record(
        self,
        record: PipelineRecord,
        max_tokens: int = 1024,
        temperature: float = 0.5,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool = False,
    ) -> PipelineRecord:
        async with self._semaphore:
            try:
                provider_kwargs = {
                    "llm": self.llm,
                    "system_prompt": "",
                    "user_prompt_template": "",
                    "max_retries": self.processor_max_retries,
                }
                if self.processor_name is not None:
                    provider_kwargs["name"] = self.processor_name
                provider = TimePressureSegmentationProvider(**provider_kwargs)
                record = await provider.provide(
                    record=record,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    enable_thinking=enable_thinking,
                )
                latest_error = record.source.status.time_pressure_segmentation.errors[-1] if record.source.status.time_pressure_segmentation.errors else None
                if latest_error:
                    self._tqdm_bar.update("Time pressure segmentation", n_finished=0, n_failed=1)
                    self._tqdm_bar.write_latest_error(latest_error, uid=record.uid, error_name="segmentation_failed")
                else:
                    self._tqdm_bar.update("Time pressure segmentation", n_finished=1, n_failed=0)
                return record
            except Exception as e:
                self._tqdm_bar.update("Time pressure segmentation", n_finished=0, n_failed=1)
                self._tqdm_bar.write_latest_error(e, uid=record.uid)
                raise
