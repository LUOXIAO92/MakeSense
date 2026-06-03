"""Run omni translation over all records in a dataset.

This script:
- reads every metadata record under a dataset root,
- loads matching audio,
- runs omni ASR + translation,
- prints and saves both scratchpad and final result.

"""
import sys
sys.path.append('src')

import warnings
import logging
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
warnings.filterwarnings("ignore", message=r"The value of the smallest subnormal.*type is zero", category=UserWarning, module=r"numpy\.(?:_core|core)\.getlimits")

import asyncio
import os
from pathlib import Path
from llm.llm_model import LLM
from pipeline.runners import (
    TranslationOnlyRunner,
    load_pipeline_records_by_part,
)
from pipeline.runners.utils import cache_output_path, is_finished_omni_translation_record, load_pipeline_records_by_uid
from pipeline.schema import PipelineRecord


# DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"
DATASET_ROOT = Path(".") / "dataset_test"

CACHE_ROOT       = Path(".") / "cache_test"
INPUT_CACHE_BASE = CACHE_ROOT / "pipeline_2_initialized"
OUTPUT_BASE      = CACHE_ROOT / "pipeline_3_asr_translation_gemini-3.1-flash-lite"

BASE_URL = os.environ.get("OPEN_ROUTER_BASE_URL")
API_KEY = os.environ.get("OPEN_ROUTER_API_KEY")
MODEL_NAME = "google/gemini-3.1-flash-lite"

# BASE_URL="http://127.0.0.1:18000/v1"
# MODEL_NAME="nemotron-3-nano-omni-30b-a3b"

DEFAULT_CONCURRENCY = 32
MAX_CURRENT_TASKS = 128
MAX_RETRIES = 5
MAX_TOKENS = 8192
TEMPERATURE = 0.3
TOP_P = 0.95
TOP_K = 40
ENABLE_THINKING = False
ENABLE_VISUALIZATION = True
SHOW_TQDM_BAR = True


async def main() -> None:
    if not BASE_URL or not API_KEY:
        raise RuntimeError("OPEN_ROUTER_BASE_URL / OPEN_ROUTER_API_KEY must be set")

    llm = LLM(
        model_name=MODEL_NAME,
        base_url=BASE_URL,
        api_key=API_KEY,
        batch_size=DEFAULT_CONCURRENCY,
    )

    prerequisite_cache_parts = load_pipeline_records_by_part(INPUT_CACHE_BASE)
    runner = TranslationOnlyRunner(
        llm=llm,
        concurrency=DEFAULT_CONCURRENCY,
        max_retries=MAX_RETRIES,
    )
    total_records = sum(len(records) for _, records in prerequisite_cache_parts)
    existing_finished = 0
    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        metadata_list = [record.metadata for record in prerequisite_records]
        metadata_jsonl_path = input_cache_path.parent / input_cache_path.name.replace("cache_", "metadata-", 1)
        output_path = cache_output_path(OUTPUT_BASE, metadata_jsonl_path, "translation")
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        existing_finished += sum(
            1
            for meta in metadata_list
            if is_finished_omni_translation_record(
                existing_output_by_uid.get(meta.uid, PipelineRecord(uid=meta.uid, metadata=meta))
            )
        )
    runner.reset_progress(
        show_tqdm_bar=SHOW_TQDM_BAR,
        total=total_records,
        desc="Processing...",
        initial=existing_finished,
    )

    print("=== Pipeline 3a: Omni transcription + translation ===")
    print("records:", total_records)
    print("input_cache_dir_name:", INPUT_CACHE_BASE.name)
    print("output_dir_name:", OUTPUT_BASE.name)
    print("concurrency:", DEFAULT_CONCURRENCY)
    print("max_retries:", MAX_RETRIES)
    print("max_tokens:", MAX_TOKENS)
    print("temperature:", TEMPERATURE)
    print("top_p:", TOP_P)
    print("top_k:", TOP_K)
    print("enable_thinking:", ENABLE_THINKING)
    print("enable_visualization:", ENABLE_VISUALIZATION)
    print("show_tqdm_bar:", SHOW_TQDM_BAR)
    print("max_current_tasks:", MAX_CURRENT_TASKS)
    print()

    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        metadata_list = [record.metadata for record in prerequisite_records]
        metadata_jsonl_path = input_cache_path.parent / input_cache_path.name.replace("cache_", "metadata-", 1)
        summary = await runner.run_omni_translation_shard(
            metadata_jsonl_path=metadata_jsonl_path,
            metadata_list=metadata_list,
            dataset_root=DATASET_ROOT,
            output_root=OUTPUT_BASE,
            max_current_tasks=MAX_CURRENT_TASKS,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            top_k=TOP_K,
            enable_thinking=ENABLE_THINKING,
            enable_visualization=ENABLE_VISUALIZATION,
        )
        # print(f"shard: {metadata_jsonl_path.name} -> {summary['output_label']}")
        # print("existing_finished:", summary["existing_finished"])
        # print("pending:", summary["pending"])
        # print("finished:", summary["finished"])
        # print("failed:", summary["failed"])
    runner.close_progress()

if __name__ == "__main__":
    asyncio.run(main())