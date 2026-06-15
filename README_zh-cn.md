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
- [ ] **高优先级**：完成 `google/gemma-4-E2B-it` 的完整 LoRA 训练。
  - **已完成**：初步的 `gemma-4-E2B-it` 大规模训练和测评，[lora 放在这里](/lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100)。详细数据请参照后半部分结果的指标小节。
  - **进行中**：目前仍在调试更合适的超参数。
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
  - PER_DEVICE_TRAIN_BATCH_SIZE: 1
  - PER_DEVICE_EVAL_BATCH_SIZE: 5
  - GRADIENT_ACCUMULATION_STEPS: 16
  - EFFECTIVE_BATCH_SIZE: 16
    `PER_DEVICE_TRAIN_BATCH_SIZE: 1 * GRADIENT_ACCUMULATION_STEPS: 16`
  - OPTIMIZER_STEPS_PER_EPOCH: 1347
    `ceil(TRAIN_EXAMPLES: 21540 / EFFECTIVE_BATCH_SIZE: 16)`
  - CONFIGURED_NUM_TRAIN_EPOCHS: 5
  - CONFIGURED_MAX_STEPS: -1
  - TOTAL_OPTIMIZER_STEPS: 6735
    `OPTIMIZER_STEPS_PER_EPOCH: 1347 * CONFIGURED_NUM_TRAIN_EPOCHS: 5`

Hyper Parmeters
  - LEARNING_RATE: 2e-4
  - WEIGHT_DECAY: 0.0
  - ADAM_BETA1: 0.9
  - ADAM_BETA2: 0.999
  - MAX_GRAD_NORM: 1.0
  - NUM_TRAIN_EPOCHS: 5 (stop at 5400 step)
```

### 结果

#### 指标说明

下面这些严格流式测试指标主要用来检查模型在流式对话中的格式控制和释放策略：输出是否符合协议单元（纯转写 `<src>...</src>` 或翻译 `<src>...</src><tgt>...</tgt>`），生成是否在预期的停止标记处结束，以及每个助手轮次中源语言侧 / 目标语言侧是应该等待还是释放内容。它们不直接衡量 ASR 文字是否逐字正确，也不直接衡量翻译语义质量。

**POSTPROCESSED_TURN_STOP_RATE**

- 含义：后处理后的输出是否干净地停在闭合协议标签边界处。
- 计算：`postprocessed_turn_stop_turns / TURN_COUNT`。当解析出的协议单元后面只剩空白或允许的 EOS / 生成停止标记时，记为通过。只要闭合协议标签之外还有非 EOS 内容，就判为不通过，例如尾随文本、逗号分隔的标签、重复协议片段等。

**PROTOCOL_VALID_RATE**

- 含义：模型输出中的源语言 / 目标语言协议标签是否合法。
- 计算：`protocol_valid_turns / TURN_COUNT`。输出以合法的纯转写单元 `<src>...</src>` 或翻译单元 `<src>...</src><tgt>...</tgt>` 开始，并且标签成对、顺序合法、字段内部没有嵌套 `<src>`、`</src>`、`<tgt>`、`</tgt>` 标签时，记为有效。这个指标只检查标签合法性；闭合协议单元之后是否继续输出非标签内内容，由 `POSTPROCESSED_TURN_STOP_RATE` 衡量。

**RAW_TURN_STOP_RATE**

- 含义：原始解码结果是否在配置的生成停止标记处正常停止。
- 计算：`raw_turn_stop_turns / TURN_COUNT`。如果原始输出在后处理输出之后紧接着 `generation_stop`，该轮次记为正常停止。

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

#### 指标：Gemma-4-E2B-it，学习率=3e-4，rank=16，batch size=16，bnb4bit，adamw

**测试指标**：
- 综合最佳 - step 8100

![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/test_metrics_plot.png)

严格测试结果请参考 [strict test](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/test_outputs)。

**训练**：
![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/train_loss.png)
![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/learning_rage_schedule.png)
![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/eval_loss.png)

#### 第 300 步测试输出

- 容忍窗口大小：1.0 秒
- 以下是选取的测试样例，左侧是标准答案，右侧是模型输出。

```text
## Test Example 2 / 60

  - UID: EN_nLFyRxIRQBo_W000057
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

