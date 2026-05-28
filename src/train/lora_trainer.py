"""Transformers Trainer + PEFT data wrapper for MakeSense real-audio LoRA training.

This module keeps the project-owned training boundary narrow:

1. read final training examples through ``build_training_dataset(...)``;
2. convert ``TrainingExample`` objects into multimodal chat message skeletons;
3. collate original audio into causal chunks configured by the caller, one chunk per user turn;
4. delegate optimization/checkpointing to ``transformers.Trainer``.

Model loading and PEFT attachment stay in ``examples/train_lora.py``. This file
does not depend on Unsloth and does not fake audio by treating ``<|audio|>`` as
ordinary text.
"""

from __future__ import annotations

import math as _math
import math
import os
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch

from data_loader.dataset import TrainingExample, TrainingDatasetSplits, build_training_dataset
from train.formatting import ChatMessage, example_to_messages
from train.monitoring import MakeSenseMonitoringCallback, TensorBoardServer

@dataclass(frozen=True)
class TrainingDataConfig:
    """Controls final-dataset sampling for LoRA training."""

    dataset_root: str | Path = "dataset_test"
    total_samples: int | None = None
    task_ratio: tuple[float, float] = (9, 1)
    split_ratio: tuple[float, float, float] = (8, 1.5, 0.5)
    tolerance_window: int | None = None
    seed: int = 4021


@dataclass(frozen=True)
class LoraTrainConfig:
    """Transformers Trainer controls for an externally prepared PEFT model."""

    output_dir: str | Path = "outputs/makesense_lora"
    max_seq_length: int = 8192
    audio_sampling_rate: int = 16000
    audio_chunk_seconds: float = 1.0
    learning_rate: float = 2e-4
    weight_decay: float = 0.0
    num_train_epochs: int = 1
    per_device_train_batch_size: int = 1
    gradient_accumulation_steps: int = 8
    warmup_steps: int = 5
    logging_steps: int = 1
    eval_steps: int = 100
    save_steps: int = 500
    max_grad_norm: float = 1.0
    max_steps: int = -1
    report_to: str = "tensorboard"
    logging_dir: str | Path | None = None
    metrics_jsonl_name: str = "train_metrics.jsonl"
    sample_generations_jsonl_name: str = "sample_generations.jsonl"
    sample_generation_steps: int = 0
    sample_generation_max_new_tokens: int = 256
    sample_evaluation_record_count: int = 1
    save_processor: bool = False
    launch_tensorboard: bool = True
    tensorboard_host: str = "127.0.0.1"
    tensorboard_port: int = 6006
    seed: int = 4021


def _set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def _examples_to_rows(
    examples: list[TrainingExample],
    *,
    requested_tolerance_window: int | None,
) -> list[dict[str, Any]]:
    return [
        {
            "example": example,
            "messages": example_to_messages(
                example,
                requested_tolerance_window=requested_tolerance_window,
            ),
        }
        for example in examples
    ]


def _assert_message_order(messages: list[ChatMessage]) -> None:
    if not messages:
        raise ValueError("Conversation has no messages")
    if messages[0]["role"] != "system":
        raise ValueError(f"Conversation must start with system message, got {messages[0]['role']!r}")
    for index, message in enumerate(messages[1:], start=1):
        expected_role = "user" if index % 2 == 1 else "assistant"
        if message["role"] != expected_role:
            raise ValueError(
                f"Conversation role order error at message {index}: "
                f"expected {expected_role!r}, got {message['role']!r}"
            )


def _assert_has_training_target(messages: list[ChatMessage]) -> None:
    assistant_contents = [str(message["content"]) for message in messages if message["role"] == "assistant"]
    if not assistant_contents:
        raise ValueError("Conversation has no assistant training target")
    if not any("<src>" in content or "<tgt>" in content for content in assistant_contents):
        raise ValueError("Assistant messages do not contain <src> or <tgt> training blocks")


def count_audio_slots(messages: list[ChatMessage]) -> int:
    """Count processor-managed audio slots in a multimodal message skeleton."""

    count = 0
    for message in messages:
        content = message.get("content")
        if isinstance(content, list):
            count += sum(isinstance(item, dict) and item.get("type") == "audio" for item in content)
    return count


def load_audio_waveform(audio_path: str | Path, *, target_sampling_rate: int) -> torch.Tensor:
    """Load mono audio and resample it to the processor sampling rate."""

    import torchaudio

    waveform, sample_rate = torchaudio.load(str(audio_path))
    if waveform.ndim != 2:
        raise ValueError(f"Expected waveform shape [channels, samples], got {tuple(waveform.shape)}")
    waveform = waveform.mean(dim=0)
    if int(sample_rate) != int(target_sampling_rate):
        waveform = torchaudio.functional.resample(waveform, int(sample_rate), int(target_sampling_rate))
    return waveform.to(dtype=torch.float32)


