"""Optionally run ASR over initialized cache records that do not yet have transcript state."""
import sys
sys.path.append('src')


import warnings
import logging
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("transformers.generation.utils").setLevel(logging.ERROR)
warnings.filterwarnings("ignore", message=r"The value of the smallest subnormal.*type is zero", category=UserWarning, module=r"numpy\.(?:_core|core)\.getlimits")

import os
import asyncio
from pathlib import Path
from configs.config import Config
from pipeline.providers.qwen3_asr_provider import Qwen3ASR
from pipeline.runners import TranscriptionRunner, load_pipeline_records_by_part_latest
from pipeline.runners.utils import load_pipeline_records_by_uid, stage_output_path_from_input_cache


# DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"
DATASET_ROOT = Path(".") / "dataset_test"

CACHE_ROOT       = Path(".") / "cache_test"
INPUT_CACHE_BASE = CACHE_ROOT  / "pipeline_2_initialized"
OUTPUT_BASE      = CACHE_ROOT  / "pipeline_3_b1_asr_qwen3asr1.7b"

DEFAULT_CONCURRENCY = 1
MAX_CURRENT_TASKS = 20
SHOW_TQDM_BAR = True
BATCH_SIZE = 1
MAX_RETRIES = 5

ASR_MODELS = {
    lang_code: Qwen3ASR(model, device_map="mps", max_inference_batch_size=BATCH_SIZE, attn_implementation=None)
    for lang_code, model in Config.asr_models.items()
}


async def main() -> None:
    prerequisite_cache_parts = load_pipeline_records_by_part_latest(INPUT_CACHE_BASE)
    runner = TranscriptionRunner(
        concurrency=DEFAULT_CONCURRENCY,
        provider_max_retries=MAX_RETRIES,
    )
    total_records = sum(len(records) for _, records in prerequisite_cache_parts)
    existing_finished = 0
    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        output_path = stage_output_path_from_input_cache(
            OUTPUT_BASE,
            INPUT_CACHE_BASE,
            input_cache_path,
            "asr",
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

    print("=== Pipeline 3 b1: Transcription ===")
    print("dataset_root:", DATASET_ROOT)
    print("input_cache_dir_name:", INPUT_CACHE_BASE.name)
    print("output_dir_name:", OUTPUT_BASE.name)
    print("max_current_tasks:", MAX_CURRENT_TASKS)
    print("max_retries:", MAX_RETRIES)
    print()

    loaded_models: dict[str, Qwen3ASR] = {}
    try:
        for input_cache_path, prerequisite_records in prerequisite_cache_parts:
            if not prerequisite_records:
                continue
            lang = prerequisite_records[0].metadata.language
            if lang not in loaded_models:
                loaded_models[lang] = ASR_MODELS[lang].load()
            await runner.run_cache_shard(
                input_cache_base=INPUT_CACHE_BASE,
                input_cache_path=input_cache_path,
                prerequisite_records=prerequisite_records,
                output_root=OUTPUT_BASE,
                dataset_root=DATASET_ROOT,
                asr_model=loaded_models[lang],
                max_current_tasks=MAX_CURRENT_TASKS,
            )
    finally:
        for model in loaded_models.values():
            model.unload()
        runner.close_progress()


if __name__ == "__main__":
    asyncio.run(main())