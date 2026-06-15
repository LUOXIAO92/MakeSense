"""Plot LoRA strict-test metrics from a ``test_metrics.json`` file.

The training callback writes historical strict-test summaries to
``OUTPUT_DIR/test_metrics.json``. This helper reads that file and renders the
main protocol / wait / release rates as a PNG image.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


METRICS_JSON = Path("outputs/makesense_lora_gemma-4-E2B-it_3e-4_r16_adamw_bs16/test_metrics.json")
OUT_PATH = None
DPI = 150
TITLE = "Strict test metrics over training steps\nGemma-4-E2B-it,lr=3e-4,rank=16,batch_size=16,bnb4bit,adamw"


PLOT_METRICS = (
    "protocol_valid_rate",
    "raw_turn_stop_rate",
    "postprocessed_turn_stop_rate",
    "src_wait_accuracy",
    "tgt_wait_accuracy",
    "src_release_accuracy",
    "tgt_release_accuracy",
)

def load_step_entries(metrics_json: Path) -> list[tuple[int, dict[str, Any]]]:
    with metrics_json.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    raw_metrics = payload.get("metrics")
    if not isinstance(raw_metrics, dict):
        raise ValueError(f"Missing object field 'metrics' in {metrics_json}")

    entries: list[tuple[int, dict[str, Any]]] = []
    for step_text, entry in raw_metrics.items():
        try:
            step = int(step_text)
        except (TypeError, ValueError):
            continue
        if isinstance(entry, dict):
            entries.append((step, entry))

    entries.sort(key=lambda item: item[0])
    if not entries:
        raise ValueError(f"No numeric step entries found in {metrics_json}")
    return entries


def collect_metric_series(
    entries: list[tuple[int, dict[str, Any]]],
    metric_name: str,
) -> tuple[list[int], list[float]]:
    steps: list[int] = []
    values: list[float] = []
    for step, entry in entries:
        test_metrics = entry.get("test_metrics")
        if not isinstance(test_metrics, dict):
            continue
        value = test_metrics.get(metric_name)
        if isinstance(value, (int, float)):
            steps.append(step)
            values.append(float(value))
    return steps, values


def plot_metrics(metrics_json: Path, output_path: Path, dpi: int) -> None:
    entries = load_step_entries(metrics_json)

    fig, ax = plt.subplots(figsize=(12, 7))
    plotted_count = 0
    for metric_name in PLOT_METRICS:
        steps, values = collect_metric_series(entries, metric_name)
        if not steps:
            print(f"[skip] {metric_name}: no numeric values found")
            continue
        ax.plot(steps, values, marker="o", linewidth=1.8, markersize=3.5, label=metric_name)
        plotted_count += 1

    if plotted_count == 0:
        raise ValueError(f"None of the requested metrics were found in {metrics_json}")

    ax.set_title(TITLE)
    ax.set_xlabel("step")
    ax.set_ylabel("metric value")
    ax.set_ylim(0.3, 1.02)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(loc="best", fontsize="small")
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi)
    plt.close(fig)
    print(f"Saved plot to: {output_path}")


def main() -> None:
    output_path = OUT_PATH or METRICS_JSON.with_name("test_metrics_plot.png")
    plot_metrics(metrics_json=METRICS_JSON, output_path=output_path, dpi=DPI)


if __name__ == "__main__":
    main()