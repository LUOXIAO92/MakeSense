"""OpenAI-compatible real-rollout strict streaming evaluation.

This module intentionally stays outside ``src/train/tester.py``.  It evaluates a
deployed OpenAI-compatible endpoint (for example vLLM / llama.cpp / OpenAI-like
servers) and does not load local HF/PEFT models.
"""

from __future__ import annotations

import asyncio
import base64
import io
import json
import random
import time
import wave
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

import torch
from openai import APIConnectionError, APIStatusError, APITimeoutError, AsyncOpenAI, OpenAIError, RateLimitError

from configs.config import Config
from core.build_conversation import (
    build_asr_blocks,
    build_conservative_translation_blocks,
    build_fixed_window_translation_blocks,
    build_translation_blocks,
    count_max_empty_translation_windows,
)
from data_loader.dataset import TrainingExample
from data_loader.dataset import load_dataset_split_manifest, load_metadata, load_transcriptions, load_translations
from train.audio import audio_chunks_for_example
from train.formatting import ChatMessage, example_to_messages
from train.tester import (
    assistant_turn_indices,
    parse_protocol_output,
    protocol_field_is_wait,
    protocol_output_adherent,
)


AudioMessageFormat = Literal["input_audio", "audio_url"]
SplitName = Literal["validate", "test"]
RuntimeConditionMode = Literal["asr", "natural", "fixed_window", "conservative"]
MARKDOWN_METRICS_PLACEHOLDER = "<!-- RUNTIME_STRICT_METRICS_PLACEHOLDER -->"


@dataclass(frozen=True)
class StrictStyleSpec:
    """One runtime strict condition plus requested-window variants to evaluate."""

    mode: RuntimeConditionMode
    windows: tuple[int | None, ...] = (None,)


@dataclass(frozen=True)
class _ExpandedCondition:
    mode: RuntimeConditionMode
    requested_window: int | None

    @property
    def label(self) -> str:
        if self.mode == "asr":
            return "asr"
        if self.mode == "natural":
            return "natural"
        return f"{self.mode}_{'random' if self.requested_window is None else self.requested_window}"

    def to_json(self) -> dict[str, Any]:
        if self.mode == "asr":
            requested_window_label: int | str = "asr"
        elif self.mode == "natural":
            requested_window_label: int | str = "natural"
        else:
            requested_window_label = "random" if self.requested_window is None else self.requested_window
        return {
            "mode": self.mode,
            "requested_window": self.requested_window,
            "requested_window_label": requested_window_label,
        }


@dataclass(frozen=True)
class OpenAIStrictTestConfig:
    """Configuration for endpoint-based strict streaming tests."""

    dataset_root: str | Path
    model_name: str
    base_url: str
    api_key: str = "no-key"
    total_samples: int | None = None
    max_window_size: int = -1
    seed: int = 4021
    split_ratio: tuple[float, float, float] = (0.8975, 0.1, 0.0025)
    split_manifest_path: str | Path | None = None
    splits: tuple[SplitName, ...] = ("validate", "test")
    style_specs: tuple[StrictStyleSpec, ...] = (StrictStyleSpec("natural", (None,)),)
    test_record_count: int = -1
    concurrency: int = 1
    constrained_decoding: bool = False
    audio_sampling_rate: int = 16000
    audio_chunk_seconds: float = 1.0
    audio_message_format: AudioMessageFormat = "input_audio"
    max_tokens: int = 256
    temperature: float | None = None
    top_p: float | None = None
    extra_body: dict[str, Any] | None = None
    metrics_output_dir: str | Path | None = None
    markdown_output_dir: str | Path | None = None
    markdown_record_limit_per_condition: int = 100
    request_timeout: float | None = None

    def __post_init__(self) -> None:
        if int(self.concurrency) <= 0:
            raise ValueError("concurrency must be positive")
        if self.constrained_decoding:
            raise NotImplementedError(
                "constrained_decoding=True is reserved for future constrained decoding and is not implemented yet"
            )
        if int(self.test_record_count) < -1:
            raise ValueError("test_record_count must be -1, 0, or a positive integer")
        if int(self.markdown_record_limit_per_condition) < 0:
            raise ValueError("markdown_record_limit_per_condition must be non-negative")
        if len(self.split_ratio) != 3:
            raise ValueError(f"split_ratio must be (train, validate, test), got: {self.split_ratio}")
        if not self.splits:
            raise ValueError("At least one split must be selected")
        invalid_splits = set(self.splits) - {"validate", "test"}
        if invalid_splits:
            raise ValueError(f"Only validate/test splits are allowed for runtime strict test: {sorted(invalid_splits)}")


@dataclass
class _RuntimeRow:
    split: str
    example: Any
    messages: list[ChatMessage]
    requested_window: int | None
    max_empty_window: int
    target_metrics_included: bool
    target_metrics_filter_reason: str | None


@dataclass(frozen=True)
class _RuntimeSourceRecord:
    uid: str
    source_language: str
    target_language: str
    metadata: Any
    transcription: Any
    translation: Any
    audio_path: str


def _language_name(language_code: str) -> str:
    if language_code not in Config.lang_code2name:
        raise ValueError(f"Unsupported language code: {language_code}")
    return Config.lang_code2name[language_code]


