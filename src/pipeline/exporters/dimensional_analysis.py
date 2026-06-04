"""Dimensional-analysis dataset exporter.

This exporter keeps Pipeline 3 whole-utterance translation analysis in an
independent final-dataset space.  It intentionally does not extend the core
transcription or translation dataset schemas.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from pipeline.schema import PipelineRecord, StatusEnum


def is_ready_for_dimensional_analysis_export(record: PipelineRecord) -> bool:
    """Check whether a record has a whole-utterance dimensional analysis."""

    return bool(
        record.target.shared.translation_analysis.strip()
        and record.source.artifacts.transcript.text.strip()
        and record.source.status.asr.status == StatusEnum.FINISHED
    )


def record_to_dimensional_analysis(record: PipelineRecord) -> dict[str, Any] | None:
    """Convert one PipelineRecord into an independent dimensional-analysis row."""

    if not is_ready_for_dimensional_analysis_export(record):
        return None

    return {
        "uid": record.uid,
        "language": record.metadata.language,
        "text": record.target.shared.translation_analysis.strip(),
        "source_text": record.source.artifacts.transcript.text,
    }


def export_dimensional_analysis_dataset(
    records: Iterable[PipelineRecord],
    output_path: str | Path,
) -> Path:
    """Export independent dimensional-analysis records to JSONL."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    exported = 0
    mode = "a" if output_path.exists() else "w"
    with output_path.open(mode, encoding="utf-8") as f:
        for record in records:
            item = record_to_dimensional_analysis(record)
            if item is not None:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
                exported += 1

    print(f"Exported {exported} dimensional-analysis records to {output_path}")
    return output_path


def export_dimensional_analysis_from_cache(
    cache_path: str | Path,
    output_path: str | Path,
) -> Path:
    """Export dimensional-analysis rows directly from a cache JSONL file."""

    cache_path = Path(cache_path)
    records = []
    with cache_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(PipelineRecord.model_validate_json(line))

    return export_dimensional_analysis_dataset(records, output_path)