# Gemma 4 audio+text batch vs single inference: the next-token choice and candidate list can change

Generated: 2026-06-14

## Summary

This report asks a simple question:

> If the input row is the same, does the model prefer the same next token when that row is run alone versus when it is run inside a batch?

For `google/gemma-4-E2B-it`, the answer is **not always** for audio+text inputs. In a small fully public `draw.mp4` audio test, the first-choice token did not change, but the list of likely next tokens was not identical. In a larger 90-row audio+text test made from three public `amphion/Emilia-Dataset` uid records, Gemma 4 chose a different first token for **5 / 90 rows** when run in a batch instead of alone.

I also ran `Qwen/Qwen2.5-Omni-3B` as a comparison model. On the same 90-row audio+text test, Qwen2.5-Omni had **1 / 90** first-choice difference. That one Qwen difference looked like a tie: the best two candidates were effectively equal, so a tiny change could swap their order.

I then added a public pure-text baseline using the `google/gemma-4-E2B-it` README split into 90 text chunks. This baseline is not meant to cancel the audio+text result. It shows the ordinary background behavior of batched text inference: when the best two token scores are almost tied, very small numerical changes can swap their order. In that setting, first-choice flips are hard to avoid and are not strong evidence by themselves. Gemma 4 had **2 / 90** text-only first-choice differences, and Qwen2.5-Omni had **7 / 90**; many were ties or near ties.

Plain-language conclusion:

- Batch inference and single-row inference are not always identical.
- A first-choice flip is not automatically a strong problem: in pure text, many flips happen when the first and second choices are already almost tied.
- The stronger concern is that, in this sample, Gemma 4 audio+text changed more than its README text-only baseline: more changed first choices, bigger raw score changes, and more movement in the likely-token list.
- This matters for sampling. Even if greedy decoding often picks the same first token, sampling can change when the likely-token list changes.

## Input assets

### Fully self-contained public minimal asset

Source video:

```text
https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-Omni/draw.mp4
```

Audio extraction:

```bash
curl -L --fail --show-error \
  --output /tmp/draw.mp4 \
  https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-Omni/draw.mp4

ffmpeg -y -i /tmp/draw.mp4 -t 4 -vn -ac 1 -ar 16000 /tmp/draw_0_4s.wav
```

For the mixed-duration public-minimal test, I also extracted these public-audio prefixes:

```bash
for d in 0.5 1.0 1.5 2.0 3.0 4.0; do
  ffmpeg -y -v error -i /tmp/draw.mp4 -t "$d" -vn -ac 1 -ar 16000 "/tmp/draw_0_${d}s.wav"
done
```

### Supplemental statistical asset from amphion/Emilia-Dataset

To increase row coverage, I also selected three long records from a local copy derived from the public `amphion/Emilia-Dataset` and split each record into 1-second wav chunks.

Selected uid records:

| uid | language | subset | duration | chunks |
|---|---|---|---:|---:|
| `ZH_P8jFMJ7Cg8Y_W000045` | ZH | `Emilia-YODAS/ZH` | 30.0s | 30 |
| `ZH_P8jFMJ7Cg8Y_W000031` | ZH | `Emilia-YODAS/ZH` | 30.0s | 30 |
| `KO_Go-OHCPzzfy_W000028` | KO | `Emilia-YODAS/KO` | 30.0s | 30 |

Chunking command pattern:

```bash
# For each selected record:
for i in $(seq 0 29); do
  ffmpeg -y -v error \
    -ss "$i" -t 1.0 \
    -i "${uid}.wav" \
    -acodec pcm_s16le -ar 16000 -ac 1 \
    "${uid}_chunk_${i}.wav"
done
```

This produced 90 one-second audio chunks. The report below only identifies the public dataset uid records used; it does not depend on private prompts, a fine-tuned checkpoint, or an application-specific evaluation pipeline.

### Public pure-text control asset

To separate audio+text behavior from ordinary text-only batch-related changes, I also used a public text-only source document:

```text
https://huggingface.co/google/gemma-4-E2B-it/blob/main/README.md
```

The raw markdown was downloaded from:

```text
https://huggingface.co/google/gemma-4-E2B-it/raw/main/README.md
```

I split the raw README markdown into 90 contiguous whitespace-token chunks. In this run the README had 3,666 whitespace-delimited tokens, producing 90 chunks of 40 or 41 tokens each. These chunks were used as 90 independent pure-text rows with no audio input.

