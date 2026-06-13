"""Strict streaming evaluation helpers for MakeSense LoRA training."""

from __future__ import annotations

import re
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any

import torch

from train.formatting import ChatMessage
from train.vram import cuda_vram_usage_gib, format_vram_usage


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
        enable_thinking=enable_thinking,
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


def _as_int_token_ids(value: Any) -> list[int]:
    if value is None:
        return []
    if isinstance(value, int):
        return [int(value)]
    if isinstance(value, (list, tuple, set)):
        return [int(item) for item in value if item is not None]
    return []


def _single_token_id_for_text(processor: Any, text: str) -> int | None:
    tokenizer = getattr(processor, "tokenizer", None)
    if tokenizer is None or not text:
        return None
    try:
        tokenized = tokenizer(text, add_special_tokens=False)
    except Exception:
        return None
    input_ids = tokenized.get("input_ids") if isinstance(tokenized, dict) else getattr(tokenized, "input_ids", None)
    if isinstance(input_ids, torch.Tensor):
        ids = [int(token) for token in input_ids.detach().cpu().flatten().tolist()]
    elif isinstance(input_ids, list):
        ids = [int(token) for token in input_ids]
    else:
        return None
    return ids[0] if len(ids) == 1 else None


def generation_stop_token_ids(processor: Any, *, generation_stop: str) -> set[int]:
    tokenizer = getattr(processor, "tokenizer", None)
    stop_ids: set[int] = set()
    if tokenizer is not None:
        stop_ids.update(_as_int_token_ids(getattr(tokenizer, "all_special_ids", None)))
        stop_ids.update(_as_int_token_ids(getattr(tokenizer, "eos_token_id", None)))
        stop_ids.update(_as_int_token_ids(getattr(tokenizer, "pad_token_id", None)))
    generation_stop_id = _single_token_id_for_text(processor, generation_stop)
    if generation_stop_id is not None:
        stop_ids.add(generation_stop_id)
    return stop_ids


def truncate_output_ids_at_stop(output_ids: torch.Tensor, *, stop_token_ids: set[int]) -> torch.Tensor:
    if not stop_token_ids:
        return output_ids
    flat_ids = [int(token) for token in output_ids.detach().cpu().flatten().tolist()]
    stop_index = next((index for index, token in enumerate(flat_ids) if token in stop_token_ids), len(flat_ids))
    return output_ids[:, :stop_index]


def decode_generated_text(processor: Any, output_ids: torch.Tensor, *, generation_stop: str) -> str:
    clean_ids = truncate_output_ids_at_stop(
        output_ids,
        stop_token_ids=generation_stop_token_ids(processor, generation_stop=generation_stop),
    )
    raw_debug = processor.batch_decode(clean_ids, skip_special_tokens=True)
    raw_text = str(raw_debug[0]) if raw_debug else ""
    return truncate_at_generation_stop(raw_text, generation_stop)


def decode_raw_generated_text(processor: Any, output_ids: torch.Tensor) -> str:
    raw_debug = processor.batch_decode(output_ids, skip_special_tokens=False)
    return str(raw_debug[0]) if raw_debug else ""


def model_device(model: Any) -> torch.device:
    return model.device


def move_tensor_batch_to_device(batch: dict[str, Any], device: torch.device) -> dict[str, Any]:
    return {key: value.to(device) if isinstance(value, torch.Tensor) else value for key, value in batch.items()}


def _pop_training_only_processor_keys(batch: dict[str, Any]) -> dict[str, Any]:
    batch.pop("labels", None)
    batch.pop("assistant_masks", None)
    batch.pop("completion_mask", None)
    batch.pop("assistant_tokens_mask", None)
    return batch


_MISSING = object()


@contextmanager
def temporarily_enable_generation_cache(model: Any):
    """Temporarily set model generation cache flags and restore them afterward."""

    touched: list[tuple[Any, str, Any]] = []
    for owner in (getattr(model, "config", None), getattr(model, "generation_config", None)):
        if owner is not None and hasattr(owner, "use_cache"):
            touched.append((owner, "use_cache", getattr(owner, "use_cache", _MISSING)))
            setattr(owner, "use_cache", True)
    try:
        yield
    finally:
        for owner, name, old_value in reversed(touched):
            if old_value is _MISSING:
                try:
                    delattr(owner, name)
                except AttributeError:
                    pass
            else:
                setattr(owner, name, old_value)


