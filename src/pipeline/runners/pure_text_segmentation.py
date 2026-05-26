"""User-facing runner APIs for pure text segmentation."""

import asyncio
import json
from pathlib import Path

from llm.llm_model import LLM
from pipeline.prompts.pure_text_segmentation import (
    SYSTEM_INSTRUCTION_PURE_TEXT_SEGMENTATION,
    USER_PROMPT_PURE_TEXT_SEGMENTATION,
)
from pipeline.providers.pure_text_segmentation_provider import PureTextSegmentationProvider
from pipeline.runners.utils import (
    TqdmBar,
    append_visualization,
    condense_pipeline_record_shard,
    load_pipeline_records_by_uid,
    safe_shard_label,
    stage_output_path_from_input_cache,
    upsert_record,
    visualization_pure_text_segmentation,
    visualized_path,
)
from pipeline.schema import PipelineRecord, StatusEnum, TaskStatus


class PureTextSegmentationRunner:
    """Public runner for per-language pure text segmentation."""

    def __init__(
        self,
        llm: LLM,
        concurrency: int = 4,
        *,
        max_retries: int,
        provider_name: str | None = None,
    ):
        self.llm = llm
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

    def _prerequisite_target_language_codes(self, record: PipelineRecord) -> list[str]:
        return sorted(
            code
            for code, target in record.target.languages.items()
            if target.artifacts.reconstruction.text
        )

    def _has_meaningful_segmentation_groups(self, record: PipelineRecord, code: str) -> bool:
        target = record.target.languages.get(code)
        if target is None:
            return False
        groups = target.artifacts.pure_text_segmentation.sense_units.groups
        return bool(groups) and any(bool(group) for group in groups)

    def _is_finished_target_branch(self, record: PipelineRecord, code: str) -> bool:
        target = record.target.languages.get(code)
        if target is None or not self._has_meaningful_segmentation_groups(record, code):
            return False
        return target.status.pure_text_segmentation.status == StatusEnum.FINISHED

    def _pending_target_language_codes(self, record: PipelineRecord) -> list[str]:
        return [
            code
            for code in self._prerequisite_target_language_codes(record)
            if not self._is_finished_target_branch(record, code)
        ]

    def _is_finished_record(self, record: PipelineRecord) -> bool:
        target_codes = self._prerequisite_target_language_codes(record)
        if not target_codes:
            return False
        return all(self._is_finished_target_branch(record, code) for code in target_codes)

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
            record.target.languages[code].status.pure_text_segmentation = TaskStatus(
                status=StatusEnum.FAILED,
                errors=[f"{stage_label}: {error}" for error in errors],
            )
        return record

    def _validate_prerequisite_record(self, prerequisite_record: PipelineRecord) -> list[str]:
        errors: list[str] = []
        if not self._prerequisite_target_language_codes(prerequisite_record):
            errors.append("Missing reconstruction dependencies")
        return errors

    def _has_failed_prerequisite_status(self, prerequisite_record: PipelineRecord) -> bool:
        for branch in prerequisite_record.target.languages.values():
            task_status = branch.status.raw_translation
            if task_status.status == StatusEnum.FAILED:
                return True
        return False

    def filter_segmentation_candidates(
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
        task_status = branch.status.pure_text_segmentation
        if task_status.status == StatusEnum.FINISHED:
            return "finished"
        if any(error.startswith("prerequisite_failed:") for error in task_status.errors):
            return "prerequisite_failed"
        if any(error.startswith("prerequisite_invalid:") for error in task_status.errors):
            return "prerequisite_invalid"
        if task_status.status == StatusEnum.RUNNING:
            return "running"
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
        top_p: float,
        top_k: int,
        enable_thinking: bool,
        enable_visualization: bool = False,
    ) -> dict[str, int | str]:
        output_path = stage_output_path_from_input_cache(output_root, input_cache_base, input_cache_path, "pure_text_segmentation")
        shard_visualized_path = visualized_path(output_path, "pure_text_segmentation")
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        candidate_records, candidate_stats = self.filter_segmentation_candidates(prerequisite_records)
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
            "existing_finished": sum(
                1
                for record in candidate_records
                for code in self._prerequisite_target_language_codes(existing_output_by_uid.get(record.uid, record))
                if record.uid in existing_output_by_uid
                and self.branch_status(existing_output_by_uid[record.uid], code) == "finished"
            ),
            "pending": len(candidate_units),
            "segmented": 0,
            "segmentation_failed": 0,
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
                    visualized = visualization_pure_text_segmentation(record, target_language_code)
                else:
                    errors = list(record.target.languages[target_language_code].status.pure_text_segmentation.errors)
                    debug_payload = record.get_debug_pure_text_segmentation(target_language_code)
                    visualized = "\n".join([
                        f"=== {record.uid} ===",
                        f"target_language: {target_language_code}",
                        f"status: {status}",
                        "scratchpad:",
                        debug_payload.get("scratchpad", ""),
                        "errors:",
                        json.dumps(errors, ensure_ascii=False, indent=2),
                        "",
                        "---",
                        "",
                    ])
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
                    self._tqdm_bar.update("Pure text segmentation", n_finished=1, n_failed=0)
                    summary["segmented"] += 1
                else:
                    self._tqdm_bar.update("Pure text segmentation", n_finished=0, n_failed=1)
                    self._tqdm_bar.write_latest_error(
                        errors[-1] if errors else None,
                        uid=record.uid,
                        error_name=status,
                    )
                    summary["segmentation_failed"] += 1
            schedule_next()

        if summary["pending"] == summary["segmented"] + summary["segmentation_failed"]:
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
        top_p: float,
        top_k: int,
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
        return await self.run_record(
            record,
            target_language_codes=[target_language_code] if target_language_code else None,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            enable_thinking=enable_thinking,
        )

    async def run_record(
        self,
        record: PipelineRecord,
        target_language_codes: list[str] | None = None,
        *,
        max_tokens: int,
        temperature: float,
        top_p: float,
        top_k: int,
        enable_thinking: bool,
    ) -> PipelineRecord:
        async with self._semaphore:
            provider_kwargs = {
                "llm": self.llm,
                "system_prompt": SYSTEM_INSTRUCTION_PURE_TEXT_SEGMENTATION,
                "user_prompt_template": USER_PROMPT_PURE_TEXT_SEGMENTATION,
                "max_retries": self.max_retries,
            }
            if self.provider_name is not None:
                provider_kwargs["name"] = self.provider_name
            provider = PureTextSegmentationProvider(**provider_kwargs)
            return await provider.provide(
                record=record,
                target_language_codes=target_language_codes,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                enable_thinking=enable_thinking,
            )