"""Reconstruction order-risk trigger and promptless semantic-validator shell.

This module intentionally keeps reconstruction semantic-check prompts empty.
The prompt content is an NLP procedure decision and must be supplied explicitly
by the user later. What is implemented here is only:

- project-token based TransAlign/LaBSE alignment adapter,
- cheap target-order blocked-distance trigger,
- local-region rendering for future semantic checks,
- LLM validator infrastructure and output-contract parsing.

Project tokenization is authoritative. TransAlign tokenizer/model internals may
only encode the already-produced project token lists; all ids returned by this
module refer to project-level token indices from ``data_process.utils.tokenize``.
"""

from __future__ import annotations

import asyncio
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping as TypingMapping, Sequence

from configs.config import Config
from core.utils import tokenize
from pipeline.providers.retry_error_rendering import (
    RECONSTRUCTION_REWRITE_LINE_RE,
    render_historical_retry_errors,
    render_historical_validation_error,
)


RECONSTRUCTION_SEMANTIC_CHECK_MAX_RETRIES = 2


SYSTEM_INSTRUCTION_RECONSTRUCTION_SEMANTIC_CHECK = """# ROLE

You are a reconstruction order-risk validator for live simultaneous interpretation.

# TASK

You are given:
- source windows, each containing source tokens in arrival order
- target tokens from the candidate reconstruction
- the raw translation before reconstruction
- the candidate reconstruction
- one ORDER RISK region produced by source-window order analysis

Your task is to validate only the given ORDER RISK region.

Decide whether the marked target order creates avoidable streaming-unfriendly blocking under source-window pressure.

# CORE IDEA

The ORDER RISK region shows target tokens in target reading order.

Each target token line may include aligned source-token evidence and the source window where that source token appears.

Markers:
- blocking span: target-side expression that raises the source-window frontier
- blocking frontier owner: the target token that owns the latest source-window frontier
- blocked span: later target tokens that depend on earlier source windows and may be delayed by the blocking span

The alignment evidence is not gold truth.

The alignment evidence is not gold truth.

`<unaligned>` is allowed.

Do not invent missing alignment.

Do not treat an ORDER RISK trigger as proof of an error.

Alignment evidence may be wrong, especially for pronouns, demonstratives, particles, auxiliaries, and function words.

If the ORDER RISK appears to be caused mainly by unreliable alignment rather than by the candidate reconstruction order, use valid or uncertain.

Do not recommend a rewrite only to satisfy suspicious alignment evidence.

# VALIDATION QUESTION

For the given ORDER RISK region, answer:

Is the marked target order necessary in the target language,
or is it only natural but still safely rewritable into an equally natural local order with lower source-window blocking?

# VERDICTS

Use only these verdicts:

- valid
- rewrite_recommend
- uncertain

## valid

Use valid when the marked source-window order risk is acceptable and no clear equally natural local rewrite with lower source-window blocking is available.

Typical valid cases:
- the target order is necessary in the target language
- the source-window gap is caused by unavoidable target-language word order
- the alignment evidence is too weak to prove a reconstruction problem
- the blocking span is required for target-language fluency
- a rewrite might reduce source-window blocking, but would make the target language less natural, less faithful, or less style-compatible
- the apparent risk is likely caused by weak or incorrect alignment evidence

## rewrite_recommend

Use rewrite_recommend only when all conditions hold:

1. The marked target order creates real head-of-line blocking measured by source-window delay.
2. The blocking is avoidable.
3. A more streaming-friendly target order is available.
4. The rewrite reduces source-window blocking.
5. The rewrite remains equally natural in the target language.
6. The rewrite preserves the meaning of the candidate reconstruction and raw translation.
7. The rewrite is clear enough to provide as a concrete local replacement.
8. The current order is not required for target-language fluency; it is only one possible natural order.

rewrite_recommend means:

the current order may be natural, but it is not necessary; an equally natural, meaning-preserving local rewrite with lower source-window blocking is clearly available.

## uncertain

Use uncertain when:
- the region looks suspicious but may be acceptable
- alignment evidence is insufficient
- the source-window gap may be caused by necessary target-language order
- a better local rewrite is not clear
- changing the order may risk meaning or fluency
- the alignment evidence may be wrong, but the target order risk cannot be confidently dismissed

# OUTPUT FORMAT

Output only one valid JSON array.

Do not output markdown.

Do not output comments.

Do not output explanations outside the JSON array.

Schema:

[
  {
    "target_token_span": [<start>, <end>],
    "verdict": "valid" | "rewrite_recommend" | "uncertain",
    "reason": "<short reason>",
    "suggested_rewrite": "<local rewritten target text>" | null
  },
  {
    ...
  }
]

# OUTPUT CONTRACT

- `target_token_span` uses the displayed target token ids.
- `target_token_span` is a closed inclusive interval: [start, end].
- `verdict` must be one of:
  - valid
  - rewrite_recommend
  - uncertain
- If verdict is valid, `suggested_rewrite` must be null.
- If verdict is uncertain, `suggested_rewrite` must be null.
- If verdict is rewrite_recommend, `suggested_rewrite` must be a non-empty target-language string.
- If no clear local rewrite is available, do not use rewrite_recommend; use uncertain.
- The JSON array may contain one or more items.
- Each item must correspond only to the given ORDER RISK region.

# IMPORTANT

The trigger is only an inspection note.

Do not force an error.

A large source-window gap is not automatically an error.

Do not treat target-language naturalness alone as sufficient for valid.

A rewrite recommendation exists only when the current target order causes avoidable source-window blocking and an equally natural local rewrite with lower blocking is clear.
"""

