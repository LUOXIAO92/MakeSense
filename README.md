English | [简体中文](README_zh-cn.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

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
- I **do not** train the sense-unit detector, audio encoder, or LLM backbone alignment from scratch;
- I **do not** modify the model architecture; infinite-time streaming translation is handled by sliding-window context management at runtime;
- I **do** create ground-truth-style datasets and pipeline validation surfaces so an omni model can learn simultaneous translation strategy;

## Requirement

### Clone repository
```bash
git clone --recursive https://github.com/LUOXIAO92/MakeSense.git 
```

### Python packages

For dataset preparation:
- Create a new python env. Dataset preparation needs an independent env since `qwen-asr` incompatible with latest transformers.
- [Flash attention prebuild wheels](https://github.com/mjun0812/flash-attention-prebuild-wheels)
```bash
pip install whisper openai stanza
pip install qwen-asr --force-reinstall
pip install torch==2.10 torchaudio==2.10.0 torchvision --force-reinstall # --index-url https://download.pytorch.org/whl/cu130
```

For training: 
- Using a python 3.13 env is fine.
```bash
pip install stanza jieba nagisa transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard
pip install git+https://github.com/LUOXIAO92/MultimodalAssistantMask.git
```

### Sub module dependence
- Word aligner: [TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- I use [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) as deafult base model.
- I also use [MultimodalAssistantMask](https://github.com/LUOXIAO92/MultimodalAssistantMask.git) to build assistant only loss for multimodal inputs.

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

### Timing drift and alignment word grouping

Forced-alignment models can produce slightly drifted timestamps near the end of an utterance. As a result, the last few aligned tokens may have end times that exceed the real audio duration.

MakeSense treats this as expected tail drift rather than a fatal alignment problem. The streaming release windows are still defined by the real audio duration and the configured window size. When tail tokens drift past the real duration, downstream stages absorb those tail tokens into the final release window instead of creating an extra window or rejecting the whole record for that reason.

This tail-drift allowance does not remove the causal timing check inside forced-alignment output. Adjacent raw alignment tokens should remain monotonic: the previous token's end time should not be later than the next token's start time. By default, MakeSense rejects a record when this adjacent-token order is violated. Pipeline 4 also exposes an optional, default-off repair switch for small boundary drift: when enabled, a recoverable overlap where `next.start < prev.end < next.end` is repaired by setting `next.start = prev.end`. A touching zero-duration next token such as `prev.end == next.start == next.end` is accepted. If an overlap would make the next token zero-length or negative after repair (`prev.end >= next.end` while `prev.end > next.start`), the forced-alignment result is rejected as a validation failure for that record, while processing can continue for other records.

During training-data construction, if the audio duration is shorter than `window_count × window_size`, the audio input is padded to the corresponding window length. This keeps the conversation turns, release windows, and audio chunks aligned while preserving the real-duration-based window boundary semantics.

Pipeline 4 stores the forced aligner's timed tokens in `alignment.tokens`. It also stores `alignment.words`, which are tokenizer-produced groups that merge those timed tokens into words. Later stages, including Pipeline 8 `source_token_ids`, refer to these words, not directly to the raw timed token positions.

This grouping is needed because Qwen3-ForcedAligner can produce tokens that are finer than the words used later. For Chinese and Korean, Qwen3-ForcedAligner handles text at a very fine, effectively character-level timed-token granularity, so the tokenizer groups characters or other fine tokens into Chinese words or Korean whitespace/eojeol words. Japanese is the special case: Qwen3-ForcedAligner uses the `nagisa` tokenizer for Japanese timed tokens, while MakeSense may use a different project tokenizer when building `alignment.words`, so Japanese words may also be formed by merging timed tokens across tokenizer-boundary differences.

MakeSense intentionally uses a conservative timing strategy for these groups. Streaming simultaneous translation depends on strict time causality, so the pipeline does not split one timed token and invent sub-token timestamps. Instead, when several timed tokens are grouped into one word, the word uses the first token's start time and the last token's end time. This avoids artificial time boundaries that could break causal streaming behavior.

## Usage: run the full dataset pipeline

The active workflow is driven by the stage scripts in `examples/`. Each stage reads the previous stage cache, writes a new stage cache, and can be resumed from existing JSONL cache state.

Before running, check the top-level configuration block in **each example script**. Common settings include dataset/cache roots, model names, target languages, `TOP_P`, provider-specific `EXTRA_BODY`, and `ENABLE_VISUALIZATION` where applicable.

`EXTRA_BODY` is passed through to the OpenAI-compatible Chat Completions request and can carry provider-specific extensions. Parameters such as `top_k` and thinking/reasoning controls use different schemas across providers; the examples below show several common provider-specific shapes:

```python
# vLLM / local OpenAI-compatible API example:
EXTRA_BODY = {"top_k": 20, "chat_template_kwargs": {"enable_thinking": False}}

# OpenRouter reasoning example:
EXTRA_BODY = {"reasoning": {"effort": "none"}}

# DeepSeek thinking example:
EXTRA_BODY = {"thinking": {"type": "disabled"}}
```

References:
- OpenRouter reasoning tokens: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens
- DeepSeek thinking mode: https://api-docs.deepseek.com/guides/thinking_mode

### Current availability

Available now:
- dataset builder pipeline, through final pipeline-9 JSONL export;
- training example construction from the final dataset via `src/data_loader`;
- initial real-audio LoRA trainer implementation via `examples/train_lora.py` and `src/train`;
- **NEW**: [MakeSense-Emilia-Dataset](https://huggingface.co/datasets/luoxiao9231/MakeSense-Emilia-Dataset), license: cc-by-nc-4.0
  - This dataset includes 8,000 audio/transcription records and 24,000 translation-strategy records in multi-turn conversation trajectory format. 
  - This dataset is built through secondary processing of [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset). I sincerely thank the Emilia-Dataset project for this excellent multilingual audio dataset.

TODO:
- [x] **High priority**: test the thin LoRA trainer path with examples/train_lora.py on a tiny sample and confirm the rendered conversation, assistant-only loss setup, and 1-2 training steps behave correctly.
- [ ] **High priority**: complete full LoRA training with `google/gemma-4-E2B-it`.
  - **Completed**: an initial large-scale `gemma-4-E2B-it` training and evaluation run is complete; the [LoRA checkpoint is here](/lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100). See the metrics section in the results below for detailed data.
  - **Ongoing**: I'm still fighting with the best hyper parameters and optimizing the vram usage. 
- [ ] **Second-highest priority:** add an inference backend for running the trained streaming model.
  - **Ongoing**: related work is tracked in [MakeSense-Inference](https://github.com/LUOXIAO92/MakeSense-Inference.git).
- [ ] Add hot words and hot translations support for training and inference contexts.

### LoRA training entry

The default LoRA training example targets `google/gemma-4-E2B-it` with a Transformers multimodal model, PEFT LoRA, real audio chunks, project-owned TensorBoard scalar logging, and strict streaming test metrics.

Configure dataset, model, LoRA, checkpoint, and monitoring options at the top of:

```text
examples/train_lora.py
```

Common controls include:
- `OUTPUT_DIR`
- `CONTINUE_TYPE`: `none`, `resume`, or `branch`
- `CHECKPOINT_PATH`
- `SAVE_PROCESSOR`
- `TEST_STEPS`, `TEST_MAX_NEW_TOKENS`, `TEST_RECORD_COUNT`

Run training with:

```bash
PYTHONPATH=src python examples/train_lora.py
```

Training writes the LoRA adapter and monitoring files under the configured `OUTPUT_DIR`:

```text
outputs/makesense_lora/
├── adapter_config.json
├── adapter_model.safetensors
├── checkpoint-*/
├── runs/
│   └── <yyyy-mm-dd_hh-mm-ss>/
└── test_metrics.json
```

Strict streaming tests generate each assistant turn with only the audio chunks available up to that turn. The number of evaluated records is controlled by `TEST_RECORD_COUNT` in `examples/train_lora.py`: `0` disables tests, `-1` uses the full test split, and a positive value selects up to that many records.

### Customization
Refer to `src/configs/config.py` and `src/configs/LANGUAGE_PACK_*.py` for pipeline-level, non-training customization. Common configurable items include dataset sampling limits, supported languages, ASR / forced-alignment model names, tokenizer choices, wait token, streaming window size, maximum chunk size, reconstruction-validator high-noise tokens, and per-language language packs / few-shot examples used by segmentation stages.

### Pipeline order

Run the stages in this order:

```bash
export PYTHONPATH=src 

# 1. Download / prepare dataset source dataset if needed. (Here we use the Emilia dataset, refer to https://huggingface.co/datasets/amphion/Emilia-Dataset)
python examples/pipeline_1_download_Emilia.py

# 2. Initialize PipelineRecord cache shards from dataset metadata.
python examples/pipeline_2_initialize_cache.py

# 3a-1. Recommended ASR path.
# This fills source transcript artifacts in the cache.
python examples/pipeline_3_a1_asr.py

# 3a-2. Recommended ASR-based raw translation path.
# In practice, ASR followed by omni/audio-assisted correction is more reliable than direct omni ASR,
# with higher accuracy and stability across Chinese, Japanese, and Korean.
python examples/pipeline_3_a2_asr_text_translation.py

# 3b. Optional direct omni ASR + translation path.
# Use this when testing one-pass multimodal translation behavior.
python examples/pipeline_3_b_asr_translation_omni.py

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
python examples/pipeline_3_a1_asr.py
python examples/pipeline_3_a2_asr_text_translation.py
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

The `dimensional_analysis/` branch is an independent export of the whole-utterance `target.shared.translation_analysis` produced during translation. It is kept separate from the transcription and translation dataset schemas.

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

## Inference framework note: constrained decoding for concurrent multimodal generation

The large-scale validation results below are real test results with `batch=1`. They measure real rollout for one sample at a time: each model output is appended back into the next prompt. So these results reflect protocol compliance without concurrent / batched generation effects. They are validation records from the current large-scale training stage, not evidence that the hyperparameters are already optimal.

As long as concurrent or batched generation exists, there is extra risk: the next-token candidate scores for the same request may not be exactly the same when the request runs alone versus inside a batch. When candidate scores are close, the first- or second-preferred token may swap. That can affect sampling and can also make protocol-style outputs drift outside the allowed forms. In this multi-batch vs single-batch investigation, this risk was more obvious for Gemma 4 audio+text than for the comparison models and the pure-text baseline.

When building the inference backend for this project, constrained decoding will be used, for example vLLM guided decoding / structured outputs or llama.cpp GBNF grammar, to restrict outputs to the six currently supported protocol forms. See [Gemma 4 multimodal batch-rank note](lessons/gemma4_multimodal_batch_rank_en.md) for details.

## Large-scale validation results (`google/gemma-4-E2B-it`, `train_examples: 21540`):

### Training paramenters

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

### Results

#### Metrics

These strict streaming test metrics measure protocol validity, generation stopping behavior, and wait/release decisions for each assistant turn. Valid protocol units include ASR-only `<src>...</src>` turns and translation `<src>...</src><tgt>...</tgt>` turns. They do **not** directly measure ASR word accuracy or translation semantic quality.

**POSTPROCESSED_TURN_STOP_RATE**

- Meaning: the rate of turns whose postprocessed output stops cleanly at a closed protocol-tag boundary.
- Calculation: `postprocessed_turn_stop_turns / TURN_COUNT`, where a turn counts as stopped when the parsed protocol unit is followed only by whitespace or an allowed EOS / generation-stop marker. Any non-EOS content outside the closed protocol tags fails this metric, such as trailing text, comma-separated tags, or repeated protocol chunks.

**PROTOCOL_VALID_RATE**

- Meaning: the rate of turns whose model output has legal source/target protocol tags.
- Calculation: `protocol_valid_turns / TURN_COUNT`, where a turn is valid if it starts with a legal ASR-only unit `<src>...</src>` or translation unit `<src>...</src><tgt>...</tgt>`, with paired tags, legal order, and no nested source/target tags inside any field. This metric checks tag legality; out-of-tag continuation after a closed protocol unit is measured by `POSTPROCESSED_TURN_STOP_RATE`.

**RAW_TURN_STOP_RATE**

- Meaning: the rate of turns whose raw decoded generation stops at the configured generation stop token.
- Calculation: `raw_turn_stop_turns / TURN_COUNT`, where a turn counts as stopped when the raw decoded text continues from the postprocessed text with `generation_stop`.

**RECORD_COUNT**

- Meaning: the number of selected test records evaluated in this strict streaming test.
- Calculation: `len(records)`.

**SRC_RELEASE_ACCURACY**

- Meaning: among turns where the ground-truth source side should release transcription text, the rate at which the model also releases source text.
- Calculation: `src_release_correct / SRC_RELEASE_TOTAL`. This checks only wait vs. non-wait behavior in `<src>...</src>`; it does not check whether the released transcription text is correct.

**SRC_RELEASE_TOTAL**

- Meaning: the number of turns where the ground-truth source side is a non-wait release.
- Calculation: count of turns where ground-truth `<src>...</src>` is not `<|wait|>`.

**SRC_WAIT_ACCURACY**

- Meaning: among turns where the ground-truth source side should wait, the rate at which the model also waits on the source side.
- Calculation: `src_wait_correct / SRC_WAIT_TOTAL`. This checks only whether model `<src>...</src>` is `<|wait|>`.

**SRC_WAIT_TOTAL**

- Meaning: the number of turns where the ground-truth source side should wait.
- Calculation: count of turns where ground-truth `<src>...</src>` is exactly `<|wait|>` after stripping whitespace.

**TGT_RELEASE_ACCURACY**

- Meaning: among turns where the ground-truth target side should release translation text, the rate at which the model also releases target text.
- Calculation: `tgt_release_correct / TGT_RELEASE_TOTAL`. This checks only wait vs. non-wait behavior in `<tgt>...</tgt>`; it does not check whether the released translation text is semantically correct.

**TGT_RELEASE_TOTAL**

- Meaning: the number of turns where the ground-truth target side is a non-wait release.
- Calculation: count of turns where ground-truth `<tgt>...</tgt>` is not `<|wait|>`.

**TGT_WAIT_ACCURACY**

- Meaning: among turns where the ground-truth target side should wait, the rate at which the model also waits on the target side.
- Calculation: `tgt_wait_correct / TGT_WAIT_TOTAL`. This checks only whether model `<tgt>...</tgt>` is `<|wait|>`.

**TGT_WAIT_TOTAL**

- Meaning: the number of turns where the ground-truth target side should wait.
- Calculation: count of turns where ground-truth `<tgt>...</tgt>` is exactly `<|wait|>` after stripping whitespace.

**TURN_COUNT**

- Meaning: the total number of assistant turns evaluated across all selected test records.
- Calculation: sum of all generated/evaluated assistant outputs across `records`.

#### Metrics: Gemma-4-E2B-it, learning rate=3e-4, rank=16, batch size=16, bnb4bit, adamw

**Test metrics**:
- best overall - step 8100

![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/test_metrics_plot.png)

Please refer to [strict test](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/test_outputs) to veiw the result of strict test.


**Training**:
![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/train_loss.png)
![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/learning_rage_schedule.png)
![](lora/Gemma-4-E2B-it_lr3e-4_r16_bs16_bnb4bit_adamw_checkpoint-8100/eval_loss.png)


#### Test Outputs - step 300

**Note**: Following sample is not the case of above hyper parameters.

- tolerance window size: 1.0 s
- The following selected test examples show ground truth on the left and model output on the right.

```text
Test Metrics
  - STEP: 300
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - POSTPROCESSED_TURN_STOP_RATE: 1.0000
  - PROTOCOL_VALID_RATE: 1.0000
  - RAW_TURN_STOP_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9443
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.2450
  - SRC_WAIT_TOTAL: 151
  - TGT_RELEASE_ACCURACY: 0.7248
  - TGT_RELEASE_TOTAL: 298
  - TGT_WAIT_ACCURACY: 0.7996
  - TGT_WAIT_TOTAL: 489
  - TURN_COUNT: 869

---

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


#### Final Test Outputs - step 5400

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