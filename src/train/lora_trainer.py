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

import json
import math as _math
import os
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import torch
from mm_assistant_mask import (
    AssistantMaskSpec,
    build_assistant_labels,
)

from data_loader.dataset import TrainingExample, TrainingDatasetSplits, TranslationTaskConfig, build_training_dataset
from train.audio import audio_chunks_for_example, load_audio_waveform, split_audio_into_chunks, validate_example_chunk_counts
from train.continue_utils import ContinuePlan, confirm_resume_arg_mismatches, timestamp_run_dir_name
from train.formatting import ChatMessage, example_to_messages
from train.monitoring import MakeSenseMonitoringCallback, TensorBoardServer, latest_logged_metrics_from_state

@dataclass(frozen=True)
class TrainingDataConfig:
    """Controls final-dataset sampling for LoRA training."""

    dataset_root: str | Path = "dataset_test"
    total_samples: int | None = None
    max_window_size: int = -1
    task_ratio: tuple[float, float] = (9, 1)
    split_ratio: tuple[float, float, float] = (8, 1.5, 0.5)
    translation_task_config: TranslationTaskConfig = field(default_factory=lambda: {
        "natural": {"ratio": 1},
        "fixed_window": {"ratio": 4, "min": None, "max": None},
        "conservative": {"ratio": 4, "min": None, "max": None},
    })
    dataset_repeat: int = 1
    seed: int = 4021


@dataclass(frozen=True)
class LoraTrainConfig:
    """Transformers Trainer controls for an externally prepared PEFT model."""

    output_dir: str | Path = "outputs/makesense_lora"
    audio_sampling_rate: int = 16000
    audio_chunk_seconds: float = 1.0
    learning_rate: float = 2e-4
    weight_decay: float = 0.0
    optimizer: str = "adamw"
    adam_beta1: float = 0.9
    adam_beta2: float = 0.999
    lr_scheduler_type: str = "linear"
    num_train_epochs: int = 1
    per_device_train_batch_size: int = 1
    per_device_eval_batch_size: int = 1
    gradient_accumulation_steps: int = 8
    warmup_steps: int = 5
    logging_steps: int = 1
    eval_steps: int = 100
    prediction_loss_only: bool = True
    eval_accumulation_steps: int | None = 1
    save_steps: int = 500
    max_grad_norm: float = 1.0
    max_steps: int = -1
    report_to: str = "tensorboard"
    logging_dir: str | Path | None = None
    test_metrics_json_name: str = "test_metrics.json"
    test_steps: int = 0
    test_max_new_tokens: int = 256
    test_record_count: int = 1
    test_batch_size: int = 1
    test_cuda_empty_cache_steps: int | None = None
    test_output_markdown: bool = False
    test_outputs_dir_name: str = "test_outputs"
    assistant_header: str = ""
    assistant_end: str = ""
    generation_stop: str = ""
    save_processor: bool = False
    launch_tensorboard: bool = True
    tensorboard_host: str = "127.0.0.1"
    tensorboard_port: int = 6006
    continue_type: str = "none"
    checkpoint_path: str | Path | None = None
    continue_plan: ContinuePlan | None = None
    model_name: str = ""
    seed: int = 4021
    cuda_empty_cache_steps: int | None = None


def _set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def training_arguments_optimizer_name(optimizer: str) -> str:
    """Map the user-facing optimizer name to Transformers TrainingArguments.optim."""

    normalized = str(optimizer).strip().lower()
    if normalized == "adamw":
        return "adamw_torch"
    if normalized == "adamw8bit":
        return "adamw_bnb_8bit"
    raise ValueError("optimizer must be one of {'adamw', 'adamw8bit'}")


class CudaEmptyCacheCallback:
    """Opt-in allocator-cache release after optimizer steps and eval loops."""

    def __init__(self, *, cuda_empty_cache_steps: int | None) -> None:
        if cuda_empty_cache_steps is not None and int(cuda_empty_cache_steps) <= 0:
            raise ValueError("cuda_empty_cache_steps must be positive when provided")
        self.cuda_empty_cache_steps = None if cuda_empty_cache_steps is None else int(cuda_empty_cache_steps)

    def _empty_cache_if_enabled(self) -> None:
        if self.cuda_empty_cache_steps is not None and torch.cuda.is_available():
            torch.cuda.empty_cache()

    def on_step_end(self, args, state, control, **kwargs):  # noqa: ANN001, D401
        if self.cuda_empty_cache_steps is None:
            return control
        step = int(getattr(state, "global_step", 0) or 0)
        if step > 0 and step % self.cuda_empty_cache_steps == 0:
            self._empty_cache_if_enabled()
        return control

    def on_evaluate(self, args, state, control, **kwargs):  # noqa: ANN001, D401
        self._empty_cache_if_enabled()
        return control


