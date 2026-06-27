"""Load final dataset JSONL files into simple LLM training examples.

This module consumes the final dataset layout produced by pipeline 9.  It is
intentionally independent from ``pipeline.*`` cache/state internals: training
data is built from final ``core.schema`` dataset records only.
"""

from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from configs.config import Config
from core.build_conversation import (
    build_asr_blocks,
    build_conservative_translation_blocks,
    build_fixed_window_translation_blocks,
    build_translation_blocks,
    count_max_empty_translation_windows,
)
from core.schema import MetaData, Transcription, Translation


TaskName = Literal["asr", "translation"]
TranslationMode = Literal["natural", "fixed_window", "conservative"]
TranslationTaskName = Literal["natural", "fixed_window", "conservative"]
TranslationTaskConfig = dict[str, dict[str, float | int | None]]
DatasetSplitName = Literal["train", "validate", "test"]
MetadataSplitKey = tuple[str, str]


@dataclass(frozen=True)
class LoadedTranslation:
    """A translation row plus languages derived from the dataset path."""

    source_language: str
    target_language: str
    translation: Translation


@dataclass(frozen=True)
class TrainingExample:
    """One LLM training example with causal streaming release arrays."""

    task: TaskName
    uid: str
    source_language: str
    target_language: str | None
    # Real maximum consecutive wait-window count observed in ``blocks``.
    # This is not necessarily the requested ``build_training_dataset(...)``
    # cadence input: e.g. requested ``tolerance_window=0`` means immediate
    # emission when ready, and the resulting real wait budget can be 0 or larger
    # depending on the source/target mapping evidence.
    tolerance_window: int
    audio_path: str
    src_outputs: list[str]
    translation_mode: TranslationMode | None = None
    min_wait_window: int | None = None
    tgt_outputs: list[str] | None = None

    @property
    def blocks(self) -> list[str]:
        """Backward-compatible combined assistant blocks."""

        if self.task == "asr":
            return list(self.src_outputs)
        if self.tgt_outputs is None:
            raise ValueError(f"Translation example {self.uid} has no target outputs")
        if len(self.src_outputs) != len(self.tgt_outputs):
            raise ValueError(
                f"Translation example {self.uid} has mismatched source/target outputs: "
                f"src={len(self.src_outputs)}, tgt={len(self.tgt_outputs)}"
            )
        return _combine_translation_blocks(self.src_outputs, self.tgt_outputs)


@dataclass(frozen=True)
class TrainingDatasetSplits:
    """Deterministically sampled train/validate/test examples."""

    train: list[TrainingExample]
    validate: list[TrainingExample]
    test: list[TrainingExample]




@dataclass(frozen=True)
class _TranslationSourceRecord:
    """One translation-capable final-dataset row before training task/window sampling."""

    uid: str
    source_language: str
    target_language: str
    metadata: MetaData
    transcription: Transcription
    translation: Translation
    audio_path: str


@dataclass(frozen=True)
class _BaseTrainingRecord:
    """One selected translation-capable record before task conversion."""

    uid: str
    source_language: str
    target_language: str
    translation_mode: TranslationMode
    min_wait_window: int | None
    tolerance_window: int
    audio_path: str
    asr_blocks: list[str]
    translation_blocks: list[str]


def _read_jsonl(path: Path) -> list[dict]:
    items: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def load_metadata(dataset_root: str | Path) -> dict[tuple[str, str], MetaData]:
    """Load original metadata rows keyed by ``(source_language, uid)``."""

    root = Path(dataset_root)
    loaded: dict[tuple[str, str], MetaData] = {}
    metadata_root = root / "metadata"
    if not metadata_root.exists():
        return loaded
    for jsonl_path in sorted(metadata_root.glob("*/*.jsonl")):
        source_language = jsonl_path.parent.name
        for item in _read_jsonl(jsonl_path):
            metadata = MetaData.model_validate(item)
            key = (source_language, metadata.uid)
            if key in loaded:
                raise ValueError(f"Duplicate metadata row for source_language={source_language}, uid={metadata.uid}")
            loaded[key] = metadata
    return loaded