def split_audio_into_chunks(waveform: torch.Tensor, *, sampling_rate: int, chunk_seconds: float) -> list[torch.Tensor]:
    """Split audio into fixed-size causal chunks and zero-pad the final chunk."""

    if waveform.ndim != 1:
        raise ValueError(f"Expected mono waveform shape [samples], got {tuple(waveform.shape)}")
    chunk_size = int(round(float(sampling_rate) * chunk_seconds))
    if chunk_size <= 0:
        raise ValueError(f"Invalid audio chunk size from sampling_rate={sampling_rate}, chunk_seconds={chunk_seconds}")
    chunk_count = max(1, math.ceil(int(waveform.numel()) / chunk_size))
    chunks: list[torch.Tensor] = []
    for index in range(chunk_count):
        start = index * chunk_size
        end = min(start + chunk_size, int(waveform.numel()))
        chunk = waveform[start:end]
        if int(chunk.numel()) < chunk_size:
            chunk = torch.nn.functional.pad(chunk, (0, chunk_size - int(chunk.numel())))
        chunks.append(chunk)
    return chunks


def _validate_example_chunk_counts(example: TrainingExample, audio_chunks: list[torch.Tensor]) -> None:
    if example.task == "asr":
        if len(audio_chunks) != len(example.src_outputs):
            raise ValueError(
                f"ASR example {example.uid} chunk/output mismatch: "
                f"audio_chunks={len(audio_chunks)}, src_outputs={len(example.src_outputs)}"
            )
        return
    if example.task == "translation":
        if example.tgt_outputs is None:
            raise ValueError(f"Translation example {example.uid} has no target outputs")
        if len(audio_chunks) != len(example.src_outputs) or len(audio_chunks) != len(example.tgt_outputs):
            raise ValueError(
                f"Translation example {example.uid} chunk/output mismatch: "
                f"audio_chunks={len(audio_chunks)}, src_outputs={len(example.src_outputs)}, "
                f"tgt_outputs={len(example.tgt_outputs)}"
            )
        return
    raise ValueError(f"Unsupported training task: {example.task}")


def _render_chat(processor: Any, messages: list[ChatMessage]) -> str:
    try:
        tokenizer = processor.tokenizer
    except AttributeError as exc:
        raise ValueError("Real-audio training requires processor.tokenizer.apply_chat_template") from exc
    try:
        rendered = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False,
        )
    except AttributeError as exc:
        raise ValueError("Real-audio training requires processor.tokenizer.apply_chat_template") from exc
    except TypeError:
        raise
    return str(rendered)


def _get_completion_mask(batch: dict[str, Any]) -> torch.Tensor | None:
    """Return a processor/template-provided assistant/completion mask tensor when available."""

    for key in ("assistant_masks", "completion_mask", "assistant_tokens_mask"):
        mask = batch.get(key)
        if mask is None:
            continue
        if not isinstance(mask, torch.Tensor):
            mask = torch.tensor(mask, dtype=torch.long)
        return mask.to(dtype=torch.bool)
    return None


def _rendered_token_ids(processor: Any, messages: list[ChatMessage]) -> list[int]:
    try:
        tokenizer = processor.tokenizer
    except AttributeError as exc:
        raise ValueError("Assistant span fallback requires processor.tokenizer") from exc
    rendered = _render_chat(processor, messages)
    encoded = tokenizer(rendered, add_special_tokens=False)
    input_ids = encoded["input_ids"] if isinstance(encoded, dict) else encoded.input_ids
    if isinstance(input_ids, torch.Tensor):
        if input_ids.ndim == 2:
            input_ids = input_ids[0]
        return [int(token_id) for token_id in input_ids.tolist()]
    if input_ids and isinstance(input_ids[0], list):
        input_ids = input_ids[0]
    return [int(token_id) for token_id in input_ids]


def _assistant_span_mask_from_messages(
    *,
    processor: Any,
    message_batches: list[list[ChatMessage]],
    input_ids: torch.Tensor,
) -> torch.Tensor:
    mask = torch.zeros_like(input_ids, dtype=torch.bool)
    sequence_length = int(input_ids.shape[1])
    for batch_index, messages in enumerate(message_batches):
        for message_index, message in enumerate(messages):
            if message["role"] != "assistant":
                continue
            prefix_ids = _rendered_token_ids(processor, messages[:message_index])
            upto_ids = _rendered_token_ids(processor, messages[: message_index + 1])
            start = min(len(prefix_ids), sequence_length)
            end = min(len(upto_ids), sequence_length)
            if end > start:
                mask[batch_index, start:end] = True
    return mask