@dataclass
class _RolloutRecordState:
    example: Any
    messages: list[ChatMessage]
    system_prompt: str
    assistant_indices: list[int]
    audio_chunks: list[torch.Tensor]
    outputs: list[dict[str, str]]
    rollout_messages: list[ChatMessage]
    record_index: int
    record_count: int
    next_turn_offset: int = 0

    def done(self) -> bool:
        return self.next_turn_offset >= len(self.assistant_indices)


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
        test_batch_size: int = 1,
        test_cuda_empty_cache_steps: int | None = None,
        generation_do_sample: bool | None = None,
        generation_temperature: float | None = None,
        generation_top_p: float | None = None,
        generation_top_k: int | None = None,
    ) -> None:
        if not generation_stop:
            raise ValueError("StreamingSampleTester requires generation_stop")
        if int(test_batch_size) <= 0:
            raise ValueError("test_batch_size must be positive")
        if test_cuda_empty_cache_steps is not None and int(test_cuda_empty_cache_steps) <= 0:
            raise ValueError("test_cuda_empty_cache_steps must be positive when provided")
        if generation_temperature is not None and float(generation_temperature) < 0:
            raise ValueError("generation_temperature must be positive when provided")
        if generation_top_p is not None and not 0 < float(generation_top_p) <= 1:
            raise ValueError("generation_top_p must be in (0, 1] when provided")
        if generation_top_k is not None and int(generation_top_k) < 0:
            raise ValueError("generation_top_k must be non-negative when provided")
        self.processor = processor
        self.test_rows = test_rows or []
        self.collator = collator
        self.test_max_new_tokens = test_max_new_tokens
        self.test_record_count = int(test_record_count)
        self.generation_stop = generation_stop
        self.enable_thinking = enable_thinking
        self.test_batch_size = int(test_batch_size)
        self.test_cuda_empty_cache_steps = (
            None if test_cuda_empty_cache_steps is None else int(test_cuda_empty_cache_steps)
        )
        self.generation_do_sample = generation_do_sample
        self.generation_temperature = None if generation_temperature is None else float(generation_temperature)
        self.generation_top_p = None if generation_top_p is None else float(generation_top_p)
        self.generation_top_k = None if generation_top_k is None else int(generation_top_k)
        self._generate_batch_count = 0
        self._last_generate_vram_usage: tuple[float, float, float, float] | None = None

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
        """Generate selected records via batched full prompt recomputation.

        Batching is only across records at their current rollout frontier.  Turns
        inside one record remain sequential because each later prompt depends on
        the previous model-generated assistant output.
        """

        selected_rows = self.selected_rows()
        progress = self._make_test_progress_bar(step=step, rows=selected_rows)
        was_training = bool(model.training)
        model.eval()
        try:
            states = [
                self._make_rollout_state(row=row, record_index=index, record_count=len(selected_rows))
                for index, row in enumerate(selected_rows, start=1)
            ]
            with temporarily_enable_generation_cache(model):
                while True:
                    active_states = [state for state in states if not state.done()]
                    if not active_states:
                        break
                    for start in range(0, len(active_states), self.test_batch_size):
                        self._generate_next_turn_batch(
                            model=model,
                            states=active_states[start:start + self.test_batch_size],
                            step=step,
                            progress=progress,
                        )
            records = [self._record_from_state(state, step=step, metrics=metrics) for state in states]
        finally:
            self._close_test_progress_bar(progress)
            if was_training:
                model.train()
        return records

    def _make_rollout_state(
        self,
        *,
        row: dict[str, Any],
        record_index: int,
        record_count: int,
    ) -> _RolloutRecordState:
        example = row["example"]
        messages: list[ChatMessage] = row["messages"]
        return _RolloutRecordState(
            example=example,
            messages=messages,
            system_prompt=str(messages[0]["content"]),
            assistant_indices=assistant_turn_indices(messages),
            audio_chunks=self.collator._audio_chunks_for_example(example),
            outputs=[],
            rollout_messages=[messages[0]],
            record_index=record_index,
            record_count=record_count,
        )

    def _generate_next_turn_batch(
        self,
        *,
        model: Any,
        states: list[_RolloutRecordState],
        step: int,
        progress: Any | None,
    ) -> None:
        rendered_texts: list[str] = []
        flat_audio_chunks: list[torch.Tensor] = []
        ground_truths: list[str] = []

        for state in states:
            turn_number = state.next_turn_offset + 1
            assistant_index = state.assistant_indices[state.next_turn_offset]
            user_index = assistant_index - 1
            if user_index <= 0 or state.messages[user_index]["role"] != "user":
                raise ValueError(
                    f"Expected user message before assistant turn {turn_number} for {state.example.uid}"
                )
            state.rollout_messages.append(state.messages[user_index])
            ground_truths.append(str(state.messages[assistant_index]["content"]))
            slot_count = audio_slot_count(state.rollout_messages)
            rendered_texts.append(
                render_chat(
                    self.processor,
                    state.rollout_messages,
                    add_generation_prompt=True,
                    enable_thinking=self.enable_thinking,
                )
            )
            flat_audio_chunks.extend(state.audio_chunks[:slot_count])

        output_ids_batch = self._generate_output_ids_batch(
            model=model,
            rendered_texts=rendered_texts,
            flat_audio_chunks=flat_audio_chunks,
        )
        for state, output_ids, ground_truth in zip(states, output_ids_batch, ground_truths, strict=True):
            raw_output = decode_raw_generated_text(self.processor, output_ids)
            postprocessed_output = decode_generated_text(
                self.processor,
                output_ids,
                generation_stop=self.generation_stop,
            )
            state.rollout_messages.append({"role": "assistant", "content": postprocessed_output})
            protocol = parse_protocol_output(postprocessed_output)
            state.outputs.append(
                {
                    "ground_truth": ground_truth,
                    "raw_output": raw_output,
                    "postprocessed_output": postprocessed_output,
                    "extracted_protocol_output": protocol["normalized_output"],
                    "protocol_valid": protocol["valid"],
                    "raw_turn_stopped": raw_turn_stopped(raw_output, postprocessed_output, self.generation_stop),
                    "postprocessed_turn_stopped": postprocessed_turn_stopped(
                        postprocessed_output,
                        protocol,
                        generation_stop=self.generation_stop,
                    ),
                }
            )
            state.next_turn_offset += 1
            self._update_test_progress_description(
                progress,
                step=step,
                uid=str(state.example.uid),
                record_index=state.record_index,
                record_count=state.record_count,
                turn_number=state.next_turn_offset,
                turn_count=len(state.assistant_indices),
                vram_usage=self._last_generate_vram_usage,
            )
            self._advance_test_progress(progress)

    def _generate_output_ids_batch(
        self,
        *,
        model: Any,
        rendered_texts: list[str],
        flat_audio_chunks: list[torch.Tensor],
    ) -> list[torch.Tensor]:
        if not rendered_texts:
            return []
        batch = self.collator._call_processor(rendered_texts=rendered_texts, flat_audio_chunks=flat_audio_chunks)
        generated: torch.Tensor | Any | None = None
        input_ids: torch.Tensor | None = None
        try:
            batch = _pop_training_only_processor_keys(batch)
            input_ids = batch.get("input_ids")
            if not isinstance(input_ids, torch.Tensor):
                raise ValueError("Processor output does not contain tensor input_ids for sample generation")
            attention_mask = batch.get("attention_mask")
            if isinstance(attention_mask, torch.Tensor):
                prompt_lengths = [int(length) for length in attention_mask.sum(dim=1).detach().cpu().tolist()]
            else:
                prompt_lengths = [int(input_ids.shape[1])] * int(input_ids.shape[0])
            padded_prompt_length = int(input_ids.shape[1])
            batch = move_tensor_batch_to_device(batch, model_device(model))
            generated = model.generate(
                **batch,
                max_new_tokens=self.test_max_new_tokens,
                use_cache=True,
                **self._generation_sampling_kwargs(),
            )
            if not isinstance(generated, torch.Tensor):
                sequences = getattr(generated, "sequences", None)
                if not isinstance(sequences, torch.Tensor):
                    raise ValueError("model.generate did not return tensor sequences")
                generated = sequences
            output_ids: list[torch.Tensor] = []
            for row_index, prompt_length in enumerate(prompt_lengths):
                start = padded_prompt_length if int(generated.shape[1]) >= padded_prompt_length else prompt_length
                output_ids.append(generated[row_index:row_index + 1, start:].detach().cpu())
            self._last_generate_vram_usage = cuda_vram_usage_gib(reset_peak=False)
            return output_ids
        finally:
            del generated
            del input_ids
            del batch
            self._maybe_empty_cuda_cache_after_generate()

    def _generation_sampling_kwargs(self) -> dict[str, Any]:
        kwargs: dict[str, Any] = {}
        if self.generation_do_sample is not None:
            kwargs["do_sample"] = bool(self.generation_do_sample)
        if self.generation_temperature is not None:
            kwargs["temperature"] = self.generation_temperature
        if self.generation_top_p is not None:
            kwargs["top_p"] = self.generation_top_p
        if self.generation_top_k is not None:
            kwargs["top_k"] = self.generation_top_k
        return kwargs

    def _maybe_empty_cuda_cache_after_generate(self) -> None:
        if self.test_cuda_empty_cache_steps is None:
            return
        self._generate_batch_count += 1
        if self._generate_batch_count % self.test_cuda_empty_cache_steps == 0 and torch.cuda.is_available():
            torch.cuda.empty_cache()

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
        with temporarily_enable_generation_cache(model):
            output_ids = self._generate_output_ids_batch(
                model=model,
                rendered_texts=[rendered],
                flat_audio_chunks=audio_chunks[:slot_count],
            )[0]
        raw_output = decode_raw_generated_text(self.processor, output_ids)
        postprocessed_output = decode_generated_text(
            self.processor,
            output_ids,
            generation_stop=self.generation_stop,
        )
        return raw_output, postprocessed_output

    @staticmethod
    def _record_from_state(
        state: _RolloutRecordState,
        *,
        step: int,
        metrics: dict[str, Any],
    ) -> dict[str, Any]:
        return {
            "step": step,
            "metrics": metrics,
            "uid": str(state.example.uid),
            "system_prompt": state.system_prompt,
            "outputs": state.outputs,
        }

    def evaluate(
        self,
        *,
        model: Any,
        step: int,
        metrics: dict[str, Any],
    ) -> dict[str, Any]:
        records = self.generate_records(model=model, step=step, metrics=metrics)
        summary_metrics = summarize_test_records(records)
        return {
            "step": step,
            "metrics": metrics,
            "test_batch_size": self.test_batch_size,
            "test_metrics": summary_metrics,
            "total_available_test_rows": self.total_available_rows(),
            "selected_test_rows": self.selected_count(),
            "records": records,
        }

    def _make_test_progress_bar(self, *, step: int, rows: list[dict[str, Any]]) -> Any | None:
        total_turns = sum(len(assistant_turn_indices(row["messages"])) for row in rows)
        if total_turns <= 0:
            return None
        from tqdm.auto import tqdm

        return tqdm(
            total=total_turns,
            desc=f"strict-test step={int(step)}",
            unit="turn",
            dynamic_ncols=False,
            leave=True,
        )

    @staticmethod
    def _update_test_progress_description(
        progress: Any | None,
        *,
        step: int,
        uid: str,
        record_index: int | None,
        record_count: int | None,
        turn_number: int,
        turn_count: int,
        vram_usage: tuple[float, float, float, float] | None = None,
    ) -> None:
        if progress is None:
            return
        record_text = "?/?" if record_index is None or record_count is None else f"{record_index}/{record_count}"
        progress.set_description_str(
            f"strict-test step={int(step)} record={record_text} turn={turn_number}/{turn_count} "
            f"uid={uid} | {format_vram_usage(vram_usage)}"
        )

    @staticmethod
    def _advance_test_progress(progress: Any | None) -> None:
        if progress is not None:
            progress.update(1)

    @staticmethod
    def _close_test_progress_bar(progress: Any | None) -> None:
        if progress is not None:
            progress.close()

    @staticmethod
    def print_record(record: dict[str, Any]) -> None:
        print(f"  - UID: {record['uid']}")
        print(f"  - SYSTEM_PROMPT: {record['system_prompt']}")
        print()
        for index, output in enumerate(record["outputs"], start=1):
            print(
                f"{index}. {output['ground_truth']}  -  {output['postprocessed_output']}"
            )


