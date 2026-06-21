"""Batch runtime strict tests for LoRA checkpoints served by vLLM Docker."""

from __future__ import annotations

import json
import re
import subprocess
import time
import urllib.request
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Callable

from openai import OpenAI

from .openai_strict_tester import OpenAIStrictTestConfig, run_openai_strict_test


_CHECKPOINT_RE = re.compile(r"^checkpoint-(\d+)$")
_CONTAINER_NAME_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_.-]*$")
_COUNT_FIELDS = ("record_count", "turn_count", "src_wait_total", "tgt_wait_total", "src_release_total", "tgt_release_total")
_TARGET_COUNT_FIELDS = (
    "target_metrics_included_record_count",
    "target_metrics_filtered_record_count",
    "target_metrics_filtered_turn_count",
)


@dataclass(frozen=True)
class VLLMDockerServeConfig:
    """Explicit vLLM Docker serving settings."""

    docker_image: str
    docker_run_args: tuple[str, ...]
    model_mount_source: str | Path
    model_mount_target: str
    base_model_path: str
    lora_mount_target: str
    served_model_name: str
    lora_model_name: str
    serve_host: str
    serve_port: int
    container_port: int
    vllm_serve_args: tuple[str, ...]
    container_name_prefix: str = "makesense-vllm-strict"
    docker_executable: str = "docker"


@dataclass(frozen=True)
class VLLMStrictBatchConfig:
    """Configuration for checkpoint-by-checkpoint strict tests."""

    strict_test_config: OpenAIStrictTestConfig
    docker: VLLMDockerServeConfig
    training_output_dir: str | Path
    lora_root: str | Path
    strict_test_output_root: str | Path
    strict_test_run_name: str
    checkpoint_steps: tuple[int, ...] | None = None
    docker_cooldown_seconds: float = 0.0
    readiness_timeout_seconds: float = 900.0
    readiness_poll_seconds: float = 5.0
    readiness_path: str = "/v1/models"
    smoke_test_enabled: bool = True
    smoke_test_messages: tuple[dict[str, str], ...] = field(
        default_factory=lambda: ({"role": "user", "content": "Say ok."},)
    )
    smoke_test_max_tokens: int = 4
    smoke_test_timeout_seconds: float | None = 60.0
    summary_output_path: str | Path | None = None

    def summary_path(self) -> Path:
        if self.summary_output_path is not None:
            return Path(self.summary_output_path)
        return Path(self.strict_test_output_root) / self.strict_test_run_name / "test_metrics.json"


def parse_checkpoint_step(path: str | Path) -> int:
    match = _CHECKPOINT_RE.match(Path(path).name)
    if match is None:
        raise ValueError(f"Checkpoint path must end with checkpoint-<step>, got {path}")
    return int(match.group(1))


def discover_checkpoint_paths(lora_root: str | Path, checkpoint_steps: tuple[int, ...] | None = None) -> list[Path]:
    root = Path(lora_root)
    if checkpoint_steps is not None:
        return [root / f"checkpoint-{step}" for step in sorted(checkpoint_steps)]
    checkpoints = [path for path in root.iterdir() if path.is_dir() and _CHECKPOINT_RE.match(path.name)]
    return sorted(checkpoints, key=parse_checkpoint_step)


def build_vllm_docker_command(
    *,
    docker: VLLMDockerServeConfig,
    checkpoint_path: str | Path,
    container_name: str,
) -> list[str]:
    model_mount_source = Path(docker.model_mount_source).expanduser().resolve()
    checkpoint_mount_source = Path(checkpoint_path).expanduser().resolve()
    return [
        docker.docker_executable,
        "run",
        *docker.docker_run_args,
        "--name",
        container_name,
        "-v",
        f"{model_mount_source}:{docker.model_mount_target}",
        "-v",
        f"{checkpoint_mount_source}:{docker.lora_mount_target}",
        "-p",
        f"{int(docker.serve_port)}:{int(docker.container_port)}",
        docker.docker_image,
        "vllm",
        "serve",
        "--host",
        docker.serve_host,
        "--model",
        docker.base_model_path,
        "--served-model-name",
        docker.served_model_name,
        "--enable-lora",
        "--lora-modules",
        f"{docker.lora_model_name}={docker.lora_mount_target}",
        *docker.vllm_serve_args,
    ]


def _validate_container_name(name: str) -> None:
    if _CONTAINER_NAME_RE.match(name) is None:
        raise ValueError(
            f"Invalid Docker container name {name!r}. Use only [a-zA-Z0-9][a-zA-Z0-9_.-]*; "
            "do not use an image name as container_name_prefix."
        )


def _readiness_url(config: VLLMStrictBatchConfig) -> str:
    base_url = config.strict_test_config.base_url.rstrip("/")
    if base_url.endswith("/v1"):
        base_url = base_url[:-3]
    return f"{base_url}{config.readiness_path}"


