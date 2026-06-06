"""Utility helpers for runner-adjacent dataset scripts."""

import json
import os
import re
import tempfile
from collections import OrderedDict
from pathlib import Path
from typing import Any
from typing import Optional

from tqdm import tqdm

from core.build_conversation import build_asr_blocks, build_translation_blocks
from core.schema import MetaData, Transcription, Translation
from core.utils import apply_mapping_groups, build_transcription_chunks, group_tokens_by_sense_units, process_words, render_transcription_chunk_word_indices, tokenize
from pipeline.schema import PipelineRecord
from pipeline.schema import StatusEnum
from pipeline.schema import TaskStatus
from configs.config import Config


UPSTREAM_LLM_ERROR_MARKERS = (
    "OpenAI-compatible provider",
    "system-level provider/API boundary error",
    "LLMResponseError",
    "APIConnectionError",
    "APITimeoutError",
    "APIStatusError",
    "RateLimitError",
    "InternalServerError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "UnprocessableEntityError",
    "Connection error",
    "ConnectionError",
    "timeout",
    "timed out",
    "rate limit",
    "429",
    "500",
    "502",
    "503",
    "504",
)


VALIDATION_ERROR_TYPE_MARKERS = (
    ("JSON Format Error", "JSONFormatError"),
    ("Output Format Error", "OutputFormatError"),
    ("Contract Error", "ContractError"),
    ("semantic_validator_failed", "SemanticValidatorFailed"),
    ("validator_contract_error", "ValidatorContractError"),
    ("ORDER_RISK", "OrderRisk"),
    ("Sense unit segmentation validation failed", "ASRChunkingValidationError"),
    ("PureTextSegmentationValidationError", "PureTextSegmentationValidationError"),
    ("TargetCentricMappingValidationError", "TargetCentricMappingValidationError"),
    ("TranslationReconstructionValidationError", "TranslationReconstructionValidationError"),
    ("OmniTranslationValidationError", "OmniTranslationValidationError"),
    ("ReconstructionValidationError", "ReconstructionValidationError"),
    ("ValidationError", "ValidationError"),
    ("validation failed", "ValidationError"),
)


def _is_upstream_llm_error(error_text: str) -> bool:
    lowered = error_text.lower()
    return any(marker.lower() in lowered for marker in UPSTREAM_LLM_ERROR_MARKERS)


def _error_type_name(error: Exception | str, fallback: str | None = None) -> str:
    if isinstance(error, Exception):
        return error.__class__.__name__

    text = str(error or "")
    for marker, name in VALIDATION_ERROR_TYPE_MARKERS:
        if marker in text:
            return name
    if fallback:
        return fallback
    first_line = text.strip().splitlines()[0] if text.strip() else ""
    if first_line.startswith("prerequisite_invalid:"):
        return "prerequisite_invalid"
    if first_line.startswith("prerequisite_failed:"):
        return "prerequisite_failed"
    return "Error"


class TqdmBar:
    def __init__(
        self,
        show_tqdm_bar: bool = False,
        total: int | None = None,
        desc: str = "Processing...",
        initial: int = 0,
    ):
        self.show_tqdm_bar = show_tqdm_bar
        self.total = total
        self.desc = desc
        self.initial = initial
        self.finished = initial
        self.failed = 0
        self.latest_uid = ""
        self.latest_error = ""
        self.tqdm_bar: Optional[tqdm] = None

    def reset(
        self,
        *,
        show_tqdm_bar: bool,
        total: int | None = None,
        desc: str = "Processing...",
        initial: int = 0,
    ) -> None:
        if self.tqdm_bar is not None:
            self.tqdm_bar.close()
            self.tqdm_bar = None
        self.show_tqdm_bar = show_tqdm_bar
        self.total = total
        self.desc = desc
        self.initial = initial
        self.finished = initial
        self.failed = 0
        self.latest_uid = ""
        self.latest_error = ""
        if self.show_tqdm_bar:
            self.tqdm_bar = tqdm(total=self.total, desc=self.desc, initial=self.initial)
            self._refresh_postfix()

    def _postfix(self) -> dict[str, int | str]:
        postfix: dict[str, int | str] = {"finished": self.finished, "failed": self.failed}
        if self.latest_uid:
            postfix["uid"] = self.latest_uid
        if self.latest_error:
            postfix["error"] = self.latest_error
        return postfix

    def _refresh_postfix(self) -> None:
        if self.tqdm_bar is not None:
            self.tqdm_bar.set_postfix(self._postfix())

    def update(
        self,
        desc: str | None = None,
        *,
        n_finished: int = 1,
        n_failed: int = 0,
    ) -> None:
        self.finished += n_finished
        self.failed += n_failed
        if not self.show_tqdm_bar:
            return
        current_desc = desc or self.desc
        if self.tqdm_bar is None:
            self.tqdm_bar = tqdm(total=self.total, desc=current_desc, initial=self.initial)
        else:
            self.tqdm_bar.set_description(current_desc)
        self._refresh_postfix()
        self.tqdm_bar.update(n_finished + n_failed)

    def set_status_message(self, *, uid: str | None = None, error_name: str | None = None) -> None:
        self.latest_uid = uid or ""
        self.latest_error = error_name or ""
        if self.show_tqdm_bar:
            if self.tqdm_bar is None:
                self.tqdm_bar = tqdm(total=self.total, desc=self.desc, initial=self.initial)
            self._refresh_postfix()
        elif self.latest_error:
            suffix = f" uid={self.latest_uid}" if self.latest_uid else ""
            print(f"error={self.latest_error}{suffix}")

    def write_latest_error(
        self,
        error: Exception | str | None,
        *,
        uid: str | None = None,
        error_name: str | None = None,
    ) -> None:
        if not error:
            return
        error_text = str(error)
        display_error_name = _error_type_name(error, error_name)
        if self.show_tqdm_bar:
            if _is_upstream_llm_error(error_text):
                tqdm.write(error_text)
            else:
                self.set_status_message(uid=uid, error_name=display_error_name)
        else:
            if _is_upstream_llm_error(error_text):
                print(error_text)
            else:
                suffix = f" uid={uid}" if uid else ""
                print(f"error={display_error_name}{suffix}")

    def close(self) -> None:
        if self.tqdm_bar is not None:
            self.tqdm_bar.close()
            self.tqdm_bar = None


