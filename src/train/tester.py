"""Strict streaming evaluation helpers for MakeSense LoRA training."""

from __future__ import annotations

import re
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
    rendered = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=add_generation_prompt,
        enable_thinking=False,
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


def truncate_at_generation_stop(text: str, generation_stop: str) -> str:
    boundary_index = text.find(generation_stop)
    if boundary_index < 0:
        return text
    return text[:boundary_index]


def decode_generated_text(processor: Any, output_ids: torch.Tensor, *, generation_stop: str) -> str:
    raw_debug = processor.batch_decode(output_ids, skip_special_tokens=False)
    raw_text = str(raw_debug[0]) if raw_debug else ""
    return truncate_at_generation_stop(raw_text, generation_stop)


def decode_raw_generated_text(processor: Any, output_ids: torch.Tensor) -> str:
    raw_debug = processor.batch_decode(output_ids, skip_special_tokens=False)
    return str(raw_debug[0]) if raw_debug else ""


def model_device(model: Any) -> torch.device:
    return model.device


def move_tensor_batch_to_device(batch: dict[str, Any], device: torch.device) -> dict[str, Any]:
    return {key: value.to(device) if isinstance(value, torch.Tensor) else value for key, value in batch.items()}


class StreamingSampleTester:
    """Evaluate test rows with strict streaming audio exposure and protocol metrics."""

    def __init__(
        self,
        *,
        processor: Any,
        test_rows: list[dict[str, Any]] | None,
        collator: Any,
        test_max_new_tokens: int,
        test_record_count: int,
        generation_stop: str,
        enable_thinking: bool = False,
    ) -> None:
        if not generation_stop:
            raise ValueError("StreamingSampleTester requires generation_stop")
        self.processor = processor
        self.test_rows = test_rows or []
        self.collator = collator
        self.test_max_new_tokens = test_max_new_tokens
        self.test_record_count = int(test_record_count)
        self.generation_stop = generation_stop
        self.enable_thinking = enable_thinking

    def has_rows(self) -> bool:
        return bool(self.selected_count() > 0)

    def total_available_rows(self) -> int:
        return len(self.test_rows)

    def selected_count(self) -> int:
        total = len(self.test_rows)
        if self.test_record_count == 0:
            return 0
        if self.test_record_count == -1:
            return total
        if self.test_record_count > 0:
            return min(self.test_record_count, total)
        raise ValueError("TEST_RECORD_COUNT must be -1, 0, or a positive integer")

    def selected_rows(self) -> list[dict[str, Any]]:
        return self.test_rows[: self.selected_count()]

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
            raw_output, postprocessed_output = self.generate_turn_text(
                model=model,
                prefix_messages=prefix_messages,
                audio_chunks=audio_chunks,
            )
            protocol = parse_protocol_output(postprocessed_output)
            outputs.append(
                {
                    "ground_truth": ground_truth,
                    "raw_output": raw_output,
                    "postprocessed_output": postprocessed_output,
                    "extracted_protocol_output": protocol["normalized_output"],
                    "protocol_valid": protocol["valid"],
                    "raw_turn_stopped": raw_turn_stopped(raw_output, postprocessed_output, self.generation_stop),
                    "postprocessed_turn_stopped": postprocessed_turn_stopped(postprocessed_output, protocol),
                }
            )

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
    ) -> tuple[str, str]:
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
            max_new_tokens=self.test_max_new_tokens,
        )
        output_ids = generated[:, prompt_length:]
        raw_output = decode_raw_generated_text(self.processor, output_ids)
        postprocessed_output = decode_generated_text(
            self.processor,
            output_ids,
            generation_stop=self.generation_stop,
        )
        return raw_output, postprocessed_output

    def evaluate(self, *, model: Any, step: int, metrics: dict[str, Any]) -> dict[str, Any]:
        records = self.generate_records(model=model, step=step, metrics=metrics)
        summary_metrics = summarize_test_records(records)
        return {
            "step": step,
            "metrics": metrics,
            "test_metrics": summary_metrics,
            "total_available_test_rows": self.total_available_rows(),
            "selected_test_rows": self.selected_count(),
            "records": records,
        }

    @staticmethod
    def print_record(record: dict[str, Any]) -> None:
        print(f"  - UID: {record['uid']}")
        print(f"  - SYSTEM_PROMPT: {record['system_prompt']}")
        print()
        for index, output in enumerate(record["outputs"], start=1):
            print(
                f"{index}. {output['ground_truth']}  -  {output['postprocessed_output']}"
            )


PROTOCOL_PATTERN = re.compile(r"^<src>(.*?)</src><tgt>(.*?)</tgt>$", re.DOTALL)


def parse_protocol_output(text: str) -> dict[str, Any]:
    match = PROTOCOL_PATTERN.fullmatch(text)
    if match is None:
        return {
            "valid": False,
            "src": None,
            "tgt": None,
            "normalized_output": None,
        }
    src_text = match.group(1)
    tgt_text = match.group(2)
    if any(tag in src_text for tag in ("<src>", "</src>", "<tgt>", "</tgt>")):
        return {"valid": False, "src": None, "tgt": None, "normalized_output": None}
    if any(tag in tgt_text for tag in ("<src>", "</src>", "<tgt>", "</tgt>")):
        return {"valid": False, "src": None, "tgt": None, "normalized_output": None}
    normalized = f"<src>{src_text}</src><tgt>{tgt_text}</tgt>"
    return {
        "valid": True,
        "src": src_text,
        "tgt": tgt_text,
        "normalized_output": normalized,
    }