def _maybe_cuda_empty_cache_callback(cuda_empty_cache_steps: int | None):
    if cuda_empty_cache_steps is None:
        return None
    from transformers import TrainerCallback

    class _CudaEmptyCacheTrainerCallback(CudaEmptyCacheCallback, TrainerCallback):
        pass

    return _CudaEmptyCacheTrainerCallback(cuda_empty_cache_steps=cuda_empty_cache_steps)

def _examples_to_rows(
    examples: list[TrainingExample],
) -> list[dict[str, Any]]:
    return [
        {
            "example": example,
            "messages": example_to_messages(
                example,
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


def _render_chat(processor: Any, messages: list[ChatMessage]) -> str:
    try:
        rendered = processor.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False,
            enable_thinking=False,
        )
    except AttributeError as exc:
        raise ValueError("Real-audio training requires processor.apply_chat_template") from exc
    except TypeError:
        raise
    return str(rendered)


def _labels_from_assistant_mask(
    batch: dict[str, Any],
    *,
    processor: Any,
    spec: AssistantMaskSpec,
) -> torch.Tensor:
    input_ids = batch.get("input_ids")
    if not isinstance(input_ids, torch.Tensor):
        raise ValueError("Processor output does not contain tensor input_ids")
    try:
        tokenizer = processor.tokenizer
    except AttributeError as exc:
        raise ValueError("Assistant frame masking requires processor.tokenizer") from exc
    return build_assistant_labels(
        batch,
        tokenizer=tokenizer,
        spec=spec,
    )


class MakeSenseAudioCollator:
    """Processor-based multimodal collator with caller-configured causal audio chunks."""

    def __init__(
        self,
        processor: Any,
        *,
        audio_sampling_rate: int,
        audio_chunk_seconds: float,
        assistant_header: str,
        assistant_end: str,
        generation_stop: str,
    ) -> None:
        if not assistant_header or not assistant_end or not generation_stop:
            raise ValueError("Assistant frame spec values must be provided by the orchestration layer")
        self.processor = processor
        self.audio_sampling_rate = audio_sampling_rate
        self.audio_chunk_seconds = audio_chunk_seconds
        self.assistant_mask_spec = AssistantMaskSpec(
            assistant_header=assistant_header,
            assistant_end=assistant_end,
            generation_stop=generation_stop,
        )

    def _audio_chunks_for_example(self, example: TrainingExample) -> list[torch.Tensor]:
        return audio_chunks_for_example(
            example,
            audio_sampling_rate=self.audio_sampling_rate,
            audio_chunk_seconds=self.audio_chunk_seconds,
        )

    def _call_processor(self, rendered_texts: list[str], flat_audio_chunks: list[torch.Tensor]) -> dict[str, Any]:
        try:
            batch = self.processor(
                text=rendered_texts,
                audio=[chunk.detach().cpu().to(dtype=torch.float32).numpy() for chunk in flat_audio_chunks],
                return_tensors="pt",
                padding=True,
            )
        except AttributeError as exc:
            raise ValueError("Real-audio training requires callable processor(text=..., audio=...)") from exc
        except TypeError:
            raise
        return dict(batch)

    def __call__(self, features: list[dict[str, Any]]) -> dict[str, Any]:
        rendered_texts: list[str] = []
        flat_audio_chunks: list[torch.Tensor] = []
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
            rendered = _render_chat(self.processor, messages)
            rendered_texts.append(rendered)
            flat_audio_chunks.extend(audio_chunks)

        batch = self._call_processor(rendered_texts, flat_audio_chunks)
        batch["labels"] = _labels_from_assistant_mask(
            batch,
            processor=self.processor,
            spec=self.assistant_mask_spec,
        )
        batch.pop("assistant_masks", None)
        batch.pop("completion_mask", None)
        batch.pop("assistant_tokens_mask", None)
        return batch


def _build_train_validate_test_rows(
    splits: TrainingDatasetSplits,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]] | None, list[dict[str, Any]]]:
    train_rows = _examples_to_rows(splits.train)
    validate_rows = _examples_to_rows(splits.validate)
    test_rows = _examples_to_rows(splits.test)
    if not train_rows:
        raise ValueError("Training split is empty; adjust total_samples/split_ratio")
    return train_rows, validate_rows or None, test_rows


