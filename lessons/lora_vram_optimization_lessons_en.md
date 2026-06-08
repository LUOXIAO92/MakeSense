English | [简体中文](lora_vram_optimization_lessons_zh-cn.md) | [日本語](lora_vram_optimization_lessons_ja.md) | [한국어](lora_vram_optimization_lessons_ko.md)

# LoRA VRAM Optimization Notes

Training environment:
- System: WSL2
- CPU: AMD Ryzen 9 9950X
- RAM: 128GiB DDR5
- GPU: Nvidia RTX 5090

## 1. Failures

### Problem 1: VRAM started too high

The first implementation used PEFT's generic `prepare_model_for_kbit_training(...)` before k-bit LoRA training. That helper casts floating-point parameters outside the 4-bit path to fp32. For a multimodal model, that policy can expand large modules that should stay in bf16, including the audio encoder, vision/video encoder, embeddings, and LM head. On smaller models, embeddings and the LM head already take a large share of memory, so fp32 casting changes the VRAM profile a lot.

Gemma 4 E2B / 4B adds another important case: it has a per-layer embedding lookup module. That module is an embedding / lookup table, not a Linear layer, so normal 4-bit Linear quantization does not touch it. The weight has about 2.3B parameters. In bf16, it already takes about 4.38GiB. If a generic preparation helper casts it to fp32, the memory cost jumps again.

The measurements matched that failure mode:
- After model load: allocated ~= 6.70GiB
- After the generic PEFT preparation helper: allocated ~= 12.43GiB
- At `train_lora` entry: allocated ~= 12.52GiB

That extra 5GiB+ appeared before dataset work could explain it. The model preparation step had expanded large non-4-bit parameters to fp32.

### Problem 2: Reserved CUDA memory kept growing during training and the run slowed down

During training, PyTorch reported a large gap between allocated memory and reserved memory:
- allocated ~= 12.77GiB
- max_allocated ~= 20.25GiB
- reserved ~= 32.86GiB

Those numbers mean the 30GiB+ driver-visible footprint did not consist only of live tensors. PyTorch's allocator held a large amount of memory as cache, workspace, or fragmented blocks. Even so, the effect was real. Without controlling reserved memory growth, training behaved like it had fallen into CPU offload territory and slowed to about `25s/it`. After limiting cache growth, throughput returned to about `6-7s/it` with 16 gradient accumulation steps.

## 2. Fixes

### Fix 1: Replace the generic PEFT preparation helper with the project-specific multimodal helper

The fix removed PEFT's `prepare_model_for_kbit_training(...)` and used the project helper instead:

```python
prepare_multimodal_model_for_kbit_lora_training(...)
```

That helper keeps only the preparation steps needed for LoRA training:
- freeze the base model
- disable `use_cache`
- enable input gradients
- enable gradient checkpointing
- avoid fp32-casting the audio / vision encoders, embeddings, LM head, and Gemma 4's large `embed_tokens_per_layer` lookup weights

After the change, the startup memory profile stayed flat:
- After model load: allocated ~= 6.70GiB
- After the project preparation helper: allocated ~= 6.70GiB
- After adding the LoRA adapter: allocated ~= 6.79GiB
- At `train_lora` entry: allocated ~= 6.79GiB

The fix did not skip LoRA preparation. It stopped the preparation step from widening multimodal modules, embedding / LM-head weights, and Gemma 4's per-layer lookup weights to fp32.

### Fix 2: Keep `CUDA_EMPTY_CACHE_STEPS = 1` for this training setup

The reserved-memory issue came from allocator-held memory, not live tensors alone. The current fix calls `torch.cuda.empty_cache()` after optimizer steps on a fixed cadence. The active setting is:

```python
CUDA_EMPTY_CACHE_STEPS = 1
```

This setting does not reduce the memory used by live tensors. It releases memory that PyTorch no longer needs but still holds in its CUDA allocator cache. In this run, the measured impact was large:
- Without limiting reserved memory: about `25s/it`
- With `CUDA_EMPTY_CACHE_STEPS=1`: about `6-7s/it`

For the current full LoRA training configuration, keeping `CUDA_EMPTY_CACHE_STEPS = 1` makes the run usable.

## 3. Final status

| Issue | Status | Evidence |
| --- | --- | --- |
| fp32 expansion from PEFT's generic preparation helper | **Solved** | Allocated VRAM stays at `6.70GiB` before and after preparation |
| LoRA adapter memory | **Not a problem** | The adapter adds only about `0.09GiB` |
| Reserved/cache growth slowing training | **Solved to a usable state** | `CUDA_EMPTY_CACHE_STEPS=1` improves speed from about `25s/it` to `6-7s/it` |
| Remaining baseline memory | **Expected and out of scope for this pass** | It mostly comes from resident model parameters such as bf16 lookup / embedding weights |

The new preparation path removes the startup VRAM spike. `CUDA_EMPTY_CACHE_STEPS=1` keeps reserved-cache growth under control for the current configuration. The remaining VRAM usage comes mostly from the model's resident parameters, so it does not belong to this bug.

## 4. Checks that ruled out other explanations

### Dataset rows did not move wholesale to GPU

GPU memory did not rise during dataset construction, row materialization, or Trainer initialization. Dataset rows also did not keep long-lived tensors.

### Padding to `MAX_SEQ_LENGTH=16000` did not cause it

The collator uses dynamic padding. It does not pad every sample to `MAX_SEQ_LENGTH=16000`. Observed sample lengths were around `1.6k-1.8k` tokens.

### Audio features could not explain the pressure

The processor produced audio features at MiB scale, not GiB scale. They cannot explain 10GiB+ of VRAM pressure.

### `use_cache=True` did not drive the spike

The current training preparation function disables `use_cache`, which is the right training behavior. The measurements did not point to `use_cache=True` as the main reason for the VRAM spike in this investigation.

### The remaining large embedding / lookup weights need a different kind of work

Gemma 4 E2B / 4B includes a large per-layer embedding lookup weight:

```text
embed_tokens_per_layer.weight ~= 2.3B parameters ~= 4.38GiB bf16
```

That weight belongs to an embedding / lookup table, not a Linear layer, so the current 4-bit Linear quantization path does not quantize it. Reducing this part of memory would require custom embedding / lookup quantization or a model-structure change. That work would go beyond the safe scope of this investigation.

## Summary

This pass fixed two concrete problems:
- Removing PEFT's generic preparation helper eliminated the fp32 VRAM expansion and reduced startup allocated memory from `12.52GiB` to `6.79GiB`.
- Keeping `CUDA_EMPTY_CACHE_STEPS=1` controlled reserved-memory growth during training and restored speed from about `25s/it` to `6-7s/it`.
