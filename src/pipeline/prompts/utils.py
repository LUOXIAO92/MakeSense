"""
Utility functions for pipeline prompts.

Contains audio normalization, message building, and prompt builders.
"""

import re
import base64
import json

from pathlib import Path
from typing import Literal, Optional, Any, Sequence

from core.schema import MetaData, Transcription
from pipeline.prompts.one_pass import (
    SYSTEM_INSTRUCTION_ASR_TRANSLATION_OMNI as SYS_ONE_PASS,
    USER_INSTRUCTION_ASR_TRANSLATION_OMNI as USR_ONE_PASS,
)
from pipeline.prompts.translation_reconstruction import (
    SYSTEM_INSTRUCTION_RESTRUCTURE as SYS_RECONSTRUCTION,
    USER_INSTRUCTION_RESTRUCTURE as USR_RECONSTRUCTION,
)
from pipeline.prompts.pure_text_translation import (
    SYSTEM_INSTRUCTION_TRANSLATION as SYS_TRANSLATION,
    USER_INSTRUCTION_TRANSLATION as USR_TRANSLATION,
)
from pipeline.prompts.pure_text_translation_assisted import (
    SYSTEM_INSTRUCTION_TRANSLATION_AUDIO_ASSISTED as SYS_TRANSLATION_AUDIO_ASSISTED,
    USER_INSTRUCTION_TRANSLATION_AUDIO_ASSISTED as USR_TRANSLATION_AUDIO_ASSISTED,
)
from pipeline.schema import PipelineRecord

from configs.config import Config

CODE2LANGUAGE = Config.lang_code2name
WINDOW_SIZE = Config.window_size


AudioLike = str | Path | bytes | bytearray | dict[str, str]


def normalize_one_audio(
    audio: AudioLike,
    default_format: str = "wav"
) -> dict[str, str]:
    """Normalize audio input to base64 data dict."""
    if isinstance(audio, dict):
        if "data" not in audio or "format" not in audio:
            raise ValueError(f"Audio dict must contain 'data' and 'format': {audio}")
        return {
            "data": audio["data"],
            "format": audio["format"].lower(),
        }

    if isinstance(audio, (str, Path)):
        path = Path(audio)
        fmt = path.suffix.lstrip(".").lower() or default_format
        data_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")
        return {"data": data_b64, "format": fmt}

    if isinstance(audio, (bytes, bytearray)):
        data_b64 = base64.b64encode(audio).decode("utf-8")
        return {"data": data_b64, "format": default_format.lower()}

    raise TypeError(f"Unsupported audio input type: {type(audio).__name__}")


def build_messages_with_audio_placeholders(
    prompt: str,
    audios: AudioLike | Sequence[AudioLike],
    placeholder: str = "{{AUDIO}}",
    default_format: str = "wav",
) -> list[dict[str, Any]]:
    """
    Replace {{AUDIO}} placeholders in `prompt` with OpenAI-style input_audio blocks.

    Supported audio inputs:
    - file path: "a.wav" / Path("a.wav")
    - raw bytes: b"..."
    - prebuilt dict: {"data": "<base64>", "format": "wav"}

    Return:
        A content list ready to be used as the value of a chat message's
        `"content"` field in OpenAI Chat Completions format.
    """

    if isinstance(audios, (str, Path, bytes, bytearray, dict)):
        audio_list = [audios]
    else:
        audio_list = list(audios)

    parts = re.split(re.escape(placeholder), prompt)
    placeholder_count = len(parts) - 1

    if placeholder_count != len(audio_list):
        raise ValueError(
            f"Placeholder count ({placeholder_count}) does not match "
            f"number of audios ({len(audio_list)})."
        )

    content: list[dict[str, Any]] = []

    for i, text_part in enumerate(parts):
        if text_part:
            content.append({"type": "text", "text": text_part})

        if i < placeholder_count:
            audio_obj = normalize_one_audio(audio_list[i])
            content.append(
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": audio_obj["data"],
                        "format": audio_obj["format"],
                    },
                }
            )

    return content


