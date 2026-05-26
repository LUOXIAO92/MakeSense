# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense is a research/data-generation project for building sense-aware training data and validation pipelines for simultaneous speech translation models with ASR/transcription support.

The goal is to convert speech translation into an incremental multi-turn conversation task: audio arrives chunk by chunk, and the model learns when to emit source transcription, when to emit target translation, and when to wait for more information.

Currently, the repository provides the dataset builder pipeline and training-data construction utilities. Hot words / hot translations support and an inference backend are planned future work.

## Project brief

Target: train an omni / multimodal model toward streaming simultaneous speech translation behavior with an additional ASR/transcription capability.

Inspired by following papers:
- sense-unit + window/time-pressure ASR: [InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation: [SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

In this project:
- we **do not** train the sense-unit detector, audio encoder, or LLM backbone alignment from scratch;
- we **do not** modify the model architecture; infinite-time streaming translation is handled by sliding-window context management at runtime;
- we **do** create ground-truth-style datasets and pipeline validation surfaces so an omni model can learn simultaneous translation strategy;

## Requirement
### Python packages
```bash
pip install stanza jieba nagisa qwen-asr transformers peft torch torchvision torchaudio unsloth
```

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
- thin LoRA SFT training entry via `examples/train_lora.py` and `src/train`, currently scoped as text-only dry-run where `<|audio|>` is a text placeholder;

TODO:
- [ ] **High priority:** test the thin LoRA trainer path with `examples/train_lora.py` on a tiny sample and confirm the rendered conversation, assistant-only loss setup, and 1-2 training steps behave correctly.
- [ ] **High priority:** run LoRA training for `Qwen/Qwen2.5-Omni-3B` after the trainer sanity check passes.
- [ ] Add hot words and hot translations support for training and inference contexts.
- [ ] Add an inference backend for running the trained streaming model.

### LoRA training entry

The LoRA training entry is:

```bash
PYTHONPATH=src python examples/train_lora.py
```

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

# 3b-1. Optional staged ASR-only path.
# This fills source transcript artifacts in the cache.
python examples/pipeline_3_b1_asr.py

# 3b-2. Staged raw translation from the ASR cache.
# Default is text-only; optional audio-assisted mode is controlled in the script.
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
