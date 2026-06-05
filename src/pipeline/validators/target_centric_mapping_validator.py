from dataclasses import dataclass
import json
from typing import Mapping as TypingMapping, Sequence

from core.schema import Mapping, Word
from core.utils import apply_mapping_groups, build_transcription_chunks


SEMANTIC_CHECK_MAX_RETRIES = 2


SYSTEM_INSTRUCTION_MAPPING_SEMANTIC_CHECK = """# ROLE

You are a semantic checker for target-sense-unit to source-token mapping.

# TASK

You are given:
- source tokens
- target sense units
- one suspicious local mapping region

Your task is to check whether the listed source tokens are directly needed to produce each target sense unit in the given local mapping.

You only judge the given local mapping.

Do not rewrite the translation.
Do not change target sense unit segmentation.
Do not create a new full mapping.
Do not assume there must be an error.

---

# CORE RULE

A source token is valid for a target sense unit if the target sense unit directly realizes that source token's meaning, or directly uses that source token as an anchor for a target-side functional unit.

A target-side functional unit is a target sense unit that is not a literal lexical translation of one source token, but is required for natural target-language expression.

Target-side functional units include:
- reference / pronoun
- anaphora
- explicitation
- discourse connector
- definition / naming frame
- result / completion expression
- natural target-side structural completion

These units may have a source anchor, but they may not have a clean one-to-one source-token replacement.

A source token is invalid only if it is broad context and does not directly realize or directly motivate the current target sense unit.

---

# INPUT FORMAT

source:
- language: <LANGUAGE NAME>
- source_tokens:
  0. <source token text>
  1. <source token text>
  2. <source token text>
  ...

target:
- language: <LANGUAGE NAME>
- target_sense_units:
  0. <target sense unit text>
  1. <target sense unit text>
  2. <target sense unit text>
  ...

current_mapping:
* target[<id>]: "<target sense unit text>"
  - source_tokens: <source token index>: "<source token text>", ...
  - triggers:
    - type: <trigger type>
      description: <short description>
      suspicious_items: <trigger-specific details>
    - type: <trigger type>
      description: <short description>
      suspicious_items: <trigger-specific details>

Each trigger explains why that specific mapping item was selected for checking.

A trigger does not mean the mapping is wrong.

A mapping item may have one or more triggers.

Check all triggers for the item, but make one final verdict for that target item.

---

# TRIGGER POLICY

Triggers are inspection notes, not error evidence.

A trigger only says why this mapping item was selected for checking.

Do not use the existence of a trigger as a reason for **mapping_error**.

For each target item, first ask:

Does the target sense unit directly realize the listed source tokens?

If yes, the verdict is valid, even if one or more triggers are present.

Use **mapping_error** only when the listed source tokens clearly are not directly realized by the target sense unit, or when directly realized source tokens are clearly missing.

If the mapping looks suspicious but the correct replacement is not clear from the local region, use uncertain.

Do not output **mapping_error** only because:
- a source token is duplicated
- the item has a backjump trigger
- the source token appears earlier than nearby mappings
- the source token is a pronoun/reference/discourse item

---

# TRIGGER INTERPRETATION

## duplicate_source_token

The same source token appears in more than one target sense unit.

This may be valid when:
- the source token expresses a relation distributed across multiple target units
- the target side explicitly repeats the same source meaning
- the target side uses reference or anaphora
- the source meaning is directly realized in more than one target unit

This is an error only when the repeated source token is broad context or is not directly realized by the current target unit.

## oversized_source_dependency

The target sense unit maps to many source tokens or to a source-token list that looks too broad.

This may be valid when the target sense unit genuinely compresses or realizes the listed source tokens.

This is an error only when some listed source tokens are broad context and are not directly needed by the current target unit.

## dependency_frontier_backjump

The target unit depends on earlier source tokens after nearby target units depend on later source tokens.

This may be valid because of word order, modifier placement, relation structure, or necessary reordering.

This is an error only when the mapping assigns unnecessary earlier source tokens, or when the target unit clearly does not directly realize those earlier tokens.

---

# OUTPUT FORMAT

You must output exactly two blocks in this order:

<scratchpad>
...
</scratchpad>
<result>
...
</result>

---

# SCRATCHPAD

In <scratchpad>, check each target item in current_mapping.

Use exactly this format:

* target[<id>]: "<target sense unit text>"
  - source_tokens: <source token index>: "<source token text>", ...
  - triggers_checked: <trigger type>, <trigger type>, ...
  - verdict: **mapping_error** / valid / uncertain
  - reason: "<short reason>"
  - replace_source_tokens: <source token index>: "<source token text>", ... / None

Rules:

1. First decide whether the listed source tokens are directly realized or directly motivate the target sense unit.

2. Use valid when all listed source tokens are directly realized or directly motivate the target sense unit.

3. Use **mapping_error** only when both conditions hold:
   - the mapping is clearly wrong because at least one listed source token is broad context / semantically wrong, or a directly realized source token is clearly missing
   - the corrected source token list is clear

4. Never output **mapping_error** with replace_source_tokens: None.

5. If the mapping looks wrong but no clear replacement exists, use uncertain.

6. Use uncertain when the mapping may be acceptable, the local region is insufficient, or the correction is unclear.

7. replace_source_tokens:
   - valid -> None
   - uncertain -> None
   - **mapping_error** -> corrected source token list

8. Triggers are inspection notes, not error evidence.

9. Keep reasons short.
   Check only the given current_mapping.

---

# FUNCTIONAL TARGET UNITS AND TRIGGERS

A trigger may point to a target-side functional unit.

Do not mark a target-side functional unit as **mapping_error** merely because it is not a literal translation of the listed source tokens.

For reference, anaphora, explicitation, discourse connector, definition / naming frame, result expression, or structural completion:
- valid means the listed source tokens are reasonable anchors for the target-side function
- uncertain means the function is reasonable but the best source anchor is unclear
- **mapping_error** means the listed source tokens are clearly wrong and a corrected source-token list is clear

---

# RESULT

<result> must contain exactly one JSON object.

Schema:

{
  "items": [
    {
      "target_senseunit_id": <int>,
      "verdict": "valid" | "mapping_error" | "uncertain",
      "reason": "<short reason>",
      "replace_source_tokens": [
        {"index": <int>, "text": "<source token text>"}
      ] | null
    }
  ],
  "final_verdict": "valid" | "mapping_error" | "uncertain"
}

Hard rules:
- If verdict is valid, replace_source_tokens must be null.
- If verdict is uncertain, replace_source_tokens must be null.
- If verdict is mapping_error, replace_source_tokens must be a non-empty list.
- Never output mapping_error with null replacement.
- If the correction is not clear, use uncertain.
- final_verdict must be derived from item verdicts.
- Do not output markdown inside <result>.

"""