def build_prompt_one_pass(
    meta: MetaData,
    target_language_names: Optional[Sequence[str]] = None
):
    """Build system and user prompts for omni ASR + translation."""

    try:
        src_lang_name = CODE2LANGUAGE[meta.language]
        if meta.language == "ZH":
            src_lang_name = "Chinese (simplified)"
        src_lang_mode = "fixed"
    except Exception as e:
        src_lang_name = "unknown"
        src_lang_mode = "infer"

    if target_language_names is None:
        tgt_lang_names = [
            CODE2LANGUAGE[code]
            for code in Config.language_codes
            if code != meta.language
        ]
    else:
        tgt_lang_names = list(target_language_names)

    system_prompt = SYS_ONE_PASS
    user_prompt = USR_ONE_PASS\
        .replace("{{SOURCE_LANGUAGE}}", src_lang_name)\
        .replace("{{SOURCE_LANGUAGE_MODE}}", src_lang_mode)\
        .replace("{{TARGET_LANGUAGES}}", ", ".join(tgt_lang_names))

    return system_prompt, user_prompt, tgt_lang_names


def build_prompt_translation_only(
    transcription: Transcription,
    target_language_codes: Optional[Sequence[str]] = None,
) -> tuple[str, str, list[str]]:
    """Build staged translation-only prompts following the builder pattern."""

    source_lang_name = CODE2LANGUAGE[transcription.language]

    if target_language_codes is None:
        tgt_lang_codes = [
            code for code in Config.language_codes
            if code != transcription.language
        ]
    else:
        tgt_lang_codes = list(target_language_codes)

    target_lang_names = ", ".join(CODE2LANGUAGE[code] for code in tgt_lang_codes)

    system_prompt = SYS_TRANSLATION.replace("{{ORIGINAL_LANGUAGE}}", source_lang_name)
    user_prompt = (
        USR_TRANSLATION
        .replace("{{SOURCE_LANGUAGE}}", source_lang_name)
        .replace("{{TARGET_LANGUAGES}}", target_lang_names)
        .replace("{{RAW_TEXT}}", transcription.text)
    )

    return system_prompt, user_prompt, tgt_lang_codes


def build_prompt_translation_audio_assisted(
    transcription: Transcription,
    target_language_codes: Optional[Sequence[str]] = None,
) -> tuple[str, str, list[str]]:
    """Build staged audio-assisted translation prompts using ASR text as anchor."""

    source_lang_name = CODE2LANGUAGE[transcription.language]

    if target_language_codes is None:
        tgt_lang_codes = [
            code for code in Config.language_codes
            if code != transcription.language
        ]
    else:
        tgt_lang_codes = list(target_language_codes)

    target_lang_names = ", ".join(CODE2LANGUAGE[code] for code in tgt_lang_codes)

    system_prompt = SYS_TRANSLATION_AUDIO_ASSISTED.replace("{{ORIGINAL_LANGUAGE}}", source_lang_name)
    user_prompt = (
        USR_TRANSLATION_AUDIO_ASSISTED
        .replace("{{SOURCE_LANGUAGE}}", source_lang_name)
        .replace("{{TARGET_LANGUAGES}}", target_lang_names)
        .replace("{{RAW_TEXT}}", transcription.text)
    )

    return system_prompt, user_prompt, tgt_lang_codes


def build_prompt_translation_reconstruction(
    record: PipelineRecord,
    target_language_codes: Optional[Sequence[str]] = None,
) -> tuple[str, str, list[str]]:
    """Build prompts for multi-language translation reconstruction."""

    transcript = record.source.artifacts.transcript
    source_language_code = (transcript.language_code if transcript else "") or record.metadata.language
    source_language_name = CODE2LANGUAGE[source_language_code]

    if target_language_codes is None:
        tgt_lang_codes = [
            code for code in Config.language_codes
            if code != source_language_code and code in record.target.languages
        ]
    else:
        tgt_lang_codes = list(target_language_codes)

    target_language_names = [CODE2LANGUAGE[code] for code in tgt_lang_codes]
    raw_translation_payload = {
        CODE2LANGUAGE[code]: record.target.languages[code].artifacts.raw_translation.text
        for code in tgt_lang_codes
        if code in record.target.languages and record.target.languages[code].artifacts.raw_translation.text
    }

    system_prompt = SYS_RECONSTRUCTION
    user_prompt = (
        USR_RECONSTRUCTION
        .replace("{{SOURCE_LANGUAGE}}", source_language_name)
        .replace("{{TARGET_LANGUAGE}}", ", ".join(target_language_names))
        .replace("{{RAW_TEXT}}", transcript.text if transcript else "")
        .replace("{{STAGE1_ANALYSIS}}", record.target.shared.translation_analysis.strip())
        .replace(
            "{{RAW_TRANSLATION}}",
            json.dumps(raw_translation_payload, ensure_ascii=False, indent=2),
        )
    )

    return system_prompt, user_prompt, tgt_lang_codes