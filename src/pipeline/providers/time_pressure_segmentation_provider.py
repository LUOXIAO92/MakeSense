"""TimePressureSegmentationProvider: segments transcript with time pressure logic via LLM."""

import asyncio
import json
import re

from configs.config import Config
from core.schema import MetaData, SenseUnits, Transcription
from core.utils import apply_mapping_groups, build_transcription_chunks, process_words, render_transcription_chunk_word_indices
from llm.llm_model import LLM
from pipeline.prompts.time_pressure_segmentation import (
    SYSTEM_INSTRUCTION as SYS_TIME_PRESSURE_SEGMENTATION,
    USER_INSTRUCTION as USR_TIME_PRESSURE_SEGMENTATION,
)
from pipeline.providers.base import BaseProvider
from pipeline.providers.retry_error_rendering import (
    ASR_VALIDATION_ISSUE_WINDOW_RE,
    is_contract_or_validation_error,
    raise_unless_contract_or_validation_error,
    render_historical_retry_errors,
    render_historical_validation_error,
)
from pipeline.schema import (
    PipelineRecord,
    StatusEnum,
    TimePressureSegmentationArtifact,
)
from pipeline.validators.transcription_segmentation_validator import (
    ASRChunkingValidationError,
    validate_chunking_or_raise,
)

ValidateExceptions = (ASRChunkingValidationError,)


