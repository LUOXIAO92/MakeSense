"""Run vLLM Docker strict tests for every LoRA checkpoint.

This wrapper starts one vLLM Docker container per checkpoint, runs the existing
runtime strict tester, stops the container, waits for GPU memory cooldown, and
writes a compact checkpoint summary.
"""

import os
import sys
from pathlib import Path

sys.path.append("src")

from eval_runtime import (  # noqa: E402
    OpenAIStrictTestConfig,
    StrictStyleSpec,
    VLLMDockerServeConfig,
    VLLMStrictBatchConfig,
    run_vllm_strict_checkpoint_batch,
)


# --- Dataset controls: keep these identical to examples/train_lora.py ---
DATASET_ROOT = Path(os.environ["DATASET"]) / "audio" / "StreamingTranslation" / "Emilia-Dataset"
TOTAL_SAMPLES: int | None = None
MAX_WINDOW_SIZE = -1
SEED = 4021
SPLIT_RATIO: tuple[float, float, float] = (0.8975, 0.1, 0.0025)
TEST_SPLITS = ("test",)


# --- Training / checkpoint controls ---
TRAINING_OUTPUT_DIR = Path("outputs") / "makesense_lora_gemma-4-E2B-it_1e-4_r16_adamw_bs16_repeat12_epoch1"
LORA_ROOT = TRAINING_OUTPUT_DIR
CHECKPOINT_STEPS: tuple[int, ...] | None = None


# --- OpenAI-compatible endpoint controls ---
API_MODEL_NAME = "gemma-4-E2B-it-lora"
SERVE_PORT = 18000
BASE_URL = f"http://127.0.0.1:{SERVE_PORT}/v1"
API_KEY = os.environ.get("OPENAI_API_KEY", "no-key")
CONCURRENCY = 90
CONSTRAINED_DECODING = False
REQUEST_TIMEOUT: float | None = None


# --- vLLM Docker controls ---
DOCKER_IMAGE = "vllm/vllm-omni:v0.22.0"
DOCKER_RUN_ARGS = (
    "--runtime",
    "nvidia",
    "--gpus",
    "all",
    "--rm",
    "--ipc=host",
)
MODEL_MOUNT_SOURCE = Path(os.environ["MODELS"]) / "LLM"
MODEL_MOUNT_TARGET = "/models"
BASE_MODEL_PATH = "/models/google/gemma-4-E2B-it"
LORA_MOUNT_TARGET = "/lora"
SERVED_MODEL_NAME = "gemma-4-E2B-it"
LORA_MODEL_NAME = API_MODEL_NAME
SERVE_HOST = "0.0.0.0"
CONTAINER_PORT = 8000
CONTAINER_NAME_PREFIX = "makesense-vllm"
VLLM_SERVE_ARGS = (
    "--quantization", "bitsandbytes",
    "--max-lora-rank", "16",
    "--trust-remote-code",
    "--skip-mm-profiling",
    "--max-num-batched-tokens", "16384",
    "--gpu-memory-utilization", "0.80",
    "--max-model-len", "10000",
    "--max-num-seqs", str(CONCURRENCY),
)
DOCKER_COOLDOWN_SECONDS = 20.0
READINESS_TIMEOUT_SECONDS = 900.0
READINESS_POLL_SECONDS = 5.0
SMOKE_TEST_ENABLED = True
SMOKE_TEST_MESSAGES = ({"role": "user", "content": "Say ok."},)
SMOKE_TEST_MAX_TOKENS = 4
SMOKE_TEST_TIMEOUT_SECONDS: float | None = 60.0


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
STRICT_TEST_RUN_NAME = f"gemma-4-E2B-it_1e-4_r16_adamw_bs16_rep12_epo1_conc{CONCURRENCY}"
STRICT_TEST_OUTPUT_ROOT = Path("outputs") / "strict_test"
MARKDOWN_RECORD_LIMIT_PER_CONDITION = 100


def _strict_test_config() -> OpenAIStrictTestConfig:
    return OpenAIStrictTestConfig(
        dataset_root=DATASET_ROOT,
        model_name=API_MODEL_NAME,
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
        markdown_record_limit_per_condition=MARKDOWN_RECORD_LIMIT_PER_CONDITION,
        request_timeout=REQUEST_TIMEOUT,
    )


def _docker_config() -> VLLMDockerServeConfig:
    return VLLMDockerServeConfig(
        docker_image=DOCKER_IMAGE,
        docker_run_args=DOCKER_RUN_ARGS,
        model_mount_source=MODEL_MOUNT_SOURCE,
        model_mount_target=MODEL_MOUNT_TARGET,
        base_model_path=BASE_MODEL_PATH,
        lora_mount_target=LORA_MOUNT_TARGET,
        served_model_name=SERVED_MODEL_NAME,
        lora_model_name=LORA_MODEL_NAME,
        serve_host=SERVE_HOST,
        serve_port=SERVE_PORT,
        container_port=CONTAINER_PORT,
        vllm_serve_args=VLLM_SERVE_ARGS,
        container_name_prefix=CONTAINER_NAME_PREFIX,
    )


def main() -> None:
    run_vllm_strict_checkpoint_batch(
        VLLMStrictBatchConfig(
            strict_test_config=_strict_test_config(),
            docker=_docker_config(),
            training_output_dir=TRAINING_OUTPUT_DIR,
            lora_root=LORA_ROOT,
            strict_test_output_root=STRICT_TEST_OUTPUT_ROOT,
            strict_test_run_name=STRICT_TEST_RUN_NAME,
            checkpoint_steps=CHECKPOINT_STEPS,
            docker_cooldown_seconds=DOCKER_COOLDOWN_SECONDS,
            readiness_timeout_seconds=READINESS_TIMEOUT_SECONDS,
            readiness_poll_seconds=READINESS_POLL_SECONDS,
            smoke_test_enabled=SMOKE_TEST_ENABLED,
            smoke_test_messages=SMOKE_TEST_MESSAGES,
            smoke_test_max_tokens=SMOKE_TEST_MAX_TOKENS,
            smoke_test_timeout_seconds=SMOKE_TEST_TIMEOUT_SECONDS,
        )
    )


if __name__ == "__main__":
    main()
