"""Train a MakeSense LoRA adapter from final pipeline-9 dataset output."""

import os
import sys
sys.path.append("src")
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True,garbage_collection_threshold:0.9" 
# os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "backend:cudaMallocAsync"

import warnings

warnings.filterwarnings(
    "ignore",
    message=r".*_check_is_size will be removed in a future PyTorch release.*",
    category=FutureWarning,
    module=r"bitsandbytes\.backends\.cuda\.ops",
)

from pathlib import Path

import torch
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForMultimodalLM, AutoProcessor, BitsAndBytesConfig

from train import LoraTrainConfig, TrainingDataConfig, prepare_multimodal_model_for_kbit_lora_training, train_lora
from train.continue_utils import prepare_lora_model_for_continue, resolve_continue_plan




# --- Dataset controls ---
DATASET_ROOT = Path(os.environ["DATASET"]) /"audio"/"StreamingTranslation"/"Emilia-Dataset"
# DATASET_ROOT = Path("dataset_test")
TOTAL_SAMPLES: int | None = None
MAX_WINDOW_SIZE = -1
SEED = 4021

# Dataset sampling group: repeat the source record pool, then shuffle and assign
# task labels. `TASK_RATIO` is (translation, asr), and `SPLIT_RATIO` is (train, validate, test).
DATASET_REPEAT = 12
TASK_RATIO: tuple[float, float] = (9, 1)
SPLIT_RATIO: tuple[float, float, float] = (0.8975, 0.1, 0.0025)

# Translation-subtask sampling group: used only after a sample is assigned to the
# translation task. The three ratio values are normalized together. For
# fixed_window/conservative, min=None means 1.
TRANSLATION_TASK_CONFIG = {
    "natural":      {"ratio": 2},
    "fixed_window": {"ratio": 4, "min": 1, "max": 10},
    "conservative": {"ratio": 4, "min": 1, "max": 10},
}


# --- Output / checkpoint controls ---
OUTPUT_DIR = Path("outputs") / "makesense_lora_gemma-4-E2B-it_1.5e-4_r16_adamw_bs16_repeat12"
CONTINUE_TYPE = "resume"  # "none" | "resume" | "branch"
CHECKPOINT_PATH: str | Path | None = None # "outputs/makesense_lora1/checkpoint-100"
SAVE_PROCESSOR = False


# --- Model / LoRA controls ---
MODEL_NAME = "google/gemma-4-E2B-it"
LOAD_IN_4BIT = True
AUDIO_SAMPLING_RATE = 16000
AUDIO_CHUNK_SECONDS = 1.0
ASSISTANT_HEADER = "<|turn>model\n"
ASSISTANT_END = "<turn|>"
GENERATION_STOP = "<turn|>"

LORA_R = 16
LORA_ALPHA = 16
LORA_DROPOUT = 0.0
LORA_TARGET_MODULES = (
    r"^model\.language_model\.layers\.\d+\."
    r"(self_attn\.(q_proj|k_proj|v_proj|o_proj)|"
    r"mlp\.(gate_proj|up_proj|down_proj))$"
)