USER_PROMPT_MAPPING_SEMANTIC_CHECK = """# CURRENT TASK

source:
- language: {{SOURCE_LANGUAGE_NAME}}
- source_tokens:
{{SOURCE_TOKENS}}

target:
- language: {{TARGET_LANGUAGE_NAME}}
- target_sense_units:
{{TARGET_SENSE_UNITS}}

current_mapping:
{{CURRENT_MAPPING}}
"""


class TargetCentricMappingValidationError(ValueError):
    """Raised when target-centric mapping violates Level 1 hard validation rules."""


class TargetCentricMappingDependencyError(TargetCentricMappingValidationError):
    """Raised when upstream artifacts cannot support target-centric mapping validation."""


class TargetCentricMappingSemanticFeedbackError(TargetCentricMappingValidationError):
    """Raised when semantic checking finds a concrete mapping error to reflect/retry."""


@dataclass(frozen=True)
class DuplicateSourceTokenDiagnostic:
    target_senseunit_id: int
    source_token_index: int
    target_senseunit_ids: list[int]
    severity: str = "needs_semantic_check"
    diagnostic: str = "duplicate_source_token"


@dataclass(frozen=True)
class OversizedSourceDependencyDiagnostic:
    target_senseunit_id: int
    source_token_ids: list[int]
    source_token_length: int
    contiguous: bool
    severity: str = "needs_semantic_check"
    diagnostic: str = "oversized_source_dependency"


@dataclass(frozen=True)
class DependencyFrontierBackjumpDiagnostic:
    target_senseunit_id: int
    ready_at: int
    previous_frontier: int
    backjump_size: int
    severity: str = "needs_semantic_check"
    diagnostic: str = "dependency_frontier_backjump"


Level2MappingDiagnostic = (
    DuplicateSourceTokenDiagnostic
    | OversizedSourceDependencyDiagnostic
    | DependencyFrontierBackjumpDiagnostic
)


