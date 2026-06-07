"""
Translation dataset exporter.

Converts PipelineRecord cache state into final translation dataset schema.
"""

import json
from pathlib import Path
from typing import Iterable, Optional

from pipeline.schema import PipelineRecord, StatusEnum
from pipeline.exporters.utils import collapse_authors
from pipeline.exporters.transcription import record_to_transcription

from core.schema import Translation
from core.build_conversation import build_translation_blocks, count_max_empty_translation_windows


def is_ready_for_translation_export(
    record: PipelineRecord,
    target_language_code: str,
) -> bool:
    """Check whether a record satisfies the minimum translation export contract."""
    target = record.target.languages.get(target_language_code)
    if target is None:
        return False
    return bool(
        target.artifacts.raw_translation.text
        and target.artifacts.reconstruction.text
        and target.artifacts.pure_text_segmentation.sense_units.groups
        and target.artifacts.tgt_src_mapping.mappings
        and target.status.raw_translation.status == StatusEnum.FINISHED
        and target.status.reconstruction.status == StatusEnum.FINISHED
        and target.status.pure_text_segmentation.status == StatusEnum.FINISHED
        and target.status.tgt_src_mapping.status == StatusEnum.FINISHED
    )


def record_to_translation(
    record: PipelineRecord,
    target_language_code: str,
) -> Optional[Translation]:
    """Convert a single PipelineRecord+target_lang into a Translation dataset object."""
    target = record.target.languages.get(target_language_code)
    if target is None:
        return None
    if not is_ready_for_translation_export(record, target_language_code):
        return None

    # Build sense units from pure text segmentation if available
    from core.schema import SenseUnits
    sense_units = SenseUnits(level="minimal", groups=[])
    if target.artifacts.pure_text_segmentation and target.artifacts.pure_text_segmentation.sense_units.groups:
        sense_units = target.artifacts.pure_text_segmentation.sense_units

    mappings = list(target.artifacts.tgt_src_mapping.mappings)
    tokens = list(target.artifacts.pure_text_segmentation.tokens)
    author = collapse_authors([
        target.artifacts.raw_translation.author,
        target.artifacts.reconstruction.author,
        target.artifacts.pure_text_segmentation.author,
        target.artifacts.tgt_src_mapping.author,
    ])

    translation = Translation(
        uid=record.uid,
        raw_translation=target.artifacts.raw_translation.text,
        text=target.artifacts.reconstruction.text,
        language=target_language_code,
        author=author,
        tokens=tokens,
        sense_units=sense_units,
        mappings=mappings,
    )

    transcription = record_to_transcription(record)
    if transcription is None:
        return None
    translation_blocks = build_translation_blocks(
        record.metadata,
        transcription,
        translation,
    )
    translation.max_empty_window = count_max_empty_translation_windows(translation_blocks)

    return translation


def export_translation_dataset(
    records: Iterable[PipelineRecord],
    source_language: str,
    target_language_code: str,
    output_path: str | Path,
) -> Path:
    """
    Export translation records to a JSONL dataset file.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    exported = 0
    mode = "a" if output_path.exists() else "w"

    with open(output_path, mode) as f:
        for record in records:
            translation = record_to_translation(record, target_language_code)
            if translation is not None:
                data = translation.model_dump()
                data["source_language"] = source_language
                f.write(json.dumps(data, ensure_ascii=False) + "\n")
                exported += 1

    print(f"Exported {exported} translation records ({source_language} -> {target_language_code}) to {output_path}")
    return output_path


def export_translation_from_cache(
    cache_path: str | Path,
    source_language: str,
    target_language_code: str,
    output_path: str | Path,
) -> Path:
    """
    Export translation dataset directly from a cache JSONL file.
    """
    cache_path = Path(cache_path)
    records = []
    with open(cache_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(PipelineRecord.model_validate_json(line))

    return export_translation_dataset(records, source_language, target_language_code, output_path)