def _audio_path_from_metadata(dataset_root: str | Path, source_language: str, metadata: MetaData) -> str:
    if not metadata.file_name:
        raise ValueError(f"Cannot resolve audio path for {metadata.uid}: metadata.file_name is empty")
    return str(Path(dataset_root) / "audio" / source_language / metadata.file_name)


def _target_language_from_translation_path(path: Path, source_language: str) -> str:
    pattern = rf"^translation-{re.escape(source_language)}_([^-]+)-part.+\.jsonl$"
    match = re.match(pattern, path.name)
    if not match:
        raise ValueError(f"Cannot derive target language from translation path: {path}")
    return match.group(1)


def _language_name(language_code: str) -> str:
    if language_code not in Config.lang_code2name:
        raise ValueError(f"Unsupported language code: {language_code}")
    return Config.lang_code2name[language_code]


def load_transcriptions(dataset_root: str | Path) -> dict[tuple[str, str], Transcription]:
    """Load final transcription rows keyed by ``(source_language, uid)``."""

    root = Path(dataset_root)
    loaded: dict[tuple[str, str], Transcription] = {}
    for jsonl_path in sorted((root / "transcription").glob("*/*.jsonl")):
        source_language = jsonl_path.parent.name
        for item in _read_jsonl(jsonl_path):
            transcription = Transcription.model_validate(item)
            key = (source_language, transcription.uid)
            if key in loaded:
                raise ValueError(f"Duplicate transcription row for source_language={source_language}, uid={transcription.uid}")
            loaded[key] = transcription
    return loaded


def load_translations(dataset_root: str | Path) -> list[LoadedTranslation]:
    """Load final translation rows with source/target languages from paths."""

    root = Path(dataset_root)
    loaded: list[LoadedTranslation] = []
    seen: set[tuple[str, str, str]] = set()
    for jsonl_path in sorted((root / "translation").glob("*/*.jsonl")):
        source_language = jsonl_path.parent.name
        target_language = _target_language_from_translation_path(jsonl_path, source_language)
        for item in _read_jsonl(jsonl_path):
            item.pop("source_language", None)
            translation = Translation.model_validate(item)
            key = (source_language, target_language, translation.uid)
            if key in seen:
                raise ValueError(
                    "Duplicate translation row for "
                    f"source_language={source_language}, target_language={target_language}, uid={translation.uid}"
                )
            seen.add(key)
            loaded.append(
                LoadedTranslation(
                    source_language=source_language,
                    target_language=target_language,
                    translation=translation,
                )
            )
    return loaded


def _effective_build_tolerance_window(
    *,
    real_max_tolerance_window: int,
    requested_tolerance_window: int,
) -> int:
    if real_max_tolerance_window < 0:
        raise ValueError(f"real_max_tolerance_window must be non-negative: {real_max_tolerance_window}")
    if requested_tolerance_window < 0:
        raise ValueError(f"requested_tolerance_window must be non-negative: {requested_tolerance_window}")
    return max(real_max_tolerance_window, requested_tolerance_window)


def _combine_translation_blocks(asr_blocks: list[str], translation_blocks: list[str]) -> list[str]:
    if len(asr_blocks) != len(translation_blocks):
        raise ValueError(
            "Cannot combine ASR and translation blocks with different lengths: "
            f"asr={len(asr_blocks)}, translation={len(translation_blocks)}"
        )
    return [f"{asr_block}{translation_block}" for asr_block, translation_block in zip(asr_blocks, translation_blocks)]


