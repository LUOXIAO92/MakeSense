"""Run pure text segmentation over prerequisite cache records only."""
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
from llm.llm_model import LLM
from pipeline.runners import (
    PureTextSegmentationRunner,
    load_pipeline_records_by_part_latest,
)
from pipeline.runners.utils import load_pipeline_records_by_uid, print_llm_pipeline_summary, stage_output_path_from_input_cache

DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"

# CACHE_ROOT       = Path(".") / "cache_test"
CACHE_ROOT   = DATASET_ROOT / "cache"
INPUT_CACHE_BASE = CACHE_ROOT / "pipeline_6_translation_reconstruction_deepseek-v4-flash"
OUTPUT_BASE      = CACHE_ROOT / "pipeline_7_pure_text_segmentation_deepseek-v4-flash"

BASE_URL = os.environ.get("OPEN_ROUTER_BASE_URL")
API_KEY = os.environ.get("OPEN_ROUTER_API_KEY")
# MODEL_NAME = "deepseek/deepseek-v4-flash"
MODEL_NAME = "google/gemini-3.1-flash-lite"

# BASE_URL="http://127.0.0.1:12345/v1"
# MODEL_NAME="qwen3.6-27b@q6_k"

DEFAULT_CONCURRENCY = 128
MAX_CURRENT_TASKS = 512
MAX_TOKENS = 7800
TEMPERATURE = 0.6
TOP_P = 0.95
MAX_RETRIES = 5
# Provider-specific OpenAI-compatible request extensions.
# vLLM / local OpenAI-compatible API example:
# EXTRA_BODY = {"top_k": 20, "chat_template_kwargs": {"enable_thinking": False}}
# OpenRouter reasoning example:
# EXTRA_BODY = {"reasoning": {"effort": "none"}}
# DeepSeek thinking example:
# EXTRA_BODY = {"thinking": {"type": "disabled"}}
EXTRA_BODY = None
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
    runner = PureTextSegmentationRunner(
        llm=llm,
        concurrency=DEFAULT_CONCURRENCY,
        max_retries=MAX_RETRIES,
    )
    prerequisite_cache_parts = load_pipeline_records_by_part_latest(INPUT_CACHE_BASE)
    total_units = 0
    existing_finished = 0
    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        output_path = stage_output_path_from_input_cache(
            OUTPUT_BASE,
            INPUT_CACHE_BASE,
            input_cache_path,
            "pure_text_segmentation",
        )
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        candidate_records, _ = runner.filter_segmentation_candidates(prerequisite_records)
        for record in candidate_records:
            existing_record = existing_output_by_uid.get(record.uid)
            source_record = existing_record or record
            target_codes = runner._prerequisite_target_language_codes(source_record)
            total_units += len(target_codes)
            if existing_record:
                existing_finished += sum(
                    1
                    for code in target_codes
                    if runner.branch_status(existing_record, code) == "finished"
                )

    runner.reset_progress(
        show_tqdm_bar=SHOW_TQDM_BAR,
        total=total_units,
        desc="Processing...",
        initial=existing_finished,
    )

    print("=== Pipeline 7: pure text segmentation ===")
    print("input_cache_dir_name:", INPUT_CACHE_BASE.name)
    print("output_dir_name:", OUTPUT_BASE.name)
    print("model_name:", MODEL_NAME)
    print("concurrency:", DEFAULT_CONCURRENCY)
    print("max_retries:", MAX_RETRIES)
    print("max_tokens:", MAX_TOKENS)
    print("temperature:", TEMPERATURE)
    print("extra_body:", EXTRA_BODY)
    print("enable_visualization:", ENABLE_VISUALIZATION)
    print("max_current_tasks:", MAX_CURRENT_TASKS)
    print()

    summaries = []
    output_paths = []
    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        output_path = stage_output_path_from_input_cache(
            OUTPUT_BASE,
            INPUT_CACHE_BASE,
            input_cache_path,
            "pure_text_segmentation",
        )
        summary = await runner.run_cache_shard(
            input_cache_base=INPUT_CACHE_BASE,
            input_cache_path=input_cache_path,
            prerequisite_records=prerequisite_records,
            output_root=OUTPUT_BASE,
            max_current_tasks=MAX_CURRENT_TASKS,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            extra_body=EXTRA_BODY,
            enable_visualization=ENABLE_VISUALIZATION,
        )
        summaries.append(summary)
        output_paths.append(output_path)

    runner.close_progress()
    print_llm_pipeline_summary(
        title="Pipeline 7: pure text segmentation",
        summaries=summaries,
        output_paths=output_paths,
        stage="pure_text_segmentation",
    )


if __name__ == "__main__":
    asyncio.run(main())