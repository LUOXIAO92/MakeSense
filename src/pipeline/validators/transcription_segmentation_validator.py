from dataclasses import dataclass, field
from math import ceil
from core.schema import MetaData, Transcription, Word
from configs.config import Config
from core.utils import apply_mapping_groups

EPS = Config.eps
WAIT_TOKEN     = Config.wait_token
WINDOW_SIZE    = Config.window_size
MAX_CHUNK_SIZE = Config.max_chunk_size


class ASRChunkingValidationError(ValueError):
    """Raised when streaming ASR chunking violates hard validation rules."""


@dataclass(frozen=True)
class OversizedChunkViolation:
    group_index: int
    emitted_window: int
    release_unit_number_in_window: int
    size: int
    threshold: int
    indices: list[int]


@dataclass(frozen=True)
class DuplicatedEmissionViolation:
    emitted_window: int
    release_unit_number_in_window: int
    duplicated_indices: list[int]
    duplicated_token_map: dict[int, str]
    first_seen_at: dict[int, tuple[int, int]]


@dataclass(frozen=True)
class MissingEmissionViolation:
    expected_window: int
    missing_indices: list[int]
    missing_token_map: dict[int, str]


@dataclass(frozen=True)
class NonMonotonicGroupViolation:
    group_index: int
    previous_max_index: int
    offending_indices: list[int]


@dataclass(frozen=True)
class WindowReleaseUnitEmission:
    group_index: int
    release_unit_number_in_window: int
    indices: list[int]
    token_map: dict[int, str]
    size: int


@dataclass(frozen=True)
class WindowTraceRow:
    window_index: int
    input_map: dict[int, str]
    output_release_units: list[WindowReleaseUnitEmission]
    issue1_note: str | None = None
    issue2_notes: list[str] = field(default_factory=list)
    issue3_notes: list[str] = field(default_factory=list)
    issue4_notes: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ValidationDiagnostics:
    window_inputs: list[dict[int, str]]
    wait_mask: list[bool]
    trace_rows: list[WindowTraceRow]
    rendered_trace: str
    oversized_chunks: list[OversizedChunkViolation]
    duplicated_emissions: list[DuplicatedEmissionViolation]
    missing_emissions: list[MissingEmissionViolation]
    non_monotonic_groups: list[NonMonotonicGroupViolation]


def _format_token_map(token_map: dict[int, str]) -> str:
    if not token_map:
        return "{}"
    return "{" + ", ".join(f"{idx}: {word!r}" for idx, word in token_map.items()) + "}"


def _window_count(duration: float, window_size: float = WINDOW_SIZE) -> int:
    return max(1, ceil(duration / window_size))


def _build_chunks_like_transcription(
    duration: float,
    words: list[Word],
    window_size: float = WINDOW_SIZE,
    eps: float = EPS,
    ) -> list[tuple[float, float, dict[int, str]]]:
    """
    Mirror build_transcription_chunks() behavior exactly for window assignment:
    consume words in order and assign a word to the earliest chunk whose end
    satisfies word.end <= chunk.end + eps.
    """
    chunks: list[tuple[float, float, dict[int, str]]] = []
    words_idx_start = 0
    n_windows = _window_count(duration, window_size)

    for i in range(n_windows):
        start = i * window_size
        end = min((i + 1) * window_size, duration)
        token_map: dict[int, str] = {}

        for rel_idx, word in enumerate(words[words_idx_start:]):
            if word.end <= end + eps or i == n_windows - 1:
                abs_idx = words_idx_start + rel_idx
                token_map[abs_idx] = word.word
            else:
                break

        words_idx_start += len(token_map)
        chunks.append((start, end, token_map))
    return chunks


def _build_window_inputs(duration: float, words: list[Word], window_size: float = WINDOW_SIZE) -> list[dict[int, str]]:
    return [token_map for _, _, token_map in _build_chunks_like_transcription(duration, words, window_size, EPS)]


