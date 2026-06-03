"""Shared retry-error rendering helpers for provider reflection loops.

This module only controls how previous failures are summarized before they are
prepended to a retry prompt. It does not change prompts, validators, NLP
procedure, persisted schema, or human-facing visualization output.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Pattern

from llm.llm_model import LLMResponseError


SYSTEM_OR_PROVIDER_ERROR_MARKERS = (
    "OpenAI-compatible provider",
    "system-level provider/API boundary error",
    "provider/API boundary error",
    "Connection error",
    "ConnectionError",
    "timeout",
    "timed out",
    "rate limit",
    "status_code=",
    "response_status_code=",
)


SYSTEM_OR_PROVIDER_ERROR_TYPES = {
    "LLMResponseError",
    "APIConnectionError",
    "APITimeoutError",
    "APIStatusError",
    "RateLimitError",
    "InternalServerError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "UnprocessableEntityError",
}


CONTRACT_OR_VALIDATION_ERROR_MARKERS = (
    "JSON Format Error",
    "Output Format Error",
    "Contract Error",
    "semantic_validator_failed",
    "validator_contract_error",
    "ORDER_RISK",
    "Validation failed",
    "validation failed",
    "Validation Error",
    "ValidationError",
)


def is_system_or_provider_error(error: Exception | str | None) -> bool:
    """Return whether an error belongs to runtime/provider/API boundary handling.

    System/provider errors must not be reflected to an LLM and must not be
    persisted as record-level cache validation failures. They are run-level
    failures, not model-output contract failures.
    """

    if error is None:
        return False
    if isinstance(error, LLMResponseError):
        return True
    if isinstance(error, Exception):
        error_type = error.__class__.__name__
        if error_type in SYSTEM_OR_PROVIDER_ERROR_TYPES:
            return True
        text = str(error)
    else:
        text = str(error)
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in SYSTEM_OR_PROVIDER_ERROR_MARKERS)


def is_contract_or_validation_error(
    error: Exception | str | None,
    *,
    validation_error_types: tuple[type[Exception], ...] = (),
) -> bool:
    """Return whether an error is an LLM-output contract/validation failure."""

    if error is None or is_system_or_provider_error(error):
        return False
    if isinstance(error, validation_error_types):
        return True
    text = str(error)
    return any(marker in text for marker in CONTRACT_OR_VALIDATION_ERROR_MARKERS)


def raise_if_system_or_provider_error(error: Exception) -> None:
    """Re-raise system/provider errors before they enter retry/cache state."""

    if is_system_or_provider_error(error):
        raise error


def raise_unless_contract_or_validation_error(
    error: Exception,
    *,
    validation_error_types: tuple[type[Exception], ...] = (),
) -> None:
    """Re-raise any non-reflectable error before retry/cache handling.

    Cache, reflection, and visualization are allowed to carry only model-output
    contract failures and explicit validator failures. Other exceptions are
    run-level failures and must remain outside ``PipelineRecord.status.errors``.
    """

    if not is_contract_or_validation_error(
        error,
        validation_error_types=validation_error_types,
    ):
        raise error


def matching_lines(text: str, patterns: list[Pattern[str]]) -> list[str]:
    """Return lines matching any issue pattern, preserving original order."""

    lines: list[str] = []
    for line in str(text).splitlines():
        if any(pattern.search(line) for pattern in patterns):
            lines.append(line)
    return lines


def render_historical_validation_error(
    error: Exception,
    *,
    patterns: list[Pattern[str]],
) -> str:
    """Render only issue-bearing lines from a historical validator error.

    If the validator error has no recognizable issue-bearing line, fall back to
    the existing historical-error policy: the tail of ``str(error)``. This keeps
    historical non-current context bounded and avoids sending full old validator
    traces back to the LLM.
    """

    text = str(error)
    issue_lines = matching_lines(text, patterns)
    if issue_lines:
        return "\n".join(issue_lines)
    return text[-200:]


def render_historical_retry_errors(
    exceptions: list[Exception],
    *,
    validation_error_types: tuple[type[Exception], ...],
    validation_renderer: Callable[[Exception], str],
) -> str:
    """Render all historical retry errors, excluding the latest/current error.

    Rule:
    - historical validator errors: stage-specific issue lines/regions only;
    - historical contract/output errors: keep bounded ``str(error)[-200:]``;
    - system/provider errors: never render into reflection text.
    """

    rendered: list[str] = []
    for i, error in enumerate(exceptions[: len(exceptions) - 1], start=1):
        if not is_contract_or_validation_error(
            error,
            validation_error_types=validation_error_types,
        ):
            continue
        if isinstance(error, validation_error_types):
            rendered_error = validation_renderer(error)
        else:
            rendered_error = str(error)[-200:]
        rendered.append(f"{i}. {rendered_error}\n")
    return "".join(rendered)


ASR_VALIDATION_ISSUE_WINDOW_RE = re.compile(r"^\* W\d+\..*\bISSUE\d+:.*$")
PURE_TEXT_OVERSIZED_LINE_RE = re.compile(r"^\d+\..*<- oversized chunk .*$")
STRUCTURED_VALIDATION_BULLET_RE = re.compile(
    r"^- (?:expected|produced|missing|unexpected|empty|non-string)\b.*$"
)
MAPPING_LOCAL_REGION_LINE_RE = re.compile(
    r"^(?:\* target\[\d+\].*|\s+- (?:source_tokens|triggers|type|description|suspicious_items):.*)$"
)
RECONSTRUCTION_REWRITE_LINE_RE = re.compile(
    r"^(?:\* target_text:.*|\s+- (?:verdict|reason|suggested_rewrite):.*)$"
)