1. <src>These people are </src><tgt><|wait|></tgt>  -  <src>These people are </src><tgt><|wait|></tgt>
2. <src>completely rare, </src><tgt><|wait|></tgt>  -  <src>completely rare. </src><tgt><|wait|></tgt>
3. <src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>  -  <src>And they often </src><tgt>これは完全に珍しいんです。そして、</tgt>
4. <src>show up to </src><tgt><|wait|></tgt>  -  <src>show up </src><tgt><|wait|></tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>to completely revolution- </src><tgt><|wait|></tgt>
6. <src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>  -  <src>ize the world. </src><tgt>世界を完全に根底から覆す人たちがよく登場します。</tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>The personality </src><tgt><|wait|></tgt>
8. <src>Their personality is </src><tgt><|wait|></tgt>  -  <src>is something </src><tgt><|wait|></tgt>
9. <src>something of a </src><tgt>彼らの性格は</tgt>  -  <src>of a contradiction. </src><tgt>彼らの個性は、ある種の矛盾をはらんでいます。</tgt>
10. <src>contradiction. </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
11. <src>While they're </src><tgt><|wait|></tgt>  -  <src>While they're extroverted, </src><tgt><|wait|></tgt>
12. <src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>  -  <src>they also </src><tgt>外向的であるにもかかわらず、彼らは</tgt>
13. <src>they also hate </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
14. <src>meaningless conversations </src><tgt><|wait|></tgt>  -  <src>hate meaningless conversations. </src><tgt><|wait|></tgt>
15. <src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>  -  <src>And like </src><tgt>無意味な会話を嫌う、</tgt>
16. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>it gets straight to the </src><tgt><|wait|></tgt>
17. <src>get straight to the point. </src><tgt><|wait|></tgt>  -  <src>point. </src><tgt><|wait|></tgt>
18. <src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>  -  <src>They also love to </src><tgt>まっすぐ本題に入りたいのです。彼らはまた</tgt>
19. <src>play </src><tgt><|wait|></tgt>  -  <src>play the devil's advocate, </src><tgt><|wait|></tgt>
20. <src>the devil's advocate, and they </src><tgt><|wait|></tgt>  -  <src>and </src><tgt><|wait|></tgt>
21. <src><|wait|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>  -  <src>never shy away </src><tgt>逆説を好むし、</tgt>
22. <src>never shy away from a debate. </src><tgt><|wait|></tgt>  -  <src>from a debate. </src><tgt><|wait|></tgt>
23. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
24. <src><|wait|></src><tgt>議論を避けることはありません。</tgt>  -  <src>EHCPS </src><tgt>議論を避けることは決してありません。EHCPSの</tgt>
25. <src>ENTP stands for </src><tgt><|wait|></tgt>  -  <src>stand for. </src><tgt><|wait|></tgt>

---