def _labels_from_completion_mask(
    batch: dict[str, Any],
    *,
    processor: Any,
    message_batches: list[list[ChatMessage]],
) -> torch.Tensor:
    input_ids = batch.get("input_ids")
    if not isinstance(input_ids, torch.Tensor):
        raise ValueError("Processor output does not contain tensor input_ids")
    completion_mask = _get_completion_mask(batch)
    if completion_mask is None:
        completion_mask = _assistant_span_mask_from_messages(
            processor=processor,
            message_batches=message_batches,
            input_ids=input_ids,
        )
    completion_mask = completion_mask.to(device=input_ids.device)
    if completion_mask.shape != input_ids.shape:
        raise ValueError(
            "Assistant/completion mask shape does not match input_ids: "
            f"mask={tuple(completion_mask.shape)}, input_ids={tuple(input_ids.shape)}"
        )

    supervised_mask = completion_mask
    attention_mask = batch.get("attention_mask")
    if isinstance(attention_mask, torch.Tensor):
        supervised_mask = supervised_mask & attention_mask.to(device=input_ids.device, dtype=torch.bool)

    labels = input_ids.clone()
    labels[~supervised_mask] = -100
    return labels


class MakeSenseAudioCollator:
    """Processor-based multimodal collator with caller-configured causal audio chunks."""

    def __init__(self, processor: Any, *, max_length: int, audio_sampling_rate: int, audio_chunk_seconds: float) -> None:
        self.processor = processor
        self.max_length = max_length
        self.audio_sampling_rate = audio_sampling_rate
        self.audio_chunk_seconds = audio_chunk_seconds

    def _audio_chunks_for_example(self, example: TrainingExample) -> list[torch.Tensor]:
        waveform = load_audio_waveform(example.audio_path, target_sampling_rate=self.audio_sampling_rate)
        audio_chunks = split_audio_into_chunks(
            waveform,
            sampling_rate=self.audio_sampling_rate,
            chunk_seconds=self.audio_chunk_seconds,
        )
        _validate_example_chunk_counts(example, audio_chunks)
        return audio_chunks

    def _call_processor(self, rendered_texts: list[str], flat_audio_chunks: list[torch.Tensor]) -> dict[str, Any]:
        try:
            batch = self.processor(
                text=rendered_texts,
                audio=[chunk.detach().cpu().to(dtype=torch.float32).numpy() for chunk in flat_audio_chunks],
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.max_length,
            )
        except AttributeError as exc:
            raise ValueError("Real-audio training requires callable processor(text=..., audio=...)") from exc
        except TypeError:
            raise
        return dict(batch)

    def __call__(self, features: list[dict[str, Any]]) -> dict[str, Any]:
        rendered_texts: list[str] = []
        flat_audio_chunks: list[torch.Tensor] = []
        message_batches: list[list[ChatMessage]] = []
        for feature in features:
            example = feature["example"]
            messages = feature["messages"]
            audio_chunks = self._audio_chunks_for_example(example)
            audio_slot_count = count_audio_slots(messages)
            if audio_slot_count != len(audio_chunks):
                raise ValueError(
                    f"Example {example.uid} audio slot/chunk mismatch: "
                    f"audio_slots={audio_slot_count}, audio_chunks={len(audio_chunks)}"
                )
            rendered_texts.append(_render_chat(self.processor, messages))
            flat_audio_chunks.extend(audio_chunks)
            message_batches.append(messages)

        batch = self._call_processor(rendered_texts, flat_audio_chunks)
        batch["labels"] = _labels_from_completion_mask(
            batch,
            processor=self.processor,
            message_batches=message_batches,
        )
        batch.pop("assistant_masks", None)
        batch.pop("completion_mask", None)
        batch.pop("assistant_tokens_mask", None)
        return batch


def _build_train_eval_rows(
    splits: TrainingDatasetSplits,
    *,
    requested_tolerance_window: int | None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]] | None]:
    train_rows = _examples_to_rows(splits.train, requested_tolerance_window=requested_tolerance_window)
    validate_rows = _examples_to_rows(splits.validate, requested_tolerance_window=requested_tolerance_window)
    if not train_rows:
        raise ValueError("Training split is empty; adjust total_samples/split_ratio")
    return train_rows, validate_rows or None