USER_PROMPT_RECONSTRUCTION_SEMANTIC_CHECK = """# CURRENT TASK

source_language: {{SOURCE_LANGUAGE_NAME}}
target_language: {{TARGET_LANGUAGE_NAME}}

source_windows:
{{SOURCE_WINDOWS}}

target_tokens:
{{TARGET_TOKENS}}

raw_translation:
{{RAW_TRANSLATION}}

candidate_reconstruction:
{{CANDIDATE_RECONSTRUCTION}}

**ORDER RISK**:
{{ORDER_RISK}}

Output:
"""


class ReconstructionValidationError(ValueError):
    """Raised when reconstruction trigger/semantic-check contracts fail."""


@dataclass(frozen=True)
class ReconstructionAlignment:
    """Target-token dependency estimated from project-token alignment."""

    target_token_id: int
    source_token_ids: list[int]


@dataclass(frozen=True)
class ReconstructionOrderRiskDiagnostic:
    """A local order-risk trigger; it is an inspection note, not an error."""

    target_token_id: int
    target_token_text: str
    source_token_ids: list[int]
    ready_window: int
    previous_window_frontier: int
    prefix_window_frontier: int
    blocked_window_gap: int
    blocking_target_token_id: int
    blocking_target_token_text: str
    blocking_ready_window: int
    blocking_source_token_ids: list[int]
    # Spans are closed inclusive intervals: (start_token_id, end_token_id).
    blocking_target_span: tuple[int, int]
    blocked_target_span: tuple[int, int]
    source_position: int = -1
    previous_frontier: int = -1
    prefix_source_frontier: int = -1
    blocked_distance: int = 0
    severity: str = "needs_semantic_check"
    diagnostic: str = "target_order_blocked_window_gap"


def _project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _ensure_transalign_on_path() -> None:
    transalign_root = _project_root() / "transalign"
    if transalign_root.exists() and str(transalign_root) not in sys.path:
        sys.path.insert(0, str(transalign_root))


class TransAlignProjectTokenAligner:
    """Align project-token lists using TransAlign internals.

    The public input/output boundary is always project tokens. The model
    tokenizer inside TransAlign is used only for subword encoding with
    ``is_split_into_words=True`` and is collapsed back to project-token ids.
    """

    def __init__(
        self,
        *,
        model_name: str = "sentence-transformers/LaBSE",
        layer: int | None = None,
        threshold: float | None = None,
        lang1: str | None = None,
        lang2: str | None = None,
        lora_path: str | None = None,
    ):
        _ensure_transalign_on_path()
        try:
            from TransAlign.align import NeurAligner, get_model_defaults
        except Exception as e:  # pragma: no cover - environment dependent
            raise ReconstructionValidationError(
                "TransAlign import failed. Ensure local transalign dependencies are available."
            ) from e

        defaults = get_model_defaults(model_name, use_defaults=True)
        resolved_layer = layer if layer is not None else defaults.get("layer")
        resolved_threshold = threshold if threshold is not None else defaults.get("softmax")
        if resolved_layer is None:
            raise ReconstructionValidationError(f"No TransAlign layer configured for model {model_name!r}")
        if resolved_threshold is None:
            raise ReconstructionValidationError(f"No TransAlign threshold configured for model {model_name!r}")

        self.model_name = model_name
        self.layer = int(resolved_layer)
        self.threshold = float(resolved_threshold)
        self._aligner = NeurAligner(
            model_name=model_name,
            layer=self.layer,
            lang1=lang1,
            lang2=lang2,
            lora_path=lora_path,
            threshold=self.threshold,
        )

    def align(self, source_tokens: Sequence[str], target_tokens: Sequence[str]) -> list[ReconstructionAlignment]:
        """Return target-centric source dependencies in project-token ids."""

        if not source_tokens or not target_tokens:
            return []

        source = [str(token) for token in source_tokens]
        target = [str(token) for token in target_tokens]
        alignments_by_target: dict[int, set[int]] = {}

        tokenizer_source = self._aligner.tokenizer_lang1
        tokenizer_target = self._aligner.tokenizer_lang2

        source_encoded = tokenizer_source(
            [source],
            is_split_into_words=True,
            add_special_tokens=False,
            padding=False,
        )
        target_encoded = tokenizer_target(
            [target],
            is_split_into_words=True,
            add_special_tokens=False,
            padding=False,
        )
        source_bpe_len = len(source_encoded["input_ids"][0])
        target_bpe_len = len(target_encoded["input_ids"][0])
        source_bpe_to_word = source_encoded.word_ids(0)
        target_bpe_to_word = target_encoded.word_ids(0)

        source_hidden = self._aligner.get_hidden_states([source], is_lang1=True)[self.layer][:, 1:-1, :]
        target_hidden = self._aligner.get_hidden_states([target], is_lang1=False)[self.layer][:, 1:-1, :]
        source_matrix = source_hidden[0, :source_bpe_len]
        target_matrix = target_hidden[0, :target_bpe_len]
        alignment_matrix = self._aligner.get_softmax(x=source_matrix, y=target_matrix)

        for source_bpe_id in range(alignment_matrix.shape[0]):
            source_token_id = source_bpe_to_word[source_bpe_id]
            if source_token_id is None:
                continue
            for target_bpe_id in range(alignment_matrix.shape[1]):
                if alignment_matrix[source_bpe_id, target_bpe_id] <= 0:
                    continue
                target_token_id = target_bpe_to_word[target_bpe_id]
                if target_token_id is None:
                    continue
                alignments_by_target.setdefault(int(target_token_id), set()).add(int(source_token_id))

        return [
            ReconstructionAlignment(target_token_id=target_id, source_token_ids=sorted(source_ids))
            for target_id, source_ids in sorted(alignments_by_target.items())
        ]


