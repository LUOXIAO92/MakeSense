"""Monitoring callbacks and TensorBoard lifecycle helpers for MakeSense LoRA training."""

from __future__ import annotations

import json
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any

import torch
from transformers import TrainerCallback, TrainerControl, TrainerState, TrainingArguments

from train.tester import StreamingSampleTester, format_test_outputs_markdown, print_test_summary


def _json_default(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, torch.Tensor):
        if value.numel() == 1:
            return value.item()
        return value.detach().cpu().tolist()
    return str(value)


def append_jsonl(path: str | Path, record: dict[str, Any]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False, default=_json_default) + "\n")


def filter_training_metrics(logs: dict[str, Any]) -> dict[str, Any] | None:
    if "loss" not in logs:
        return None
    allowed_keys = {"loss", "grad_norm", "learning_rate", "epoch"}
    return {key: logs[key] for key in allowed_keys if key in logs}


def _as_float(value: Any) -> float | None:
    if isinstance(value, torch.Tensor):
        if value.numel() != 1:
            return None
        value = value.item()
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _format_compact_float(value: Any) -> str | None:
    number = _as_float(value)
    if number is None:
        return None
    return f"{number:8.2e}"


def _format_metric_value(value: Any) -> str:
    rendered = _format_compact_float(value)
    return rendered if rendered is not None else "None"


def format_monitoring_prefix(latest_metrics: dict[str, Any], *, epoch: Any, global_step: int) -> str:
    """Format the project-owned live progress prefix.

    Prefix is intentionally limited to training state. The progress renderer
    owns total progress and runtime telemetry.
    """

    epoch_number = _as_float(epoch)
    epoch_text = str(int(epoch_number)) if epoch_number is not None else "0"
    parts = [f"epoch={epoch_text}", f"step={int(global_step)}"]
    for key in ("loss", "eval_loss", "grad_norm"):
        parts.append(f"{key}={_format_metric_value(latest_metrics.get(key))}")
    return ", ".join(parts)


def format_training_time(seconds: float) -> str:
    """Format elapsed training time as HH:MM:SS for compact CLI progress."""

    total_seconds = max(0, int(seconds))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def format_monitoring_progress_line(
    *,
    step: int,
    total: int | None,
    prefix: str,
    elapsed_seconds: float,
) -> str:
    """Format a short single-line training progress message without a visual bar."""

    step = int(step)
    if total is not None and total > 0:
        percentage = round(step / total * 100)
        progress = f"{percentage}%, {step}/{total}"
    else:
        progress = f"step={step}"
    return f"{progress} | {prefix}, train_time={format_training_time(elapsed_seconds)}"


def tensorboard_scalar_tag(metric_name: str) -> str:
    """Map Trainer log keys to stable project-owned TensorBoard scalar tags."""

    if metric_name.startswith("eval_"):
        return "eval/" + metric_name.removeprefix("eval_")
    if metric_name in {"loss", "grad_norm", "learning_rate", "epoch"}:
        return "train/" + metric_name
    return "trainer/" + metric_name


def latest_logged_metrics_from_state(state: TrainerState) -> dict[str, Any]:
    """Return the latest known monitoring metrics from in-memory Trainer state.

    This intentionally reads only the already-loaded ``state.log_history``. It
    does not inspect checkpoint JSON files; if the Trainer has not loaded prior
    history yet, the caller receives an empty dict and live logs will populate
    metrics later.
    """

    latest: dict[str, Any] = {}
    for entry in getattr(state, "log_history", []) or []:
        if not isinstance(entry, dict):
            continue
        latest.update(
            {
                key: value
                for key, value in entry.items()
                if key in {"loss", "eval_loss", "grad_norm", "learning_rate", "epoch"}
            }
        )
    return latest


class ProjectTensorBoardWriter:
    """Small project-owned TensorBoard scalar writer wrapper."""

    def __init__(self, *, logdir: str | Path, enabled: bool = True) -> None:
        self.logdir = Path(logdir)
        self.enabled = bool(enabled)
        self._writer: Any | None = None

    def start(self) -> None:
        if not self.enabled or self._writer is not None:
            return
        self.logdir.mkdir(parents=True, exist_ok=True)
        try:
            from torch.utils.tensorboard import SummaryWriter
        except ImportError as exc:
            raise RuntimeError("TensorBoard monitoring requires torch.utils.tensorboard") from exc
        self._writer = SummaryWriter(log_dir=str(self.logdir))

    def write_logs(self, logs: dict[str, Any], *, step: int) -> None:
        if not self.enabled:
            return
        self.start()
        if self._writer is None:
            return
        for key, value in logs.items():
            scalar = _as_float(value)
            if scalar is None:
                continue
            self._writer.add_scalar(tensorboard_scalar_tag(str(key)), scalar, int(step))
        self._writer.flush()

    def close(self) -> None:
        writer = self._writer
        self._writer = None
        if writer is not None:
            writer.close()