## Test Example 9 / 60

  - UID: EN_nSOXneMb4Ec_W000365
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 3 wait windows before each target release.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>Meaningful individual </src><tgt><|wait|></tgt>  -  <src>Meaningful individual </src><tgt><|wait|></tgt>
3. <src>right, </src><tgt><|wait|></tgt>  -  <src>right, </src><tgt><|wait|></tgt>
4. <src>and the Supreme Court </src><tgt>有意义的个人权利，而最高法院</tgt>  -  <src>and the Supreme Court </src><tgt>有意义的个体权利，</tgt>
5. <src>came along </src><tgt><|wait|></tgt>  -  <src>came along last, </src><tgt><|wait|></tgt>
6. <src>last, not leading. </src><tgt><|wait|></tgt>  -  <src>not leading. </src><tgt><|wait|></tgt>
7. <src>And I don't think the courts want to be </src><tgt><|wait|></tgt>  -  <src>And I don't I don't think the courts want to be </src><tgt><|wait|></tgt>
8. <src><|wait|></src><tgt>是最后才介入的，不是引领者。我不认为</tgt>  -  <src>the </src><tgt>法院总是最后一个加入的。我个人认为，</tgt>
9. <src>the the vanguard of social </src><tgt><|wait|></tgt>  -  <src>vanard of social </src><tgt><|wait|></tgt>
10. <src>change </src><tgt><|wait|></tgt>  -  <src>change, </src><tgt><|wait|></tgt>
11. <src>these days, </src><tgt><|wait|></tgt>  -  <src>these days. </src><tgt><|wait|></tgt>
12. <src><|wait|></src><tgt>法院现在想成为社会变革的先锋，</tgt>  -  <src>But they rather </src><tgt>这些天似乎不想成为社会变革的典范。但他们更</tgt>
13. <src>but they rather reflect </src><tgt><|wait|></tgt>  -  <src>reflect the </src><tgt><|wait|></tgt>
14. <src>the consensus </src><tgt><|wait|></tgt>  -  <src>consensus. </src><tgt><|wait|></tgt>
15. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>That's already </src><tgt><|wait|></tgt>
16. <src>that's already emerged. </src><tgt>它们更倾向于反映已经形成的共识。</tgt>  -  <src>emerged. </src><tgt>选择反映已经形成的共识。</tgt>
17. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>So. </src><tgt><|wait|></tgt>
18. <src>So you have some </src><tgt><|wait|></tgt>  -  <src>You have </src><tgt><|wait|></tgt>
19. <src>federal judges </src><tgt><|wait|></tgt>  -  <src>some federal judges </src><tgt><|wait|></tgt>
20. <src><|wait|></src><tgt>所以，有些联邦法官……</tgt>  -  <src>who </src><tgt><|wait|></tgt>
21. <src>who. </src><tgt><|wait|></tgt>  -  <src>who </src><tgt><|wait|></tgt>

---

## Test Example 32 / 60

  - UID: ZH_B00041_S00155_W000028
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>家长需要</src><tgt>Parents need to</tgt>
2. <src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>  -  <src>做的是</src><tgt>do the following:</tgt>
3. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>用我们</src><tgt><|wait|></tgt>
4. <src>用我们深深的</src><tgt><|wait|></tgt>  -  <src>身上的爱</src><tgt>use the love in our own hearts</tgt>
5. <src>爱浇水、</src><tgt><|wait|></tgt>  -  <src>交世界，</src><tgt>to make love happen.</tgt>
6. <src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
7. <src>给足</src><tgt><|wait|></tgt>  -  <src>可以做</src><tgt><|wait|></tgt>
8. <src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>  -  <src>孩子心里的影响力。</src><tgt>That is the influence</tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>以内心，</src><tgt>that we want to instill in our children</tgt>
10. <src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>  -  <src>等他孩子</src><tgt><|wait|></tgt>
11. <src>慢慢长大。</src><tgt>them to grow slowly.</tgt>  -  <src>慢慢长大。</src><tgt>as they grow up: by teaching them how to share their hearts.</tgt>

---

## Test Example 40 / 60

  - UID: JA_Xv3zO_K9SuU_W000011
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>そうです。</src>  -  <src>そうですね、</src>
2. <src>そこで</src>  -  <src>そこで</src>
3. <src><|wait|></src>  -  <src>っていう</src>
4. <src>テキという設備寺が</src>  -  <src>設定</src>
5. <src>ありましたね。</src>  -  <src>済みか読みましたね</src>
6. <src>で、</src>  -  <src>って。</src>
7. <src><|wait|></src>  -  <src><|wait|></src>
8. <src>長井慶義氏の仕組み</src>  -  <src>細井親父の</src>
9. <src><|wait|></src>  -  <src>仕組みは</src>
10. <src>は五経、</src>  -  <src>元</src>
11. <src><|wait|></src>  -  <src>設定</src>
12. <src>設備寺、五比</src>  -  <src>済み？</src>
13. <src>です。</src>  -  <src>合図。</src>

---

## Test Example 48 / 60

  - UID: EN_n_COVPwr54I_W000006
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

1. <src>My name is </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>  -  <src>My name is Jinah Tree,</src><tgt>제 이름은 진아 트리예요. 저는</tgt>
3. <src>I am currently </src><tgt><|wait|></tgt>  -  <src>I am currently studying</src><tgt><|wait|></tgt>
4. <src><|wait|></src><tgt>저는 현재</tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
5. <src>studying a Bachelor of Finance </src><tgt><|wait|></tgt>  -  <src>AABX, back roll finance, and AABX</src><tgt>AABX, 배경 투자, 그리고 AABX를 지금 공부하고 있고요.</tgt>
6. <src>and a Bachelor of Psychology </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>of psychology, here at </src><tgt>심리학자들을 여기서</tgt>
8. <src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>  -  <src>Jianyu, </src><tgt><|wait|></tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt>Jianyu에서 배웠어요. 심리학자</tgt>
10. <src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>  -  <src>and in the future, </src><tgt><|wait|></tgt>
11. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>I want to go into corporate consulting </src><tgt>들도요. 미래에는 기업 자문가로</tgt>
12. <src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>  -  <src>or </src><tgt><|wait|></tgt>

