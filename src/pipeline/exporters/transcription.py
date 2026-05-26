"""
Transcription dataset exporter.

Converts PipelineRecord cache state into final transcription dataset schema.
This exporter reads cache records, selects ones that satisfy the transcription
dataset contract, and converts them into the final dataset format.
"""

import json
from pathlib import Path
from typing import Iterable, Optional

from pipeline.schema import PipelineRecord, StatusEnum
from pipeline.exporters.utils import collapse_authors

# Import final dataset schema types
from core.schema import Transcription, Word


def is_ready_for_transcription_export(record: PipelineRecord) -> bool:
    """Check whether a record satisfies the minimum transcription export contract."""
    transcript = record.source.artifacts.transcript
    return bool(
        transcript
        and transcript.text
        and record.source.status.asr.status == StatusEnum.FINISHED
    )


def record_to_transcription(record: PipelineRecord) -> Optional[Transcription]:
    """Convert a single PipelineRecord into a Transcription dataset object."""
    if not is_ready_for_transcription_export(record):
        return None

    transcript = record.source.artifacts.transcript
    alignment = record.source.artifacts.alignment
    segmentation = record.source.artifacts.time_pressure_segmentation
    text = transcript.text
    language = transcript.language_code or record.metadata.language

    # Build tokens and words from alignment if available
    tokens: list = []
    words: list = []
    if alignment and alignment.tokens:
        tokens = alignment.tokens
        words = alignment.words

    # Build sense units from segmentation if available
    from core.schema import SenseUnits
    sense_units = SenseUnits(level="minimal", groups=[])
    if segmentation and segmentation.sense_units:
        sense_units = segmentation.sense_units

    author = collapse_authors([
        transcript.author if transcript else "",
        alignment.author if alignment else "",
        segmentation.author if segmentation else "",
    ])

    return Transcription(
        uid=record.uid,
        text=text,
        language=language,
        author=author,
        tokens=tokens,
        words=words,
        sense_units=sense_units,
    )


def export_transcription_dataset(
    records: Iterable[PipelineRecord],
    output_path: str | Path,
) -> Path:
    """
    Export transcription records to a JSONL dataset file.

    Only records that satisfy the contract will be included.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    exported = 0
    mode = "a" if output_path.exists() else "w"

    with open(output_path, mode) as f:
        for record in records:
            transcription = record_to_transcription(record)
            if transcription is not None:
                f.write(json.dumps(transcription.model_dump(), ensure_ascii=False) + "\n")
                exported += 1

    print(f"Exported {exported} transcription records to {output_path}")
    return output_path


def export_transcription_from_cache(
    cache_path: str | Path,
    output_path: str | Path,
) -> Path:
    """
    Export transcription dataset directly from a cache JSONL file.

    Reads records from cache, filters, and writes final dataset.
    """
    cache_path = Path(cache_path)
    records = []
    with open(cache_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(PipelineRecord.model_validate_json(line))

    return export_transcription_dataset(records, output_path)