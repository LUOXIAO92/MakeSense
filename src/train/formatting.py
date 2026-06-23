"""Format final dataset training examples as chat conversations."""

from __future__ import annotations

from typing import Any

from data_loader.dataset import TrainingExample


ChatMessage = dict[str, Any]

# Optional ablation variant to test whether explicitly encouraging
# transcription-guided translation helps the model learn the
# audio+transcription->translation strategy faster:
# TRANSLATION_PROMPT_WITH_TRANSCRIPTION = (
#     "You are a professional simultaneous interpreter. "
#     "Refer to the transcription, then translate to {target_language}."
# )


def system_prompt_for_example(example: TrainingExample) -> str:
    """Return the system prompt for one training example."""

    if example.task == "asr":
        return "You are a professional transcriptionist. Transcribe what you hear."
    if example.task != "translation":
        raise ValueError(f"Unsupported training task: {example.task}")
    if example.target_language is None:
        raise ValueError(f"Translation example {example.uid} has no target language")

    if example.translation_mode == "natural":
        return (
            "You are a professional simultaneous interpreter. "
            f"Translate to {example.target_language}."
        )
    if example.translation_mode == "fixed_window":
        return (
            "You are a professional simultaneous interpreter. "
            f"Translate to {example.target_language}. "
            f"Tolerance window size is {example.tolerance_window}."
        )
    if example.translation_mode == "conservative":
        if example.min_wait_window is None:
            raise ValueError(f"Conservative translation example {example.uid} has no min_wait_window")
        return (
            "You are a professional simultaneous interpreter. "
            f"Translate to {example.target_language}. "
            f"Keep at least {example.min_wait_window} wait windows before each target release."
        )
    raise ValueError(
        f"Unsupported translation mode for example {example.uid}: {example.translation_mode}"
    )


def example_to_messages(example: TrainingExample) -> list[ChatMessage]:
    """Convert one training example into multi-turn chat messages."""

    src_outputs = example.src_outputs
    if example.task == "translation":
        if example.tgt_outputs is None:
            raise ValueError(f"Translation example {example.uid} has no target outputs")
        if len(src_outputs) != len(example.tgt_outputs):
            raise ValueError(
                f"Translation example {example.uid} has mismatched source/target outputs: "
                f"src={len(src_outputs)}, tgt={len(example.tgt_outputs)}"
            )
        assistant_outputs = [
            f"{src_output}{tgt_output}"
            for src_output, tgt_output in zip(src_outputs, example.tgt_outputs)
        ]
    elif example.task == "asr":
        assistant_outputs = list(src_outputs)
    else:
        raise ValueError(f"Unsupported training task: {example.task}")

    messages: list[ChatMessage] = [
        {
            "role": "system",
            "content": system_prompt_for_example(example),
        }
    ]
    for assistant_output in assistant_outputs:
        messages.append(
            {
                "role": "user",
                "content": [{"type": "audio"}],
            }
        )
        messages.append(
            {
                "role": "assistant",
                "content": str(assistant_output),
            }
        )
    return messages


def _is_qwen2_5_omni_processor(processor: object) -> bool:
    return processor.__class__.__name__ == "Qwen2_5OmniProcessor"


def render_chat_template(
    processor: object,
    messages: list[ChatMessage],
    *,
    add_generation_prompt: bool,
    enable_thinking: bool,
) -> str:
    kwargs: dict[str, Any] = {
        "tokenize": False,
        "add_generation_prompt": add_generation_prompt,
    }
    if not _is_qwen2_5_omni_processor(processor):
        kwargs["enable_thinking"] = enable_thinking
    rendered = processor.apply_chat_template(messages, **kwargs)
    return str(rendered)


def messages_to_chat_text(processor: object, messages: list[ChatMessage]) -> str:
    """Render chat messages as model-specific training text.

    Multimodal processors own chat-template rendering and audio/image packing.
    """

    try:
        return render_chat_template(
            processor,
            messages,
            add_generation_prompt=False,
            enable_thinking=False,
        )
    except AttributeError as exc:
        raise ValueError("Real-audio training requires processor.apply_chat_template")
    except TypeError:
        raise
