"""Shared audio loading/chunking helpers for LoRA training and strict testing.

This module intentionally contains only low-level audio/window mechanics.  It is
not a Trainer collator and it does not build labels or training batches.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import torch


def load_audio_waveform(audio_path: str | Path, *, target_sampling_rate: int) -> torch.Tensor:
    """Load mono audio and resample it to the processor sampling rate."""

    import torchaudio

    waveform, sample_rate = torchaudio.load(str(audio_path))
    if waveform.ndim != 2:
        raise ValueError(f"Expected waveform shape [channels, samples], got {tuple(waveform.shape)}")
    waveform = waveform.mean(dim=0)
    if int(sample_rate) != int(target_sampling_rate):
        waveform = torchaudio.functional.resample(waveform, int(sample_rate), int(target_sampling_rate))
    return waveform.to(dtype=torch.float32)


def split_audio_into_chunks(
    waveform: torch.Tensor,
    *,
    sampling_rate: int,
    chunk_seconds: float,
    expected_chunk_count: int | None = None,
) -> list[torch.Tensor]:
    """Split audio into fixed-size causal chunks and zero-pad the final chunk.

    When ``expected_chunk_count`` is provided, it is the authoritative
    metadata-derived window count. This keeps training/test audio turns aligned
    with final-dataset ASR/translation output windows even if the physical audio
    file contains a tiny encoder/container tail beyond ``metadata.duration``.
    """

    if waveform.ndim != 1:
        raise ValueError(f"Expected mono waveform shape [samples], got {tuple(waveform.shape)}")
    chunk_size = int(round(float(sampling_rate) * chunk_seconds))
    if chunk_size <= 0:
        raise ValueError(f"Invalid audio chunk size from sampling_rate={sampling_rate}, chunk_seconds={chunk_seconds}")
    if expected_chunk_count is None:
        chunk_count = max(1, math.ceil(int(waveform.numel()) / chunk_size))
    else:
        chunk_count = int(expected_chunk_count)
        if chunk_count <= 0:
            raise ValueError(f"expected_chunk_count must be positive: {expected_chunk_count}")
    chunks: list[torch.Tensor] = []
    for index in range(chunk_count):
        start = index * chunk_size
        end = min(start + chunk_size, int(waveform.numel()))
        chunk = waveform[start:end]
        if int(chunk.numel()) < chunk_size:
            chunk = torch.nn.functional.pad(chunk, (0, chunk_size - int(chunk.numel())))
        chunks.append(chunk)
    return chunks


def validate_example_chunk_counts(example: Any, audio_chunks: list[torch.Tensor]) -> None:
    """Validate that final-dataset text windows and audio chunks stay aligned."""

    if example.task == "asr":
        if len(audio_chunks) != len(example.src_outputs):
            raise ValueError(
                f"ASR example {example.uid} chunk/output mismatch: "
                f"audio_chunks={len(audio_chunks)}, src_outputs={len(example.src_outputs)}"
            )
        return
    if example.task == "translation":
        if example.tgt_outputs is None:
            raise ValueError(f"Translation example {example.uid} has no target outputs")
        if len(audio_chunks) != len(example.src_outputs) or len(audio_chunks) != len(example.tgt_outputs):
            raise ValueError(
                f"Translation example {example.uid} chunk/output mismatch: "
                f"audio_chunks={len(audio_chunks)}, src_outputs={len(example.src_outputs)}, "
                f"tgt_outputs={len(example.tgt_outputs)}"
            )
        return
    raise ValueError(f"Unsupported training task: {example.task}")


def audio_chunks_for_example(
    example: Any,
    *,
    audio_sampling_rate: int,
    audio_chunk_seconds: float,
) -> list[torch.Tensor]:
    """Build metadata/final-dataset-window-authoritative audio chunks."""

    waveform = load_audio_waveform(example.audio_path, target_sampling_rate=audio_sampling_rate)
    audio_chunks = split_audio_into_chunks(
        waveform,
        sampling_rate=audio_sampling_rate,
        chunk_seconds=audio_chunk_seconds,
        expected_chunk_count=len(example.src_outputs),
    )
    validate_example_chunk_counts(example, audio_chunks)
    return audio_chunks