def _counts_from_ratio(total: int, ratio: tuple[float, ...]) -> list[int]:
    if total < 0:
        raise ValueError("total must be non-negative")
    if not ratio:
        raise ValueError("ratio must not be empty")
    if any(value < 0 for value in ratio):
        raise ValueError(f"ratio values must be non-negative: {ratio}")
    ratio_sum = sum(ratio)
    if ratio_sum <= 0:
        raise ValueError(f"ratio sum must be positive: {ratio}")

    raw_counts = [total * value / ratio_sum for value in ratio]
    counts = [int(value) for value in raw_counts]
    remaining = total - sum(counts)
    remainders = sorted(
        enumerate(value - int(value) for value in raw_counts),
        key=lambda item: (-item[1], item[0]),
    )
    for idx, _ in remainders[:remaining]:
        counts[idx] += 1
    return counts


def _sample_examples(
    rng: random.Random,
    examples: list[_TranslationSourceRecord],
    count: int,
) -> list[_TranslationSourceRecord]:
    if count == 0:
        return []
    if not examples:
        raise ValueError("Cannot sample requested examples from an empty task pool")
    if count <= len(examples):
        return rng.sample(examples, count)
    return [rng.choice(examples) for _ in range(count)]


def _metadata_split_key(source_record: _TranslationSourceRecord) -> MetadataSplitKey:
    return (source_record.source_language, source_record.uid)


def _group_source_records_by_metadata(
    source_records: list[_TranslationSourceRecord],
) -> list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]]:
    grouped: dict[MetadataSplitKey, list[_TranslationSourceRecord]] = {}
    for source_record in source_records:
        grouped.setdefault(_metadata_split_key(source_record), []).append(source_record)
    return list(grouped.items())


def _flatten_source_record_groups(
    groups: list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]],
) -> list[_TranslationSourceRecord]:
    return [source_record for _, records in groups for source_record in records]


def _sorted_source_records_for_sampling(
    records: list[_TranslationSourceRecord],
) -> list[_TranslationSourceRecord]:
    return sorted(records, key=lambda record: record.target_language)


def _sample_source_record_groups(
    rng: random.Random,
    groups: list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]],
    count: int,
) -> list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]]:
    if count == 0:
        return []
    if not groups:
        raise ValueError("Cannot sample requested metadata groups from an empty task pool")
    if count <= len(groups):
        return rng.sample(groups, count)
    return [rng.choice(groups) for _ in range(count)]


def _split_source_record_groups(
    groups: list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]],
    split_ratio: tuple[float, float, float],
) -> dict[DatasetSplitName, list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]]]:
    train_count, validate_count, test_count = _counts_from_ratio(len(groups), split_ratio)
    train_end = train_count
    validate_end = train_end + validate_count
    test_end = validate_end + test_count
    return {
        "train": groups[:train_end],
        "validate": groups[train_end:validate_end],
        "test": groups[validate_end:test_end],
    }


def _metadata_key_to_json(key: MetadataSplitKey) -> dict[str, str]:
    source_language_code, uid = key
    return {
        "source_language": _language_name(source_language_code),
        "source_language_code": source_language_code,
        "uid": uid,
    }


def _metadata_key_from_json(item: Any) -> MetadataSplitKey:
    if not isinstance(item, dict):
        raise ValueError(f"Split manifest entry must be an object: {item!r}")
    source_language = item.get("source_language")
    source_language_code = item.get("source_language_code")
    uid = item.get("uid")
    if not isinstance(source_language, str) or not isinstance(source_language_code, str) or not isinstance(uid, str):
        raise ValueError(
            "Split manifest entry requires string source_language, source_language_code, and uid: "
            f"{item!r}"
        )
    expected_language = _language_name(source_language_code)
    if source_language != expected_language:
        raise ValueError(
            "Split manifest source_language must match Config.lang_code2name[source_language_code]: "
            f"source_language={source_language!r}, source_language_code={source_language_code!r}, "
            f"expected={expected_language!r}"
        )
    return (source_language_code, uid)


