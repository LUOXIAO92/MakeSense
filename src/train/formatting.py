"""Format final dataset training examples as chat conversations."""

from __future__ import annotations

from typing import Any

from data_loader.dataset import TrainingExample


ChatMessage = dict[str, Any]


def system_prompt_for_example(
    example: TrainingExample,
    *,
    requested_tolerance_window: int | None,
) -> str:
    """Return the system prompt for one training example.

    ``requested_tolerance_window`` mirrors the value passed to
    ``build_training_dataset(...)``.  When it is ``None``, examples may have a
    sampled/effective real wait budget and the prompt should expose the concrete
    ``TrainingExample.tolerance_window``.  When it is fixed at ``0``, translation
    examples use the concise no-latency instruction tested by the user.
    """

    if example.task == "asr":
        return "Transcribe"
    if example.task != "translation":
        raise ValueError(f"Unsupported training task: {example.task}")
    if example.target_language is None:
        raise ValueError(f"Translation example {example.uid} has no target language")

    if requested_tolerance_window is not None and requested_tolerance_window == 0:
        return f"Translate to {example.target_language}."
    return f"Translate to {example.target_language}, tolerance window size is {example.tolerance_window}"


def example_to_messages(
    example: TrainingExample,
    *,
    requested_tolerance_window: int | None,
) -> list[ChatMessage]:
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
            "content": system_prompt_for_example(
                example,
                requested_tolerance_window=requested_tolerance_window,
            ),
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


def messages_to_chat_text(tokenizer: object, messages: list[ChatMessage]) -> str:
    """Render chat messages as model-specific training text.

    Multimodal processors own audio/image packing, but chat templates live on
    the tokenizer boundary for the target model family.  The caller must pass
    the explicit tokenizer object, not the processor wrapper.
    """

    try:
        rendered = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False,
        )
    except AttributeError as exc:
        raise ValueError("Real-audio training requires tokenizer.apply_chat_template")
    except TypeError:
        raise
    return str(rendered)