def _translation_window_interval(example: TrainingExample) -> int | None:
    if example.translation_mode == "natural":
        return None
    if example.translation_mode == "fixed_window":
        return int(example.tolerance_window)
    if example.translation_mode == "conservative":
        if example.min_wait_window is None:
            raise ValueError(f"Conservative translation example {example.uid} has no min_wait_window")
        return int(example.min_wait_window)
    raise ValueError(
        f"Unsupported translation mode for distribution summary: {example.translation_mode!r}"
    )


def summarize_translation_task_distribution(
    examples: list[TrainingExample],
    *,
    bin_size: int,
) -> dict[str, Any]:
    """Summarize train translation samples by mode and requested/effective window."""

    if int(bin_size) <= 0:
        raise ValueError(f"bin_size must be positive: {bin_size}")
    bin_size = int(bin_size)
    translation_examples = [example for example in examples if example.task == "translation"]
    translation_total = len(translation_examples)
    counts: dict[tuple[str, int | None, int | None], int] = {}
    for example in translation_examples:
        if example.translation_mode is None:
            raise ValueError(f"Translation example {example.uid} has no translation_mode")
        interval = _translation_window_interval(example)
        if interval is None:
            key = (example.translation_mode, None, None)
        else:
            bin_start = ((interval - 1) // bin_size) * bin_size + 1 if interval > 0 else 0
            key = (example.translation_mode, bin_start, bin_start + bin_size - 1)
        counts[key] = counts.get(key, 0) + 1

    mode_order = {"natural": 0, "fixed_window": 1, "conservative": 2}
    bins = []
    for (mode, window_start, window_end), count in sorted(
        counts.items(),
        key=lambda item: (
            mode_order.get(item[0][0], 99),
            -1 if item[0][1] is None else int(item[0][1]),
            -1 if item[0][2] is None else int(item[0][2]),
        ),
    ):
        bins.append(
            {
                "translation_mode": mode,
                "window_start": window_start,
                "window_end": window_end,
                "count": count,
                "ratio_of_translation_tasks": 0.0 if translation_total == 0 else count / translation_total,
            }
        )
    return {
        "bin_size": bin_size,
        "translation_examples": translation_total,
        "bins": bins,
    }


def _format_translation_task_distribution(summary: dict[str, Any]) -> str:
    lines = [
        f"Translation Task Distribution (bin size {summary['bin_size']})",
        f"  - TRANSLATION_EXAMPLES: {summary['translation_examples']}",
        "  - Percentages are relative to translation tasks.",
    ]
    bins = summary.get("bins", [])
    if not bins:
        lines.append("  - none")
        return "\n".join(lines)
    for item in bins:
        window_start = item["window_start"]
        window_end = item["window_end"]
        if window_start is None:
            window_label = "natural"
        elif window_start == window_end:
            window_label = str(window_start)
        else:
            window_label = f"{window_start}-{window_end}"
        ratio = float(item["ratio_of_translation_tasks"])
        lines.append(
            f"  - {item['translation_mode']} | window={window_label}: "
            f"{item['count']} ({ratio * 100:.2f}%)"
        )
    return "\n".join(lines)


def write_translation_task_distribution(
    output_dir: str | Path,
    summary: dict[str, Any],
    *,
    filename: str = "translation_task_distribution.json",
) -> Path:
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, ensure_ascii=False, indent=2)
    return output_path


