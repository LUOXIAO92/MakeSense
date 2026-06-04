"""
OmniTranslationProvider: produces raw source transcription AND raw multilingual translations in one pass.
"""

import asyncio
import json
from pathlib import Path
from typing import Optional, Sequence

from llm.llm_model import LLM
from core.utils import normalize_generated_text
from pipeline.schema import OmniTranslationResult
from pipeline.validators.omni_translation_validator import (
    OmniTranslationValidationError,
    validate_omni_translation_or_raise,
)
from pipeline.schema import (
    PipelineRecord,
    RawTranslationArtifact,
    StatusEnum,
    TargetLanguageEntry,
    TaskStatus,
    TranscriptArtifact,
)
from pipeline.providers.base import BaseProvider
from pipeline.providers.retry_error_rendering import (
    STRUCTURED_VALIDATION_BULLET_RE,
    is_contract_or_validation_error,
    raise_unless_contract_or_validation_error,
    render_historical_retry_errors,
    render_historical_validation_error,
)

AudioLike = str | Path | bytes | bytearray | dict[str, str]


ValidateExceptions = (OmniTranslationValidationError,)


def _render_historical_validation_error(error: Exception) -> str:
    return render_historical_validation_error(
        error,
        patterns=[STRUCTURED_VALIDATION_BULLET_RE],
    )


def exception_rendering(exceptions: list[Exception]) -> str:
    exception_messages = render_historical_retry_errors(
        exceptions,
        validation_error_types=ValidateExceptions,
        validation_renderer=_render_historical_validation_error,
    )
    if not is_contract_or_validation_error(
        exceptions[-1],
        validation_error_types=ValidateExceptions,
    ):
        return exception_messages
    if isinstance(exceptions[-1], ValidateExceptions):
        exception_messages += f"{len(exceptions)}. **Validation Error**:\n{exceptions[-1]}\n"
    else:
        exception_messages += f"{len(exceptions)}. Current error:\n{exceptions[-1]}\n"
    return exception_messages


def terminal_error_rendering(exceptions: list[Exception], max_retries: int) -> list[str]:
    lines = [f"- Retries: {max_retries}"]
    if len(exceptions) > 1:
        lines.append("- History errors:")
        for i, error in enumerate(exceptions[:-1], start=1):
            lines.append(f"  {i}. {error}")
    lines.append("- Current error:")
    lines.append(f"  {exceptions[-1]}")
    return lines


def _normalize_audio(audio: AudioLike) -> dict[str, str]:
    import base64

    if isinstance(audio, dict):
        if "data" not in audio or "format" not in audio:
            raise ValueError(f"Audio dict must contain 'data' and 'format': {audio}")
        return {"data": audio["data"], "format": audio["format"].lower()}

    if isinstance(audio, (str, Path)):
        from pathlib import Path as _Path
        p = _Path(audio)
        fmt = p.suffix.lstrip(".").lower() or "wav"
        data_b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
        return {"data": data_b64, "format": fmt}

    if isinstance(audio, (bytes, bytearray)):
        data_b64 = base64.b64encode(audio).decode("utf-8")
        return {"data": data_b64, "format": "wav"}

    raise TypeError(f"Unsupported audio input type: {type(audio).__name__}")