# --- Trainer controls ---
LEARNING_RATE = 1.5e-4
WEIGHT_DECAY = 0.0
OPTIMIZER = "adamw"  # "adamw" | "adamw8bit"
ADAM_BETA1 = 0.9
ADAM_BETA2 = 0.999
LR_SCHEDULER_TYPE = "linear"  # "linear" | "cosine" | "constant" | "constant_with_warmup"
MAX_GRAD_NORM = 1.0
NUM_TRAIN_EPOCHS = 1
MAX_STEPS = -1
PER_DEVICE_TRAIN_BATCH_SIZE = 2
PER_DEVICE_EVAL_BATCH_SIZE = 2
GRADIENT_ACCUMULATION_STEPS = 8
WARMUP_STEPS = 0.05 #int(0.01 * 24000 * DATASET_REPEAT * SPLIT_RATIO[0] * NUM_TRAIN_EPOCHS / GRADIENT_ACCUMULATION_STEPS)
LOGGING_STEPS = 1
EVAL_ACCUMULATION_STEPS = 1
EVAL_STEPS = 300
SAVE_STEPS = 300
TEST_STEPS = 300
TEST_MAX_NEW_TOKENS = 256
TEST_RECORD_COUNT = -1
TEST_BATCH_SIZE = 1
TEST_OUTPUT_MARKDOWN = True
CUDA_EMPTY_CACHE_STEPS: int | None = None
TEST_CUDA_EMPTY_CACHE_STEPS: int | None = None


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
        attn_implementation="sdpa"
    )
    if LOAD_IN_4BIT:
        base_model = prepare_multimodal_model_for_kbit_lora_training(base_model)
    return base_model


def attach_fresh_lora(base_model):
    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=LORA_TARGET_MODULES,
    )
    model = get_peft_model(base_model, lora_config)
    model.print_trainable_parameters()
    return model


def main() -> None:
    data_config = TrainingDataConfig(
        dataset_root=DATASET_ROOT,
        total_samples=TOTAL_SAMPLES,
        max_window_size=MAX_WINDOW_SIZE,
        task_ratio=TASK_RATIO,
        split_ratio=SPLIT_RATIO,
        translation_task_config=TRANSLATION_TASK_CONFIG,
        dataset_repeat=DATASET_REPEAT,
        seed=SEED,
    )
    continue_plan = resolve_continue_plan(
        continue_type=CONTINUE_TYPE,
        checkpoint_path=CHECKPOINT_PATH,
        output_dir=OUTPUT_DIR,
    )
    train_config = LoraTrainConfig(
        output_dir=OUTPUT_DIR,
        audio_sampling_rate=AUDIO_SAMPLING_RATE,
        audio_chunk_seconds=AUDIO_CHUNK_SECONDS,
        learning_rate=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY,
        optimizer=OPTIMIZER,
        adam_beta1=ADAM_BETA1,
        adam_beta2=ADAM_BETA2,
        lr_scheduler_type=LR_SCHEDULER_TYPE,
        num_train_epochs=NUM_TRAIN_EPOCHS,
        max_steps=MAX_STEPS,
        per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
        per_device_eval_batch_size=PER_DEVICE_EVAL_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        warmup_steps=WARMUP_STEPS,
        logging_steps=LOGGING_STEPS,
        eval_steps=EVAL_STEPS,
        eval_accumulation_steps=EVAL_ACCUMULATION_STEPS,
        save_steps=SAVE_STEPS,
        max_grad_norm=MAX_GRAD_NORM,
        test_steps=TEST_STEPS,
        test_max_new_tokens=TEST_MAX_NEW_TOKENS,
        test_record_count=TEST_RECORD_COUNT,
        test_batch_size=TEST_BATCH_SIZE,
        test_cuda_empty_cache_steps=TEST_CUDA_EMPTY_CACHE_STEPS,
        test_output_markdown=TEST_OUTPUT_MARKDOWN,
        cuda_empty_cache_steps=CUDA_EMPTY_CACHE_STEPS,
        assistant_header=ASSISTANT_HEADER,
        assistant_end=ASSISTANT_END,
        generation_stop=GENERATION_STOP,
        save_processor=SAVE_PROCESSOR,
        continue_type=CONTINUE_TYPE,
        checkpoint_path=CHECKPOINT_PATH,
        continue_plan=continue_plan,
        model_name=MODEL_NAME,
        seed=SEED,
    )
    processor = load_processor()
    model = prepare_lora_model_for_continue(
        continue_plan=continue_plan,
        base_model_factory=load_base_model,
        fresh_lora_factory=attach_fresh_lora,
    )
    train_lora(model=model, processor=processor, data_config=data_config, train_config=train_config)


if __name__ == "__main__":
    main()