def _is_wait_content(text: str | None) -> bool | None:
    if text is None:
        return None
    return text.strip() == "<|wait|>"


def raw_turn_stopped(raw_output: str, postprocessed_output: str, generation_stop: str) -> bool:
    remainder = raw_output[len(postprocessed_output):]
    return remainder.startswith(generation_stop)


def postprocessed_turn_stopped(postprocessed_output: str, protocol: dict[str, Any]) -> bool:
    return bool(protocol["valid"] and postprocessed_output == protocol["normalized_output"])


def summarize_test_records(records: list[dict[str, Any]]) -> dict[str, Any]:
    total_turns = 0
    protocol_valid_turns = 0
    raw_turn_stop_turns = 0
    postprocessed_turn_stop_turns = 0
    src_wait_total = 0
    src_wait_correct = 0
    tgt_wait_total = 0
    tgt_wait_correct = 0
    src_release_total = 0
    src_release_correct = 0
    tgt_release_total = 0
    tgt_release_correct = 0

    for record in records:
        for output in record["outputs"]:
            total_turns += 1
            gt_protocol = parse_protocol_output(str(output["ground_truth"]))
            model_protocol = parse_protocol_output(str(output["postprocessed_output"]))
            if bool(output["protocol_valid"]):
                protocol_valid_turns += 1
            if bool(output["raw_turn_stopped"]):
                raw_turn_stop_turns += 1
            if bool(output["postprocessed_turn_stopped"]):
                postprocessed_turn_stop_turns += 1

            gt_src_wait = _is_wait_content(gt_protocol["src"])
            gt_tgt_wait = _is_wait_content(gt_protocol["tgt"])
            model_src_wait = _is_wait_content(model_protocol["src"])
            model_tgt_wait = _is_wait_content(model_protocol["tgt"])

            if gt_src_wait is True:
                src_wait_total += 1
                src_wait_correct += int(model_src_wait is True)
            elif gt_src_wait is False:
                src_release_total += 1
                src_release_correct += int(model_src_wait is False)

            if gt_tgt_wait is True:
                tgt_wait_total += 1
                tgt_wait_correct += int(model_tgt_wait is True)
            elif gt_tgt_wait is False:
                tgt_release_total += 1
                tgt_release_correct += int(model_tgt_wait is False)

    def _rate(correct: int, total: int) -> float:
        return 0.0 if total == 0 else correct / total

    return {
        "record_count": len(records),
        "turn_count": total_turns,
        "protocol_valid_rate": _rate(protocol_valid_turns, total_turns),
        "raw_turn_stop_rate": _rate(raw_turn_stop_turns, total_turns),
        "postprocessed_turn_stop_rate": _rate(postprocessed_turn_stop_turns, total_turns),
        "src_wait_accuracy": _rate(src_wait_correct, src_wait_total),
        "tgt_wait_accuracy": _rate(tgt_wait_correct, tgt_wait_total),
        "src_release_accuracy": _rate(src_release_correct, src_release_total),
        "tgt_release_accuracy": _rate(tgt_release_correct, tgt_release_total),
        "src_wait_total": src_wait_total,
        "tgt_wait_total": tgt_wait_total,
        "src_release_total": src_release_total,
        "tgt_release_total": tgt_release_total,
    }


def format_test_metrics_section(summary: dict[str, Any]) -> str:
    metrics = summary["test_metrics"]
    lines = [
        "",
        "",
        "Test Metrics",
        f"  - STEP: {summary['step']}",
        f"  - TOTAL_AVAILABLE_TEST_ROWS: {summary['total_available_test_rows']}",
        f"  - SELECTED_TEST_ROWS: {summary['selected_test_rows']}",
    ]
    for key in sorted(metrics):
        value = metrics[key]
        display = f"{value:.4f}" if isinstance(value, float) else str(value)
        lines.append(f"  - {key.upper()}: {display}")
    return "\n".join(lines)


def format_test_record_section(record: dict[str, Any], *, index: int, total: int) -> str:
    """Format one strict-test record using the same comparison style as stdout."""

    lines = [
        f"## Test Example {index} / {total}",
        "",
        f"  - UID: {record['uid']}",
        f"  - SYSTEM_PROMPT: {record['system_prompt']}",
        "",
    ]
    for output_index, output in enumerate(record["outputs"], start=1):
        lines.append(
            f"{output_index}. {output['ground_truth']}  -  {output['postprocessed_output']}"
        )
    return "\n".join(lines)


def format_test_outputs_markdown(summary: dict[str, Any], *, title: str | None = None) -> str:
    """Format all selected strict-test records as one Markdown document."""

    records = summary.get("records", [])
    heading = title or f"Test Outputs - step {summary['step']}"
    sections = [f"# {heading}\n\n{format_test_metrics_section(summary).strip()}"]
    total = len(records)
    for index, record in enumerate(records, start=1):
        sections.append(format_test_record_section(record, index=index, total=total))
    return "\n\n---\n\n".join(sections) + "\n"


def print_test_summary(summary: dict[str, Any]) -> None:
    print(format_test_metrics_section(summary))
    records = summary["records"]
    if not records:
        return
    print()
    print("Test Example (first record only)")
    StreamingSampleTester.print_record(records[0])