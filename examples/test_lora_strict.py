"""Run runtime strict streaming tests through an OpenAI-compatible API.

This entrypoint intentionally stays thin: endpoint rollout, concurrent API
execution, metrics, and Markdown formatting live in ``src/eval_runtime``.
"""

import os
import sys
from pathlib import Path

sys.path.append("src")

from eval_runtime import OpenAIStrictTestConfig, StrictStyleSpec, run_openai_strict_test


# --- Dataset controls: keep these identical to examples/train_lora.py ---
DATASET_ROOT = Path(os.environ["DATASET"]) / "audio" / "StreamingTranslation" / "Emilia-Dataset"
TOTAL_SAMPLES: int | None = None
MAX_WINDOW_SIZE = -1
SEED = 4021
SPLIT_RATIO: tuple[float, float, float] = (0.8975, 0.1, 0.0025)
TEST_SPLITS = ("test",)


# --- OpenAI-compatible endpoint controls ---
MODEL_NAME = "gemma-4-E2B-it-lora"
BASE_URL = "http://127.0.0.1:18000/v1"
API_KEY = os.environ.get("OPENAI_API_KEY", "no-key")
CONCURRENCY = 90
CONSTRAINED_DECODING = False
REQUEST_TIMEOUT: float | None = None


# --- Runtime multimodal request controls ---
AUDIO_SAMPLING_RATE = 16000
AUDIO_CHUNK_SECONDS = 1.0
AUDIO_MESSAGE_FORMAT = "input_audio"  # "input_audio" or "audio_url"


# --- Generation controls ---
TEST_MAX_NEW_TOKENS = 256
GENERATION_DO_SAMPLE: bool | None = False
GENERATION_TEMPERATURE: float | None = None
GENERATION_TOP_P: float | None = None
GENERATION_TOP_K: int | None = None
EXTRA_BODY = {"top_k": GENERATION_TOP_K} if GENERATION_TOP_K is not None else None


# --- Strict runtime test controls ---
TEST_RECORD_COUNT = -1
STRICT_TRANSLATION_STYLES = (
    StrictStyleSpec("asr", (None,)),
    StrictStyleSpec("natural", (None,)),
    StrictStyleSpec("fixed_window", (1, 2, 4, 6, 8, 10)),
    StrictStyleSpec("conservative", (1, 2, 4, 6, 8, 10)),
)
STRICT_TEST_OUTPUT_DIR = Path("outputs") / "strict_test" / f"gemma-4-E2B-it_1e-4_r16_adamw_bs16_rep12_epo1_conc{CONCURRENCY}"
METRICS_OUTPUT_DIR: Path | None = STRICT_TEST_OUTPUT_DIR / "metrics"
MARKDOWN_OUTPUT_DIR: Path | None = STRICT_TEST_OUTPUT_DIR / "markdown"
MARKDOWN_RECORD_LIMIT_PER_CONDITION = 100


def main() -> None:
    run_openai_strict_test(
        OpenAIStrictTestConfig(
            dataset_root=DATASET_ROOT,
            model_name=MODEL_NAME,
            base_url=BASE_URL,
            api_key=API_KEY,
            total_samples=TOTAL_SAMPLES,
            max_window_size=MAX_WINDOW_SIZE,
            seed=SEED,
            split_ratio=SPLIT_RATIO,
            splits=TEST_SPLITS,
            style_specs=STRICT_TRANSLATION_STYLES,
            test_record_count=TEST_RECORD_COUNT,
            concurrency=CONCURRENCY,
            constrained_decoding=CONSTRAINED_DECODING,
            audio_sampling_rate=AUDIO_SAMPLING_RATE,
            audio_chunk_seconds=AUDIO_CHUNK_SECONDS,
            audio_message_format=AUDIO_MESSAGE_FORMAT,
            max_tokens=TEST_MAX_NEW_TOKENS,
            temperature=GENERATION_TEMPERATURE if GENERATION_DO_SAMPLE else 0,
            top_p=GENERATION_TOP_P,
            extra_body=EXTRA_BODY,
            metrics_output_dir=METRICS_OUTPUT_DIR,
            markdown_output_dir=MARKDOWN_OUTPUT_DIR,
            markdown_record_limit_per_condition=MARKDOWN_RECORD_LIMIT_PER_CONDITION,
            request_timeout=REQUEST_TIMEOUT,
        )
    )


if __name__ == "__main__":
    main()
