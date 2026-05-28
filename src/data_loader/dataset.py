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
from core.build_conversation import build_asr_blocks, build_translation_blocks
from core.schema import MetaData, Transcription, Translation


TaskName = Literal["asr", "translation"]


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
class _BaseTrainingRecord:
    """One selected translation-capable record before task conversion."""

    uid: str
    source_language: str
    target_language: str
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


def _sample_tolerance(
    rng: random.Random,
    *,
    max_empty_window: int,
    tolerance_window: int | None,
) -> int:
    if tolerance_window is not None:
        if tolerance_window < 0:
            raise ValueError(f"tolerance_window must be non-negative or None: {tolerance_window}")
        return tolerance_window

    upper = max_empty_window - 1
    return rng.randint(0, max(0, upper))


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


def _count_real_wait_windows(translation_blocks: list[str]) -> int:
    max_empty_window_count = 0
    current_empty_window_count = 0
    for block in translation_blocks:
        if "<tgt><|wait|></tgt>" in block:
            current_empty_window_count += 1
        else:
            max_empty_window_count = max(max_empty_window_count, current_empty_window_count)
            current_empty_window_count = 0
    return max(max_empty_window_count, current_empty_window_count)


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
    examples: list[_BaseTrainingRecord],
    count: int,
) -> list[_BaseTrainingRecord]:
    if count == 0:
        return []
    if not examples:
        raise ValueError("Cannot sample requested examples from an empty task pool")
    if count <= len(examples):
        return rng.sample(examples, count)
    return [rng.choice(examples) for _ in range(count)]


def _build_base_training_records(
    dataset_root: str | Path,
    *,
    tolerance_window: int | None = None,
    seed: int = 4021,
) -> list[_BaseTrainingRecord]:
    """Build translation-capable base records from final dataset files.

    Final dataset rows currently store canonical transcription/translation schema,
    not materialized training ``src_outputs`` / ``tgt_outputs`` arrays.  Therefore
    this function performs the narrow final-schema -> training-release-array
    conversion at the data-loader boundary.  Trainer code must consume the
    resulting arrays and must not rebuild release logic.
    """

    rng = random.Random(seed)
    transcriptions = load_transcriptions(dataset_root)
    metadata_by_key = load_metadata(dataset_root)
    base_records: list[_BaseTrainingRecord] = []
    configured_tolerance_window = tolerance_window

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
        requested_tolerance_window = _sample_tolerance(
            rng,
            max_empty_window=loaded_translation.translation.max_empty_window,
            tolerance_window=configured_tolerance_window,
        )
        effective_tolerance_window = _effective_build_tolerance_window(
            real_max_tolerance_window=loaded_translation.translation.max_empty_window,
            requested_tolerance_window=requested_tolerance_window,
        )
        translation_blocks, real_tolerance_window = build_translation_blocks(
            metadata,
            transcription,
            loaded_translation.translation,
            tolerance_window=effective_tolerance_window,
        )
        observed_real_tolerance_window = _count_real_wait_windows(translation_blocks)
        if real_tolerance_window != observed_real_tolerance_window:
            raise ValueError(
                "build_translation_blocks returned inconsistent wait-window count: "
                f"returned={real_tolerance_window}, observed={observed_real_tolerance_window}"
            )
        base_records.append(
            _BaseTrainingRecord(
                uid=loaded_translation.translation.uid,
                source_language=_language_name(loaded_translation.source_language),
                target_language=_language_name(loaded_translation.target_language),
                tolerance_window=real_tolerance_window,
                audio_path=audio_path,
                asr_blocks=build_asr_blocks(metadata, transcription),
                translation_blocks=translation_blocks,
            )
        )

    return base_records


def _base_record_to_training_example(base_record: _BaseTrainingRecord, task: TaskName) -> TrainingExample:
    if task == "asr":
        return TrainingExample(
            task="asr",
            uid=base_record.uid,
            source_language=base_record.source_language,
            target_language=None,
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
        tolerance_window=base_record.tolerance_window,
        audio_path=base_record.audio_path,
        src_outputs=base_record.asr_blocks,
        tgt_outputs=base_record.translation_blocks,
    )


def build_training_dataset(
    dataset_root: str | Path,
    *,
    total_samples: int | None = None,
    task_ratio: tuple[float, float] = (9, 1),
    split_ratio: tuple[float, float, float] = (8, 1.5, 0.5),
    tolerance_window: int | None = None,
    seed: int = 4021,
) -> TrainingDatasetSplits:
    """Build fixed-size train/validate/test splits from translation base records.

    ``task_ratio`` is ``(translation, asr)``.  ASR examples are created by
    converting selected base translation records to source-only blocks; they are
    not added as extra samples.  Therefore the final sample count is always the
    selected translation-base count.  If ``total_samples`` is ``None``, all
    available translation records are used as the base set.

    ``tolerance_window`` and random tolerance augmentation are exclusive.  When
    ``tolerance_window`` is an integer, including ``0``, that exact value is used
    as the requested emission-cadence input.  When ``tolerance_window`` is
    ``None``, a random requested cadence is sampled from the exported real wait
    budget ``Translation.max_empty_window``.  Translation blocks are built with
    ``max(Translation.max_empty_window, requested_tolerance_window)`` so final
    outputs satisfy the exported real wait budget and any requested lower bound.
    The ``TrainingExample.tolerance_window`` stored on output is the real maximum
    consecutive wait-window count observed in the produced blocks, not merely
    the requested cadence input.  Therefore requested ``tolerance_window=0``
    means "translate immediately when ready" only when the exported real wait
    budget is also ``0``; otherwise the exported real budget controls block
    generation.
    """

    if len(task_ratio) != 2:
        raise ValueError(f"task_ratio must be (translation, asr), got: {task_ratio}")
    if len(split_ratio) != 3:
        raise ValueError(f"split_ratio must be (train, validate, test), got: {split_ratio}")

    rng = random.Random(seed)
    base_records = _build_base_training_records(
        dataset_root,
        tolerance_window=tolerance_window,
        seed=seed,
    )
    sample_count = len(base_records) if total_samples is None else total_samples
    sampled_base_records = _sample_examples(rng, base_records, sample_count)

    translation_count, asr_count = _counts_from_ratio(sample_count, task_ratio)
    task_labels: list[TaskName] = ["translation"] * translation_count + ["asr"] * asr_count
    rng.shuffle(task_labels)
    sampled_examples = [
        _base_record_to_training_example(base_record, task_label)
        for base_record, task_label in zip(sampled_base_records, task_labels)
    ]
    rng.shuffle(sampled_examples)

    train_count, validate_count, test_count = _counts_from_ratio(sample_count, split_ratio)
    train_end = train_count
    validate_end = train_end + validate_count
    test_end = validate_end + test_count

    return TrainingDatasetSplits(
        train=sampled_examples[:train_end],
        validate=sampled_examples[train_end:validate_end],
        test=sampled_examples[validate_end:test_end],
    )