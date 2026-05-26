from dataclasses import dataclass

from configs.config import Config


MAX_CHUNK_SIZE = Config.max_chunk_size


class PureTextSegmentationValidationError(ValueError):
    """Raised when pure-text segmentation violates hard validation rules."""


@dataclass(frozen=True)
class OversizedChunkViolation:
    group_index: int
    size: int
    threshold: int
    indices: list[int]


@dataclass(frozen=True)
class ValidationDiagnostics:
    groups: list[list[int]]
    oversized_chunks: list[OversizedChunkViolation]
    rendered_trace: str


def _format_token_map(token_map: dict[int, str]) -> str:
    if not token_map:
        return "{}"
    return "{" + ", ".join(f"{idx}: {word!r}" for idx, word in token_map.items()) + "}"


def _build_group_token_map(
    group: list[int],
    token_indices: dict[int, str],
) -> dict[int, str]:
    return {idx: token_indices[idx] for idx in group if idx in token_indices}


def _collect_oversized_chunks(
    groups: list[list[int]],
    threshold: int,
) -> list[OversizedChunkViolation]:
    violations: list[OversizedChunkViolation] = []
    for group_index, group in enumerate(groups):
        if len(group) > threshold:
            violations.append(
                OversizedChunkViolation(
                    group_index=group_index,
                    size=len(group),
                    threshold=threshold,
                    indices=list(group),
                )
            )
    return violations


def _render_trace(
    groups: list[list[int]],
    violations: list[OversizedChunkViolation],
    token_indices: dict[int, str],
) -> str:
    violations_by_group = {item.group_index: item for item in violations}
    lines: list[str] = []
    for group_index, group in enumerate(groups):
        token_map = _build_group_token_map(group, token_indices)
        line = f"{group_index}. {_format_token_map(token_map)}"
        violation = violations_by_group.get(group_index)
        if violation is not None:
            line += f" <- oversized chunk size={violation.size} > {violation.threshold}"
        lines.append(line)
    return "\n".join(lines)


def collect_pure_text_segmentation_diagnostics(
    *,
    language: str,
    groups: list[list[int]],
    token_indices: dict[int, str],
    thresholds: dict[str, int] = MAX_CHUNK_SIZE,
) -> ValidationDiagnostics:
    threshold = thresholds.get(language.upper(), 6)
    oversized_chunks = _collect_oversized_chunks(groups, threshold)
    return ValidationDiagnostics(
        groups=groups,
        oversized_chunks=oversized_chunks,
        rendered_trace=_render_trace(groups, oversized_chunks, token_indices),
    )


def validate_pure_text_segmentation_or_raise(
    *,
    language: str,
    groups: list[list[int]],
    token_indices: dict[int, str],
) -> None:
    diagnostics = collect_pure_text_segmentation_diagnostics(
        language=language,
        groups=groups,
        token_indices=token_indices,
    )
    if diagnostics.oversized_chunks:
        parts = [
            "Pure text segmentation validation failed:",
            diagnostics.rendered_trace,
            "\nReconfirm the RULEs and your task!\n",
        ]
        raise PureTextSegmentationValidationError("\n".join(parts))