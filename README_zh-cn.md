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
- 我们**不**从零训练 语义单元检测器、音频编码器，也不做 LLM 主干对齐；
- 我们**不**修改模型架构；无限时长的流式翻译通过运行时的滑动窗口上下文管理来实现；
- 我们**会**构建接近标准答案的数据集和流程验证机制，让全模态模型学习同步翻译策略；

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
- 默认基础模型使用 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE)。
- 多模态训练中的 仅助手侧损失 由 [MultimodalAssistantMask](https://github.com/LUOXIAO92/MultimodalAssistantMask.git) 构造。

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

待办：
- [x] **高优先级**：用极小样本跑通 `examples/train_lora.py`，确认对话渲染、仅助手侧损失和 1-2 个训练步骤正常。
- [ ] **高优先级**：完成 `google/gemma-4-E2B-it` 的完整 LoRA 训练。
  - **进行中**：目前主要在准备更大规模的训练数据。计划发布的数据集约包含 8,000 条音频及转写样本，以及 24,000 条用于训练翻译策略的多轮对话轨迹。数据基于 [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) 二次处理而来；感谢 Emilia-Dataset 项目提供高质量的多语言音频资源。
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

## 小规模验证结果 (`google/gemma-4-E2B-it`, `train_examples: 96`):

### 训练参数

```text
Dataset
  - TRAIN_EXAMPLES: 96
  - VALIDATE_EXAMPLES: 18
  - TEST_EXAMPLES: 6

Audio
  - AUDIO_SAMPLING_RATE: 16000
  - AUDIO_CHUNK_SECONDS: 1.0

Training Steps
  - PER_DEVICE_TRAIN_BATCH_SIZE: 1
  - GRADIENT_ACCUMULATION_STEPS: 8
  - EFFECTIVE_BATCH_SIZE: 8
    `PER_DEVICE_TRAIN_BATCH_SIZE: 1 * GRADIENT_ACCUMULATION_STEPS: 8`
  - OPTIMIZER_STEPS_PER_EPOCH: 12
    `ceil(TRAIN_EXAMPLES: 96 / EFFECTIVE_BATCH_SIZE: 8)`
  - CONFIGURED_NUM_TRAIN_EPOCHS: 20
  - CONFIGURED_MAX_STEPS: -1
  - TOTAL_OPTIMIZER_STEPS: 240
    `OPTIMIZER_STEPS_PER_EPOCH: 12 * CONFIGURED_NUM_TRAIN_EPOCHS: 20`
  
Hyper Parmeters
  - LEARNING_RATE: 1e-4
  - WEIGHT_DECAY: 0.0
  - ADAM_BETA1: 0.9
  - ADAM_BETA2: 0.999
  - MAX_GRAD_NORM: 1.0
  - NUM_TRAIN_EPOCHS: 20
```

### 结果

#### 指标说明

下面这些严格流式测试指标主要用来检查模型在流式对话中的格式控制和释放策略：输出是否符合 `<src>...</src><tgt>...</tgt>` 协议，生成是否在预期的停止标记处结束，以及每个助手轮次中源语言侧 / 目标语言侧是应该等待还是释放内容。它们不直接衡量 ASR 文字是否逐字正确，也不直接衡量翻译语义质量。

**POSTPROCESSED_TURN_STOP_RATE**

- 含义：后处理后的输出是否是干净、完整的协议输出。
- 计算：`postprocessed_turn_stop_turns / TURN_COUNT`。当一个轮次的后处理文本协议合法，并且正好等于规范化后的 `<src>...</src><tgt>...</tgt>` 输出时，记为通过。

**PROTOCOL_VALID_RATE**

- 含义：模型输出符合规定协议的比例。
- 计算：`protocol_valid_turns / TURN_COUNT`。输出必须匹配 `<src>...</src><tgt>...</tgt>`，并且源语言侧 / 目标语言侧内容内部不能再嵌套 `<src>`、`</src>`、`<tgt>`、`</tgt>` 标签。

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

#### 第 50 步测试输出

- 容忍窗口大小：1.0 秒
- 以下是小规模测试结果，左侧是标准答案，右侧是模型输出。

```text
Test Metrics
  - STEP: 50
  - TOTAL_AVAILABLE_TEST_ROWS: 6
  - SELECTED_TEST_ROWS: 6
  - POSTPROCESSED_TURN_STOP_RATE: 1.0000
  - PROTOCOL_VALID_RATE: 1.0000
  - RAW_TURN_STOP_RATE: 1.0000
  - RECORD_COUNT: 6
  - SRC_RELEASE_ACCURACY: 0.9067
  - SRC_RELEASE_TOTAL: 75
  - SRC_WAIT_ACCURACY: 0.2857
  - SRC_WAIT_TOTAL: 14
  - TGT_RELEASE_ACCURACY: 0.3000
  - TGT_RELEASE_TOTAL: 20
  - TGT_WAIT_ACCURACY: 0.7536
  - TGT_WAIT_TOTAL: 69
  - TURN_COUNT: 89

---

## Test Example 1 / 6

  - UID: JA__gKKQYSi4mg_W000167
  - SYSTEM_PROMPT: Translate to English, tolerance window size is 2

1. <src>あの</src><tgt><|wait|></tgt>  -  <src>あのー</src><tgt><|wait|></tgt>
2. <src>測量した</src><tgt><|wait|></tgt>  -  <src>所乗しました</src><tgt><|wait|></tgt>
3. <src><|wait|></src><tgt>This is the survey</tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
4. <src>データになります。</src><tgt><|wait|></tgt>  -  <src>データに</src><tgt><|wait|></tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>こういったデータ</src><tgt><|wait|></tgt>
6. <src>こういったデータであったり、</src><tgt>data. You can see data like this—</tgt>  -  <src>こういったデータがあったり</src><tgt><|wait|></tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>これは</src><tgt><|wait|></tgt>
8. <src>これは</src><tgt><|wait|></tgt>  -  <src>これは中野県の</src><tgt><|wait|></tgt>
9. <src>奈良県の</src><tgt>this one, for example,</tgt>  -  <src>奈良県。</src><tgt><|wait|></tgt>
10. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
11. <src>工事なんですけど。</src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>

---

## Test Example 2 / 6

  - UID: EN_nIpxsCym-BM_W000211
  - SYSTEM_PROMPT: Translate to Korean, tolerance window size is 3

1. <src>By default, </src><tgt><|wait|></tgt>  -  <src>Um, </src><tgt><|wait|></tgt>
2. <src>if you create </src><tgt><|wait|></tgt>  -  <src>if you create a fail, </src><tgt><|wait|></tgt>
3. <src>a file </src><tgt><|wait|></tgt>  -  <src>a file, </src><tgt>기본적으로 파일 생성 시, </tgt>
4. <src>called source/index, </src><tgt>기본적으로 source/index라는 파일을 만들면,</tgt>  -  <src>called course </src><tgt><|wait|></tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>so the index </src><tgt><|wait|></tgt>
6. <src>it's then going to push </src><tgt><|wait|></tgt>  -  <src>it's then going to push </src><tgt>그것을 푸시 하면,</tgt>
7. <src>whatever you put in </src><tgt><|wait|></tgt>  -  <src>whatever you put </src><tgt><|wait|></tgt>
8. <src>that file, </src><tgt>그 안에 담긴 내용이나</tgt>  -  <src>that file, </src><tgt><|wait|></tgt>
9. <src>any imports you use, </src><tgt><|wait|></tgt>  -  <src>any imports you use. </src><tgt><|wait|></tgt>
10. <src>things like that, </src><tgt><|wait|></tgt>  -  <src>think </src><tgt><|wait|></tgt>
11. <src>out to. </src><tgt><|wait|></tgt>  -  <src>to use. </src><tgt><|wait|></tgt>

---

## Test Example 3 / 6

  - UID: ZH_UJBZXO0vtl8_W000127
  - SYSTEM_PROMPT: Translate to Korean, tolerance window size is 5

1. <src>同样也是</src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>针对要留意</src><tgt><|wait|></tgt>  -  <src>正在流溢引起经济</src><tgt><|wait|></tgt>
3. <src>金钱的部分，</src><tgt><|wait|></tgt>  -  <src>资金的阶段部分。 </src><tgt><|wait|></tgt>
4. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>我们从这里，</src><tgt>똑같이 돈 문제가 있는데 그 부분을 주의해야 한다. 그 얘기는 여기서부터 하는 거지.</tgt>
5. <src>我们从这里呢可以</src><tgt><|wait|></tgt>  -  <src>我们从这里，</src><tgt><|wait|></tgt>
6. <src>看到的是</src><tgt>마찬가지로 금전적인 부분에서 주의할 점인데,</tgt>  -  <src>看到的是</src><tgt><|wait|></tgt>
7. <src>这一副卡片，</src><tgt><|wait|></tgt>  -  <src>这一卡片</src><tgt>이 카드를 보니까</tgt>
8. <src>它代表的是</src><tgt><|wait|></tgt>  -  <src>它代表的是</src><tgt>이 카드가 상징하는 것을 볼 수 있죠.</tgt>
9. <src>手。</src><tgt><|wait|></tgt>  -  <src>这双收。</src><tgt><|wait|></tgt>
10. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt>이 카드가 의미하는 것은 손을 쥐고 있는 것입니다.</tgt>
11. <src>那么手的时候呢，</src><tgt><|wait|></tgt>  -  <src>手呢，</src><tgt><|wait|></tgt>
12. <src>通常它</src><tgt>이 카드는 손을 의미합니다. 손은</tgt>  -  <src>通常，啊，</src><tgt><|wait|></tgt>
13. <src>非常的</src><tgt><|wait|></tgt>  -  <src>常常害怕写的。</src><tgt><|wait|></tgt>
14. <src>直白，代表是</src><tgt><|wait|></tgt>  -  <src>比较指白，</src><tgt>만약 손을 가질 때는</tgt>
15. <src>我们的金钱</src><tgt><|wait|></tgt>  -  <src>我们的金钱</src><tgt><|wait|></tgt>
16. <src>呢，可能就</src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
17. <src>尽量呢</src><tgt><|wait|></tgt>  -  <src>拿到，可能就</src><tgt><|wait|></tgt>
18. <src>不要，</src><tgt>아주 직설적인 카드라 돈과 관련해</tgt>  -  <src>不去。</src><tgt><|wait|></tgt>
19. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>就不是</src><tgt>관련해 최대한 지키려고 노력하는 게 좋을 것 같습니다. 이것은</tgt>
20. <src>就是做太多的</src><tgt><|wait|></tgt>  -  <src>就是说太多的。</src><tgt><|wait|></tgt>
21. <src>规划，</src><tgt><|wait|></tgt>  -  <src>规划。</src><tgt><|wait|></tgt>
22. <src>尤其是</src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
23. <src>针对家中</src><tgt><|wait|></tgt>  -  <src>正宗的，</src><tgt><|wait|></tgt>
24. <src>的男性</src><tgt>너무 많은 계획을 세우지 않는 게 좋다는 뜻인데요,</tgt>  -  <src>的女性</src><tgt>과도한 계획은 특히 가정의 여성들이</tgt>
25. <src>长男。</src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>

---

## Test Example 4 / 6

  - UID: ZH_B00021_S00398_W000012
  - SYSTEM_PROMPT: Translate to English, tolerance window size is 4

1. <src>三月二十二号，</src><tgt><|wait|></tgt>  -  <src>3-22</src><tgt><|wait|></tgt>
2. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>法国政权</src><tgt>March 22nd, France’s current regime</tgt>
3. <src>美国证券交易委员会宣布对</src><tgt><|wait|></tgt>  -  <src>国众权交议委员会宣布对内，</src><tgt>On March 22nd, the National Legislative Council announced that it will... <|wait|></tgt>
4. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>海 密资产欺诈</src><tgt><|wait|></tgt>
5. <src>加密资产企业家孙宇晨</src><tgt>On March 22nd, the U.S. Securities and Exchange Commission</tgt>  -  <src>亚马逊资产齐</src><tgt><|wait|></tgt>
6. <src>及其三家</src><tgt><|wait|></tgt>  -  <src>积资参加</src><tgt><|wait|></tgt>
7. <src>全资公司</src><tgt><|wait|></tgt>  -  <src>子公司，提及了</src><tgt><|wait|></tgt>
8. <src>提起诉讼，</src><tgt><|wait|></tgt>  -  <src>旗</i>计出售，</src><tgt><|wait|></tgt>
9. <src>指控他们没有经过注册</src><tgt><|wait|></tgt>  -  <src>指控他们没有任何经过</src><tgt>filed a lawsuit, accusing</tgt>
10. <src>提供和出售</src><tgt>announced a lawsuit against crypto entrepreneur Justin Sun and three of his companies, alleging that they offered and sold</tgt>  -  <src><|wait|></src><tgt>filed a lawsuit against crypto asset entrepreneur</tgt>
11. <src>加密资产</src><tgt><|wait|></tgt>  -  <src>加密资产证券。</src><tgt><|wait|></tgt>
12. <src>证券Tronics</src><tgt><|wait|></tgt>  -  <src>证券，</src><tgt>unregistered securities.</tgt>
13. <src>和BitTorrent。</src><tgt><|wait|></tgt>  -  <src>和Tarant</src><tgt><|wait|></tgt>

---

## Test Example 5 / 6

  - UID: ZH_NWf8Wc2GVvM_W000007
  - SYSTEM_PROMPT: Translate to Japanese, tolerance window size is 1

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>石</src><tgt><|wait|></tgt>
2. <src>启示录和</src><tgt>『ヨハネの黙示録』と</tgt>  -  <src>खीस ही रूस,</src><tgt><|wait|></tgt>
3. <src>翡翠石板</src><tgt><|wait|></tgt>  -  <src>首页</src><tgt>その巻第一章では</tgt>
4. <src>都曾经预测到，</src><tgt>『エメラルド・タブレット』のどちらもが予言していたことがあります。</tgt>  -  <src>都成为</src><tgt>翡翠石板。</tgt>
5. <src>这十四万四千名</src><tgt><|wait|></tgt>  -  <src>那这四千万</src><tgt><|wait|></tgt>
6. <src>光之工作者</src><tgt>それは、14万4000人のライトワーカーが</tgt>  -  <src>十字工作者的道路。</src><tgt><|wait|></tgt>
7. <src>的到来，会</src><tgt><|wait|></tgt>  -  <src>的到来，将会</src><tgt><|wait|></tgt>
8. <src>在卡利年代</src><tgt>到来し、カリ・ユガの</tgt>  -  <src>在下一个</src><tgt>来ることを</tgt>
9. <src>结束时，</src><tgt><|wait|></tgt>  -  <src>结束时，将</src><tgt>終わりを迎えるときに、</tgt>
10. <src>将地球</src><tgt>終わりに地球を</tgt>  -  <src>将</src><tgt>終結までに</tgt>
11. <src>从黑暗势力的手中</src><tgt><|wait|></tgt>  -  <src>从黑石里的手</src><tgt>破壊するでしょう。</tgt>
12. <src>拯救出来。</src><tgt>闇の勢力から救い出すということです。</tgt>  -  <src>拯救出来。</src><tgt>ダークパワーの手から救い出す</tgt>

---

## Test Example 6 / 6

  - UID: ZH_Y4xRc2amPxY_W000024
  - SYSTEM_PROMPT: Translate to Korean, tolerance window size is 4

1. <src>就会</src><tgt><|wait|></tgt>  -  <src>就会</src><tgt><|wait|></tgt>
2. <src>消耗我们</src><tgt><|wait|></tgt>  -  <src>像 </src><tgt><|wait|></tgt>
3. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>的身体</src><tgt><|wait|></tgt>
4. <src>身体骨骼当中的</src><tgt><|wait|></tgt>  -  <src>去库存</src><tgt><|wait|></tgt>
5. <src>矿物质，更多的</src><tgt>우리 몸은 뼈 속의 미네랄을 소모하게 되고, 더 많은</tgt>  -  <src>钙质消耗</src><tgt><|wait|></tgt>
6. <src>靠物矿物质。</src><tgt><|wait|></tgt>  -  <src>矿物这种</src><tgt><|wait|></tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
8. <src>所以呢，</src><tgt><|wait|></tgt>  -  <src>所以呢，</src><tgt>무기물 미네랄이 소모되기 때문에</tgt>
9. <src>这个肥胖人</src><tgt><|wait|></tgt>  -  <src>吃蛋白质，</src><tgt>그리고 단백질을 섭취하면</tgt>
10. <src>往往都会有</src><tgt>미네랄을 필요로 하게 됩니다. 그래서 비만인 분들은</tgt>  -  <src>甩胖人</src><tgt><|wait|></tgt>
11. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>这个</src><tgt><|wait|></tgt>
12. <src>这种关节</src><tgt><|wait|></tgt>  -  <src>这个</src><tgt><|wait|></tgt>
13. <src>和软组织</src><tgt><|wait|></tgt>  -  <src>关节</src><tgt><|wait|></tgt>
14. <src>的问题，就是</src><tgt><|wait|></tgt>  -  <src>的限制，就是因为</src><tgt><|wait|></tgt>
15. <src>因为什么？</src><tgt>관절이나 연조직 문제를 자주 겪는데요. 왜 그럴까요?</tgt>  -  <src>因为</src><tgt><|wait|></tgt>
16. <src>就是消耗了</src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
17. <src>太多的矿物质。</src><tgt><|wait|></tgt>  -  <src>太多</src><tgt><|wait|></tgt>
```


#### 第 240 步最终测试输出

```text
Test Metrics
  - STEP: 240
  - TOTAL_AVAILABLE_TEST_ROWS: 6
  - SELECTED_TEST_ROWS: 6
  - POSTPROCESSED_TURN_STOP_RATE: 1.0000
  - PROTOCOL_VALID_RATE: 1.0000
  - RAW_TURN_STOP_RATE: 1.0000
  - RECORD_COUNT: 6
  - SRC_RELEASE_ACCURACY: 0.9867
  - SRC_RELEASE_TOTAL: 75
  - SRC_WAIT_ACCURACY: 1.0000
  - SRC_WAIT_TOTAL: 14
  - TGT_RELEASE_ACCURACY: 0.8000
  - TGT_RELEASE_TOTAL: 20
  - TGT_WAIT_ACCURACY: 0.9130
  - TGT_WAIT_TOTAL: 69
  - TURN_COUNT: 89

---

## Test Example 1 / 6

  - UID: JA__gKKQYSi4mg_W000167
  - SYSTEM_PROMPT: Translate to English, tolerance window size is 2

1. <src>あの</src><tgt><|wait|></tgt>  -  <src>あの</src><tgt><|wait|></tgt>
2. <src>測量した</src><tgt><|wait|></tgt>  -  <src>測量した</src><tgt><|wait|></tgt>
3. <src><|wait|></src><tgt>This is the survey</tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
4. <src>データになります。</src><tgt><|wait|></tgt>  -  <src>データになります。</src><tgt><|wait|></tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
6. <src>こういったデータであったり、</src><tgt>data. You can see data like this—</tgt>  -  <src>こういったデータであったり、</src><tgt>data we've collected— things like this, or</tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
8. <src>これは</src><tgt><|wait|></tgt>  -  <src>これは</src><tgt><|wait|></tgt>
9. <src>奈良県の</src><tgt>this one, for example,</tgt>  -  <src>奈良県の</src><tgt>this is</tgt>
10. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
11. <src>工事なんですけど。</src><tgt><|wait|></tgt>  -  <src>工事なんですけど。</src><tgt><|wait|></tgt>

---

## Test Example 2 / 6

  - UID: EN_nIpxsCym-BM_W000211
  - SYSTEM_PROMPT: Translate to Korean, tolerance window size is 3

1. <src>By default, </src><tgt><|wait|></tgt>  -  <src>By default, </src><tgt><|wait|></tgt>
2. <src>if you create </src><tgt><|wait|></tgt>  -  <src>if you create </src><tgt><|wait|></tgt>
3. <src>a file </src><tgt><|wait|></tgt>  -  <src>a file </src><tgt><|wait|></tgt>
4. <src>called source/index, </src><tgt>기본적으로 source/index라는 파일을 만들면,</tgt>  -  <src>called source/index, </src><tgt>기본적으로 source/index 파일을 만드시면 </tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
6. <src>it's then going to push </src><tgt><|wait|></tgt>  -  <src>it's then going to push </src><tgt><|wait|></tgt>
7. <src>whatever you put in </src><tgt><|wait|></tgt>  -  <src>whatever you put in </src><tgt><|wait|></tgt>
8. <src>that file, </src><tgt>그 안에 담긴 내용이나</tgt>  -  <src>that file, </src><tgt>해당 파일에</tgt>
9. <src>any imports you use, </src><tgt><|wait|></tgt>  -  <src>any imports you use, </src><tgt><|wait|></tgt>
10. <src>things like that, </src><tgt><|wait|></tgt>  -  <src>things like that, </src><tgt><|wait|></tgt>
11. <src>out to. </src><tgt><|wait|></tgt>  -  <src>out to. </src><tgt><|wait|></tgt>

---

## Test Example 3 / 6

  - UID: ZH_UJBZXO0vtl8_W000127
  - SYSTEM_PROMPT: Translate to Korean, tolerance window size is 5

1. <src>同样也是</src><tgt><|wait|></tgt>  -  <src>同样也是</src><tgt><|wait|></tgt>
2. <src>针对要留意</src><tgt><|wait|></tgt>  -  <src>针对要留意</src><tgt><|wait|></tgt>
3. <src>金钱的部分，</src><tgt><|wait|></tgt>  -  <src>金钱的部分，</src><tgt><|wait|></tgt>
4. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt>양안 모두 돈과 관련해서 유의하셔야 할 점은, </tgt>
5. <src>我们从这里呢可以</src><tgt><|wait|></tgt>  -  <src>我们从这里呢可以</src><tgt><|wait|></tgt>
6. <src>看到的是</src><tgt>마찬가지로 금전적인 부분에서 주의할 점인데,</tgt>  -  <src>看到的是</src><tgt>양쪽 모두에게 공통점이 있는데요,</tgt>
7. <src>这一副卡片，</src><tgt><|wait|></tgt>  -  <src>这一副卡片，</src><tgt><|wait|></tgt>
8. <src>它代表的是</src><tgt><|wait|></tgt>  -  <src>它代表的是</src><tgt><|wait|></tgt>
9. <src>手。</src><tgt><|wait|></tgt>  -  <src>手。</src><tgt><|wait|></tgt>
10. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
11. <src>那么手的时候呢，</src><tgt><|wait|></tgt>  -  <src>那么手的时候呢，</src><tgt><|wait|></tgt>
12. <src>通常它</src><tgt>이 카드는 손을 의미합니다. 손은</tgt>  -  <src>通常它</src><tgt><|wait|></tgt>
13. <src>非常的</src><tgt><|wait|></tgt>  -  <src>非常的</src><tgt><|wait|></tgt>
14. <src>直白，代表是</src><tgt><|wait|></tgt>  -  <src>直白，代表是</src><tgt><|wait|></tgt>
15. <src>我们的金钱</src><tgt><|wait|></tgt>  -  <src>我们的金钱</src><tgt><|wait|></tgt>
16. <src>呢，可能就</src><tgt><|wait|></tgt>  -  <src>呢，可能就</src><tgt><|wait|></tgt>
17. <src>尽量呢</src><tgt><|wait|></tgt>  -  <src>尽量呢</src><tgt><|wait|></tgt>
18. <src>不要，</src><tgt>아주 직설적인 카드라 돈과 관련해</tgt>  -  <src>不要，</src><tgt><|wait|></tgt>
19. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
20. <src>就是做太多的</src><tgt><|wait|></tgt>  -  <src>就是做太多的</src><tgt><|wait|></tgt>
21. <src>规划，</src><tgt><|wait|></tgt>  -  <src>规划，</src><tgt><|wait|></tgt>
22. <src>尤其是</src><tgt><|wait|></tgt>  -  <src>尤其是</src><tgt><|wait|></tgt>
23. <src>针对家中</src><tgt><|wait|></tgt>  -  <src>针对家中</src><tgt><|wait|></tgt>
24. <src>的男性</src><tgt>너무 많은 계획을 세우지 않는 게 좋다는 뜻인데요,</tgt>  -  <src>的男性</src><tgt>지나,</tgt>
25. <src>长男。</src><tgt><|wait|></tgt>  -  <src>长</i>性紧张。</src><tgt><|wait|></tgt>

---

## Test Example 4 / 6

  - UID: ZH_B00021_S00398_W000012
  - SYSTEM_PROMPT: Translate to English, tolerance window size is 4

1. <src>三月二十二号，</src><tgt><|wait|></tgt>  -  <src>三月二十二号，</src><tgt><|wait|></tgt>
2. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
3. <src>美国证券交易委员会宣布对</src><tgt><|wait|></tgt>  -  <src>美国证券交易委员会宣布对</src><tgt><|wait|></tgt>
4. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
5. <src>加密资产企业家孙宇晨</src><tgt>On March 22nd, the U.S. Securities and Exchange Commission</tgt>  -  <src>加密资产企业家孙羽晨</src><tgt>On March 22nd, the U.S. Securities and Exchange Commission announced that crypto entrepreneur</tgt>
6. <src>及其三家</src><tgt><|wait|></tgt>  -  <src>及其三家</src><tgt><|wait|></tgt>
7. <src>全资公司</src><tgt><|wait|></tgt>  -  <src>知名</i>知名</i>数字公司，</src><tgt><|wait|></tgt>
8. <src>提起诉讼，</src><tgt><|wait|></tgt>  -  <src>提起诉讼，</src><tgt><|wait|></tgt>
9. <src>指控他们没有经过注册</src><tgt><|wait|></tgt>  -  <src>指控他们没有经过注册</src><tgt>filed a lawsuit against crypto entrepreneur</tgt>
10. <src>提供和出售</src><tgt>announced a lawsuit against crypto entrepreneur Justin Sun and three of his companies, alleging that they offered and sold</tgt>  -  <src>提供和出售加密</src><tgt><|wait|></tgt>
11. <src>加密资产</src><tgt><|wait|></tgt>  -  <src>加密资产</src><tgt><|wait|></tgt>
12. <src>证券Tronics</src><tgt><|wait|></tgt>  -  <src>证券Tronics</src><tgt><|wait|></tgt>
13. <src>和BitTorrent。</src><tgt><|wait|></tgt>  -  <src>和BitTorrent。</src><tgt><|wait|></tgt>

---

## Test Example 5 / 6

  - UID: ZH_NWf8Wc2GVvM_W000007
  - SYSTEM_PROMPT: Translate to Japanese, tolerance window size is 1

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>启示录和</src><tgt>『ヨハネの黙示録』と</tgt>  -  <src>启示录和</src><tgt>ヨハネの黙示録と</tgt>
3. <src>翡翠石板</src><tgt><|wait|></tgt>  -  <src>肥衰时班</src><tgt><|wait|></tgt>
4. <src>都曾经预测到，</src><tgt>『エメラルド・タブレット』のどちらもが予言していたことがあります。</tgt>  -  <src>都曾经预测到，</src><tgt>水晶の石板があるからといって、予言していたのは</tgt>
5. <src>这十四万四千名</src><tgt><|wait|></tgt>  -  <src>这十四万四千名</src><tgt><|wait|></tgt>
6. <src>光之工作者</src><tgt>それは、14万4000人のライトワーカーが</tgt>  -  <src>光十字工作者退出了</src><tgt>14万4000人の光の十字架たちが退職したと。</tgt>
7. <src>的到来，会</src><tgt><|wait|></tgt>  -  <src>的到来，会</src><tgt><|wait|></tgt>
8. <src>在卡利年代</src><tgt>到来し、カリ・ユガの</tgt>  -  <src>在卡利年代</src><tgt>到来すると</tgt>
9. <src>结束时，</src><tgt><|wait|></tgt>  -  <src>结束时，</src><tgt><|wait|></tgt>
10. <src>将地球</src><tgt>終わりに地球を</tgt>  -  <src>将地球</src><tgt>終焉を迎える</tgt>
11. <src>从黑暗势力的手中</src><tgt><|wait|></tgt>  -  <src>从黑暗势力的手中</src><tgt>滅ぼそうと</tgt>
12. <src>拯救出来。</src><tgt>闇の勢力から救い出すということです。</tgt>  -  <src>拯救出来。</src><tgt>闇の勢力から救い出すと。</tgt>

---

## Test Example 6 / 6

  - UID: ZH_Y4xRc2amPxY_W000024
  - SYSTEM_PROMPT: Translate to Korean, tolerance window size is 4

1. <src>就会</src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>消耗我们</src><tgt><|wait|></tgt>  -  <src>消耗我们</src><tgt><|wait|></tgt>
3. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
4. <src>身体骨骼当中的</src><tgt><|wait|></tgt>  -  <src>身体骨骼当中的</src><tgt>우리 몸에서,</tgt>
5. <src>矿物质，更多的</src><tgt>우리 몸은 뼈 속의 미네랄을 소모하게 되고, 더 많은</tgt>  -  <src>矿物质，更多的</src><tgt>우리 몸에 있던 칼슘을</tgt>
6. <src>靠物矿物质。</src><tgt><|wait|></tgt>  -  <src>靠物</src><tgt><|wait|></tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
8. <src>所以呢，</src><tgt><|wait|></tgt>  -  <src>所以呢，</src><tgt>부 உலோக 성분이 필요하죠. 그래서 말 그대로</tgt>
9. <src>这个肥胖人</src><tgt><|wait|></tgt>  -  <src>这个肥胖人</src><tgt>부동사람이나</tgt>
10. <src>往往都会有</src><tgt>미네랄을 필요로 하게 됩니다. 그래서 비만인 분들은</tgt>  -  <src>往往都会有</src><tgt>종양이 환자들에게서 흔히 발견되는데요,</tgt>
11. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
12. <src>这种关节</src><tgt><|wait|></tgt>  -  <src>这种关节和</src><tgt><|wait|></tgt>
13. <src>和软组织</src><tgt><|wait|></tgt>  -  <src>和软组织</src><tgt><|wait|></tgt>
14. <src>的问题，就是</src><tgt><|wait|></tgt>  -  <src>的就是</src><tgt><|wait|></tgt>
15. <src>因为什么？</src><tgt>관절이나 연조직 문제를 자주 겪는데요. 왜 그럴까요?</tgt>  -  <src>因为什么？</src><tgt>관절이나 연부 조직 질환을 흔히 앓 곤두 돌기 때문인데요.</tgt>
16. <src>就是消耗了</src><tgt><|wait|></tgt>  -  <src>就是消耗了</src><tgt><|wait|></tgt>
17. <src>太多的矿物质。</src><tgt><|wait|></tgt>  -  <src>体内的矿物质。</src><tgt><|wait|></tgt>
```