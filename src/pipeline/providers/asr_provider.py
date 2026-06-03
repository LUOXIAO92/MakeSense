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
from pipeline.providers.retry_error_rendering import raise_unless_contract_or_validation_error


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

    def _normalize_language(self, language_code: Optional[str], language_name: Optional[str], record: PipelineRecord) -> tuple[str, str, str]:
        lang = language_name or language_code or ""
        resolved_language_code = language_code or record.metadata.language or ""
        resolved_language_name = language_name or Config.lang_code2name.get(
            resolved_language_code, ""
        )
        return lang, resolved_language_code, resolved_language_name

    def _transcribe_raw(self, audio, lang: str):
        try:
            return self.asr_model.transcribe(audio, language=lang, return_text=False)
        except TypeError:
            return self.asr_model.transcribe(audio, language=lang)

    def _result_text(self, result, language_code: str) -> str:
        text = result.text if hasattr(result, "text") else str(result)
        return normalize_generated_text(text.lstrip(" "), language_code)

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
                lang, resolved_language_code, resolved_language_name = self._normalize_language(
                    language_code,
                    language_name,
                    record,
                )
                result = self._transcribe_raw(audio, lang)[0]

                text = self._result_text(result, resolved_language_code)
                author = self.asr_model.model_name

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
                    raise_unless_contract_or_validation_error(e)
                    record.source.status.asr.status = StatusEnum.FAILED
                    record.source.status.asr.errors.append(
                        f"- Retries: {self.max_retries}\n- Errors: {exceptions}"
                    )
                    return record
                await asyncio.sleep(0.5 * (n_retry + 1))

        return record

    async def provide_batch(
        self,
        records: list[PipelineRecord],
        audio_list: list[str | Path | bytes],
        *,
        language_codes: Optional[list[str]] = None,
        language_names: Optional[list[str]] = None,
    ) -> list[PipelineRecord]:
        if len(records) != len(audio_list):
            raise ValueError("records and audio_list must have the same length")

        language_codes = language_codes or [record.metadata.language for record in records]
        language_names = language_names or [None] * len(records)

        if len(language_codes) != len(records) or len(language_names) != len(records):
            raise ValueError("language metadata must match records length")

        for record in records:
            record.source.status.asr.status = StatusEnum.RUNNING
            record.source.status.asr.errors.clear()

        batched_records = [
            (record, audio, language_code, language_name)
            for record, audio, language_code, language_name in zip(records, audio_list, language_codes, language_names)
            if audio is not None
        ]

        for record, audio, _language_code, _language_name in zip(records, audio_list, language_codes, language_names):
            if audio is None:
                record.source.status.asr.status = StatusEnum.FAILED
                record.source.status.asr.errors.append("No audio input provided")

        if not batched_records:
            return records

        payload = [
            (
                audio,
                *self._normalize_language(language_code, language_name, record),
                record,
            )
            for record, audio, language_code, language_name in batched_records
        ]
        batch_languages = [lang for _audio, lang, _code, _name, _record in payload]
        unique_batch_languages = set(batch_languages)
        if len(unique_batch_languages) != 1:
            raise ValueError(
                "ASRProvider batch received multiple languages for one ASR model: "
                f"{sorted(unique_batch_languages)}"
            )
        batch_language = batch_languages[0]

        exceptions = []
        for n_retry in range(self.max_retries + 1):
            try:
                raw_results = self._transcribe_raw(
                    [audio for audio, *_rest in payload],
                    batch_language,
                )
                author = self.asr_model.model_name

                for raw_result, (_audio, _lang, resolved_language_code, resolved_language_name, record) in zip(raw_results, payload):
                    record.source.artifacts.transcript = TranscriptArtifact(
                        language_code=resolved_language_code,
                        language_name=resolved_language_name,
                        text=self._result_text(raw_result, resolved_language_code),
                        author=author,
                    )
                    record.source.status.asr.status = StatusEnum.FINISHED
                return records
            except Exception as e:
                exceptions.append(str(e))
                if n_retry == self.max_retries:
                    raise_unless_contract_or_validation_error(e)
                    for record, _audio, _language_code, _language_name in batched_records:
                        record.source.status.asr.status = StatusEnum.FAILED
                        record.source.status.asr.errors.append(
                            f"- Retries: {self.max_retries}\n- Errors: {exceptions}"
                        )
                    return records
                await asyncio.sleep(0.5 * (n_retry + 1))

        return records