"""Reusable training utility helpers."""

from __future__ import annotations

import torch


def prepare_multimodal_model_for_kbit_lora_training(
    model,
    *,
    fp32_cast_blacklist: tuple[str, ...] = (
        "embed",
        "lm_head",
        "embed_tokens_per_layer",
        "audio",
        "vision",
    ),
):
    """Prepare a k-bit multimodal model for LoRA training.

    This project-owned variant keeps the useful parts of PEFT's generic
    k-bit preparation while avoiding a blind fp32 cast of high-memory
    multimodal / embedding components.

    The visible ``fp32_cast_blacklist`` default intentionally protects large
    lookup tables, output heads, and multimodal encoder blocks. Callers may
    pass additional name fragments when a model has other components that
    should stay in their loaded dtype.
    """

    normalized_blacklist = tuple(item.lower() for item in fp32_cast_blacklist)

    for parameter in model.parameters():
        parameter.requires_grad_(False)

    config = getattr(model, "config", None)
    if config is not None and hasattr(config, "use_cache"):
        config.use_cache = False

    for name, parameter in model.named_parameters():
        lowered_name = name.lower()
        if any(fragment in lowered_name for fragment in normalized_blacklist):
            continue
        if not parameter.is_floating_point():
            continue
        if getattr(parameter, "quant_state", None) is not None:
            continue
        if parameter.dtype != torch.float32:
            parameter.data = parameter.data.to(torch.float32)

    if hasattr(model, "enable_input_require_grads"):
        model.enable_input_require_grads()
    else:
        input_embeddings = model.get_input_embeddings() if hasattr(model, "get_input_embeddings") else None
        if input_embeddings is not None:

            def make_inputs_require_grad(_module, _inputs, output):
                if isinstance(output, torch.Tensor):
                    output.requires_grad_(True)

            input_embeddings.register_forward_hook(make_inputs_require_grad)

    if hasattr(model, "gradient_checkpointing_enable"):
        try:
            model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
        except TypeError:
            model.gradient_checkpointing_enable()

    return model