def _audio_path_from_metadata(dataset_root: str | Path, source_language: str, metadata: Any) -> str:
    if not metadata.file_name:
        raise ValueError(f"Cannot resolve audio path for {metadata.uid}: metadata.file_name is empty")
    return str(Path(dataset_root) / "audio" / source_language / metadata.file_name)


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
    for index, _ in remainders[:remaining]:
        counts[index] += 1
    return counts


def _sample_records(
    rng: random.Random,
    records: list[_RuntimeSourceRecord],
    count: int,
) -> list[_RuntimeSourceRecord]:
    if count == 0:
        return []
    if not records:
        raise ValueError("Cannot sample requested examples from an empty task pool")
    if count <= len(records):
        return rng.sample(records, count)
    return [rng.choice(records) for _ in range(count)]


def _runtime_metadata_split_key(source_record: "_RuntimeSourceRecord") -> tuple[str, str]:
    return (source_record.source_language, source_record.uid)


def _group_runtime_records_by_metadata(
    source_records: list["_RuntimeSourceRecord"],
) -> list[tuple[tuple[str, str], list["_RuntimeSourceRecord"]]]:
    grouped: dict[tuple[str, str], list[_RuntimeSourceRecord]] = {}
    for source_record in source_records:
        grouped.setdefault(_runtime_metadata_split_key(source_record), []).append(source_record)
    return list(grouped.items())


def _flatten_runtime_record_groups(
    groups: list[tuple[tuple[str, str], list["_RuntimeSourceRecord"]]],
) -> list["_RuntimeSourceRecord"]:
    return [source_record for _, records in groups for source_record in records]


def _sample_runtime_record_groups(
    rng: random.Random,
    groups: list[tuple[tuple[str, str], list["_RuntimeSourceRecord"]]],
    count: int,
) -> list[tuple[tuple[str, str], list["_RuntimeSourceRecord"]]]:
    if count == 0:
        return []
    if not groups:
        raise ValueError("Cannot sample requested metadata groups from an empty task pool")
    if count <= len(groups):
        return rng.sample(groups, count)
    return [rng.choice(groups) for _ in range(count)]


def _runtime_groups_from_manifest(
    source_records: list["_RuntimeSourceRecord"],
    manifest: dict[str, Any],
) -> dict[str, list[tuple[tuple[str, str], list["_RuntimeSourceRecord"]]]]:
    available = dict(_group_runtime_records_by_metadata(source_records))
    used: dict[tuple[str, str], str] = {}
    split_groups: dict[str, list[tuple[tuple[str, str], list[_RuntimeSourceRecord]]]] = {
        "train": [],
        "validate": [],
        "test": [],
    }
    for split_name in ("train", "validate", "test"):
        for item in manifest["splits"][split_name]:
            key = (item["source_language_code"], item["uid"])
            if key in used:
                raise ValueError(
                    f"Split manifest metadata key appears in both {used[key]} and {split_name}: {key}"
                )
            if key not in available:
                raise ValueError(f"Split manifest key not found in dataset: {key}")
            used[key] = split_name
            split_groups[split_name].append((key, available[key]))
    return split_groups


def _build_runtime_source_records(dataset_root: str | Path) -> list[_RuntimeSourceRecord]:
    transcriptions = load_transcriptions(dataset_root)
    metadata_by_key = load_metadata(dataset_root)
    source_records: list[_RuntimeSourceRecord] = []
    for loaded_translation in load_translations(dataset_root):
        key = (loaded_translation.source_language, loaded_translation.translation.uid)
        if key not in transcriptions:
            raise ValueError(
                "Missing transcription for translation row: "
                f"source_language={loaded_translation.source_language}, uid={loaded_translation.translation.uid}"
            )
        if key not in metadata_by_key:
            raise ValueError(
                "Missing metadata for translation row: "
                f"source_language={loaded_translation.source_language}, uid={loaded_translation.translation.uid}"
            )
        metadata = metadata_by_key[key]
        source_records.append(
            _RuntimeSourceRecord(
                uid=loaded_translation.translation.uid,
                source_language=loaded_translation.source_language,
                target_language=loaded_translation.target_language,
                metadata=metadata,
                transcription=transcriptions[key],
                translation=loaded_translation.translation,
                audio_path=_audio_path_from_metadata(dataset_root, loaded_translation.source_language, metadata),
            )
        )
    return source_records


def _expand_conditions(style_specs: tuple[StrictStyleSpec, ...]) -> list[_ExpandedCondition]:
    conditions: list[_ExpandedCondition] = []
    for spec in style_specs:
        if spec.mode == "asr":
            for window in spec.windows:
                if window is not None:
                    raise ValueError("asr strict condition only supports window=None")
                conditions.append(_ExpandedCondition(mode="asr", requested_window=None))
            continue
        if spec.mode == "natural":
            for window in spec.windows:
                if window is not None:
                    raise ValueError("natural strict style only supports window=None")
                conditions.append(_ExpandedCondition(mode="natural", requested_window=None))
            continue
        for window in spec.windows:
            if window is not None and int(window) <= 0:
                raise ValueError(f"{spec.mode} requested window must be positive or None: {window}")
            conditions.append(
                _ExpandedCondition(
                    mode=spec.mode,
                    requested_window=None if window is None else int(window),
                )
            )
    if not conditions:
        raise ValueError("No strict style conditions were configured")
    return conditions


