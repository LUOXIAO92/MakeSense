"""Run translation reconstruction over prerequisite cache records only."""
import sys
sys.path.append('src')


import warnings
import logging
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
warnings.filterwarnings("ignore", message=r"The value of the smallest subnormal.*type is zero", category=UserWarning, module=r"numpy\.(?:_core|core)\.getlimits")


import asyncio
import json
import os
from pathlib import Path
from tqdm import tqdm
from configs.config import Config
from core.utils import tokenize
from llm.llm_model import LLM
from pipeline.runners import (
    TranslationReconstructionRunner,
)
from pipeline.runners.utils import load_pipeline_records_by_uid, print_llm_pipeline_summary, reconstruction_output_path_from_input_cache
from pipeline.schema import PipelineRecord

DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"

# CACHE_ROOT       = Path(".") / "cache_test"
CACHE_ROOT   = DATASET_ROOT / "cache"
OUTPUT_BASE      = CACHE_ROOT / "pipeline_6_translation_reconstruction_deepseek-v4-flash"
INPUT_CACHE_BASE = CACHE_ROOT / "pipeline_5_asr_segmentation_deepseek-v4-flash"

BASE_URL = os.environ.get("OPEN_ROUTER_BASE_URL")
API_KEY = os.environ.get("OPEN_ROUTER_API_KEY")
# MODEL_NAME = "deepseek/deepseek-v4-flash"
MODEL_NAME = "google/gemini-3.1-flash-lite"

RECONSTRUCTION_VALIDATOR_BASE_URL = BASE_URL
RECONSTRUCTION_VALIDATOR_API_KEY  = API_KEY
RECONSTRUCTION_VALIDATOR_MODEL_NAME = MODEL_NAME

# BASE_URL="http://127.0.0.1:12345/v1"
# MODEL_NAME="qwen3.6-27b@q6_k"
# RECONSTRUCTION_VALIDATOR_BASE_URL="http://127.0.0.1:12345/v1"
# RECONSTRUCTION_VALIDATOR_MODEL_NAME="qwen3.6-27b@q6_k"

DEFAULT_CONCURRENCY = 128
MAX_CURRENT_TASKS = 512
MAX_TOKENS = 8192
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
RECONSTRUCTION_VALIDATOR_WINDOW_SIZE = 3
RECONSTRUCTION_TOKEN_WARNING_LIMIT = 200


def _write_reconstruction_token_warning(message: str) -> None:
    if SHOW_TQDM_BAR:
        tqdm.write(message)
    else:
        print(message)


