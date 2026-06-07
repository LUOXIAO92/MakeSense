"""Strict streaming evaluation helpers for MakeSense LoRA training."""

from __future__ import annotations

import re
from dataclasses import dataclass
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


def _pop_training_only_processor_keys(batch: dict[str, Any]) -> dict[str, Any]:
    batch.pop("labels", None)
    batch.pop("assistant_masks", None)
    batch.pop("completion_mask", None)
    batch.pop("assistant_tokens_mask", None)
    return batch


def _past_key_values_from_output(output: Any) -> Any:
    past_key_values = getattr(output, "past_key_values", None)
    if past_key_values is None and isinstance(output, dict):
        past_key_values = output.get("past_key_values")
    if past_key_values is None:
        raise ValueError("Model output does not contain past_key_values for prefill-cache reuse")
    return past_key_values


@dataclass(frozen=True)
class PromptPrefillCacheState:
    """KV cache plus exact rendered/token/audio prefix represented by it."""

    rendered_text: str
    input_ids: torch.Tensor
    audio_slots: int
    past_key_values: Any


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
        """Generate selected records without prompt-prefill reuse.

        This method is kept as a backup/debug baseline only. Normal training
        monitoring uses ``generate_records_with_prefill_cache(...)`` directly;
        switch to this method in code only when debugging the prefill path.
        """

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
        assistant_indices = assistant_turn_indices(messages)
        audio_chunks = self.collator._audio_chunks_for_example(example)
        outputs: list[dict[str, str]] = []
        rollout_messages: list[ChatMessage] = [messages[0]]

        for turn_number, assistant_index in enumerate(assistant_indices, start=1):
            user_index = assistant_index - 1
            if user_index <= 0 or messages[user_index]["role"] != "user":
                raise ValueError(
                    f"Expected user message before assistant turn {turn_number} for {example.uid}"
                )
            rollout_messages.append(messages[user_index])
            ground_truth = str(messages[assistant_index]["content"])
            raw_output, postprocessed_output = self.generate_turn_text(
                model=model,
                prefix_messages=rollout_messages,
                audio_chunks=audio_chunks,
            )
            rollout_messages.append(
                {
                    "role": "assistant",
                    "content": postprocessed_output,
                }
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

    @torch.no_grad()
    def generate_records_with_prefill_cache(
        self,
        *,
        model: Any,
        step: int,
        metrics: dict[str, Any],
    ) -> list[dict[str, Any]]:
        """Generate selected records with experimental cross-turn prompt prefill reuse.

        This is the normal training-monitoring path. ``generate_records`` is
        retained only as a backup/debug baseline. The method keeps the same
        real-rollout semantics: generated assistant text is appended to the
        conversation before exposing the next audio turn.
        """

        records: list[dict[str, Any]] = []
        was_training = bool(model.training)
        model.eval()
        try:
            for row in self.selected_rows():
                records.append(
                    self._generate_record_for_row_with_prefill_cache(
                        model=model,
                        row=row,
                        step=step,
                        metrics=metrics,
                    )
                )
        finally:
            if was_training:
                model.train()
        return records

    def _generate_record_for_row_with_prefill_cache(
        self,
        *,
        model: Any,
        row: dict[str, Any],
        step: int,
        metrics: dict[str, Any],
    ) -> dict[str, Any]:
        """Generate one record with real rollout and reusable prompt KV cache."""

        example = row["example"]
        messages: list[ChatMessage] = row["messages"]
        system_prompt = str(messages[0]["content"])
        assistant_indices = assistant_turn_indices(messages)
        audio_chunks = self.collator._audio_chunks_for_example(example)
        outputs: list[dict[str, str]] = []
        rollout_messages: list[ChatMessage] = [messages[0]]
        cache_state: PromptPrefillCacheState | None = None

        for turn_number, assistant_index in enumerate(assistant_indices, start=1):
            user_index = assistant_index - 1
            if user_index <= 0 or messages[user_index]["role"] != "user":
                raise ValueError(
                    f"Expected user message before assistant turn {turn_number} for {example.uid}"
                )
            rollout_messages.append(messages[user_index])
            ground_truth = str(messages[assistant_index]["content"])
            raw_output, postprocessed_output = self.generate_turn_text_with_prefill_cache(
                model=model,
                prefix_messages=rollout_messages,
                audio_chunks=audio_chunks,
                cache_state=cache_state,
            )
            rollout_messages.append(
                {
                    "role": "assistant",
                    "content": postprocessed_output,
                }
            )
            cache_state = self.prefill_prompt_cache_for_messages(
                model=model,
                messages=rollout_messages,
                audio_chunks=audio_chunks,
                add_generation_prompt=False,
                cache_state=cache_state,
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

    def generate_turn_text_with_prefill_cache(
        self,
        *,
        model: Any,
        prefix_messages: list[ChatMessage],
        audio_chunks: list[torch.Tensor],
        cache_state: PromptPrefillCacheState | None,
    ) -> tuple[str, str]:
        """Generate one turn by reusing cached prompt prefill when possible.

        ``cache_state`` must describe the exact text/token/audio prefix
        represented by its ``past_key_values``. The method validates both the
        rendered-string prefix and token prefix, then processor-encodes only the
        newly appended rendered suffix with only newly exposed audio chunks. A
        mismatch is treated as an error rather than silently falling back,
        because silent fallback would make benchmark timing ambiguous.
        """

        full_batch, full_input_ids, slot_count, full_rendered = self._processor_batch_for_messages(
            messages=prefix_messages,
            audio_chunks=audio_chunks,
            add_generation_prompt=True,
        )
        suffix_batch, suffix_input_ids, prefix_length = self._suffix_batch_for_cache_state(
            full_batch=full_batch,
            full_input_ids=full_input_ids,
            full_rendered=full_rendered,
            full_audio_slots=slot_count,
            all_audio_chunks=audio_chunks,
            cache_state=cache_state,
        )
        if int(suffix_input_ids.shape[1]) <= 0:
            raise ValueError("Prefill-cache generation requires a non-empty prompt suffix")
        suffix_batch = move_tensor_batch_to_device(suffix_batch, model_device(model))
        if cache_state is not None:
            suffix_batch["past_key_values"] = cache_state.past_key_values
        generated = model.generate(
            **suffix_batch,
            max_new_tokens=self.test_max_new_tokens,
            use_cache=True,
            return_dict_in_generate=True,
            output_scores=False,
        )
        sequences = getattr(generated, "sequences", generated)
        if not isinstance(sequences, torch.Tensor):
            raise ValueError("model.generate did not return tensor sequences for prefill-cache generation")
        output_ids = self._extract_generated_suffix_output_ids(
            sequences=sequences,
            full_input_ids=full_input_ids.to(sequences.device),
            suffix_input_ids=suffix_input_ids.to(sequences.device),
        )
        raw_output = decode_raw_generated_text(self.processor, output_ids)
        postprocessed_output = decode_generated_text(
            self.processor,
            output_ids,
            generation_stop=self.generation_stop,
        )
        return raw_output, postprocessed_output

    def prefill_prompt_cache_for_messages(
        self,
        *,
        model: Any,
        messages: list[ChatMessage],
        audio_chunks: list[torch.Tensor],
        add_generation_prompt: bool,
        cache_state: PromptPrefillCacheState | None,
    ) -> PromptPrefillCacheState:
        """Return KV cache for the canonical rendered prompt for ``messages``."""

        full_batch, full_input_ids, slot_count, full_rendered = self._processor_batch_for_messages(
            messages=messages,
            audio_chunks=audio_chunks,
            add_generation_prompt=add_generation_prompt,
        )
        suffix_batch, suffix_input_ids, prefix_length = self._suffix_batch_for_cache_state(
            full_batch=full_batch,
            full_input_ids=full_input_ids,
            full_rendered=full_rendered,
            full_audio_slots=slot_count,
            all_audio_chunks=audio_chunks,
            cache_state=cache_state,
        )
        if int(suffix_input_ids.shape[1]) <= 0:
            if cache_state is None:
                raise ValueError("Initial prompt prefill cache update requires a non-empty prompt")
            return cache_state
        if prefix_length == int(full_input_ids.shape[1]) and cache_state is not None:
            return cache_state
        if prefix_length > 0 and cache_state is None:
            raise ValueError("Internal error: non-zero cached prefix without cache state")
        if prefix_length == int(full_input_ids.shape[1]):
            raise ValueError("Prompt prefill cache update requires a non-empty suffix")
        suffix_batch = move_tensor_batch_to_device(suffix_batch, model_device(model))
        if cache_state is not None:
            suffix_batch["past_key_values"] = cache_state.past_key_values
        output = model(
            **suffix_batch,
            use_cache=True,
            return_dict=True,
        )
        return PromptPrefillCacheState(
            rendered_text=full_rendered,
            input_ids=full_input_ids.detach().cpu(),
            audio_slots=slot_count,
            past_key_values=_past_key_values_from_output(output),
        )

    def _processor_batch_for_messages(
        self,
        *,
        messages: list[ChatMessage],
        audio_chunks: list[torch.Tensor],
        add_generation_prompt: bool,
    ) -> tuple[dict[str, Any], torch.Tensor, int, str]:
        slot_count = audio_slot_count(messages)
        rendered = render_chat(
            self.processor,
            messages,
            add_generation_prompt=add_generation_prompt,
            enable_thinking=self.enable_thinking,
        )
        batch = self.collator._call_processor(rendered_texts=[rendered], flat_audio_chunks=audio_chunks[:slot_count])
        batch = _pop_training_only_processor_keys(batch)
        input_ids = batch.get("input_ids")
        if not isinstance(input_ids, torch.Tensor):
            raise ValueError("Processor output does not contain tensor input_ids for prefill-cache generation")
        if int(input_ids.shape[0]) != 1:
            raise ValueError("Prefill-cache tester only supports one generated sample at a time")
        return batch, input_ids.detach().cpu(), slot_count, rendered

    def _processor_batch_for_rendered_suffix(
        self,
        *,
        rendered_suffix: str,
        audio_chunks: list[torch.Tensor],
        full_attention_mask: torch.Tensor | None,
    ) -> tuple[dict[str, Any], torch.Tensor]:
        batch = self.collator._call_processor(rendered_texts=[rendered_suffix], flat_audio_chunks=audio_chunks)
        batch = _pop_training_only_processor_keys(batch)
        input_ids = batch.get("input_ids")
        if not isinstance(input_ids, torch.Tensor):
            raise ValueError("Processor output does not contain tensor input_ids for prefill-cache suffix")
        if int(input_ids.shape[0]) != 1:
            raise ValueError("Prefill-cache suffix processor only supports batch size 1")
        if full_attention_mask is not None:
            batch["attention_mask"] = full_attention_mask
        return batch, input_ids.detach().cpu()

    def _suffix_batch_for_cache_state(
        self,
        *,
        full_batch: dict[str, Any],
        full_input_ids: torch.Tensor,
        full_rendered: str,
        full_audio_slots: int,
        all_audio_chunks: list[torch.Tensor],
        cache_state: PromptPrefillCacheState | None,
    ) -> tuple[dict[str, Any], torch.Tensor, int]:
        if cache_state is None:
            input_ids = full_batch.get("input_ids")
            if not isinstance(input_ids, torch.Tensor):
                raise ValueError("Processor output does not contain tensor input_ids")
            return full_batch, input_ids.detach().cpu(), 0

        prefix_length = self._validate_cached_prefix(
            full_input_ids=full_input_ids,
            cache_state=cache_state,
        )
        if full_audio_slots < cache_state.audio_slots:
            raise ValueError(
                f"Cached audio slots exceed current prompt audio slots: "
                f"cached={cache_state.audio_slots}, current={full_audio_slots}"
            )
        if not full_rendered.startswith(cache_state.rendered_text):
            raise ValueError("Cached rendered prompt is not a string prefix of the current rendered prompt")
        rendered_suffix = full_rendered[len(cache_state.rendered_text):]
        suffix_audio_chunks = all_audio_chunks[cache_state.audio_slots:full_audio_slots]
        full_attention_mask = full_batch.get("attention_mask")
        full_attention_mask = full_attention_mask if isinstance(full_attention_mask, torch.Tensor) else None
        suffix_batch, suffix_input_ids = self._processor_batch_for_rendered_suffix(
            rendered_suffix=rendered_suffix,
            audio_chunks=suffix_audio_chunks,
            full_attention_mask=full_attention_mask,
        )
        reconstructed = torch.cat([cache_state.input_ids.detach().cpu(), suffix_input_ids], dim=1)
        if not torch.equal(reconstructed, full_input_ids.detach().cpu()):
            raise ValueError(
                "Rendered suffix tokenization does not reconstruct the full prompt token ids; "
                "cannot safely reuse multimodal prefill cache"
            )
        return suffix_batch, suffix_input_ids, prefix_length

    @staticmethod
    def _validate_cached_prefix(
        *,
        full_input_ids: torch.Tensor,
        cache_state: PromptPrefillCacheState,
    ) -> int:
        cached_prompt_ids = cache_state.input_ids.detach().cpu()
        full_input_ids = full_input_ids.detach().cpu()
        if int(cached_prompt_ids.shape[0]) != 1 or int(full_input_ids.shape[0]) != 1:
            raise ValueError("Prefill-cache prefix validation expects batch size 1")
        prefix_length = int(cached_prompt_ids.shape[1])
        full_length = int(full_input_ids.shape[1])
        if prefix_length > full_length:
            raise ValueError(
                f"Cached prompt is longer than full prompt: cached={prefix_length}, full={full_length}"
            )
        if prefix_length and not torch.equal(cached_prompt_ids[:, :prefix_length], full_input_ids[:, :prefix_length]):
            raise ValueError(
                "Cached prompt tokens are not an exact prefix of the freshly rendered prompt; "
                "cannot safely reuse prefill cache"
            )
        return prefix_length

    @staticmethod
    def _slice_batch_for_cached_suffix(
        *,
        full_batch: dict[str, Any],
        full_sequence_length: int,
        prefix_length: int,
    ) -> dict[str, Any]:
        suffix_batch: dict[str, Any] = {}
        for key, value in full_batch.items():
            if not isinstance(value, torch.Tensor):
                suffix_batch[key] = value
                continue
            if value.ndim >= 2 and int(value.shape[0]) == 1 and int(value.shape[1]) == full_sequence_length:
                if key == "attention_mask":
                    suffix_batch[key] = value
                else:
                    suffix_batch[key] = value[:, prefix_length:]
            else:
                suffix_batch[key] = value
        return suffix_batch

    @staticmethod
    def _extract_generated_suffix_output_ids(
        *,
        sequences: torch.Tensor,
        full_input_ids: torch.Tensor,
        suffix_input_ids: torch.Tensor,
    ) -> torch.Tensor:
        suffix_length = int(suffix_input_ids.shape[1])
        full_length = int(full_input_ids.shape[1])
        if int(sequences.shape[1]) >= suffix_length and torch.equal(sequences[:, :suffix_length], suffix_input_ids):
            return sequences[:, suffix_length:]
        if int(sequences.shape[1]) >= full_length and torch.equal(sequences[:, :full_length], full_input_ids):
            return sequences[:, full_length:]
        raise ValueError("Generated sequence does not preserve expected prompt/suffix prefix")

    def evaluate(
        self,
        *,
        model: Any,
        step: int,
        metrics: dict[str, Any],
    ) -> dict[str, Any]:
        records = self.generate_records_with_prefill_cache(model=model, step=step, metrics=metrics)
        summary_metrics = summarize_test_records(records)
        return {
            "step": step,
            "metrics": metrics,
            "test_use_prefill_cache": True,
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