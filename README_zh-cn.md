# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense 是一个面向研究和数据生成的项目，用来为同步语音翻译模型构建具备语义感知能力的训练数据和验证流程，同时支持 ASR / 转写任务。

项目目标是把语音翻译改造成增量式多轮对话任务：音频按片段陆续到达，模型学习何时输出源语言转写、何时输出目标语言翻译，以及何时等待更多上下文。

目前，仓库提供数据集构建 pipeline 和训练数据构造工具。热词 / 指定译法支持以及推理后端属于后续工作。

## 项目简介

目标：训练一个 omni / 多模态模型，使其具备流式同步语音翻译能力，并额外支持 ASR / 转写。

本项目受到以下论文启发：
- 无限输入窗口 / time-pressure 同步翻译：[InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation：[SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

在本项目中：
- 我们**不**从零训练 sense-unit detector、audio encoder 或 LLM backbone alignment；
- 我们**不**修改模型架构；无限时长的流式翻译由运行时的滑动窗口上下文管理来处理；
- 我们**会**构建 ground-truth 风格的数据集和 pipeline 验证界面，让 omni 模型学习同步翻译策略；

## 环境要求
### Python packages
```bash
pip install stanza jieba nagisa qwen-asr
pip install transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard --force-reinstall
```
- `qwen-asr` 会安装较旧版本的 `transformers`。

### 子模块依赖
- 词对齐工具：[TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- 默认基础模型使用 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE)。

## Pipeline

### 源语言 / 转写侧
1. 从 metadata 初始化 cache records
2. 可选 ASR 转写
3. forced alignment
4. time-pressure 源语言 sense-unit segmentation

### 目标语言 / 翻译侧
1. raw translation
2. translation reconstruction
3. pure-text target sense-unit segmentation
4. target-centric source mapping
5. final dataset collection/export

## 使用方法：运行完整数据集 pipeline

当前工作流由 `examples/` 下的阶段脚本驱动。每个阶段读取上一阶段 cache，写入新的阶段 cache，并且可以从已有 JSONL cache 状态恢复运行。

运行前请检查**每个 example 脚本顶部的配置区块**。常见配置包括 dataset/cache roots、model names、target languages、`ENABLE_THINKING`、`TOP_P`、`TOP_K`，以及适用场景下的 `ENABLE_VISUALIZATION`。

### 当前可用功能

已经可用：
- 数据集构建 pipeline，可运行到最终 pipeline-9 JSONL 导出；
- 通过 `src/data_loader` 从最终数据集构造训练样本；
- 通过 `examples/train_lora.py` 和 `src/train` 提供初版 real-audio LoRA trainer；

TODO：
- [x] 高优先级：在极小样本上测试 `examples/train_lora.py` 的 LoRA trainer 路径，确认 conversation 渲染、assistant-only loss 设置以及 1-2 个 training steps 正常工作。
- [ ] 完成 `google/gemma-4-E2B-it` 的完整 LoRA 训练。
- [ ] **次高优先级：** 增加推理后端，用于运行训练好的 streaming model。
- [ ] 为训练和推理上下文增加 hot words 和 hot translations 支持。

小规模验证结果（`google/gemma-4-E2B-it`, `train_examples: 96`）：
- tolerance window size: 1.0 s
- system prompt: Translate to Japanese, tolerance window size is 1
- 以下为小规模测试结果，左侧是 ground truth，右侧是 model output。thinking 已经关闭，但输出里仍出现 thinking 内容，需要进一步排查。
```text
1. <src><|wait|></src><tgt><|wait|></tgt>  -  「そして」
2. <src>그리고 아 그리고 </src><tgt>それと、あ、</tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
user
thought
Thinking Process:

1.  **Analyze the Request:** The user has provided a series of input prompts (in this case, "그리고 우리" and "그리고 우리" repeated) and expects a Japanese translation. The user also specified a constraint: "tolerance window size is 1".

2.  **Analyze the Input (Source Text):** The input is "그리고 우리" (and we/us). This is a very short, somewhat vague phrase.

3.  **Analyze the Constraint (Tolerance Window Size is 1):** This is a machine translation task. The constraint means that the generated translation should be very close to the expected meaning, and the input translation should be very close to the provided input (or in this case, the target translation should be the most natural equivalent).

4.  **Determine the Meaning of "그리고 우리":**
    *   "그리고" (그리고) means "and".
    *   "우리" (우리) means "we" or "us" (inclusive of the speaker and listener).
    *   The combination is "And we/us".

5.
3. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>그리고 우리 ... </src><tgt>そして、私たちは...</tgt>
4. <src>우리 가 뉴욕 에 </src><tgt>私たちはニューヨークに</tgt>  -  <src>그리고 우리가 살고 있으니까 </src><tgt>私たちは住んでいるので、</tgt>
5. <src>살고 있으니까 좀 </src><tgt><|wait|></tgt>  -  <src>살고 있으니까 뉴욕과 뉴저지는 </src><tgt>住んでいるので、ニューヨークとニュージャージーは</tgt>
6. <src>뉴욕 과 뉴저지 지역 의 </src><tgt>住んでいるので、ニューヨークやニュージャージーの</tgt>  -  <src>유명한 뉴요커 </src><tgt><|wait|></tgt>
7. <src>유명 한 곳을 소개 해드릴 </src><tgt><|wait|></tgt>  -  <src>유명한 곳들 </src><tgt>有名な場所たち</tgt>
8. <src>수도 있어요. 그렇 죠, 그렇 죠. </src><tgt>有名な場所をご紹介することもできます。そうですね、その通りです。</tgt>  -  <src>유명한 곳을 소개 해드릴 수 있습니다.</src><tgt><|wait|></tgt>
9. <src>직접 </src><tgt><|wait|></tgt>  -  <src>네. 현장에 </src><tgt><|wait|></tgt>
10. <src>그 현장 에 가서 </src><tgt>実際にその現場へ行って、</tgt>  -  <src>직접 </src><tgt><|wait|></tgt>
11. <src>저희 들이 이제 </src><tgt><|wait|></tgt>  -  <src>체험해 보세요. </src><tgt>体験してみてください。</tgt>
12. <src>체험 도 해보고 </src><tgt>私たちが体験した様子を</tgt>  -  <src>시험해 드릴게요. </src><tgt>体験して差し上げましょう。</tgt>
13. <src>소개 도 해드리고 </src><tgt><|wait|></tgt>  -  <src>보고 싶어요. </src><tgt>見てみたいです。</tgt>
14. <src>그런 프로그램 도 </src><tgt>お届けするような番組も</tgt>  -  <src>프로그램도 만들게요. </src><tgt>プログラムも作ります。</tgt>
15. <src>만들 기획 이고요. </src><tgt><|wait|></tgt>  -  <src>만들게요. 어떠세요? </src><tgt>作りますよ。いかがですか？</tgt>
16. <src><|wait|></src><tgt>企画しています。では、</tgt>  -  <src>네. 맞습니다. </src><tgt>はい。その通りです。</tgt>
17. <src>뉴욕 미니 스에 대한 </src><tgt><|wait|></tgt>  -  <src>뉴욕 미니 </src><tgt>ニューヨークについて説明します。</tgt>
18. <src>설명 을 좀 해주시죠. </src><tgt>ニューヨーク・ミニについて少し説明していただけますか。</tgt>  -  <src>설명을 해주시죠. </src><tgt>ミニ番組について説明してください。</tgt>
```

### LoRA 训练入口

默认 LoRA 训练示例使用 `google/gemma-4-E2B-it`，基于 Transformers multimodal model、PEFT LoRA、真实音频 chunks、TensorBoard logging 和 JSONL metrics。

请在下面文件顶部配置 dataset、model、LoRA 和 monitoring 选项：

```text
examples/train_lora.py
```

运行训练：

```bash
PYTHONPATH=src python examples/train_lora.py
```

训练会把 LoRA adapter 和 monitoring 文件写入配置的 `OUTPUT_DIR`：

```text
outputs/makesense_lora/
  adapter_config.json
  adapter_model.safetensors
  runs/
  train_metrics.jsonl
  sample_generations.jsonl
```

Sample generation 使用 strict streaming evaluation：每个 assistant turn 只使用截至该 turn 已经可见的音频 chunks。评估记录数由 `examples/train_lora.py` 中的 `SAMPLE_EVALUATION_RECORD_COUNT` 控制。

### Pipeline 运行顺序

按以下顺序运行各阶段：

```bash
export PYTHONPATH=src 

# 1. 如有需要，下载 / 准备数据集源数据。（这里使用 Emilia dataset，参考 https://huggingface.co/datasets/amphion/Emilia-Dataset）
python examples/pipeline_1_download_Emilia.py

# 2. 从 dataset metadata 初始化 PipelineRecord cache shards。
python examples/pipeline_2_initialize_cache.py

# 3a. 可选 omni ASR + translation 路径。
# 用于测试 one-pass multimodal translation 行为。
python examples/pipeline_3_a_asr_translation_omni.py

# 3b-1. ASR-only path。
# 这一步会在 cache 中填入 source transcript artifacts。
python examples/pipeline_3_b1_asr.py

# 3b-2. 从 ASR cache 生成 raw translation。
# 默认是 text-only；可选 audio-assisted mode 在脚本中控制，需要支持 audio 的 omni model。
python examples/pipeline_3_b2_asr_text_translation.py

# 4. 对 source transcription 执行 forced alignment。
python examples/pipeline_4_forced_alignment.py

# 5. Time-pressure source sense-unit segmentation。
python examples/pipeline_5_asr_segmentation.py

# 6. Translation reconstruction。
python examples/pipeline_6_translation_reconstruction.py

# 7. Pure-text target sense-unit segmentation。
python examples/pipeline_7_pure_text_segmentation.py

# 8. 将 target sense units 映射到 source token ids。
python examples/pipeline_8_target_centric_mapping.py

# 9. 从已完成的 pipeline-8 cache state 收集 / export 最终数据集。
python examples/pipeline_9_collect_dataset.py
```

推荐顺序：

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

Pipeline 9 导出如下最终数据集结构：

```text
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

### Streaming model output

```text
<src>(transcription text)</src><tgt>(target translation text)</tgt>
```

当信息不足以稳定输出源语言转写或目标语言翻译时，模型可以输出 `<|wait|>`。

### Conversation format

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
