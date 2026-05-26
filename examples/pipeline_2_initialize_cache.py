"""Initialize canonical PipelineRecord cache shards from dataset metadata/transcription files."""

import sys
sys.path.append('src')

import os
import json
from pathlib import Path
from pipeline.runners import cache_output_path, load_metadata_by_part
from pipeline.schema import PipelineRecord, RawTranslationArtifact, StatusEnum, TaskStatus, TranscriptArtifact
from configs.config import Config


# DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"
DATASET_ROOT = Path(".") / "dataset_test"
TRANSCRIPTION_ROOT = DATASET_ROOT / "transcription"
TRANSLATION_ROOT   = DATASET_ROOT / "translation"

CACHE_ROOT  = Path(".") / "cache_test"
OUTPUT_BASE = CACHE_ROOT / "pipeline_2_initialized"


def load_transcriptions_by_uid(transcription_jsonl_path: Path) -> dict[str, object]:
    if not transcription_jsonl_path.exists():
        return {}
    from core.schema import Transcription

    records: dict[str, object] = {}
    with transcription_jsonl_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = Transcription(**json.loads(line))
            records[record.uid] = record
    return records


def load_metadata_authors_by_uid(metadata_jsonl_path: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    with metadata_jsonl_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw_record = json.loads(line)
            uid = raw_record.get("uid", "")
            if uid:
                records[uid] = raw_record.get("author", "") or ""
    return records


def load_translations_by_uid(translation_jsonl_path: Path) -> dict[str, object]:
    if not translation_jsonl_path.exists():
        return {}
    from core.schema import Translation

    records: dict[str, object] = {}
    with translation_jsonl_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = Translation(**json.loads(line))
            records[record.uid] = record
    return records


def load_target_translations_by_uid(metadata_jsonl_path: Path, source_language: str) -> dict[str, dict[str, object]]:
    translations_by_target: dict[str, dict[str, object]] = {}
    if not TRANSLATION_ROOT.exists():
        return translations_by_target

    source_dir = TRANSLATION_ROOT / source_language
    if not source_dir.exists():
        return translations_by_target

    for target_language in Config.language_codes:
        if target_language == source_language:
            continue
        translation_jsonl_path = source_dir / metadata_jsonl_path.name.replace(
            f"metadata-{source_language}-",
            f"translation-{source_language}_{target_language}-",
            1,
        )
        translations = load_translations_by_uid(translation_jsonl_path)
        if translations:
            translations_by_target[target_language] = translations
    return translations_by_target


def main() -> None:
    metadata_parts = load_metadata_by_part(DATASET_ROOT)
    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)

    print("=== Pipeline 2: initialize cache ===")
    print("dataset_root:", DATASET_ROOT)
    print("transcription_root:", TRANSCRIPTION_ROOT)
    print("translation_root:", TRANSLATION_ROOT)
    print("output_dir_name:", OUTPUT_BASE.name)
    print("metadata_shards:", len(metadata_parts))
    print()

    for metadata_jsonl_path, metadata_list in metadata_parts:
        transcription_jsonl_path = TRANSCRIPTION_ROOT / metadata_jsonl_path.parent.name / metadata_jsonl_path.name.replace(
            "metadata-", "transcription-", 1
        )
        metadata_authors_by_uid = load_metadata_authors_by_uid(metadata_jsonl_path)
        transcriptions_by_uid = load_transcriptions_by_uid(transcription_jsonl_path)
        translations_by_target = load_target_translations_by_uid(metadata_jsonl_path, metadata_jsonl_path.parent.name)
        output_path = cache_output_path(OUTPUT_BASE, metadata_jsonl_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w", encoding="utf-8") as f:
            for meta in metadata_list:
                record = PipelineRecord(uid=meta.uid, metadata=meta)
                metadata_author = metadata_authors_by_uid.get(meta.uid, "")
                transcription = transcriptions_by_uid.get(meta.uid)
                if transcription is not None and getattr(transcription, "text", ""):
                    record.source.artifacts.transcript = TranscriptArtifact(
                        language_code=meta.language,
                        language_name=Config.lang_code2name.get(meta.language, meta.language),
                        text=transcription.text,
                        author=getattr(transcription, "author", "") or metadata_author,
                    )
                    record.source.status.asr = TaskStatus(status=StatusEnum.FINISHED)
                for target_language, translations_by_uid in translations_by_target.items():
                    translation = translations_by_uid.get(meta.uid)
                    if translation is None or not getattr(translation, "text", ""):
                        continue
                    branch = record.target.languages[target_language]
                    branch.artifacts.raw_translation = RawTranslationArtifact(
                        text=translation.text,
                        author=getattr(translation, "author", "") or metadata_author,
                    )
                    branch.status.raw_translation = TaskStatus(status=StatusEnum.FINISHED)
                f.write(record.model_dump_json() + "\n")

        print(f"shard: {metadata_jsonl_path.name} -> {output_path.name}")
        print("  - records: ", {len(metadata_list)})
        print("  - initialized_transcripts: ", len(transcriptions_by_uid))
        print("  - initialized_translation_targets: ", len(translations_by_target))
        print()


if __name__ == "__main__":
    main()