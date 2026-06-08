[English](lora_vram_optimization_lessons_en.md) | 简体中文 | [日本語](lora_vram_optimization_lessons_ja.md) | [한국어](lora_vram_optimization_lessons_ko.md)

# LoRA 显存优化心得

训练环境:
- System: wsl2
- CPU: AMD Ryzen 9 9950x
- RAM: 128GiB ddr5
- GPU: Nvidia RTX 5090

## 1. 出现的问题

### 问题一：训练开始前显存就异常偏高

最开始是直接使用 PEFT 的通用函数 `prepare_model_for_kbit_training(...)` 来准备 k-bit LoRA 训练。可是这个函数会把非 4bit 的浮点参数转成 fp32。这个策略对多模态模型风险很大：音频编码器、视觉/视频编码器、embedding、lm head 等模块都可能被放大。对小模型来说，embedding 和 lm head 原本占比就不低，一旦转成 fp32，会显著提高它们在总显存里的占比。

Gemma 4 E2B / 4B 家族还有一个额外特殊点：它有一个 per-layer embeddings 查表模块，属于 embedding/lookup table，不是 Linear，因此普通 4bit Linear quantization 不会处理它。这块总参数量约 2.3B，bf16 下已经约 4.38GiB；如果再被通用准备函数转成 fp32，显存会进一步大幅增加。

当时观察到的现象是：
- 模型刚加载完: allocated≈6.70GiB
- PEFT 通用准备函数执行后: allocated≈12.43GiB
- 进入 train_lora 时: allocated≈12.52GiB

也就是说，启动阶段多出来的 5GiB+ 显存，不是数据集造成的，而是模型准备阶段把大块参数转成 fp32 造成的。

### 问题二：训练过程中显存预留缓存持续膨胀，速度明显变慢

训练过程中，实际占用显存（allocated）和 PyTorch 预留显存缓存（reserved/cache）差距很大。典型观察是：
- 际占用显存 allocated≈12.77GiB
- 史峰值 max_allocated≈20.25GiB
- 留显存 reserved≈32.86GiB


这说明 30GiB+ 的 driver-visible 显存并不全是正在使用的 tensor，其中很大一部分是 PyTorch allocator 保留下来的缓存、workspace 或碎片。这个问题虽然不是“真实 tensor 占了 30GiB”，但它会带来实际后果：不限制时训练明显像发生了 CPU offload，速度掉到约 `25s/it`；限制缓存增长后速度恢复到约 `6–7s/it`(16梯度累积步)。

## 2. 如何解决

### 解决一：不用 PEFT 通用准备函数，改用项目自己的多模态准备函数

处理方式是移除 PEFT 的 `prepare_model_for_kbit_training(...)`，改用项目自己的：
```python
prepare_multimodal_model_for_kbit_lora_training(...)
```

这个函数只保留 LoRA 训练必须的准备动作：

- 冻结 base model
- 关闭 `use_cache`
- 启用 input gradients
- 启用 gradient checkpointing
- 避免把音频/视觉编码器、embedding、lm head，以及 Gemma 4 的 `embed_tokens_per_layer` 这类巨大查表参数整体转成 fp32

修改后的效果：
- 模型刚加载完: allocated≈6.70GiB
- 项目自有准备函数执行后: allocated≈6.70GiB
- LoRA adapter 加上后: allocated≈6.79GiB
- 进入 train_lora 时: allocated≈6.79GiB

也就是说，原来由通用准备函数造成的 5GiB+ 显存上涨被消掉了。这里的关键不是少做了 LoRA 训练准备，而是避免把不该转成 fp32 的多模态模块、embedding/lm head 和 Gemma 4 特有的 per-layer embeddings 查表模块放大。

### 解决二：保留 `CUDA_EMPTY_CACHE_STEPS = 1`，控制训练中的预留缓存增长

对训练过程中 reserved/cache 膨胀的问题，处理方式是在 optimizer step 结束后定期调用 `torch.cuda.empty_cache()`，释放 PyTorch 没有继续使用、但还预留在 allocator 里的显存缓存。当前配置是 `CUDA_EMPTY_CACHE_STEPS = 1`。这个设置不会减少正在使用的 tensor 显存，但会减少 driver 看到的预留显存压力。实测结果：
- 不限制预留缓存: ~25s/it
- CUDA_EMPTY_CACHE_STEPS=1: ~6–7s/it

因此，对当前这次完整 LoRA 训练配置来说，`CUDA_EMPTY_CACHE_STEPS = 1` 是有效的。

## 3. 最终解决了没有

| 问题 | 结果 | 证据 |
| --- | --- | --- |
| PEFT 通用准备函数导致 fp32 膨胀 | **已解决** | 准备函数执行前后都保持 `6.70GiB`，不再上涨 |
| LoRA adapter 显存是否异常 | **不是问题** | adapter 只增加约 `0.09GiB` |
| 训练中 reserved/cache 膨胀导致速度变慢 | **已解决到可用状态** | `CUDA_EMPTY_CACHE_STEPS=1` 后从约 `25s/it` 恢复到 `6–7s/it` |
| 剩余的基础显存占用 | **没有消除，也不应该在本轮处理** | 主要是模型本身的 resident 参数，例如 bf16 lookup/embedding 参数 |

结论：

- 启动阶段异常显存已经解决。
- 训练过程中的缓存膨胀问题，在当前配置下已经通过 `CUDA_EMPTY_CACHE_STEPS=1` 解决到可正常训练的状态。
- 剩下的显存主要是模型结构本身需要的 resident memory，不属于这次 bug。

## 4. 哪些方向确认不是问题

### 不是数据集整体进 GPU

数据集构建、rows materialization、Trainer 初始化前后，GPU 显存没有上涨；dataset rows 里也没有长期持有 tensor。

### 不是 padding 到导致的

当前 collator 使用动态 padding，不是把每条样本都 pad 到 `MAX_SEQ_LENGTH=16000`。实际观察到的样本长度大约是 `1.6k–1.8k` tokens。

### 不是 audio features 过大导致的

processor 产生的 audio features 是 MiB 级，不是 GiB 级，不能解释 10GiB+ 的显存压力。

### `use_cache=True` 不是主要根因

当前训练准备函数会关闭 `use_cache`，这是合理的训练设置。但这次没有证据表明 `use_cache=True` 是显存暴涨的主要原因。

### 剩余的大 embedding/lookup 参数不是本轮要解决的问题

Gemma 4 E2B / 4B 家族里有一块额外的 per-layer embeddings 查表参数：

```
embed_tokens_per_layer.weight ≈ 2.3B parameters ≈ 4.38GiB bf16
```

它属于 embedding/lookup table，不是 Linear 层，所以不会被当前 4bit Linear quantization 量化。继续压这部分显存需要自定义 embedding/lookup quantization 或模型结构级处理，这会超出本研究的的安全范围。

## 总结

这次真正解决了两个问题：
- 去掉 PEFT 通用准备函数造成的 fp32 显存膨胀，把启动显存从 `12.52GiB` 降到 `6.79GiB`
- 同时用 `CUDA_EMPTY_CACHE_STEPS=1` 控制训练中预留显存缓存膨胀，把速度从约 `25s/it` 恢复到 `6–7s/it`