## Environment

```text
Python environment: local conda environment
PyTorch: 2.12.0+cu130
CUDA available: True
Transformers: 5.9.0
ffmpeg: 6.1.1
```

Models:

```text
Gemma test model: google/gemma-4-E2B-it
Gemma model class: AutoModelForMultimodalLM
Gemma processor class: AutoProcessor / Gemma4Processor

Control model: Qwen/Qwen2.5-Omni-3B
Qwen model class: Qwen2_5OmniForConditionalGeneration
Qwen processor class: Qwen2_5OmniProcessor
Qwen forward surface used for raw model scores: model.thinker(...)
```

Both models were loaded in `torch.bfloat16` with `attn_implementation="sdpa"` and `device_map="auto"`.

## Test design

For each model, I compared the next-token scores from:

- one batched forward call with native processor padding forced to `padding_side="left"`, and
- separate single-row forward calls for the same rows.

The raw model scores I compared were the model output logits:

```python
outputs.logits[:, -1, :]
```

In plain language, these are the model's scores for "what token should come next?" after the prompt.

The larger Emilia-derived audio+text test used batch size 15, producing 6 batched forward groups for 90 audio chunks. The README pure-text control used the same 90-row / batch-size-15 grouping structure.

## How to read the metrics in plain language

The tables still keep some compact numeric columns for reproducibility, but the important meanings are below. Think of the model as making an ordered list of possible next tokens.

| Metric name in this report | Plain-language meaning | Why it matters |
|---|---|---|
| First choice changed | The token with the highest score changed between single-row inference and batched inference. In other words, the model would start its answer with a different token. | Greedy decoding would choose a different next token for that row, but this is only strong evidence when the best token was not already tied with the runner-up. |
| Same candidates in the likely-token list | Out of the model's N most likely next tokens, how many are the same between single-row and batched inference. For example, 43/50 means 7 of the top 50 candidates were replaced. | Sampling methods choose from a list of likely tokens, not only from the single best token. |
| First-vs-second score gap | How far ahead the best candidate is from the second-best candidate. A gap of 0 means they are tied. | If the gap is tiny, the first-choice change may just be a tie being broken differently. |
| Raw score change | How much the model's internal score for the same token changed between single-row and batched inference. | Larger score changes are more concerning than tiny tie-breaking noise. |
| Candidate order change | A candidate moves up or down in the ordered list of likely next tokens. | The first token may stay the same, but sampling can still change if the order or list changes. |

So the most important distinction is:

- **Tie-like change:** first and second choices were already almost equal, so the winner can swap easily. This is common in the pure-text baseline and is not very surprising by itself.
- **Stronger change:** score changes are larger and/or many candidates enter or leave the likely-token list. This is the main concern for the audio+text case.

## Minimal reproduction skeleton

```python
import torch
from contextlib import contextmanager
from transformers.audio_utils import load_audio
from transformers import AutoProcessor, AutoModelForMultimodalLM

MODEL_ID = "google/gemma-4-E2B-it"
AUDIO_PATHS = [
    "/tmp/example_chunk_00.wav",
    "/tmp/example_chunk_01.wav",
    # ... more one-second chunks ...
]
PROMPTS = [
    "Transcribe the speech in this one-second audio chunk.",
    "Please transcribe only what is spoken in this short audio segment.",
    "Listen carefully and write the spoken words from this one-second clip.",
]

@contextmanager
def left_padding(processor):
    targets = []
    if hasattr(processor, "padding_side"):
        targets.append(processor)
    if hasattr(processor, "tokenizer") and hasattr(processor.tokenizer, "padding_side"):
        targets.append(processor.tokenizer)
    old = [(obj, obj.padding_side) for obj in targets]
    for obj, _ in old:
        obj.padding_side = "left"
    try:
        yield
    finally:
        for obj, value in old:
            obj.padding_side = value

def make_messages(prompt, audio_path):
    return [{
        "role": "user",
        "content": [
            {"type": "audio", "audio": audio_path},
            {"type": "text", "text": prompt},
        ],
    }]

def make_batch(processor, prompts, audio_paths):
    rendered = [
        processor.apply_chat_template(
            make_messages(prompt, audio_path),
            tokenize=False,
            add_generation_prompt=True,
        )
        for prompt, audio_path in zip(prompts, audio_paths)
    ]
    audio = [load_audio(path) for path in audio_paths]
    return processor(text=rendered, audio=audio, return_tensors="pt", padding=True)

def to_device(batch, device):
    return {k: (v.to(device) if torch.is_tensor(v) else v) for k, v in batch.items()}

processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModelForMultimodalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="sdpa",
).eval()
device = next(model.parameters()).device

with left_padding(processor), torch.no_grad():
    batch = make_batch(processor, PROMPTS, AUDIO_PATHS)
    batch_logits = model(**to_device(batch, device), use_cache=False).logits[:, -1, :].float().cpu()

    single_logits = []
    for prompt, audio_path in zip(PROMPTS, AUDIO_PATHS):
        single = make_batch(processor, [prompt], [audio_path])
        logits = model(**to_device(single, device), use_cache=False).logits[:, -1, :]
        single_logits.append(logits[0].float().cpu())
    single_logits = torch.stack(single_logits)

# Compare torch.topk(batch_logits[row], k) with torch.topk(single_logits[row], k).
```