def build_dataset_split_manifest(
    dataset_root: str | Path,
    *,
    total_samples: int | None = None,
    split_ratio: tuple[float, float, float] = (8, 1.5, 0.5),
    seed: int = 4021,
) -> dict[str, Any]:
    """Build a reusable metadata/audio-level train/validate/test split manifest."""

    if len(split_ratio) != 3:
        raise ValueError(f"split_ratio must be (train, validate, test), got: {split_ratio}")
    rng = random.Random(seed)
    source_records = _build_translation_source_records(dataset_root)
    groups = _group_source_records_by_metadata(source_records)
    requested_total_samples: int | str = "all" if total_samples is None else int(total_samples)
    sample_count = len(groups) if total_samples is None else min(total_samples, len(groups))
    sampled_groups = _sample_source_record_groups(rng, groups, sample_count)
    rng.shuffle(sampled_groups)
    split_groups = _split_source_record_groups(sampled_groups, split_ratio)

    splits = {
        split_name: [_metadata_key_to_json(key) for key, _ in split_groups[split_name]]
        for split_name in ("train", "validate", "test")
    }
    row_counts = {
        split_name: sum(len(records) for _, records in split_groups[split_name])
        for split_name in ("train", "validate", "test")
    }
    group_counts = {
        split_name: len(split_groups[split_name])
        for split_name in ("train", "validate", "test")
    }
    return {
        "dataset_root": str(dataset_root),
        "sampling": {
            "requested_total_samples": requested_total_samples,
            "total_samples": sample_count,
            "seed": seed,
            "split_ratio": list(split_ratio),
        },
        "splits": splits,
        "counts": {
            "metadata_group_count": group_counts,
            "translation_row_count": row_counts,
        },
    }


def write_dataset_split_manifest(
    output_path: str | Path,
    dataset_root: str | Path,
    *,
    total_samples: int | None = None,
    split_ratio: tuple[float, float, float] = (8, 1.5, 0.5),
    seed: int = 4021,
) -> dict[str, Any]:
    """Write a reusable metadata/audio-level split manifest and return its payload."""

    payload = build_dataset_split_manifest(
        dataset_root,
        total_samples=total_samples,
        split_ratio=split_ratio,
        seed=seed,
    )
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def load_dataset_split_manifest(split_manifest_path: str | Path) -> dict[str, Any]:
    payload = json.loads(Path(split_manifest_path).read_text(encoding="utf-8"))
    dataset_root = payload.get("dataset_root")
    if not isinstance(dataset_root, str) or not dataset_root:
        raise ValueError("Split manifest requires non-empty dataset_root")
    splits = payload.get("splits")
    if not isinstance(splits, dict):
        raise ValueError("Split manifest requires splits object")
    for split_name in ("train", "validate", "test"):
        if split_name not in splits or not isinstance(splits[split_name], list):
            raise ValueError(f"Split manifest requires splits.{split_name} list")
        seen: set[MetadataSplitKey] = set()
        for item in splits[split_name]:
            key = _metadata_key_from_json(item)
            if key in seen:
                raise ValueError(f"Duplicate metadata key in manifest split {split_name}: {key}")
            seen.add(key)
    return payload


def _source_record_groups_from_manifest(
    source_records: list[_TranslationSourceRecord],
    manifest: dict[str, Any],
) -> dict[DatasetSplitName, list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]]]:
    available = dict(_group_source_records_by_metadata(source_records))
    used: dict[MetadataSplitKey, str] = {}
    split_groups: dict[DatasetSplitName, list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]]] = {
        "train": [],
        "validate": [],
        "test": [],
    }
    for split_name in ("train", "validate", "test"):
        for item in manifest["splits"][split_name]:
            key = _metadata_key_from_json(item)
            if key in used:
                raise ValueError(
                    f"Split manifest metadata key appears in both {used[key]} and {split_name}: {key}"
                )
            if key not in available:
                raise ValueError(f"Split manifest key not found in dataset: {key}")
            used[key] = split_name
            split_groups[split_name].append((key, available[key]))
    return split_groups