def _build_window_emissions(
    duration: float,
    words: list[Word],
    groups: list[list[int]],
    threshold: int,
    window_size: float = WINDOW_SIZE,
    eps: float = EPS,
    ) -> tuple[list[bool], list[list[WindowReleaseUnitEmission]], list[OversizedChunkViolation]]:
    """
    Rebuild per-window ASR emissions using the same rule as build_asr_blocks:
    a release_unit is emitted in the earliest chunk whose end time is >= release_unit end.
    Chunk boundaries are the same as build_transcription_chunks().
    """
    chunks = _build_chunks_like_transcription(duration, words, window_size, eps)
    wait_mask: list[bool] = []
    per_window: list[list[WindowReleaseUnitEmission]] = []
    oversized: list[OversizedChunkViolation] = []

    group_idx = 0
    for wi, (_, end, _) in enumerate(chunks):
        release_units: list[WindowReleaseUnitEmission] = []
        is_final_window = wi == len(chunks) - 1

        while group_idx < len(groups):
            group = groups[group_idx]
            if not group:
                group_idx += 1
                continue

            seg_end = words[group[-1]].end
            if seg_end < end + eps or is_final_window:
                release_unit_num = len(release_units) + 1
                token_map = {idx: words[idx].word for idx in group}
                release_units.append(
                    WindowReleaseUnitEmission(
                        group_index=group_idx,
                        release_unit_number_in_window=release_unit_num,
                        indices=list(group),
                        token_map=token_map,
                        size=len(group),
                    )
                )
                if len(group) > threshold:
                    oversized.append(
                        OversizedChunkViolation(
                            group_index=group_idx,
                            emitted_window=wi,
                            release_unit_number_in_window=release_unit_num,
                            size=len(group),
                            threshold=threshold,
                            indices=list(group),
                        )
                    )
                group_idx += 1
            else:
                break

        per_window.append(release_units)
        wait_mask.append(len(release_units) == 0)

    return wait_mask, per_window, oversized


def _detect_duplicated_emissions(
    per_window_release_units: list[list[WindowReleaseUnitEmission]],
) -> list[DuplicatedEmissionViolation]:
    """Detect indices emitted more than once across the final ASR timeline."""
    seen: dict[int, tuple[int, int]] = {}
    violations: list[DuplicatedEmissionViolation] = []

    for wi, release_units in enumerate(per_window_release_units):
        for release_unit in release_units:
            duplicated_indices: list[int] = []
            duplicated_token_map: dict[int, str] = {}
            first_seen_at: dict[int, tuple[int, int]] = {}

            for idx in release_unit.indices:
                if idx in seen:
                    duplicated_indices.append(idx)
                    duplicated_token_map[idx] = release_unit.token_map[idx]
                    first_seen_at[idx] = seen[idx]
                else:
                    seen[idx] = (wi, release_unit.release_unit_number_in_window)

            if duplicated_indices:
                violations.append(
                    DuplicatedEmissionViolation(
                        emitted_window=wi,
                        release_unit_number_in_window=release_unit.release_unit_number_in_window,
                        duplicated_indices=duplicated_indices,
                        duplicated_token_map=duplicated_token_map,
                        first_seen_at=first_seen_at,
                    )
                )

    return violations


def _detect_missing_emissions(
    window_inputs: list[dict[int, str]],
    per_window_release_units: list[list[WindowReleaseUnitEmission]],
    words: list[Word],
) -> list[MissingEmissionViolation]:
    """Detect reconstructed word indices that never appear in any emitted release unit.

    Window inputs are duration-driven, but downstream mapping requires every
    reconstructed aligned source word to belong to exactly one emitted sense unit.
    Therefore ISSUE4 must also catch aligned words whose ``word.end`` falls just
    beyond metadata duration and never enters any duration-derived input window.
    """
    emitted_indices: set[int] = set()
    for release_units in per_window_release_units:
        for release_unit in release_units:
            emitted_indices.update(release_unit.indices)

    violations: list[MissingEmissionViolation] = []
    window_input_indices: set[int] = set()
    for wi, input_map in enumerate(window_inputs):
        window_input_indices.update(input_map.keys())
        missing_token_map = {
            idx: token
            for idx, token in input_map.items()
            if idx not in emitted_indices
        }
        if missing_token_map:
            violations.append(
                MissingEmissionViolation(
                    expected_window=wi,
                    missing_indices=list(missing_token_map.keys()),
                    missing_token_map=missing_token_map,
                )
            )

    out_of_window_missing_token_map = {
        idx: word.word
        for idx, word in enumerate(words)
        if idx not in emitted_indices and idx not in window_input_indices
    }
    if out_of_window_missing_token_map:
        violations.append(
            MissingEmissionViolation(
                expected_window=max(0, len(window_inputs) - 1),
                missing_indices=list(out_of_window_missing_token_map.keys()),
                missing_token_map=out_of_window_missing_token_map,
            )
        )
    return violations