def _limit_windows(outputs: list[str], *, max_window_size: int) -> list[str]:
    if max_window_size == -1:
        return list(outputs)
    if max_window_size == 0:
        raise ValueError("max_window_size must not be 0; use -1 for all windows or a positive limit")
    if max_window_size < -1:
        raise ValueError(f"max_window_size must be -1 or positive: {max_window_size}")
    return list(outputs[:max_window_size])


def _runtime_source_records_by_split(config: OpenAIStrictTestConfig) -> dict[str, list[_RuntimeSourceRecord]]:
    rng = random.Random(config.seed)
    if config.split_manifest_path is None:
        source_records = _build_runtime_source_records(config.dataset_root)
        groups = _group_runtime_records_by_metadata(source_records)
        base_sample_count = len(groups) if config.total_samples is None else min(config.total_samples, len(groups))
        sampled_groups = _sample_runtime_record_groups(rng, groups, base_sample_count)
        rng.shuffle(sampled_groups)
        train_count, validate_count, test_count = _counts_from_ratio(base_sample_count, config.split_ratio)
        train_end = train_count
        validate_end = train_end + validate_count
        test_end = validate_end + test_count
        split_groups = {
            "validate": sampled_groups[train_end:validate_end],
            "test": sampled_groups[validate_end:test_end],
        }
    else:
        split_manifest = load_dataset_split_manifest(config.split_manifest_path)
        source_records = _build_runtime_source_records(split_manifest["dataset_root"])
        manifest_groups = _runtime_groups_from_manifest(source_records, split_manifest)
        split_groups = {
            "validate": manifest_groups["validate"],
            "test": manifest_groups["test"],
        }
    return {
        "validate": _flatten_runtime_record_groups(split_groups["validate"]),
        "test": _flatten_runtime_record_groups(split_groups["test"]),
    }


def _requested_window_for_condition(
    rng: random.Random,
    source_record: _RuntimeSourceRecord,
    condition: _ExpandedCondition,
) -> int | None:
    if condition.mode in {"asr", "natural"}:
        return None
    if condition.requested_window is not None:
        return int(condition.requested_window)
    max_request_window = max(0, len(build_asr_blocks(source_record.metadata, source_record.transcription)) - 1)
    if max_request_window < 1:
        return None
    return rng.randint(1, max_request_window)


def _example_for_condition(
    *,
    source_record: _RuntimeSourceRecord,
    condition: _ExpandedCondition,
    requested_window: int | None,
    max_window_size: int,
) -> TrainingExample | None:
    asr_blocks = build_asr_blocks(source_record.metadata, source_record.transcription)
    min_wait_window: int | None = None
    if condition.mode == "asr":
        translation_blocks = build_translation_blocks(
            source_record.metadata,
            source_record.transcription,
            source_record.translation,
        )
        return TrainingExample(
            task="asr",
            uid=source_record.uid,
            source_language=_language_name(source_record.source_language),
            target_language=None,
            translation_mode=None,
            min_wait_window=None,
            tolerance_window=count_max_empty_translation_windows(translation_blocks),
            audio_path=source_record.audio_path,
            src_outputs=_limit_windows(asr_blocks, max_window_size=max_window_size),
            tgt_outputs=None,
        )
    if condition.mode == "natural":
        translation_blocks = build_translation_blocks(
            source_record.metadata,
            source_record.transcription,
            source_record.translation,
        )
    elif condition.mode == "fixed_window":
        if requested_window is None:
            return None
        translation_blocks = build_fixed_window_translation_blocks(
            source_record.metadata,
            source_record.transcription,
            source_record.translation,
            tolerance_window=requested_window,
        )
    elif condition.mode == "conservative":
        if requested_window is None:
            return None
        min_wait_window = requested_window
        translation_blocks = build_conservative_translation_blocks(
            source_record.metadata,
            source_record.transcription,
            source_record.translation,
            min_wait_window=min_wait_window,
        )
    else:
        raise ValueError(f"Unsupported translation mode: {condition.mode}")

    displayed_tolerance_window = (
        requested_window
        if condition.mode == "fixed_window" and requested_window is not None
        else count_max_empty_translation_windows(translation_blocks)
    )

    return TrainingExample(
        task="translation",
        uid=source_record.uid,
        source_language=_language_name(source_record.source_language),
        target_language=_language_name(source_record.target_language),
        translation_mode=condition.mode,
        min_wait_window=min_wait_window,
        tolerance_window=displayed_tolerance_window,
        audio_path=source_record.audio_path,
        src_outputs=_limit_windows(asr_blocks, max_window_size=max_window_size),
        tgt_outputs=_limit_windows(translation_blocks, max_window_size=max_window_size),
    )


