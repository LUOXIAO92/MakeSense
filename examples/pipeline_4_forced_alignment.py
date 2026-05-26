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
from configs.config import Config
from pipeline.providers import Qwen3ForcedAlignment, WhisperXForcedAlignment
from pipeline.runners import ForcedAlignmentRunner, load_pipeline_records_by_part_latest
from pipeline.runners.utils import load_pipeline_records_by_uid, stage_output_path_from_input_cache


# DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"
DATASET_ROOT = Path(".") / "dataset_test"

CACHE_ROOT       = Path(".") / "cache_test"
INPUT_CACHE_BASE = CACHE_ROOT / "pipeline_3_b2_translation_text_only_gemini-3.1-flash-lite"
OUTPUT_BASE      = CACHE_ROOT / "pipeline_4_forced_alignment_qwen3forcedaligner"


DEFAULT_CONCURRENCY = 1
MAX_CURRENT_TASKS = 20
SHOW_TQDM_BAR = True
ENABLE_VISUALIZATION = True
BATCH_SIZE = 1
ALIGN_PROVIDER = "qwen3"  # "qwen3" | "whisperx"

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
    runner = ForcedAlignmentRunner(concurrency=DEFAULT_CONCURRENCY)
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
    print()

    if ALIGN_PROVIDER not in {"qwen3", "whisperx"}:
        raise ValueError(f"Unsupported ALIGN_PROVIDER: {ALIGN_PROVIDER}")

    loaded_models: dict[str, Qwen3ForcedAlignment | WhisperXForcedAlignment] = {}
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
    finally:
        for model in loaded_models.values():
            model.unload()
        runner.close_progress()


if __name__ == "__main__":
    asyncio.run(main())