def _validate_translation_task_config(config: TranslationTaskConfig) -> None:
    expected = {"natural", "fixed_window", "conservative"}
    unknown = set(config) - expected
    if unknown:
        raise ValueError(f"Unsupported translation task config keys: {sorted(unknown)}")
    for name in expected:
        if name not in config:
            raise ValueError(f"Missing translation task config section: {name}")
        ratio = config[name].get("ratio")
        if ratio is None:
            raise ValueError(f"translation task {name!r} requires an explicit ratio")
        if float(ratio) < 0:
            raise ValueError(f"translation task {name!r} ratio must be non-negative: {ratio}")
    ratio_sum = sum(float(config[name]["ratio"]) for name in expected)
    if ratio_sum <= 0:
        raise ValueError("At least one translation task ratio must be positive")
    for name in ("fixed_window", "conservative"):
        min_value = config[name].get("min")
        max_value = config[name].get("max")
        if min_value is not None and int(min_value) < 0:
            raise ValueError(f"{name}.min must be non-negative or None: {min_value}")
        if max_value is not None and int(max_value) < 0:
            raise ValueError(f"{name}.max must be non-negative or None: {max_value}")
        if min_value is not None and max_value is not None and int(min_value) > int(max_value):
            raise ValueError(f"{name}.min must be <= max: min={min_value}, max={max_value}")


def _translation_task_labels(config: TranslationTaskConfig, count: int) -> list[TranslationTaskName]:
    names: tuple[TranslationTaskName, ...] = ("natural", "fixed_window", "conservative")
    ratios = tuple(float(config[name]["ratio"]) for name in names)
    counts = _counts_from_ratio(count, ratios)
    labels: list[TranslationTaskName] = []
    for name, name_count in zip(names, counts):
        labels.extend([name] * name_count)
    return labels


def _window_bounds_for_record(
    *,
    config: dict[str, float | int | None],
    max_request_window: int,
    mode: TranslationTaskName,
) -> tuple[int, int]:
    if max_request_window < 0:
        raise ValueError(f"max_request_window must be non-negative: {max_request_window}")
    configured_min = config.get("min")
    configured_max = config.get("max")
    lower = 1 if configured_min is None else int(configured_min)
    upper = max_request_window if configured_max is None else min(int(configured_max), max_request_window)
    if lower > upper:
        raise ValueError(
            f"No valid {mode} requested window for record max_request_window={max_request_window}: "
            f"min={configured_min}, max={configured_max}."
        )
    return lower, upper


def _sample_window_from_config(
    rng: random.Random,
    *,
    config: dict[str, float | int | None],
    max_request_window: int,
    mode: TranslationTaskName,
) -> int:
    lower, upper = _window_bounds_for_record(config=config, max_request_window=max_request_window, mode=mode)
    return rng.randint(lower, upper)


def _max_request_window_for_source_record(source_record: _TranslationSourceRecord) -> int:
    """Return the largest requested wait-window interval this record can carry.

    ``Translation.max_empty_window`` describes the maximum wait already present in
    natural/evidence-ready translation blocks.  Fixed-window and conservative
    training modes are allowed to introduce artificial waits, so sampling must be
    bounded by the number of available source windows instead.
    """

    asr_blocks = build_asr_blocks(source_record.metadata, source_record.transcription)
    return max(0, len(asr_blocks) - 1)


def _build_translation_source_records(dataset_root: str | Path) -> list[_TranslationSourceRecord]:
    transcriptions = load_transcriptions(dataset_root)
    metadata_by_key = load_metadata(dataset_root)
    source_records: list[_TranslationSourceRecord] = []

    for loaded_translation in load_translations(dataset_root):
        key = (loaded_translation.source_language, loaded_translation.translation.uid)
        if key not in transcriptions:
            raise ValueError(
                "Missing transcription for translation row: "
                f"source_language={loaded_translation.source_language}, uid={loaded_translation.translation.uid}"
            )
        transcription = transcriptions[key]
        if key not in metadata_by_key:
            raise ValueError(
                "Missing metadata for translation row: "
                f"source_language={loaded_translation.source_language}, uid={loaded_translation.translation.uid}"
            )
        metadata = metadata_by_key[key]
        audio_path = _audio_path_from_metadata(dataset_root, loaded_translation.source_language, metadata)
        source_records.append(
            _TranslationSourceRecord(
                uid=loaded_translation.translation.uid,
                source_language=loaded_translation.source_language,
                target_language=loaded_translation.target_language,
                metadata=metadata,
                transcription=transcription,
                translation=loaded_translation.translation,
                audio_path=audio_path,
            )
        )
    return source_records


