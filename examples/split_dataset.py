"""Create a reusable metadata-level train/validate/test split manifest."""

import json
import os
import sys
from pathlib import Path

sys.path.append("src")

from data_loader import write_dataset_split_manifest


# --- Dataset controls: keep these identical to examples/train_lora.py ---
DATASET_ROOT = Path(os.environ["DATASET"]) / "audio" / "StreamingTranslation" / "Emilia-Dataset"
# DATASET_ROOT = Path("dataset_test")
TOTAL_SAMPLES: int | None = None
SEED = 4021
SPLIT_RATIO: tuple[float, float, float] = (0.8975, 0.1, 0.0025)


# --- Output controls ---
OUTPUT_JSON_PATH = Path("outputs") / "dataset_splits" / "emilia_metadata_split_seed4021.json"


def main() -> None:
    payload = write_dataset_split_manifest(
        OUTPUT_JSON_PATH,
        DATASET_ROOT,
        total_samples=TOTAL_SAMPLES,
        split_ratio=SPLIT_RATIO,
        seed=SEED,
    )
    print(f"Wrote split manifest: {OUTPUT_JSON_PATH}")
    print(json.dumps(payload["counts"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