def _format_startup_metadata(
    *,
    data_config: TrainingDataConfig,
    train_config: LoraTrainConfig,
    continue_plan: ContinuePlan,
    logging_dir: Path,
    tensorboard_root: Path,
    train_examples: int,
    validate_examples: int,
    test_examples: int,
    selected_test_rows: int,
    effective_batch_size: int,
    optimizer_steps_per_epoch: int,
    total_optimizer_steps: int,
    tensorboard_url: str | None,
    tensorboard_enabled: bool,
) -> str:
    checkpoint_path = "none" if train_config.checkpoint_path is None else str(train_config.checkpoint_path)
    resolved_checkpoint = "none" if continue_plan.resolved_checkpoint is None else str(continue_plan.resolved_checkpoint)
    lines = [
        "\n\n=== MakeSense LoRA Training ===",
        "",
        "Paths",
        f"  - DATASET_ROOT: {data_config.dataset_root}",
        f"  - OUTPUT_DIR: {train_config.output_dir}",
        f"  - LOGGING_DIR: {logging_dir}",
        f"  - TENSORBOARD_ROOT: {tensorboard_root}",
        "",
        "Checkpoint / Continue",
        f"  - CONTINUE_TYPE: {continue_plan.continue_type}",
        f"  - CHECKPOINT_PATH: {checkpoint_path}",
        f"  - RESOLVED_CHECKPOINT_PATH: {resolved_checkpoint}",
        f"  - SAVE_PROCESSOR: {str(train_config.save_processor).lower()}",
        f"  - CUDA_EMPTY_CACHE_STEPS: {train_config.cuda_empty_cache_steps}",
        "",
        "Dataset",
        f"  - TRAIN_EXAMPLES: {train_examples}",
        f"  - VALIDATE_EXAMPLES: {validate_examples}",
        f"  - TEST_EXAMPLES: {test_examples}",
        f"  - MAX_WINDOW_SIZE: {data_config.max_window_size}",
        "",
        "Audio",
        f"  - AUDIO_SAMPLING_RATE: {train_config.audio_sampling_rate}",
        f"  - AUDIO_CHUNK_SECONDS: {train_config.audio_chunk_seconds}",
        "",
        "Training Steps",
        f"  - OPTIMIZER: {train_config.optimizer}",
        f"  - PER_DEVICE_TRAIN_BATCH_SIZE: {train_config.per_device_train_batch_size}",
        f"  - PER_DEVICE_EVAL_BATCH_SIZE: {train_config.per_device_eval_batch_size}",
        f"  - GRADIENT_ACCUMULATION_STEPS: {train_config.gradient_accumulation_steps}",
        f"  - EFFECTIVE_BATCH_SIZE: {effective_batch_size}",
        f"    `PER_DEVICE_TRAIN_BATCH_SIZE: {train_config.per_device_train_batch_size} * GRADIENT_ACCUMULATION_STEPS: {train_config.gradient_accumulation_steps}`",
        f"  - OPTIMIZER_STEPS_PER_EPOCH: {optimizer_steps_per_epoch}",
        f"    `ceil(TRAIN_EXAMPLES: {train_examples} / EFFECTIVE_BATCH_SIZE: {effective_batch_size})`",
        f"  - CONFIGURED_NUM_TRAIN_EPOCHS: {train_config.num_train_epochs}",
        f"  - CONFIGURED_MAX_STEPS: {train_config.max_steps}",
        f"  - TOTAL_OPTIMIZER_STEPS: {total_optimizer_steps}",
    ]
    if int(train_config.max_steps) > 0:
        lines.append("    `MAX_STEPS override is active`")
    else:
        lines.append(
            f"    `OPTIMIZER_STEPS_PER_EPOCH: {optimizer_steps_per_epoch} * CONFIGURED_NUM_TRAIN_EPOCHS: {train_config.num_train_epochs}`"
        )
    lines.extend(
        [
            "",
            "Test",
            f"  - TEST_STEPS: {train_config.test_steps}",
            f"  - TEST_RECORD_COUNT: {train_config.test_record_count}",
            f"  - TEST_BATCH_SIZE: {train_config.test_batch_size}",
            f"  - TEST_CUDA_EMPTY_CACHE_STEPS: {train_config.test_cuda_empty_cache_steps}",
            f"  - TEST_ROWS_SELECTED_THIS_RUN: {selected_test_rows}",
            f"  - TEST_ROW_SELECTION_TOTAL_AVAILABLE: {test_examples}",
        ]
    )
    if tensorboard_enabled:
        lines.extend(
            [
                "",
                "TensorBoard",
                f"  - URL: {tensorboard_url}",
                f"  - LOGDIR: {tensorboard_root}",
            ]
        )
    return "\n".join(lines)


def _test_metadata(
    *,
    data_config: TrainingDataConfig,
    train_config: LoraTrainConfig,
    continue_plan: ContinuePlan,
    logging_dir: Path,
    tensorboard_root: Path,
    train_examples: int,
    validate_examples: int,
    test_examples: int,
) -> dict[str, Any]:
    return {
        "dataset_root": str(data_config.dataset_root),
        "output_dir": str(train_config.output_dir),
        "logging_dir": str(logging_dir),
        "tensorboard_root": str(tensorboard_root),
        "continue_type": continue_plan.continue_type,
        "checkpoint_path": None if train_config.checkpoint_path is None else str(train_config.checkpoint_path),
        "resolved_checkpoint_path": None if continue_plan.resolved_checkpoint is None else str(continue_plan.resolved_checkpoint),
        "model_name": train_config.model_name,
        "max_window_size": data_config.max_window_size,
        "train_examples": train_examples,
        "validate_examples": validate_examples,
        "test_examples": test_examples,
        "test_record_count": train_config.test_record_count,
    }


