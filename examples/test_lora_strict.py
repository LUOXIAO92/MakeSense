"""Run standalone strict streaming tests for a MakeSense LoRA adapter.

This entrypoint intentionally does not import or modify ``examples/train_lora.py``.
Keep the dataset sampling constants below in sync with the training script when
you need the standalone run to select the same strict-test samples.
"""

import json
import os
import sys
from pathlib import Path

sys.path.append("src")
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True,garbage_collection_threshold:0.9")

import torch
from peft import PeftModel
from transformers import AutoModelForMultimodalLM, AutoProcessor, BitsAndBytesConfig

from data_loader.dataset import build_training_dataset
from train import TrainingDataConfig, prepare_multimodal_model_for_kbit_lora_training
from train.lora_trainer import _build_train_validate_test_rows
from train.tester import StreamingSampleTester, format_test_outputs_markdown, print_test_summary


# --- Dataset controls: keep these identical to examples/train_lora.py ---
DATASET_ROOT = Path(os.environ["DATASET"]) / "audio" / "StreamingTranslation" / "Emilia-Dataset"
TOTAL_SAMPLES: int | None = None
MAX_WINDOW_SIZE = -1
SEED = 4021
DATASET_REPEAT = 2
TASK_RATIO: tuple[float, float] = (9, 1)
SPLIT_RATIO: tuple[float, float, float] = (0.8975, 0.1, 0.0025)
TRANSLATION_TASK_CONFIG = {
    "natural":      {"ratio": 2},
    "fixed_window": {"ratio": 4, "min": 1, "max": 10},
    "conservative": {"ratio": 4, "min": 1, "max": 10},
}


# --- Model / adapter controls ---
MODEL_NAME = "google/gemma-4-E2B-it"
ADAPTER_PATH: str | Path = Path("outputs") / "makesense_lora_gemma-4-E2B-it_3e-4_r16_adamw_bs16" / "checkpoint-4500"
LOAD_IN_4BIT = True
AUDIO_SAMPLING_RATE = 16000
AUDIO_CHUNK_SECONDS = 1.0
ASSISTANT_HEADER = "<|turn>model\n"
ASSISTANT_END = "<turn|>"
GENERATION_STOP = "<turn|>"


# --- Strict-test controls ---
TEST_MAX_NEW_TOKENS = 256
TEST_RECORD_COUNT = -1
TEST_BATCH_SIZE = 1
TEST_CUDA_EMPTY_CACHE_STEPS: int | None = None
TEST_OUTPUT_MARKDOWN = True
TEST_OUTPUT_PATH: Path | None = Path("outputs") / "standalone_lora_strict_test_3e-4_r16_adamw_bs16_step4500_testbs1_fixed_temp1.md"
GENERATION_DO_SAMPLE: bool | None = True
GENERATION_TEMPERATURE: float | None = 1
GENERATION_TOP_P: float | None = 0.95
GENERATION_TOP_K: int | None = 20


def make_data_config() -> TrainingDataConfig:
    return TrainingDataConfig(
        dataset_root=DATASET_ROOT,
        total_samples=TOTAL_SAMPLES,
        max_window_size=MAX_WINDOW_SIZE,
        task_ratio=TASK_RATIO,
        split_ratio=SPLIT_RATIO,
        translation_task_config=TRANSLATION_TASK_CONFIG,
        dataset_repeat=DATASET_REPEAT,
        seed=SEED,
    )


def load_processor():
    return AutoProcessor.from_pretrained(MODEL_NAME, trust_remote_code=True, dtype=torch.bfloat16)


def load_base_model():
    quantization_config = None
    if LOAD_IN_4BIT:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
            llm_int8_skip_modules=[
                "lm_head",
                "audio_tower",
                "embed_audio",
                "model.audio_tower",
                "model.embed_audio",
            ],
        )
    base_model = AutoModelForMultimodalLM.from_pretrained(
        MODEL_NAME,
        dtype=torch.bfloat16,
        device_map="auto",
        quantization_config=quantization_config,
        trust_remote_code=True,
        attn_implementation="sdpa",
    )
    if LOAD_IN_4BIT:
        base_model = prepare_multimodal_model_for_kbit_lora_training(base_model)
    return base_model


def load_lora_model():
    return PeftModel.from_pretrained(load_base_model(), str(ADAPTER_PATH))


def build_test_rows(data_config: TrainingDataConfig) -> list[dict[str, object]]:
    splits = build_training_dataset(
        data_config.dataset_root,
        total_samples=data_config.total_samples,
        max_window_size=data_config.max_window_size,
        task_ratio=data_config.task_ratio,
        split_ratio=data_config.split_ratio,
        translation_task_config=data_config.translation_task_config,
        dataset_repeat=data_config.dataset_repeat,
        seed=data_config.seed,
    )
    _, _, test_rows = _build_train_validate_test_rows(splits)
    return test_rows


def main() -> None:
    data_config = make_data_config()
    processor = load_processor()
    model = load_lora_model()
    tester = StreamingSampleTester(
        processor=processor,
        test_rows=build_test_rows(data_config),
        audio_sampling_rate=AUDIO_SAMPLING_RATE,
        audio_chunk_seconds=AUDIO_CHUNK_SECONDS,
        test_max_new_tokens=TEST_MAX_NEW_TOKENS,
        test_record_count=TEST_RECORD_COUNT,
        test_batch_size=TEST_BATCH_SIZE,
        test_cuda_empty_cache_steps=TEST_CUDA_EMPTY_CACHE_STEPS,
        generation_stop=GENERATION_STOP,
        enable_thinking=False,
        generation_do_sample=GENERATION_DO_SAMPLE,
        generation_temperature=GENERATION_TEMPERATURE,
        generation_top_p=GENERATION_TOP_P,
        generation_top_k=GENERATION_TOP_K,
    )
    summary = tester.evaluate(model=model, step=0, metrics={})
    print_test_summary(summary)
    if TEST_OUTPUT_MARKDOWN and TEST_OUTPUT_PATH is not None:
        TEST_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        TEST_OUTPUT_PATH.write_text(
            format_test_outputs_markdown(summary, title="Standalone LoRA Strict Test"),
            encoding="utf-8",
        )
        print(f"\nWrote strict-test markdown to {TEST_OUTPUT_PATH}")
    print("\nStrict-test metrics JSON")
    print(json.dumps(summary["test_metrics"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()