def source_dependencies_by_target(
    alignments: Sequence[ReconstructionAlignment],
) -> dict[int, list[int]]:
    deps: dict[int, set[int]] = {}
    for alignment in alignments:
        if alignment.target_token_id < 0:
            continue
        deps.setdefault(alignment.target_token_id, set()).update(
            source_id for source_id in alignment.source_token_ids if source_id >= 0
        )
    return {target_id: sorted(source_ids) for target_id, source_ids in sorted(deps.items()) if source_ids}


def _normalize_trigger_source_token(token: str) -> str:
    return str(token).strip().lower()


def is_trigger_eligible_source_token(token: str, source_language_code: str | None) -> bool:
    """Return whether a source token may be sole blocking evidence for an order-risk trigger."""

    normalized = _normalize_trigger_source_token(token)
    if not normalized:
        return False
    high_noise_tokens = Config.reconstruction_validator_trigger_high_noise_tokens.get(
        source_language_code or "",
        set(),
    )
    return normalized not in {_normalize_trigger_source_token(item) for item in high_noise_tokens}


def has_trigger_eligible_blocking_evidence(
    source_token_ids: Sequence[int],
    source_tokens: Sequence[str],
    source_language_code: str | None,
) -> bool:
    """Check only blocking/frontier-owner source evidence for trigger eligibility."""

    return any(
        0 <= source_id < len(source_tokens)
        and is_trigger_eligible_source_token(source_tokens[source_id], source_language_code)
        for source_id in source_token_ids
    )


def collect_reconstruction_order_risk_diagnostics(
    *,
    source_tokens: Sequence[str],
    source_language_code: str | None = None,
    source_window_by_token: TypingMapping[int, int] | None = None,
    target_tokens: Sequence[str],
    alignments: Sequence[ReconstructionAlignment],
    blocked_window_gap_threshold: int = 3,
) -> list[ReconstructionOrderRiskDiagnostic]:
    """Collect source-window-gap based order-risk triggers.

    ``blocked_window_gap`` is measured in source windows, not source-token index
    distance. Token distance is retained only as debug context.
    """

    if blocked_window_gap_threshold < 0:
        raise ReconstructionValidationError("blocked_window_gap_threshold must be non-negative")

    deps = source_dependencies_by_target(alignments)
    if source_window_by_token is None:
        source_window_by_token = {idx: idx for idx in range(len(source_tokens))}
    diagnostics: list[ReconstructionOrderRiskDiagnostic] = []
    prefix_window_frontier = -1
    prefix_source_frontier = -1  # debug only
    frontier_owner_target_token_id = -1
    frontier_owner_source_token_ids: list[int] = []
    frontier_owner_ready_window = -1

    def _source_ids_for_target_span(start: int, end: int) -> list[int]:
        source_ids: set[int] = set()
        if start < 0 or end < start:
            return []
        for span_target_id in range(max(0, start), min(len(target_tokens) - 1, end) + 1):
            source_ids.update(deps.get(span_target_id, []))
        return sorted(source_id for source_id in source_ids if source_id < len(source_tokens))

    def _expanded_blocking_span(owner_target_id: int) -> tuple[int, int]:
        if owner_target_id < 0:
            return (-1, -1)
        start = owner_target_id
        owner_source_ids = deps.get(owner_target_id, [])
        current_min = min(
            source_window_by_token.get(source_id, -1) for source_id in owner_source_ids
        ) if owner_source_ids else prefix_window_frontier
        probe = owner_target_id - 1
        while probe >= 0:
            probe_source_ids = deps.get(probe, [])
            if not probe_source_ids:
                start = probe
                probe -= 1
                continue
            probe_window = max(source_window_by_token.get(source_id, -1) for source_id in probe_source_ids)
            if probe_window == current_min - 1:
                start = probe
                current_min = min(source_window_by_token.get(source_id, -1) for source_id in probe_source_ids)
                probe -= 1
                continue
            break
        return (start, owner_target_id)

    for target_token_id, target_token_text in enumerate(target_tokens):
        source_token_ids = [source_id for source_id in deps.get(target_token_id, []) if source_id < len(source_tokens)]
        if not source_token_ids:
            continue
        source_position = max(source_token_ids)
        ready_window = max(source_window_by_token.get(source_id, -1) for source_id in source_token_ids)
        previous_window_frontier = prefix_window_frontier
        blocked_window_gap = previous_window_frontier - ready_window
        previous_frontier = prefix_source_frontier  # debug only
        blocked_distance = previous_frontier - source_position
        if blocked_window_gap >= blocked_window_gap_threshold:
            blocking_target_token_text = ""
            if 0 <= frontier_owner_target_token_id < len(target_tokens):
                blocking_target_token_text = str(target_tokens[frontier_owner_target_token_id])
            blocking_target_span = _expanded_blocking_span(frontier_owner_target_token_id)
            blocking_source_token_ids = _source_ids_for_target_span(*blocking_target_span)
            blocking_source_token_ids = blocking_source_token_ids or list(frontier_owner_source_token_ids)
            if not has_trigger_eligible_blocking_evidence(
                blocking_source_token_ids,
                source_tokens,
                source_language_code,
            ):
                continue
            diagnostics.append(
                ReconstructionOrderRiskDiagnostic(
                    target_token_id=target_token_id,
                    target_token_text=str(target_token_text),
                    source_token_ids=source_token_ids,
                    ready_window=ready_window,
                    previous_window_frontier=previous_window_frontier,
                    prefix_window_frontier=prefix_window_frontier,
                    blocked_window_gap=blocked_window_gap,
                    source_position=source_position,
                    previous_frontier=previous_frontier,
                    prefix_source_frontier=prefix_source_frontier,
                    blocked_distance=blocked_distance,
                    blocking_target_token_id=frontier_owner_target_token_id,
                    blocking_target_token_text=blocking_target_token_text,
                    blocking_ready_window=frontier_owner_ready_window,
                    blocking_source_token_ids=blocking_source_token_ids,
                    blocking_target_span=blocking_target_span,
                    blocked_target_span=(target_token_id, target_token_id),
                )
            )

        if ready_window > prefix_window_frontier:
            prefix_window_frontier = ready_window
            prefix_source_frontier = source_position
            frontier_owner_target_token_id = target_token_id
            frontier_owner_source_token_ids = list(source_token_ids)
            frontier_owner_ready_window = ready_window

    return diagnostics


