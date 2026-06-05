"""Target-centric mapping provider for source-target sense unit mapping."""

import asyncio
import json
import re
from typing import Optional, Sequence

from configs.config import Config
from core.schema import Mapping
from core.utils import group_tokens_by_sense_units
from llm.llm_model import LLM
from pipeline.prompts.target_centric_mapping import (
    SYSTEM_INSTRUCTION_SENSE_UNIT_MAPPING,
    USER_PROMPT__SENSE_UNIT_MAPPING,
)
from pipeline.providers.base import BaseProvider
from pipeline.providers.retry_error_rendering import (
    MAPPING_LOCAL_REGION_LINE_RE,
    is_contract_or_validation_error,
    raise_unless_contract_or_validation_error,
    render_historical_retry_errors,
    render_historical_validation_error,
)
from pipeline.schema import PipelineRecord, StatusEnum, TaskStatus
from pipeline.validators.target_centric_mapping_validator import (
    SEMANTIC_CHECK_MAX_RETRIES,
    SYSTEM_INSTRUCTION_MAPPING_SEMANTIC_CHECK,
    TargetCentricMappingDependencyError,
    TargetCentricMappingSemanticFeedbackError,
    TargetCentricMappingValidationError,
    build_local_regions_with_inline_triggers,
    collect_level2_mapping_diagnostics,
    extract_semantic_check_raw_blocks,
    extract_semantic_mapping_error_feedback_or_raise,
    render_level3_semantic_check_input,
    validate_mapping_downstream_readiness_or_raise,
    validate_mapping_result_or_raise,
)


ValidateExceptions = (TargetCentricMappingValidationError,)