---

## Test Example 54 / 60

  - UID: ZH_W0NbyT5Ak-A_W000071
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>弗洛伊德</src>  -  <src>Four in </src>
2. <src>首次觉知到</src>  -  <src>the subject had</src>
3. <src>那个现象：</src>  -  <src>solved that problem.</src>
4. <src>每当我们</src>  -  <src>But we, </src>
5. <src><|wait|></src>  -  <src>in our pursuit of </src>
6. <src>处于爱之中，</src>  -  <src>love, we</src>
7. <src>所谓的爱，</src>  -  <src>find</src>
8. <src>我们也</src>  -  <src>the other love</src>
9. <src>同时进入恨。</src>  -  <src>that has entered</src>
10. <src><|wait|></src>  -  <src>the heart</src>
11. <src>在早上的时候，</src>  -  <src>when we are seeking, that</src>
12. <src>它是爱；</src>  -  <src>is that love.</src>
13. <src>到了晚上，</src>  -  <src>The end result</src>
14. <src>它就变成恨。</src>  -  <src>is that, it turns into</src>
15. <src><|wait|></src>  -  <src>that</src>
16. <src>那个钟摆</src>  -  <src>love.</src>
17. <src><|wait|></src>  -  <src>It continues to grow</src>
18. <src>继续在移动。</src>  -  <src>and and.</src>
```


#### 第 5400 步最终测试输出

```text
Test Metrics
  - STEP: 5400
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - POSTPROCESSED_TURN_STOP_RATE: 1.0000
  - PROTOCOL_VALID_RATE: 1.0000
  - RAW_TURN_STOP_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9610
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.7219
  - SRC_WAIT_TOTAL: 151
  - TGT_RELEASE_ACCURACY: 0.8725
  - TGT_RELEASE_TOTAL: 298
  - TGT_WAIT_ACCURACY: 0.8896
  - TGT_WAIT_TOTAL: 489
  - TURN_COUNT: 869

---

## Test Example 2 / 60

  - UID: EN_nLFyRxIRQBo_W000057
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

1. <src>These people are </src><tgt><|wait|></tgt>  -  <src>These people are </src><tgt><|wait|></tgt>
2. <src>completely rare, </src><tgt><|wait|></tgt>  -  <src>completely rare, </src><tgt><|wait|></tgt>
3. <src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>  -  <src>and they often </src><tgt>これらの人々は非常に稀です。そして、</tgt>
4. <src>show up to </src><tgt><|wait|></tgt>  -  <src>show up to </src><tgt><|wait|></tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
6. <src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>  -  <src>completely revolutionize the world. </src><tgt>世界の完全な革命を起こすためにしばしば現れます。</tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
8. <src>Their personality is </src><tgt><|wait|></tgt>  -  <src>Their personality is </src><tgt><|wait|></tgt>
9. <src>something of a </src><tgt>彼らの性格は</tgt>  -  <src>something of a contradiction. </src><tgt>彼らの性格は矛盾していることも特徴です。</tgt>
10. <src>contradiction. </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
11. <src>While they're </src><tgt><|wait|></tgt>  -  <src>While they're </src><tgt><|wait|></tgt>
12. <src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>  -  <src>extroverted, </src><tgt>外向的であるだけでなく、</tgt>
13. <src>they also hate </src><tgt><|wait|></tgt>  -  <src>they also hate </src><tgt><|wait|></tgt>
14. <src>meaningless conversations </src><tgt><|wait|></tgt>  -  <src>meaningless conversations </src><tgt><|wait|></tgt>
15. <src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>  -  <src><|wait|></src><tgt>無意味な会話を嫌い、</tgt>
16. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>and like to get straight to </src><tgt><|wait|></tgt>
17. <src>get straight to the point. </src><tgt><|wait|></tgt>  -  <src>the point. </src><tgt><|wait|></tgt>
18. <src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>  -  <src>They also love to </src><tgt>すぐ本題に入りたいと考えます。また、</tgt>
19. <src>play </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
20. <src>the devil's advocate, and they </src><tgt><|wait|></tgt>  -  <src>play the devil's advocate, </src><tgt><|wait|></tgt>
21. <src><|wait|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>  -  <src><|wait|></src><tgt>悪魔の代弁をするのも好きです。</tgt>
22. <src>never shy away from a debate. </src><tgt><|wait|></tgt>  -  <src>and they're never shy over a debate. </src><tgt><|wait|></tgt>
23. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
24. <src><|wait|></src><tgt>議論を避けることはありません。</tgt>  -  <src>ENTP stands for </src><tgt>そして議論が始まっても決して臆しません。ENTPとは、</tgt>
25. <src>ENTP stands for </src><tgt><|wait|></tgt>  -  <src>Extraverted, Intuitive, \, </src><tgt><|wait|></tgt>