def _source_record_to_base_training_record(
    source_record: _TranslationSourceRecord,
    *,
    translation_mode: TranslationMode,
    requested_window: int | None,
) -> _BaseTrainingRecord:
    if translation_mode == "natural":
        min_wait_window = None
        translation_blocks = build_translation_blocks(
            source_record.metadata,
            source_record.transcription,
            source_record.translation,
        )
    elif translation_mode == "conservative":
        if requested_window is None:
            raise ValueError("Conservative translation requires requested_window")
        min_wait_window = requested_window
        translation_blocks = build_conservative_translation_blocks(
            source_record.metadata,
            source_record.transcription,
            source_record.translation,
            min_wait_window=min_wait_window,
        )
    elif translation_mode == "fixed_window":
        if requested_window is None:
            raise ValueError("Fixed-window translation requires requested_window")
        min_wait_window = None
        effective_tolerance_window = _effective_build_tolerance_window(
            real_max_tolerance_window=source_record.translation.max_empty_window,
            requested_tolerance_window=requested_window,
        )
        translation_blocks = build_fixed_window_translation_blocks(
            source_record.metadata,
            source_record.transcription,
            source_record.translation,
            tolerance_window=effective_tolerance_window,
        )
    else:
        raise ValueError(f"Unsupported translation_mode: {translation_mode}")

    real_tolerance_window = count_max_empty_translation_windows(translation_blocks)
    return _BaseTrainingRecord(
        uid=source_record.uid,
        source_language=_language_name(source_record.source_language),
        target_language=_language_name(source_record.target_language),
        translation_mode=translation_mode,
        min_wait_window=min_wait_window,
        tolerance_window=real_tolerance_window,
        audio_path=source_record.audio_path,
        asr_blocks=build_asr_blocks(source_record.metadata, source_record.transcription),
        translation_blocks=translation_blocks,
    )


def _build_sampled_training_record(
    rng: random.Random,
    source_record: _TranslationSourceRecord,
    *,
    translation_mode: TranslationTaskName,
    translation_task_config: TranslationTaskConfig,
) -> _BaseTrainingRecord:
    if translation_mode == "natural":
        requested_window = None
    else:
        requested_window = _sample_window_from_config(
            rng,
            config=translation_task_config[translation_mode],
            max_request_window=_max_request_window_for_source_record(source_record),
            mode=translation_mode,
        )
        if requested_window == 0:
            translation_mode = "natural"
            requested_window = None
    return _source_record_to_base_training_record(
        source_record,
        translation_mode=translation_mode,
        requested_window=requested_window,
    )


def _base_record_to_training_example(
    base_record: _BaseTrainingRecord,
    task: TaskName,
    *,
    max_window_size: int,
) -> TrainingExample:
    def limit_windows(outputs: list[str]) -> list[str]:
        if max_window_size == -1:
            return list(outputs)
        if max_window_size == 0:
            raise ValueError("max_window_size must not be 0; use -1 for all windows or a positive limit")
        if max_window_size < -1:
            raise ValueError(f"max_window_size must be -1 or positive: {max_window_size}")
        return list(outputs[:max_window_size])

    if task == "asr":
        return TrainingExample(
            task="asr",
            uid=base_record.uid,
            source_language=base_record.source_language,
            target_language=None,
            translation_mode=None,
            min_wait_window=None,
            tolerance_window=base_record.tolerance_window,
            audio_path=base_record.audio_path,
            src_outputs=limit_windows(base_record.asr_blocks),
            tgt_outputs=None,
        )
    src_outputs = limit_windows(base_record.asr_blocks)
    tgt_outputs = limit_windows(base_record.translation_blocks)
    return TrainingExample(
        task="translation",
        uid=base_record.uid,
        source_language=base_record.source_language,
        target_language=base_record.target_language,
        translation_mode=base_record.translation_mode,
        min_wait_window=base_record.min_wait_window,
        tolerance_window=base_record.tolerance_window,
        audio_path=base_record.audio_path,
        src_outputs=src_outputs,
        tgt_outputs=tgt_outputs,
    )