def _render_historical_validation_error(error: Exception) -> str:
    """Render only actionable issue rows from a historical validation error."""

    return render_historical_validation_error(
        error,
        patterns=[ASR_VALIDATION_ISSUE_WINDOW_RE],
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
    elif "JSON Format Error:" in str(exceptions[-1]) or "Output Format Error" in str(exceptions[-1]):
        exception_messages += f"{len(exceptions)}. **JSON Format Error**:\n{exceptions[-1]}\n"
    else:
        exception_messages += f"{len(exceptions)}. Current error:\n{exceptions[-1]}\n"
    return exception_messages


class TimePressureSegmentationProvider(BaseProvider):
    """
    Upstream provider that runs an LLM to segment the source transcript
    into sense units (minimal sense unit-level groupings of token indices).

    This provider populates record.source.artifacts.time_pressure_segmentation.
    """

    def __init__(
        self,
        llm: LLM,
        system_prompt: str,
        user_prompt_template: str,
        name: str = "TimePressureSegmentationProvider",
        max_retries: int = 6,
    ):
        super().__init__(name=name, max_retries=max_retries)
        self.llm = llm
        self.system_prompt = system_prompt
        self.user_prompt_template = user_prompt_template

    async def provide(
        self,
        record: PipelineRecord,
        max_tokens: int = 1024,
        temperature: float = 0.5,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        **kwargs,
    ) -> PipelineRecord:
        """Run time-pressure segmentation on the transcript and alignment."""
        author = self.llm.model_name
        record.source.status.time_pressure_segmentation.status = StatusEnum.RUNNING
        record.source.status.time_pressure_segmentation.errors.clear()

        transcript = record.source.artifacts.transcript
        alignment = record.source.artifacts.alignment

        if transcript is None or not transcript.text:
            record.source.status.time_pressure_segmentation.status = StatusEnum.FAILED
            record.source.status.time_pressure_segmentation.errors.append(
                "No source transcript available for segmentation"
            )
            return record

        if alignment is None or not alignment.tokens:
            record.source.status.time_pressure_segmentation.status = StatusEnum.FAILED
            record.source.status.time_pressure_segmentation.errors.append(
                "No source alignment/tokens available for segmentation"
            )
            return record

        system_prompt, user_prompt, _ = self._build_transcription_prompt(
            record.metadata,
            transcript.language_code or record.metadata.language,
            transcript.text,
            alignment.tokens,
            alignment.words,
        )

        exceptions: list[Exception] = []
        attempts_debug: list[dict[str, str | int]] = []
        scratchpad_text = ""
        result_text = ""
        for n_retry in range(self.max_retries + 1):
            retry_user_prompt = user_prompt
            if exceptions:
                exception_messages = exception_rendering(exceptions)
                if exception_messages.strip():
                    exception_messages += f"\nRETRY:{n_retry}/{self.max_retries}\n\n"
                    retry_user_prompt = exception_messages + retry_user_prompt

            messages = [
                {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": retry_user_prompt}]},
            ]

            attempt_debug: dict[str, str | int] = {
                "attempt": n_retry + 1,
                "retry_index": n_retry,
                "retry": n_retry,  # Backward-compatible debug key for old readers.
                "max_retries": self.max_retries,
                "max_attempts": self.max_retries + 1,
                "scratchpad": "",
                "result": "",
                "status": "running",
                "reason": "",
                "error": "",
            }
            attempts_debug.append(attempt_debug)
            try:
                response = await self.llm.chat(
                    messages, max_tokens, temperature, top_p, extra_body
                )
                scratchpad_text, result_text = self._extract_scratchpad_and_result(response.content)
                attempt_debug["scratchpad"] = scratchpad_text
                attempt_debug["result"] = result_text
                groups = self._parse_segmentation_result(result_text)

                sense_units = SenseUnits(level="minimal", groups=groups)

                transcription = Transcription(
                    uid=record.uid,
                    language=transcript.language_code or record.metadata.language,
                    text=transcript.text,
                    tokens=alignment.tokens,
                    words=alignment.words,
                    sense_units=sense_units,
                    author=transcript.author,
                )
                metadata = MetaData(
                    uid=record.metadata.uid,
                    file_name=record.metadata.file_name,
                    duration=record.metadata.duration,
                    sample_rate=record.metadata.sample_rate,
                    language=record.metadata.language,
                    subset=record.metadata.subset,
                    quality=record.metadata.quality,
                )

                validate_chunking_or_raise(metadata, transcription)
                attempt_debug["status"] = "succeeded"
                attempt_debug["reason"] = (
                    "initial attempt succeeded"
                    if n_retry == 0
                    else "retry attempt succeeded"
                )

                record.source.artifacts.time_pressure_segmentation = TimePressureSegmentationArtifact(
                    sense_units=sense_units,
                    author=author,
                )
                record.set_debug_time_pressure_segmentation(
                    scratchpad=scratchpad_text,
                    result=result_text,
                    attempts=attempts_debug,
                )
                record.source.status.time_pressure_segmentation.status = StatusEnum.FINISHED
                return record

            except Exception as e:
                attempt_debug["status"] = (
                    "failed_after_response"
                    if attempt_debug.get("scratchpad") or attempt_debug.get("result")
                    else "failed_before_response"
                )
                attempt_debug["error"] = str(e)
                attempt_debug["reason"] = str(e)
                exceptions.append(e)
                if n_retry == self.max_retries:
                    raise_unless_contract_or_validation_error(e, validation_error_types=ValidateExceptions)
                    exceptions_str = [str(error) for error in exceptions]
                    record.set_debug_time_pressure_segmentation(
                        scratchpad=scratchpad_text,
                        result=result_text,
                        attempts=attempts_debug,
                    )
                    record.source.status.time_pressure_segmentation.status = StatusEnum.FAILED
                    record.source.status.time_pressure_segmentation.errors.append(
                        f"- Retries: {self.max_retries}\n- Errors: {exceptions_str}"
                    )
                    return record
                await asyncio.sleep(0.5 * (n_retry + 1))

        return record

    def _build_transcription_prompt(
        self,
        metadata: MetaData,
        language: str,
        raw_text: str,
        tokens: list,
        words_groups: list[list[int]],
    ) -> tuple[str, str, list[list[int]]]:
        lang_pack = Config.language_packs[language]

        if not any(words_groups):
            groups = process_words(language, tokens, raw_text)
        else:
            groups = words_groups

        words = apply_mapping_groups(tokens, groups, language=language)
        chunks = build_transcription_chunks(duration=metadata.duration, words=words)
        word_indices = render_transcription_chunk_word_indices(chunks)

        system_prompt = SYS_TIME_PRESSURE_SEGMENTATION.replace(
            "Each dictionary in `word_indices` is one **{{WINDOW_SIZE}}-second time window**.\n", ""
        )
        system_prompt = system_prompt \
            .replace("{{LANGUAGE_PACK}}", lang_pack["transcription"]["prompt"]) \
            .replace("{{FEW_SHOT_SAMPLES}}", lang_pack["transcription"]["few_shot_samples"])

        user_prompt = USR_TIME_PRESSURE_SEGMENTATION \
            .replace("{{RAW_TEXT}}", raw_text) \
            .replace("{{WORD_INDICES}}", str(word_indices))
        return system_prompt, user_prompt, groups

    def _extract_scratchpad_and_result(self, response_text: str) -> tuple[str, str]:
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

        return scratchpad_text, result_text

    def _parse_segmentation_result(self, result_text: str) -> list[list[int]]:
        """Parse extracted result block into list of token index groups."""

        # Look for the outermost [...] pattern
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
                    result_text = result_text[start_idx:i+1]
                    break

        if not result_text:
            raise Exception("Output Format Error: result block could not be recovered")

        try:
            groups = json.loads(result_text)
        except Exception as e:
            raise Exception(f"JSON Format Error: {e}") from e

        # If the LLM returns a flat list, wrap each element in its own list
        if groups and isinstance(groups, list) and isinstance(groups[0], int):
            groups = [[x] for x in groups]

        return groups