PROTOCOL_TAG_PATTERN = re.compile(r"</?(?:src|tgt)>")
PROTOCOL_TAGS = ("<src>", "</src>", "<tgt>", "</tgt>")
DEFAULT_ALLOWED_EOS_REMAINDERS = ("<turn|>", "<eos>", "</s>", "<|end_of_text|>")


def parse_protocol_output(text: str) -> dict[str, Any]:
    if not text.startswith("<src>"):
        return {
            "valid": False,
            "kind": None,
            "src": None,
            "tgt": None,
            "normalized_output": None,
            "remainder": text,
            "stopped_at_protocol_boundary": False,
        }

    src_start = len("<src>")
    src_end = text.find("</src>", src_start)
    if src_end < 0:
        return _invalid_protocol_result(text)
    src_text = text[src_start:src_end]
    if _contains_protocol_tag(src_text):
        return _invalid_protocol_result(text)

    unit_end = src_end + len("</src>")
    tgt_text: str | None = None
    kind = "asr"
    if text.startswith("<tgt>", unit_end):
        tgt_start = unit_end + len("<tgt>")
        tgt_end = text.find("</tgt>", tgt_start)
        if tgt_end < 0:
            return _invalid_protocol_result(text)
        tgt_text = text[tgt_start:tgt_end]
        if _contains_protocol_tag(tgt_text):
            return _invalid_protocol_result(text)
        unit_end = tgt_end + len("</tgt>")
        kind = "translation"

    remainder = text[unit_end:]
    if not _protocol_tags_are_balanced(remainder):
        return _invalid_protocol_result(text, remainder=remainder)

    normalized = f"<src>{src_text}</src>"
    if tgt_text is not None:
        normalized = f"{normalized}<tgt>{tgt_text}</tgt>"
    return {
        "valid": True,
        "kind": kind,
        "src": src_text,
        "tgt": tgt_text,
        "normalized_output": normalized,
        "remainder": remainder,
        "stopped_at_protocol_boundary": _is_allowed_eos_remainder(remainder),
    }