def aggregate_shard_summaries(summaries: list[dict[str, int | str]]) -> dict[str, int]:
    """Aggregate numeric shard summary fields for end-of-run printing."""
    aggregated: dict[str, int] = {"shards": len(summaries)}
    for summary in summaries:
        for key, value in summary.items():
            if isinstance(value, int):
                aggregated[key] = aggregated.get(key, 0) + value
    return aggregated


def _failed_units_for_stage(record: PipelineRecord, stage: str) -> list[dict[str, str]]:
    """Return failed units as minimal JSON-serializable uid/side/lang objects."""
    failed_units: list[dict[str, str]] = []

    if stage == "staged_translation":
        for code, branch in sorted(record.target.languages.items()):
            if branch.status.raw_translation.status == StatusEnum.FAILED:
                failed_units.append({"uid": record.uid, "side": "target", "lang": code})
        return failed_units

    if stage == "omni_translation":
        if record.source.status.asr.status == StatusEnum.FAILED:
            failed_units.append({"uid": record.uid, "side": "source", "lang": record.metadata.language})
        for code, branch in sorted(record.target.languages.items()):
            if branch.status.raw_translation.status == StatusEnum.FAILED:
                failed_units.append({"uid": record.uid, "side": "target", "lang": code})
        return failed_units

    if stage == "time_pressure_segmentation":
        if record.source.status.time_pressure_segmentation.status == StatusEnum.FAILED:
            failed_units.append({"uid": record.uid, "side": "source", "lang": record.metadata.language})
        return failed_units

    if stage == "translation_reconstruction":
        for code, branch in sorted(record.target.languages.items()):
            if branch.status.reconstruction.status == StatusEnum.FAILED:
                failed_units.append({"uid": record.uid, "side": "target", "lang": code})
        return failed_units

    if stage == "pure_text_segmentation":
        for code, branch in sorted(record.target.languages.items()):
            if branch.status.pure_text_segmentation.status == StatusEnum.FAILED:
                failed_units.append({"uid": record.uid, "side": "target", "lang": code})
        return failed_units

    if stage == "target_centric_mapping":
        for code, branch in sorted(record.target.languages.items()):
            if branch.status.tgt_src_mapping.status == StatusEnum.FAILED:
                failed_units.append({"uid": record.uid, "side": "target", "lang": code})
        return failed_units

    raise ValueError(f"Unsupported LLM pipeline summary stage: {stage}")


def collect_failed_units_from_output_paths(
    *,
    output_paths: list[Path],
    stage: str,
) -> list[dict[str, str]]:
    """Collect unique failed uid/side/lang units from final output cache shards."""
    seen: set[tuple[str, str, str]] = set()
    failed_units: list[dict[str, str]] = []
    for output_path in output_paths:
        for record in load_pipeline_records_by_uid(output_path).values():
            for unit in _failed_units_for_stage(record, stage):
                key = (unit["uid"], unit["side"], unit["lang"])
                if key in seen:
                    continue
                seen.add(key)
                failed_units.append(unit)
    failed_units.sort(key=lambda item: (item["uid"], item["side"], item["lang"]))
    return failed_units


def print_llm_pipeline_summary(
    *,
    title: str,
    summaries: list[dict[str, int | str]],
    output_paths: list[Path],
    stage: str,
) -> None:
    """Print an end-of-run summary and JSONL failed uid/side/lang units."""
    print(f"=== {title} summary ===")
    for key, value in sorted(aggregate_shard_summaries(summaries).items()):
        print(f"{key}: {value}")
    print()

    failed_units = collect_failed_units_from_output_paths(output_paths=output_paths, stage=stage)
    if not failed_units:
        print("failed_items_jsonl: 0")
        return

    print("failed_items_jsonl:")
    for unit in failed_units:
        print(json.dumps(unit, ensure_ascii=False, separators=(",", ":")))


def load_metadata_by_part(dataset_root: Path) -> list[tuple[Path, list[MetaData]]]:
    items: list[tuple[Path, list[MetaData]]] = []
    for jsonl_path in sorted((dataset_root / "metadata").glob("*/*.jsonl")):
        records: list[MetaData] = []
        with jsonl_path.open() as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(MetaData(**json.loads(line)))
        items.append((jsonl_path, records))
    return items


def load_metadata_map(dataset_root: Path) -> dict[str, MetaData]:
    metadata_by_uid: dict[str, MetaData] = {}
    for _, records in load_metadata_by_part(dataset_root):
        for meta in records:
            metadata_by_uid[meta.uid] = meta
    return metadata_by_uid


def load_transcriptions_by_part(dataset_root: Path) -> list[tuple[Path, list[Transcription]]]:
    items: list[tuple[Path, list[Transcription]]] = []
    for jsonl_path in sorted((dataset_root / "transcription").glob("*/*.jsonl")):
        records: list[Transcription] = []
        with jsonl_path.open() as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(Transcription(**json.loads(line)))
        items.append((jsonl_path, records))
    return items


def load_pipeline_records_by_uid(output_path: Path) -> dict[str, PipelineRecord]:
    items: dict[str, PipelineRecord] = {}
    if not output_path.exists():
        return items
    with output_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = PipelineRecord(**json.loads(line))
            normalize_pipeline_record_state(record)
            items[record.uid] = record
    return items


def load_pipeline_records_by_part(cache_root: Path) -> list[tuple[Path, list[PipelineRecord]]]:
    items: list[tuple[Path, list[PipelineRecord]]] = []
    for jsonl_path in sorted(cache_root.rglob("*.jsonl")):
        records: list[PipelineRecord] = []
        with jsonl_path.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = PipelineRecord(**json.loads(line))
                normalize_pipeline_record_state(record)
                records.append(record)
        items.append((jsonl_path, records))
    return items


