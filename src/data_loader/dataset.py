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
from typing import Literal

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


def _metadata_from_transcription(source_language: str, transcription: Transcription) -> MetaData:
    if not transcription.tokens:
        raise ValueError(f"Cannot build metadata for {transcription.uid}: transcription has no tokens")
    duration = max(token.end for token in transcription.tokens)
    return MetaData(
        uid=transcription.uid,
        file_name="",
        duration=duration,
        sample_rate=0.0,
        language=source_language,
    )


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
    max_empty_window: int,
    mode: TranslationTaskName,
) -> tuple[int, int]:
    if max_empty_window < 0:
        raise ValueError(f"max_empty_window must be non-negative: {max_empty_window}")
    configured_min = config.get("min")
    configured_max = config.get("max")
    lower = 1 if configured_min is None else int(configured_min)
    upper = max_empty_window if configured_max is None else min(int(configured_max), max_empty_window)
    if lower > upper:
        raise ValueError(
            f"No valid {mode} window for record max_empty_window={max_empty_window}: "
            f"min={configured_min}, max={configured_max}. Use min=0 explicitly to allow zero-window sampling."
        )
    return lower, upper


def _sample_window_from_config(
    rng: random.Random,
    *,
    config: dict[str, float | int | None],
    max_empty_window: int,
    mode: TranslationTaskName,
) -> int:
    lower, upper = _window_bounds_for_record(config=config, max_empty_window=max_empty_window, mode=mode)
    return rng.randint(lower, upper)


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
        original_metadata = metadata_by_key.get(key)
        metadata = original_metadata or _metadata_from_transcription(loaded_translation.source_language, transcription)
        audio_path = _audio_path_from_metadata(dataset_root, loaded_translation.source_language, metadata) if original_metadata else str(
            Path(dataset_root) / "audio" / loaded_translation.source_language / f"{transcription.uid}.wav"
        )
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
            max_empty_window=source_record.translation.max_empty_window,
            mode=translation_mode,
        )
    return _source_record_to_base_training_record(
        source_record,
        translation_mode=translation_mode,
        requested_window=requested_window,
    )


def _base_record_to_training_example(base_record: _BaseTrainingRecord, task: TaskName) -> TrainingExample:
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
            src_outputs=base_record.asr_blocks,
            tgt_outputs=None,
        )
    return TrainingExample(
        task="translation",
        uid=base_record.uid,
        source_language=base_record.source_language,
        target_language=base_record.target_language,
        translation_mode=base_record.translation_mode,
        min_wait_window=base_record.min_wait_window,
        tolerance_window=base_record.tolerance_window,
        audio_path=base_record.audio_path,
        src_outputs=base_record.asr_blocks,
        tgt_outputs=base_record.translation_blocks,
    )


def _build_training_examples_from_source_records(
    rng: random.Random,
    source_records: list[_TranslationSourceRecord],
    *,
    task_ratio: tuple[float, float],
    translation_task_config: TranslationTaskConfig,
) -> list[TrainingExample]:
    """Assign task/subtask labels and convert selected source rows to examples."""

    sample_count = len(source_records)
    if sample_count == 0:
        return []

    translation_count, asr_count = _counts_from_ratio(sample_count, task_ratio)
    task_labels: list[TaskName] = ["translation"] * translation_count + ["asr"] * asr_count
    rng.shuffle(task_labels)
    translation_labels = _translation_task_labels(translation_task_config, translation_count)
    rng.shuffle(translation_labels)

    examples: list[TrainingExample] = []
    translation_label_idx = 0
    for source_record, task_label in zip(source_records, task_labels):
        if task_label == "asr":
            base_record = _source_record_to_base_training_record(
                source_record,
                translation_mode="natural",
                requested_window=None,
            )
            examples.append(_base_record_to_training_example(base_record, "asr"))
            continue
        translation_subtask = translation_labels[translation_label_idx]
        translation_label_idx += 1
        base_record = _build_sampled_training_record(
            rng,
            source_record,
            translation_mode=translation_subtask,
            translation_task_config=translation_task_config,
        )
        examples.append(_base_record_to_training_example(base_record, "translation"))

    rng.shuffle(examples)
    return examples


def build_training_dataset(
    dataset_root: str | Path,
    *,
    total_samples: int | None = None,
    task_ratio: tuple[float, float] = (9, 1),
    split_ratio: tuple[float, float, float] = (8, 1.5, 0.5),
    translation_task_config: TranslationTaskConfig,
    dataset_repeat: int = 1,
    seed: int = 4021,
) -> TrainingDatasetSplits:
    """Build fixed-size train/validate/test splits from translation base records.

    ``task_ratio`` is ``(translation, asr)`` and is one configuration group.
    ``translation_task_config`` is a separate group used only after a selected
    sample has been assigned to the ``translation`` task.  Its required keys are
    ``natural``, ``fixed_window``, and ``conservative``; their ``ratio`` values
    are normalized together.  ``fixed_window`` / ``conservative`` additionally
    accept explicit ``min`` / ``max`` window bounds.  ``None`` lower bounds mean
    ``1`` by default, so zero-window training is included only when ``min`` is
    explicitly set to ``0``.

    ``dataset_repeat`` repeats only the selected train source-record pool before
    assigning task labels / translation subtask labels, so the same final dataset
    row can appear in multiple training modes without duplicating validation or
    test samples.  No ``**kwargs`` are used: all sampling controls are explicit
    parameters.
    """

    if len(task_ratio) != 2:
        raise ValueError(f"task_ratio must be (translation, asr), got: {task_ratio}")
    if len(split_ratio) != 3:
        raise ValueError(f"split_ratio must be (train, validate, test), got: {split_ratio}")
    if dataset_repeat < 1:
        raise ValueError(f"dataset_repeat must be >= 1: {dataset_repeat}")

    rng = random.Random(seed)
    _validate_translation_task_config(translation_task_config)
    source_records = _build_translation_source_records(dataset_root)
    base_sample_count = len(source_records) if total_samples is None else min(total_samples, len(source_records))
    sampled_source_records = _sample_examples(rng, source_records, base_sample_count)
    rng.shuffle(sampled_source_records)

    train_count, validate_count, test_count = _counts_from_ratio(base_sample_count, split_ratio)
    train_end = train_count
    validate_end = train_end + validate_count
    test_end = validate_end + test_count

    train_source_records = sampled_source_records[:train_end] * dataset_repeat
    validate_source_records = sampled_source_records[train_end:validate_end]
    test_source_records = sampled_source_records[validate_end:test_end]

    return TrainingDatasetSplits(
        train=_build_training_examples_from_source_records(
            rng,
            train_source_records,
            task_ratio=task_ratio,
            translation_task_config=translation_task_config,
        ),
        validate=_build_training_examples_from_source_records(
            rng,
            validate_source_records,
            task_ratio=task_ratio,
            translation_task_config=translation_task_config,
        ),
        test=_build_training_examples_from_source_records(
            rng,
            test_source_records,
            task_ratio=task_ratio,
            translation_task_config=translation_task_config,
        ),
    )
