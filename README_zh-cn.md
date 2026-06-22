[English](README.md) | 简体中文 | [日本語](README_ja.md) | [한국어](README_ko.md)

# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense 是一个面向研究和数据生成的项目，用来为同步语音翻译模型构建具备语义感知能力的训练数据和验证流程，同时支持自动语音识别 / 转写任务。

项目的核心思路是把语音翻译整理成增量式多轮对话：音频一段一段到达，模型需要学会什么时候输出源语言转写、什么时候输出目标语言翻译，以及什么时候继续等待更多上下文。

目前，仓库已经提供数据集构建流程和训练数据构造工具。热词 / 指定译法支持以及推理后端仍是后续计划。

## 项目简介

目标：训练一个全模态 / 多模态模型，使其具备流式同步语音翻译能力，同时保留自动语音识别 / 转写能力。

本项目受到以下论文启发：
- 无限输入窗口 / time-pressure 同步翻译：[InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation：[SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

在本项目中：
- **不**从零训练语义单元检测器、音频编码器，也不做 LLM 主干对齐；
- **不**修改模型架构；无限时长的流式翻译通过运行时的滑动窗口上下文管理来实现；
- **会**构建接近标准答案的数据集和流程验证机制，让全模态模型学习同步翻译策略；

## 环境要求

### 克隆仓库
```bash
git clone --recursive https://github.com/LUOXIAO92/MakeSense.git
```

### Python 依赖

用于数据集准备：
- 建议单独创建一个 Python 环境。数据集准备依赖 `qwen-asr`，而 `qwen-asr` 与较新的 `transformers` 版本不兼容，因此不要和训练环境混用。
- Flash Attention 可参考预编译 wheel：[Flash attention prebuild wheels](https://github.com/mjun0812/flash-attention-prebuild-wheels)
```bash
pip install whisper openai stanza
pip install qwen-asr --force-reinstall
pip install torch==2.10 torchaudio==2.10.0 torchvision --force-reinstall # --index-url https://download.pytorch.org/whl/cu130
```

用于训练：
- 训练环境可以使用 Python 3.13。
```bash
pip install stanza jieba nagisa transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard
pip install git+https://github.com/LUOXIAO92/MultimodalAssistantMask.git
```

### 子模块依赖
- 词对齐工具：[TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- 词对齐默认使用 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) 作为基础模型。
- 多模态输入的仅助手侧损失通过 [MultimodalAssistantMask](https://github.com/LUOXIAO92/MultimodalAssistantMask.git) 构造。

## 流程

### 源语言 / 转写侧
1. 从元数据初始化缓存记录
2. 可选的自动语音识别转写
3. 强制对齐
4. 有时间压力的源语言语义单元分段

### 目标语言 / 翻译侧
1. 原始译文生成
2. 翻译重建
3. 纯文本目标语语义单元分段
4. 以目标侧为中心的源侧映射
5. 最终数据集收集与导出

### 时间漂移与对齐词分组

强制对齐模型可能在语音末尾产生轻微时间漂移，因此最后几个对齐标记的结束时间有时会超过真实音频时长。

MakeSense 将这种情况视为可预期的尾部漂移，而不是致命的对齐错误。流式释放窗口仍然由真实音频时长和配置的窗口大小定义。当尾部标记漂移到真实时长之后时，下游阶段会把这些尾部标记吸收到最后一个释放窗口中，而不是额外创建窗口，也不会仅因为这个原因拒绝整条记录。

这个尾部漂移容忍并不取消强制对齐输出内部的时间因果校验。相邻的原始带时间标记仍应保持单调：前一个标记的结束时间不应晚于后一个标记的开始时间。默认情况下，如果这个相邻标记顺序被破坏，MakeSense 会拒绝该记录。Pipeline 4 也提供一个默认关闭的可选修复开关，用于处理小的边界漂移：启用后，如果重叠可恢复，即 `next.start < prev.end < next.end`，会通过设置 `next.start = prev.end` 修复。像 `prev.end == next.start == next.end` 这样的相接零时长后续标记会被接受。如果重叠会在修复后让下一个标记变成零长度或负长度（`prev.end >= next.end` 且 `prev.end > next.start`），该强制对齐结果会作为该记录的校验失败被拒绝，同时其他记录仍可继续处理。

构造训练数据时，如果音频时长短于 `window_count × window_size`，音频输入会补齐到对应窗口长度。这样可以保持对话轮次、释放窗口和音频分块对齐，同时保留基于真实时长的窗口边界语义。

Pipeline 4 在 `alignment.tokens` 中保存强制对齐模型输出的带时间标记，同时在 `alignment.words` 中保存分词器把这些标记合并成词的分组。后续阶段使用这些词；Pipeline 8 的 `source_token_ids` 指的也是这些词的编号，而不是原始带时间标记的编号。

需要这一步分组，是因为 Qwen3-ForcedAligner 产生的标记粒度不一定等于后续阶段使用的词粒度。在 Qwen3-ForcedAligner 的处理中，中文和韩文会被处理成非常细的、接近字符级的带时间标记，因此分词器会把字符或其他细粒度标记合并成中文词，或者合并成韩文按空格 / 语节组织的词。日语比较特殊：Qwen3-ForcedAligner 对日语使用 `nagisa` 分词器产生带时间标记，而 MakeSense 生成 `alignment.words` 时可能使用项目中配置的另一个分词器，所以日语也会因为分词边界不完全一致而发生标记合并。对这些情况，MakeSense 有意采用保守的时间策略。流式同传依赖严格的时间因果关系，因此流程不会把一个带时间标记的时间轴切开，再人为创造更细的时间戳分配给多个词。相反，当多个带时间标记被合并成一个词时，这个词使用第一个标记的开始时间和最后一个标记的结束时间。这样可以避免制造不可靠的人工时间边界，防止破坏流式输出的因果关系。

## 使用方法：运行完整数据集流程

当前工作流由 `examples/` 下的阶段脚本驱动。每个阶段读取上一阶段的缓存，写入新的阶段缓存，并且可以基于已有 JSONL 缓存继续运行。

运行前请先检查**每个示例脚本顶部的配置区块**。常见配置包括数据集 / 缓存路径、模型名称、目标语言、`TOP_P`、服务商相关的 `EXTRA_BODY`，以及适用场景下的 `ENABLE_VISUALIZATION`。

`EXTRA_BODY` 会原样透传给兼容 OpenAI 的对话补全请求，用于承载不同服务商的扩展参数。`top_k`、思考 / 推理开关等参数在不同服务中的结构不完全相同，因此这里列出几种服务商专用配置示例：

```python
# vLLM / local OpenAI-compatible API 示例：
EXTRA_BODY = {"top_k": 20, "chat_template_kwargs": {"enable_thinking": False}}

# OpenRouter reasoning 示例：
EXTRA_BODY = {"reasoning": {"effort": "none"}}

# DeepSeek thinking 示例：
EXTRA_BODY = {"thinking": {"type": "disabled"}}
```

参考文档：
- OpenRouter reasoning tokens: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens
- DeepSeek thinking mode: https://api-docs.deepseek.com/guides/thinking_mode

### 当前可用功能

已经可用：
- 数据集构建流程，可运行到最终第 9 阶段 JSONL 导出；
- 通过 `src/data_loader` 从最终数据集构造训练样本；
- 通过 `examples/train_lora.py` 和 `src/train` 提供初版真实音频 LoRA 训练入口；
- **NEW**：[MakeSense-Emilia-Dataset](https://huggingface.co/datasets/luoxiao9231/MakeSense-Emilia-Dataset)，许可证：cc-by-nc-4.0
  - 该数据集包含 8,000 条音频 / 转写记录，以及 24,000 条用于训练翻译策略的多轮对话轨迹记录。
  - 数据基于 [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) 二次处理而来。感谢 Emilia-Dataset 项目提供高质量的多语言音频数据。

待办：
- [x] **高优先级**：用极小样本跑通 `examples/train_lora.py`，确认对话渲染、仅助手侧损失和 1-2 个训练步骤正常。
- [x] **高优先级**：完成 `google/gemma-4-E2B-it` 的完整 LoRA 训练。
  - **已完成**：初步的 `gemma-4-E2B-it` 大规模训练和测评，[lora 放在这里](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000)。详细数据请参照后半部分结果的指标小节。
  - **进行中**：目前仍在调试更合适的超参数并优化显存使用。
- [ ] **次高优先级：** 增加推理后端，用于运行训练好的流式模型。
  - **进行中**：推理侧的实现正在 [MakeSense-Inference](https://github.com/LUOXIAO92/MakeSense-Inference.git) 中推进。
- [ ] 为训练和推理上下文增加热词和指定译法支持。

### LoRA 训练入口

默认 LoRA 训练示例面向 `google/gemma-4-E2B-it`。训练代码基于 Transformers 多模态模型和 PEFT LoRA，直接使用真实音频分块；训练过程会写入项目自管的 TensorBoard 标量日志，并运行严格的流式测试指标。

数据集、模型、LoRA、检查点和监控相关选项都在下面这个脚本顶部配置：

```text
examples/train_lora.py
```

常用配置包括：
- `OUTPUT_DIR`
- `CONTINUE_TYPE`：`none`、`resume` 或 `branch`
- `CHECKPOINT_PATH`
- `SAVE_PROCESSOR`
- `TEST_STEPS`、`TEST_MAX_NEW_TOKENS`、`TEST_RECORD_COUNT`

运行训练：

```bash
PYTHONPATH=src python examples/train_lora.py
```

训练会把 LoRA 适配器、检查点和监控文件写入配置的 `OUTPUT_DIR`：

```text
outputs/makesense_lora/
├── adapter_config.json
├── adapter_model.safetensors
├── checkpoint-*/
├── runs/
│   └── <yyyy-mm-dd_hh-mm-ss>/
└── test_metrics.json
```

严格流式测试会限制每个助手轮次的可见上下文：模型只能使用截至该轮次已经到达的音频分块。测试记录数由 `examples/train_lora.py` 里的 `TEST_RECORD_COUNT` 控制：`0` 表示不跑测试，`-1` 表示使用完整测试集，正整数表示最多选取对应数量的记录。

### 定制化配置
如需调整流程级别的非训练配置，请参考 `src/configs/config.py` 和 `src/configs/LANGUAGE_PACK_*.py`。常见可定制内容包括数据采样范围、支持语言、ASR / 强制对齐模型、分词器、等待标记、流式窗口大小、最大分块大小、重建验证器使用的高噪声标记，以及各语言的语言包 / 少样本示例。

### 流程 运行顺序

按以下顺序运行各阶段：

```bash
export PYTHONPATH=src

# 1. 如有需要，下载 / 准备数据集源数据。（这里使用 Emilia dataset，参考 https://huggingface.co/datasets/amphion/Emilia-Dataset）
python examples/pipeline_1_download_Emilia.py

# 2. 从数据集元数据初始化 PipelineRecord 缓存分片。
python examples/pipeline_2_initialize_cache.py

# 3a-1. 推荐的 ASR 路径。
# 这一步会在 cache 中补齐源语言转写结果。
python examples/pipeline_3_a1_asr.py

# 3a-2. 推荐的基于 ASR 的原始译文生成路径。
# 根据实测，在中文、日文、韩文三种语言上，先做 ASR 再用 omni/audio-assisted translation 辅助纠错，通常都比直接用 omni 模型做 ASR 精度更高、更稳。
python examples/pipeline_3_a2_asr_text_translation.py

# 3b. 可选的 direct omni ASR + translation 路径。
# 用于测试 one-pass multimodal translation 行为。
python examples/pipeline_3_b_asr_translation_omni.py

# 4. 对源语言转写执行强制对齐。
python examples/pipeline_4_forced_alignment.py

# 5. Time-pressure source sense-unit segmentation。
python examples/pipeline_5_asr_segmentation.py

# 6. Translation reconstruction。
python examples/pipeline_6_translation_reconstruction.py

# 7. Pure-text target sense-unit segmentation。
python examples/pipeline_7_pure_text_segmentation.py

# 8. 将 target sense units 映射到 source token ids。
python examples/pipeline_8_target_centric_mapping.py

# 9. 从已完成的第 8 阶段缓存中收集 / 导出最终数据集。
python examples/pipeline_9_collect_dataset.py
```

推荐顺序：

```bash
python examples/pipeline_2_initialize_cache.py
python examples/pipeline_3_a1_asr.py
python examples/pipeline_3_a2_asr_text_translation.py
python examples/pipeline_4_forced_alignment.py
python examples/pipeline_5_asr_segmentation.py
python examples/pipeline_6_translation_reconstruction.py
python examples/pipeline_7_pure_text_segmentation.py
python examples/pipeline_8_target_centric_mapping.py
python examples/pipeline_9_collect_dataset.py
```

### 最终数据集输出

第 9 阶段导出如下最终数据集结构：

```text
path/to/output/dir/
├── dimensional_analysis/
│   ├── EN/dimensional_analysis-EN-partXXXXXX.jsonl
│   ├── JA/dimensional_analysis-JA-partXXXXXX.jsonl
│   ├── KO/dimensional_analysis-KO-partXXXXXX.jsonl
│   └── ZH/dimensional_analysis-ZH-partXXXXXX.jsonl
├── transcription/
│   ├── EN/transcription-EN-partXXXXXX.jsonl
│   ├── JA/transcription-JA-partXXXXXX.jsonl
│   ├── KO/transcription-KO-partXXXXXX.jsonl
│   └── ZH/transcription-ZH-partXXXXXX.jsonl
└── translation/
    ├── EN/translation-EN_JA-partXXXXXX.jsonl
    ├── EN/translation-EN_KO-partXXXXXX.jsonl
    ├── EN/translation-EN_ZH-partXXXXXX.jsonl
    └── ...
```

`dimensional_analysis/` 是对翻译阶段生成的整句级 `target.shared.translation_analysis` 的独立导出。它与转写 / 翻译数据集结构分开保存。

## 输出格式

### 流式模型输出

```text
<src>(transcription text)</src><tgt>(target translation text)</tgt>
```

当信息还不足以稳定输出源语言转写或目标语言翻译时，模型可以输出 `<|wait|>`。

### 对话格式

```text
system
[system prompts]
[hot words / task context]
user
<|audio|>
assistant
<src>(transcription text or <|wait|>)</src><tgt>(target translation text or <|wait|>)</tgt>
user
<|audio|>
assistant
<src>(next transcription text or <|wait|>)</src><tgt>(next target translation text or <|wait|>)</tgt>
...
```

## 推理框架说明：并发多模态生成中的约束解码

下面的大规模验证结果是 `batch=1` 的真实测试结果。它们评估的是单条样本的真实 rollout：每一轮生成的模型输出都会被放回下一轮提示词。因此，这些结果反映的是没有并发 / 批处理生成影响时的协议遵守情况。这是当前大规模训练后的验证记录，不表示超参数已经达到最优。

只要存在并发或批处理生成，就会有额外风险：同一个请求单独运行和放进 batch 运行时，下一 token 的候选分数可能不完全一致；当候选分数接近时，第一或第二偏好的 token 可能交换位置。这会影响采样，也可能让协议化输出偏离允许格式。本次多批次 vs 单批次调查中，Gemma4 音频文本的这种风险比对照模型和纯文本基线更明显。因此本项目构建推理后端时候会使用约束解码，例如 vLLM guided decoding / structured outputs 或 llama.cpp GBNF grammar，把输出限制在目前支持的六种协议形式内。详情见 [Gemma 4 multimodal batch-rank note](lessons/gemma4_multimodal_batch_rank_en.md)。

## 大规模验证结果 (`google/gemma-4-E2B-it`, `train_examples: 21540`):

### 训练参数

```text
Dataset
  - TRAIN_EXAMPLES: 21540
  - VALIDATE_EXAMPLES: 2400
  - TEST_EXAMPLES: 60

Audio
  - AUDIO_SAMPLING_RATE: 16000
  - AUDIO_CHUNK_SECONDS: 1.0

Training Steps
  - PER_DEVICE_TRAIN_BATCH_SIZE: 2
  - PER_DEVICE_EVAL_BATCH_SIZE: 2
  - GRADIENT_ACCUMULATION_STEPS: 8
  - EFFECTIVE_BATCH_SIZE: 16
    `PER_DEVICE_TRAIN_BATCH_SIZE: 2 * GRADIENT_ACCUMULATION_STEPS: 8`
  - OPTIMIZER_STEPS_PER_EPOCH: 1347
    `ceil(TRAIN_EXAMPLES: 21540 / EFFECTIVE_BATCH_SIZE: 16)`
  - CONFIGURED_NUM_TRAIN_EPOCHS: 1
  - CONFIGURED_MAX_STEPS: -1
  - TOTAL_OPTIMIZER_STEPS: 16155
    `OPTIMIZER_STEPS_PER_EPOCH: 1347 * CONFIGURED_NUM_TRAIN_EPOCHS: 5`

Hyper Parmeters
  - LEARNING_RATE: 1e-4
  - WEIGHT_DECAY: 0.0
  - ADAM_BETA1: 0.9
  - ADAM_BETA2: 0.999
  - MAX_GRAD_NORM: 1.0
  - NUM_TRAIN_EPOCHS: 1 (stop at 15000 step / total 16155)
```

![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/training_metrics_plot.png)

### 结果

#### 指标说明

下面这些严格流式测试指标用于检查模型在流式对话中的协议遵守和释放策略。它们检查输出是否是完整协议单元（纯转写 `<src>...</src>` 或翻译 `<src>...</src><tgt>...</tgt>`），以及每个助手轮次中源语言侧 / 目标语言侧应该等待还是释放内容。它们不衡量 ASR 文字是否逐字正确，也不衡量翻译语义质量。

**PROTOCOL_ADHERENCE_RATE**

- 含义：模型输出完整遵守协议的轮次比例。
- 计算：`protocol_adherent_turns / TURN_COUNT`。
- 合格输出只能是完整的 `<src>...</src>` 或 `<src>...</src><tgt>...</tgt>`。
- `<src>` / `<tgt>` 内不能嵌套协议 tag。
- 闭合协议单元外不能有非空内容。
- 字段包含 `<|wait|>` 时，字段内容去掉首尾空白后必须等于 `<|wait|>`。
- 尾随文本、逗号拼接、重复协议块、错序 / 残缺 tag、wait 与其他字符混合都计为不遵守协议。

所有 source / target wait/release accuracy 指标都只使用 protocol-adherent 模型轮次作为分母基础。不遵守协议的模型轮次只影响 `PROTOCOL_ADHERENCE_RATE`。Fixed-window 和 conservative target 指标还保留 record-level window eligibility filter。

**RECORD_COUNT**

- 含义：本次严格流式测试实际评估的测试样本数。
- 计算：`len(records)`。

**SRC_RELEASE_ACCURACY**

- 含义：在标准答案要求源语言侧释放转写文本的轮次中，模型也选择释放源语言侧内容的比例。
- 计算：`src_release_correct / SRC_RELEASE_TOTAL`。这里只判断 `<src>...</src>` 是不是非等待标记，不检查释放出来的转写文本是否正确。

**SRC_RELEASE_TOTAL**

- 含义：标准答案中源语言侧应该释放内容的轮次数。
- 计算：统计标准答案的 `<src>...</src>` 不是 `<|wait|>` 的轮次。

**SRC_WAIT_ACCURACY**

- 含义：在标准答案要求源语言侧等待的轮次中，模型也输出源语言侧等待标记的比例。
- 计算：`src_wait_correct / SRC_WAIT_TOTAL`。这里只检查模型的 `<src>...</src>` 是否为 `<|wait|>`。

**SRC_WAIT_TOTAL**

- 含义：标准答案中源语言侧应该等待的轮次数。
- 计算：统计标准答案的 `<src>...</src>` 去掉首尾空白后正好等于 `<|wait|>` 的轮次。

**TGT_RELEASE_ACCURACY**

- 含义：在标准答案要求目标语言侧释放翻译的轮次中，模型也选择释放目标语言侧内容的比例。
- 计算：`tgt_release_correct / TGT_RELEASE_TOTAL`。这里只判断 `<tgt>...</tgt>` 是不是非等待标记，不检查释放出来的翻译是否语义正确。

**TGT_RELEASE_TOTAL**

- 含义：标准答案中目标语言侧应该释放翻译的轮次数。
- 计算：统计标准答案的 `<tgt>...</tgt>` 不是 `<|wait|>` 的轮次。

**TGT_WAIT_ACCURACY**

- 含义：在标准答案要求目标语言侧等待的轮次中，模型也输出目标语言侧等待标记的比例。
- 计算：`tgt_wait_correct / TGT_WAIT_TOTAL`。这里只检查模型的 `<tgt>...</tgt>` 是否为 `<|wait|>`。

**TGT_WAIT_TOTAL**

- 含义：标准答案中目标语言侧应该等待的轮次数。
- 计算：统计标准答案的 `<tgt>...</tgt>` 去掉首尾空白后正好等于 `<|wait|>` 的轮次。

**TURN_COUNT**

- 含义：所有被选中测试样本中，实际评估的助手轮次总数。
- 计算：对 `records` 中所有生成并评估过的助手输出求和。

#### Gemma-4-E2B-it, learning rate=1e-4, rank=16, batch size=16, bnb nf4 4bit, adamw

best overall - step 12000~15000 (early stop at step 15000)

- Average metrics:
![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/test_metrics_plot.png)

- Protocol adherence rate 
![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/condition_metrics_plots/condition_protocol_adherence_rate.png)

- Source release accuracy
![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/condition_metrics_plots/condition_src_release_accuracy.png)

- Source wait accuracy
![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/condition_metrics_plots/condition_src_wait_accuracy.png)

- Target release accuracy 
![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/condition_metrics_plots/condition_tgt_release_accuracy.png)

- Target wait accuracy 
![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/condition_metrics_plots/condition_tgt_wait_accuracy.png)

Please refer to [strict test](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics) to veiw the result of strict test.


## Test Outputs - step 300 (left) vs 15000 (right)

- tolerance window size: 1.0 s
- Selected examples compare step 300 and step 15000 outputs for the same README UID anchors.
- concurrency=90, so the process time is high
- In vLLM testing, multi-batch processing did not show the quality degeneration seen in the hand-built training-time prompt cache test.

### ASR

---

- UID: JA_A7kJ7PmPk8g_W000017

  SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>最初から</src>` | `<src>最初から</src>` | `<src>最初から</src>` |
  | 2 | `<src>あの</src>` | `<src>あの特に</src>` | `<src>あの特に</src>` |
  | 3 | `<src>特に</src>` | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` |
  | 4 | `<src>中まだ1年生からね。</src>` | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` |
  | 5 | `<src>はい、はい。</src>` | `<src>この時点で</src>` | `<src>この時点で</src>` |
  | 6 | `<src>その時点で</src>` | `<src>こう短く</src>` | `<src>こう短く</src>` |
  | 7 | `<src>こう</src>` | `<src>剪定を</src>` | `<src>剪定を</src>` |
  | 8 | `<src>資格を</src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 9 | `<src>とりあえず</src>` | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` |
  | 10 | `<src>資格を</src>` | `<src>十年経っても</src>` | `<src>十年経っても</src>` |
  | 11 | `<src>持っても</src>` | `<src>大した。</src>` | `<src>大した。</src>` |

---

- UID: ZH_B00041_S00155_W000028

  SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>家长需要</src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 2 | `<src>做的是</src>` | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` |
  | 3 | `<src>用我们</src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 4 | `<src>身上的爱胶水</src>` | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` |
  | 5 | `<src>是</src>` | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` |
  | 6 | `<src>是</src>` | `<src>施肥，</src>` | `<src>施肥，</src>` |
  | 7 | `<src>给儿子</src>` | `<src>给足</src>` | `<src>给足</src>` |
  | 8 | `<src>心里影响</src>` | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` |
  | 9 | `<src>给内心的</src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 10 | `<src>孩子慢慢</src>` | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` |
  | 11 | `<src>长大</src>` | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` |

---

- UID: KO_Djg2xNdyFCU_W000010

  SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>I am </src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 2 | `<src>Apple </src>` | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` |
  | 3 | `<src>fruit </src>` | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` |
  | 4 | `<src>pick and </src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 5 | `<src>eat </src>` | `<src>자신 의 </src>` | `<src>자신 의 </src>` |
  | 6 | `<src>your own </src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 7 | `<src>jogging </src>` | `<src>부모 를 죽인 페르 나 </src>` | `<src>부모 를 죽인 페르 나 </src>` |
  | 8 | `<src>heruna </src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 9 | `<src>pachang </src>` | `<src>박한상과 </src>` | `<src>박한상과 </src>` |
  | 10 | `<src>and </src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 11 | `<src>four generations </src>` | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` |

---

- UID: EN_nUuwxonVyYE_W000054

  SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | `<src>What is your body </src>` |
  | 2 | `<src>saying? </src>` | `<src>doing? </src>` | `<src>doing? </src>` |
  | 3 | `<src>Drop pin to your body. </src>` | `<src>Drop into </src>` | `<src>Drop into </src>` |
  | 4 | `<src>Where does </src>` | `<src>your body. </src>` | `<src>your body. </src>` |
  | 5 | `<src>attention start? </src>` | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` |
  | 6 | `<src>What is it? Is it a </src>` | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` |
  | 7 | `<src>day? Cuz it's a </src>` | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` |
  | 8 | `<src>time in your chest. </src>` | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` |
  | 9 | `<src>I have a sob. </src>` | `<src>I ask them what </src>` | `<src>I ask them what </src>` |
  | 10 | `<src>Like which are you using? </src>` | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` |
  | 11 | `<src>Saying. </src>` | `<src>language are you using? </src>` | `<src>language are you using? </src>` |


### Conservative: 6 wait windows

---

- UID: JA_A7kJ7PmPk8g_W000017

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 6 wait windows before each target release.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` |
  | 2 | `<src>あの、特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>中まだ1年</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>はい、その時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>こう</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>四角線で</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>剪定を</src><tgt>从一开始，特别是现在才一年级。这个时候</tgt>` |
  | 8 | `<src>こう</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>対数してい</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>上げる</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>と10年経っても</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` |

---

- UID: ZH_B00041_S00155_W000028

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 6 wait windows before each target release.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>家长需要</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 2 | `<src>做的是</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>用我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>湿气</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>湿气</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>去阻止孩子</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt>What parents need to do is this: water and fertilize with our deep love,</tgt>` | `<src>给足</src><tgt>What parents need to do is water and fertilize with our deep love,</tgt>` |
  | 8 | `<src>心瘾</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>影响</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>你的孩子慢慢</src><tgt><\|wait\|></tgt>` | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` |

---

- UID: KO_Djg2xNdyFCU_W000010

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 6 wait windows before each target release.

  - TGT_METRICS: filtered (max_empty_window=8 > requested_window=6)

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>I am </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>apple, </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>축 썰기 고. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>자신의 모로 조깅 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` |
  | 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>같은 세대들이 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>입니다. </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt>They are the same generation that triggered the MEAP— the Park Han- sang who killed his own parents.</tgt>` |

---

- UID: EN_nUuwxonVyYE_W000054

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 6 wait windows before each target release.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` |
  | 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>saying, "Drop pin your body </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>where does </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>attention start? </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` |
  | 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>What is it is a day, </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>你的身体在做什么呢？进入你的身体里。紧张感从哪里开始？是什么感觉？是头痛吗？</tgt>` |
  | 8 | `<src>cause it's time </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>in your chest. </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>I have a sob, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>like which are you using, </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` |


### Fixed window: 6 wait windows

---

- UID: JA_A7kJ7PmPk8g_W000017

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>最初</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` |
  | 2 | `<src>から</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>あの、特に</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>中まだ1年生</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>ですからね。はい、</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>その時点で</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>こう</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>剪定を</src><tgt>从一开始，特别是现在才一年级。这个时候</tgt>` |
  | 8 | `<src>積極</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>に</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>持っていった</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>一年経っても</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` |

---

- UID: ZH_B00041_S00155_W000028

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>家长需要</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 2 | `<src>做的是</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>用我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>湿气</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>湿气</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>去阻止孩子</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt>What parents need to do is this: water and fertilize with our deep love,</tgt>` | `<src>给足</src><tgt>What parents need to do is water and fertilize with our deep love,</tgt>` |
  | 8 | `<src>心瘾</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>影响</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>你的孩子慢慢</src><tgt><\|wait\|></tgt>` | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` |

---

- UID: KO_Djg2xNdyFCU_W000010

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

  - TGT_METRICS: filtered (max_empty_window=8 > requested_window=6)

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>I am </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>어버이 척박히고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` |
  | 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>자신의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>모로 죽기 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>모로 죽기 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt>I am triggering the affair</tgt>` |
  | 8 | `<src>하려나 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>박한 상과 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>같은 세대들이 </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` |

---

- UID: EN_nUuwxonVyYE_W000054

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` |
  | 2 | `<src>saying, </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>drop pin to your body. </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>Where does </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>attention start? </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>What is it? Is it a </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>day? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>你的身体在做什么呢？进入你的身体里。紧张感从哪里开始？是什么感觉？是头痛吗？</tgt>` |
  | 8 | `<src>Is it time is in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>I have a sob, </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>lament which are you </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` |


### Natural

---

- UID: JA_A7kJ7PmPk8g_W000017

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt>一开始</tgt>` |
  | 2 | `<src>あの、特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>中まだ1年</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>就是，这个还没满一年呢。</tgt>` |
  | 5 | `<src>はい、その時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>この時点で</src><tgt>这时候</tgt>` |
  | 6 | `<src>こう</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>資格を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` |
  | 8 | `<src>こう</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>退職してあげると</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>こうタイズしてってあげると</src><tgt>如果把它剪短一点，收紧一点，</tgt>` |
  | 10 | `<src>10年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>十年経っても</src><tgt>就算过了十年，</tgt>` |
  | 11 | `<src>大丈夫だ。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>大した。</src><tgt>它也不会有事。</tgt>` |

---

- UID: ZH_B00041_S00155_W000028

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>家长</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 2 | `<src>需要做的是</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is</tgt>` |
  | 3 | `<src>用我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>湿气</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt>water- water our deep love,</tgt>` |
  | 6 | `<src>湿气</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>fertilize them,</tgt>` |
  | 7 | `<src>去阻止孩子</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` |
  | 8 | `<src>心瘾</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心理营养，</src><tgt>and provide our children with enough psychological nourishment,</tgt>` |
  | 9 | `<src>影响</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>你的孩子慢慢</src><tgt><\|wait\|></tgt>` | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>并耐心等待孩子</src><tgt>and patiently wait for them</tgt>` |
  | 11 | `<src>长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>慢慢长大。</src><tgt>to grow up slowly.</tgt>` |

---

- UID: KO_Djg2xNdyFCU_W000010

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>I am </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 2 | `<src>Apple </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` |
  | 3 | `<src>초밥 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` |
  | 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 5 | `<src>치키고 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` |
  | 6 | `<src>자신의 모로 조깅 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 7 | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` |
  | 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 9 | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` |
  | 10 | `<src>같은 세대들이 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>있답니다. </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>같은 세대 들입니다. </src><tgt>They are the same generation that triggered the MEAP— the Park Han- sang who killed his own parents.</tgt>` |

---

- UID: EN_nUuwxonVyYE_W000054

  SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

  | round | predict (300) | ground truth | predict (15000) |
  |---|---|---|---|
  | 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` |
  | 2 | `<src>saying, </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` |
  | 3 | `<src>drop pin to your body. </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` |
  | 4 | `<src>Where does </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>your body. </src><tgt>进入你的身体。</tgt>` |
  | 5 | `<src>attention start? </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>紧张感</tgt>` |
  | 6 | `<src>What is it? Is it a </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>从哪里开始？是什么？</tgt>` |
  | 7 | `<src>day? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` |
  | 8 | `<src>Is it time is in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是胸闷吗？</tgt>` |
  | 9 | `<src>I have a sob, </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>I ask them what </src><tgt>我问他们</tgt>` |
  | 10 | `<src>lament which are you used </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` |
  | 11 | `<src>saying. </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` |
