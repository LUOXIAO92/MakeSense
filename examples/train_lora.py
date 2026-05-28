"""Train a MakeSense LoRA adapter from final pipeline-9 dataset output."""

import sys
sys.path.append("src")

from pathlib import Path

import torch
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForMultimodalLM, AutoProcessor, BitsAndBytesConfig

from train import LoraTrainConfig, TrainingDataConfig, train_lora


# --- Dataset controls ---
DATASET_ROOT = Path("dataset_test")
TOTAL_SAMPLES: int | None = None
TASK_RATIO: tuple[float, float] = (9, 1)
SPLIT_RATIO: tuple[float, float, float] = (8, 1.5, 0.5)
TOLERANCE_WINDOW: int | None = None
SEED = 4021


# --- Model / LoRA controls ---
MODEL_NAME = "google/gemma-4-E2B-it"
OUTPUT_DIR = Path("outputs") / "makesense_lora"
MAX_SEQ_LENGTH = 32000
LOAD_IN_4BIT = True
AUDIO_SAMPLING_RATE = 16000
AUDIO_CHUNK_SECONDS = 1.0

LORA_R = 16
LORA_ALPHA = 16
LORA_DROPOUT = 0.0
LORA_TARGET_MODULES = (
    r"^model\.language_model\.layers\.\d+\."
    r"(self_attn\.(q_proj|k_proj|v_proj|o_proj)|"
    r"mlp\.(gate_proj|up_proj|down_proj))$"
)


# --- Trainer controls ---
LEARNING_RATE = 2e-4
WEIGHT_DECAY = 0.0
NUM_TRAIN_EPOCHS = 1
MAX_STEPS = -1
PER_DEVICE_TRAIN_BATCH_SIZE = 1
GRADIENT_ACCUMULATION_STEPS = 8
WARMUP_STEPS = 5
LOGGING_STEPS = 1
EVAL_STEPS = 100
SAVE_STEPS = 500
MAX_GRAD_NORM = 1.0
SAMPLE_GENERATION_STEPS = 12
SAMPLE_GENERATION_MAX_NEW_TOKENS = 256
SAMPLE_EVALUATION_RECORD_COUNT = 1


def load_model_and_processor():
    """Load the target model/processor and attach PEFT LoRA."""

    processor = AutoProcessor.from_pretrained(MODEL_NAME, trust_remote_code=True, dtype=torch.bfloat16)
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
    model = AutoModelForMultimodalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        quantization_config=quantization_config,
        trust_remote_code=True,
    )
    if LOAD_IN_4BIT:
        model = prepare_model_for_kbit_training(model)
    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=LORA_TARGET_MODULES,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    return model, processor


def main() -> None:
    data_config = TrainingDataConfig(
        dataset_root=DATASET_ROOT,
        total_samples=TOTAL_SAMPLES,
        task_ratio=TASK_RATIO,
        split_ratio=SPLIT_RATIO,
        tolerance_window=TOLERANCE_WINDOW,
        seed=SEED,
    )
    train_config = LoraTrainConfig(
        output_dir=OUTPUT_DIR,
        max_seq_length=MAX_SEQ_LENGTH,
        audio_sampling_rate=AUDIO_SAMPLING_RATE,
        audio_chunk_seconds=AUDIO_CHUNK_SECONDS,
        learning_rate=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY,
        num_train_epochs=NUM_TRAIN_EPOCHS,
        max_steps=MAX_STEPS,
        per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        warmup_steps=WARMUP_STEPS,
        logging_steps=LOGGING_STEPS,
        eval_steps=EVAL_STEPS,
        save_steps=SAVE_STEPS,
        max_grad_norm=MAX_GRAD_NORM,
        sample_generation_steps=SAMPLE_GENERATION_STEPS,
        sample_generation_max_new_tokens=SAMPLE_GENERATION_MAX_NEW_TOKENS,
        sample_evaluation_record_count=SAMPLE_EVALUATION_RECORD_COUNT,
        seed=SEED,
    )
    model, processor = load_model_and_processor()
    train_lora(model=model, processor=processor, data_config=data_config, train_config=train_config)


if __name__ == "__main__":
    main()
