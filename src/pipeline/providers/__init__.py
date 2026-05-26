"""
Upstream provider package.

Providers produce the initial ingredients for the pipeline:
- ASRProvider: raw source transcription
- OmniTranslationProvider: raw source transcription + raw multilingual translations
- RawTranslationProvider: raw multilingual translations from source text only
"""

from pipeline.providers.base import BaseProvider
from pipeline.providers.qwen3_forced_alignment_provider import Qwen3ForcedAlignment
from pipeline.providers.target_centric_mapping_provider import TargetCentricMappingProvider
from pipeline.providers.whisperx_forced_alignment_provider import WhisperXForcedAlignment

__all__ = [
    "BaseProvider",
    "Qwen3ForcedAlignment",
    "TargetCentricMappingProvider",
    "WhisperXForcedAlignment",
]