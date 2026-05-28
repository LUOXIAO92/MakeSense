# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense 是一个面向研究和数据生成的项目，用于为同步语音翻译模型构建具备语义单元感知能力的训练数据和验证流程，并同时支持 ASR / 转写能力。

这个项目的目标，是把语音翻译改造成一个增量式的多轮对话任务: 音频会一段一段地输入，模型需要学习什么时候输出源语言转写，什么时候输出目标语言翻译，以及什么时候应该继续等待更多信息。

目前，这个仓库主要提供数据集构建 pipeline 和训练数据构造工具。热词 / 热门译法支持以及推理后端仍属于后续计划。

## 项目简介

目标: 训练一个全模态 / 多模态模型，使其具备流式同步语音翻译能力，同时额外支持 ASR / 语音转写。

本项目受到以下论文启发: 
- 无限输入 window/time-pressure 同步翻译: [InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation: [SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

在这个项目中: 
- 我们**不**从零训练语义单元检测器、音频编码器，或 LLM backbone 的对齐模块；
- 我们**不**修改模型架构；无限时长的流式翻译会在运行时通过滑动窗口上下文管理来处理；
- 我们**会**构建接近 ground truth 风格的数据集，并提供用于验证 pipeline 的接口和中间结果，让全模态模型能够学习同步翻译策略；

## 环境要求
### Python 依赖包
```bash
pip install stanza jieba nagisa qwen-asr transformers peft torch torchvision torchaudio unsloth
```

### 子模块依赖
- 词对齐工具: [TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- 默认基础模型使用 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE)。

## Pipeline

### 源语言 / 转写侧
1. 根据 metadata 初始化 cache records
2. 可选的 ASR 转写
3. forced alignment
4. 基于时间压力的源语言语义单元切分

### 目标语言 / 翻译侧
1. 原始翻译
2. 翻译重构
3. 纯文本目标语言语义单元切分
4. 以目标语言为中心的源语言映射
5. 最终数据集收集与导出

## 使用方法: 运行完整数据集 pipeline

当前工作流由 `examples/` 目录下的各阶段脚本驱动。每个阶段都会读取上一个阶段的 cache，写入新的阶段 cache，并且可以基于已有的 JSONL cache 状态继续运行。

运行前，首先检查**每个 example 脚本顶部的配置区块**。常见配置包括数据集 / cache 根目录、模型名称、目标语言、`ENABLE_THINKING`、`TOP_P`、`TOP_K`，以及在适用场景下的 `ENABLE_VISUALIZATION`。

### 当前可用功能

目前已经可用: 
- 数据集构建 pipeline，可一直运行到最终的 pipeline-9 JSONL 导出；
- 通过 `src/data_loader`，从最终数据集中构造训练样本；
- 通过 `examples/train_lora.py` 和 `src/train` 提供轻量级 LoRA SFT 训练入口；目前它只覆盖文本 dry-run 场景，其中 `<|audio|>` 只是一个文本占位符；

待办事项: 
- [ ] **高优先级:** 在一个极小样本上测试 `examples/train_lora.py` 这条轻量 LoRA 训练路径，并确认 conversation 渲染、assistant-only loss 设置，以及 1-2 个训练 step 都能正常工作。 <- 由于unsloth的兼容问题，计划转为使用 transformers `trainer` (transformers 的 `AutoModelForCausalLM` 不支持直接加载 qwen2.5/3-omni 系列的模型，必须要通过 `Qwen2_5OmniForConditionalGeneration`)。 目前 `SFTtrainer` 似乎也不支持音频输入
- [ ] **高优先级:** 训练器完成 sanity check 后，对 `Qwen/Qwen2.5-Omni-3B` 运行 LoRA 训练。
- [ ] **次高优先级:** 增加推理后端，用于运行训练好的流式模型。
- [ ] 为训练和推理上下文加入热词与热门译法支持。

### LoRA 训练入口

LoRA 训练入口为: 

```bash
PYTHONPATH=src python examples/train_lora.py
```

### Pipeline 运行顺序

请按以下顺序运行各阶段: 

```bash
export PYTHONPATH=src 

# 1. 如有需要，下载 / 准备数据集源数据。
#    这里使用 Emilia 数据集，详见 https://huggingface.co/datasets/amphion/Emilia-Dataset
python examples/pipeline_1_download_Emilia.py

# 2. 根据数据集 metadata 初始化 PipelineRecord cache shards。
python examples/pipeline_2_initialize_cache.py

# 3a. 可选的 omni ASR + translation 路径。
#     当需要测试一次性多模态翻译行为时使用这一路径。
python examples/pipeline_3_a_asr_translation_omni.py

# 3b-1. 仅 ASR 路径。
#       这一步会在 cache 中填入源语言转写结果。
python examples/pipeline_3_b1_asr.py

# 3b-2. 基于 ASR cache 生成原始翻译。
#       默认是纯文本模式；可选的音频辅助模式由脚本内部配置控制，需要支持音频输入的omni模型。
python examples/pipeline_3_b2_asr_text_translation.py

# 4. 对源语言转写结果进行 forced alignment。
python examples/pipeline_4_forced_alignment.py

# 5. 基于时间压力的源语言语义单元切分。
python examples/pipeline_5_asr_segmentation.py

# 6. 翻译重构。
python examples/pipeline_6_translation_reconstruction.py

# 7. 纯文本目标语言语义单元切分。
python examples/pipeline_7_pure_text_segmentation.py

# 8. 将目标语言语义单元映射到源语言 token ids。
python examples/pipeline_8_target_centric_mapping.py

# 9. 从已完成的 pipeline-8 cache 状态中收集并导出最终数据集。
python examples/pipeline_9_collect_dataset.py
```

推荐运行顺序为: 

```bash
python examples/pipeline_2_initialize_cache.py
python examples/pipeline_3_b1_asr.py
python examples/pipeline_3_b2_asr_text_translation.py
python examples/pipeline_4_forced_alignment.py
python examples/pipeline_5_asr_segmentation.py
python examples/pipeline_6_translation_reconstruction.py
python examples/pipeline_7_pure_text_segmentation.py
python examples/pipeline_8_target_centric_mapping.py
python examples/pipeline_9_collect_dataset.py
```

### 最终数据集输出

Pipeline 9 会导出如下最终数据集目录结构: 

```
path/to/output/dir/
  transcription/
    EN/transcription-EN-partXXXXXX.jsonl
    JA/transcription-JA-partXXXXXX.jsonl
    KO/transcription-KO-partXXXXXX.jsonl
    ZH/transcription-ZH-partXXXXXX.jsonl
  translation/
    EN/translation-EN_JA-partXXXXXX.jsonl
    EN/translation-EN_KO-partXXXXXX.jsonl
    EN/translation-EN_ZH-partXXXXXX.jsonl
    ...
```

## 输出格式

### 流式模型输出

```text
<src>(转写文本)</src><tgt>(目标语言翻译文本)</tgt>
```

当信息还不足以稳定地产生源语言转写或目标语言翻译时，模型可以输出 `<|wait|>`。

### Conversation 格式

```text
system
[system prompts]
[hot words / task context]
user
<|audio|>
assistant
<src>(转写文本或 <|wait|>)</src><tgt>(目标语言翻译文本或 <|wait|>)</tgt>
user
<|audio|>
assistant
<src>(下一段转写文本或 <|wait|>)</src><tgt>(下一段目标语言翻译文本或 <|wait|>)</tgt>
...
```