def _parse_semantic_check_result_json_or_raise(result_text: str) -> dict:
    try:
        payload = json.loads(result_text)
    except Exception as e:
        raise TargetCentricMappingValidationError(f"JSON Format Error: semantic checker <result> must be valid JSON: {e}") from e
    if not isinstance(payload, dict):
        raise TargetCentricMappingValidationError("Output Format Error: semantic checker <result> must be a JSON object")
    return payload


def _validate_replace_source_tokens_or_raise(*, item_index: int, verdict: str, replace_source_tokens: object) -> None:
    if verdict in {"valid", "uncertain"}:
        if replace_source_tokens is not None:
            raise TargetCentricMappingValidationError(
                f"Contract Error: semantic checker item {item_index} with verdict {verdict!r} must use replace_source_tokens = null"
            )
        return

    if verdict != "mapping_error":
        raise TargetCentricMappingValidationError(
            f"Output Format Error: semantic checker item {item_index} has invalid verdict {verdict!r}"
        )

    if replace_source_tokens is None:
        raise TargetCentricMappingValidationError(
            f"Contract Error: semantic checker item {item_index} cannot use verdict 'mapping_error' with replace_source_tokens = null"
        )
    if not isinstance(replace_source_tokens, list) or not replace_source_tokens:
        raise TargetCentricMappingValidationError(
            f"Contract Error: semantic checker item {item_index} with verdict 'mapping_error' must use a non-empty replace_source_tokens list"
        )
    for replacement_index, replacement in enumerate(replace_source_tokens):
        if not isinstance(replacement, dict):
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} replace_source_tokens[{replacement_index}] must be a JSON object"
            )
        if "index" not in replacement or "text" not in replacement:
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} replace_source_tokens[{replacement_index}] must contain 'index' and 'text'"
            )
        if not isinstance(replacement["index"], int):
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} replace_source_tokens[{replacement_index}].index must be an integer"
            )
        if not isinstance(replacement["text"], str):
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} replace_source_tokens[{replacement_index}].text must be a string"
            )


def validate_semantic_check_result_or_raise(result_text: str) -> str:
    payload = _parse_semantic_check_result_json_or_raise(result_text)
    if "items" not in payload:
        raise TargetCentricMappingValidationError("Output Format Error: semantic checker <result> is missing required field 'items'")
    if "final_verdict" not in payload:
        raise TargetCentricMappingValidationError(
            "Output Format Error: semantic checker <result> is missing required field 'final_verdict'"
        )

    items = payload["items"]
    final_verdict = payload["final_verdict"]
    if not isinstance(items, list):
        raise TargetCentricMappingValidationError("Output Format Error: semantic checker 'items' must be a list")
    if final_verdict not in {"valid", "mapping_error", "uncertain"}:
        raise TargetCentricMappingValidationError(
            f"Output Format Error: semantic checker final_verdict must be one of valid / mapping_error / uncertain, got {final_verdict!r}"
        )

    item_verdicts: list[str] = []
    for item_index, item in enumerate(items):
        if not isinstance(item, dict):
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} must be a JSON object"
            )
        for field_name in ("target_senseunit_id", "verdict", "reason", "replace_source_tokens"):
            if field_name not in item:
                raise TargetCentricMappingValidationError(
                    f"Output Format Error: semantic checker item {item_index} is missing required field {field_name!r}"
                )
        if not isinstance(item["target_senseunit_id"], int):
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} target_senseunit_id must be an integer"
            )
        verdict = item["verdict"]
        if verdict not in {"valid", "mapping_error", "uncertain"}:
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} has invalid verdict {verdict!r}"
            )
        if not isinstance(item["reason"], str):
            raise TargetCentricMappingValidationError(
                f"Output Format Error: semantic checker item {item_index} reason must be a string"
            )
        _validate_replace_source_tokens_or_raise(
            item_index=item_index,
            verdict=verdict,
            replace_source_tokens=item["replace_source_tokens"],
        )
        item_verdicts.append(verdict)

    derived_final_verdict = "valid"
    if any(verdict == "mapping_error" for verdict in item_verdicts):
        derived_final_verdict = "mapping_error"
    elif any(verdict == "uncertain" for verdict in item_verdicts):
        derived_final_verdict = "uncertain"

    if final_verdict != derived_final_verdict:
        raise TargetCentricMappingValidationError(
            "Contract Error: semantic checker final_verdict contradicts item verdicts; "
            f"expected {derived_final_verdict!r}, got {final_verdict!r}"
        )
    return final_verdict


