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
- [x] **High priority**: complete full LoRA training with `google/gemma-4-E2B-it`.
  - **Completed**: an initial large-scale `gemma-4-E2B-it` training and evaluation run is complete; the [LoRA checkpoint is here](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000). See the metrics section in the results below for detailed data.
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

## Training Configs

### Gemma4-E2B/E4B-it

```python
ASSISTANT_HEADER = "<|turn>model\n"
ASSISTANT_END = "<turn|>"
GENERATION_STOP = "<turn|>"

LORA_TARGET_MODULES = (
    r"^model\.language_model\.layers\.\d+\."
    r"(self_attn\.(q_proj|k_proj|v_proj|o_proj)|"
    r"mlp\.(gate_proj|up_proj|down_proj))$"
)
```

## Inference framework note: constrained decoding for concurrent multimodal generation

The large-scale validation results below are real test results with `batch=1`. They measure real rollout for one sample at a time: each model output is appended back into the next prompt. So these results reflect protocol compliance without concurrent / batched generation effects. They are validation records from the current large-scale training stage, not evidence that the hyperparameters are already optimal.

As long as concurrent or batched generation exists, there is extra risk: the next-token candidate scores for the same request may not be exactly the same when the request runs alone versus inside a batch. When candidate scores are close, the first- or second-preferred token may swap. That can affect sampling and can also make protocol-style outputs drift outside the allowed forms. In this multi-batch vs single-batch investigation, this risk was more obvious for Gemma 4 audio+text than for the comparison models and the pure-text baseline.

When building the inference backend for this project, constrained decoding will be used, for example vLLM guided decoding / structured outputs or llama.cpp GBNF grammar, to restrict outputs to the six currently supported protocol forms. See [Gemma 4 multimodal batch-rank note](lessons/gemma4_multimodal_batch_rank_en.md) for details.

## Large-scale validation results (`google/gemma-4-E2B-it`, `train_examples: 21540`):

# IMPORTANT: SINCE I LEAKED THE TRAIN SET WITH A STUPID BUG (SPLIT THE DATASET FROM TRANSLATION RECORDS BUT NOT AUDIO RECORDS), THE FOLLOWING METIRCS IS UNRELIABLE. I WILL RETRAIN THE LORA SOON. ALSO SINCE THERE ARE NO AVALIABLE DETAILED AUDIO METRICS OF GEMMA4, I WILL SWITCH THE BASE MODEL TO QWEN2.5-OMNI

<!-- 
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

### Results

#### Metrics

These strict streaming test metrics measure protocol adherence and wait/release decisions for each assistant turn. Clean protocol units include ASR-only `<src>...</src>` turns and translation `<src>...</src><tgt>...</tgt>` turns.

**PROTOCOL_ADHERENCE_RATE**

- Meaning: the rate of turns whose model output follows the strict source/target protocol.
- Calculation: `protocol_adherent_turns / TURN_COUNT`.
- A turn is protocol-adherent when the full model output is exactly one clean `<src>...</src>` unit or one clean `<src>...</src><tgt>...</tgt>` unit.
- `<src>` and `<tgt>` fields must contain clean transcription or translation text. They cannot contain nested `<src>` / `<tgt>` tags.
- If a field contains `<|wait|>`, the stripped field content must equal `<|wait|>`.
- Text outside the closed protocol unit, comma-joined chunks, repeated protocol chunks, broken tags, wrong tag order, and mixed wait/text fields fail this metric.

All source/target wait/release accuracy metrics use protocol-adherent model turns as their denominator base. A non-adherent model turn only affects `PROTOCOL_ADHERENCE_RATE`. Fixed-window and conservative target metrics also keep the record-level window eligibility filter.

**RECORD_COUNT**

- Meaning: the number of selected test records evaluated in this strict streaming test.
- Calculation: `len(records)`.

**SRC_RELEASE_ACCURACY**

- Meaning: among protocol-adherent model turns where the ground-truth source side should release transcription text, the rate at which the model also releases source text.
- Calculation: `src_release_correct / SRC_RELEASE_TOTAL`. This checks only wait vs. non-wait behavior in `<src>...</src>`; it does not check whether the released transcription text is correct.

**SRC_RELEASE_TOTAL**

- Meaning: the number of protocol-adherent model turns where the ground-truth source side is a non-wait release.
- Calculation: count of protocol-adherent model turns where ground-truth `<src>...</src>` is not `<|wait|>`.

**SRC_WAIT_ACCURACY**

- Meaning: among protocol-adherent model turns where the ground-truth source side should wait, the rate at which the model also waits on the source side.
- Calculation: `src_wait_correct / SRC_WAIT_TOTAL`. This checks only whether model `<src>...</src>` is `<|wait|>`.

**SRC_WAIT_TOTAL**

- Meaning: the number of protocol-adherent model turns where the ground-truth source side should wait.
- Calculation: count of protocol-adherent model turns where ground-truth `<src>...</src>` is exactly `<|wait|>` after stripping whitespace.

**TGT_RELEASE_ACCURACY**

- Meaning: among protocol-adherent model turns where the ground-truth target side should release translation text, the rate at which the model also releases target text.
- Calculation: `tgt_release_correct / TGT_RELEASE_TOTAL`. This checks only wait vs. non-wait behavior in `<tgt>...</tgt>`; it does not check whether the released translation text is semantically correct.

**TGT_RELEASE_TOTAL**

- Meaning: the number of protocol-adherent model turns where the ground-truth target side is a non-wait release.
- Calculation: count of protocol-adherent model turns where ground-truth `<tgt>...</tgt>` is not `<|wait|>`.

**TGT_WAIT_ACCURACY**

- Meaning: among protocol-adherent model turns where the ground-truth target side should wait, the rate at which the model also waits on the target side.
- Calculation: `tgt_wait_correct / TGT_WAIT_TOTAL`. This checks only whether model `<tgt>...</tgt>` is `<|wait|>`.

**TGT_WAIT_TOTAL**

- Meaning: the number of protocol-adherent model turns where the ground-truth target side should wait.
- Calculation: count of protocol-adherent model turns where ground-truth `<tgt>...</tgt>` is exactly `<|wait|>` after stripping whitespace.

**TURN_COUNT**

- Meaning: the total number of assistant turns evaluated across all selected test records.
- Calculation: sum of all generated/evaluated assistant outputs across `records`.

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
--->