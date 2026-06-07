import sys
sys.path.append('src')

import warnings
import logging
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
warnings.filterwarnings("ignore", message=r"The value of the smallest subnormal.*type is zero", category=UserWarning, module=r"numpy\.(?:_core|core)\.getlimits")


import os
import asyncio
from pathlib import Path
from tqdm import tqdm
from configs.config import Config
from pipeline.providers import Qwen3ForcedAlignment, WhisperXForcedAlignment
from pipeline.runners import ForcedAlignmentRunner, load_pipeline_records_by_part_latest
from pipeline.runners.utils import load_pipeline_records_by_uid, stage_output_path_from_input_cache


DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"
# DATASET_ROOT = Path(".") / "dataset_test"

# CACHE_ROOT       = Path(".") / "cache_test"
CACHE_ROOT = DATASET_ROOT / "cache"
INPUT_CACHE_BASE = CACHE_ROOT / "pipeline_3_b2_translation_text_only_gemini-3.1-flash-lite"
OUTPUT_BASE      = CACHE_ROOT / "pipeline_4_forced_alignment_qwen3forcedaligner"


DEFAULT_CONCURRENCY = 1
MAX_CURRENT_TASKS = 1
SHOW_TQDM_BAR = True
ENABLE_VISUALIZATION = True
BATCH_SIZE = 32
ALIGN_PROVIDER = "qwen3"  # "qwen3" | "whisperx"
REPAIR_RAW_TOKEN_TIMING_OVERLAP = False  # Default/recommended: False. If True, repair only recoverable adjacent-token boundary drift.


def _write_alignment_duration_notice(message: str) -> None:
    if SHOW_TQDM_BAR:
        tqdm.write(message)
    else:
        print(message)


def collect_alignment_duration_notices(
    *,
    output_path: Path,
    current_task_uids: set[str],
) -> list[dict[str, object]]:
    notices: list[dict[str, object]] = []
    if not current_task_uids or not output_path.exists():
        return notices

    output_by_uid = load_pipeline_records_by_uid(output_path)
    for uid in sorted(current_task_uids):
        record = output_by_uid.get(uid)
        if record is None:
            continue
        alignment = record.source.artifacts.alignment
        if alignment is None or not alignment.tokens:
            continue
        last_token = alignment.tokens[-1]
        last_end = float(last_token.end)
        duration = float(record.metadata.duration)
        if last_end <= duration:
            continue
        notice = {
            "uid": record.uid,
            "source_language": record.metadata.language,
            "last_token": last_token.word,
            "last_end": last_end,
            "duration": duration,
            "delta": last_end - duration,
            "file": str(output_path),
        }
        notices.append(notice)
        _write_alignment_duration_notice(
            "ALIGNMENT_DURATION_NOTICE "
            f"pipeline=4 uid={record.uid} source={record.metadata.language} "
            f"last_token={last_token.word!r} last_end={last_end:.4f} "
            f"duration={duration:.4f} delta={last_end - duration:.4f} "
            "tail_absorption=final_window "
            "note='last token exceeds duration and will be absorbed into the final window' "
            f"file={output_path}"
        )
    return notices


def print_alignment_duration_notice_summary(notices: list[dict[str, object]]) -> None:
    print()
    print("=== Pipeline 4: alignment duration reminders (absorbed into final window) ===")
    print("count:", len(notices))
    if not notices:
        return
    for notice in notices:
        print(
            f"uid={notice['uid']} "
            f"source={notice['source_language']} "
            f"last_token={notice['last_token']!r} "
            f"last_end={float(notice['last_end']):.4f} "
            f"duration={float(notice['duration']):.4f} "
            f"delta={float(notice['delta']):.4f} "
            "note='will be absorbed into the final window' "
            f"file={notice['file']}"
        )

QWEN3_ALIGN_MODELS = {
    lang_code: Qwen3ForcedAlignment(model, device_map="cpu", attn_implementation=None, max_inference_batch_size=BATCH_SIZE)
    for lang_code, model in Config.forced_alignment.items()
}

WHISPERX_ALIGN_MODELS = {
    lang_code: WhisperXForcedAlignment(model_name="default", language=lang_code, device="cpu")
    for lang_code in Config.language_codes
}