def _format_indexed_tokens(tokens: Sequence[str]) -> str:
    return "\n".join(f"  {idx}. {token}" for idx, token in enumerate(tokens))


def _format_inline_indexed_tokens(tokens: Sequence[str]) -> str:
    return "{" + ",".join(f"{idx}:{token}" for idx, token in enumerate(tokens)) + "}"


def _format_source_windows(
    source_tokens: Sequence[str],
    source_window_by_token: TypingMapping[int, int],
) -> str:
    windows: dict[int, list[str]] = {}
    for source_id, token in enumerate(source_tokens):
        window_id = source_window_by_token.get(source_id, -1)
        windows.setdefault(window_id, []).append(f'{source_id}: "{token}"')
    return "\n".join(
        f"* W{window_id}. " + "{" + ", ".join(items) + "}"
        for window_id, items in sorted(windows.items())
    )


def _format_source_tokens(source_token_ids: Sequence[int], source_tokens: Sequence[str]) -> str:
    return ", ".join(
        f'{source_id}: "{source_tokens[source_id]}"'
        for source_id in source_token_ids
        if 0 <= source_id < len(source_tokens)
    )


def _format_target_alignment(
    source_token_ids: Sequence[int],
    source_tokens: Sequence[str],
    source_window_by_token: TypingMapping[int, int] | None = None,
) -> str:
    if source_window_by_token is None:
        formatted = _format_source_tokens(source_token_ids, source_tokens)
    else:
        formatted = ", ".join(
            f'W{source_window_by_token.get(source_id, -1)} {source_id}: "{source_tokens[source_id]}"'
            for source_id in source_token_ids
            if 0 <= source_id < len(source_tokens)
        )
    if not formatted:
        return "`<unaligned>`"
    return f"`{formatted}`"


def _expand_blocking_display_token_ids(
    *,
    owner_target_id: int,
    blocked_source_token_ids: Sequence[int],
    source_ids_by_target: TypingMapping[int, Sequence[int]],
) -> set[int]:
    if owner_target_id < 0:
        return set()
    if not blocked_source_token_ids:
        return {owner_target_id}
    blocked_frontier = max(blocked_source_token_ids)
    token_ids = {owner_target_id}
    probe = owner_target_id - 1
    while probe >= 0:
        probe_source_ids = source_ids_by_target.get(probe, [])
        if not probe_source_ids:
            token_ids.add(probe)
            probe -= 1
            continue
        if max(probe_source_ids) <= blocked_frontier:
            break
        token_ids.add(probe)
        probe -= 1
    return token_ids