def extract_mapping_error_items_or_raise(result_text: str) -> list[dict]:
    validate_semantic_check_result_or_raise(result_text)
    payload = _parse_semantic_check_result_json_or_raise(result_text)
    items = payload["items"]

    mapping_error_items: list[dict] = []
    for item in items:
        if item["verdict"] == "mapping_error":
            mapping_error_items.append(item)
    return mapping_error_items


def render_mapping_error_items(mapping_error_items: Sequence[TypingMapping[str, object]]) -> str:
    rendered_items: list[str] = []
    for item in mapping_error_items:
        target_senseunit_id = item["target_senseunit_id"]
        reason = item["reason"]
        replace_source_tokens = item["replace_source_tokens"]
        replacement_text = "None"
        if isinstance(replace_source_tokens, list) and replace_source_tokens:
            replacement_text = ", ".join(
                f'{replacement["index"]}: "{replacement["text"]}"'
                for replacement in replace_source_tokens
                if isinstance(replacement, dict)
            )
        rendered_items.append(
            "\n".join(
                [
                    f"* target[{target_senseunit_id}]",
                    "  - verdict: mapping_error",
                    f'  - reason: "{reason}"',
                    f"  - replace_source_tokens: {replacement_text}",
                ]
            )
        )
    return "\n\n".join(rendered_items)


def _format_source_tokens(source_token_ids: Sequence[int], source_token_texts: TypingMapping[int, str]) -> str:
    return ", ".join(
        f'{source_token_id}: "{source_token_texts.get(source_token_id, "")}"'
        for source_token_id in source_token_ids
    )


def _is_contiguous(indices: Sequence[int]) -> bool:
    if not indices:
        return False
    ordered = sorted(indices)
    return ordered == list(range(ordered[0], ordered[-1] + 1))


def find_duplicate_source_tokens(mappings: Sequence[Mapping]) -> dict[int, list[int]]:
    usage: dict[int, list[int]] = {}
    for mapping in mappings:
        for source_token_id in mapping.source_token_ids:
            usage.setdefault(source_token_id, []).append(mapping.target_senseunit_id)
    return {source_token_id: target_ids for source_token_id, target_ids in usage.items() if len(target_ids) > 1}


def find_oversized_source_dependencies(
    mappings: Sequence[Mapping],
    *,
    max_len: int = 8,
    max_contiguous_len: int = 6,
) -> list[OversizedSourceDependencyDiagnostic]:
    diagnostics: list[OversizedSourceDependencyDiagnostic] = []
    for mapping in mappings:
        source_token_ids = list(mapping.source_token_ids)
        contiguous = _is_contiguous(source_token_ids)
        if len(source_token_ids) > max_len or (contiguous and len(source_token_ids) > max_contiguous_len):
            diagnostics.append(
                OversizedSourceDependencyDiagnostic(
                    target_senseunit_id=mapping.target_senseunit_id,
                    source_token_ids=source_token_ids,
                    source_token_length=len(source_token_ids),
                    contiguous=contiguous,
                )
            )
    return diagnostics


def find_dependency_frontier_backjumps(
    mappings: Sequence[Mapping],
    *,
    threshold: int = 5,
) -> list[DependencyFrontierBackjumpDiagnostic]:
    diagnostics: list[DependencyFrontierBackjumpDiagnostic] = []
    frontier = -1
    for mapping in mappings:
        ready_at = max(mapping.source_token_ids)
        if frontier >= 0 and ready_at < frontier:
            backjump_size = frontier - ready_at
            if backjump_size >= threshold:
                diagnostics.append(
                    DependencyFrontierBackjumpDiagnostic(
                        target_senseunit_id=mapping.target_senseunit_id,
                        ready_at=ready_at,
                        previous_frontier=frontier,
                        backjump_size=backjump_size,
                    )
                )
        frontier = max(frontier, ready_at)
    return diagnostics


def collect_level2_mapping_diagnostics(mappings: Sequence[Mapping]) -> list[Level2MappingDiagnostic]:
    duplicate_map = find_duplicate_source_tokens(mappings)
    diagnostics: list[Level2MappingDiagnostic] = []
    for source_token_index, target_senseunit_ids in duplicate_map.items():
        for target_senseunit_id in target_senseunit_ids:
            diagnostics.append(
                DuplicateSourceTokenDiagnostic(
                    target_senseunit_id=target_senseunit_id,
                    source_token_index=source_token_index,
                    target_senseunit_ids=list(target_senseunit_ids),
                )
            )
    diagnostics.extend(find_oversized_source_dependencies(mappings))
    diagnostics.extend(find_dependency_frontier_backjumps(mappings))
    return diagnostics