async def main() -> None:
    prerequisite_cache_parts = load_pipeline_records_by_part_latest(INPUT_CACHE_BASE)
    runner = ForcedAlignmentRunner(
        concurrency=DEFAULT_CONCURRENCY,
        repair_raw_token_timing_overlap=REPAIR_RAW_TOKEN_TIMING_OVERLAP,
    )
    total_records = sum(len(records) for _, records in prerequisite_cache_parts)
    existing_finished = 0
    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        output_path = stage_output_path_from_input_cache(
            OUTPUT_BASE,
            INPUT_CACHE_BASE,
            input_cache_path,
            "forced_alignment",
        )
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        existing_finished += sum(
            1
            for record in prerequisite_records
            if record.uid in existing_output_by_uid
            and runner.record_status(existing_output_by_uid[record.uid]) == "finished"
        )
    runner.reset_progress(
        show_tqdm_bar=SHOW_TQDM_BAR,
        total=total_records,
        desc="Processing...",
        initial=existing_finished,
    )

    print("=== Pipeline 4: forced alignment ===")
    print("dataset_root:", DATASET_ROOT)
    print("input_cache_dir_name:", INPUT_CACHE_BASE.name)
    print("output_dir_name:", OUTPUT_BASE.name)
    print("max_current_tasks:", MAX_CURRENT_TASKS)
    print("enable_visualization:", ENABLE_VISUALIZATION)
    print("repair_raw_token_timing_overlap:", REPAIR_RAW_TOKEN_TIMING_OVERLAP)
    print()

    if ALIGN_PROVIDER not in {"qwen3", "whisperx"}:
        raise ValueError(f"Unsupported ALIGN_PROVIDER: {ALIGN_PROVIDER}")

    loaded_models: dict[str, Qwen3ForcedAlignment | WhisperXForcedAlignment] = {}
    alignment_duration_notices: list[dict[str, object]] = []
    try:
        for input_cache_path, prerequisite_records in prerequisite_cache_parts:
            if not prerequisite_records:
                continue

            output_path = stage_output_path_from_input_cache(
                OUTPUT_BASE,
                INPUT_CACHE_BASE,
                input_cache_path,
                "forced_alignment",
            )
            existing_output_by_uid = load_pipeline_records_by_uid(output_path)
            pending_records = [
                record
                for record in prerequisite_records
                if record.uid not in existing_output_by_uid
                or runner.record_status(existing_output_by_uid[record.uid]) != "finished"
            ]
            current_task_uids = {record.uid for record in pending_records}

            if not pending_records:
                continue

            lang = prerequisite_records[0].metadata.language
            if lang not in loaded_models:
                if ALIGN_PROVIDER == "qwen3":
                    loaded_models[lang] = QWEN3_ALIGN_MODELS[lang].load()
                else:
                    loaded_models[lang] = WHISPERX_ALIGN_MODELS[lang].load()

            if ALIGN_PROVIDER == "qwen3":
                summary = await runner.run_cache_shard_qwen3(
                    input_cache_base=INPUT_CACHE_BASE,
                    input_cache_path=input_cache_path,
                    prerequisite_records=prerequisite_records,
                    output_root=OUTPUT_BASE,
                    dataset_root=DATASET_ROOT,
                    provider=loaded_models[lang],
                    max_current_tasks=MAX_CURRENT_TASKS,
                    enable_visualization=ENABLE_VISUALIZATION,
                )
            else:
                summary = await runner.run_cache_shard_whisperx(
                    input_cache_base=INPUT_CACHE_BASE,
                    input_cache_path=input_cache_path,
                    prerequisite_records=prerequisite_records,
                    output_root=OUTPUT_BASE,
                    dataset_root=DATASET_ROOT,
                    provider=loaded_models[lang],
                    max_current_tasks=MAX_CURRENT_TASKS,
                    enable_visualization=ENABLE_VISUALIZATION,
                )
            alignment_duration_notices.extend(
                collect_alignment_duration_notices(
                    output_path=output_path,
                    current_task_uids=current_task_uids,
                )
            )
    finally:
        for model in loaded_models.values():
            model.unload()
        runner.close_progress()
    print_alignment_duration_notice_summary(alignment_duration_notices)


if __name__ == "__main__":
    asyncio.run(main())