class _SingleLineProgress:
    """Lazy short-line tqdm wrapper so importing tests does not require terminal setup."""

    def __init__(self, *, total: int | None) -> None:
        self.total = total
        self._bar: Any | None = None
        self._last_step = 0
        self._started_at: float | None = None

    def start(self, *, initial: int = 0) -> None:
        if self._bar is not None:
            return
        from tqdm.auto import tqdm

        self._bar = tqdm(
            total=self.total,
            initial=int(initial),
            bar_format="{desc} | {elapsed}<{remaining}, {rate_fmt}",
            dynamic_ncols=False,
            leave=True,
        )

    def update(self, *, step: int, prefix: str) -> None:
        step = int(step)
        if step <= 0 and self._bar is None:
            return
        self.start(initial=step if self._started_at is None else 0)
        if self._bar is None:
            return
        if self._started_at is None:
            self._started_at = time.monotonic()
            self._last_step = step
            elapsed = 0.0
        else:
            delta = max(0, step - self._last_step)
            if delta:
                self._bar.update(delta)
                self._last_step = step
            elapsed = max(0.0, time.monotonic() - self._started_at)
        self._bar.set_description_str(
            format_monitoring_progress_line(
                step=step,
                total=self.total,
                prefix=prefix,
                elapsed_seconds=elapsed,
            )
        )

    def break_line(self) -> None:
        self.start()
        if self._bar is not None:
            self._bar.write("")

    def close(self) -> None:
        bar = self._bar
        self._bar = None
        if bar is not None:
            bar.close()


class TensorBoardServer:
    """Manage a background TensorBoard process for the trainer lifecycle."""

    def __init__(
        self,
        *,
        logdir: str | Path,
        host: str = "127.0.0.1",
        port: int = 6006,
        enabled: bool = True,
    ) -> None:
        self.logdir = Path(logdir)
        self.host = host
        self.port = int(port)
        self.enabled = bool(enabled)
        self.process: subprocess.Popen[str] | None = None

    def start(self) -> None:
        if not self.enabled or self.process is not None:
            return
        if shutil.which("tensorboard") is None:
            print("TensorBoard executable not found; skipping background server startup")
            return
        self.logdir.mkdir(parents=True, exist_ok=True)
        command = [
            "tensorboard",
            "--logdir",
            str(self.logdir),
            "--host",
            self.host,
            "--port",
            str(self.port),
            "--reload_interval",
            "1",
        ]
        self.process = subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
        )

    def stop(self) -> None:
        process = self.process
        self.process = None
        if process is None:
            return
        if process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
        print("TensorBoard stopped")


