"""Shared retry-error rendering helpers for provider reflection loops.

This module only controls how previous failures are summarized before they are
prepended to a retry prompt. It does not change prompts, validators, NLP
procedure, persisted schema, or human-facing visualization output.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Pattern


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
    - historical non-validator errors: keep existing ``str(error)[-200:]``.
    """

    rendered: list[str] = []
    for i, error in enumerate(exceptions[: len(exceptions) - 1], start=1):
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