def _build_asr_examples_from_source_record_groups(
    source_record_groups: list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]],
    *,
    max_window_size: int,
) -> list[TrainingExample]:
    """Build one ASR example per metadata/audio UID group."""

    asr_examples: list[TrainingExample] = []
    for group_key, group_source_records in source_record_groups:
        source_records = _sorted_source_records_for_sampling(group_source_records)
        if not source_records:
            raise ValueError(f"Metadata group has no source records: {group_key}")
        base_record = _source_record_to_base_training_record(
            source_records[0],
            translation_mode="natural",
            requested_window=None,
        )
        asr_examples.append(_base_record_to_training_example(base_record, "asr", max_window_size=max_window_size))
    return asr_examples


def _build_translation_examples_from_source_records(
    rng: random.Random,
    source_records: list[_TranslationSourceRecord],
    *,
    translation_task_config: TranslationTaskConfig,
    max_window_size: int,
) -> list[TrainingExample]:
    """Assign translation styles/windows over translation-row occurrences."""

    sample_count = len(source_records)
    if sample_count == 0:
        return []

    translation_labels = _translation_task_labels(translation_task_config, sample_count)
    rng.shuffle(translation_labels)

    examples: list[TrainingExample] = []
    for source_record, translation_subtask in zip(source_records, translation_labels):
        base_record = _build_sampled_training_record(
            rng,
            source_record,
            translation_mode=translation_subtask,
            translation_task_config=translation_task_config,
        )
        examples.append(_base_record_to_training_example(base_record, "translation", max_window_size=max_window_size))

    rng.shuffle(examples)
    return examples


def _build_eval_examples_from_source_record_groups(
    rng: random.Random,
    source_record_groups: list[tuple[MetadataSplitKey, list[_TranslationSourceRecord]]],
    *,
    translation_task_config: TranslationTaskConfig,
    max_window_size: int,
) -> list[TrainingExample]:
    """Build deterministic eval/test examples after metadata-level split."""

    if not source_record_groups:
        return []

    asr_examples = _build_asr_examples_from_source_record_groups(
        source_record_groups,
        max_window_size=max_window_size,
    )
    translation_source_records: list[_TranslationSourceRecord] = []
    for _, group_source_records in source_record_groups:
        translation_source_records.extend(_sorted_source_records_for_sampling(group_source_records))
    translation_examples = _build_translation_examples_from_source_records(
        rng,
        translation_source_records,
        translation_task_config=translation_task_config,
        max_window_size=max_window_size,
    )

    examples = asr_examples + translation_examples
    rng.shuffle(examples)
    return examples