def _detect_non_monotonic_groups(groups: list[list[int]]) -> list[NonMonotonicGroupViolation]:
    violations: list[NonMonotonicGroupViolation] = []
    previous_max_index = -1
    for group_index, group in enumerate(groups):
        if not group:
            continue
        offending_indices = [idx for idx in group if idx <= previous_max_index]
        if offending_indices:
            violations.append(
                NonMonotonicGroupViolation(
                    group_index=group_index,
                    previous_max_index=previous_max_index,
                    offending_indices=offending_indices,
                )
            )
        previous_max_index = max(previous_max_index, max(group))
    return violations


def _build_trace_rows(
    window_inputs: list[dict[int, str]],
    wait_mask: list[bool],
    per_window_release_units: list[list[WindowReleaseUnitEmission]],
    oversized_chunks: list[OversizedChunkViolation],
    duplicated_emissions: list[DuplicatedEmissionViolation],
    missing_emissions: list[MissingEmissionViolation],
    forbidden_streak: int,
    ) -> list[WindowTraceRow]:
    oversized_by_window: dict[int, list[OversizedChunkViolation]] = {}
    for item in oversized_chunks:
        oversized_by_window.setdefault(item.emitted_window, []).append(item)

    duplicated_by_window: dict[int, list[DuplicatedEmissionViolation]] = {}
    for item in duplicated_emissions:
        duplicated_by_window.setdefault(item.emitted_window, []).append(item)

    missing_by_window: dict[int, list[MissingEmissionViolation]] = {}
    for item in missing_emissions:
        missing_by_window.setdefault(item.expected_window, []).append(item)

    rows: list[WindowTraceRow] = []
    nonempty_wait_streak = 0

    for wi, input_map in enumerate(window_inputs):
        is_nonempty = bool(input_map)
        is_wait = wait_mask[wi]
        release_units = per_window_release_units[wi]

        if is_nonempty and is_wait:
            nonempty_wait_streak += 1
        else:
            nonempty_wait_streak = 0

        issue1_note = None
        if nonempty_wait_streak >= forbidden_streak:
            issue1_note = f"ISSUE1: consecutive non-empty wait x{nonempty_wait_streak}, delay too long."

        issue2_notes: list[str] = []
        for item in oversized_by_window.get(wi, []):
            issue2_notes.append(
                f"ISSUE2: oversized chunk release unit {item.release_unit_number_in_window} size={item.size} > {item.threshold}. "
                f"Likely accumulated too much before emitting or packed too many tokens into one phrase."
                )

        issue3_notes: list[str] = []
        for item in duplicated_by_window.get(wi, []):
            dup_map = _format_token_map(item.duplicated_token_map)
            first_refs = ", ".join(
                f"{idx}@W{w}/U{u}" for idx, (w, u) in sorted(item.first_seen_at.items())
            )
            issue3_notes.append(
                f"ISSUE3: duplicated emitted indices in release unit {item.release_unit_number_in_window} {dup_map} "
                f"(first emitted at {first_refs})."
            )

        issue4_notes: list[str] = []
        for item in missing_by_window.get(wi, []):
            missing_map = _format_token_map(item.missing_token_map)
            issue4_notes.append(
                f"ISSUE4: missing emitted indices {missing_map}. "
                "Every input word index must be emitted exactly once in sense_units.groups."
            )

        rows.append(
            WindowTraceRow(
                window_index=wi,
                input_map=input_map,
                output_release_units=release_units,
                issue1_note=issue1_note,
                issue2_notes=issue2_notes,
                issue3_notes=issue3_notes,
                issue4_notes=issue4_notes,
                )
            )

    return rows