class OmniTranslationProvider(BaseProvider):
    """
    Upstream provider that runs an omni multimodal model to produce both
    source transcription and multilingual raw translations in one pass.

    This provider populates:
    - record.source.artifacts.transcript
    - record.target.languages[lang].artifacts.raw_translation for each target language
    """

    def __init__(
        self,
        llm: LLM,
        system_prompt: str,
        user_prompt: str,
        name: str = "OmniTranslationProvider",
        max_retries: int = 6,
    ):
        super().__init__(name=name, max_retries=max_retries)
        self.llm = llm
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt

    async def provide(
        self,
        record: PipelineRecord,
        audio: Optional[AudioLike] = None,
        target_language_names: Optional[Sequence[str]] = None,
        max_tokens: int = 8000,
        temperature: float = 0.6,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        **kwargs,
    ) -> PipelineRecord:
        """
        Run omni-translation ASR+translation and populate transcript + translation artifacts.
        """
        from pipeline.prompts.utils import build_messages_with_audio_placeholders

        if audio is None:
            record.source.status.asr = TaskStatus(
                status=StatusEnum.FAILED,
                errors=["No audio input provided"],
            )
            return record

        if target_language_names is None:
            from configs.config import Config
            expected_target_language_names = [
                Config.lang_code2name[code]
                for code in Config.language_codes
                if code != record.metadata.language
            ]
        else:
            expected_target_language_names = list(target_language_names)

        author = self.llm.model_name
        exceptions: list[Exception] = []
        for n_retry in range(self.max_retries + 1):
            user_prompt = self.user_prompt
            if exceptions:
                exception_messages = exception_rendering(exceptions)
                exception_messages += f"\nRETRY:{n_retry}/{self.max_retries}\n\n"
                user_prompt = exception_messages + user_prompt

            try:
                user_content = build_messages_with_audio_placeholders(user_prompt, audio)
                messages = [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_content},
                ]

                response = await self.llm.chat(
                    messages, max_tokens, temperature, top_p, extra_body
                )

                result_text, scratchpad = self._parse_llm_response(response.content)
                result_text = result_text.lstrip("```json\n").rstrip("\n```")
                result = OmniTranslationResult(**json.loads(result_text))

                validate_omni_translation_or_raise(result, expected_target_language_names)

                from configs.config import Config
                metadata_language_code = (record.metadata.language or "").upper()
                if metadata_language_code in Config.lang_code2name:
                    transcript_language_code = metadata_language_code
                    transcript_language_name = Config.lang_code2name[metadata_language_code]
                else:
                    transcript_language_code = result.asr.get("language_code", "").upper()
                    transcript_language_name = result.asr.get("language_name", "")
                record.source.artifacts.transcript = TranscriptArtifact(
                    language_code=transcript_language_code,
                    language_name=transcript_language_name,
                    text=normalize_generated_text(result.asr.get("text", ""), transcript_language_code),
                    author=author,
                )
                record.source.status.asr = TaskStatus(status=StatusEnum.FINISHED)

                for tgt_lang_name, tgt_text in result.translation.items():
                    from configs.config import Config
                    tgt_lang_code = ""
                    for name, code in Config.lang_name2code.items():
                        if name.lower() == tgt_lang_name.lower():
                            tgt_lang_code = code.upper()
                            break

                    if not tgt_lang_code:
                        continue

                    branch = record.target.languages.setdefault(
                        tgt_lang_code,
                        TargetLanguageEntry(language_code=tgt_lang_code),
                    )

                    branch.artifacts.raw_translation = RawTranslationArtifact(
                        text=normalize_generated_text(tgt_text, tgt_lang_code),
                        author=author,
                    )
                    branch.status.raw_translation = TaskStatus(status=StatusEnum.FINISHED)

                record.target.shared.translation_analysis = scratchpad
                return record

            except Exception as e:
                exceptions.append(e)
                if n_retry == self.max_retries:
                    raise_unless_contract_or_validation_error(e, validation_error_types=ValidateExceptions)
                    errors = terminal_error_rendering(exceptions, self.max_retries)
                    record.source.status.asr = TaskStatus(
                        status=StatusEnum.FAILED,
                        errors=errors,
                    )
                    for tgt_lang_name in expected_target_language_names:
                        from configs.config import Config
                        tgt_lang_code = Config.lang_name2code.get(tgt_lang_name, "").upper()
                        if not tgt_lang_code:
                            continue
                        branch = record.target.languages.setdefault(
                            tgt_lang_code,
                            TargetLanguageEntry(language_code=tgt_lang_code),
                        )
                        branch.status.raw_translation = TaskStatus(
                            status=StatusEnum.FAILED,
                            errors=[],
                        )
                    return record
                await asyncio.sleep(0.5 * (n_retry + 1))

        return record

    def _parse_llm_response(self, response_text: str) -> tuple[str, str]:
        import re

        text = response_text
        sp_open = re.search(r"<scratchpad\s*>", text, re.IGNORECASE)
        sp_close = re.search(r"</scratchpad\s*>", text, re.IGNORECASE)
        rs_open = re.search(r"<result\s*>", text, re.IGNORECASE)
        rs_close = re.search(r"</result\s*>", text, re.IGNORECASE)

        scratchpad = ""
        result = ""

        if sp_open and sp_close and sp_close.start() >= sp_open.end():
            scratchpad = text[sp_open.end() : sp_close.start()].strip()
        elif sp_open and rs_open and rs_open.start() >= sp_open.end():
            scratchpad = text[sp_open.end() : rs_open.start()].strip()

        if rs_open and rs_close and rs_close.start() >= rs_open.end():
            result = text[rs_open.end() : rs_close.start()].strip()
        elif rs_open:
            result = text[rs_open.end() :].strip()
        elif sp_close:
            result = text[sp_close.end() :].strip()

        if not scratchpad and not re.search(r"<scratchpad\s*>", text, re.IGNORECASE):
            raise Exception("Output Format Error: scratchpad block could not be recovered")
        if not result:
            raise Exception("Output Format Error: result block could not be recovered")

        return result, scratchpad


OnePassProvider = OmniTranslationProvider