def _invalid_protocol_result(text: str, *, remainder: str | None = None) -> dict[str, Any]:
    return {
        "valid": False,
        "kind": None,
        "src": None,
        "tgt": None,
        "normalized_output": None,
        "remainder": text if remainder is None else remainder,
        "stopped_at_protocol_boundary": False,
    }


def _contains_protocol_tag(text: str) -> bool:
    return any(tag in text for tag in PROTOCOL_TAGS)


def _protocol_tags_are_balanced(text: str) -> bool:
    stack: list[str] = []
    for match in PROTOCOL_TAG_PATTERN.finditer(text):
        tag = match.group(0)
        if tag == "<src>":
            if stack:
                return False
            stack.append("src")
        elif tag == "<tgt>":
            if stack:
                return False
            stack.append("tgt")
        elif tag == "</src>":
            if stack != ["src"]:
                return False
            stack.pop()
        elif tag == "</tgt>":
            if stack != ["tgt"]:
                return False
            stack.pop()
    return not stack


def _is_allowed_eos_remainder(text: str, *, generation_stop: str | None = None) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    allowed = set(DEFAULT_ALLOWED_EOS_REMAINDERS)
    if generation_stop:
        allowed.add(generation_stop)
    return stripped in allowed


def _is_wait_content(text: str | None) -> bool | None:
    if text is None:
        return None
    return text.strip() == "<|wait|>"


def raw_turn_stopped(raw_output: str, postprocessed_output: str, generation_stop: str) -> bool:
    remainder = raw_output[len(postprocessed_output):]
    return remainder.startswith(generation_stop)


def postprocessed_turn_stopped(
    postprocessed_output: str,
    protocol: dict[str, Any],
    *,
    generation_stop: str | None = None,
) -> bool:
    if not bool(protocol["valid"]):
        return False
    return _is_allowed_eos_remainder(str(protocol.get("remainder") or ""), generation_stop=generation_stop)


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