def _rows_for_condition(config: OpenAIStrictTestConfig, condition: _ExpandedCondition) -> list[_RuntimeRow]:
    rng = random.Random(f"{config.seed}:{condition.label}")
    source_records_by_split = _runtime_source_records_by_split(config)
    rows: list[_RuntimeRow] = []
    for split_name in config.splits:
        for source_record in source_records_by_split[split_name]:
            requested_window = _requested_window_for_condition(rng, source_record, condition)
            example = _example_for_condition(
                source_record=source_record,
                condition=condition,
                requested_window=requested_window,
                max_window_size=config.max_window_size,
            )
            if example is None:
                continue
            max_empty_window = int(source_record.translation.max_empty_window)
            target_metrics_included = True
            target_metrics_filter_reason = None
            if (
                condition.mode in {"fixed_window", "conservative"}
                and requested_window is not None
                and max_empty_window > requested_window
            ):
                target_metrics_included = False
                target_metrics_filter_reason = (
                    f"max_empty_window={max_empty_window} > requested_window={requested_window}"
                )
            rows.append(
                _RuntimeRow(
                    split=split_name,
                    example=example,
                    messages=example_to_messages(example),
                    requested_window=requested_window,
                    max_empty_window=max_empty_window,
                    target_metrics_included=target_metrics_included,
                    target_metrics_filter_reason=target_metrics_filter_reason,
                )
            )
    if config.test_record_count == -1:
        return rows
    return rows[: int(config.test_record_count)]


def _audio_chunk_to_wav_base64(chunk: torch.Tensor, *, sampling_rate: int) -> str:
    waveform = chunk.detach().cpu().to(dtype=torch.float32).flatten().clamp(-1.0, 1.0)
    pcm = (waveform.numpy() * 32767.0).round().astype("<i2")
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(int(sampling_rate))
        wav_file.writeframes(pcm.tobytes())
    return base64.b64encode(buffer.getvalue()).decode("ascii")


def _audio_content_part(audio_base64: str, *, audio_message_format: AudioMessageFormat) -> dict[str, Any]:
    if audio_message_format == "input_audio":
        return {
            "type": "input_audio",
            "input_audio": {
                "data": audio_base64,
                "format": "wav",
            },
        }
    if audio_message_format == "audio_url":
        return {
            "type": "audio_url",
            "audio_url": {
                "url": f"data:audio/wav;base64,{audio_base64}",
            },
        }
    raise ValueError(f"Unsupported audio_message_format: {audio_message_format}")


def _make_user_audio_message(audio_base64: str, *, audio_message_format: AudioMessageFormat) -> dict[str, Any]:
    return {
        "role": "user",
        "content": [_audio_content_part(audio_base64, audio_message_format=audio_message_format)],
    }


def _extract_response_content_and_finish_reason(response: Any) -> tuple[str, str | None]:
    choices = getattr(response, "choices", None)
    if not choices:
        raise RuntimeError("OpenAI-compatible provider returned no choices")
    choice = choices[0]
    message = getattr(choice, "message", None)
    if message is None:
        raise RuntimeError("OpenAI-compatible provider returned a choice without message")
    content = getattr(message, "content", None)
    if content is None:
        raise RuntimeError("OpenAI-compatible provider returned assistant message content=None")
    if not isinstance(content, str):
        raise RuntimeError(f"OpenAI-compatible provider returned non-string content: {type(content).__name__}")
    return content, getattr(choice, "finish_reason", None)


def _build_api_error_context(error: Exception, *, uid: str, turn_number: int, model_name: str) -> str:
    parts = [
        f"uid={uid!r}",
        f"turn={turn_number}",
        f"model={model_name!r}",
        f"error_type={error.__class__.__module__}.{error.__class__.__name__}",
        f"error={str(error)!r}",
    ]
    status_code = getattr(error, "status_code", None)
    if status_code is not None:
        parts.append(f"status_code={status_code}")
    response = getattr(error, "response", None)
    if response is not None:
        parts.append(f"response_status_code={getattr(response, 'status_code', None)!r}")
        text = getattr(response, "text", None)
        if text:
            parts.append(f"response_text={text[:2000]!r}")
    return ", ".join(parts)


