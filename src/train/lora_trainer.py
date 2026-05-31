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
from mm_assistant_mask import (
    AssistantFrameSpec,
    build_assistant_frame_masks,
    build_labels_from_frame_mask,
)

from data_loader.dataset import TrainingExample, TrainingDatasetSplits, build_training_dataset
from train.continue_utils import ContinuePlan, confirm_resume_arg_mismatches, timestamp_run_dir_name
from train.formatting import ChatMessage, example_to_messages
from train.monitoring import MakeSenseMonitoringCallback, TensorBoardServer, latest_logged_metrics_from_state

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
    adam_beta1: float = 0.9
    adam_beta2: float = 0.999
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
    test_metrics_json_name: str = "test_metrics.json"
    test_steps: int = 0
    test_max_new_tokens: int = 256
    test_record_count: int = 1
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


def _labels_from_assistant_frames(
    batch: dict[str, Any],
    *,
    processor: Any,
    frame_spec: AssistantFrameSpec,
) -> torch.Tensor:
    input_ids = batch.get("input_ids")
    if not isinstance(input_ids, torch.Tensor):
        raise ValueError("Processor output does not contain tensor input_ids")
    try:
        tokenizer = processor.tokenizer
    except AttributeError as exc:
        raise ValueError("Assistant frame masking requires processor.tokenizer") from exc
    frame_mask = build_assistant_frame_masks(
        input_ids=input_ids,
        tokenizer=tokenizer,
        spec=frame_spec,
    )
    return build_labels_from_frame_mask(
        input_ids=input_ids,
        frame_mask=frame_mask,
        attention_mask=batch.get("attention_mask"),
    )


class MakeSenseAudioCollator:
    """Processor-based multimodal collator with caller-configured causal audio chunks."""

    def __init__(
        self,
        processor: Any,
        *,
        max_length: int,
        audio_sampling_rate: int,
        audio_chunk_seconds: float,
        assistant_header: str,
        assistant_end: str,
        generation_stop: str,
    ) -> None:
        if not assistant_header or not assistant_end or not generation_stop:
            raise ValueError("Assistant frame spec values must be provided by the orchestration layer")
        self.processor = processor
        self.max_length = max_length
        self.audio_sampling_rate = audio_sampling_rate
        self.audio_chunk_seconds = audio_chunk_seconds
        self.assistant_frame_spec = AssistantFrameSpec(
            assistant_header=assistant_header,
            assistant_end=assistant_end,
            generation_stop=generation_stop,
        )

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

        batch = self._call_processor(rendered_texts, flat_audio_chunks)
        batch["labels"] = _labels_from_assistant_frames(
            batch,
            processor=self.processor,
            frame_spec=self.assistant_frame_spec,
        )
        batch.pop("assistant_masks", None)
        batch.pop("completion_mask", None)
        batch.pop("assistant_tokens_mask", None)
        return batch


def _build_train_validate_test_rows(
    splits: TrainingDatasetSplits,
    *,
    requested_tolerance_window: int | None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]] | None, list[dict[str, Any]]]:
    train_rows = _examples_to_rows(splits.train, requested_tolerance_window=requested_tolerance_window)
    validate_rows = _examples_to_rows(splits.validate, requested_tolerance_window=requested_tolerance_window)
    test_rows = _examples_to_rows(splits.test, requested_tolerance_window=requested_tolerance_window)
    if not train_rows:
        raise ValueError("Training split is empty; adjust total_samples/split_ratio")
    return train_rows, validate_rows or None, test_rows


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
        "",
        "Dataset",
        f"  - TRAIN_EXAMPLES: {train_examples}",
        f"  - VALIDATE_EXAMPLES: {validate_examples}",
        f"  - TEST_EXAMPLES: {test_examples}",
        "",
        "Audio",
        f"  - AUDIO_SAMPLING_RATE: {train_config.audio_sampling_rate}",
        f"  - AUDIO_CHUNK_SECONDS: {train_config.audio_chunk_seconds}",
        "",
        "Training Steps",
        f"  - PER_DEVICE_TRAIN_BATCH_SIZE: {train_config.per_device_train_batch_size}",
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
    splits = build_training_dataset(
        data_config.dataset_root,
        total_samples=data_config.total_samples,
        task_ratio=data_config.task_ratio,
        split_ratio=data_config.split_ratio,
        tolerance_window=data_config.tolerance_window,
        seed=data_config.seed,
    )
    train_rows, validate_rows, test_rows = _build_train_validate_test_rows(
        splits,
        requested_tolerance_window=data_config.tolerance_window,
    )
    for row in train_rows:
        messages = row["messages"]
        _assert_message_order(messages)
        _assert_has_training_target(messages)

    from transformers import Trainer, TrainingArguments
    from transformers.integrations import TensorBoardCallback
    from transformers.trainer_callback import PrinterCallback, ProgressCallback

    output_dir = Path(train_config.output_dir)
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
        max_length=train_config.max_seq_length,
        audio_sampling_rate=train_config.audio_sampling_rate,
        audio_chunk_seconds=train_config.audio_chunk_seconds,
        assistant_header=train_config.assistant_header,
        assistant_end=train_config.assistant_end,
        generation_stop=train_config.generation_stop,
    )

    args = TrainingArguments(
        output_dir=str(output_dir),
        per_device_train_batch_size=train_config.per_device_train_batch_size,
        gradient_accumulation_steps=train_config.gradient_accumulation_steps,
        learning_rate=train_config.learning_rate,
        weight_decay=train_config.weight_decay,
        adam_beta1=train_config.adam_beta1,
        adam_beta2=train_config.adam_beta2,
        num_train_epochs=train_config.num_train_epochs,
        warmup_steps=train_config.warmup_steps,
        logging_steps=train_config.logging_steps,
        eval_steps=train_config.eval_steps,
        save_steps=train_config.save_steps,
        max_grad_norm=train_config.max_grad_norm,
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
    callbacks = [
        MakeSenseMonitoringCallback(
            processor=processor,
            test_rows=test_rows,
            collator=data_collator,
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
            test_output_markdown=train_config.test_output_markdown,
            test_outputs_dir_name=train_config.test_outputs_dir_name,
            generation_stop=train_config.generation_stop,
            total_optimizer_steps=total_optimizer_steps,
            enable_tensorboard=train_config.report_to == "tensorboard",
            enable_progress=True,
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
    trainer.remove_callback(ProgressCallback)
    trainer.remove_callback(TensorBoardCallback)
    callbacks[0].latest_metrics.update(latest_logged_metrics_from_state(trainer.state))

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
            selected_test_rows=callbacks[0].tester.selected_count(),
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
        callbacks[0].run_final_test(model=trainer.model, step=int(trainer.state.global_step))
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
