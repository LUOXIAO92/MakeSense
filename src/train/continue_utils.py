"""Explicit continue/resume helpers for MakeSense LoRA training."""

from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable

import torch


VALID_CONTINUE_TYPES = {"none", "resume", "branch"}
CHECKPOINT_RE = re.compile(r"^checkpoint-(\d+)$")
BRANCH_COPY_NAMES = {"adapter_model.safetensors", "adapter_config.json", "README.md"}
TRAINER_STATE_NAMES = {
    "optimizer.pt",
    "scheduler.pt",
    "rng_state.pth",
    "trainer_state.json",
    "training_args.bin",
}
RESUME_ARG_NAMES = (
    "learning_rate",
    "warmup_steps",
    "lr_scheduler_type",
    "max_steps",
    "num_train_epochs",
    "per_device_train_batch_size",
    "gradient_accumulation_steps",
    "weight_decay",
    "max_grad_norm",
    "optim",
    "adam_beta1",
    "adam_beta2",
    "adam_epsilon",
)


@dataclass(frozen=True)
class ContinuePlan:
    continue_type: str
    source_checkpoint: Path | None
    resolved_checkpoint: Path | None
    checkpoint_step: int | None
    trainer_resume_from_checkpoint: Path | None
    copied_checkpoint: bool
    copied_tensorboard: bool
    copied_test_metrics: bool


def parse_checkpoint_step(path: str | Path) -> int:
    match = CHECKPOINT_RE.fullmatch(Path(path).name)
    if match is None:
        raise ValueError(f"Checkpoint path must end with checkpoint-<step>, got {path}")
    return int(match.group(1))


def list_checkpoints(output_dir: str | Path) -> list[Path]:
    root = Path(output_dir)
    if not root.exists():
        return []
    checkpoints = [path for path in root.iterdir() if path.is_dir() and CHECKPOINT_RE.fullmatch(path.name)]
    return sorted(checkpoints, key=parse_checkpoint_step)


def latest_checkpoint(output_dir: str | Path) -> Path:
    checkpoints = list_checkpoints(output_dir)
    if not checkpoints:
        raise FileNotFoundError(f"No checkpoint-* directories found under {output_dir}")
    return checkpoints[-1]


def timestamp_run_dir_name(now: Any | None = None) -> str:
    from datetime import datetime

    current = now if now is not None else datetime.now()
    return current.strftime("%Y-%m-%d_%H-%M-%S")


def _copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _copy_tree_contents(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            _copy_file(item, target)
    return True


def copy_branch_adapter_files(source_checkpoint: str | Path, destination_checkpoint: str | Path) -> bool:
    src = Path(source_checkpoint)
    dst = Path(destination_checkpoint)
    if not src.is_dir():
        raise FileNotFoundError(f"Checkpoint directory not found: {src}")
    dst.mkdir(parents=True, exist_ok=True)
    copied = False
    for item in src.iterdir():
        if item.name in TRAINER_STATE_NAMES:
            continue
        if item.name in BRANCH_COPY_NAMES or item.name.startswith("adapter_") or item.suffix in {".json", ".safetensors"}:
            if item.is_dir():
                shutil.copytree(item, dst / item.name, dirs_exist_ok=True)
            else:
                _copy_file(item, dst / item.name)
            copied = True
    if not (dst / "adapter_config.json").exists():
        raise FileNotFoundError(f"Branch checkpoint is missing adapter_config.json after copy: {dst}")
    return copied


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data if isinstance(data, dict) else {}


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2, default=str)


def prune_test_metrics_file(path: str | Path, *, max_step: int) -> bool:
    metrics_path = Path(path)
    if not metrics_path.exists():
        return False
    payload = _load_json(metrics_path)
    metrics = payload.get("metrics")
    if not isinstance(metrics, dict):
        legacy_step = payload.get("step")
        metrics = {str(legacy_step): payload} if legacy_step is not None else {}
    kept: dict[str, Any] = {}
    for key, value in metrics.items():
        try:
            step = int(key)
        except ValueError:
            step = int(value.get("step", -1)) if isinstance(value, dict) else -1
        if step <= max_step:
            kept[str(step)] = value
    payload["metrics"] = kept
    payload.setdefault("metadata", {})
    _write_json(metrics_path, payload)
    return True