def _expand_blocking_display_token_ids_by_window(
    *,
    owner_target_id: int,
    blocked_source_token_ids: Sequence[int],
    source_ids_by_target: TypingMapping[int, Sequence[int]],
    source_window_by_token: TypingMapping[int, int],
) -> set[int]:
    if owner_target_id < 0:
        return set()
    if not blocked_source_token_ids:
        return {owner_target_id}
    blocked_window = max(source_window_by_token.get(source_id, -1) for source_id in blocked_source_token_ids)
    token_ids = {owner_target_id}
    probe = owner_target_id - 1
    while probe >= 0:
        probe_source_ids = source_ids_by_target.get(probe, [])
        if not probe_source_ids:
            token_ids.add(probe)
            probe -= 1
            continue
        if max(source_window_by_token.get(source_id, -1) for source_id in probe_source_ids) <= blocked_window:
            break
        token_ids.add(probe)
        probe -= 1
    return token_ids


def build_reconstruction_local_regions_with_inline_triggers(
    *,
    diagnostics: Sequence[ReconstructionOrderRiskDiagnostic],
    source_tokens: Sequence[str],
    source_window_by_token: TypingMapping[int, int] | None = None,
    target_tokens: Sequence[str],
    alignments: Sequence[ReconstructionAlignment],
) -> list[str]:
    """Render suspicious local target-token windows for future semantic checks."""

    source_ids_by_target = source_dependencies_by_target(alignments)
    if source_window_by_token is None:
        source_window_by_token = {idx: idx for idx in range(len(source_tokens))}
    blocked_token_ids = {diagnostic.target_token_id for diagnostic in diagnostics}
    blocking_token_ids: set[int] = set()
    frontier_owner_token_ids: set[int] = set()

    for diagnostic in diagnostics:
        frontier_owner_token_ids.add(diagnostic.blocking_target_token_id)
        blocking_token_ids.update(
            _expand_blocking_display_token_ids_by_window(
                owner_target_id=diagnostic.blocking_target_token_id,
                blocked_source_token_ids=diagnostic.source_token_ids,
                source_ids_by_target=source_ids_by_target,
                source_window_by_token=source_window_by_token,
            )
        )

    frontier_owner_token_ids = {idx for idx in frontier_owner_token_ids if idx >= 0}

    def _marker(idx: int) -> str:
        markers: list[str] = []
        if idx in blocking_token_ids:
            markers.append("blocking")
        if idx in frontier_owner_token_ids:
            markers.append("blocking frontier owner")
        if idx in blocked_token_ids:
            markers.append("blocked")
        return ", ".join(markers)

    target_lines: list[str] = []
    for idx, target_token in enumerate(target_tokens):
        alignment = _format_target_alignment(source_ids_by_target.get(idx, []), source_tokens, source_window_by_token)
        marker = _marker(idx)
        if marker:
            target_lines.append(f"{idx}. {target_token} <-- {marker}, {alignment}")
        else:
            target_lines.append(f"{idx}. {target_token} <- {alignment}")

    return [
        "\n".join(
            [
                "",
                "source_windows:",
                _format_source_windows(source_tokens, source_window_by_token),
                "",
                "target_tokens:",
                *target_lines,
                "",
                "risk:",
                "A late-source-window-dependent target expression appears before target tokens whose source evidence arrives in earlier source windows.",
                "",
                "question:",
                "Is this target order necessary in the target language, or can an equally natural local rewrite reduce source-window blocking?",
            ]
        )
    ]


def render_reconstruction_semantic_check_input(
    *,
    user_prompt_template: str,
    source_language_name: str,
    target_language_name: str,
    source_windows: str,
    target_tokens: Sequence[str],
    raw_translation: str,
    candidate_reconstruction: str,
    order_risk: str,
) -> str:
    """Render prompt input only when a user-supplied template exists."""

    if not user_prompt_template.strip():
        return ""
    return (
        user_prompt_template.replace("{{SOURCE_LANGUAGE_NAME}}", source_language_name)
        .replace("{{TARGET_LANGUAGE_NAME}}", target_language_name)
        .replace("{{SOURCE_WINDOWS}}", source_windows)
        .replace("{{TARGET_TOKENS}}", _format_indexed_tokens(target_tokens))
        .replace("{{RAW_TRANSLATION}}", raw_translation)
        .replace("{{CANDIDATE_RECONSTRUCTION}}", candidate_reconstruction)
        .replace("{{ORDER_RISK}}", order_risk)
    )


def extract_reconstruction_check_raw_blocks(response_text: str) -> tuple[str, str]:
    lowered = response_text.lower()

    def _extract_block(tag_name: str) -> str:
        open_tag = f"<{tag_name}>"
        close_tag = f"</{tag_name}>"
        start = lowered.find(open_tag)
        if start < 0:
            return ""
        end = lowered.find(close_tag, start + len(open_tag))
        if end < 0:
            return response_text[start + len(open_tag) :].strip()
        return response_text[start + len(open_tag) : end].strip()

    scratchpad = _extract_block("scratchpad")
    result = _extract_block("result")
    return scratchpad, result


def _strip_json_fence(text: str) -> str:
    stripped = text.strip()
    if not stripped.startswith("```"):
        return stripped
    lines = stripped.splitlines()
    if not lines or not lines[0].strip().startswith("```"):
        return stripped
    if lines[-1].strip() != "```":
        return stripped
    return "\n".join(lines[1:-1]).strip()