def load_pipeline_records_by_part_latest(cache_root: Path) -> list[tuple[Path, list[PipelineRecord]]]:
    items: list[tuple[Path, list[PipelineRecord]]] = []
    for jsonl_path in sorted(cache_root.rglob("*.jsonl")):
        records_by_uid = load_pipeline_records_by_uid(jsonl_path)
        items.append((jsonl_path, list(records_by_uid.values())))
    return items


def load_pipeline_records(output_path: Path) -> list[PipelineRecord]:
    items: list[PipelineRecord] = []
    if not output_path.exists():
        return items
    with output_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = PipelineRecord(**json.loads(line))
            normalize_pipeline_record_state(record)
            items.append(record)
    return items


def omni_translation_errors(record: PipelineRecord) -> list[str]:
    errors = list(record.source.status.asr.errors)
    seen = set(errors)
    for language_code, branch in sorted(record.target.languages.items()):
        for error in branch.status.raw_translation.errors:
            tagged = f"[{language_code}] {error}"
            if error in seen or tagged in seen:
                continue
            errors.append(tagged)
            seen.add(tagged)
    return errors


def is_finished_omni_translation_record(record: PipelineRecord) -> bool:
    transcript = record.source.artifacts.transcript
    if record.source.status.asr.status != StatusEnum.FINISHED:
        return False
    if transcript is None or not transcript.text:
        return False
    if not record.target.languages:
        return False
    for language_code, target in record.target.languages.items():
        status = target.status.raw_translation
        if not target.artifacts.raw_translation.text:
            return False
        if status.status != StatusEnum.FINISHED:
            return False
    return True


async def append_record(
    *,
    output_path: Path,
    record: PipelineRecord,
    file_lock,
) -> None:
    async with file_lock:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        jsonl_mode = "a" if output_path.exists() else "w"
        with output_path.open(jsonl_mode) as jsonl_f:
            jsonl_f.write(record.model_dump_json() + "\n")


async def upsert_record(
    *,
    output_path: Path,
    record: PipelineRecord,
    file_lock,
) -> None:
    async with file_lock:
        existing_records = load_pipeline_records(output_path)
        merged_by_uid: OrderedDict[str, PipelineRecord] = OrderedDict()
        for existing in existing_records:
            merged_by_uid[existing.uid] = existing

        existing_record = merged_by_uid.get(record.uid)
        if existing_record is None:
            merged_by_uid[record.uid] = record
        else:
            merged_by_uid[record.uid] = merge_pipeline_records([existing_record, record])[0]

        normalize_pipeline_record_state(merged_by_uid[record.uid])
        atomic_write_pipeline_records(output_path, list(merged_by_uid.values()))


async def append_visualization(
    *,
    shard_visualized_path: Path,
    visualized: str,
    file_lock,
) -> None:
    async with file_lock:
        shard_visualized_path.parent.mkdir(parents=True, exist_ok=True)
        md_mode = "a" if shard_visualized_path.exists() else "w"
        with shard_visualized_path.open(md_mode) as md_f:
            md_f.write(visualized)


async def append_record_and_visualization(
    *,
    output_path: Path,
    shard_visualized_path: Path,
    record: PipelineRecord,
    visualized: str,
    file_lock,
) -> None:
    await append_record(
        output_path=output_path,
        record=record,
        file_lock=file_lock,
    )
    await append_visualization(
        shard_visualized_path=shard_visualized_path,
        visualized=visualized,
        file_lock=file_lock,
    )


async def upsert_record_and_visualization(
    *,
    output_path: Path,
    shard_visualized_path: Path,
    record: PipelineRecord,
    visualized: str,
    file_lock,
) -> None:
    await upsert_record(
        output_path=output_path,
        record=record,
        file_lock=file_lock,
    )
    await append_visualization(
        shard_visualized_path=shard_visualized_path,
        visualized=visualized,
        file_lock=file_lock,
    )


def _is_effectively_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value)
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    if hasattr(value, "model_dump"):
        dumped = value.model_dump()
        return any(_is_effectively_present(v) for v in dumped.values())
    return True


def _has_meaningful_groups(groups: list[list[int]] | None) -> bool:
    return bool(groups) and any(bool(group) for group in groups)


def _has_meaningful_target_segmentation_groups(record: Any) -> bool:
    if record is None:
        return False
    groups = getattr(record, "groups", None)
    return _has_meaningful_groups(groups)


def _has_meaningful_source_segmentation(record: Any) -> bool:
    if record is None:
        return False
    sense_units = getattr(record, "sense_units", None)
    if sense_units is None:
        return False
    groups = getattr(sense_units, "groups", None)
    return _has_meaningful_groups(groups)


def normalize_pipeline_record_state(record: PipelineRecord) -> PipelineRecord:
    transcript = record.source.artifacts.transcript
    if transcript is not None and transcript.text and record.source.status.asr.status == StatusEnum.PENDING:
        record.source.status.asr.status = StatusEnum.FINISHED

    alignment = record.source.artifacts.alignment
    if alignment is not None and alignment.tokens and record.source.status.forced_alignment.status == StatusEnum.PENDING:
        record.source.status.forced_alignment.status = StatusEnum.FINISHED

    source_segmentation = record.source.artifacts.time_pressure_segmentation
    if (
        source_segmentation is not None
        and _has_meaningful_groups(source_segmentation.sense_units.groups)
        and record.source.status.time_pressure_segmentation.status == StatusEnum.PENDING
    ):
        record.source.status.time_pressure_segmentation.status = StatusEnum.FINISHED

    for code, branch in record.target.languages.items():
        branch.language_code = branch.language_code or code

        if branch.artifacts.raw_translation.text and branch.status.raw_translation.status == StatusEnum.PENDING:
            branch.status.raw_translation.status = StatusEnum.FINISHED

        if branch.artifacts.reconstruction.text and branch.status.reconstruction.status == StatusEnum.PENDING:
            branch.status.reconstruction.status = StatusEnum.FINISHED

        segmentation_groups = branch.artifacts.pure_text_segmentation.sense_units.groups
        if _has_meaningful_groups(segmentation_groups) and branch.status.pure_text_segmentation.status == StatusEnum.PENDING:
            branch.status.pure_text_segmentation.status = StatusEnum.FINISHED
        elif not _has_meaningful_groups(segmentation_groups) and branch.status.pure_text_segmentation.status == StatusEnum.FINISHED:
            branch.status.pure_text_segmentation = TaskStatus()

        if branch.artifacts.tgt_src_mapping.mappings and branch.status.tgt_src_mapping.status == StatusEnum.PENDING:
            branch.status.tgt_src_mapping.status = StatusEnum.FINISHED

    return record


