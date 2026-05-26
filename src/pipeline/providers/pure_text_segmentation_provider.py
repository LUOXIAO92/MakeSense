"""Pure-text segmentation provider for translated text."""

import asyncio
import json
import re
from typing import Optional, Sequence

from configs.config import Config
from core.schema import SenseUnits
from core.utils import tokenize
from llm.llm_model import LLM
from pipeline.schema import (
    PipelineRecord,
    PureTextSegmentationArtifact,
    StatusEnum,
    TaskStatus,
)
from pipeline.providers.base import BaseProvider
from pipeline.providers.retry_error_rendering import (
    PURE_TEXT_OVERSIZED_LINE_RE,
    render_historical_retry_errors,
    render_historical_validation_error,
)
from pipeline.validators.pure_text_segmentation_validator import (
    PureTextSegmentationValidationError,
    validate_pure_text_segmentation_or_raise,
)


ValidateExceptions = (PureTextSegmentationValidationError,)


def _format_token_indices_for_prompt(token_indices: dict[int, str]) -> str:
    """Render token indices as a Python dict-style map for LLM prompt input."""

    return str(token_indices)


def _render_historical_validation_error(error: Exception) -> str:
    return render_historical_validation_error(
        error,
        patterns=[PURE_TEXT_OVERSIZED_LINE_RE],
    )


def exception_rendering(exceptions: list[Exception]) -> str:
    exception_messages = render_historical_retry_errors(
        exceptions,
        validation_error_types=ValidateExceptions,
        validation_renderer=_render_historical_validation_error,
    )
    if isinstance(exceptions[-1], ValidateExceptions):
        exception_messages += f"{len(exceptions)}. **Validation Error**:\n{exceptions[-1]}\n"
    elif "JSON Format Error:" in str(exceptions[-1]) or "Output Format Error" in str(exceptions[-1]):
        exception_messages += f"{len(exceptions)}. **JSON Format Error**:\n{exceptions[-1]}\n"
    else:
        exception_messages += f"{len(exceptions)}. Current error:\n{exceptions[-1]}\n"
    return exception_messages


