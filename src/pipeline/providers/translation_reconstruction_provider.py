"""Translation reconstruction provider for multi-language target-side restructuring."""

import asyncio
import json
import re
from dataclasses import dataclass
from typing import Optional, Sequence

from core.utils import apply_mapping_groups, build_transcription_chunks, normalize_generated_text, process_words
from configs.config import Config
from llm.llm_model import LLM
from pipeline.providers.base import BaseProvider
from pipeline.providers.retry_error_rendering import (
    STRUCTURED_VALIDATION_BULLET_RE,
    is_contract_or_validation_error,
    raise_unless_contract_or_validation_error,
    render_historical_retry_errors,
    render_historical_validation_error,
)
from pipeline.schema import (
    PipelineRecord,
    ReconstructedTranslationArtifact,
    StatusEnum,
    TaskStatus,
    TargetLanguageEntry,
)
from pipeline.validators.reconstruction_validator import ReconstructionValidator


class TranslationReconstructionProvider(BaseProvider):
    """Provider that reconstructs target translations for the requested language branch set."""

    def __init__(
        self,
        llm: LLM,
        system_prompt: str,
        user_prompt_template: str,
        name: str = "TranslationReconstructionProvider",
        max_retries: int = 6,
        reconstruction_validator: ReconstructionValidator | None = None,
        source_windows_per_validator_window: int = 1,
    ):
        super().__init__(name=name, max_retries=max_retries)
        self.llm = llm
        self.system_prompt = system_prompt
        self.user_prompt_template = user_prompt_template
        self.reconstruction_validator = reconstruction_validator or ReconstructionValidator(llm=llm)
        if source_windows_per_validator_window < 1:
            raise ValueError("source_windows_per_validator_window must be >= 1")
        self.source_windows_per_validator_window = source_windows_per_validator_window

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
        transcript = record.source.artifacts.transcript
        if transcript is None or not transcript.text:
            for code in list(target_language_codes or []):
                branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
                branch.status.reconstruction = TaskStatus(
                    status=StatusEnum.FAILED,
                    errors=["No source transcript available for reconstruction"],
                )
            return record

        if target_language_codes is None:
            target_language_codes = [
                code for code in Config.language_codes if code != record.metadata.language
            ]

        target_language_codes = list(target_language_codes)
        target_language_names = [Config.lang_code2name.get(code, code) for code in target_language_codes]

        missing_raw = [
            code for code in target_language_codes
            if code not in record.target.languages or not record.target.languages[code].artifacts.raw_translation.text
        ]
        if missing_raw:
            for code in target_language_codes:
                branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
                branch.status.reconstruction = TaskStatus(
                    status=StatusEnum.FAILED,
                    errors=[f"Missing raw translation dependencies: {missing_raw}"],
                )
            return record

        for code in target_language_codes:
            branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
            branch.status.reconstruction = TaskStatus(status=StatusEnum.RUNNING)

        author = self.llm.model_name
        exceptions: list[Exception] = []
        attempts_debug: list[dict[str, str | int]] = []
        scratchpad = ""
        result_text = ""
        for n_retry in range(self.max_retries + 1):
            user_prompt = self.user_prompt_template
            if exceptions:
                exception_messages = exception_rendering(exceptions)
                if exception_messages.strip():
                    exception_messages += f"\nRETRY:{n_retry}/{self.max_retries}\n\n"
                    user_prompt = exception_messages + user_prompt

            messages = [
                {"role": "system", "content": [{"type": "text", "text": self.system_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
            ]

            response = None
            attempt_debug: dict[str, str | int] = {
                "attempt": n_retry + 1,
                "retry_index": n_retry,
                "retry": n_retry,
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
                result_text, scratchpad = self._parse_reconstruction_response(response.content)
                attempt_debug["scratchpad"] = scratchpad
                attempt_debug["result"] = result_text
                reconstructions = self._parse_reconstruction_result(
                    result_text=result_text,
                    expected_target_language_names=target_language_names,
                )

                for code, target_name in zip(target_language_codes, target_language_names):
                    semantic_feedback = await self._run_reconstruction_semantic_check(
                        record=record,
                        target_language_code=code,
                        raw_translation=record.target.languages[code].artifacts.raw_translation.text,
                        candidate_reconstruction=reconstructions[target_name],
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        extra_body=extra_body,
                    )
                    if semantic_feedback:
                        raise TranslationReconstructionValidationError(semantic_feedback)

                for code, target_name in zip(target_language_codes, target_language_names):
                    branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
                    branch.artifacts.reconstruction = ReconstructedTranslationArtifact(
                        text=normalize_generated_text(reconstructions[target_name], code),
                        author=author,
                    )
                    attempt_debug["status"] = "succeeded"
                    attempt_debug["reason"] = (
                        "initial attempt succeeded"
                        if n_retry == 0
                        else "retry attempt succeeded"
                    )
                    self._set_debug_translation_reconstruction(
                        record,
                        code,
                        scratchpad=scratchpad,
                        result=result_text,
                        attempts=attempts_debug,
                    )
                    branch.status.reconstruction = TaskStatus(status=StatusEnum.FINISHED)

                return record
            except Exception as e:
                validator_debug = self._reconstruction_validator_debug()
                if validator_debug:
                    for key, value in validator_debug.items():
                        attempt_debug[f"validator_{key}"] = value
                attempt_debug["status"] = (
                    "failed_after_response"
                    if attempt_debug.get("scratchpad") or attempt_debug.get("result") or validator_debug
                    else "failed_before_response"
                )
                attempt_debug["error"] = str(e)
                attempt_debug["reason"] = str(e)
                exceptions.append(e)
                if n_retry == self.max_retries:
                    raise_unless_contract_or_validation_error(e, validation_error_types=ValidateExceptions)
                    exceptions_str = [str(error) for error in exceptions]
                    for code in target_language_codes:
                        branch = record.target.languages.setdefault(code, TargetLanguageEntry(language_code=code))
                        self._set_debug_translation_reconstruction(
                            record,
                            code,
                            scratchpad=locals().get("scratchpad", ""),
                            result=locals().get("result_text", "") or (response.content if response else ""),
                            attempts=attempts_debug,
                        )
                        branch.status.reconstruction = TaskStatus(
                            status=StatusEnum.FAILED,
                            errors=[
                                str(
                                    TranslationReconstructionFailed(
                                        f"- Retries: {self.max_retries}\n- Errors: {exceptions_str}"
                                    )
                                )
                            ],
                        )
                    return record
                await asyncio.sleep(0.5 * (n_retry + 1))

        return record

    def _source_alignment_tokens_and_windows(self, record: PipelineRecord) -> tuple[list[str], dict[int, int]] | tuple[None, None]:
        alignment = record.source.artifacts.alignment
        if alignment is None or not alignment.tokens:
            return None, None
        if not any(alignment.words):
            word_groups = process_words(
                record.metadata.language,
                alignment.tokens,
                record.source.artifacts.transcript.text if record.source.artifacts.transcript else None,
            )
        else:
            word_groups = alignment.words
        source_words = apply_mapping_groups(
            alignment.tokens,
            word_groups,
            language=record.metadata.language,
        )
        if not source_words:
            return None, None
        chunks = build_transcription_chunks(
            duration=record.metadata.duration,
            words=source_words,
        )
        source_window_by_token: dict[int, int] = {}
        source_token_id = 0
        for pure_window_id, chunk in enumerate(chunks):
            validator_window_id = pure_window_id // self.source_windows_per_validator_window
            for _ in chunk.words:
                source_window_by_token[source_token_id] = validator_window_id
                source_token_id += 1
        return [word.word for word in source_words], source_window_by_token

    def _reconstruction_validator_debug(self) -> dict[str, str]:
        debug = getattr(self.reconstruction_validator, "last_debug", {})
        if not isinstance(debug, dict):
            return {}
        return {str(key): str(value) for key, value in debug.items()}

    async def _run_reconstruction_semantic_check(
        self,
        *,
        record: PipelineRecord,
        target_language_code: str,
        raw_translation: str,
        candidate_reconstruction: str,
        max_tokens: int,
        temperature: float,
        top_p: float,
        extra_body: dict | None,
    ) -> str | None:
        transcript = record.source.artifacts.transcript
        if transcript is None or not transcript.text:
            return None
        source_tokens, source_window_by_token = self._source_alignment_tokens_and_windows(record)
        return await self.reconstruction_validator.validate_or_get_feedback(
            source_language_code=record.metadata.language,
            target_language_code=target_language_code,
            source_text=transcript.text,
            raw_translation=raw_translation,
            candidate_reconstruction=candidate_reconstruction,
            source_tokens=source_tokens,
            source_window_by_token=source_window_by_token,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            extra_body=extra_body,
        )

    def _set_debug_translation_reconstruction(
        self,
        record: PipelineRecord,
        language_code: str,
        *,
        scratchpad: str = "",
        result: str = "",
        attempts: list[dict[str, str | int]] | None = None,
    ) -> None:
        validator_debug = self._reconstruction_validator_debug()
        record.set_debug_translation_reconstruction(
            language_code,
            scratchpad=scratchpad,
            result=result,
            validator_scratchpad=validator_debug.get("scratchpad", ""),
            validator_result=validator_debug.get("validator_result", validator_debug.get("result", "")),
            validator_order_risk=validator_debug.get("order_risk", ""),
            validator_source_tokens=validator_debug.get("source_tokens_inline", ""),
            validator_source_windows=validator_debug.get("source_windows", ""),
            validator_feedback=validator_debug.get("feedback", ""),
            attempts=attempts,
        )

    def _parse_reconstruction_response(self, response_text: str) -> tuple[str, str]:
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
            result = text.strip()

        return result, scratchpad

    def _parse_reconstruction_result(
        self,
        result_text: str,
        expected_target_language_names: Sequence[str],
    ) -> dict[str, str]:
        if len(expected_target_language_names) == 1:
            value = parse_single_translation_reconstruction_text_or_raise(result_text)
            return {expected_target_language_names[0]: value}

        payload = parse_translation_reconstruction_payload_or_raise(result_text)
        payload = validate_translation_reconstruction_or_raise(
            payload=payload,
            expected_target_language_names=expected_target_language_names,
        )
        return payload


class TranslationReconstructionFailed(Exception):
    pass


class TranslationReconstructionValidationError(ValueError):
    """Raised when translation reconstruction violates hard validation rules."""


@dataclass(frozen=True)
class TranslationReconstructionDiagnostics:
    expected_target_languages: list[str]
    produced_target_languages: list[str]
    missing_target_languages: list[str]
    unexpected_target_languages: list[str]
    empty_target_languages: list[str]
    non_string_target_languages: list[str]

    @property
    def has_error(self) -> bool:
        return any([
            self.missing_target_languages,
            self.unexpected_target_languages,
            self.empty_target_languages,
            self.non_string_target_languages,
        ])


def _is_blank_string(value) -> bool:
    return not isinstance(value, str) or not value.strip()


def collect_translation_reconstruction_diagnostics(
    payload: dict[str, object],
    expected_target_language_names: Sequence[str],
) -> TranslationReconstructionDiagnostics:
    expected_target_languages = list(expected_target_language_names)

    produced_target_languages = list(payload.keys())
    expected_set = set(expected_target_languages)
    produced_set = set(produced_target_languages)

    missing_target_languages = sorted(expected_set - produced_set)
    unexpected_target_languages = sorted(produced_set - expected_set)
    empty_target_languages: list[str] = []
    non_string_target_languages: list[str] = []

    for lang_name in expected_target_languages:
        if lang_name not in payload:
            continue
        value = payload[lang_name]
        if not isinstance(value, str):
            non_string_target_languages.append(lang_name)
        elif _is_blank_string(value):
            empty_target_languages.append(lang_name)

    return TranslationReconstructionDiagnostics(
        expected_target_languages=expected_target_languages,
        produced_target_languages=produced_target_languages,
        missing_target_languages=missing_target_languages,
        unexpected_target_languages=unexpected_target_languages,
        empty_target_languages=empty_target_languages,
        non_string_target_languages=non_string_target_languages,
    )


def validate_translation_reconstruction_or_raise(
    payload: dict[str, object],
    expected_target_language_names: Sequence[str],
) -> dict[str, str]:
    diagnostics = collect_translation_reconstruction_diagnostics(
        payload=payload,
        expected_target_language_names=expected_target_language_names,
    )

    if not diagnostics.has_error:
        return {key: str(value) for key, value in payload.items()}

    parts: list[str] = ["Translation reconstruction validation failed:"]
    parts.append(
        f"- expected target languages: {diagnostics.expected_target_languages}"
    )
    parts.append(
        f"- produced target languages: {diagnostics.produced_target_languages}"
    )

    if diagnostics.missing_target_languages:
        parts.append(
            f"- missing reconstruction outputs: {diagnostics.missing_target_languages}"
        )

    if diagnostics.unexpected_target_languages:
        parts.append(
            f"- unexpected reconstruction outputs: {diagnostics.unexpected_target_languages}"
        )

    if diagnostics.empty_target_languages:
        parts.append(
            f"- empty reconstruction outputs: {diagnostics.empty_target_languages}"
        )

    if diagnostics.non_string_target_languages:
        parts.append(
            f"- non-string reconstruction outputs: {diagnostics.non_string_target_languages}"
        )

    parts.append("\nReconfirm the OUTPUT FORMAT and OUTPUT RULES!\n")
    raise TranslationReconstructionValidationError("\n".join(parts))


def parse_translation_reconstruction_payload_or_raise(result_text: str) -> dict[str, object]:
    try:
        parsed = json.loads(result_text)
    except Exception as e:
        raise Exception(f"JSON Format Error: {e}") from e

    if not isinstance(parsed, dict):
        raise Exception("JSON Format Error: <result> must be a JSON object")

    return parsed


def parse_single_translation_reconstruction_text_or_raise(result_text: str) -> str:
    if not isinstance(result_text, str) or not result_text.strip():
        raise TranslationReconstructionValidationError(
            "Translation reconstruction validation failed:\n"
            "- empty reconstruction output for single-language reconstruction\n"
            "\nReconfirm the OUTPUT FORMAT and OUTPUT RULES!\n"
        )
    return result_text.strip()


ValidateExceptions = (TranslationReconstructionValidationError,)


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
    elif "JSON Format Error:" in str(exceptions[-1]):
        exception_messages += f"{len(exceptions)}. **JSON Format Error**:\n{exceptions[-1]}\n"
    else:
        exception_messages += f"{len(exceptions)}. Current error:\n{exceptions[-1]}\n"
    return exception_messages