def _merge_task_status(current: TaskStatus, incoming: TaskStatus) -> TaskStatus:
    priority = {
        StatusEnum.FINISHED: 4,
        StatusEnum.FAILED: 3,
        StatusEnum.RUNNING: 2,
        StatusEnum.PENDING: 1,
    }
    if priority[incoming.status] > priority[current.status]:
        return incoming.model_copy(deep=True)
    if priority[incoming.status] < priority[current.status]:
        return current
    merged = current.model_copy(deep=True)
    seen = set(merged.errors)
    for error in incoming.errors:
        if error not in seen:
            merged.errors.append(error)
            seen.add(error)
    return merged


def merge_pipeline_records(records: list[PipelineRecord]) -> list[PipelineRecord]:
    """Merge duplicate rows into one consolidated record per UID."""
    merged_by_uid: OrderedDict[str, PipelineRecord] = OrderedDict()

    for record in records:
        existing = merged_by_uid.get(record.uid)
        if existing is None:
            merged_by_uid[record.uid] = record.model_copy(deep=True)
            continue

        if not existing.source.artifacts.transcript and record.source.artifacts.transcript:
            existing.source.artifacts.transcript = record.source.artifacts.transcript.model_copy(deep=True)
        if not existing.source.artifacts.alignment and record.source.artifacts.alignment:
            existing.source.artifacts.alignment = record.source.artifacts.alignment.model_copy(deep=True)
        if (
            not _has_meaningful_source_segmentation(existing.source.artifacts.time_pressure_segmentation)
            and _has_meaningful_source_segmentation(record.source.artifacts.time_pressure_segmentation)
        ):
            existing.source.artifacts.time_pressure_segmentation = record.source.artifacts.time_pressure_segmentation.model_copy(deep=True)

        existing.source.status.asr = _merge_task_status(existing.source.status.asr, record.source.status.asr)
        existing.source.status.forced_alignment = _merge_task_status(
            existing.source.status.forced_alignment,
            record.source.status.forced_alignment,
        )
        existing.source.status.time_pressure_segmentation = _merge_task_status(
            existing.source.status.time_pressure_segmentation,
            record.source.status.time_pressure_segmentation,
        )

        if not existing.target.shared.translation_analysis and record.target.shared.translation_analysis:
            existing.target.shared.translation_analysis = record.target.shared.translation_analysis

        for code, incoming_branch in record.target.languages.items():
            existing_branch = existing.target.languages.setdefault(
                code,
                incoming_branch.model_copy(deep=True),
            )
            if existing_branch is incoming_branch:
                continue

            existing_branch.language_code = existing_branch.language_code or incoming_branch.language_code or code

            for field_name in ("raw_translation", "reconstruction"):
                existing_value = getattr(existing_branch.artifacts, field_name)
                incoming_value = getattr(incoming_branch.artifacts, field_name)
                if not existing_value and incoming_value:
                    setattr(existing_branch.artifacts, field_name, incoming_value)

            if (
                not _has_meaningful_target_segmentation_groups(existing_branch.artifacts.pure_text_segmentation.sense_units)
                and _has_meaningful_target_segmentation_groups(incoming_branch.artifacts.pure_text_segmentation.sense_units)
            ):
                existing_branch.artifacts.pure_text_segmentation = incoming_branch.artifacts.pure_text_segmentation.model_copy(deep=True)

            if (
                not existing_branch.artifacts.tgt_src_mapping.mappings
                and incoming_branch.artifacts.tgt_src_mapping.mappings
            ):
                existing_branch.artifacts.tgt_src_mapping = incoming_branch.artifacts.tgt_src_mapping.model_copy(deep=True)

            existing_branch.status.raw_translation = _merge_task_status(
                existing_branch.status.raw_translation,
                incoming_branch.status.raw_translation,
            )
            existing_branch.status.pure_text_segmentation = _merge_task_status(
                existing_branch.status.pure_text_segmentation,
                incoming_branch.status.pure_text_segmentation,
            )
            if (
                existing_branch.status.pure_text_segmentation.status == StatusEnum.FINISHED
                and not _has_meaningful_target_segmentation_groups(existing_branch.artifacts.pure_text_segmentation.sense_units)
            ):
                existing_branch.status.pure_text_segmentation = TaskStatus()

            existing_branch.status.tgt_src_mapping = _merge_task_status(
                existing_branch.status.tgt_src_mapping,
                incoming_branch.status.tgt_src_mapping,
            )

            current_reconstruction = existing_branch.status.reconstruction
            incoming_reconstruction = incoming_branch.status.reconstruction
            if incoming_reconstruction.status == StatusEnum.FINISHED and current_reconstruction.status != StatusEnum.FINISHED:
                existing_branch.artifacts.reconstruction = incoming_branch.artifacts.reconstruction
            elif not existing_branch.artifacts.reconstruction and incoming_branch.artifacts.reconstruction:
                existing_branch.artifacts.reconstruction = incoming_branch.artifacts.reconstruction
            existing_branch.status.reconstruction = _merge_task_status(
                current_reconstruction,
                incoming_reconstruction,
            )

    return list(merged_by_uid.values())


