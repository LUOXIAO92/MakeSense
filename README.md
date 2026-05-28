# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense is a research/data-generation project for building sense-aware training data and validation pipelines for simultaneous speech translation models with ASR/transcription support.

The goal is to convert speech translation into an incremental multi-turn conversation task: audio arrives chunk by chunk, and the model learns when to emit source transcription, when to emit target translation, and when to wait for more information.

Currently, the repository provides the dataset builder pipeline and training-data construction utilities. Hot words / hot translations support and an inference backend are planned future work.

## Project brief

Target: train an omni / multimodal model toward streaming simultaneous speech translation behavior with an additional ASR/transcription capability.

Inspired by following papers:
- Infinit input window/time-pressure simultaneous translation: [InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation: [SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

In this project:
- we **do not** train the sense-unit detector, audio encoder, or LLM backbone alignment from scratch;
- we **do not** modify the model architecture; infinite-time streaming translation is handled by sliding-window context management at runtime;
- we **do** create ground-truth-style datasets and pipeline validation surfaces so an omni model can learn simultaneous translation strategy;

## Requirement
### Python packages
```bash
pip install stanza jieba nagisa qwen-asr
pip install transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard --force-reinstall
```
- `qwen-asr` will install outdated `transformers` package

### Sub module dependence
- Word aligner: [TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- We use [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) as deafult base model.

## Pipeline

### Source / transcription side
1. initialize cache records from metadata
2. optional ASR transcription
3. forced alignment
4. time-pressure source sense-unit segmentation

### Target / translation side
1. raw translation
2. translation reconstruction
3. pure-text target sense-unit segmentation
4. target-centric source mapping
5. final dataset collection/export

## Usage: run the full dataset pipeline

The active workflow is driven by the stage scripts in `examples/`. Each stage reads the previous stage cache, writes a new stage cache, and can be resumed from existing JSONL cache state.

Before running, check the top-level configuration block in **each example script**. Common settings include dataset/cache roots, model names, target languages, `ENABLE_THINKING`, `TOP_P`, `TOP_K`, and `ENABLE_VISUALIZATION` where applicable.

### Current availability

Available now:
- dataset builder pipeline, through final pipeline-9 JSONL export;
- training example construction from the final dataset via `src/data_loader`;
- initial real-audio LoRA trainer implementation via `examples/train_lora.py` and `src/train`;

TODO:
- [x] High priority: test the thin LoRA trainer path with examples/train_lora.py on a tiny sample and confirm the rendered conversation, assistant-only loss setup, and 1-2 training steps behave correctly.
- [ ] Complete full LoRA training with `google/gemma-4-E2B-it`.
- [ ] **Second-highest priority:** add an inference backend for running the trained streaming model.
- [ ] Add hot words and hot translations support for training and inference contexts.

Small-scale validation result (`google/gemma-4-E2B-it`, `train_examples: 96`):
- tolerance window size: 1.0 s
- system prompt: Translate to Japanese, tolerance window size is 1
- Following is small scale test, left is ground truth, right is model output. I have disabled the thinking, but thinking content still occurs. An in-depth check is needed.
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

### LoRA training entry

The default LoRA training example targets `google/gemma-4-E2B-it` with a Transformers multimodal model, PEFT LoRA, real audio chunks, TensorBoard logging, and JSONL metric output.

Configure dataset, model, LoRA, and monitoring options at the top of:

```text
examples/train_lora.py
```

Run training with:

```bash
PYTHONPATH=src python examples/train_lora.py
```

Training writes the LoRA adapter and monitoring files under the configured `OUTPUT_DIR`:

```text
outputs/makesense_lora/
  adapter_config.json
  adapter_model.safetensors
  runs/
  train_metrics.jsonl
  sample_generations.jsonl
```

Sample generation uses strict streaming evaluation: each assistant turn is generated with only the audio chunks available up to that turn. The number of evaluated records is controlled by `SAMPLE_EVALUATION_RECORD_COUNT` in `examples/train_lora.py`.

### Pipeline order

Run the stages in this order:

```bash
export PYTHONPATH=src 

# 1. Download / prepare dataset source dataset if needed. (Here we use the Emilia dataset, refer to https://huggingface.co/datasets/amphion/Emilia-Dataset)
python examples/pipeline_1_download_Emilia.py

# 2. Initialize PipelineRecord cache shards from dataset metadata.
python examples/pipeline_2_initialize_cache.py

# 3a. Optional omni ASR + translation path.
# Use this when testing one-pass multimodal translation behavior.
python examples/pipeline_3_a_asr_translation_omni.py

# 3b-1. ASR-only path.
# This fills source transcript artifacts in the cache.
python examples/pipeline_3_b1_asr.py

# 3b-2. Raw translation from the ASR cache.
# Default is text-only; optional audio-assisted mode is controlled in the script, audio supported omni model is needed.
python examples/pipeline_3_b2_asr_text_translation.py

# 4. Forced alignment for source transcription.
python examples/pipeline_4_forced_alignment.py

# 5. Time-pressure source sense-unit segmentation.
python examples/pipeline_5_asr_segmentation.py

# 6. Translation reconstruction.
python examples/pipeline_6_translation_reconstruction.py

# 7. Pure-text target sense-unit segmentation.
python examples/pipeline_7_pure_text_segmentation.py

# 8. Target-centric mapping from target sense units to source token ids.
python examples/pipeline_8_target_centric_mapping.py

# 9. Collect/export the final dataset from finished pipeline-8 cache state.
python examples/pipeline_9_collect_dataset.py
```

Recommending sequence is:

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

### Final dataset output

Pipeline 9 exports the final dataset layout:

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

## Output format

### Streaming model output

```text
<src>(transcription text)</src><tgt>(target translation text)</tgt>
```

The model may emit `<|wait|>` when there is insufficient information to produce a stable source or target release.

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
