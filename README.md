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

#### Metrics: Gemma-4-E2B-it, learning rate=1e-4, rank=16, batch size=16, bnb nf4 4bit, adamw

**Test metrics**:

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


**Training**:
![](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000/training_and_testing_metrics/training_metrics_plot.png)

#### Test Outputs - step 300

- tolerance window size: 1.0 s
- The following selected test examples show ground truth on the left and model output on the right.
- concurrency=90, so the process time is high
- Unlike the stric test during the training, in the case of vllm, I did not find the degeneration of quality in multi-batch processing

##### ASR

**SYSTEM_PROMPT**: You are a professional transcriptionist. Transcribe what you hear.

---

- UID: JA_A7kJ7PmPk8g_W000017

  | round | ground truth | predict | process time (ms) |
  |---|---|---|---|
  | 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1848 |
  | 2 | `<src>あの特に</src>` | `<src>あの</src>` | 865 |
  | 3 | `<src>これなんかまだ</src>` | `<src>特に</src>` | 1508 |
  | 4 | `<src>一年生ですからね。</src>` | `<src>中まだ1年生からね。</src>` | 545 |
  | 5 | `<src>この時点で</src>` | `<src>はい、はい。</src>` | 907 |
  | 6 | `<src>こう短く</src>` | `<src>その時点で</src>` | 2451 |
  | 7 | `<src>剪定を</src>` | `<src>こう</src>` | 380 |
  | 8 | `<src><\|wait\|></src>` | `<src>資格を</src>` | 2015 |
  | 9 | `<src>こうタイズしてってあげると</src>` | `<src>とりあえず</src>` | 2086 |
  | 10 | `<src>十年経っても</src>` | `<src>資格を</src>` | 762 |
  | 11 | `<src>大した。</src>` | `<src>持っても</src>` | 2292 |

---

- UID: ZH_B00041_S00155_W000028

  | round | ground truth | predict | process time (ms) |
  |---|---|---|---|
  | 1 | `<src><\|wait\|></src>` | `<src>家长需要</src>` | 2310 |
  | 2 | `<src>家长需要做的是，</src>` | `<src>做的是</src>` | 922 |
  | 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 1455 |
  | 4 | `<src>用我们深深的</src>` | `<src>身上的爱胶水</src>` | 1235 |
  | 5 | `<src>爱浇水、</src>` | `<src>是</src>` | 531 |
  | 6 | `<src>施肥，</src>` | `<src>是</src>` | 2257 |
  | 7 | `<src>给足</src>` | `<src>给儿子</src>` | 506 |
  | 8 | `<src>孩子心理营养，</src>` | `<src>心里影响</src>` | 1780 |
  | 9 | `<src><\|wait\|></src>` | `<src>给内心的</src>` | 2300 |
  | 10 | `<src>并耐心等待孩子</src>` | `<src>孩子慢慢</src>` | 627 |
  | 11 | `<src>慢慢长大。</src>` | `<src>长大</src>` | 2578 |

---

- UID: KO_Djg2xNdyFCU_W000010

  | round | ground truth | predict | process time (ms) |
  |---|---|---|---|
  | 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1994 |
  | 2 | `<src>아이 엠 애플 을 </src>` | `<src>Apple </src>` | 850 |
  | 3 | `<src>촉발 시키고 </src>` | `<src>fruit </src>` | 1539 |
  | 4 | `<src><\|wait\|></src>` | `<src>pick and </src>` | 1256 |
  | 5 | `<src>자신 의 </src>` | `<src>eat </src>` | 651 |
  | 6 | `<src><\|wait\|></src>` | `<src>your own </src>` | 2167 |
  | 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>jogging </src>` | 944 |
  | 8 | `<src><\|wait\|></src>` | `<src>heruna </src>` | 1432 |
  | 9 | `<src>박한상과 </src>` | `<src>pachang </src>` | 2292 |
  | 10 | `<src><\|wait\|></src>` | `<src>and </src>` | 638 |
  | 11 | `<src>같은 세대 들입니다. </src>` | `<src>four generations </src>` | 2745 |

---

- UID: EN_nUuwxonVyYE_W000054

  | round | ground truth | predict | process time (ms) |
  |---|---|---|---|
  | 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1869 |
  | 2 | `<src>doing? </src>` | `<src>saying? </src>` | 907 |
  | 3 | `<src>Drop into </src>` | `<src>Drop pin to your body. </src>` | 1565 |
  | 4 | `<src>your body. </src>` | `<src>Where does </src>` | 1186 |
  | 5 | `<src>Where does the tension </src>` | `<src>attention start? </src>` | 1165 |
  | 6 | `<src>start? What is it? </src>` | `<src>What is it? Is it a </src>` | 1787 |
  | 7 | `<src>Is it a headache? </src>` | `<src>day? Cuz it's a </src>` | 1320 |
  | 8 | `<src>Is it a tightness in your chest? </src>` | `<src>time in your chest. </src>` | 2285 |
  | 9 | `<src>I ask them what </src>` | `<src>I have a sob. </src>` | 1311 |
  | 10 | `<src><\|wait\|></src>` | `<src>Like which are you using? </src>` | 2634 |
  | 11 | `<src>language are you using? </src>` | `<src>Saying. </src>` | 1337 |

---


> Under edit...