def copy_and_prune_test_metrics(
    *,
    source_output_dir: str | Path,
    destination_output_dir: str | Path,
    test_metrics_json_name: str,
    max_step: int,
    metadata_updates: dict[str, Any] | None = None,
) -> bool:
    src = Path(source_output_dir) / test_metrics_json_name
    if not src.exists():
        return False
    dst = Path(destination_output_dir) / test_metrics_json_name
    _copy_file(src, dst)
    prune_test_metrics_file(dst, max_step=max_step)
    if metadata_updates:
        payload = _load_json(dst)
        metadata = payload.setdefault("metadata", {})
        if isinstance(metadata, dict):
            metadata.update(metadata_updates)
        _write_json(dst, payload)
    return True


def _source_output_root(checkpoint: Path) -> Path:
    return checkpoint.parent


def _has_later_checkpoints(output_dir: Path, step: int) -> bool:
    return any(parse_checkpoint_step(path) > step for path in list_checkpoints(output_dir))


def _copy_full_checkpoint(source_checkpoint: Path, destination_checkpoint: Path) -> bool:
    if source_checkpoint.resolve() == destination_checkpoint.resolve():
        return False
    shutil.copytree(source_checkpoint, destination_checkpoint, dirs_exist_ok=True)
    return True


def _copy_tensorboard_for_resume(source_root: Path, output_dir: Path) -> bool:
    if source_root.resolve() == output_dir.resolve():
        return False
    return _copy_tree_contents(source_root / "runs", output_dir / "runs")


def _copy_tensorboard_for_branch(source_root: Path, output_dir: Path) -> bool:
    src_runs = source_root / "runs"
    if not src_runs.exists():
        return False
    return _copy_tree_contents(src_runs, output_dir / "runs" / "old")


def _branch_checkpoint_name(source_checkpoint: Path) -> str:
    source_output_name = source_checkpoint.parent.name
    return f"branch--{source_output_name}--{source_checkpoint.name}"


def _ensure_no_existing_checkpoints(output_dir: Path, *, continue_type: str) -> None:
    existing_checkpoints = list_checkpoints(output_dir)
    if not existing_checkpoints:
        return
    checkpoint_names = ", ".join(path.name for path in existing_checkpoints)
    raise ValueError(
        f"Refusing CONTINUE_TYPE='{continue_type}' because OUTPUT_DIR already contains checkpoint directories: "
        f"{checkpoint_names}. Use CONTINUE_TYPE='resume' to continue in place, or choose a different OUTPUT_DIR."
    )


def resolve_continue_plan(
    *,
    continue_type: str,
    checkpoint_path: str | Path | None,
    output_dir: str | Path,
    test_metrics_json_name: str = "test_metrics.json",
) -> ContinuePlan:
    if continue_type not in VALID_CONTINUE_TYPES:
        raise ValueError(f"CONTINUE_TYPE must be one of {sorted(VALID_CONTINUE_TYPES)}, got {continue_type!r}")
    output_root = Path(output_dir)
    if continue_type == "none":
        if checkpoint_path is not None:
            raise ValueError("CHECKPOINT_PATH must be None when CONTINUE_TYPE='none'")
        _ensure_no_existing_checkpoints(output_root, continue_type="none")
        return ContinuePlan("none", None, None, None, None, False, False, False)

    source_checkpoint = latest_checkpoint(output_root) if checkpoint_path is None and continue_type == "resume" else Path(checkpoint_path) if checkpoint_path is not None else None
    if source_checkpoint is None:
        raise ValueError("CHECKPOINT_PATH is required when CONTINUE_TYPE='branch'")
    if not source_checkpoint.is_dir():
        raise FileNotFoundError(f"Checkpoint directory not found: {source_checkpoint}")
    step = parse_checkpoint_step(source_checkpoint)

    if continue_type == "resume":
        destination_checkpoint = output_root / f"checkpoint-{step}"
        if source_checkpoint.parent.resolve() == output_root.resolve() and _has_later_checkpoints(output_root, step):
            raise ValueError(
                f"Refusing to resume historical checkpoint {source_checkpoint}: later checkpoints exist under {output_root}. Use CONTINUE_TYPE='branch' to start from an older checkpoint."
            )
        if checkpoint_path is None:
            return ContinuePlan("resume", source_checkpoint, source_checkpoint, step, source_checkpoint, False, False, False)
        copied_checkpoint = _copy_full_checkpoint(source_checkpoint, destination_checkpoint)
        copied_tb = _copy_tensorboard_for_resume(_source_output_root(source_checkpoint), output_root)
        copied_metrics = copy_and_prune_test_metrics(
            source_output_dir=_source_output_root(source_checkpoint),
            destination_output_dir=output_root,
            test_metrics_json_name=test_metrics_json_name,
            max_step=step,
            metadata_updates={"continue_type": "resume", "resolved_checkpoint_path": str(destination_checkpoint)},
        )
        return ContinuePlan("resume", source_checkpoint, destination_checkpoint, step, destination_checkpoint, copied_checkpoint, copied_tb, copied_metrics)

    _ensure_no_existing_checkpoints(output_root, continue_type="branch")
    destination_checkpoint = output_root / _branch_checkpoint_name(source_checkpoint)
    copied_checkpoint = copy_branch_adapter_files(source_checkpoint, destination_checkpoint)
    copied_tb = False
    copied_metrics = copy_and_prune_test_metrics(
        source_output_dir=_source_output_root(source_checkpoint),
        destination_output_dir=output_root,
        test_metrics_json_name=test_metrics_json_name,
        max_step=step,
        metadata_updates={"continue_type": "branch", "branched_from_checkpoint": str(source_checkpoint)},
    )
    return ContinuePlan("branch", source_checkpoint, destination_checkpoint, step, None, copied_checkpoint, copied_tb, copied_metrics)