def _parse_reconstruction_check_result_json_or_raise(result_text: str) -> list[dict[str, Any]]:
    decoder = json.JSONDecoder()
    text = _strip_json_fence(result_text)
    try:
        payload, end_index = decoder.raw_decode(text)
    except Exception as e:
        raise ReconstructionValidationError(
            "JSON Format Error: reconstruction semantic checker output must be a valid JSON array; "
            f"failed to parse JSON: {e}"
        ) from e
    trailing = text[end_index:].strip()
    if trailing:
        raise ReconstructionValidationError(
            "JSON Format Error: reconstruction semantic checker output must contain exactly one JSON array; "
            "found extra non-whitespace content after the first JSON value. "
            "If there are multiple judgments, put them inside one array like [{...}, {...}], not as separate arrays."
        )
    if not isinstance(payload, list):
        raise ReconstructionValidationError(
            "Output Format Error: reconstruction semantic checker output must be a JSON array of item objects"
        )
    if not all(isinstance(item, dict) for item in payload):
        raise ReconstructionValidationError(
            "Output Format Error: every reconstruction checker array item must be a JSON object"
        )
    return payload


def _validate_suggested_rewrite_or_raise(*, item_index: int, verdict: str, suggested_rewrite: object) -> None:
    if verdict in {"valid", "uncertain"}:
        if suggested_rewrite is not None:
            raise ReconstructionValidationError(
                f"Contract Error: reconstruction checker item {item_index} with verdict {verdict!r} must use suggested_rewrite = null"
            )
        return
    if verdict != "rewrite_recommend":
        raise ReconstructionValidationError(
            f"Output Format Error: reconstruction checker item {item_index} has invalid verdict {verdict!r}"
        )
    if not isinstance(suggested_rewrite, str) or not suggested_rewrite.strip():
        raise ReconstructionValidationError(
            f"Contract Error: reconstruction checker item {item_index} with verdict 'rewrite_recommend' must provide non-empty suggested_rewrite"
        )


def validate_reconstruction_check_result_or_raise(result_text: str) -> list[dict[str, Any]]:
    items = _parse_reconstruction_check_result_json_or_raise(result_text)
    allowed = {"valid", "rewrite_recommend", "uncertain"}

    for item_index, item in enumerate(items):
        for field_name in ("target_token_span", "verdict", "reason", "suggested_rewrite"):
            if field_name not in item:
                raise ReconstructionValidationError(
                    f"Output Format Error: reconstruction checker item {item_index} missing required field {field_name!r}"
                )
        span = item["target_token_span"]
        if (
            not isinstance(span, list)
            or len(span) != 2
            or any(not isinstance(value, int) for value in span)
            or span[0] < 0
            or span[1] < span[0]
        ):
            raise ReconstructionValidationError(
                f"Output Format Error: reconstruction checker item {item_index} target_token_span must be [start:int, end:int]"
            )
        verdict = item["verdict"]
        if verdict not in allowed:
            raise ReconstructionValidationError(
                f"Output Format Error: reconstruction checker item {item_index} has invalid verdict {verdict!r}"
            )
        if not isinstance(item["reason"], str):
            raise ReconstructionValidationError(
                f"Output Format Error: reconstruction checker item {item_index} reason must be a string"
            )
        _validate_suggested_rewrite_or_raise(
            item_index=item_index,
            verdict=verdict,
            suggested_rewrite=item["suggested_rewrite"],
        )
    return items


def extract_rewrite_recommend_items_or_raise(result_text: str) -> list[dict[str, Any]]:
    items = validate_reconstruction_check_result_or_raise(result_text)
    return [item for item in items if item["verdict"] == "rewrite_recommend"]


def _join_target_tokens_for_feedback(tokens: Sequence[str], target_language_code: str | None) -> str:
    if target_language_code in {"ZH", "JA"}:
        return "".join(str(token) for token in tokens)
    return " ".join(str(token) for token in tokens)


def _target_token_span_text(
    *,
    span: Sequence[int],
    target_tokens: Sequence[str],
    target_language_code: str | None,
) -> str:
    start, end = span
    if start < 0 or end < start or start >= len(target_tokens):
        return ""
    bounded_end = min(end, len(target_tokens) - 1)
    return _join_target_tokens_for_feedback(
        target_tokens[start : bounded_end + 1],
        target_language_code,
    )


def render_rewrite_recommend_items(
    items: Sequence[TypingMapping[str, object]],
    *,
    target_tokens: Sequence[str],
    target_language_code: str | None = None,
) -> str:
    rendered: list[str] = []
    for item in items:
        span = item.get("target_token_span")
        target_text = ""
        if isinstance(span, list) and len(span) == 2 and all(isinstance(value, int) for value in span):
            target_text = _target_token_span_text(
                span=span,
                target_tokens=target_tokens,
                target_language_code=target_language_code,
            )
        rendered.append(
            "\n".join(
                [
                    f"* target_text: {target_text!r}",
                    "  - verdict: rewrite_recommend",
                    f"  - reason: {item.get('reason', '')!r}",
                    f"  - suggested_rewrite: {item.get('suggested_rewrite', '')!r}",
                ]
            )
        )
    return "\n\n".join(rendered)


