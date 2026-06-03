"""User-facing runner APIs and runner-adjacent utilities."""

from .utils import (
    cache_output_path,
    load_metadata_by_part,
    load_metadata_map,
    load_pipeline_records_by_part,
    load_pipeline_records_by_part_latest,
    load_transcriptions_by_part,
    reconstruction_output_path,
    stage_output_path_from_input_cache,
    shard_part_suffix_from_transcription_path,
    TqdmBar,
    visualization_omni_translation_only,
    visualization_pure_text_segmentation,
    visualization_target_centric_mapping,
    visualization_time_pressure_segmentation,
    visualization_translation_only,
    visualization_translation_reconstruction,
    visualized_path,
    safe_shard_label,
)


def __getattr__(name: str):
    if name == "TranscriptionRunner":
        from .transcription import TranscriptionRunner

        return TranscriptionRunner
    if name == "ForcedAlignmentRunner":
        from .forced_alignment import ForcedAlignmentRunner

        return ForcedAlignmentRunner
    if name == "TimePressureSegmentationRunner":
        from .time_pressure_segmentation import TimePressureSegmentationRunner

        return TimePressureSegmentationRunner
    if name == "PureTextSegmentationRunner":
        from .pure_text_segmentation import PureTextSegmentationRunner

        return PureTextSegmentationRunner
    if name == "TargetCentricMappingRunner":
        from .target_centric_mapping import TargetCentricMappingRunner

        return TargetCentricMappingRunner
    if name == "TranslationReconstructionRunner":
        from .translation_reconstruction import TranslationReconstructionRunner

        return TranslationReconstructionRunner
    if name == "TranslationOnlyRunner":
        from .translation_only import TranslationOnlyRunner

        return TranslationOnlyRunner
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "TranscriptionRunner",
    "ForcedAlignmentRunner",
    "TimePressureSegmentationRunner",
    "PureTextSegmentationRunner",
    "TargetCentricMappingRunner",
    "TranslationReconstructionRunner",
    "TranslationOnlyRunner",
    "cache_output_path",
    "load_metadata_by_part",
    "load_metadata_map",
    "load_pipeline_records_by_part",
    "load_pipeline_records_by_part_latest",
    "load_transcriptions_by_part",
    "reconstruction_output_path",
    "stage_output_path_from_input_cache",
    "shard_part_suffix_from_transcription_path",
    "TqdmBar",
    "visualization_omni_translation_only",
    "visualization_pure_text_segmentation",
    "visualization_target_centric_mapping",
    "visualization_time_pressure_segmentation",
    "visualization_translation_only",
    "visualization_translation_reconstruction",
    "visualized_path",
    "safe_shard_label",
]