def _summarize_token_counts(values: list[int]) -> dict[str, int | float]:
    sorted_values = sorted(values)
    n = len(sorted_values)
    return {
        "n": n,
        "min": sorted_values[0],
        "p50": sorted_values[n // 2],
        "mean": round(sum(sorted_values) / n, 1),
        "p95": sorted_values[min(n - 1, int(n * 0.95))],
        "max": sorted_values[-1],
    }


def collect_reconstruction_token_stats(current_task_units_by_output_path: dict[Path, set[tuple[str, str]]]) -> dict[str, list[int]]:
    stats_by_lang: dict[str, list[int]] = {}
    for output_path, current_task_units in current_task_units_by_output_path.items():
        if not current_task_units:
            continue
        if not output_path.exists():
            continue
        with output_path.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = PipelineRecord(**json.loads(line))
                for tgt_lang_code, branch in sorted(record.target.languages.items()):
                    if (record.uid, tgt_lang_code) not in current_task_units:
                        continue
                    reconstruction_text = branch.artifacts.reconstruction.text
                    if not reconstruction_text:
                        continue
                    token_count = len(
                        tokenize(
                            language=tgt_lang_code,
                            raw_text=reconstruction_text,
                            indexing=False,
                        )
                    )
                    stats_by_lang.setdefault(tgt_lang_code, []).append(token_count)
                    if token_count > RECONSTRUCTION_TOKEN_WARNING_LIMIT:
                        _write_reconstruction_token_warning(
                            "TOKEN_COUNT_WARNING "
                            f"pipeline=6 uid={record.uid} target={tgt_lang_code} "
                            f"tokens={token_count} limit={RECONSTRUCTION_TOKEN_WARNING_LIMIT} "
                            f"file={output_path}"
                        )
    return stats_by_lang


def print_reconstruction_token_summary(stats_by_lang: dict[str, list[int]]) -> None:
    print()
    print("=== Pipeline 6: Reconstruction token statistics ===")
    print("token_warning_limit:", RECONSTRUCTION_TOKEN_WARNING_LIMIT)
    if not stats_by_lang:
        print("No reconstruction text found.")
        return
    for lang_code in sorted(stats_by_lang):
        summary = _summarize_token_counts(stats_by_lang[lang_code])
        print(
            f"{lang_code}: "
            f"n={summary['n']} "
            f"min={summary['min']} "
            f"p50={summary['p50']} "
            f"mean={summary['mean']} "
            f"p95={summary['p95']} "
            f"max={summary['max']}"
        )

def load_input_cache_by_shard() -> list[tuple[Path, list[PipelineRecord]]]:
    items: list[tuple[Path, list[PipelineRecord]]] = []
    for jsonl_path in sorted(INPUT_CACHE_BASE.rglob("*.jsonl")):
        records: list[PipelineRecord] = []
        with jsonl_path.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                records.append(PipelineRecord(**json.loads(line)))
        items.append((jsonl_path, records))
    return items
async def main() -> None:
    if not BASE_URL or not API_KEY:
        raise RuntimeError("OPEN_ROUTER_BASE_URL / OPEN_ROUTER_API_KEY must be set")

    llm = LLM(
        model_name=MODEL_NAME,
        base_url=BASE_URL,
        api_key=API_KEY,
        batch_size=DEFAULT_CONCURRENCY,
    )
    reconstruction_validator_llm = LLM(
        model_name=RECONSTRUCTION_VALIDATOR_MODEL_NAME,
        base_url=RECONSTRUCTION_VALIDATOR_BASE_URL,
        api_key=API_KEY,
        batch_size=DEFAULT_CONCURRENCY,
    )

    prerequisite_cache_parts = load_input_cache_by_shard()
    reconstruction_runner = TranslationReconstructionRunner(
        llm=llm,
        reconstruction_validator_llm=reconstruction_validator_llm,
        reconstruction_validator_window_size=RECONSTRUCTION_VALIDATOR_WINDOW_SIZE,
        concurrency=DEFAULT_CONCURRENCY,
        max_retries=MAX_RETRIES,
    )
    total_units = 0
    existing_finished = 0
    candidate_total = 0
    current_task_units_by_output_path: dict[Path, set[tuple[str, str]]] = {}
    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        output_path = reconstruction_output_path_from_input_cache(OUTPUT_BASE, INPUT_CACHE_BASE, input_cache_path)
        existing_output_by_uid = load_pipeline_records_by_uid(output_path)
        candidate_records, _ = reconstruction_runner.filter_reconstruction_candidates(prerequisite_records)
        candidate_total += len(candidate_records)
        for record in candidate_records:
            existing_record = existing_output_by_uid.get(record.uid)
            source_record = existing_record or record
            target_codes = reconstruction_runner._prerequisite_target_language_codes(source_record)
            total_units += len(target_codes)
            pending_codes = reconstruction_runner._pending_target_language_codes(source_record)
            if pending_codes:
                current_task_units_by_output_path.setdefault(output_path, set()).update(
                    (record.uid, code) for code in pending_codes
                )
            if existing_record:
                existing_finished += sum(
                    1
                    for code in target_codes
                    if reconstruction_runner.branch_status(existing_record, code) == "finished"
                )

    reconstruction_runner.reset_progress(
        show_tqdm_bar=SHOW_TQDM_BAR,
        total=total_units,
        desc="Processing...",
        initial=existing_finished,
    )

    print("=== Pipeline 6: Translation reconstruction ===")
    print("records:", candidate_total)
    print("output_dir_name:", OUTPUT_BASE.name)
    print("input_cache_dir_name:", INPUT_CACHE_BASE.name)
    print("concurrency:", DEFAULT_CONCURRENCY)
    print("max_retries:", MAX_RETRIES)
    print("max_tokens:", MAX_TOKENS)
    print("temperature:", TEMPERATURE)
    print("top_p:", TOP_P)
    print("reconstruction_validator_model_name:", RECONSTRUCTION_VALIDATOR_MODEL_NAME)
    print("reconstruction_validator_window_size_pure_windows:", RECONSTRUCTION_VALIDATOR_WINDOW_SIZE)
    print("extra_body:", EXTRA_BODY)
    print("enable_visualization:", ENABLE_VISUALIZATION)
    print("show_tqdm_bar:", SHOW_TQDM_BAR)
    print("max_current_tasks:", MAX_CURRENT_TASKS)
    print("reconstruction_token_warning_limit:", RECONSTRUCTION_TOKEN_WARNING_LIMIT)
    print()

    summaries = []
    output_paths = []
    for input_cache_path, prerequisite_records in prerequisite_cache_parts:
        output_path = reconstruction_output_path_from_input_cache(OUTPUT_BASE, INPUT_CACHE_BASE, input_cache_path)
        summary = await reconstruction_runner.run_cache_shard(
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
        # print(f"cache: {input_cache_path.name} -> {summary['output_label']}")
        # print("existing_finished:", summary["existing_finished"])
        # print("pending:", summary["pending"])
        # print("shard_summary:", summary)
        # print()
        summaries.append(summary)
        output_paths.append(output_path)

    reconstruction_token_stats = collect_reconstruction_token_stats(current_task_units_by_output_path)
    reconstruction_runner.close_progress()
    print_llm_pipeline_summary(
        title="Pipeline 6: Translation reconstruction",
        summaries=summaries,
        output_paths=output_paths,
        stage="translation_reconstruction",
    )
    print_reconstruction_token_summary(reconstruction_token_stats)


if __name__ == "__main__":
    asyncio.run(main())