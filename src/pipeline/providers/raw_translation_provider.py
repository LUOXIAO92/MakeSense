"""
RawTranslationProvider: produces raw multilingual translations from source text via LLM.
"""

import asyncio
from typing import Optional, Sequence

from llm.llm_model import LLM
from core.utils import normalize_generated_text
from pipeline.schema import (
    PipelineRecord,
    RawTranslationArtifact,
    StatusEnum,
    TaskStatus,
    TargetLanguageEntry,
)
from pipeline.providers.base import BaseProvider
from pipeline.providers.retry_error_rendering import raise_unless_contract_or_validation_error


class RawTranslationProvider(BaseProvider):
    """
    Upstream provider that runs an LLM to produce raw translations
    from the source transcription text.

    This provider populates record.target.languages[lang].artifacts.raw_translation for each target language.
    It does NOT perform reconstruction, segmentation, or mapping.
    """

    def __init__(
        self,
        llm: LLM,
        system_prompt: str,
        user_prompt_template: str,
        name: str = "RawTranslationProvider",
        max_retries: int = 6,
    ):
        super().__init__(name=name, max_retries=max_retries)
        self.llm = llm
        self.system_prompt = system_prompt
        self.user_prompt_template = user_prompt_template

    async def provide(
        self,
        record: PipelineRecord,
        target_language_codes: Optional[Sequence[str]] = None,
        max_tokens: int = 4096,
        temperature: float = 0.5,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        **kwargs,
    ) -> PipelineRecord:
        """
        Run translation for each target language from the source transcript text.
        """

        if target_language_codes is None:
            from configs.config import Config
            target_language_codes = [
                code for code in Config.language_codes
                if code != record.metadata.language
            ]

        tgt_lang_codes = list(target_language_codes)

        transcript = record.source.artifacts.transcript
        if transcript is None or not transcript.text:
            for tgt_lang_code in tgt_lang_codes:
                branch = record.target.languages.setdefault(
                    tgt_lang_code,
                    TargetLanguageEntry(language_code=tgt_lang_code),
                )
                branch.status.raw_translation = TaskStatus(
                    status=StatusEnum.FAILED,
                    errors=["No source transcript available for translation"],
                )
            return record

        source_text = transcript.text
        from configs.config import Config
        source_language_code = (record.metadata.language or "").upper()
        if source_language_code not in Config.lang_code2name:
            for tgt_lang_code in tgt_lang_codes:
                branch = record.target.languages.setdefault(
                    tgt_lang_code,
                    TargetLanguageEntry(language_code=tgt_lang_code),
                )
                branch.status.raw_translation = TaskStatus(
                    status=StatusEnum.FAILED,
                    errors=["Missing or unsupported source language for raw translation"],
                )
            return record

        source_lang_name = Config.lang_code2name[source_language_code]

        tgt_lang_names = [
            Config.lang_code2name.get(code, code) for code in tgt_lang_codes
        ]

        user_prompt = (
            self.user_prompt_template
            .replace("{{SOURCE_LANGUAGE}}", source_lang_name)
            .replace("{{TARGET_LANGUAGES}}", ", ".join(tgt_lang_names) if tgt_lang_names else "all")
            .replace("{{RAW_TEXT}}", source_text)
        )

        messages = [
            {"role": "system", "content": [{"type": "text", "text": self.system_prompt}]},
            {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
        ]

        author = self.llm.model_name
        errors_by_lang: dict[str, list[str]] = {}

        for tgt_lang_code, tgt_lang_name in zip(tgt_lang_codes, tgt_lang_names):
            branch = record.target.languages.setdefault(
                tgt_lang_code,
                TargetLanguageEntry(language_code=tgt_lang_code),
            )
            branch.status.raw_translation = TaskStatus(
                status=StatusEnum.RUNNING
            )

            exceptions: list[str] = []
            for n_retry in range(self.max_retries + 1):
                try:
                    response = await self.llm.chat(
                        messages, max_tokens, temperature, top_p, extra_body
                    )
                    translation_text, scratchpad = self._parse_translation_response(
                        response.content
                    )

                    branch.artifacts.raw_translation = RawTranslationArtifact(
                        text=normalize_generated_text(translation_text, tgt_lang_code),
                        author=author,
                    )
                    branch.status.raw_translation = TaskStatus(
                        status=StatusEnum.FINISHED
                    )
                    break

                except Exception as e:
                    exceptions.append(str(e))
                    if n_retry == self.max_retries:
                        raise_unless_contract_or_validation_error(e)
                        branch.status.raw_translation = TaskStatus(
                            status=StatusEnum.FAILED,
                            errors=exceptions,
                        )
                        errors_by_lang[tgt_lang_code] = exceptions
                    else:
                        await asyncio.sleep(0.5 * (n_retry + 1))

        return record

    def _parse_translation_response(self, response_text: str) -> tuple[str, str]:
        """
        Parse LLM response into translation text and optional scratchpad/analysis.
        Uses the same <scratchpad>/<result> convention as other agents.
        """
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
        elif not sp_open and not rs_open:
            # No tags found, treat whole response as result
            result = text.strip()

        if "source_rhythm_profile" not in scratchpad:
            scratchpad += "\n- source_rhythm_profile:\n  - none"
        scratchpad = scratchpad.strip()

        return result, scratchpad