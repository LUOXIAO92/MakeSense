"""Collect final dataset shards from pipeline-8 cache output."""
import sys
sys.path.append('src')


import json
from pathlib import Path
from configs.config import Config
from pipeline.exporters import (
    record_to_dimensional_analysis,
    record_to_transcription,
    record_to_translation,
)
from pipeline.runners import load_pipeline_records_by_part_latest

import os
DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"

# CACHE_ROOT          = Path(".") / "cache_test"
CACHE_ROOT          = DATASET_ROOT / "cache"
INPUT_CACHE_BASE    = CACHE_ROOT / "pipeline_8_target_centric_mapping_deepseek-v4-flash"
OUTPUT_DATASET_ROOT = CACHE_ROOT / "pipeline_9_dataset"


def _part_from_cache_name(cache_name: str, source_language: str) -> str:
    marker = f"{source_language}-part"
    idx = cache_name.find(marker)
    if idx == -1:
        raise ValueError(f"Cannot derive shard suffix from cache name: {cache_name}")
    return cache_name[idx:].removeprefix(f"{source_language}-")


def _write_jsonl(path: Path, items: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def main() -> None:
    cache_parts = load_pipeline_records_by_part_latest(INPUT_CACHE_BASE)

    print("=== Pipeline 9: collect dataset ===")
    print("input_cache_dir_name:", INPUT_CACHE_BASE.name)
    print("output_dataset_root:", OUTPUT_DATASET_ROOT)
    print()

    for input_cache_path, records in cache_parts:
        source_language = input_cache_path.parent.name
        source_records = [r for r in records if r.metadata.language == source_language]
        part_suffix = _part_from_cache_name(input_cache_path.name, source_language)
        metadata_file_name = f"metadata-{source_language}-{part_suffix}"

        transcription_output_path = (
            OUTPUT_DATASET_ROOT
            / "transcription"
            / source_language
            / Config.dataset.get_file_name(
                file_type="transcription",
                metadata_file_name=metadata_file_name,
                source_language=source_language,
            )
        )

        transcriptions = []
        for record in source_records:
            transcription = record_to_transcription(record)
            if transcription is not None:
                transcriptions.append(transcription.model_dump())
        _write_jsonl(transcription_output_path, transcriptions)
        print(f"transcription: {input_cache_path.name} -> {transcription_output_path.name} ({len(transcriptions)})")

        dimensional_analysis_output_path = (
            OUTPUT_DATASET_ROOT
            / "dimensional_analysis"
            / source_language
            / f"dimensional_analysis-{source_language}-{part_suffix}"
        )
        dimensional_analysis_rows = []
        for record in source_records:
            dimensional_analysis = record_to_dimensional_analysis(record)
            if dimensional_analysis is not None:
                dimensional_analysis_rows.append(dimensional_analysis)
        _write_jsonl(dimensional_analysis_output_path, dimensional_analysis_rows)
        print(
            f"dimensional_analysis: {input_cache_path.name} -> "
            f"{dimensional_analysis_output_path.name} ({len(dimensional_analysis_rows)})"
        )

        for target_language in Config.language_codes:
            if target_language == source_language:
                continue

            translation_output_path = (
                OUTPUT_DATASET_ROOT
                / "translation"
                / source_language
                / Config.dataset.get_file_name(
                    file_type="translation",
                    metadata_file_name=metadata_file_name,
                    source_language=source_language,
                    target_language=target_language,
                )
            )

            translations = []
            for record in source_records:
                translation = record_to_translation(record, target_language)
                if translation is not None:
                    translations.append(translation.model_dump())
            _write_jsonl(translation_output_path, translations)
            print(
                f"translation: {input_cache_path.name} -> {translation_output_path.name} "
                f"({source_language}->{target_language}, {len(translations)})"
            )


if __name__ == "__main__":
    main()