For Qwen2.5-Omni, the analogous comparison used:

```python
from transformers import Qwen2_5OmniForConditionalGeneration, Qwen2_5OmniProcessor

processor = Qwen2_5OmniProcessor.from_pretrained("Qwen/Qwen2.5-Omni-3B", trust_remote_code=True)
model = Qwen2_5OmniForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-Omni-3B",
    dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="sdpa",
).eval()

# The top-level object did not expose a normal forward(input_ids=...) surface in this environment.
# The logits comparison therefore used the thinker module:
outputs = model.thinker(**inputs, use_cache=False)
```

## Results

### Public minimal `draw.mp4` results

| Model | Condition | Rows | Rows where first choice changed | Avg same candidates in top 2 | Avg same candidates in top 5 | Avg same candidates in top 10 | Avg same candidates in top 50 | Worst same-candidates count in top 50 | Largest raw score change | Average raw score change |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemma 4 E2B-it | same 4s audio, mixed text lengths | 6 | 0 | 2.00 | 4.83 | 9.83 | 48.50 | n/a | 1.0000 | 0.1463 |
| Qwen2.5-Omni-3B | same 4s audio, mixed text lengths | 6 | 0 | 2.00 | 4.83 | 9.50 | 48.50 | n/a | 0.5312 | 0.0667 |
| Gemma 4 E2B-it | mixed audio durations + mixed text lengths | 6 | 0 | 2.00 | 4.50 | 9.83 | 48.50 | 47 | 1.3750 | 0.2331 |
| Qwen2.5-Omni-3B | mixed audio durations + mixed text lengths | 6 | 0 | 2.00 | 4.67 | 9.67 | 48.17 | 47 | 0.5312 | 0.0638 |

The small fully self-contained public test did not happen to change the first-choice token, but the list of likely next tokens was not identical. In other words, greedy decoding stayed the same in this tiny test, but sampling could still be affected because the candidate list changed.

### 90-row amphion/Emilia-Dataset-derived chunk results

Audio+text test: 90 one-second chunks from the three uid records listed above, batch size 15.

| Model | Rows | # rows where first choice changed | Rows where first choice changed | Avg same candidates in top 2 | Avg same candidates in top 5 | Avg same candidates in top 10 | Avg same candidates in top 50 | Worst same-candidates count in top 50 | Largest raw score change | Average raw score change | 95th pct largest score change | 95th pct average score change |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemma 4 E2B-it | 90 | 5 | 27, 44, 56, 86, 89 | 1.9222 | 4.7444 | 9.4667 | 47.9333 | 43 | 3.6563 | 0.3649 | 2.3125 | 1.1867 |
| Qwen2.5-Omni-3B | 90 | 1 | 31 | 1.9667 | 4.7333 | 9.7222 | 48.3667 | 43 | 1.2422 | 0.0644 | 0.5625 | 0.1378 |

### Public README pure-text control results

Pure-text control with 90 chunks from the public `google/gemma-4-E2B-it` README, batch size 15:

| Model | Rows | # rows where first choice changed | Rows where first choice changed | Avg same candidates in top 2 | Avg same candidates in top 5 | Avg same candidates in top 10 | Avg same candidates in top 50 | Worst same-candidates count in top 50 | Largest raw score change | Average raw score change | 95th pct largest score change | 95th pct average score change |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemma 4 E2B-it | 90 | 2 | 2, 23 | 1.9667 | 4.8778 | 9.6222 | 48.3778 | 45 | 2.6953 | 0.2022 | 1.3402 | 0.5728 |
| Qwen2.5-Omni-3B | 90 | 7 | 20, 24, 34, 38, 67, 71, 72 | 1.8889 | 4.8556 | 9.7444 | 48.9778 | 47 | 0.3750 | 0.0376 | 0.3125 | 0.0552 |