def _trigger_lines_for_diagnostic(
    diagnostic: Level2MappingDiagnostic,
    *,
    source_token_texts: TypingMapping[int, str],
) -> list[str]:
    if isinstance(diagnostic, DuplicateSourceTokenDiagnostic):
        source_token_text = source_token_texts.get(diagnostic.source_token_index, "")
        other_target_ids = [target_id for target_id in diagnostic.target_senseunit_ids if target_id != diagnostic.target_senseunit_id]
        other_targets_text = ", ".join(f"target[{target_id}]" for target_id in other_target_ids)
        return [
            "    - type: duplicate_source_token",
            (
                f"      description: source token {diagnostic.source_token_index} appears in multiple "
                f"target sense units"
            ),
            (
                f"      suspicious_items: source token `{diagnostic.source_token_index}: \"{source_token_text}\"`; "
                f"also appears in {other_targets_text}"
            ),
        ]
    if isinstance(diagnostic, OversizedSourceDependencyDiagnostic):
        return [
            "    - type: oversized_source_dependency",
            "      description: this target sense unit maps to an unusually large source-token list",
            (
                f"      suspicious_items: source_token_ids length = {diagnostic.source_token_length}; "
                f"contiguous = {str(diagnostic.contiguous).lower()}"
            ),
        ]
    return [
        "    - type: dependency_frontier_backjump",
        (
            "      description: this target sense unit depends on earlier source tokens after nearby "
            "target units used later source tokens"
        ),
        (
            f"      suspicious_items: ready_at = {diagnostic.ready_at}; previous_frontier = "
            f"{diagnostic.previous_frontier}; backjump_size = {diagnostic.backjump_size}"
        ),
    ]


def build_local_regions_with_inline_triggers(
    *,
    mappings: Sequence[Mapping],
    diagnostics: Sequence[Level2MappingDiagnostic],
    target_senseunit_texts: TypingMapping[int, str],
    source_token_texts: TypingMapping[int, str],
) -> list[str]:
    mapping_by_target_id = {mapping.target_senseunit_id: mapping for mapping in mappings}
    diagnostics_by_target_id: dict[int, list[Level2MappingDiagnostic]] = {}
    for diagnostic in diagnostics:
        diagnostics_by_target_id.setdefault(diagnostic.target_senseunit_id, []).append(diagnostic)

    rendered_regions: list[str] = []
    for target_senseunit_id in sorted(diagnostics_by_target_id):
        mapping = mapping_by_target_id.get(target_senseunit_id)
        if mapping is None:
            continue
        target_text = target_senseunit_texts.get(target_senseunit_id, "")
        trigger_lines: list[str] = []
        for diagnostic in diagnostics_by_target_id[target_senseunit_id]:
            trigger_lines.extend(
                _trigger_lines_for_diagnostic(
                    diagnostic,
                    source_token_texts=source_token_texts,
                )
            )
        rendered_regions.append(
            "\n".join(
                [
                    f'* target[{target_senseunit_id}]: "{target_text}"',
                    f"  - source_tokens: `{_format_source_tokens(mapping.source_token_ids, source_token_texts)}`",
                    "  - triggers:",
                    *trigger_lines,
                ]
            )
        )
    return rendered_regions


def render_level3_semantic_check_input(
    *,
    source_language_name: str,
    target_language_name: str,
    source_token_texts: TypingMapping[int, str],
    target_senseunit_texts: TypingMapping[int, str],
    current_mapping: str,
) -> str:
    source_tokens_rendered = "\n".join(
        f"  {source_token_id}. {source_token_text}"
        for source_token_id, source_token_text in source_token_texts.items()
    )
    target_units_rendered = "\n".join(
        f"  {target_senseunit_id}. {target_senseunit_text}"
        for target_senseunit_id, target_senseunit_text in target_senseunit_texts.items()
    )
    return (
        USER_PROMPT_MAPPING_SEMANTIC_CHECK.replace("{{SOURCE_LANGUAGE_NAME}}", source_language_name)
        .replace("{{SOURCE_TOKENS}}", source_tokens_rendered)
        .replace("{{TARGET_LANGUAGE_NAME}}", target_language_name)
        .replace("{{TARGET_SENSE_UNITS}}", target_units_rendered)
        .replace("{{CURRENT_MAPPING}}", current_mapping)
    )


