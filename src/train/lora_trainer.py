"""Thin SFTTrainer wrapper for MakeSense LoRA training.

The project-owned responsibility here is intentionally narrow:

1. read final training examples through ``build_training_dataset(...)``;
2. convert ``TrainingExample`` objects into chat ``messages``;
3. pass the resulting conversation dataset to a standard trainer;
4. save the adapter through the standard trainer API.

Model loading, Unsloth patching, LoRA attachment, and processor selection belong
to the example/orchestration layer.  This module must not guess whether a value
returned by a model loader is a tokenizer or an omni processor.

Current supported mode is text-only dry-run: ``<|audio|>`` remains a literal text
placeholder.  Real audio training needs a separate processor-based multimodal
collator design and is not faked here.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import torch

from data_loader.dataset import TrainingExample, TrainingDatasetSplits, build_training_dataset
from train.formatting import ChatMessage, example_to_messages, messages_to_chat_text


TrainingMode = Literal["text_only", "audio"]


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
    """SFTTrainer-facing controls for an externally prepared LoRA model."""

    output_dir: str | Path = "outputs/makesense_lora"
    max_seq_length: int = 8192
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
    assistant_only_loss: bool = True
    packing: bool = False
    optim: str = "adamw_8bit"
    report_to: str = "none"
    seed: int = 4021
    print_sample: bool = True
    training_mode: TrainingMode = "text_only"


def _set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def _examples_to_rows(
    examples: list[TrainingExample],
    *,
    requested_tolerance_window: int | None,
) -> list[dict[str, list[ChatMessage]]]:
    """Convert examples into conversation rows consumed by SFTTrainer."""

    return [
        {
            "messages": example_to_messages(
                example,
                requested_tolerance_window=requested_tolerance_window,
            )
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
    assistant_contents = [message["content"] for message in messages if message["role"] == "assistant"]
    if not assistant_contents:
        raise ValueError("Conversation has no assistant training target")
    if not any("<src>" in content or "<tgt>" in content for content in assistant_contents):
        raise ValueError("Assistant messages do not contain <src> or <tgt> training blocks")


def _print_sample_conversation(processor: Any, train_rows: list[dict[str, list[ChatMessage]]]) -> None:
    """Print and sanity-check one rendered chat-template sample."""

    if not train_rows:
        return
    messages = train_rows[0]["messages"]
    _assert_message_order(messages)
    _assert_has_training_target(messages)
    print("=== MakeSense sample conversation messages ===")
    for index, message in enumerate(messages):
        print(f"[{index}] {message['role']}: {message['content']}")
    print()
    print("=== MakeSense sample chat template text ===")
    print(messages_to_chat_text(processor, messages))
    print("=== End sample ===")
    print()


def _build_sft_datasets(
    splits: TrainingDatasetSplits,
    *,
    requested_tolerance_window: int | None,
) -> tuple[Any, Any, list[dict[str, list[ChatMessage]]]]:
    """Build Hugging Face datasets with a single ``messages`` column."""

    from datasets import Dataset

    train_rows = _examples_to_rows(
        splits.train,
        requested_tolerance_window=requested_tolerance_window,
    )
    validate_rows = _examples_to_rows(
        splits.validate,
        requested_tolerance_window=requested_tolerance_window,
    )
    if not train_rows:
        raise ValueError("Training split is empty; adjust total_samples/split_ratio")
    train_dataset = Dataset.from_list(train_rows)
    validate_dataset = Dataset.from_list(validate_rows) if validate_rows else None
    return train_dataset, validate_dataset, train_rows


def _require_text_only_mode(train_config: LoraTrainConfig) -> None:
    if train_config.training_mode == "text_only":
        return
    if train_config.training_mode == "audio":
        raise NotImplementedError(
            "Real audio LoRA training requires a processor-based multimodal collator "
            "over true audio messages. This trainer does not fake audio support with "
            "the text-only <|audio|> placeholder."
        )
    raise ValueError(f"Unsupported training_mode: {train_config.training_mode!r}")


def train_lora(
    *,
    model: Any,
    processor: Any,
    data_config: TrainingDataConfig,
    train_config: LoraTrainConfig,
) -> None:
    """Train and save an externally prepared LoRA model with SFTTrainer."""

    _require_text_only_mode(train_config)
    _set_seed(train_config.seed)

    splits = build_training_dataset(
        data_config.dataset_root,
        total_samples=data_config.total_samples,
        task_ratio=data_config.task_ratio,
        split_ratio=data_config.split_ratio,
        tolerance_window=data_config.tolerance_window,
        seed=data_config.seed,
    )
    train_dataset, validate_dataset, train_rows = _build_sft_datasets(
        splits,
        requested_tolerance_window=data_config.tolerance_window,
    )

    if train_config.print_sample:
        _print_sample_conversation(processor, train_rows)

    from trl import SFTConfig, SFTTrainer

    args = SFTConfig(
        output_dir=str(train_config.output_dir),
        max_length=train_config.max_seq_length,
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
        assistant_only_loss=train_config.assistant_only_loss,
        packing=train_config.packing,
        optim=train_config.optim,
        report_to=train_config.report_to,
        seed=train_config.seed,
    )
    trainer = SFTTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=validate_dataset,
        processing_class=processor,
    )

    print("=== MakeSense LoRA SFT training ===")
    print("dataset_root:", data_config.dataset_root)
    print("train_examples:", len(train_dataset))
    print("validate_examples:", 0 if validate_dataset is None else len(validate_dataset))
    print("output_dir:", train_config.output_dir)
    print("training_mode:", train_config.training_mode)
    print()

    trainer.train()
    trainer.save_model(str(train_config.output_dir))
    save_pretrained = getattr(processor, "save_pretrained", None)
    if callable(save_pretrained):
        save_pretrained(str(train_config.output_dir))
    print(f"Saved LoRA adapter and processor to {train_config.output_dir}")