def build_training_dataset(
    dataset_root: str | Path,
    *,
    total_samples: int | None = None,
    max_window_size: int = -1,
    task_ratio: tuple[float, float] = (9, 1),
    split_ratio: tuple[float, float, float] = (8, 1.5, 0.5),
    translation_task_config: TranslationTaskConfig,
    dataset_repeat: int = 1,
    seed: int = 4021,
    split_manifest_path: str | Path | None = None,
) -> TrainingDatasetSplits:
    """Build train/validate/test splits from metadata/audio-level groups.

    ``max_window_size`` controls how many streaming windows are kept per training
    example.  ``-1`` keeps all windows, ``0`` is invalid, and positive values keep
    the first N windows.  Processor-level truncation must not be used for this.

    Train ASR examples use split-local metadata/audio UID groups as the sample
    base: one ASR example is built per UID.  Train translation examples use
    split-local translation rows as the sample base, and those rows are repeated
    by ``dataset_repeat`` before translation style/window sampling.
    ``task_ratio`` is accepted for compatibility but does not control example
    counts.

    Validation/test examples are evaluation sets, not training samples: each
    metadata/audio UID contributes one ASR example, and each target-language
    translation row contributes one translation example.  Translation styles are
    balanced across those translation rows with ``translation_task_config``.
    ``fixed_window`` / ``conservative`` additionally accept explicit ``min`` /
    ``max`` window bounds.  ``None`` lower bounds mean ``1`` by default, so
    zero-window training/evaluation is included only when ``min`` is explicitly
    set to ``0``.

    Split membership is always decided by metadata/audio key
    ``(source_language, uid)`` before flattening back to translation rows.  This
    keeps all target-language rows for the same audio file in the same split.
    When ``split_manifest_path`` is provided, the manifest's dataset root and
    split membership are used instead of ``dataset_root`` / ``total_samples`` /
    ``split_ratio`` / ``seed``.

    ``dataset_repeat`` repeats only the selected train translation rows.
    Validation/test examples are built before the repeated train examples, so
    train-side repetition cannot change validation/test style labels, sampled
    translation windows, or final example order.  No ``**kwargs`` are used: all
    sampling controls are explicit parameters.
    """

    if len(task_ratio) != 2:
        raise ValueError(f"task_ratio must be (translation, asr), got: {task_ratio}")
    if len(split_ratio) != 3:
        raise ValueError(f"split_ratio must be (train, validate, test), got: {split_ratio}")
    if dataset_repeat < 1:
        raise ValueError(f"dataset_repeat must be >= 1: {dataset_repeat}")
    if max_window_size == 0:
        raise ValueError("max_window_size must not be 0; use -1 for all windows or a positive limit")
    if max_window_size < -1:
        raise ValueError(f"max_window_size must be -1 or positive: {max_window_size}")

    rng = random.Random(seed)
    _validate_translation_task_config(translation_task_config)
    if split_manifest_path is None:
        source_records = _build_translation_source_records(dataset_root)
        groups = _group_source_records_by_metadata(source_records)
        base_sample_count = len(groups) if total_samples is None else min(total_samples, len(groups))
        sampled_groups = _sample_source_record_groups(rng, groups, base_sample_count)
        rng.shuffle(sampled_groups)
        split_groups = _split_source_record_groups(sampled_groups, split_ratio)
    else:
        split_manifest = load_dataset_split_manifest(split_manifest_path)
        source_records = _build_translation_source_records(split_manifest["dataset_root"])
        split_groups = _source_record_groups_from_manifest(source_records, split_manifest)

    train_source_records = _flatten_source_record_groups(split_groups["train"]) * dataset_repeat
    train_asr_source_record_groups = split_groups["train"]
    validate_source_record_groups = split_groups["validate"]
    test_source_record_groups = split_groups["test"]

    validate_examples = _build_eval_examples_from_source_record_groups(
        rng,
        validate_source_record_groups,
        translation_task_config=translation_task_config,
        max_window_size=max_window_size,
    )
    test_examples = _build_eval_examples_from_source_record_groups(
        rng,
        test_source_record_groups,
        translation_task_config=translation_task_config,
        max_window_size=max_window_size,
    )
    train_asr_examples = _build_asr_examples_from_source_record_groups(
        train_asr_source_record_groups,
        max_window_size=max_window_size,
    )
    train_translation_examples = _build_translation_examples_from_source_records(
        rng,
        train_source_records,
        translation_task_config=translation_task_config,
        max_window_size=max_window_size,
    )
    train_examples = train_asr_examples + train_translation_examples
    rng.shuffle(train_examples)

    return TrainingDatasetSplits(
        train=train_examples,
        validate=validate_examples,
        test=test_examples,
    )