This text-only control is included as a baseline, not as a replacement for the audio+text result. It shows that pure-text batched inference can also choose a different first token, especially when the first and second choices are already tied or nearly tied. That kind of pure-text flip is expected background noise for this test design, so the important comparison is not just whether any first-choice flip exists. The important comparison is whether audio+text causes larger raw score changes or stronger movement in the likely-token list than the text-only baseline.

Pure-text examples where the first-choice token changed:

| Model | Row | single-row first choice | batched first choice | single-row choice position in batched list | batched choice position in single-row list | single first-vs-second score gap | batched first-vs-second score gap | same candidates in top 2/5/10/50 | largest raw score change | average raw score change |
|---|---:|---|---|---:|---:|---:|---:|---|---:|---:|
| Gemma 4 E2B-it | 2 | `to` | `for` | 2 | 1 | 0.0000 | 0.1250 | 2/5/10/49 | 0.6875 | 0.2231 |
| Gemma 4 E2B-it | 23 | `8` | `MM` | 1 | 1 | 0.0000 | 0.0000 | 2/5/10/50 | 0.3750 | 0.0494 |
| Qwen2.5-Omni-3B | 20 | `\|` | `E` | 1 | 1 | 0.0000 | 0.0000 | 2/5/10/50 | 0.1719 | 0.0276 |
| Qwen2.5-Omni-3B | 24 | `\|` | `The` | 2 | 1 | 0.0000 | 0.0625 | 2/5/10/49 | 0.1758 | 0.0262 |
| Qwen2.5-Omni-3B | 34 | `enable` | <code>```</code> | 1 | 2 | 0.1250 | 0.0000 | 2/5/10/48 | 0.2500 | 0.0378 |
| Qwen2.5-Omni-3B | 38 | `messages` | `*` | 2 | 1 | 0.0000 | 0.0625 | 2/5/9/49 | 0.2500 | 0.0390 |
| Qwen2.5-Omni-3B | 67 | `###` | `G` | 1 | 2 | 0.1250 | 0.0000 | 2/5/10/48 | 0.3125 | 0.0711 |
| Qwen2.5-Omni-3B | 71 | `are` | `The` | 1 | 1 | 0.0000 | 0.0000 | 2/5/10/49 | 0.1875 | 0.0299 |
| Qwen2.5-Omni-3B | 72 | `Certainly` | `###` | 1 | 1 | 0.0000 | 0.0000 | 1/5/10/48 | 0.2109 | 0.0389 |

Per-record audio+text summary:

| Model | uid | Rows | # rows where first choice changed | Rows where first choice changed | Avg same candidates in top 50 | Worst same-candidates count in top 50 | Largest raw score change | Average raw score change |
|---|---|---:|---:|---|---:|---:|---:|---:|
| Gemma 4 E2B-it | `ZH_P8jFMJ7Cg8Y_W000045` | 30 | 1 | 27 | 47.9667 | 45 | 2.3125 | 0.2965 |
| Gemma 4 E2B-it | `ZH_P8jFMJ7Cg8Y_W000031` | 30 | 2 | 44, 56 | 48.0333 | 45 | 2.7500 | 0.3982 |
| Gemma 4 E2B-it | `KO_Go-OHCPzzfy_W000028` | 30 | 2 | 86, 89 | 47.8000 | 43 | 3.6563 | 0.3999 |
| Qwen2.5-Omni-3B | `ZH_P8jFMJ7Cg8Y_W000045` | 30 | 0 | — | 48.4000 | 46 | 0.6563 | 0.0630 |
| Qwen2.5-Omni-3B | `ZH_P8jFMJ7Cg8Y_W000031` | 30 | 1 | 31 | 48.5333 | 47 | 0.5625 | 0.0545 |
| Qwen2.5-Omni-3B | `KO_Go-OHCPzzfy_W000028` | 30 | 0 | — | 48.1667 | 43 | 1.2422 | 0.0758 |

Gemma 4 examples where the first-choice token changed in the 90-row audio+text run:

