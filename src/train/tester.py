"""Strict streaming evaluation helpers for MakeSense LoRA training."""

from __future__ import annotations

from typing import Any

import torch

from train.formatting import ChatMessage


def render_chat(
    processor: Any,
    messages: list[ChatMessage],
    *,
    add_generation_prompt: bool,
    enable_thinking: bool,
) -> str:
    tokenizer = processor.tokenizer
    rendered = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=add_generation_prompt,
        chat_template_kwargs={"enable_thinking": enable_thinking},
    )
    return str(rendered)


def assistant_turn_indices(messages: list[ChatMessage]) -> list[int]:
    return [index for index, message in enumerate(messages) if message["role"] == "assistant"]


def audio_slot_count(messages: list[ChatMessage]) -> int:
    count = 0
    for message in messages:
        content = message.get("content")
        if isinstance(content, list):
            count += sum(isinstance(item, dict) and item.get("type") == "audio" for item in content)
    return count


def decode_generated_text(processor: Any, output_ids: torch.Tensor) -> str:
    decoded = processor.batch_decode(output_ids, skip_special_tokens=True)
    return str(decoded[0]) if decoded else ""


def model_device(model: Any) -> torch.device:
    return model.device


def move_tensor_batch_to_device(batch: dict[str, Any], device: torch.device) -> dict[str, Any]:
    return {key: value.to(device) if isinstance(value, torch.Tensor) else value for key, value in batch.items()}


class StreamingSampleTester:
    """Evaluate a small number of rows with strict streaming audio exposure."""

    def __init__(
        self,
        *,
        processor: Any,
        sample_rows: list[dict[str, Any]] | None,
        collator: Any,
        sample_generation_max_new_tokens: int,
        sample_evaluation_record_count: int,
        enable_thinking: bool = False,
    ) -> None:
        self.processor = processor
        self.sample_rows = sample_rows or []
        self.collator = collator
        self.sample_generation_max_new_tokens = sample_generation_max_new_tokens
        self.sample_evaluation_record_count = max(0, int(sample_evaluation_record_count))
        self.enable_thinking = enable_thinking

    def has_rows(self) -> bool:
        return bool(self.sample_rows and self.sample_evaluation_record_count > 0)

    def selected_rows(self) -> list[dict[str, Any]]:
        return self.sample_rows[: self.sample_evaluation_record_count]

    @torch.no_grad()
    def generate_records(self, *, model: Any, step: int, metrics: dict[str, Any]) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        was_training = bool(model.training)
        model.eval()
        try:
            for row in self.selected_rows():
                records.append(self._generate_record_for_row(model=model, row=row, step=step, metrics=metrics))
        finally:
            if was_training:
                model.train()
        return records

    def _generate_record_for_row(
        self,
        *,
        model: Any,
        row: dict[str, Any],
        step: int,
        metrics: dict[str, Any],
    ) -> dict[str, Any]:
        example = row["example"]
        messages: list[ChatMessage] = row["messages"]
        system_prompt = str(messages[0]["content"])
        audio_chunks = self.collator._audio_chunks_for_example(example)
        outputs: list[dict[str, str]] = []

        for assistant_index in assistant_turn_indices(messages):
            prefix_messages = messages[:assistant_index]
            ground_truth = str(messages[assistant_index]["content"])
            model_output = self.generate_turn_text(
                model=model,
                prefix_messages=prefix_messages,
                audio_chunks=audio_chunks,
            )
            outputs.append({"ground_truth": ground_truth, "model_output": model_output})

        return {
            "step": step,
            "metrics": metrics,
            "uid": str(example.uid),
            "system_prompt": system_prompt,
            "outputs": outputs,
        }

    def generate_turn_text(
        self,
        *,
        model: Any,
        prefix_messages: list[ChatMessage],
        audio_chunks: list[torch.Tensor],
    ) -> str:
        slot_count = audio_slot_count(prefix_messages)
        rendered = render_chat(
            self.processor,
            prefix_messages,
            add_generation_prompt=True,
            enable_thinking=self.enable_thinking,
        )
        batch = self.collator._call_processor(rendered_texts=[rendered], flat_audio_chunks=audio_chunks[:slot_count])
        batch.pop("labels", None)
        batch.pop("assistant_masks", None)
        batch.pop("completion_mask", None)
        batch.pop("assistant_tokens_mask", None)
        input_ids = batch.get("input_ids")
        if not isinstance(input_ids, torch.Tensor):
            raise ValueError("Processor output does not contain tensor input_ids for sample generation")
        prompt_length = int(input_ids.shape[1])
        batch = move_tensor_batch_to_device(batch, model_device(model))
        generated = model.generate(
            **batch,
            max_new_tokens=self.sample_generation_max_new_tokens,
        )
        return decode_generated_text(self.processor, generated[:, prompt_length:])

    @staticmethod
    def print_record(record: dict[str, Any]) -> None:
        print(str(record["uid"]))
        print(str(record["system_prompt"]))
        for index, output in enumerate(record["outputs"], start=1):
            print(f"{index}. {output['ground_truth']}  -  {output['model_output']}")