def extract_semantic_check_raw_blocks(response_text: str) -> tuple[str, str]:
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


def extract_semantic_check_blocks(response_text: str) -> tuple[str, str]:
    scratchpad, result = extract_semantic_check_raw_blocks(response_text)
    if not result:
        raise TargetCentricMappingValidationError("Output Format Error: semantic checker result block could not be recovered")
    normalized_verdict = validate_semantic_check_result_or_raise(result)
    return scratchpad, normalized_verdict


def extract_semantic_mapping_error_feedback_or_raise(response_text: str) -> str | None:
    """Return retry feedback for mapping_error items from a semantic-check response.

    Level-3 semantic-check output is object-shaped. This helper intentionally
    parses the semantic-check <result> directly instead of reusing the main
    mapping-stage array extractor.
    """
    _, result = extract_semantic_check_raw_blocks(response_text)
    if not result:
        raise TargetCentricMappingValidationError("Output Format Error: semantic checker result block could not be recovered")
    final_verdict = validate_semantic_check_result_or_raise(result)
    if final_verdict != "mapping_error":
        return None
    mapping_error_items = extract_mapping_error_items_or_raise(result)
    if not mapping_error_items:
        return None
    return render_mapping_error_items(mapping_error_items)


def validate_mapping_result_or_raise(
    *,
    mappings: Sequence[Mapping],
    expected_target_ids: Sequence[int],
    source_token_count: int,
) -> None:
    actual_target_ids = [mapping.target_senseunit_id for mapping in mappings]
    if list(actual_target_ids) != list(expected_target_ids):
        raise TargetCentricMappingValidationError(
            f"Output Format Error: target IDs must appear exactly once in order {list(expected_target_ids)}, got {actual_target_ids}"
        )

    max_source_id = source_token_count - 1
    for mapping in mappings:
        if not mapping.source_token_ids:
            raise TargetCentricMappingValidationError("Output Format Error: source_token_ids must be non-empty")
        for source_id in mapping.source_token_ids:
            if source_id < 0 or source_id > max_source_id:
                raise TargetCentricMappingValidationError(
                    f"Output Format Error: invalid source token index {source_id}"
                )


def _format_word(word_id: int, word: Word) -> str:
    return f'word[{word_id}]: "{word.word}" start={word.start:.2f} end={word.end:.2f}'


def _format_source_group(group_id: int, group: Sequence[int], words: Sequence[Word]) -> str:
    group_words = [words[word_id].word for word_id in group if 0 <= word_id < len(words)]
    return f"source_senseunit[{group_id}]: word ids {list(group)} => \"{' '.join(group_words)}\""


def _mapped_target_ids_by_source_token(mappings: Sequence[Mapping]) -> dict[int, list[int]]:
    usage: dict[int, list[int]] = {}
    for mapping in mappings:
        for source_token_id in mapping.source_token_ids:
            usage.setdefault(source_token_id, []).append(mapping.target_senseunit_id)
    return {source_token_id: sorted(set(target_ids)) for source_token_id, target_ids in usage.items()}