---

## Test Example 9 / 60

  - UID: EN_nSOXneMb4Ec_W000365
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 3 wait windows before each target release.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>Meaningful individual </src><tgt><|wait|></tgt>  -  <src>Meaningful, </src><tgt><|wait|></tgt>
3. <src>right, </src><tgt><|wait|></tgt>  -  <src>individual write, </src><tgt><|wait|></tgt>
4. <src>and the Supreme Court </src><tgt>有意义的个人权利，而最高法院</tgt>  -  <src>and the Supreme Court </src><tgt>有意义的个人著作，最高法院</tgt>
5. <src>came along </src><tgt><|wait|></tgt>  -  <src>came along </src><tgt><|wait|></tgt>
6. <src>last, not leading. </src><tgt><|wait|></tgt>  -  <src>last, not leading. </src><tgt><|wait|></tgt>
7. <src>And I don't think the courts want to be </src><tgt><|wait|></tgt>  -  <src>And I don't think the courts want to be </src><tgt><|wait|></tgt>
8. <src><|wait|></src><tgt>是最后才介入的，不是引领者。我不认为</tgt>  -  <src><|wait|></src><tgt>最后才跟进。我认为法院不想</tgt>
9. <src>the the vanguard of social </src><tgt><|wait|></tgt>  -  <src>the the vanguard of social </src><tgt><|wait|></tgt>
10. <src>change </src><tgt><|wait|></tgt>  -  <src>change </src><tgt><|wait|></tgt>
11. <src>these days, </src><tgt><|wait|></tgt>  -  <src>these days. </src><tgt><|wait|></tgt>
12. <src><|wait|></src><tgt>法院现在想成为社会变革的先锋，</tgt>  -  <src>But they rather </src><tgt>成为社会变革的前沿阵线。</tgt>
13. <src>but they rather reflect </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
14. <src>the consensus </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
15. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>reflect the consensus </src><tgt><|wait|></tgt>
16. <src>that's already emerged. </src><tgt>它们更倾向于反映已经形成的共识。</tgt>  -  <src>that's already emerged. </src><tgt>但它们更多是反映已经形成的共识。</tgt>
17. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>So, </src><tgt><|wait|></tgt>
18. <src>So you have some </src><tgt><|wait|></tgt>  -  <src>you have </src><tgt><|wait|></tgt>
19. <src>federal judges </src><tgt><|wait|></tgt>  -  <src>some federal judges </src><tgt><|wait|></tgt>
20. <src><|wait|></src><tgt>所以，有些联邦法官……</tgt>  -  <src>who </src><tgt>所以，你们有了一些联邦法官，</tgt>
21. <src>who. </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>

---

