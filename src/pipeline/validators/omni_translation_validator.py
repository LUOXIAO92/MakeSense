"""Omni-translation validation utilities."""

from dataclasses import dataclass
from typing import Sequence

from pipeline.schema import OmniTranslationResult

class OmniTranslationValidationError(ValueError):
    """Raised when omni ASR+translation violates hard validation rules."""


@dataclass(frozen=True)
class OmniTranslationDiagnostics:
    expected_target_languages: list[str]
    produced_target_languages: list[str]
    missing_target_languages: list[str]
    unexpected_target_languages: list[str]
    empty_target_languages: list[str]
    missing_asr_keys: list[str]
    empty_asr_keys: list[str]

    @property
    def has_error(self) -> bool:
        return any([
            self.missing_target_languages,
            self.unexpected_target_languages,
            self.empty_target_languages,
            self.missing_asr_keys,
            self.empty_asr_keys,
        ])


REQUIRED_ASR_KEYS = ("language_name", "language_code", "text")


def _is_blank_string(value) -> bool:
    return not isinstance(value, str) or not value.strip()


def _validate_asr(result: OmniTranslationResult) -> tuple[list[str], list[str]]:
    missing_keys: list[str] = []
    empty_keys: list[str] = []

    for key in REQUIRED_ASR_KEYS:
        if key not in result.asr:
            missing_keys.append(key)
        elif _is_blank_string(result.asr[key]):
            empty_keys.append(key)

    return missing_keys, empty_keys


def _validate_translation_outputs(
    result: OmniTranslationResult,
    target_language_names: Sequence[str],
) -> tuple[list[str], list[str], list[str], list[str], list[str]]:
    expected_target_languages = list(target_language_names)
    produced_target_languages = list(result.translation.keys())

    expected_set = set(expected_target_languages)
    produced_set = set(produced_target_languages)

    missing_target_languages = sorted(expected_set - produced_set)
    unexpected_target_languages = sorted(produced_set - expected_set)

    empty_target_languages: list[str] = []
    for lang_name in expected_target_languages:
        if lang_name in result.translation and _is_blank_string(result.translation[lang_name]):
            empty_target_languages.append(lang_name)

    return (
        expected_target_languages,
        produced_target_languages,
        missing_target_languages,
        unexpected_target_languages,
        empty_target_languages,
    )


def collect_omni_translation_diagnostics(
    result: OmniTranslationResult,
    target_language_names: Sequence[str],
) -> OmniTranslationDiagnostics:
    missing_asr_keys, empty_asr_keys = _validate_asr(result)
    (
        expected_target_languages,
        produced_target_languages,
        missing_target_languages,
        unexpected_target_languages,
        empty_target_languages,
    ) = _validate_translation_outputs(result, target_language_names)

    return OmniTranslationDiagnostics(
        expected_target_languages=expected_target_languages,
        produced_target_languages=produced_target_languages,
        missing_target_languages=missing_target_languages,
        unexpected_target_languages=unexpected_target_languages,
        empty_target_languages=empty_target_languages,
        missing_asr_keys=missing_asr_keys,
        empty_asr_keys=empty_asr_keys,
    )


def validate_omni_translation_or_raise(
    result: OmniTranslationResult,
    target_language_names: Sequence[str],
) -> None:
    diagnostics = collect_omni_translation_diagnostics(result, target_language_names)

    if not diagnostics.has_error:
        return

    parts: list[str] = ["Omni-translation validation failed:"]

    parts.append(
        f"- expected target languages: {diagnostics.expected_target_languages}"
    )
    parts.append(
        f"- produced target languages: {diagnostics.produced_target_languages}"
    )

    if diagnostics.missing_asr_keys:
        parts.append(f"- missing ASR keys: {diagnostics.missing_asr_keys}")

    if diagnostics.empty_asr_keys:
        parts.append(f"- empty ASR keys: {diagnostics.empty_asr_keys}")

    if diagnostics.missing_target_languages:
        parts.append(
            f"- missing translation outputs: {diagnostics.missing_target_languages}"
        )

    if diagnostics.unexpected_target_languages:
        parts.append(
            f"- unexpected translation outputs: {diagnostics.unexpected_target_languages}"
        )

    if diagnostics.empty_target_languages:
        parts.append(
            f"- empty translation outputs: {diagnostics.empty_target_languages}"
        )

    parts.append("\nReconfirm the OUTPUT FORMAT and OUTPUT RULES!\n")
    raise OmniTranslationValidationError("\n".join(parts))