def atomic_write_pipeline_records(output_path: Path, records: list[PipelineRecord]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_path_str = tempfile.mkstemp(prefix=f".{output_path.name}.", suffix=".tmp", dir=str(output_path.parent))
    temp_path = Path(temp_path_str)
    try:
        with os.fdopen(fd, "w") as f:
            for record in records:
                f.write(record.model_dump_json() + "\n")
        os.replace(temp_path, output_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def condense_pipeline_record_shard(*, output_path: Path) -> dict[str, int]:
    records = load_pipeline_records(output_path)
    if not records:
        return {"rows_before": 0, "rows_after": 0}

    merged_records = merge_pipeline_records(records)
    for record in merged_records:
        normalize_pipeline_record_state(record)
    atomic_write_pipeline_records(output_path, merged_records)
    return {"rows_before": len(records), "rows_after": len(merged_records)}


def safe_shard_label(output_path: Path) -> str:
    return f"{output_path.parent.name}/{output_path.name}"


def shard_language_and_part_suffix(shard_jsonl_path: Path) -> tuple[str, str]:
    language = shard_jsonl_path.parent.name
    match = re.match(r"^(?:metadata|transcription)-([^-]+)-(part.+\.jsonl)$", shard_jsonl_path.name)
    if match:
        language = match.group(1)
        part_suffix = f"{language}-{match.group(2)}"
        return language, part_suffix
    return language, shard_jsonl_path.name


def shard_part_suffix_from_transcription_path(transcription_jsonl_path: Path) -> tuple[str, str]:
    return shard_language_and_part_suffix(transcription_jsonl_path)


def _append_multiline_block(parts: list[str], title: str, content: str | None) -> None:
    parts += [title, content or ""]


def _format_inline_code(value: Any) -> str:
    return f"`{value}`"


def _format_numbered_lines(text: str) -> list[str]:
    stripped = (text or "").strip()
    if not stripped:
        return []
    return [f"{idx}. {line}" for idx, line in enumerate(stripped.splitlines()) if line.strip()]


def _format_asr_blocks_html(asr_blocks: list[str]) -> str:
    return "```html\n" + "\n".join(f"* W{i}. {asr}" for i, asr in enumerate(asr_blocks)) + "\n```"


def _format_numbered_html_lines(lines: list[str]) -> str:
    if not lines:
        return "```html\n```"
    return "```html\n" + "\n".join(f"{idx}. {line}" for idx, line in enumerate(lines)) + "\n```"


def _split_block_and_timestamp(block: str) -> tuple[str, str]:
    text = (block or "").strip()
    if not text:
        return "", ""
    if "; " not in text:
        return text, ""
    content, timestamp = text.split("; ", 1)
    return content.strip(), timestamp.strip()


def visualization_translation_only(
    uid: str,
    scratchpad: str,
    final_result: Any,
    asr_language_name: str | None = None,
    asr_text: str | None = None,
    status: str | None = None,
    errors: list[str] | None = None,
) -> str:
    parts = [f"=== {uid} ===", ""]
    _append_multiline_block(parts, "scratchpad:", scratchpad)
    parts.append("")
    transcript = None
    translations: dict[str, Any] = {}
    source_anchor_review = None
    if isinstance(final_result, dict):
        if isinstance(final_result.get("asr"), dict) or isinstance(final_result.get("translation"), dict):
            transcript = final_result.get("asr")
            if isinstance(final_result.get("source_anchor_review"), dict):
                source_anchor_review = final_result.get("source_anchor_review")
            raw_translations = final_result.get("translation")
            if isinstance(raw_translations, dict):
                translations = raw_translations
        else:
            translations = final_result

    parts += ["asr:"]
    if asr_language_name is not None or asr_text is not None:
        parts += [f"- {asr_language_name or 'Source'}", f"  {asr_text or ''}"]
    elif isinstance(transcript, dict):
        language_name = transcript.get("language_name") or "Source"
        text = transcript.get("text") or ""
        parts += [f"- {language_name}", f"  {text}"]
    else:
        parts += ["- Source", ""]

    if isinstance(source_anchor_review, dict):
        parts.append("")
        parts += ["source_anchor_review:"]
        status_text = source_anchor_review.get("status") or ""
        source_anchor_used = source_anchor_review.get("source_anchor_used") or ""
        anchor_text = source_anchor_review.get("text") or ""
        parts += [f"- status: {status_text}", f"- source_anchor_used: {source_anchor_used}"]
        _append_multiline_block(parts, "- text:", anchor_text)
        changes = source_anchor_review.get("changes")
        if changes:
            parts += ["- changes:"]
            for change in changes:
                if not isinstance(change, dict):
                    continue
                parts += [
                    f"  - raw: {change.get('raw') or ''}",
                    f"    audio_supported: {change.get('audio_supported') or ''}",
                    f"    reason: {change.get('reason') or ''}",
                ]
        else:
            parts += ["- changes: none"]

    parts.append("")
    parts += ["translation:"]
    if translations:
        for language, text in sorted(translations.items(), key=lambda item: _readable_language_name(item[0])):
            parts += [f"- {_readable_language_name(language)}", f"  {text}"]
    elif isinstance(final_result, dict) and not transcript:
        parts += ["- none"]
    elif not isinstance(final_result, dict):
        parts += ["- raw", f"  {final_result}"]
    else:
        parts += ["- none"]
    parts += ["", "---", ""]
    return "\n".join(parts)


def visualization_omni_translation_only(
    uid: str,
    scratchpad: str,
    final_result: Any,
    asr_language_name: str | None = None,
    asr_text: str | None = None,
    status: str | None = None,
    errors: list[str] | None = None,
) -> str:
    return visualization_translation_only(
        uid=uid,
        scratchpad=scratchpad,
        final_result=final_result,
        asr_language_name=asr_language_name,
        asr_text=asr_text,
        status=status,
        errors=errors,
    )


def _readable_language_name(language: str) -> str:
    if not isinstance(language, str) or not language.strip():
        return "Unknown"
    text = language.strip()
    upper = text.upper()
    if upper in Config.lang_code2name:
        return Config.lang_code2name[upper]
    return text


def _single_visualization_value(values: dict[str, Any]) -> str:
    if not values:
        return ""
    for value in values.values():
        if value is not None:
            return str(value)
    return ""


def _append_retry_attempts(parts: list[str], attempts: list[dict[str, Any]] | None) -> None:
    if not attempts:
        return
    parts += ["", "attempts:"]
    for attempt in attempts:
        retry = attempt.get("retry", attempt.get("retry_index", ""))
        max_retries = attempt.get("max_retries", "")
        status = str(attempt.get("status", ""))
        reason = str(attempt.get("reason", attempt.get("error", "")))
        retry_label = f"{retry}/{max_retries}" if max_retries != "" else str(retry)
        parts += [
            "",
            f"- retry: {retry_label}",
            f"  status: {status}",
            f"  reason: {reason}",
        ]
        if status != "failed_after_response":
            continue
        validation_items = [
            ("scratchpad", attempt.get("scratchpad", "")),
            ("result", attempt.get("result", "")),
            ("validator_scratchpad", attempt.get("validator_scratchpad", "")),
            ("validator_result", attempt.get("validator_validator_result", attempt.get("validator_result", ""))),
            ("validator_order_risk", attempt.get("validator_order_risk", "")),
            ("validator_source_tokens", attempt.get("validator_source_tokens_inline", attempt.get("validator_source_tokens", ""))),
            ("validator_source_windows", attempt.get("validator_source_windows", "")),
            ("validator_feedback", attempt.get("validator_feedback", "")),
        ]
        if any(str(value or "").strip() for _, value in validation_items):
            parts.append("  validation:")
            for label, value in validation_items:
                text = str(value or "")
                if text.strip():
                    _append_multiline_block(parts, f"    {label}:", text)


def visualization_translation_reconstruction(
    uid: str,
    scratchpad: str,
    asr_language_name: str,
    asr_text: str,
    raw_translation: dict[str, Any],
    reconstructed_translation: dict[str, Any],
    shared_translation_analysis: str = "",
    validator_scratchpad: str = "",
    validator_result: str = "",
    validator_order_risk: str = "",
    validator_source_tokens: str = "",
    validator_source_windows: str = "",
    validator_feedback: str = "",
    attempts: list[dict[str, Any]] | None = None,
    errors: list[str] | None = None,
) -> str:
    parts = [f"=== {uid} ===", ""]
    if shared_translation_analysis:
        _append_multiline_block(parts, "shared translation analysis:", shared_translation_analysis)
        parts.append("")
    parts += [
        "scratchpad:",
        scratchpad or "",
        "",
        "raw transcription text:",
        f"- {asr_language_name or 'Source'}",
        f"  {asr_text or ''}",
        "",
        "comparison of raw and reconstructed:",
    ]
    language_names = sorted(set(raw_translation.keys()) | set(reconstructed_translation.keys()))
    for language_name in language_names:
        parts += [
            f"- {language_name}",
            f"  - raw: {raw_translation.get(language_name, '')}",
            f"  - reconstructed: {reconstructed_translation.get(language_name, '')}",
        ]
    if validator_order_risk:
        order_risk = (validator_order_risk or "").strip()
        if order_risk.startswith("target_tokens:"):
            target_tokens_block = order_risk
        elif "\ntarget_tokens:" in order_risk:
            target_tokens_block = "target_tokens:" + order_risk.split("\ntarget_tokens:", 1)[1]
        else:
            target_tokens_block = order_risk
        parts += [
            "",
            "**ORDER_RISK**",
            "",
            "source_windows:",
            validator_source_windows.strip() or validator_source_tokens.strip() or "{}",
            "",
        ]
        if target_tokens_block:
            parts.append(target_tokens_block)
            parts.append("")
        if validator_result:
            parts += ["validator_result:", "```json", validator_result.strip(), "```", ""]
        if validator_feedback:
            feedback_lines = [
                f"* raw_transcription: {asr_text or ''}",
                f"* raw_reconstruction: {_single_visualization_value(raw_translation)}",
                f"* candidate_reconstruction: {_single_visualization_value(reconstructed_translation)}",
                "",
                validator_feedback.strip(),
            ]
            parts += ["feed_back:", "```md", "\n".join(feedback_lines).strip(), "```", ""]
    if errors:
        parts += ["errors:", "```json", json.dumps(errors, ensure_ascii=False, indent=2), "```", ""]
    _append_retry_attempts(parts, attempts)
    parts += ["", "---", ""]
    return "\n".join(parts)


def _format_segmentation_groups(
    *,
    unit_label: str,
    units: list[str],
    groups: list[list[int]],
) -> list[str]:
    parts = ["segmentation:"]
    if not groups:
        parts.append("- none")
        return parts

    for group_idx, group in enumerate(groups, start=1):
        group_units = [units[idx] for idx in group if 0 <= idx < len(units)]
        parts += [
            f"- group_{group_idx}",
            f"  - {unit_label}_indices: {group}",
            f"  - {unit_label}s: {json.dumps(group_units, ensure_ascii=False)}",
            f"  - text: {''.join(group_units) if unit_label == 'word' else ' '.join(group_units).strip()}",
        ]
    return parts


def _append_multiline_block(parts: list[str], heading: str, text: str) -> None:
    parts.append(heading)
    parts.append(text or "")


def visualization_time_pressure_segmentation(record: PipelineRecord) -> str:
    transcript = record.source.artifacts.transcript
    alignment = record.source.artifacts.alignment
    segmentation = record.source.artifacts.time_pressure_segmentation
    debug_payload = record.get_debug_time_pressure_segmentation()
    status = record.source.status.time_pressure_segmentation.status.value
    errors = record.source.status.time_pressure_segmentation.errors
    raw_text = transcript.text if transcript else ""
    word_indices_text = ""
    if alignment and alignment.tokens:
        chunks = build_transcription_chunks(duration=record.metadata.duration, words=apply_mapping_groups(alignment.tokens, alignment.words, language=record.metadata.language))
        word_indices_text = render_transcription_chunk_word_indices(chunks).rstrip()

    parts = [
        f"=== {record.uid} ===",
        "",
        f"status: {status}",
        "",
        "raw_text:",
        raw_text,
        "",
        "word_indices:",
        word_indices_text,
        "",
        "scratchpad:",
        debug_payload.get("scratchpad", ""),
        "",
        "result:",
        debug_payload.get("result", ""),
    ]
    attempts = debug_payload.get("attempts", [])
    if attempts:
        parts += ["", "attempts:"]
        for attempt in attempts:
            retry = attempt.get("retry", attempt.get("retry_index", ""))
            max_retries = attempt.get("max_retries", "")
            status = attempt.get("status", "")
            reason = attempt.get("reason", attempt.get("error", ""))
            retry_label = f"{retry}/{max_retries}" if max_retries != "" else str(retry)
            parts += [
                "",
                f"- retry: {retry_label}",
                f"  status: {status}",
                f"  reason: {reason}",
            ]
            if status == "failed_after_response":
                _append_multiline_block(parts, "  scratchpad:", str(attempt.get("scratchpad", "")))
                _append_multiline_block(parts, "  result:", str(attempt.get("result", "")))
            _append_multiline_block(parts, "  error:", str(attempt.get("error", "")))
    if transcript and alignment and segmentation and record.metadata:
        debug_transcription = Transcription(
            uid=record.uid,
            language=transcript.language_code or record.metadata.language,
            text=transcript.text,
            tokens=alignment.tokens,
            words=alignment.words,
            sense_units=segmentation.sense_units,
            author=transcript.author,
        )
        asr_blocks = build_asr_blocks(record.metadata, debug_transcription, debug=True)
        parts += ["", "parsed_asr_blocks:", _format_asr_blocks_html(asr_blocks) if asr_blocks else "```html\n```"]
    if errors:
        parts += ["", "errors:", "```json", json.dumps(errors, ensure_ascii=False, indent=2), "```"]
    parts += ["", "---", ""]
    return "\n".join(parts)


def visualization_pure_text_segmentation(record: PipelineRecord, target_language_code: str) -> str:
    target = record.target.languages.get(target_language_code)
    reconstructed_translation = target.artifacts.reconstruction.text if target else ""
    target_tokens = list(target.artifacts.pure_text_segmentation.tokens) if target else []
    token_indices = {idx: token for idx, token in enumerate(target_tokens)}
    grouped_result = group_tokens_by_sense_units(
        language=target_language_code,
        tokens=target_tokens,
        sense_unit_groups=target.artifacts.pure_text_segmentation.sense_units.groups if target else [],
    )
    debug_payload = record.get_debug_pure_text_segmentation(target_language_code)
    scratchpad_text = debug_payload.get("scratchpad", "")

    parts = [
        f"=== {record.uid} ===",
        "",
        "reconstructed_translation:",
        reconstructed_translation,
        "",
        "token_indices:",
        _format_inline_code(json.dumps(token_indices, ensure_ascii=False)),
        "",
        "scratchpad:",
        scratchpad_text,
        "",
        "result:",
    ]
    numbered_result_lines = [f"{idx}. {text}" for idx, text in grouped_result.items()]
    if numbered_result_lines:
        parts += numbered_result_lines
    else:
        parts.append("")
    _append_retry_attempts(parts, debug_payload.get("attempts", []))
    parts += ["", "---", ""]
    return "\n".join(parts)


def visualization_target_centric_mapping(record: PipelineRecord, target_language_code: str) -> str:
    target = record.target.languages.get(target_language_code)
    transcript = record.source.artifacts.transcript
    alignment = record.source.artifacts.alignment
    source_segmentation = record.source.artifacts.time_pressure_segmentation
    source_text = transcript.text if transcript else ""
    target_text = target.artifacts.reconstruction.text if target else ""
    target_groups = target.artifacts.pure_text_segmentation.sense_units.groups if target else []
    source_language_code = record.metadata.language
    source_language_name = _readable_language_name(source_language_code)
    target_language_name = _readable_language_name(target_language_code)
    target_tokens = list(target.artifacts.pure_text_segmentation.tokens) if target else []
    source_tokens = {}
    if alignment and alignment.tokens and alignment.words:
        source_words = apply_mapping_groups(
            alignment.tokens,
            alignment.words,
            language=record.metadata.language,
        )
        source_tokens = {idx: word.word for idx, word in enumerate(source_words)}
    target_units = group_tokens_by_sense_units(
        language=target_language_code,
        tokens=target_tokens,
        sense_unit_groups=target_groups,
    )
    debug_payload = record.get_debug_target_centric_mapping(target_language_code)
    asr_blocks: list[str] = []
    translation_blocks: list[str] = []
    max_empty_window_count = 0
    if transcript and alignment and source_segmentation and target:
        debug_transcription = Transcription(
            uid=record.uid,
            language=transcript.language_code or record.metadata.language,
            text=transcript.text,
            tokens=alignment.tokens,
            words=alignment.words,
            sense_units=source_segmentation.sense_units,
            author=transcript.author,
        )
        asr_blocks = build_asr_blocks(
            record.metadata,
            debug_transcription,
            debug=True,
        )
        debug_translation = Translation(
            uid=record.uid,
            language=target_language_code,
            text=target_text,
            tokens=target_tokens,
            sense_units=target.artifacts.pure_text_segmentation.sense_units,
            mappings=list(target.artifacts.tgt_src_mapping.mappings),
            author=target.artifacts.tgt_src_mapping.author,
        )
        translation_blocks, max_empty_window_count = build_translation_blocks(
            record.metadata,
            debug_transcription,
            debug_translation,
            tolerance_window=0,
            debug=True,
        )

    combined_blocks: list[str] = []
    for idx in range(max(len(asr_blocks), len(translation_blocks))):
        src_block, src_timestamp = _split_block_and_timestamp(asr_blocks[idx] if idx < len(asr_blocks) else "")
        tgt_block, tgt_timestamp = _split_block_and_timestamp(translation_blocks[idx] if idx < len(translation_blocks) else "")
        timestamp = tgt_timestamp or src_timestamp
        combined_line = f"{src_block or '<src><|wait|></src>'} {tgt_block or '<tgt><|wait|></tgt>'}".strip()
        if timestamp:
            combined_line += f"; {timestamp}"
        combined_blocks.append(combined_line)

    parts = [
        f"=== {record.uid} ===",
        "",
        "source:",
        f"- language: {source_language_name}",
        f"- transcription: {source_text}",
        "- source_tokens:",
    ]
    parts += [f"  {idx}. {text}" for idx, text in source_tokens.items()] or [""]
    parts += [
        "",
        "target:",
        f"- language: {target_language_name}",
        f"- translation: {target_text}",
        "- target_sense_units:",
    ]
    parts += [f"  {idx}. {text}" for idx, text in target_units.items()] or [""]
    parts += [
        "",
        "scratchpad:",
        debug_payload.get("scratchpad", ""),
        "",
        "result:",
        _format_numbered_html_lines(combined_blocks),
        "",
        f"- max_empty_window_count: {max_empty_window_count}",
        "",
    ]
    _append_retry_attempts(parts, debug_payload.get("attempts", []))
    parts += ["", "---", ""]
    return "\n".join(parts)


def failed_visualization_target_centric_mapping(record: PipelineRecord, target_language_code: str) -> str:
    target = record.target.languages.get(target_language_code)
    transcript = record.source.artifacts.transcript
    alignment = record.source.artifacts.alignment
    source_text = transcript.text if transcript else ""
    target_text = target.artifacts.reconstruction.text if target else ""
    target_groups = target.artifacts.pure_text_segmentation.sense_units.groups if target else []
    source_language_code = record.metadata.language
    source_language_name = _readable_language_name(source_language_code)
    target_language_name = _readable_language_name(target_language_code)
    target_tokens = list(target.artifacts.pure_text_segmentation.tokens) if target else []
    source_tokens = {}
    if alignment and alignment.tokens and alignment.words:
        source_words = apply_mapping_groups(
            alignment.tokens,
            alignment.words,
            language=record.metadata.language,
        )
        source_tokens = {idx: word.word for idx, word in enumerate(source_words)}
    target_units = group_tokens_by_sense_units(
        language=target_language_code,
        tokens=target_tokens,
        sense_unit_groups=target_groups,
    )
    debug_payload = record.get_debug_target_centric_mapping(target_language_code)

    parts = [
        f"=== {record.uid} ===",
        "",
        "source:",
        f"- language: {source_language_name}",
        f"- transcription: {source_text}",
        "- source_tokens:",
    ]
    parts += [f"  {idx}. {text}" for idx, text in source_tokens.items()] or [""]
    parts += [
        "",
        "target:",
        f"- language: {target_language_name}",
        f"- translation: {target_text}",
        "- target_sense_units:",
    ]
    parts += [f"  {idx}. {text}" for idx, text in target_units.items()] or [""]
    parts += [
        "",
        "scratchpad:",
        debug_payload.get("scratchpad", ""),
        "",
        "result:",
        debug_payload.get("result", ""),
        "",
        "errors:",
        debug_payload.get("error", ""),
    ]
    _append_retry_attempts(parts, debug_payload.get("attempts", []))
    parts += ["", "---", ""]
    return "\n".join(parts)


def canonical_stage_name(stage_name: str | None) -> str:
    normalized_stage = (stage_name or "").strip()
    if normalized_stage == "asr":
        return "transcription"
    return normalized_stage


def cache_output_path(output_root: Path, shard_jsonl_path: Path, stage_name: str | None = None) -> Path:
    language, part_suffix = shard_language_and_part_suffix(shard_jsonl_path)
    normalized_stage = canonical_stage_name(stage_name)
    if normalized_stage:
        file_name = f"cache_{normalized_stage}_{part_suffix}"
    else:
        file_name = f"cache_{part_suffix}"
    return output_root / language / file_name


def reconstruction_output_path(output_root: Path, transcription_jsonl_path: Path) -> Path:
    return cache_output_path(output_root, transcription_jsonl_path, "translation_reconstruction")


def reconstruction_output_path_from_input_cache(
    output_root: Path,
    input_cache_base: Path,
    input_cache_path: Path,
) -> Path:
    relative_parent = input_cache_path.parent.relative_to(input_cache_base)
    language = relative_parent.name if str(relative_parent) != "." else input_cache_path.parent.name
    match = re.search(rf"({re.escape(language)}-part.+\.jsonl)$", input_cache_path.name)
    suffix = match.group(1) if match else input_cache_path.name.removeprefix("cache_")
    file_name = f"cache_translation_reconstruction_{suffix}"
    return output_root / relative_parent / file_name


def stage_output_path_from_input_cache(
    output_root: Path,
    input_cache_base: Path,
    input_cache_path: Path,
    stage_name: str,
) -> Path:
    relative_parent = input_cache_path.parent.relative_to(input_cache_base)
    language = relative_parent.name if str(relative_parent) != "." else input_cache_path.parent.name
    match = re.search(rf"({re.escape(language)}-part.+\.jsonl)$", input_cache_path.name)
    suffix = match.group(1) if match else input_cache_path.name.removeprefix("cache_")
    normalized_stage = canonical_stage_name(stage_name)
    file_name = f"cache_{normalized_stage}_{suffix}"
    return output_root / relative_parent / file_name


def visualized_path(output_path: Path, stage_name: str) -> Path:
    normalized_stage = canonical_stage_name(stage_name)
    expected_prefix = f"cache_{normalized_stage}_"
    if output_path.name.startswith(expected_prefix):
        file_name = output_path.name.replace(expected_prefix, f"visualized_{normalized_stage}_", 1)
    else:
        file_name = output_path.name.replace("cache_", "visualized_", 1)
    return output_path.parent / file_name.replace(".jsonl", ".md")