class MakeSenseMonitoringCallback(TrainerCallback):
    """Project-owned TensorBoard/progress/test monitoring callback."""

    def __init__(
        self,
        *,
        processor: Any,
        test_rows: list[dict[str, Any]] | None,
        collator: Any,
        output_dir: str | Path,
        logging_dir: str | Path,
        test_metrics_json_name: str,
        test_metadata: dict[str, Any] | None = None,
        test_steps: int,
        test_max_new_tokens: int,
        test_record_count: int,
        test_batch_size: int = 1,
        test_output_markdown: bool = False,
        test_outputs_dir_name: str = "test_outputs",
        generation_stop: str,
        total_optimizer_steps: int | None = None,
        enable_tensorboard: bool = True,
        enable_progress: bool = True,
    ) -> None:
        self.processor = processor
        self.test_metrics_json_path = Path(output_dir) / test_metrics_json_name
        self.test_outputs_dir = Path(output_dir) / test_outputs_dir_name
        self.test_output_markdown = bool(test_output_markdown)
        self.test_metadata = dict(test_metadata or {})
        self.test_steps = test_steps
        self._last_test_step: int | None = None
        self.logging_dir = Path(logging_dir)
        self.latest_metrics: dict[str, Any] = {}
        self.tensorboard_writer = ProjectTensorBoardWriter(
            logdir=self.logging_dir,
            enabled=enable_tensorboard,
        )
        self.progress = _SingleLineProgress(total=total_optimizer_steps) if enable_progress else None
        self.tester = StreamingSampleTester(
            processor=processor,
            test_rows=test_rows,
            collator=collator,
            test_max_new_tokens=test_max_new_tokens,
            test_record_count=test_record_count,
            test_batch_size=test_batch_size,
            generation_stop=generation_stop,
            enable_thinking=False,
        )

    def on_train_begin(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        **kwargs: Any,
    ) -> None:
        self.tensorboard_writer.start()

    def on_step_end(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        **kwargs: Any,
    ) -> None:
        self._update_progress(state)
        step = int(state.global_step)
        if self._should_defer_step_test_to_evaluate(args=args, step=step):
            return
        self._maybe_run_periodic_test(state=state, kwargs=kwargs)

    def on_log(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        logs: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        if not logs:
            return
        step = int(state.global_step)
        log_payload = dict(logs)
        self.tensorboard_writer.write_logs(log_payload, step=step)
        self.latest_metrics.update(
            {
                key: value
                for key, value in log_payload.items()
                if key in {"loss", "eval_loss", "grad_norm", "learning_rate", "epoch"}
            }
        )
        self._update_progress(state)

    def on_evaluate(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        metrics: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        if metrics:
            self.latest_metrics.update(
                {
                    key: value
                    for key, value in metrics.items()
                    if key in {"loss", "eval_loss", "grad_norm", "learning_rate", "epoch"}
                }
            )
        self._update_progress(state)
        self._maybe_run_periodic_test(state=state, kwargs=kwargs)

    def on_save(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        **kwargs: Any,
    ) -> None:
        return None

    def on_train_end(
        self,
        args: TrainingArguments,
        state: TrainerState,
        control: TrainerControl,
        **kwargs: Any,
    ) -> None:
        self._update_progress(state)
        self.tensorboard_writer.close()
        if self.progress is not None:
            self.progress.close()

    def _update_progress(self, state: TrainerState) -> None:
        if self.progress is None:
            return
        prefix = format_monitoring_prefix(
            self.latest_metrics,
            epoch=state.epoch,
            global_step=int(state.global_step),
        )
        self.progress.update(step=int(state.global_step), prefix=prefix)

    def _should_test(self, step: int) -> bool:
        return bool(
            self.test_steps > 0
            and step > 0
            and step % self.test_steps == 0
            and self.tester.has_rows()
        )

    def _should_defer_step_test_to_evaluate(self, *, args: TrainingArguments, step: int) -> bool:
        if not self._should_test(step):
            return False
        eval_steps = getattr(args, "eval_steps", None)
        if not eval_steps:
            return False
        eval_strategy = getattr(args, "eval_strategy", getattr(args, "evaluation_strategy", None))
        if eval_strategy is None or str(eval_strategy).lower().endswith("no"):
            return False
        return step % int(eval_steps) == 0

    def _maybe_run_periodic_test(self, *, state: TrainerState, kwargs: dict[str, Any]) -> dict[str, Any] | None:
        step = int(state.global_step)
        if not self._should_test(step):
            return None
        if self._last_test_step == step:
            return None
        model = kwargs["model"]
        self._last_test_step = step
        return self._run_and_persist_test(model=model, step=step, metrics=dict(self.latest_metrics))

    def _write_test_metrics(self, summary: dict[str, Any]) -> None:
        payload = _load_test_metrics_history(self.test_metrics_json_path)
        metadata = payload.setdefault("metadata", {})
        if isinstance(metadata, dict):
            metadata.update(self.test_metadata)
        metrics = payload.setdefault("metrics", {})
        if not isinstance(metrics, dict):
            metrics = {}
            payload["metrics"] = metrics
        metrics[str(summary["step"])] = summary
        self.test_metrics_json_path.parent.mkdir(parents=True, exist_ok=True)
        with self.test_metrics_json_path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, default=_json_default, indent=2)

    def _write_test_markdown(self, summary: dict[str, Any], *, final: bool = False) -> Path | None:
        if not self.test_output_markdown:
            return None
        step = int(summary["step"])
        file_name = f"final-step-{step}.md" if final else f"step-{step}.md"
        output_path = self.test_outputs_dir / file_name
        output_path.parent.mkdir(parents=True, exist_ok=True)
        title = f"Final Test Outputs - step {step}" if final else f"Test Outputs - step {step}"
        output_path.write_text(
            format_test_outputs_markdown(summary, title=title),
            encoding="utf-8",
        )
        return output_path

    def _run_and_persist_test(
        self,
        *,
        model: Any,
        step: int,
        metrics: dict[str, Any],
        final: bool = False,
    ) -> dict[str, Any]:
        if self.progress is not None:
            self.progress.break_line()
        summary = self.tester.evaluate(
            model=model,
            step=step,
            metrics=metrics,
        )
        print_test_summary(summary)
        markdown_path = self._write_test_markdown(summary, final=final)
        if markdown_path is not None:
            print(f"  - TEST_OUTPUT_MARKDOWN: {markdown_path}")
        if self.progress is not None:
            self.progress.break_line()
        self._write_test_metrics(summary)
        return summary

    def run_final_test(self, *, model: Any, step: int) -> dict[str, Any] | None:
        if not self.tester.has_rows():
            return None
        metrics = dict(self.latest_metrics)
        return self._run_and_persist_test(model=model, step=step, metrics=metrics, final=True)


def _load_test_metrics_history(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"metadata": {}, "metrics": {}}
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        return {"metadata": {}, "metrics": {}}
    if "metrics" in data and isinstance(data.get("metrics"), dict):
        data.setdefault("metadata", {})
        return data
    step = data.get("step")
    return {
        "metadata": {},
        "metrics": {str(step): data} if step is not None else {},
    }