| Row | uid | chunk | single-row first choice | batched first choice | single-row choice position in batched list | batched choice position in single-row list | same candidates in top 2/5/10/50 | largest raw score change | average raw score change |
|---:|---|---:|---|---|---:|---:|---|---:|---:|
| 27 | `ZH_P8jFMJ7Cg8Y_W000045` | 27 | `<turn\|>` | `I` | 2 | 2 | 2/5/10/47 | 0.6875 | 0.1393 |
| 44 | `ZH_P8jFMJ7Cg8Y_W000031` | 14 | `People` | `心理` | 2 | 3 | 1/4/9/48 | 0.7500 | 0.1092 |
| 56 | `ZH_P8jFMJ7Cg8Y_W000031` | 26 | `I` | `无法` | 2 | 2 | 2/5/9/47 | 2.6250 | 1.1867 |
| 86 | `KO_Go-OHCPzzfy_W000028` | 26 | `네` | `I` | 2 | 2 | 2/5/9/48 | 0.7813 | 0.1591 |
| 89 | `KO_Go-OHCPzzfy_W000028` | 29 | `8` | `팔` | 2 | 2 | 2/5/10/47 | 0.7500 | 0.2766 |

The one Qwen2.5-Omni audio+text first-choice difference in this run looks like a tie-breaking case: in the batched run, the best two candidates were tied (`0.0` score gap), so a different tied or nearly tied token became the first choice.

## Interpretation

The larger 90-row audio+text test changes the conclusion from the small public-minimal test:

- The first-choice token does not change on every input. Small examples may miss it.
- With more rows, Gemma 4 did choose a different first token for 5 / 90 audio+text rows when the row was run in a batch instead of alone.
- The public README pure-text control showed that text-only batching can also change the first token: Gemma 4 had 2 / 90 changed rows, and Qwen2.5-Omni had 7 / 90 changed rows.
- Those pure-text flips are mostly not dramatic by themselves because the first and second choices were tied or nearly tied. In that situation, a tiny numerical change can swap the winner, so this kind of flip is difficult to avoid.
- The README pure-text baseline therefore gives the expected background level for ordinary text batching behavior. It should not be used to claim that every first-choice flip is a serious problem.
- The audio+text concern is stronger when its changes exceed that background: in this sample, Gemma 4 audio+text had more changed first choices (`5 / 90` vs `2 / 90`) and larger average raw score change (`0.3649` vs `0.2022`) than Gemma 4 README text-only.
- Candidate-list changes matter even when the first choice stays the same. For example, in the 90-row audio+text runs, the top-50 list dropped as low as 43/50 matching candidates. That means 7 of the 50 likely next tokens were different between single-row and batched inference.

The practical concern is not exact floating-point equality by itself. The concern is whether batching can change what the model is likely to generate. If the first choice changes, greedy decoding can change. If the broader candidate list changes, sampling can change even when greedy decoding does not.

## Expected behavior / question

For left-padded multimodal audio+text batches where each row has the same prompt/audio content as its single-row counterpart, should the model's next-token preferences be expected to stay the same apart from tiny numerical noise?

If exact score equality is not expected, the pure-text baseline suggests that near-tie first-choice flips are unavoidable background behavior. The more specific question is whether the following are expected/acceptable for Gemma 4 multimodal inference:

- audio+text rows show larger raw score changes than the text-only baseline,
- the likely-token list changes substantially, for example only 43 of the top 50 candidates remain the same,
- the audio+text changes are stronger than the public text-only baseline under the same single-row vs batch comparison.

This is especially relevant for sampling methods that choose from multiple likely tokens, such as temperature, top-k, or top-p sampling. Those methods use more than just the single best token, so changing the likely-token list can change generated output even when greedy decoding happens to stay the same in a small example.

## Notes

- The fully self-contained minimal audio+text reproduction uses only the public Qwen2.5-Omni `draw.mp4` asset and generic transcription prompts.
- The larger statistical audio+text test uses uid records from `amphion/Emilia-Dataset` / `Emilia-YODAS` and reports only those public dataset identifiers.
- The pure-text baseline uses the public `google/gemma-4-E2B-it` README split into 90 contiguous text chunks.
- The tests do not depend on a fine-tuned checkpoint, private prompts, or an application-specific evaluation pipeline.
- The result should not be interpreted as “the first choice always changes.” The behavior depends on the input row and what other rows are in the batch.
- The result does show that batch vs single inference can change both the first-choice token and the broader likely-token list. In the larger Gemma 4 audio+text sample, the first-choice token was not always the same.