def _validate_source_sense_units_assign_to_release_windows_or_raise(
    *,
    source_duration: float,
    words: Sequence[Word],
    source_sense_unit_groups: Sequence[Sequence[int]],
    eps: float = 1e-6,
) -> None:
    chunks = build_transcription_chunks(duration=source_duration, words=list(words))
    if not chunks:
        raise TargetCentricMappingDependencyError(
            "Upstream Dependency Error: source release-window construction produced no windows.\n\n"
            f"metadata.duration/source_duration: {source_duration}\n"
            f"reconstructed source words: {len(words)}\n\n"
            "This is an upstream timing/source segmentation dependency problem, not a target mapping JSON problem."
        )

    assigned_group_count = 0
    word_release_window_indices: list[int | None] = [None] * len(words)
    for chunk_idx, chunk in enumerate(chunks):
        is_final_chunk = chunk_idx == len(chunks) - 1
        while assigned_group_count < len(source_sense_unit_groups):
            group = list(source_sense_unit_groups[assigned_group_count])
            last_word_idx = group[-1]
            seg_end = words[last_word_idx].end
            last_word_is_in_chunk = any(word is words[last_word_idx] for word in chunk.words)
            last_token_final_overrun = is_final_chunk and last_word_idx == len(words) - 1 and last_word_is_in_chunk
            if seg_end < chunk.end + eps or last_token_final_overrun:
                for word_id in group:
                    word_release_window_indices[word_id] = chunk_idx
                assigned_group_count += 1
            else:
                break

    if assigned_group_count == len(source_sense_unit_groups) and all(
        release_window is not None for release_window in word_release_window_indices
    ):
        return

    unassigned_group_lines: list[str] = []
    for group_id in range(assigned_group_count, len(source_sense_unit_groups)):
        group = list(source_sense_unit_groups[group_id])
        last_word_idx = group[-1]
        last_word = words[last_word_idx]
        unassigned_group_lines.append(
            f'- source_senseunit[{group_id}]: word ids {group}; '
            f'last {_format_word(last_word_idx, last_word)}'
        )

    uncovered_word_lines = [
        f"- {_format_word(word_id, words[word_id])}"
        for word_id, release_window in enumerate(word_release_window_indices)
        if release_window is None
    ]
    chunk_lines = [
        f"- window[{chunk_idx}]: start={chunk.start:.2f} end={chunk.end:.2f} words={len(chunk.words)}"
        for chunk_idx, chunk in enumerate(chunks)
    ]
    message_lines = [
        "Upstream Dependency Error: source sense units cannot all be assigned to release windows.",
        "",
        "Why this matters:",
        "Target-centric mapping can only be accepted when source tokens project through source words and source sense units into streaming release windows. If a source sense unit has no release window, mapped target emission timing is undefined.",
        "",
        f"metadata.duration/source_duration: {source_duration}",
        f"constructed release windows: {len(chunks)}",
        f"assigned source sense units: {assigned_group_count}/{len(source_sense_unit_groups)}",
        "",
        "This is an upstream timing/source segmentation dependency problem, not a target mapping JSON problem. Do not invent source_token_ids to bypass it.",
        "",
        "Constructed release windows:",
        *chunk_lines,
    ]
    if unassigned_group_lines:
        message_lines.extend(["", "Unassigned source sense-unit groups:", *unassigned_group_lines])
    if uncovered_word_lines:
        message_lines.extend(["", "Source words without release windows:", *uncovered_word_lines])
    raise TargetCentricMappingDependencyError("\n".join(message_lines))