def _extract_reconstruction_check_result_text(response_text: str) -> str:
    _, result = extract_reconstruction_check_raw_blocks(response_text)
    return result if result else response_text.strip()


def extract_rewrite_recommend_feedback_or_raise(
    response_text: str,
    *,
    target_tokens: Sequence[str],
    target_language_code: str | None = None,
) -> str | None:
    result_text = _extract_reconstruction_check_result_text(response_text)
    items = extract_rewrite_recommend_items_or_raise(result_text)
    if not items:
        return None
    return render_rewrite_recommend_items(
        items,
        target_tokens=target_tokens,
        target_language_code=target_language_code,
    )


def _exception_rendering(exceptions: Sequence[Exception]) -> str:
    if not exceptions:
        return ""
    messages = render_historical_retry_errors(
        list(exceptions),
        validation_error_types=(ReconstructionValidationError,),
        validation_renderer=lambda exc: render_historical_validation_error(
            exc,
            patterns=[RECONSTRUCTION_REWRITE_LINE_RE],
        ),
    )
    last = exceptions[-1]
    if "JSON Format Error:" in str(last):
        messages += f"{len(exceptions)}. **JSON Format Error**:\n{last}\n"
        messages += (
            "Required output: exactly one valid JSON array, for example [{...}, {...}], "
            "with no markdown, no comments, and no second JSON array.\n"
        )
    elif "Output Format Error" in str(last) or "Contract Error" in str(last):
        messages += f"{len(exceptions)}. **Output Contract Error**:\n{last}\n"
        messages += (
            "Required output: every item must follow the schema. "
            "Use suggested_rewrite = null for valid/uncertain. "
            "For rewrite_recommend, suggested_rewrite must be a non-empty target-language string; "
            "if no clear rewrite is available, use uncertain.\n"
        )
    else:
        messages += f"{len(exceptions)}. Current error:\n{last}\n"
    return messages


def _render_semantic_validator_failed_feedback(exceptions: Sequence[Exception]) -> str:
    last_error = str(exceptions[-1]) if exceptions else "unknown validator failure"
    return "\n".join(
        [
            "* validator_contract_error:",
            "  - verdict: semantic_validator_failed",
            "  - reason: reconstruction semantic validator did not return one valid contract-compliant JSON array after retries",
            f"  - last_error: {last_error!r}",
            "  - required_fix: validator must retry with exactly one JSON array; do not output multiple arrays, malformed JSON, or rewrite_recommend without a non-empty suggested_rewrite",
        ]
    )


