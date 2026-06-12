"""Shared CUDA VRAM telemetry helpers for training and strict-test progress."""

from __future__ import annotations

import torch


def cuda_vram_usage_gib(*, reset_peak: bool = False) -> tuple[float, float, float, float] | None:
    """Return PyTorch CUDA allocator current/peak memory in GiB."""

    if not torch.cuda.is_available():
        return None
    try:
        allocated_bytes = int(torch.cuda.memory_allocated())
        reserved_bytes = int(torch.cuda.memory_reserved())
        max_allocated_bytes = max(int(torch.cuda.max_memory_allocated()), allocated_bytes)
        max_reserved_bytes = max(int(torch.cuda.max_memory_reserved()), reserved_bytes)
    except Exception:
        return None
    allocated_gib = allocated_bytes / 1024**3
    reserved_gib = reserved_bytes / 1024**3
    max_allocated_gib = max_allocated_bytes / 1024**3
    max_reserved_gib = max_reserved_bytes / 1024**3
    if reset_peak:
        try:
            torch.cuda.reset_peak_memory_stats()
        except Exception:
            pass
    return allocated_gib, reserved_gib, max_allocated_gib, max_reserved_gib


def format_vram_usage(vram_usage: tuple[float, float, float, float] | None = None) -> str:
    """Format allocator VRAM telemetry for progress displays."""

    if vram_usage is None:
        return "vram: alloc/reserved=n/a/n/a (max n/a/n/a) GiB"
    allocated_gib, reserved_gib, max_allocated_gib, max_reserved_gib = vram_usage
    return (
        f"vram: alloc/reserved={allocated_gib:.1f}/{reserved_gib:.1f} "
        f"(max {max_allocated_gib:.1f}/{max_reserved_gib:.1f}) GiB"
    )