def _training_args_to_dict(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    args = torch.load(path, map_location="cpu", weights_only=False)
    if hasattr(args, "to_dict"):
        return dict(args.to_dict())
    if hasattr(args, "__dict__"):
        return dict(args.__dict__)
    raise ValueError(f"Unsupported training_args.bin content at {path}")


def collect_resume_arg_mismatches(checkpoint: str | Path, current_args: Any) -> list[tuple[str, Any, Any]]:
    old_args = _training_args_to_dict(Path(checkpoint) / "training_args.bin")
    if hasattr(current_args, "to_dict"):
        new_args = dict(current_args.to_dict())
    else:
        new_args = dict(getattr(current_args, "__dict__", {}))
    mismatches: list[tuple[str, Any, Any]] = []
    for name in RESUME_ARG_NAMES:
        if name in old_args and name in new_args and old_args[name] != new_args[name]:
            mismatches.append((name, old_args[name], new_args[name]))
    return mismatches


def format_resume_mismatch_markdown(mismatches: Iterable[tuple[str, Any, Any]]) -> str:
    lines = [
        "## Resume Training Argument Mismatch",
        "",
        "The checkpoint training arguments differ from the current config:",
        "",
    ]
    for name, old, new in mismatches:
        lines.append(f"- {name}: {old} -> {new}")
    lines.extend(["", "Continue resume with current config? [y/N]"])
    return "\n".join(lines)


def confirm_resume_arg_mismatches(
    *,
    checkpoint: str | Path,
    current_args: Any,
    input_fn: Callable[[str], str] = input,
    print_fn: Callable[[str], None] = print,
) -> None:
    mismatches = collect_resume_arg_mismatches(checkpoint, current_args)
    if not mismatches:
        return
    print_fn(format_resume_mismatch_markdown(mismatches))
    answer = input_fn("").strip().lower()
    if answer not in {"y", "yes"}:
        raise RuntimeError("Aborted resume because training arguments differ from checkpoint")


def prepare_lora_model_for_continue(
    *,
    continue_plan: ContinuePlan,
    base_model_factory: Callable[[], Any],
    fresh_lora_factory: Callable[[Any], Any],
) -> Any:
    """Build a PEFT model according to the resolved continue plan."""

    base_model = base_model_factory()
    if continue_plan.continue_type == "branch":
        from peft import PeftModel

        if continue_plan.resolved_checkpoint is None:
            raise ValueError("Branch continue plan requires resolved_checkpoint")
        return PeftModel.from_pretrained(base_model, str(continue_plan.resolved_checkpoint), is_trainable=True)
    return fresh_lora_factory(base_model)