class _OpenAIRolloutRunner:
    def __init__(self, *, config: OpenAIStrictTestConfig) -> None:
        self.config = config
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.request_timeout,
        )
        self.semaphore = asyncio.Semaphore(int(config.concurrency))

    async def iter_rows(self, rows: list[_RuntimeRow]):
        tasks = [
            asyncio.create_task(self._run_row_with_semaphore(row=row, index=index, total=len(rows)))
            for index, row in enumerate(rows, start=1)
        ]
        try:
            for task in asyncio.as_completed(tasks):
                yield await task
        finally:
            pending = [task for task in tasks if not task.done()]
            for task in pending:
                task.cancel()
            if pending:
                await asyncio.gather(*pending, return_exceptions=True)

    async def _run_row_with_semaphore(self, *, row: _RuntimeRow, index: int, total: int) -> dict[str, Any]:
        async with self.semaphore:
            return await self._run_row(row=row, index=index, total=total)

    async def _run_row(self, *, row: _RuntimeRow, index: int, total: int) -> dict[str, Any]:
        assistant_indices = assistant_turn_indices(row.messages)
        audio_chunks = audio_chunks_for_example(
            row.example,
            audio_sampling_rate=self.config.audio_sampling_rate,
            audio_chunk_seconds=self.config.audio_chunk_seconds,
        )
        audio_payloads = [
            _audio_chunk_to_wav_base64(chunk, sampling_rate=self.config.audio_sampling_rate)
            for chunk in audio_chunks
        ]
        rollout_messages: list[dict[str, Any]] = [{"role": "system", "content": str(row.messages[0]["content"])}]
        outputs: list[dict[str, Any]] = []
        for turn_offset, assistant_index in enumerate(assistant_indices):
            turn_number = turn_offset + 1
            user_index = assistant_index - 1
            if user_index <= 0 or row.messages[user_index]["role"] != "user":
                raise ValueError(f"Expected user message before assistant turn {turn_number} for {row.example.uid}")
            rollout_messages.append(
                _make_user_audio_message(
                    audio_payloads[turn_offset],
                    audio_message_format=self.config.audio_message_format,
                )
            )
            ground_truth = str(row.messages[assistant_index]["content"])
            raw_output, finish_reason, process_time_ms = await self._generate_assistant_text(
                messages=rollout_messages,
                uid=str(row.example.uid),
                turn_number=turn_number,
            )
            rollout_messages.append({"role": "assistant", "content": raw_output})
            protocol = parse_protocol_output(raw_output)
            outputs.append(
                {
                    "ground_truth": ground_truth,
                    "raw_output": raw_output,
                    "extracted_protocol_output": protocol["normalized_output"],
                    "protocol_adherent": protocol_output_adherent(raw_output, protocol),
                    "api_finish_reason": finish_reason,
                    "process_time_ms": process_time_ms,
                }
            )
        print(f"strict-runtime record={index}/{total} split={row.split} uid={row.example.uid} turns={len(outputs)}")
        return {
            "uid": str(row.example.uid),
            "split": row.split,
            "task": row.example.task,
            "translation_mode": row.example.translation_mode,
            "requested_window": row.requested_window,
            "max_empty_window": row.max_empty_window,
            "target_metrics_included": row.target_metrics_included,
            "target_metrics_filter_reason": row.target_metrics_filter_reason,
            "tolerance_window": row.example.tolerance_window,
            "min_wait_window": row.example.min_wait_window,
            "system_prompt": str(row.messages[0]["content"]),
            "outputs": outputs,
        }

    async def _generate_assistant_text(
        self,
        *,
        messages: list[dict[str, Any]],
        uid: str,
        turn_number: int,
    ) -> tuple[str, str | None, float]:
        create_kwargs: dict[str, Any] = {
            "model": self.config.model_name,
            "messages": messages,
            "max_tokens": int(self.config.max_tokens),
        }
        if self.config.temperature is not None:
            create_kwargs["temperature"] = float(self.config.temperature)
        if self.config.top_p is not None:
            create_kwargs["top_p"] = float(self.config.top_p)
        if self.config.extra_body is not None:
            create_kwargs["extra_body"] = self.config.extra_body
        try:
            request_started_at = time.perf_counter()
            response = await self.client.chat.completions.create(**create_kwargs)
            process_time_ms = round((time.perf_counter() - request_started_at) * 1000.0, 3)
            content, finish_reason = _extract_response_content_and_finish_reason(response)
            return content, finish_reason, process_time_ms
        except (APIStatusError, RateLimitError, APIConnectionError, APITimeoutError, OpenAIError) as exc:
            raise RuntimeError(
                "OpenAI-compatible strict-test API call failed "
                f"({_build_api_error_context(exc, uid=uid, turn_number=turn_number, model_name=self.config.model_name)})"
            ) from exc


def _runtime_protocol_state(text: str, *, side: Literal["src", "tgt"]) -> bool | None:
    protocol = parse_protocol_output(text)
    if not protocol_output_adherent(text, protocol):
        return None
    if side == "src":
        return protocol_field_is_wait(protocol["src"])
    if protocol["kind"] != "translation":
        return None
    return protocol_field_is_wait(protocol["tgt"])


