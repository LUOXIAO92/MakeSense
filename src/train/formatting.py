"""Format final dataset training examples as chat conversations."""

from __future__ import annotations

from data_loader.dataset import TrainingExample


ChatMessage = dict[str, str]


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

    messages: list[ChatMessage] = [
        {
            "role": "system",
            "content": system_prompt_for_example(
                example,
                requested_tolerance_window=requested_tolerance_window,
            ),
        }
    ]
    for block in example.blocks:
        messages.append({"role": "user", "content": "<|audio|>"})
        messages.append({"role": "assistant", "content": str(block)})
    return messages


def messages_to_chat_text(tokenizer: object, messages: list[ChatMessage]) -> str:
    """Render chat messages as model-specific training text.

    Prefer the tokenizer chat template.  A small plain-text fallback is retained
    so formatting tests and dry runs can use minimal tokenizer stubs.
    """

    apply_chat_template = getattr(tokenizer, "apply_chat_template", None)
    if callable(apply_chat_template):
        return str(
            apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False,
            )
        )
    return "\n".join(f"{message['role']}\n{message['content']}" for message in messages)