def _render_historical_validation_error(error: Exception) -> str:
    return render_historical_validation_error(
        error,
        patterns=[MAPPING_LOCAL_REGION_LINE_RE],
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
    if "JSON Format Error:" in str(exceptions[-1]) or "Output Format Error" in str(exceptions[-1]):
        exception_messages += f"{len(exceptions)}. **JSON Format Error**:\n{exceptions[-1]}\n"
    else:
        exception_messages += f"{len(exceptions)}. Current error:\n{exceptions[-1]}\n"
    return exception_messages


SEMANTIC_CHECK_UNVERIFIED_MAPPING_FEEDBACK = (
    "Validation failed because the candidate mapping could not be semantically verified. "
    "Please revise the mapping so each target_senseunit_id maps only to source_token_ids "
    "directly needed by that target sense unit."
)


class TargetCentricMappingProvider(BaseProvider):
    """Provider that runs target-centric source-target sense-unit mapping."""

    def __init__(
        self,
        llm: LLM,
        system_prompt: str = SYSTEM_INSTRUCTION_SENSE_UNIT_MAPPING,
        user_prompt_template: str = USER_PROMPT__SENSE_UNIT_MAPPING,
        semantic_check_system_prompt: str = SYSTEM_INSTRUCTION_MAPPING_SEMANTIC_CHECK,
        name: str = "TargetCentricMappingProvider",
        max_retries: int = 6,
    ):
        super().__init__(name=name, max_retries=max_retries)
        self.llm = llm
        self.system_prompt = system_prompt
        self.user_prompt_template = user_prompt_template
        self.semantic_check_system_prompt = semantic_check_system_prompt

    async def provide(
        self,
        record: PipelineRecord,
        target_language_codes: Optional[Sequence[str]] = None,
        max_tokens: int = 1024,
        temperature: float = 0.5,
        top_p: float = 0.95,
        extra_body: dict | None = None,
        **kwargs,
    ) -> PipelineRecord:
        if target_language_codes is None:
            target_language_codes = list(record.target.languages.keys())

        author = self.llm.model_name
        for tgt_lang_code in target_language_codes:
            if tgt_lang_code not in record.target.languages:
                continue

            branch = record.target.languages[tgt_lang_code]
            prerequisite_errors = self._validate_prerequisites(record, tgt_lang_code)
            if prerequisite_errors:
                branch.status.tgt_src_mapping = TaskStatus(
                    status=StatusEnum.FAILED,
                    errors=prerequisite_errors,
                )
                continue

            branch.status.tgt_src_mapping = TaskStatus(status=StatusEnum.RUNNING)
            system_prompt, user_prompt = self._build_mapping_prompt(record, tgt_lang_code)
            messages = [
                {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
                {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
            ]

            exceptions: list[Exception] = []
            attempts_debug: list[dict[str, str | int]] = []
            scratchpad_text = ""
            result_text = ""
            for n_retry in range(self.max_retries + 1):
                retry_messages = messages
                if exceptions:
                    exception_messages = exception_rendering(exceptions)
                    if exception_messages.strip():
                        exception_messages += f"\nRETRY:{n_retry}/{self.max_retries}\n\n"
                        retry_messages = [
                            messages[0],
                            {
                                "role": "user",
                                "content": [{"type": "text", "text": exception_messages + user_prompt}],
                            },
                        ]
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
                        retry_messages, max_tokens, temperature, top_p, extra_body
                    )
                    scratchpad_text, result_text = self._extract_scratchpad_and_result_blocks(response.content)
                    attempt_debug["scratchpad"] = scratchpad_text
                    attempt_debug["result"] = result_text
                    mappings = self._parse_mapping_result(result_text)
                    self._validate_mapping_result(record, tgt_lang_code, mappings)
                    semantic_feedback = await self._run_level3_semantic_checks(
                        record=record,
                        target_language_code=tgt_lang_code,
                        mappings=mappings,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        extra_body=extra_body,
                    )
                    if semantic_feedback:
                        raise TargetCentricMappingSemanticFeedbackError(semantic_feedback)
                    branch.artifacts.tgt_src_mapping.mappings = mappings
                    branch.artifacts.tgt_src_mapping.author = author
                    attempt_debug["status"] = "succeeded"
                    attempt_debug["reason"] = (
                        "initial attempt succeeded"
                        if n_retry == 0
                        else "retry attempt succeeded"
                    )
                    record.set_debug_target_centric_mapping(
                        tgt_lang_code,
                        scratchpad=scratchpad_text,
                        result=result_text,
                        attempts=attempts_debug,
                    )
                    branch.status.tgt_src_mapping = TaskStatus(status=StatusEnum.FINISHED)
                    break
                except TargetCentricMappingDependencyError as e:
                    branch.artifacts.tgt_src_mapping.mappings = []
                    branch.artifacts.tgt_src_mapping.author = ""
                    attempt_debug["status"] = (
                        "failed_after_response"
                        if attempt_debug.get("scratchpad") or attempt_debug.get("result")
                        else "failed_before_response"
                    )
                    attempt_debug["error"] = str(e)
                    attempt_debug["reason"] = str(e)
                    response_content = getattr(locals().get("response", None), "content", "")
                    scratchpad_text = locals().get("scratchpad_text", "")
                    result_text = locals().get("result_text", "") or response_content
                    record.set_debug_target_centric_mapping(
                        tgt_lang_code,
                        scratchpad=scratchpad_text,
                        result=result_text,
                        error=str(e),
                        attempts=attempts_debug,
                    )
                    branch.status.tgt_src_mapping = TaskStatus(
                        status=StatusEnum.FAILED,
                        errors=[str(e)],
                    )
                    break
                except Exception as e:
                    attempt_debug["status"] = (
                        "failed_after_response"
                        if attempt_debug.get("scratchpad") or attempt_debug.get("result")
                        else "failed_before_response"
                    )
                    attempt_debug["error"] = str(e)
                    attempt_debug["reason"] = str(e)
                    response_content = getattr(locals().get("response", None), "content", "")
                    scratchpad_text = locals().get("scratchpad_text", "")
                    result_text = locals().get("result_text", "") or response_content
                    existing_debug_payload = record.get_debug_target_centric_mapping(tgt_lang_code)
                    if str(e) != SEMANTIC_CHECK_UNVERIFIED_MAPPING_FEEDBACK or not existing_debug_payload:
                        record.set_debug_target_centric_mapping(
                            tgt_lang_code,
                            scratchpad=scratchpad_text,
                            result=result_text,
                            error=str(e),
                            attempts=attempts_debug,
                        )
                    exceptions.append(e)
                    if n_retry == self.max_retries:
                        raise_unless_contract_or_validation_error(e, validation_error_types=ValidateExceptions)
                        branch.artifacts.tgt_src_mapping.mappings = []
                        branch.artifacts.tgt_src_mapping.author = ""
                        record.set_debug_target_centric_mapping(
                            tgt_lang_code,
                            scratchpad=scratchpad_text,
                            result=result_text,
                            error=str(e),
                            attempts=attempts_debug,
                        )
                        branch.status.tgt_src_mapping = TaskStatus(
                            status=StatusEnum.FAILED,
                            errors=[f"- Retries: {self.max_retries}\n- Errors: {[str(error) for error in exceptions]}"],
                        )
                    else:
                        await asyncio.sleep(0.5 * (n_retry + 1))

        return record

    def _validate_prerequisites(self, record: PipelineRecord, target_language_code: str) -> list[str]:
        errors: list[str] = []
        transcript = record.source.artifacts.transcript
        alignment = record.source.artifacts.alignment
        source_segmentation = record.source.artifacts.time_pressure_segmentation
        branch = record.target.languages[target_language_code]
        if transcript is None or not transcript.text:
            errors.append("No source transcript available for mapping")
        if alignment is None or not alignment.tokens or not alignment.words:
            errors.append("No source alignment/word groups available for mapping downstream-readiness validation")
        if source_segmentation is None or not source_segmentation.sense_units.groups:
            errors.append("No time pressure segmentation available for mapping")
        if not branch.artifacts.reconstruction.text:
            errors.append("No reconstructed translation available for mapping")
        if not branch.artifacts.pure_text_segmentation.sense_units.groups:
            errors.append("No pure text segmentation available for mapping")
        if (
            branch.artifacts.pure_text_segmentation.sense_units.groups
            and not branch.artifacts.pure_text_segmentation.tokens
        ):
            errors.append("No pure text segmentation tokens available for mapping")
        return errors

    def _build_mapping_prompt(self, record: PipelineRecord, target_language_code: str) -> tuple[str, str]:
        transcript = record.source.artifacts.transcript
        source_text = transcript.text if transcript else ""
        source_language_code = record.metadata.language
        source_language_name = Config.lang_code2name.get(source_language_code, source_language_code)
        target_branch = record.target.languages[target_language_code]
        target_text = target_branch.artifacts.reconstruction.text
        target_language_name = Config.lang_code2name.get(target_language_code, target_language_code)
        source_tokens = self._get_source_token_texts(record)
        target_tokens = list(target_branch.artifacts.pure_text_segmentation.tokens)
        target_units = group_tokens_by_sense_units(
            language=target_language_code,
            tokens=target_tokens,
            sense_unit_groups=target_branch.artifacts.pure_text_segmentation.sense_units.groups,
        )
        source_rendered = "\n".join(f"  {idx}. {text}" for idx, text in source_tokens.items())
        target_rendered = "\n".join(f"  {idx}. {text}" for idx, text in target_units.items())
        user_prompt = (
            self.user_prompt_template
            .replace("{{SOURCE_LANGUAGE_NAME}}", source_language_name)
            .replace("{{SOURCE_TEXT}}", source_text)
            .replace("{{SOURCE_TOKENS}}", source_rendered)
            .replace("{{TARGET_LANGUAGE_NAME}}", target_language_name)
            .replace("{{TARGET_TEXT}}", target_text)
            .replace("{{TARGET_SENSE_UNITS}}", target_rendered)
        )
        return self.system_prompt, user_prompt

    def _get_source_token_texts(self, record: PipelineRecord) -> dict[int, str]:
        alignment = record.source.artifacts.alignment
        if alignment is None or not alignment.tokens:
            return {}
        return {idx: token.word for idx, token in enumerate(alignment.tokens)}

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

    def _parse_mapping_result(self, result_text: str) -> list[Mapping]:
        try:
            payload = json.loads(result_text)
        except Exception as e:
            raise Exception(f"JSON Format Error: {e}") from e
        if not isinstance(payload, list):
            raise Exception("Output Format Error: mapping result must be a JSON array")
        mappings: list[Mapping] = []
        for idx, item in enumerate(payload):
            if not isinstance(item, dict):
                raise Exception(f"Output Format Error: mapping item at index {idx} must be a JSON object")
            if "target_senseunit_id" not in item:
                raise Exception(
                    f"Output Format Error: mapping item at index {idx} is missing required field 'target_senseunit_id'"
                )
            if "source_token_ids" not in item:
                raise Exception(
                    f"Output Format Error: mapping item at index {idx} is missing required field 'source_token_ids'"
                )

            target_senseunit_id = item["target_senseunit_id"]
            source_token_ids = item["source_token_ids"]

            if not isinstance(target_senseunit_id, int):
                raise Exception(
                    f"Output Format Error: mapping item at index {idx} has invalid 'target_senseunit_id': it must be an integer"
                )
            if not isinstance(source_token_ids, list) or not source_token_ids:
                raise Exception(
                    f"Output Format Error: mapping item at index {idx} has invalid 'source_token_ids': it must be a non-empty list of integers"
                )
            if any(not isinstance(source_token_id, int) for source_token_id in source_token_ids):
                raise Exception(
                    f"Output Format Error: mapping item at index {idx} has invalid 'source_token_ids': every item must be an integer"
                )

            mappings.append(
                Mapping(
                    target_senseunit_id=target_senseunit_id,
                    source_token_ids=source_token_ids,
                )
            )
        return mappings

    def _trigger_level2_mapping_diagnostics(
        self,
        mappings: list[Mapping],
    ):
        return collect_level2_mapping_diagnostics(mappings)

    async def _run_level3_semantic_checks(
        self,
        *,
        record: PipelineRecord,
        target_language_code: str,
        mappings: list[Mapping],
        max_tokens: int,
        temperature: float,
        top_p: float,
        extra_body: dict | None,
    ) -> str | None:
        diagnostics = self._trigger_level2_mapping_diagnostics(mappings)
        if not diagnostics:
            return None

        source_language_code = record.metadata.language
        source_language_name = Config.lang_code2name.get(source_language_code, source_language_code)
        target_language_name = Config.lang_code2name.get(target_language_code, target_language_code)
        source_token_texts = self._get_source_token_texts(record)
        target_tokens = list(record.target.languages[target_language_code].artifacts.pure_text_segmentation.tokens)
        target_senseunit_texts = group_tokens_by_sense_units(
            language=target_language_code,
            tokens=target_tokens,
            sense_unit_groups=record.target.languages[target_language_code].artifacts.pure_text_segmentation.sense_units.groups,
        )
        local_regions = build_local_regions_with_inline_triggers(
            mappings=mappings,
            diagnostics=diagnostics,
            target_senseunit_texts=target_senseunit_texts,
            source_token_texts=source_token_texts,
        )
        semantic_errors: list[str] = []
        for local_region in local_regions:
            semantic_exceptions: list[Exception] = []
            for n_retry in range(SEMANTIC_CHECK_MAX_RETRIES + 1):
                semantic_user_prompt = render_level3_semantic_check_input(
                    source_language_name=source_language_name,
                    target_language_name=target_language_name,
                    source_token_texts=source_token_texts,
                    target_senseunit_texts=target_senseunit_texts,
                    current_mapping=local_region,
                )
                semantic_messages = [
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": self.semantic_check_system_prompt}],
                    },
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": semantic_user_prompt}],
                    },
                ]
                if semantic_exceptions:
                    exception_messages = exception_rendering(semantic_exceptions)
                    if exception_messages.strip():
                        semantic_messages = [
                            semantic_messages[0],
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": exception_messages
                                        + f"\nRETRY:{n_retry}/{SEMANTIC_CHECK_MAX_RETRIES}\n\n"
                                        + semantic_user_prompt,
                                    }
                                ],
                            },
                        ]
                try:
                    semantic_response = await self.llm.chat(
                        semantic_messages,
                        max_tokens,
                        temperature,
                        top_p,
                        extra_body,
                    )
                    semantic_error_feedback = extract_semantic_mapping_error_feedback_or_raise(
                        semantic_response.content
                    )
                    if semantic_error_feedback:
                        semantic_errors.append(semantic_error_feedback)
                    break
                except Exception as e:
                    semantic_exceptions.append(e)
                    if n_retry == SEMANTIC_CHECK_MAX_RETRIES:
                        raise_unless_contract_or_validation_error(e, validation_error_types=ValidateExceptions)
                        semantic_response_content = getattr(locals().get("semantic_response", None), "content", "")
                        semantic_scratchpad, semantic_result = extract_semantic_check_raw_blocks(
                            semantic_response_content
                        )
                        record.set_debug_target_centric_mapping(
                            target_language_code,
                            scratchpad=semantic_scratchpad,
                            result=semantic_result or semantic_response_content,
                            error=str(e),
                        )
                        return SEMANTIC_CHECK_UNVERIFIED_MAPPING_FEEDBACK
                    await asyncio.sleep(0.5 * (n_retry + 1))
        if not semantic_errors:
            return None
        return "\n\n".join(semantic_errors)

    def _validate_mapping_result(
        self,
        record: PipelineRecord,
        target_language_code: str,
        mappings: list[Mapping],
    ) -> None:
        branch = record.target.languages[target_language_code]
        target_groups = branch.artifacts.pure_text_segmentation.sense_units.groups
        source_tokens = record.source.artifacts.alignment.tokens
        validate_mapping_result_or_raise(
            mappings=mappings,
            expected_target_ids=list(range(len(target_groups))),
            source_token_count=len(source_tokens),
        )
        validate_mapping_downstream_readiness_or_raise(
            mappings=mappings,
            source_duration=record.metadata.duration,
            source_language_code=record.metadata.language,
            alignment_tokens=record.source.artifacts.alignment.tokens,
            alignment_word_groups=record.source.artifacts.alignment.words,
            source_sense_unit_groups=record.source.artifacts.time_pressure_segmentation.sense_units.groups,
        )