def _wait_for_endpoint(url: str, *, timeout_seconds: float, poll_seconds: float, process: subprocess.Popen[Any]) -> None:
    deadline = time.monotonic() + float(timeout_seconds)
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"vLLM Docker process exited before readiness check passed: {url}")
        try:
            with urllib.request.urlopen(url, timeout=max(float(poll_seconds), 1.0)) as response:
                if 200 <= int(response.status) < 300:
                    return
        except Exception as exc:  # noqa: BLE001 - readiness failures are retried until timeout.
            last_error = exc
        time.sleep(float(poll_seconds))
    raise TimeoutError(f"Timed out waiting for vLLM endpoint {url}: {last_error}")


def _stop_container(docker: VLLMDockerServeConfig, container_name: str) -> None:
    subprocess.run([docker.docker_executable, "stop", container_name], check=False)


def _smoke_response_content(response: Any) -> str:
    choices = getattr(response, "choices", None)
    if not choices:
        raise RuntimeError("OpenAI-compatible provider returned no choices during smoke test")
    message = getattr(choices[0], "message", None)
    if message is None:
        raise RuntimeError("OpenAI-compatible provider returned a smoke choice without message")
    content = getattr(message, "content", None)
    if not isinstance(content, str):
        raise RuntimeError(f"OpenAI-compatible provider returned non-string smoke content: {type(content).__name__}")
    if not content.strip():
        raise RuntimeError("OpenAI-compatible provider returned empty smoke content")
    return content


def _run_lora_generation_smoke_test(config: VLLMStrictBatchConfig, checkpoint_step: int) -> None:
    client = OpenAI(
        api_key=config.strict_test_config.api_key,
        base_url=config.strict_test_config.base_url,
        timeout=config.smoke_test_timeout_seconds,
    )
    try:
        response = client.chat.completions.create(
            model=config.strict_test_config.model_name,
            messages=[dict(message) for message in config.smoke_test_messages],
            max_tokens=int(config.smoke_test_max_tokens),
        )
        _smoke_response_content(response)
    except Exception as exc:  # noqa: BLE001 - smoke failure should include checkpoint context.
        raise RuntimeError(
            "vLLM LoRA smoke test failed "
            f"checkpoint-{checkpoint_step} "
            f"model={config.strict_test_config.model_name!r} "
            f"base_url={config.strict_test_config.base_url!r} "
            f"error_type={exc.__class__.__module__}.{exc.__class__.__name__} "
            f"error={str(exc)!r}"
        ) from exc


def _condition_key(payload: dict[str, Any]) -> str:
    condition = payload["condition"]
    mode = condition["mode"]
    if mode in {"asr", "natural"}:
        return str(mode)
    return f"{mode}_{condition['requested_window_label']}"


def _normalize_condition_metrics(test_metrics: dict[str, Any], *, include_tgt: bool) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    for key in ("protocol_adherence_rate", "src_wait_accuracy", "src_release_accuracy"):
        if key in test_metrics:
            normalized[key] = test_metrics[key]
    if include_tgt:
        for key in ("tgt_wait_accuracy", "tgt_release_accuracy"):
            if key in test_metrics:
                normalized[key] = test_metrics[key]
    for key in _COUNT_FIELDS:
        if not include_tgt and key.startswith("tgt_"):
            continue
        if key in test_metrics:
            normalized[key] = test_metrics[key]
    if include_tgt:
        for key in _TARGET_COUNT_FIELDS:
            if key in test_metrics:
                normalized[key] = test_metrics[key]
    for key, value in test_metrics.items():
        if key.startswith("process_time_ms_"):
            normalized[key] = value
    return normalized


def _weighted_rate(metrics: list[dict[str, Any]], *, rate_key: str, count_key: str) -> float | None:
    total = 0.0
    correct = 0.0
    for metric in metrics:
        if rate_key not in metric or count_key not in metric:
            continue
        count = float(metric[count_key])
        total += count
        correct += float(metric[rate_key]) * count
    if total == 0:
        return None
    return correct / total


def _aggregate_condition_metrics(condition_metrics: dict[str, dict[str, Any]]) -> dict[str, Any]:
    all_metrics = list(condition_metrics.values())
    translation_metrics = [
        metric for key, metric in condition_metrics.items() if key != "asr" and not key.startswith("asr")
    ]
    aggregate: dict[str, Any] = {}
    count_for_rate = {
        "protocol_adherence_rate": "turn_count",
        "src_wait_accuracy": "src_wait_total",
        "src_release_accuracy": "src_release_total",
    }
    for rate_key, count_key in count_for_rate.items():
        value = _weighted_rate(all_metrics, rate_key=rate_key, count_key=count_key)
        if value is not None:
            aggregate[rate_key] = value
            aggregate[count_key] = sum(int(metric.get(count_key, 0)) for metric in all_metrics)
    for rate_key, count_key in {
        "tgt_wait_accuracy": "tgt_wait_total",
        "tgt_release_accuracy": "tgt_release_total",
    }.items():
        value = _weighted_rate(translation_metrics, rate_key=rate_key, count_key=count_key)
        if value is not None:
            aggregate[rate_key] = value
            aggregate[count_key] = sum(int(metric.get(count_key, 0)) for metric in translation_metrics)
    for key in _TARGET_COUNT_FIELDS:
        total = sum(int(metric.get(key, 0)) for metric in translation_metrics)
        if total:
            aggregate[key] = total
    return aggregate