def validate_mapping_downstream_readiness_or_raise(
    *,
    mappings: Sequence[Mapping],
    source_duration: float,
    source_language_code: str,
    alignment_tokens: Sequence[Word],
    alignment_word_groups: Sequence[Sequence[int]],
    source_sense_unit_groups: Sequence[Sequence[int]],
) -> None:
    """Validate that accepted mapping can be projected to streaming release windows.

    Target-centric mapping itself uses source text-token ids. Downstream conversation
    construction must project those ids onto reconstructed source words, then onto
    source sense-unit release windows. This helper catches dependency failures at
    the mapping validation boundary and renders actionable diagnostics instead of
    leaking low-context errors from ``build_translation_blocks``.
    """

    try:
        words = apply_mapping_groups(
            list(alignment_tokens),
            [list(group) for group in alignment_word_groups],
            language=source_language_code,
        )
    except Exception as e:
        raise TargetCentricMappingDependencyError(
            "Contract Error: source word reconstruction failed, so target-centric mapping cannot be validated "
            "for streaming release.\n\n"
            "Why this matters:\n"
            "Target-centric mapping uses source_token_ids, but streaming release requires converting each "
            "source token to timed source words first.\n\n"
            f"Underlying source word reconstruction error:\n{e}\n\n"
            "This is not a mapping JSON-format problem. It is an upstream forced-alignment/word-group "
            "dependency problem. Do not invent source_token_ids to bypass it."
        ) from e

    if not words:
        raise TargetCentricMappingDependencyError(
            "Contract Error: source word reconstruction produced no words, so target-centric mapping cannot be "
            "validated for streaming release.\n\n"
            "This is an upstream source alignment dependency problem, not a target mapping JSON-format problem."
        )

    covered_word_ids: set[int] = set()
    invalid_group_lines: list[str] = []
    group_lines: list[str] = []
    for group_id, group in enumerate(source_sense_unit_groups):
        group_list = list(group)
        if not group_list:
            invalid_group_lines.append(f"source_senseunit[{group_id}] is empty")
            continue
        invalid_word_ids = [word_id for word_id in group_list if word_id < 0 or word_id >= len(words)]
        if invalid_word_ids:
            invalid_group_lines.append(
                f"source_senseunit[{group_id}] contains out-of-range word ids {invalid_word_ids}; "
                f"available source words: {len(words)}"
            )
        covered_word_ids.update(word_id for word_id in group_list if 0 <= word_id < len(words))
        group_lines.append(_format_source_group(group_id, group_list, words))

    uncovered_word_ids = [word_id for word_id in range(len(words)) if word_id not in covered_word_ids]
    if not invalid_group_lines and not uncovered_word_ids:
        source_text_tokens = [token.word for token in alignment_tokens]
        source_token_word_groups = _build_alignment_token_to_word_groups(
            alignment_token_count=len(alignment_tokens),
            alignment_word_groups=alignment_word_groups,
        )
        empty_token_groups = [token_id for token_id, word_group in enumerate(source_token_word_groups) if not word_group]
        if not empty_token_groups:
            _validate_source_sense_units_assign_to_release_windows_or_raise(
                source_duration=source_duration,
                words=words,
                source_sense_unit_groups=source_sense_unit_groups,
            )
            return
    else:
        source_text_tokens = [token.word for token in alignment_tokens]
        source_token_word_groups = _build_alignment_token_to_word_groups(
            alignment_token_count=len(alignment_tokens),
            alignment_word_groups=alignment_word_groups,
        )
        empty_token_groups = []

    affected_lines: list[str] = []
    usage_by_source_token = _mapped_target_ids_by_source_token(mappings)
    uncovered_word_id_set = set(uncovered_word_ids)
    for source_token_id, word_group in enumerate(source_token_word_groups):
        affected_word_ids = [word_id for word_id in word_group if word_id in uncovered_word_id_set]
        if affected_word_ids:
            token_text = source_text_tokens[source_token_id] if source_token_id < len(source_text_tokens) else ""
            affected_lines.append(
                f'- source_token[{source_token_id}]: "{token_text}" aligns to word ids {list(word_group)}; '
                f"uncovered word ids {affected_word_ids}; used by target_senseunit_id(s): "
                f"{usage_by_source_token.get(source_token_id, [])}"
            )

    message_lines = [
        "Upstream Dependency Error: source time-pressure segmentation has incomplete word coverage.",
        "",
        "Why this matters:",
        "Target-centric mapping uses source_token_ids, but streaming release requires converting each source token to aligned source word ids and then to source sense-unit release windows. Any source word without a source sense-unit release window makes mapped target emission timing undefined.",
        "",
        "This is not a target mapping JSON-format problem. The mapping candidate may already include the affected source_token_id. This should have been rejected by pipeline 5 as ISSUE4: missing emitted indices. Rerun or repair source time-pressure segmentation instead of asking the target-centric mapping agent to change source_token_ids.",
    ]
    if invalid_group_lines:
        message_lines.extend(["", "Invalid source sense-unit groups:", *[f"- {line}" for line in invalid_group_lines]])
    if uncovered_word_ids:
        message_lines.extend(
            [
                "",
                "Source words not covered by any source sense-unit group:",
                *[f"- {_format_word(word_id, words[word_id])}" for word_id in uncovered_word_ids],
            ]
        )
    if empty_token_groups:
        message_lines.extend(
            [
                "",
                "Source tokens that did not align to any reconstructed source word:",
                *[f'- source_token[{token_id}]: "{source_text_tokens[token_id]}"' for token_id in empty_token_groups],
            ]
        )
    message_lines.extend(["", "Current source sense-unit groups cover these word ids:", *[f"- {line}" for line in group_lines]])
    if affected_lines:
        message_lines.extend(["", "Mapped source tokens affected by uncovered source words:", *affected_lines])
    raise TargetCentricMappingDependencyError("\n".join(message_lines))


def _build_alignment_token_to_word_groups(
    *,
    alignment_token_count: int,
    alignment_word_groups: Sequence[Sequence[int]],
) -> list[list[int]]:
    token_to_word_ids: list[list[int]] = [[] for _ in range(alignment_token_count)]
    for word_id, token_group in enumerate(alignment_word_groups):
        for token_id in token_group:
            if 0 <= token_id < alignment_token_count:
                token_to_word_ids[token_id].append(word_id)
    return token_to_word_ids