def train_lora(
    *,
    model: Any,
    processor: Any,
    data_config: TrainingDataConfig,
    train_config: LoraTrainConfig,
) -> None:
    """Train and save an externally prepared PEFT model with Transformers Trainer."""

    _set_seed(train_config.seed)
    splits = build_training_dataset(
        data_config.dataset_root,
        total_samples=data_config.total_samples,
        task_ratio=data_config.task_ratio,
        split_ratio=data_config.split_ratio,
        tolerance_window=data_config.tolerance_window,
        seed=data_config.seed,
    )
    train_rows, validate_rows = _build_train_eval_rows(
        splits,
        requested_tolerance_window=data_config.tolerance_window,
    )
    for row in train_rows:
        messages = row["messages"]
        _assert_message_order(messages)
        _assert_has_training_target(messages)

    from transformers import Trainer, TrainingArguments
    from transformers.trainer_callback import PrinterCallback

    output_dir = Path(train_config.output_dir)
    logging_dir = Path(train_config.logging_dir) if train_config.logging_dir is not None else output_dir / "runs"
    os.environ.setdefault("WANDB_DISABLED", "true")
    data_collator = MakeSenseAudioCollator(
        processor,
        max_length=train_config.max_seq_length,
        audio_sampling_rate=train_config.audio_sampling_rate,
        audio_chunk_seconds=train_config.audio_chunk_seconds,
    )

    args = TrainingArguments(
        output_dir=str(output_dir),
        per_device_train_batch_size=train_config.per_device_train_batch_size,
        gradient_accumulation_steps=train_config.gradient_accumulation_steps,
        learning_rate=train_config.learning_rate,
        weight_decay=train_config.weight_decay,
        num_train_epochs=train_config.num_train_epochs,
        warmup_steps=train_config.warmup_steps,
        logging_steps=train_config.logging_steps,
        eval_steps=train_config.eval_steps,
        save_steps=train_config.save_steps,
        max_grad_norm=train_config.max_grad_norm,
        max_steps=train_config.max_steps,
        report_to=train_config.report_to,
        logging_dir=str(logging_dir),
        seed=train_config.seed,
        remove_unused_columns=False,
        eval_strategy="steps" if validate_rows else "no",
        save_strategy="steps",
    )
    callbacks = [
        MakeSenseMonitoringCallback(
            processor=processor,
            sample_rows=validate_rows or train_rows,
            collator=data_collator,
            output_dir=output_dir,
            logging_dir=logging_dir,
            metrics_jsonl_name=train_config.metrics_jsonl_name,
            sample_generations_jsonl_name=train_config.sample_generations_jsonl_name,
            sample_generation_steps=train_config.sample_generation_steps,
            sample_generation_max_new_tokens=train_config.sample_generation_max_new_tokens,
            sample_evaluation_record_count=train_config.sample_evaluation_record_count,
        )
    ]
    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_rows,
        eval_dataset=validate_rows,
        data_collator=data_collator,
        callbacks=callbacks,
    )
    trainer.remove_callback(PrinterCallback)

    train_example_count = len(train_rows)
    effective_batch_size = (
        train_config.per_device_train_batch_size * train_config.gradient_accumulation_steps
    )
    optimizer_steps_per_epoch = max(1, _math.ceil(train_example_count / effective_batch_size))

    print("=== MakeSense LoRA training ===")
    print("dataset_root:", data_config.dataset_root)
    print("train_examples:", len(train_rows))
    print("validate_examples:", 0 if validate_rows is None else len(validate_rows))
    print("output_dir:", train_config.output_dir)
    print("logging_dir:", logging_dir)
    print("tensorboard_logdir:", logging_dir)
    print("audio_sampling_rate:", train_config.audio_sampling_rate)
    print("audio_chunk_seconds:", train_config.audio_chunk_seconds)
    print("per_device_train_batch_size:", train_config.per_device_train_batch_size)
    print("gradient_accumulation_steps:", train_config.gradient_accumulation_steps)
    print("effective_batch_size:", effective_batch_size)
    print("optimizer_steps_per_epoch:", optimizer_steps_per_epoch)
    print()

    tensorboard = TensorBoardServer(
        logdir=logging_dir,
        host=train_config.tensorboard_host,
        port=train_config.tensorboard_port,
        enabled=train_config.launch_tensorboard and train_config.report_to == "tensorboard",
    )
    try:
        tensorboard.start()
        trainer.train()
        trainer.save_model(str(output_dir))
        if train_config.save_processor:
            try:
                processor.save_pretrained(str(output_dir))
            except AttributeError as exc:
                raise ValueError("Real-audio training requires processor.save_pretrained") from exc
            print(f"Saved LoRA adapter and processor to {output_dir}")
        else:
            print(f"Saved LoRA adapter to {output_dir}")
    finally:
        tensorboard.stop()
