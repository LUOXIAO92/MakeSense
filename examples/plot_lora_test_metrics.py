"""Plot LoRA strict-test and training metrics from a ``test_metrics.json`` file.

Training-time tests and vLLM batch summaries both write step-keyed strict-test
summaries to ``test_metrics.json``. This helper renders the main protocol /
wait / release rates and the training loss / learning-rate curves as PNG images.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


METRICS_JSON = Path("outputs") / "strict_test" / "gemma-4-E2B-it_1e-4_r16_adamw_bs16_rep12_epo1_conc90" / "test_metrics.json"
OUT_PATH = None
TRAINING_OUT_PATH = None
CONDITION_OUT_DIR = None
DPI = 150
TITLE = "Strict test metrics over training steps\nGemma-4-E2B-it,lr=1e-4,rank=16,α=16,batch_size=16,repetition=12,bnb4bit,adamw"
TRAINING_TITLE = ("Training metrics over training steps\n"
    "Gemma-4-E2B-it, train: bnb 4bit nf4, test: bnb nf4 4bit\n"
    "lr=1e-4, rank=16, α=16, batch_size=16, repetition=12, adamw")


PLOT_METRICS = (
    "protocol_adherence_rate",
    "src_wait_accuracy",
    "tgt_wait_accuracy",
    "src_release_accuracy",
    "tgt_release_accuracy",
)
PLOT_TRAINING_METRICS = (
    "loss",
    "eval_loss",
    "grad_norm",
    "learning_rate",
)
PLOT_CONDITION_METRICS = (
    "protocol_adherence_rate",
    "src_wait_accuracy",
    "tgt_wait_accuracy",
    "src_release_accuracy",
    "tgt_release_accuracy",
)
AXIS_VALUE_MARGIN = 0.01


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


def collect_training_metric_series(
    entries: list[tuple[int, dict[str, Any]]],
    metric_name: str,
) -> tuple[list[int], list[float]]:
    steps: list[int] = []
    values: list[float] = []
    for step, entry in entries:
        metrics = entry.get("metrics")
        if not isinstance(metrics, dict):
            continue
        value = metrics.get(metric_name)
        if isinstance(value, (int, float)):
            steps.append(step)
            values.append(float(value))
    return steps, values


def natural_sort_key(value: str) -> list[tuple[int, Any]]:
    parts = re.split(r"(\d+)", value)
    return [(1, int(part)) if part.isdigit() else (0, part) for part in parts]


def collect_condition_names(entries: list[tuple[int, dict[str, Any]]]) -> list[str]:
    names: set[str] = set()
    for _, entry in entries:
        condition_metrics = entry.get("condition_metrics")
        if not isinstance(condition_metrics, dict):
            continue
        names.update(name for name in condition_metrics if isinstance(name, str))
    return sorted(names, key=natural_sort_key)


def collect_condition_metric_series(
    entries: list[tuple[int, dict[str, Any]]],
    condition_name: str,
    metric_name: str,
) -> tuple[list[int], list[float]]:
    steps: list[int] = []
    values: list[float] = []
    for step, entry in entries:
        condition_metrics = entry.get("condition_metrics")
        if not isinstance(condition_metrics, dict):
            continue
        metrics = condition_metrics.get(condition_name)
        if not isinstance(metrics, dict):
            continue
        value = metrics.get(metric_name)
        if isinstance(value, (int, float)):
            steps.append(step)
            values.append(float(value))
    return steps, values


def padded_axis_limits(values: list[float], margin: float = AXIS_VALUE_MARGIN) -> tuple[float, float]:
    if not values:
        raise ValueError("Cannot compute axis limits for an empty value list")
    return min(values) * (1 - margin), max(values) * (1 + margin)


def plot_metrics(metrics_json: Path, output_path: Path, dpi: int) -> None:
    entries = load_step_entries(metrics_json)

    fig, ax = plt.subplots(figsize=(12, 7))
    plotted_count = 0
    plotted_values: list[float] = []
    for metric_name in PLOT_METRICS:
        steps, values = collect_metric_series(entries, metric_name)
        if not steps:
            print(f"[skip] {metric_name}: no numeric values found")
            continue
        ax.plot(steps, values, marker="o", linewidth=1.8, markersize=3.5, label=metric_name)
        plotted_count += 1
        plotted_values.extend(values)

    if plotted_count == 0:
        raise ValueError(f"None of the requested metrics were found in {metrics_json}")

    ax.set_title(TITLE)
    ax.set_xlabel("step")
    ax.set_ylabel("metric value")
    ax.set_ylim(*padded_axis_limits(plotted_values))
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(loc="best", fontsize="small")
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi)
    plt.close(fig)
    print(f"Saved plot to: {output_path}")


def plot_training_metrics(metrics_json: Path, output_path: Path, dpi: int) -> None:
    entries = load_step_entries(metrics_json)

    fig, (metric_ax, lr_ax) = plt.subplots(2, 1, figsize=(12, 9), sharex=True)
    plotted_count = 0
    metric_values: list[float] = []
    for metric_name in PLOT_TRAINING_METRICS:
        steps, values = collect_training_metric_series(entries, metric_name)
        if not steps:
            print(f"[skip] {metric_name}: no numeric training values found")
            continue

        ax = lr_ax if metric_name == "learning_rate" else metric_ax
        ax.plot(steps, values, marker="o", linewidth=1.8, markersize=3.5, label=metric_name)
        plotted_count += 1
        if metric_name != "learning_rate":
            metric_values.extend(values)

    if plotted_count == 0:
        raise ValueError(f"None of the requested training metrics were found in {metrics_json}")

    metric_ax.set_title(TRAINING_TITLE)
    metric_ax.set_ylabel("loss / grad norm")
    if metric_values:
        metric_ax.set_ylim(*padded_axis_limits(metric_values))
    metric_ax.grid(True, linestyle="--", alpha=0.35)
    metric_ax.legend(loc="best", fontsize="small")

    lr_ax.set_xlabel("step")
    lr_ax.set_ylabel("learning rate")
    lr_ax.grid(True, linestyle="--", alpha=0.35)
    lr_ax.legend(loc="best", fontsize="small")
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi)
    plt.close(fig)
    print(f"Saved training plot to: {output_path}")


def plot_condition_metric_comparisons(metrics_json: Path, output_dir: Path, dpi: int) -> list[Path]:
    entries = load_step_entries(metrics_json)
    condition_names = collect_condition_names(entries)
    if not condition_names:
        print("[skip] condition metrics: no condition_metrics found")
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    saved_paths: list[Path] = []
    for metric_name in PLOT_CONDITION_METRICS:
        fig, ax = plt.subplots(figsize=(12, 7))
        plotted_count = 0
        plotted_values: list[float] = []
        for condition_name in condition_names:
            steps, values = collect_condition_metric_series(entries, condition_name, metric_name)
            if not steps:
                continue
            ax.plot(steps, values, marker="o", linewidth=1.6, markersize=3.0, label=condition_name)
            plotted_count += 1
            plotted_values.extend(values)

        if plotted_count == 0:
            plt.close(fig)
            print(f"[skip] condition {metric_name}: no numeric values found")
            continue

        ax.set_title(f"{metric_name} by condition\n{TITLE.splitlines()[-1]}")
        ax.set_xlabel("step")
        ax.set_ylabel(metric_name)
        ax.set_ylim(*padded_axis_limits(plotted_values))
        ax.grid(True, linestyle="--", alpha=0.35)
        ax.legend(loc="best", fontsize="x-small", ncol=2)
        fig.tight_layout()

        output_path = output_dir / f"condition_{metric_name}.png"
        fig.savefig(output_path, dpi=dpi)
        plt.close(fig)
        saved_paths.append(output_path)
        print(f"Saved condition plot to: {output_path}")

    return saved_paths


def main() -> None:
    output_path = OUT_PATH or METRICS_JSON.with_name("test_metrics_plot.png")
    training_output_path = TRAINING_OUT_PATH or METRICS_JSON.with_name("training_metrics_plot.png")
    condition_output_dir = CONDITION_OUT_DIR or METRICS_JSON.with_name("condition_metrics_plots")
    plot_metrics(metrics_json=METRICS_JSON, output_path=output_path, dpi=DPI)
    plot_training_metrics(metrics_json=METRICS_JSON, output_path=training_output_path, dpi=DPI)
    plot_condition_metric_comparisons(metrics_json=METRICS_JSON, output_dir=condition_output_dir, dpi=DPI)


if __name__ == "__main__":
    main()