class ReconstructionValidator:
    """Owns reconstruction trigger and optional semantic LLM validation."""

    def __init__(
        self,
        *,
        llm: Any | None = None,
        aligner: TransAlignProjectTokenAligner | None = None,
        semantic_check_system_prompt: str = SYSTEM_INSTRUCTION_RECONSTRUCTION_SEMANTIC_CHECK,
        semantic_check_user_prompt_template: str = USER_PROMPT_RECONSTRUCTION_SEMANTIC_CHECK,
        blocked_window_gap_threshold: int = 3,
        max_retries: int = RECONSTRUCTION_SEMANTIC_CHECK_MAX_RETRIES,
    ):
        self.llm = llm
        self.aligner = aligner
        self.semantic_check_system_prompt = semantic_check_system_prompt
        self.semantic_check_user_prompt_template = semantic_check_user_prompt_template
        self.blocked_window_gap_threshold = blocked_window_gap_threshold
        self.max_retries = max_retries
        self.last_debug: dict[str, str] = {}

    def collect_trigger_diagnostics(
        self,
        *,
        source_language_code: str,
        target_language_code: str,
        source_text: str,
        candidate_reconstruction: str,
        source_tokens: Sequence[str] | None = None,
        source_window_by_token: TypingMapping[int, int] | None = None,
    ) -> tuple[list[str], dict[int, int], list[str], list[ReconstructionAlignment], list[ReconstructionOrderRiskDiagnostic]]:
        source_tokens = list(source_tokens) if source_tokens is not None else tokenize(
            language=source_language_code,
            raw_text=source_text,
            indexing=False,
        )
        source_window_by_token = dict(source_window_by_token or {idx: idx for idx in range(len(source_tokens))})
        target_tokens = tokenize(language=target_language_code, raw_text=candidate_reconstruction, indexing=False)
        if self.aligner is None:
            self.aligner = TransAlignProjectTokenAligner()
        alignments = self.aligner.align(source_tokens=source_tokens, target_tokens=target_tokens)
        diagnostics = collect_reconstruction_order_risk_diagnostics(
            source_tokens=source_tokens,
            source_language_code=source_language_code,
            source_window_by_token=source_window_by_token,
            target_tokens=target_tokens,
            alignments=alignments,
            blocked_window_gap_threshold=self.blocked_window_gap_threshold,
        )
        return source_tokens, source_window_by_token, target_tokens, alignments, diagnostics

    async def validate_or_get_feedback(
        self,
        *,
        source_language_code: str,
        target_language_code: str,
        source_text: str,
        raw_translation: str,
        candidate_reconstruction: str,
        source_tokens: Sequence[str] | None = None,
        source_window_by_token: TypingMapping[int, int] | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.3,
        top_p: float = 0.95,
        top_k: int = 40,
        enable_thinking: bool = False,
    ) -> str | None:
        self.last_debug = {}
        source_tokens, source_window_by_token, target_tokens, alignments, diagnostics = self.collect_trigger_diagnostics(
            source_language_code=source_language_code,
            target_language_code=target_language_code,
            source_text=source_text,
            candidate_reconstruction=candidate_reconstruction,
            source_tokens=source_tokens,
            source_window_by_token=source_window_by_token,
        )
        source_windows = _format_source_windows(source_tokens, source_window_by_token)
        self.last_debug = {
            "source_tokens": _format_indexed_tokens(source_tokens),
            "source_tokens_inline": _format_inline_indexed_tokens(source_tokens),
            "source_windows": source_windows,
            "target_tokens": _format_indexed_tokens(target_tokens),
            "diagnostics_count": str(len(diagnostics)),
        }
        if not diagnostics:
            self.last_debug["result"] = "No reconstruction order-risk diagnostics triggered."
            return None

        if (
            self.llm is None
            or not self.semantic_check_system_prompt.strip()
            or not self.semantic_check_user_prompt_template.strip()
        ):
            self.last_debug["result"] = "Semantic check skipped: missing LLM or semantic-check prompt."
            return None

        source_language_name = Config.lang_code2name.get(source_language_code, source_language_code)
        target_language_name = Config.lang_code2name.get(target_language_code, target_language_code)
        local_regions = build_reconstruction_local_regions_with_inline_triggers(
            diagnostics=diagnostics,
            source_tokens=source_tokens,
            source_window_by_token=source_window_by_token,
            target_tokens=target_tokens,
            alignments=alignments,
        )
        self.last_debug["regions"] = "\n\n".join(local_regions)

        semantic_errors: list[str] = []
        order_risk_blocks: list[str] = []
        validator_result_blocks: list[str] = []
        feedback_blocks: list[str] = []
        for order_risk in local_regions:
            semantic_exceptions: list[Exception] = []
            order_risk_blocks.append(order_risk.strip())
            base_user_prompt = render_reconstruction_semantic_check_input(
                user_prompt_template=self.semantic_check_user_prompt_template,
                source_language_name=source_language_name,
                target_language_name=target_language_name,
                source_windows=source_windows,
                target_tokens=target_tokens,
                raw_translation=raw_translation,
                candidate_reconstruction=candidate_reconstruction,
                order_risk=order_risk,
            )
            if not base_user_prompt:
                self.last_debug["result"] = "Semantic check skipped: rendered user prompt is empty."
                return None
            for n_retry in range(self.max_retries + 1):
                user_prompt = base_user_prompt
                if semantic_exceptions:
                    user_prompt = (
                        _exception_rendering(semantic_exceptions)
                        + f"\nRETRY:{n_retry}/{self.max_retries}\n\n"
                        + base_user_prompt
                    )
                messages = [
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": self.semantic_check_system_prompt}],
                    },
                    {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
                ]
                try:
                    response = await self.llm.chat(
                        messages,
                        max_tokens,
                        temperature,
                        top_p,
                        top_k,
                        enable_thinking,
                    )
                    semantic_scratchpad, semantic_result = extract_reconstruction_check_raw_blocks(response.content)
                    raw_validator_output = semantic_result or response.content
                    if semantic_scratchpad:
                        raw_validator_output = "\n".join(
                            [
                                "model scratchpad:",
                                semantic_scratchpad,
                                "",
                                raw_validator_output,
                            ]
                        )
                    validator_result_blocks.append(raw_validator_output)
                    feedback = extract_rewrite_recommend_feedback_or_raise(
                        response.content,
                        target_tokens=target_tokens,
                        target_language_code=target_language_code,
                    )
                    if feedback:
                        semantic_errors.append(feedback)
                        feedback_blocks.append(feedback)
                    break
                except Exception as e:
                    semantic_exceptions.append(e)
                    if n_retry == self.max_retries:
                        failed_feedback = _render_semantic_validator_failed_feedback(semantic_exceptions)
                        semantic_errors.append(failed_feedback)
                        feedback_blocks.append(failed_feedback)
                        self.last_debug["order_risk"] = "\n\n".join(order_risk_blocks)
                        self.last_debug["validator_result"] = "\n\n".join(
                            validator_result_blocks + [f"Semantic checker failed: {e}"]
                        )
                        self.last_debug["feedback"] = "\n\n".join(feedback_blocks)
                        self.last_debug["result"] = self.last_debug["validator_result"]
                        return failed_feedback
                    await asyncio.sleep(0.5 * (n_retry + 1))

        self.last_debug["order_risk"] = "\n\n".join(order_risk_blocks)
        self.last_debug["validator_result"] = "\n\n".join(validator_result_blocks)
        self.last_debug["feedback"] = "\n\n".join(feedback_blocks)
        if not semantic_errors:
            self.last_debug["result"] = self.last_debug["validator_result"] or "Semantic checker returned no rewrite_recommend feedback."
            return None
        feedback_text = "\n\n".join(semantic_errors)
        self.last_debug["result"] = self.last_debug["validator_result"]
        return feedback_text