def train_lora(
    *,
    model: Any,
    processor: Any,
    data_config: TrainingDataConfig,
    train_config: LoraTrainConfig,
) -> None:
    """Train and save an externally prepared PEFT model with Transformers Trainer."""

    _set_seed(train_config.seed)
    if not train_config.assistant_header or not train_config.assistant_end or not train_config.generation_stop:
        raise ValueError("LoraTrainConfig requires assistant_header, assistant_end, and generation_stop")
    output_dir = Path(train_config.output_dir)
    splits = build_training_dataset(
        data_config.dataset_root,
        total_samples=data_config.total_samples,
        max_window_size=data_config.max_window_size,
        task_ratio=data_config.task_ratio,
        split_ratio=data_config.split_ratio,
        translation_task_config=data_config.translation_task_config,
        dataset_repeat=data_config.dataset_repeat,
        seed=data_config.seed,
    )
    train_rows, validate_rows, test_rows = _build_train_validate_test_rows(splits)
    translation_distribution_bin1 = summarize_translation_task_distribution(splits.train, bin_size=1)
    translation_distribution_bin4 = summarize_translation_task_distribution(splits.train, bin_size=4)
    write_translation_task_distribution(output_dir, translation_distribution_bin1)
    for row in train_rows:
        messages = row["messages"]
        _assert_message_order(messages)
        _assert_has_training_target(messages)

    from transformers import Trainer, TrainingArguments
    from transformers.integrations import TensorBoardCallback
    from transformers.trainer_callback import PrinterCallback, ProgressCallback

    continue_plan = train_config.continue_plan or ContinuePlan(
        continue_type=train_config.continue_type,
        source_checkpoint=None,
        resolved_checkpoint=None,
        checkpoint_step=None,
        trainer_resume_from_checkpoint=None,
        copied_checkpoint=False,
        copied_tensorboard=False,
        copied_test_metrics=False,
    )
    default_run_dir = output_dir / "runs" / timestamp_run_dir_name()
    logging_dir = Path(train_config.logging_dir) if train_config.logging_dir is not None else default_run_dir
    tensorboard_root = logging_dir.parent
    os.environ.setdefault("WANDB_DISABLED", "true")
    if train_config.report_to == "tensorboard":
        os.environ["TENSORBOARD_LOGGING_DIR"] = str(logging_dir)
    data_collator = MakeSenseAudioCollator(
        processor,
        audio_sampling_rate=train_config.audio_sampling_rate,
        audio_chunk_seconds=train_config.audio_chunk_seconds,
        assistant_header=train_config.assistant_header,
        assistant_end=train_config.assistant_end,
        generation_stop=train_config.generation_stop,
    )

    args = TrainingArguments(
        output_dir=str(output_dir),
        per_device_train_batch_size=train_config.per_device_train_batch_size,
        per_device_eval_batch_size=train_config.per_device_eval_batch_size,
        gradient_accumulation_steps=train_config.gradient_accumulation_steps,
        learning_rate=train_config.learning_rate,
        weight_decay=train_config.weight_decay,
        optim=training_arguments_optimizer_name(train_config.optimizer),
        adam_beta1=train_config.adam_beta1,
        adam_beta2=train_config.adam_beta2,
        lr_scheduler_type=train_config.lr_scheduler_type,
        num_train_epochs=train_config.num_train_epochs,
        warmup_steps=train_config.warmup_steps,
        logging_steps=train_config.logging_steps,
        eval_steps=train_config.eval_steps,
        prediction_loss_only=train_config.prediction_loss_only,
        eval_accumulation_steps=train_config.eval_accumulation_steps,
        save_steps=train_config.save_steps,
        max_grad_norm=train_config.max_grad_norm,
        bf16=True,
        max_steps=train_config.max_steps,
        report_to="none",
        seed=train_config.seed,
        remove_unused_columns=False,
        eval_strategy="steps" if validate_rows else "no",
        save_strategy="steps",
    )
    train_example_count = len(train_rows)
    validate_example_count = 0 if validate_rows is None else len(validate_rows)
    effective_batch_size = (
        train_config.per_device_train_batch_size * train_config.gradient_accumulation_steps
    )
    optimizer_steps_per_epoch = max(1, _math.ceil(train_example_count / effective_batch_size))
    epoch_limited_total_optimizer_steps = optimizer_steps_per_epoch * int(train_config.num_train_epochs)
    total_optimizer_steps = (
        int(train_config.max_steps)
        if int(train_config.max_steps) > 0
        else epoch_limited_total_optimizer_steps
    )
    monitoring_callback = MakeSenseMonitoringCallback(
        processor=processor,
        test_rows=test_rows,
        audio_sampling_rate=train_config.audio_sampling_rate,
        audio_chunk_seconds=train_config.audio_chunk_seconds,
        output_dir=output_dir,
        logging_dir=logging_dir,
        test_metrics_json_name=train_config.test_metrics_json_name,
        test_metadata=_test_metadata(
            data_config=data_config,
            train_config=train_config,
            continue_plan=continue_plan,
            logging_dir=logging_dir,
            tensorboard_root=tensorboard_root,
            train_examples=train_example_count,
            validate_examples=validate_example_count,
            test_examples=len(test_rows),
        ),
        test_steps=train_config.test_steps,
        test_max_new_tokens=train_config.test_max_new_tokens,
        test_record_count=train_config.test_record_count,
        test_batch_size=train_config.test_batch_size,
        test_cuda_empty_cache_steps=train_config.test_cuda_empty_cache_steps,
        test_output_markdown=train_config.test_output_markdown,
        test_outputs_dir_name=train_config.test_outputs_dir_name,
        generation_stop=train_config.generation_stop,
        total_optimizer_steps=total_optimizer_steps,
        enable_tensorboard=train_config.report_to == "tensorboard",
        enable_progress=True,
    )
    callbacks = []
    cuda_empty_cache_callback = _maybe_cuda_empty_cache_callback(train_config.cuda_empty_cache_steps)
    callbacks.append(monitoring_callback)
    if cuda_empty_cache_callback is not None:
        callbacks.append(cuda_empty_cache_callback)
    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_rows,
        eval_dataset=validate_rows,
        data_collator=data_collator,
        callbacks=callbacks,
    )
    trainer.remove_callback(PrinterCallback)
    trainer.remove_callback(ProgressCallback)
    trainer.remove_callback(TensorBoardCallback)
    monitoring_callback.latest_metrics.update(latest_logged_metrics_from_state(trainer.state))

    print(
        _format_startup_metadata(
            data_config=data_config,
            train_config=train_config,
            continue_plan=continue_plan,
            logging_dir=logging_dir,
            tensorboard_root=tensorboard_root,
            train_examples=train_example_count,
            validate_examples=validate_example_count,
            test_examples=len(test_rows),
            selected_test_rows=monitoring_callback.tester.selected_count(),
            effective_batch_size=effective_batch_size,
            optimizer_steps_per_epoch=optimizer_steps_per_epoch,
            total_optimizer_steps=total_optimizer_steps,
            tensorboard_url=(
                f"http://{train_config.tensorboard_host}:{train_config.tensorboard_port}"
                if train_config.launch_tensorboard and train_config.report_to == "tensorboard"
                else None
            ),
            tensorboard_enabled=train_config.launch_tensorboard and train_config.report_to == "tensorboard",
        )
    )
    print()
    print(_format_translation_task_distribution(translation_distribution_bin4))
    print()

    tensorboard = TensorBoardServer(
        logdir=tensorboard_root,
        host=train_config.tensorboard_host,
        port=train_config.tensorboard_port,
        enabled=train_config.launch_tensorboard and train_config.report_to == "tensorboard",
    )
    try:
        tensorboard.start()
        if continue_plan.trainer_resume_from_checkpoint is not None:
            confirm_resume_arg_mismatches(
                checkpoint=continue_plan.trainer_resume_from_checkpoint,
                current_args=args,
            )
            trainer.train(resume_from_checkpoint=str(continue_plan.trainer_resume_from_checkpoint))
        else:
            trainer.train()
        trainer.save_model(str(output_dir))
        monitoring_callback.run_final_test(model=trainer.model, step=int(trainer.state.global_step))
        if train_config.save_processor:
            try:
                processor.save_pretrained(str(output_dir))
            except AttributeError as exc:
                raise ValueError("Real-audio training requires processor.save_pretrained") from exc
            print(f"\nSaved LoRA adapter and processor to {output_dir}")
        else:
            print(f"\nSaved LoRA adapter to {output_dir}")
    finally:
        tensorboard.stop()
