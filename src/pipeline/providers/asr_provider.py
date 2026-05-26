"""
ASRProvider: produces raw source transcription from an ASR model.
"""

import asyncio
from pathlib import Path
from typing import Optional

from configs.config import Config
from core.utils import normalize_generated_text
from pipeline.schema import (
    PipelineRecord,
    StatusEnum,
    TranscriptArtifact,
)
from pipeline.providers.base import BaseProvider


class ASRProvider(BaseProvider):
    """
    Upstream provider that runs an ASR model to produce source transcription.

    This provider populates record.source.artifacts.transcript.
    It does NOT perform forced alignment or segmentation.
    """

    def __init__(
        self,
        asr_model,
        name: str = "ASRProvider",
        max_retries: int = 6,
    ):
        super().__init__(name=name, max_retries=max_retries)
        self.asr_model = asr_model

    async def provide(
        self,
        record: PipelineRecord,
        audio: Optional[str | Path | bytes] = None,
        language_code: Optional[str] = None,
        language_name: Optional[str] = None,
        **kwargs,
    ) -> PipelineRecord:
        """
        Run ASR on the provided audio and populate the transcript artifact.
        """
        record.source.status.asr.status = StatusEnum.RUNNING
        record.source.status.asr.errors.clear()

        if audio is None:
            record.source.status.asr.status = StatusEnum.FAILED
            record.source.status.asr.errors.append("No audio input provided")
            return record

        exceptions = []
        for n_retry in range(self.max_retries + 1):
            try:
                lang = language_name or language_code or ""
                try:
                    result = self.asr_model.transcribe(audio, language=lang, return_text=False)[0]
                except TypeError:
                    result = self.asr_model.transcribe(audio, language=lang)[0]

                text = result.text if hasattr(result, "text") else str(result)
                text = normalize_generated_text(text.lstrip(" "), language_code or record.metadata.language or "")
                author = self.asr_model.model_name

                resolved_language_code = language_code or record.metadata.language or ""
                resolved_language_name = language_name or Config.lang_code2name.get(
                    resolved_language_code, ""
                )

                record.source.artifacts.transcript = TranscriptArtifact(
                    language_code=resolved_language_code,
                    language_name=resolved_language_name,
                    text=text,
                    author=author,
                )

                record.source.status.asr.status = StatusEnum.FINISHED
                return record

            except Exception as e:
                exceptions.append(str(e))
                if n_retry == self.max_retries:
                    record.source.status.asr.status = StatusEnum.FAILED
                    record.source.status.asr.errors.append(
                        f"- Retries: {self.max_retries}\n- Errors: {exceptions}"
                    )
                    return record
                await asyncio.sleep(0.5 * (n_retry + 1))

        return record