## Test Example 32 / 60

  - UID: ZH_B00041_S00155_W000028
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>家长需要</src><tgt>Parents need to</tgt>
2. <src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>  -  <src>做的是</src><tgt><|wait|></tgt>
3. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
4. <src>用我们深深的</src><tgt><|wait|></tgt>  -  <src>用我们深深的</src><tgt><|wait|></tgt>
5. <src>爱浇水、</src><tgt><|wait|></tgt>  -  <src>爱浇水、</src><tgt>show their love for the child, like watering a plant,</tgt>
6. <src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>  -  <src>施肥，</src><tgt>fertilizing it,</tgt>
7. <src>给足</src><tgt><|wait|></tgt>  -  <src>给足</src><tgt><|wait|></tgt>
8. <src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>  -  <src>孩子心理营养，</src><tgt>and giving them enough emotional nourishment.</tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>并耐心</src><tgt><|wait|></tgt>
10. <src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>  -  <src>等他</src><tgt><|wait|></tgt>
11. <src>慢慢长大。</src><tgt>them to grow slowly.</tgt>  -  <src>慢慢长大。</src><tgt>And patiently waiting as they grow up.</tgt>

---

## Test Example 40 / 60

  - UID: JA_Xv3zO_K9SuU_W000011
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>そうです。</src>  -  <src>そうです。</src>
2. <src>そこで</src>  -  <src>そこで</src>
3. <src><|wait|></src>  -  <src><|wait|></src>
4. <src>テキという設備寺が</src>  -  <src>テキという設備寺が</src>
5. <src>ありましたね。</src>  -  <src>ありましたね。</src>
6. <src>で、</src>  -  <src>で、</src>
7. <src><|wait|></src>  -  <src><|wait|></src>
8. <src>長井慶義氏の仕組み</src>  -  <src>長井慶義氏の仕組み</src>
9. <src><|wait|></src>  -  <src><|wait|></src>
10. <src>は五経、</src>  -  <src>は五個</src>
11. <src><|wait|></src>  -  <src><|wait|></src>
12. <src>設備寺、五比</src>  -  <src>設備寺五個</src>
13. <src>です。</src>  -  <src>です。</src>

---

## Test Example 48 / 60

  - UID: EN_n_COVPwr54I_W000006
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

1. <src>My name is </src><tgt><|wait|></tgt>  -  <src>My name is </src><tgt><|wait|></tgt>
2. <src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>  -  <src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그( Kerenath Dettig) 입니다.</tgt>
3. <src>I am currently </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
4. <src><|wait|></src><tgt>저는 현재</tgt>  -  <src>I am currently studying </src><tgt>현재</tgt>
5. <src>studying a Bachelor of Finance </src><tgt><|wait|></tgt>  -  <src>a Bachelor of Finance </src><tgt><|wait|></tgt>
6. <src>and a Bachelor of Psychology </src><tgt><|wait|></tgt>  -  <src>and a Bachelor of Psychology </src><tgt>경영학 학사 학위와</tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
8. <src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>  -  <src>here at the ANU, </src><tgt>심리학 학사 학위를 안데번 대학교( ANU ) 에서</tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
10. <src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>  -  <src>and in the future, I want to go into </src><tgt>수강 중이고요, 나중에는</tgt>
11. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
12. <src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>  -  <src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>

---

## Test Example 54 / 60

  - UID: ZH_W0NbyT5Ak-A_W000071
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>弗洛伊德</src>  -  <src>弗洛伊德</src>
2. <src>首次觉知到</src>  -  <src>首次觉知到</src>
3. <src>那个现象：</src>  -  <src>那个现象。</src>
4. <src>每当我们</src>  -  <src>美登们</src>
5. <src><|wait|></src>  -  <src><|wait|></src>
6. <src>处于爱之中，</src>  -  <src>处于爱之中，</src>
7. <src>所谓的爱，</src>  -  <src>所谓的爱，</src>
8. <src>我们也</src>  -  <src><|wait|></src>
9. <src>同时进入恨。</src>  -  <src>我们也同时进入黑暗，</src>
10. <src><|wait|></src>  -  <src><|wait|></src>
11. <src>在早上的时候，</src>  -  <src>在早上的时候，</src>
12. <src>它是爱；</src>  -  <src>他是爱。</src>
13. <src>到了晚上，</src>  -  <src>到了晚上，</src>
14. <src>它就变成恨。</src>  -  <src>他就变成</src>
15. <src><|wait|></src>  -  <src>黑暗，</src>
16. <src>那个钟摆</src>  -  <src>那个钟表。</src>
17. <src><|wait|></src>  -  <src><|wait|></src>
18. <src>继续在移动。</src>  -  <src>继续在移动。</src>
```