@dataclass
class _StreamingMetricsAccumulator:
    record_count: int = 0
    total_turns: int = 0
    protocol_adherent_turns: int = 0
    src_wait_total: int = 0
    src_wait_correct: int = 0
    tgt_wait_total: int = 0
    tgt_wait_correct: int = 0
    src_release_total: int = 0
    src_release_correct: int = 0
    tgt_release_total: int = 0
    tgt_release_correct: int = 0
    target_metrics_included_record_count: int = 0
    target_metrics_filtered_record_count: int = 0
    target_metrics_filtered_turn_count: int = 0
    process_time_ms_values: list[float] = field(default_factory=list)
    process_time_ms_by_record: list[dict[str, Any]] = field(default_factory=list)
    target_metrics_filtered_records: list[dict[str, Any]] = field(default_factory=list)

    def add_record(self, record: dict[str, Any]) -> None:
        self.record_count += 1
        target_metrics_included = bool(record.get("target_metrics_included", True))
        if target_metrics_included:
            self.target_metrics_included_record_count += 1
        else:
            self.target_metrics_filtered_record_count += 1
            self.target_metrics_filtered_records.append(
                {
                    "uid": record.get("uid"),
                    "split": record.get("split"),
                    "translation_mode": record.get("translation_mode"),
                    "requested_window": record.get("requested_window"),
                    "max_empty_window": record.get("max_empty_window"),
                    "reason": record.get("target_metrics_filter_reason"),
                }
            )
        record_process_times: list[float] = []
        for output in record["outputs"]:
            self.total_turns += 1
            process_time_ms = output.get("process_time_ms")
            if isinstance(process_time_ms, (int, float)):
                normalized_process_time_ms = round(float(process_time_ms), 3)
                self.process_time_ms_values.append(normalized_process_time_ms)
                record_process_times.append(normalized_process_time_ms)
            raw_output = str(output["raw_output"])
            protocol = parse_protocol_output(raw_output)
            model_adherent = protocol_output_adherent(raw_output, protocol)
            if model_adherent:
                self.protocol_adherent_turns += 1

            gt_src_wait = _runtime_protocol_state(str(output["ground_truth"]), side="src")
            gt_tgt_wait = _runtime_protocol_state(str(output["ground_truth"]), side="tgt")
            model_src_wait = _runtime_protocol_state(raw_output, side="src") if model_adherent else None
            model_tgt_wait = _runtime_protocol_state(raw_output, side="tgt") if model_adherent else None

            if not model_adherent:
                continue

            if gt_src_wait is True:
                self.src_wait_total += 1
                self.src_wait_correct += int(model_src_wait is True)
            elif gt_src_wait is False:
                self.src_release_total += 1
                self.src_release_correct += int(model_src_wait is False)

            if not target_metrics_included and gt_tgt_wait is not None:
                self.target_metrics_filtered_turn_count += 1
            elif gt_tgt_wait is True:
                self.tgt_wait_total += 1
                self.tgt_wait_correct += int(model_tgt_wait is True)
            elif gt_tgt_wait is False:
                self.tgt_release_total += 1
                self.tgt_release_correct += int(model_tgt_wait is False)
        self.process_time_ms_by_record.append(
            {
                "uid": record.get("uid"),
                "split": record.get("split"),
                "turn_process_time_ms": record_process_times,
            }
        )

    def metrics(self) -> dict[str, Any]:
        def _rate(correct: int, total: int) -> float:
            return 0.0 if total == 0 else correct / total

        def _percentile(values: list[float], percentile: float) -> float:
            if not values:
                return 0.0
            sorted_values = sorted(values)
            index = round((len(sorted_values) - 1) * percentile)
            return sorted_values[int(index)]

        return {
            "record_count": self.record_count,
            "turn_count": self.total_turns,
            "protocol_adherence_rate": _rate(self.protocol_adherent_turns, self.total_turns),
            "src_wait_accuracy": _rate(self.src_wait_correct, self.src_wait_total),
            "tgt_wait_accuracy": _rate(self.tgt_wait_correct, self.tgt_wait_total),
            "src_release_accuracy": _rate(self.src_release_correct, self.src_release_total),
            "tgt_release_accuracy": _rate(self.tgt_release_correct, self.tgt_release_total),
            "src_wait_total": self.src_wait_total,
            "tgt_wait_total": self.tgt_wait_total,
            "src_release_total": self.src_release_total,
            "tgt_release_total": self.tgt_release_total,
            "target_metrics_included_record_count": self.target_metrics_included_record_count,
            "target_metrics_filtered_record_count": self.target_metrics_filtered_record_count,
            "target_metrics_filtered_turn_count": self.target_metrics_filtered_turn_count,
            "process_time_ms_count": len(self.process_time_ms_values),
            "process_time_ms_total": round(sum(self.process_time_ms_values), 3),
            "process_time_ms_avg": (
                0.0
                if not self.process_time_ms_values
                else round(sum(self.process_time_ms_values) / len(self.process_time_ms_values), 3)
            ),
            "process_time_ms_p50": round(_percentile(self.process_time_ms_values, 0.5), 3),
            "process_time_ms_p95": round(_percentile(self.process_time_ms_values, 0.95), 3),
            "process_time_ms_max": round(max(self.process_time_ms_values), 3) if self.process_time_ms_values else 0.0,
        }


def _summary_for_metrics(
    *,
    config: OpenAIStrictTestConfig,
    condition: _ExpandedCondition,
    row_count: int,
    metrics: dict[str, Any],
    process_time_ms_by_record: list[dict[str, Any]],
    target_metrics_filtered_records: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "condition": condition.to_json(),
        "step": 0,
        "metrics": {},
        "test_metrics": metrics,
        "total_available_test_rows": row_count,
        "selected_test_rows": row_count,
        "splits": list(config.splits),
        "concurrency": int(config.concurrency),
        "constrained_decoding": bool(config.constrained_decoding),
        "process_time_ms_by_record": process_time_ms_by_record,
        "target_metrics_filtered_records": target_metrics_filtered_records,
    }


def _metrics_json_payload(
    config: OpenAIStrictTestConfig,
    summary: dict[str, Any],
    *,
    records_jsonl_path: str | None,
) -> dict[str, Any]:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model_name": config.model_name,
        "base_url": config.base_url,
        "concurrency": int(config.concurrency),
        "constrained_decoding": bool(config.constrained_decoding),
        "splits": list(config.splits),
        "split_ratio": list(config.split_ratio),
        "split_manifest_path": None if config.split_manifest_path is None else str(config.split_manifest_path),
        "total_samples": config.total_samples,
        "max_window_size": config.max_window_size,
        "test_record_count": config.test_record_count,
        "audio_message_format": config.audio_message_format,
        "max_tokens": config.max_tokens,
        "temperature": config.temperature,
        "top_p": config.top_p,
        "extra_body": config.extra_body,
        "condition": summary["condition"],
        "total_available_test_rows": summary["total_available_test_rows"],
        "selected_test_rows": summary["selected_test_rows"],
        "test_metrics": summary["test_metrics"],
        "process_time_ms_by_record": summary["process_time_ms_by_record"],
        "target_metrics_filtered_records": summary["target_metrics_filtered_records"],
        "records_jsonl_path": records_jsonl_path,
    }


