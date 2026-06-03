"""
Upstream provider package.

Providers produce the initial ingredients for the pipeline:
- ASRProvider: raw source transcription
- OmniTranslationProvider: raw source transcription + raw multilingual translations
- RawTranslationProvider: raw multilingual translations from source text only
"""

from pipeline.providers.base import BaseProvider

_LAZY_EXPORTS = {
    "Qwen3ForcedAlignment": (
        "pipeline.providers.qwen3_forced_alignment_provider",
        "Qwen3ForcedAlignment",
    ),
    "TargetCentricMappingProvider": (
        "pipeline.providers.target_centric_mapping_provider",
        "TargetCentricMappingProvider",
    ),
    "WhisperXForcedAlignment": (
        "pipeline.providers.whisperx_forced_alignment_provider",
        "WhisperXForcedAlignment",
    ),
}

__all__ = [
    "BaseProvider",
    "Qwen3ForcedAlignment",
    "TargetCentricMappingProvider",
    "WhisperXForcedAlignment",
]


def __getattr__(name: str):
    if name not in _LAZY_EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attr_name = _LAZY_EXPORTS[name]
    from importlib import import_module

    value = getattr(import_module(module_name), attr_name)
    globals()[name] = value
    return value