def _render_trace(rows: list[WindowTraceRow]) -> str:
    lines: list[str] = []
    for row in rows:
        input_s = _format_token_map(row.input_map)
        if row.output_release_units:
            parts = [f"{p.release_unit_number_in_window}.{_format_token_map(p.token_map)}" for p in row.output_release_units]
            output_s = "release_units " + "; ".join(parts)
        else:
            output_s = "release_units None"

        notes: list[str] = []
        if row.issue1_note:
            notes.append(row.issue1_note)
        notes.extend(row.issue2_notes)
        notes.extend(row.issue3_notes)
        notes.extend(row.issue4_notes)
        suffix = f" <- {'; '.join(notes)}" if notes else ""
        lines.append(f"* W{row.window_index}. input: {input_s} - output: {output_s}{suffix}")
    return "\n".join(lines)


def collect_chunking_diagnostics(
        metadata: MetaData,
        transcription: Transcription,
        issue1_forbidden_streak: int = 2,
        thresholds: dict[str, int] = MAX_CHUNK_SIZE,
    ) -> ValidationDiagnostics:
    threshold = thresholds.get(transcription.language.upper(), 6)
    words = apply_mapping_groups(transcription.tokens, transcription.words, language=transcription.language)

    window_inputs = _build_window_inputs(metadata.duration, words)
    wait_mask, per_window_release_units, oversized_chunks = _build_window_emissions(
        metadata.duration,
        words,
        transcription.sense_units.groups,
        threshold,
        )
    duplicated_emissions = _detect_duplicated_emissions(per_window_release_units)
    missing_emissions = _detect_missing_emissions(window_inputs, per_window_release_units, words)
    non_monotonic_groups = _detect_non_monotonic_groups(transcription.sense_units.groups)
    rows = _build_trace_rows(
        window_inputs,
        wait_mask,
        per_window_release_units,
        oversized_chunks,
        duplicated_emissions,
        missing_emissions,
        issue1_forbidden_streak,
        )
    rendered = _render_trace(rows)

    return ValidationDiagnostics(
        window_inputs=window_inputs,
        wait_mask=wait_mask,
        trace_rows=rows,
        rendered_trace=rendered,
        oversized_chunks=oversized_chunks,
        duplicated_emissions=duplicated_emissions,
        missing_emissions=missing_emissions,
        non_monotonic_groups=non_monotonic_groups,
        )


def validate_chunking_or_raise(
        metadata: MetaData,
        transcription: Transcription,
        issue1_forbidden_streak: int = 2,
    ) -> None:
    diagnostics = collect_chunking_diagnostics(
        metadata,
        transcription,
        issue1_forbidden_streak=issue1_forbidden_streak,
        )

    has_issue1 = any(row.issue1_note for row in diagnostics.trace_rows)
    has_issue2 = bool(diagnostics.oversized_chunks)
    has_issue3 = bool(diagnostics.duplicated_emissions)
    has_issue4 = bool(diagnostics.missing_emissions)
    has_issue5 = bool(diagnostics.non_monotonic_groups)

    if has_issue1 or has_issue2 or has_issue3 or has_issue4 or has_issue5:
        parts = ["Sense unit segmentation validation failed:", diagnostics.rendered_trace]
        if has_issue5:
            parts.extend(
                [
                    "",
                    "Non-monotonic sense unit groups:",
                    *[
                        (
                            f"ISSUE5: sense_units.groups[{item.group_index}] contains indices {item.offending_indices} "
                            f"that do not come strictly after previous emitted index {item.previous_max_index}. "
                            "sense_units.groups must be globally monotonic and non-overlapping."
                        )
                        for item in diagnostics.non_monotonic_groups
                    ],
                ]
            )
        parts.append("\nReconfirm the RULEs and your task!\n")
        raise ASRChunkingValidationError("\n".join(parts))