class PureTextSegmentationProvider(BaseProvider):
    """
    Provider that runs pure text segmentation on translated text.

    This provider populates per-language pure-text segmentation as minimal sense units.
    """

    def __init__(
        self,
        llm: LLM,
        system_prompt: str,
        user_prompt_template: str,
        name: str = "PureTextSegmentationProvider",
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
        max_tokens: int = 1024,
        temperature: float = 0.5,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool = False,
        **kwargs,
    ) -> PipelineRecord:
        """
        Run pure text segmentation for each requested language.
        """
        if target_language_codes is None:
            target_language_codes = list(record.target.languages.keys())

        author = self.llm.model_name
        for tgt_lang_code in target_language_codes:
            if tgt_lang_code not in record.target.languages:
                continue

            language_branch = record.target.languages[tgt_lang_code]
            if not language_branch.artifacts.reconstruction.text:
                language_branch.status.pure_text_segmentation = TaskStatus(
                    status=StatusEnum.FAILED,
                    errors=["No reconstructed translation available for segmentation"],
                )
                continue

            language_branch.status.pure_text_segmentation = TaskStatus(
                status=StatusEnum.RUNNING
            )

            translation_text = language_branch.artifacts.reconstruction.text
            system_prompt, user_prompt = self._build_pure_text_segmentation_prompt(
                language=tgt_lang_code,
                raw_text=translation_text,
            )
            token_indices = tokenize(language=tgt_lang_code, raw_text=translation_text, indexing=True)
            target_tokens = [token_indices[idx] for idx in sorted(token_indices)]

            messages = [
                {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
            ]

            exceptions: list[Exception] = []
            for n_retry in range(self.max_retries + 1):
                retry_messages = messages
                if exceptions:
                    exception_messages = exception_rendering(exceptions)
                    exception_messages += f"\nRETRY:{n_retry}/{self.max_retries}\n\n"
                    retry_messages = [
                        messages[0],
                        {
                            "role": "user",
                            "content": [{"type": "text", "text": exception_messages + user_prompt}],
                        },
                    ]
                try:
                    response = await self.llm.chat(
                        retry_messages, max_tokens, temperature, top_p, top_k, enable_thinking
                    )
                    scratchpad_text, result_text = self._extract_scratchpad_and_result_blocks(response.content)
                    groups = self._parse_segmentation_result(result_text)
                    validate_pure_text_segmentation_or_raise(
                        language=tgt_lang_code,
                        groups=groups,
                        token_indices=token_indices,
                    )

                    sense_units = SenseUnits(level="minimal", groups=groups)

                    language_branch.artifacts.pure_text_segmentation = PureTextSegmentationArtifact(
                        tokens=target_tokens,
                        sense_units=sense_units,
                        author=author,
                    )
                    record.set_debug_pure_text_segmentation(
                        tgt_lang_code,
                        scratchpad=scratchpad_text,
                        result=result_text,
                    )
                    language_branch.status.pure_text_segmentation = TaskStatus(
                        status=StatusEnum.FINISHED
                    )
                    break

                except Exception as e:
                    exceptions.append(e)
                    if n_retry == self.max_retries:
                        language_branch.status.pure_text_segmentation = TaskStatus(
                            status=StatusEnum.FAILED,
                            errors=[f"- Retries: {self.max_retries}\n- Errors: {[str(error) for error in exceptions]}"],
                        )
                    else:
                        await asyncio.sleep(0.5 * (n_retry + 1))

        return record

    def _build_pure_text_segmentation_prompt(
        self,
        language: str,
        raw_text: str,
    ) -> tuple[str, str]:
        lang_pack = Config.language_packs[language]
        token_indices = tokenize(language=language, raw_text=raw_text, indexing=True)

        system_prompt = self.system_prompt \
            .replace("{{LANGUAGE_PACK}}", lang_pack["translation"]["prompt"]) \
            .replace("{{FEW_SHOT_SAMPLES}}", lang_pack["translation"]["few_shot_samples"])

        user_prompt = self.user_prompt_template \
            .replace("{{LANGUAGE}}", language) \
            .replace("{{TOKEN_INDICES}}", _format_token_indices_for_prompt(token_indices))

        return system_prompt, user_prompt

    def _extract_scratchpad_and_result_blocks(self, response_text: str) -> tuple[str, str]:
        text = response_text
        sp_open = re.search(r"<scratchpad\s*>", text, re.IGNORECASE)
        sp_close = re.search(r"</scratchpad\s*>", text, re.IGNORECASE)
        rs_open = re.search(r"<result\s*>", text, re.IGNORECASE)
        rs_close = re.search(r"</result\s*>", text, re.IGNORECASE)

        scratchpad_text = ""
        if sp_open and sp_close and sp_close.start() >= sp_open.end():
            scratchpad_text = text[sp_open.end() : sp_close.start()].strip()
        elif sp_open and rs_open and rs_open.start() >= sp_open.end():
            scratchpad_text = text[sp_open.end() : rs_open.start()].strip()

        result_text = ""
        if rs_open and rs_close and rs_close.start() >= rs_open.end():
            result_text = text[rs_open.end() : rs_close.start()].strip()
        elif rs_open:
            result_text = text[rs_open.end() :].strip()
        else:
            result_text = text.strip()

        bracket_depth = 0
        start_idx = None
        for i, ch in enumerate(result_text):
            if ch == '[' and start_idx is None:
                start_idx = i
                bracket_depth = 1
            elif ch == '[' and start_idx is not None:
                bracket_depth += 1
            elif ch == ']' and start_idx is not None:
                bracket_depth -= 1
                if bracket_depth == 0:
                    result_text = result_text[start_idx:i + 1]
                    break

        if not result_text:
            raise Exception("Output Format Error: result block could not be recovered")

        return scratchpad_text, result_text

    def _parse_segmentation_result(self, result_text: str) -> list[list[int]]:
        """Parse extracted result block into list of token index groups."""

        try:
            groups = json.loads(result_text)
        except Exception as e:
            raise Exception(f"JSON Format Error: {e}") from e

        if groups and isinstance(groups, list) and isinstance(groups[0], int):
            groups = [[x] for x in groups]

        return groups
