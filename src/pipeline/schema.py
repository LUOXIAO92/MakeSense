"""
Shared processing-state / cache schema.

This module defines the unified cache schema used by both the staged
ASR pipeline and the optional omni-translation pipeline.

Important:
    This schema is for cache / processing-state use only.
    It is NOT the final dataset schema.
    Final dataset structures should remain in src/data_process/schema.py.
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

from core.schema import Mapping, MetaData, SenseUnits, Word


class StatusEnum(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    FINISHED = "finished"
    FAILED = "failed"


class TaskStatus(BaseModel):
    status: StatusEnum = StatusEnum.PENDING
    errors: list[str] = Field(default_factory=list)


class TranscriptArtifact(BaseModel):
    """Source transcription artifact."""

    language_code: str = ""
    language_name: str = ""
    text: str = ""
    author: str = ""


class AlignmentArtifact(BaseModel):
    """Source alignment artifact."""

    tokens: list[Word] = Field(default_factory=list)
    words: list[list[int]] = Field(default_factory=list)
    author: str = ""


class TimePressureSegmentationArtifact(BaseModel):
    """Time-pressure sense-unit segmentation artifact."""

    sense_units: SenseUnits = Field(default_factory=lambda: SenseUnits(level="minimal"))
    author: str = ""


class RawTranslationArtifact(BaseModel):
    """Raw translation artifact before reconstruction."""

    text: str = ""
    author: str = ""


class ReconstructedTranslationArtifact(BaseModel):
    """Reconstructed translation artifact for simultaneous-translation-friendly output."""

    text: str = ""
    author: str = ""


class PureTextSegmentationArtifact(BaseModel):
    """Pure-text sense-unit segmentation artifact."""

    tokens: list[str] = Field(default_factory=list)
    sense_units: SenseUnits = Field(default_factory=lambda: SenseUnits(level="clause", groups=[]))
    author: str = ""


class SenseUnitMappingArtifact(BaseModel):
    """Source-to-target sense-unit mapping artifact."""

    mappings: list[Mapping] = Field(default_factory=list)
    author: str = ""


class SourceArtifacts(BaseModel):
    transcript: TranscriptArtifact | None = None
    alignment: AlignmentArtifact | None = None
    time_pressure_segmentation: TimePressureSegmentationArtifact | None = None


class SourceStatus(BaseModel):
    asr: TaskStatus = Field(default_factory=TaskStatus)
    forced_alignment: TaskStatus = Field(default_factory=TaskStatus)
    time_pressure_segmentation: TaskStatus = Field(default_factory=TaskStatus)


class SourceScope(BaseModel):
    artifacts: SourceArtifacts = Field(default_factory=SourceArtifacts)
    status: SourceStatus = Field(default_factory=SourceStatus)


class TargetLanguageArtifacts(BaseModel):
    raw_translation: RawTranslationArtifact = Field(default_factory=RawTranslationArtifact)
    reconstruction: ReconstructedTranslationArtifact = Field(default_factory=ReconstructedTranslationArtifact)
    pure_text_segmentation: PureTextSegmentationArtifact = Field(default_factory=PureTextSegmentationArtifact)
    tgt_src_mapping: SenseUnitMappingArtifact = Field(default_factory=SenseUnitMappingArtifact)


class TargetLanguageStatus(BaseModel):
    raw_translation: TaskStatus = Field(default_factory=TaskStatus)
    reconstruction: TaskStatus = Field(default_factory=TaskStatus)
    pure_text_segmentation: TaskStatus = Field(default_factory=TaskStatus)
    tgt_src_mapping: TaskStatus = Field(default_factory=TaskStatus)


class TargetLanguageEntry(BaseModel):
    language_code: str = ""
    artifacts: TargetLanguageArtifacts = Field(default_factory=TargetLanguageArtifacts)
    status: TargetLanguageStatus = Field(default_factory=TargetLanguageStatus)


class TargetShared(BaseModel):
    translation_analysis: str = ""


class TargetScope(BaseModel):
    shared: TargetShared = Field(default_factory=TargetShared)
    languages: dict[str, TargetLanguageEntry] = Field(default_factory=dict)


class PipelineRecord(BaseModel):
    """Unified cache / processing-state record for one sample."""

    model_config = ConfigDict(populate_by_name=True)

    uid: str
    metadata: MetaData
    source: SourceScope = Field(default_factory=SourceScope)
    target: TargetScope = Field(default_factory=TargetScope)
    cache_version: str = "v4"
    _debug_time_pressure_segmentation: dict[str, Any] = PrivateAttr(default_factory=dict)
    _debug_pure_text_segmentation: dict[str, dict[str, Any]] = PrivateAttr(default_factory=dict)
    _debug_translation_reconstruction: dict[str, dict[str, Any]] = PrivateAttr(default_factory=dict)
    _debug_target_centric_mapping: dict[str, dict[str, Any]] = PrivateAttr(default_factory=dict)

    def model_post_init(self, __context) -> None:
        from configs.config import Config

        if not self.target.languages:
            self.target.languages = {
                code: TargetLanguageEntry(language_code=code)
                for code in Config.language_codes
                if code != self.metadata.language
            }

    def set_debug_pure_text_segmentation(
        self,
        language_code: str,
        *,
        scratchpad: str = "",
        result: str = "",
        attempts: list[dict[str, Any]] | None = None,
    ) -> None:
        self._debug_pure_text_segmentation[language_code] = {
            "scratchpad": scratchpad or "",
            "result": result or "",
            "attempts": [dict(attempt) for attempt in (attempts or [])],
        }

    def get_debug_pure_text_segmentation(self, language_code: str) -> dict[str, Any]:
        return dict(self._debug_pure_text_segmentation.get(language_code, {}))

    def set_debug_time_pressure_segmentation(
        self,
        *,
        scratchpad: str = "",
        result: str = "",
        attempts: list[dict[str, Any]] | None = None,
    ) -> None:
        self._debug_time_pressure_segmentation = {
            "scratchpad": scratchpad or "",
            "result": result or "",
            "attempts": [dict(attempt) for attempt in (attempts or [])],
        }

    def get_debug_time_pressure_segmentation(self) -> dict[str, Any]:
        return dict(self._debug_time_pressure_segmentation)

    def set_debug_translation_reconstruction(
        self,
        language_code: str,
        *,
        scratchpad: str = "",
        result: str = "",
        validator_scratchpad: str = "",
        validator_result: str = "",
        validator_order_risk: str = "",
        validator_source_tokens: str = "",
        validator_source_windows: str = "",
        validator_feedback: str = "",
        attempts: list[dict[str, Any]] | None = None,
    ) -> None:
        self._debug_translation_reconstruction[language_code] = {
            "scratchpad": scratchpad or "",
            "result": result or "",
            "validator_scratchpad": validator_scratchpad or "",
            "validator_result": validator_result or "",
            "validator_order_risk": validator_order_risk or "",
            "validator_source_tokens": validator_source_tokens or "",
            "validator_source_windows": validator_source_windows or "",
            "validator_feedback": validator_feedback or "",
            "attempts": [dict(attempt) for attempt in (attempts or [])],
        }

    def get_debug_translation_reconstruction(self, language_code: str) -> dict[str, Any]:
        return dict(self._debug_translation_reconstruction.get(language_code, {}))

    def set_debug_target_centric_mapping(
        self,
        language_code: str,
        *,
        scratchpad: str = "",
        result: str = "",
        error: str = "",
        attempts: list[dict[str, Any]] | None = None,
    ) -> None:
        self._debug_target_centric_mapping[language_code] = {
            "scratchpad": scratchpad or "",
            "result": result or "",
            "error": error or "",
            "attempts": [dict(attempt) for attempt in (attempts or [])],
        }

    def get_debug_target_centric_mapping(self, language_code: str) -> dict[str, Any]:
        return dict(self._debug_target_centric_mapping.get(language_code, {}))


class OmniTranslationResult(BaseModel):
    """Intermediate schema for omni-translation LLM output validation."""

    asr: dict[str, str] = Field(default_factory=dict)
    translation: dict[str, str] = Field(default_factory=dict)


__all__ = [
    "StatusEnum",
    "TaskStatus",
    "TranscriptArtifact",
    "AlignmentArtifact",
    "TimePressureSegmentationArtifact",
    "RawTranslationArtifact",
    "ReconstructedTranslationArtifact",
    "PureTextSegmentationArtifact",
    "SenseUnitMappingArtifact",
    "SourceArtifacts",
    "SourceStatus",
    "SourceScope",
    "TargetLanguageArtifacts",
    "TargetLanguageStatus",
    "TargetLanguageEntry",
    "TargetShared",
    "TargetScope",
    "PipelineRecord",
    "OmniTranslationResult",
]