def summarize_checkpoint_strict_metrics(metrics_dir: str | Path) -> tuple[int, dict[str, Any], dict[str, Any]]:
    condition_metrics: dict[str, dict[str, Any]] = {}
    test_record_count: int | None = None
    for path in sorted(Path(metrics_dir).glob("strict_test_metrics-*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        key = _condition_key(payload)
        include_tgt = key != "asr"
        condition_metrics[key] = _normalize_condition_metrics(payload["test_metrics"], include_tgt=include_tgt)
        if test_record_count is None:
            test_record_count = int(payload["selected_test_rows"])
    if test_record_count is None:
        raise FileNotFoundError(f"No strict_test_metrics-*.json files found under {metrics_dir}")
    aggregate_metrics = _aggregate_condition_metrics(condition_metrics)
    aggregate_metrics["record_count"] = test_record_count
    return test_record_count, aggregate_metrics, condition_metrics


def write_vllm_strict_batch_summary(
    *,
    config: VLLMStrictBatchConfig,
    checkpoint_paths: list[Path],
) -> dict[str, Any]:
    training_output_dir = Path(config.training_output_dir)
    training_metrics_path = training_output_dir / "test_metrics.json"
    training_metrics = json.loads(training_metrics_path.read_text(encoding="utf-8"))
    strict_run_root = Path(config.strict_test_output_root) / config.strict_test_run_name
    summary: dict[str, Any] = {
        "metadata": {
            "dataset_root": str(config.strict_test_config.dataset_root),
            "training_output_dir": str(training_output_dir),
            "strict_test_output_dir": str(strict_run_root),
            "model_name": config.docker.base_model_path,
            "served_model_name": config.docker.served_model_name,
            "lora_root": str(config.lora_root),
            "concurrency": config.strict_test_config.concurrency,
        },
        "metrics": {},
    }
    for checkpoint_path in checkpoint_paths:
        step = parse_checkpoint_step(checkpoint_path)
        step_key = str(step)
        training_entry = dict(training_metrics.get("metrics", {}).get(step_key, {}))
        training_entry.pop("records", None)
        metrics_dir = strict_run_root / f"checkpoint-{step}" / "metrics"
        test_record_count, aggregate_metrics, condition_metrics = summarize_checkpoint_strict_metrics(metrics_dir)
        summary["metrics"][step_key] = {
            "step": step,
            "metrics": training_entry.get("metrics", {}),
            "test_batch_size": training_entry.get("test_batch_size"),
            "test_record_count": test_record_count,
            "test_metrics": aggregate_metrics,
            "condition_metrics": condition_metrics,
        }
    output_path = config.summary_path()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def run_vllm_strict_checkpoint_batch(
    config: VLLMStrictBatchConfig,
    *,
    strict_test_runner: Callable[[OpenAIStrictTestConfig], dict[str, Any]] = run_openai_strict_test,
    smoke_tester: Callable[[VLLMStrictBatchConfig, int], None] = _run_lora_generation_smoke_test,
) -> dict[str, Any]:
    checkpoints = discover_checkpoint_paths(config.lora_root, config.checkpoint_steps)
    strict_run_root = Path(config.strict_test_output_root) / config.strict_test_run_name
    for checkpoint_index, checkpoint_path in enumerate(checkpoints):
        step = parse_checkpoint_step(checkpoint_path)
        container_name = f"{config.docker.container_name_prefix}-checkpoint-{step}"
        _validate_container_name(container_name)
        command = build_vllm_docker_command(
            docker=config.docker,
            checkpoint_path=checkpoint_path,
            container_name=container_name,
        )
        process = subprocess.Popen(command)
        try:
            _wait_for_endpoint(
                _readiness_url(config),
                timeout_seconds=config.readiness_timeout_seconds,
                poll_seconds=config.readiness_poll_seconds,
                process=process,
            )
            if config.smoke_test_enabled:
                smoke_tester(config, step)
            output_dir = strict_run_root / f"checkpoint-{step}"
            strict_test_runner(
                replace(
                    config.strict_test_config,
                    metrics_output_dir=output_dir / "metrics",
                    markdown_output_dir=output_dir / "markdown",
                )
            )
        finally:
            if process.poll() is None:
                _stop_container(config.docker, container_name)
            try:
                process.wait(timeout=60)
            except subprocess.TimeoutExpired:
                pass
            if config.docker_cooldown_seconds > 0 and checkpoint_index < len(checkpoints) - 1:
                time.sleep(float(config.docker_cooldown_seconds))
    return write_vllm_strict_batch_summary(config=config, checkpoint_paths=checkpoints)
