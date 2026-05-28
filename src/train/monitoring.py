"""Monitoring callbacks and TensorBoard lifecycle helpers for MakeSense LoRA training."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

import torch
from transformers import TrainerCallback, TrainerControl, TrainerState, TrainingArguments

from train.tester import StreamingSampleTester


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
        print(f"TensorBoard started at http://{self.host}:{self.port} (logdir={self.logdir})")

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
    """Persist training logs and periodically print/save one sample generation comparison."""

    def __init__(
        self,
        *,
        processor: Any,
        sample_rows: list[dict[str, Any]] | None,
        collator: Any,
        output_dir: str | Path,
        logging_dir: str | Path,
        metrics_jsonl_name: str,
        sample_generations_jsonl_name: str,
        sample_generation_steps: int,
        sample_generation_max_new_tokens: int,
        sample_evaluation_record_count: int,
    ) -> None:
        self.processor = processor
        self.metrics_jsonl_path = Path(output_dir) / metrics_jsonl_name
        self.sample_generations_jsonl_path = Path(output_dir) / sample_generations_jsonl_name
        self.sample_generation_steps = sample_generation_steps
        self.logging_dir = Path(logging_dir)
        self.latest_metrics: dict[str, Any] = {}
        self.tester = StreamingSampleTester(
            processor=processor,
            sample_rows=sample_rows,
            collator=collator,
            sample_generation_max_new_tokens=sample_generation_max_new_tokens,
            sample_evaluation_record_count=sample_evaluation_record_count,
            enable_thinking=False,
        )

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
        metrics = filter_training_metrics(dict(logs))
        if metrics is None:
            return
        self.latest_metrics = metrics
        append_jsonl(self.metrics_jsonl_path, {"step": step, "metrics": metrics})
        if self._should_generate(step):
            model = kwargs["model"]
            records = self.tester.generate_records(model=model, step=step, metrics=metrics)
            for record in records:
                self.tester.print_record(record)
                append_jsonl(self.sample_generations_jsonl_path, record)

    def _should_generate(self, step: int) -> bool:
        return bool(
            self.sample_generation_steps > 0
            and step > 0
            and step % self.sample_generation_steps == 0
            and self.tester.has_rows()
        )