def _write_json_atomic(path: str | Path, payload: dict[str, Any]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    temp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp_path.replace(output_path)


def _append_jsonl(path: str | Path, record: dict[str, Any]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def _condition_output_path(output_dir: str | Path, *, prefix: str, condition: _ExpandedCondition, suffix: str) -> Path:
    return Path(output_dir) / f"{prefix}-{condition.label}.{suffix}"


def _format_metric_value(value: Any) -> str:
    return f"{value:.4f}" if isinstance(value, float) else str(value)


def _format_runtime_test_metrics_section(summary: dict[str, Any]) -> str:
    metrics = summary["test_metrics"]
    timing_keys = {
        "process_time_ms_count",
        "process_time_ms_avg",
        "process_time_ms_p50",
        "process_time_ms_p95",
        "process_time_ms_max",
    }
    lines = [
        "",
        "",
        "Test Metrics",
        f"  - STEP: {summary['step']}",
        f"  - TOTAL_AVAILABLE_TEST_ROWS: {summary['total_available_test_rows']}",
        f"  - SELECTED_TEST_ROWS: {summary['selected_test_rows']}",
    ]
    for key in sorted(key for key in metrics if not key.startswith("process_time_ms_")):
        lines.append(f"  - {key.upper()}: {_format_metric_value(metrics[key])}")
    present_timing_keys = [key for key in timing_keys if key in metrics]
    if present_timing_keys:
        lines += ["", "Timing Metrics"]
        for key in ("process_time_ms_count", "process_time_ms_avg", "process_time_ms_p50", "process_time_ms_p95", "process_time_ms_max"):
            if key in metrics:
                lines.append(f"  - {key.upper()}: {_format_metric_value(metrics[key])}")
    return "\n".join(lines)


def _markdown_code_cell(value: Any) -> str:
    text = str(value)
    text = text.replace("`", "&#96;").replace("|", "\\|").replace("\n", "<br>")
    return f"`{text}`"


def _markdown_process_time_ms(value: Any) -> str:
    if isinstance(value, (int, float)):
        return str(round(float(value)))
    return str(value)


def _format_runtime_markdown_record_section(record: dict[str, Any], *, index: int, total: int) -> str:
    lines = [
        f"### Test Example {index} / {total}",
        f"- UID: {record['uid']}",
        f"- SYSTEM_PROMPT: {record['system_prompt']}",
    ]
    if not bool(record.get("target_metrics_included", True)):
        lines.append(f"- TGT_METRICS: filtered ({record.get('target_metrics_filter_reason')})")
    lines += [
        "",
        "| round | ground truth | predict | process time (ms) |",
        "|---|---|---|---|",
    ]
    for output_index, output in enumerate(record["outputs"], start=1):
        process_time_ms = _markdown_process_time_ms(output.get("process_time_ms", ""))
        if "raw_output" not in output:
            raise KeyError("Runtime strict Markdown predict requires raw_output")
        lines.append(
            "| "
            f"{output_index} | "
            f"{_markdown_code_cell(output['ground_truth'])} | "
            f"{_markdown_code_cell(output['raw_output'])} | "
            f"{process_time_ms} |"
        )
    return "\n".join(lines)


def _write_markdown_header(path: str | Path, config: OpenAIStrictTestConfig) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sections = [
        "# OpenAI-Compatible Runtime Strict Test",
        "",
        MARKDOWN_METRICS_PLACEHOLDER,
        "",
        "---",
        "",
        f"- model_name: `{config.model_name}`",
        f"- base_url: `{config.base_url}`",
        f"- concurrency: `{config.concurrency}`",
        f"- splits: `{', '.join(config.splits)}`",
        f"- constrained_decoding: `{config.constrained_decoding}`",
        "",
    ]
    output_path.write_text("\n".join(sections), encoding="utf-8")


def _append_markdown(path: str | Path, text: str) -> None:
    with Path(path).open("a", encoding="utf-8") as file:
        file.write(text)


def _replace_markdown_metrics_placeholder(path: str | Path, summary: dict[str, Any]) -> None:
    output_path = Path(path)
    text = output_path.read_text(encoding="utf-8")
    metrics_text = _format_runtime_test_metrics_section(summary).strip()
    if MARKDOWN_METRICS_PLACEHOLDER not in text:
        raise RuntimeError(f"Markdown metrics placeholder is missing: {output_path}")
    output_path.write_text(text.replace(MARKDOWN_METRICS_PLACEHOLDER, metrics_text, 1), encoding="utf-8")


class _ConditionOutputWriter:
    def __init__(self, *, config: OpenAIStrictTestConfig, condition: _ExpandedCondition, row_count: int) -> None:
        self.config = config
        self.condition = condition
        self.row_count = row_count
        self.accumulator = _StreamingMetricsAccumulator()
        self.records_jsonl_path = (
            _condition_output_path(
                config.metrics_output_dir,
                prefix="strict_test_records",
                condition=condition,
                suffix="jsonl",
            )
            if config.metrics_output_dir is not None
            else None
        )
        self.metrics_path = (
            _condition_output_path(
                config.metrics_output_dir,
                prefix="strict_test_metrics",
                condition=condition,
                suffix="json",
            )
            if config.metrics_output_dir is not None
            else None
        )
        self.markdown_path = (
            _condition_output_path(
                config.markdown_output_dir,
                prefix="strict_test_outputs",
                condition=condition,
                suffix="md",
            )
            if config.markdown_output_dir is not None
            else None
        )
        self.markdown_record_count = 0

    def start(self) -> None:
        if self.records_jsonl_path is not None:
            self.records_jsonl_path.parent.mkdir(parents=True, exist_ok=True)
            self.records_jsonl_path.write_text("", encoding="utf-8")
        if self.markdown_path is not None:
            _write_markdown_header(self.markdown_path, self.config)
        self._write_metrics()

    def append_record(self, record: dict[str, Any]) -> None:
        self.accumulator.add_record(record)
        if self.records_jsonl_path is not None:
            _append_jsonl(self.records_jsonl_path, record)
        if (
            self.markdown_path is not None
            and self.markdown_record_count < self.config.markdown_record_limit_per_condition
        ):
            self.markdown_record_count += 1
            _append_markdown(
                self.markdown_path,
                "\n---\n\n"
                + _format_runtime_markdown_record_section(record, index=self.markdown_record_count, total=self.row_count)
                + "\n",
            )
        self._write_metrics()

    def finalize(self) -> dict[str, Any]:
        summary = self.summary()
        self._write_metrics(summary)
        if self.markdown_path is not None:
            if self.row_count > self.markdown_record_count:
                _append_markdown(
                    self.markdown_path,
                    "\n"
                    f"Markdown records are capped at {self.markdown_record_count} / {self.row_count} "
                    "for this condition.\n",
                )
            _replace_markdown_metrics_placeholder(self.markdown_path, summary)
        return summary

    def summary(self) -> dict[str, Any]:
        return _summary_for_metrics(
            config=self.config,
            condition=self.condition,
            row_count=self.row_count,
            metrics=self.accumulator.metrics(),
            process_time_ms_by_record=self.accumulator.process_time_ms_by_record,
            target_metrics_filtered_records=self.accumulator.target_metrics_filtered_records,
        )

    def paths(self) -> dict[str, str | None]:
        return {
            "records_jsonl_path": str(self.records_jsonl_path) if self.records_jsonl_path is not None else None,
            "metrics_path": str(self.metrics_path) if self.metrics_path is not None else None,
            "markdown_path": str(self.markdown_path) if self.markdown_path is not None else None,
        }

    def _write_metrics(self, summary: dict[str, Any] | None = None) -> None:
        if self.metrics_path is None:
            return
        effective_summary = self.summary() if summary is None else summary
        _write_json_atomic(
            self.metrics_path,
            _metrics_json_payload(
                self.config,
                effective_summary,
                records_jsonl_path=str(self.records_jsonl_path) if self.records_jsonl_path is not None else None,
            ),
        )


async def _run_openai_strict_test_async(config: OpenAIStrictTestConfig) -> dict[str, Any]:
    runner = _OpenAIRolloutRunner(config=config)
    condition_summaries: list[dict[str, Any]] = []
    written_records: list[str] = []
    written_metrics: list[str] = []
    written_markdown: list[str] = []
    for condition in _expand_conditions(config.style_specs):
        print(f"\nRunning condition: {condition.label}")
        rows = _rows_for_condition(config, condition)
        writer = _ConditionOutputWriter(config=config, condition=condition, row_count=len(rows))
        writer.start()
        paths = writer.paths()
        for path in (paths["records_jsonl_path"], paths["metrics_path"], paths["markdown_path"]):
            if path is not None:
                print(f"  writing: {path}")
        async for record in runner.iter_rows(rows):
            writer.append_record(record)
        summary = writer.finalize()
        condition_summaries.append(summary)
        print(_format_runtime_test_metrics_section(summary))
        if paths["records_jsonl_path"] is not None:
            written_records.append(paths["records_jsonl_path"])
        if paths["metrics_path"] is not None:
            written_metrics.append(paths["metrics_path"])
        if paths["markdown_path"] is not None:
            written_markdown.append(paths["markdown_path"])
    if written_records:
        print("\nWrote strict runtime record JSONL files:")
        for path in written_records:
            print(f"  - {path}")
    if written_metrics:
        print("Wrote strict runtime metrics JSON files:")
        for path in written_metrics:
            print(f"  - {path}")
    if written_markdown:
        print("Wrote strict runtime markdown files:")
        for path in written_markdown:
            print(f"  - {path}")
    return {
        "condition_summaries": condition_summaries,
        "records_jsonl_paths": written_records,
        "metrics_paths": written_metrics,
        "markdown_paths": written_markdown,
    }


def run_openai_strict_test(config: OpenAIStrictTestConfig) -> dict[str, Any]:
    """Run configured OpenAI-compatible strict tests and write requested outputs."""

    return asyncio.run(_run_openai_strict_test_async(config))
