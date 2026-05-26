"""Train a MakeSense LoRA adapter from final pipeline-9 dataset output."""
import sys
sys.path.append("src")
from pathlib import Path

from unsloth import FastModel
from transformers import Qwen2_5OmniProcessor

from train import LoraTrainConfig, TrainingDataConfig, train_lora


# --- Dataset controls ---
DATASET_ROOT = Path("dataset_test")
TOTAL_SAMPLES: int | None = None
TASK_RATIO: tuple[float, float] = (9, 1)
SPLIT_RATIO: tuple[float, float, float] = (8, 1.5, 0.5)
TOLERANCE_WINDOW: int | None = None
SEED = 4021


# --- Model / LoRA controls ---
MODEL_NAME = "Qwen/Qwen2.5-Omni-3B"
OUTPUT_DIR = Path("outputs") / "makesense_lora"
MAX_SEQ_LENGTH = 8192
LOAD_IN_4BIT = True

LORA_R = 16
LORA_ALPHA = 16
LORA_DROPOUT = 0.0
LORA_TARGET_MODULES = (
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
)


# --- Optimizer / loop controls ---
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
ASSISTANT_ONLY_LOSS = True
PACKING = False
OPTIM = "adamw_8bit"
REPORT_TO = "none"
PRINT_SAMPLE = True
TRAINING_MODE = "text_only"


def load_model_and_processor():
    """Load Qwen2.5-Omni with Unsloth FastModel and explicit processor."""

    model, _ = FastModel.from_pretrained(
        model_name=MODEL_NAME,
        max_seq_length=MAX_SEQ_LENGTH,
        dtype=None,
        load_in_4bit=LOAD_IN_4BIT,
    )
    processor = Qwen2_5OmniProcessor.from_pretrained(MODEL_NAME)
    model = FastModel.get_peft_model(
        model,
        r=LORA_R,
        target_modules=list(LORA_TARGET_MODULES),
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=SEED,
    )
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
        assistant_only_loss=ASSISTANT_ONLY_LOSS,
        packing=PACKING,
        optim=OPTIM,
        report_to=REPORT_TO,
        print_sample=PRINT_SAMPLE,
        training_mode=TRAINING_MODE,
        seed=SEED,
    )
    model, processor = load_model_and_processor()
    train_lora(model=model, processor=processor, data_config=data_config, train_config=train_config)


if __name__ == "__main__":
    main()
