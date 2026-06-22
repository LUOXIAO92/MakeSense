[English](README.md) | [简体中文](README_zh-cn.md) | [日本語](README_ja.md) | 한국어

# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense는 동시 음성 번역 모델을 위한 의미 단위 기반 학습 데이터와 검증 파이프라인을 만드는 연구·데이터 생성 프로젝트입니다. ASR / 전사 작업도 함께 다룹니다.

이 프로젝트는 음성 번역을 점진적인 멀티턴 대화로 다룹니다. 오디오가 조각 단위로 들어오면, 모델은 그 시점에 원문 전사를 내보낼지, 목표 언어 번역을 내보낼지, 아니면 더 많은 문맥을 기다릴지를 학습합니다.

현재 이 저장소는 데이터셋 구축 파이프라인과 학습 데이터 구성 도구를 제공합니다. 핫워드 / 지정 번역어 지원과 추론 백엔드는 향후 추가할 예정입니다.

## 프로젝트 개요

목표: ASR / 전사 기능도 갖춘 옴니 / 멀티모달 모델에 스트리밍 동시 음성 번역 동작을 학습시키는 것.

이 프로젝트는 다음 논문에서 아이디어를 얻었습니다.
- 무제한 입력 창 / 시간 압박 동시 번역: [InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation: [SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

이 프로젝트에서는:
- 의미 단위 감지기, 오디오 인코더, LLM 백본 정렬을 처음부터 학습하지 **않습니다**.
- 모델 아키텍처를 수정하지 **않습니다**. 긴 시간의 스트리밍 번역은 런타임의 슬라이딩 창 문맥 관리로 처리합니다.
- 정답에 가까운 데이터셋과 파이프라인 검증 체계를 만들어, 옴니 모델이 동시 번역 전략을 학습할 수 있게 합니다.

## 요구 사항

### 저장소 받기
```bash
git clone --recursive https://github.com/LUOXIAO92/MakeSense.git
```

### Python 패키지

데이터셋 준비용:
- 데이터셋 준비에는 별도의 Python 환경을 사용하는 것을 권장합니다. `qwen-asr` 는 최신 `transformers` 와 호환되지 않으므로 학습 환경과 분리하는 편이 안전합니다.
- Flash Attention 은 필요에 따라 prebuilt wheel 을 참고하세요: [Flash attention prebuild wheels](https://github.com/mjun0812/flash-attention-prebuild-wheels)
```bash
pip install whisper openai stanza
pip install qwen-asr --force-reinstall
pip install torch==2.10 torchaudio==2.10.0 torchvision --force-reinstall # --index-url https://download.pytorch.org/whl/cu130
```

학습용:
- 학습 환경은 Python 3.13 을 사용해도 됩니다.
```bash
pip install stanza jieba nagisa transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard
pip install git+https://github.com/LUOXIAO92/MultimodalAssistantMask.git
```

### 서브모듈 의존성
- 단어 정렬 도구: [TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- 단어 정렬의 기본 베이스 모델로 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) 를 사용합니다.
- 멀티모달 입력에서 어시스턴트 부분에만 손실을 적용하기 위해 [MultimodalAssistantMask](https://github.com/LUOXIAO92/MultimodalAssistantMask.git) 를 사용합니다.

## 파이프라인

### 원언어 / 전사 측
1. 메타데이터에서 캐시 레코드 초기화
2. 필요 시 ASR 전사
3. 강제 정렬
4. 시간 압박 원언어 의미 단위 분할

### 목표 언어 / 번역 측
1. 원시 번역 생성
2. 번역 재구성
3. 텍스트 기반 목표 언어 의미 단위 분할
4. 목표 중심 원문 매핑
5. 최종 데이터셋 수집·내보내기

### 시간 흔들림과 정렬 단어 묶음

강제 정렬 모델은 발화 끝부분에서 시간이 조금 뒤로 밀린 값을 낼 수 있습니다. 그래서 마지막 몇 개의 정렬 토큰 종료 시간이 실제 오디오 길이를 넘는 경우가 있습니다.

MakeSense 는 이런 경우를 치명적인 정렬 오류가 아니라 예상 가능한 끝부분 시간 흔들림으로 봅니다. 스트리밍 출력 창은 실제 오디오 길이와 설정된 창 크기로 정해집니다. 끝부분 토큰이 실제 길이를 조금 넘더라도, 아래 단계에서는 그 토큰들을 마지막 출력 창에 포함합니다. 이 이유만으로 새 창을 만들거나 전체 레코드를 거부하지는 않습니다.

다만 이 허용이 강제 정렬 출력 내부의 시간 인과성 검사를 없애는 것은 아닙니다. 이웃한 원래 시간 토큰은 단조로워야 합니다. 즉 앞 토큰의 종료 시간이 다음 토큰의 시작 시간보다 늦으면 안 됩니다. 기본 설정에서는 이 순서가 깨진 레코드를 거부합니다. Pipeline 4 에는 작은 경계 흔들림을 고치는 선택적 수정 스위치가 있으며, 기본값은 꺼져 있습니다. 이 스위치를 켜면 `next.start < prev.end < next.end` 인 고칠 수 있는 겹침은 `next.start = prev.end` 로 수정합니다. `prev.end == next.start == next.end` 처럼 맞닿은 0 길이 다음 토큰은 허용합니다. 반대로 수정 후 다음 토큰이 0 길이 또는 음수 길이가 되는 겹침(`prev.end >= next.end` 이고 `prev.end > next.start`)은 해당 레코드의 검증 실패로 거부하며, 다른 레코드 처리는 계속할 수 있습니다.

학습 데이터를 만들 때 오디오 길이가 `window_count × window_size` 보다 짧으면, 오디오 입력을 해당 창 길이까지 채웁니다. 이렇게 하면 대화 차례, 출력 창, 오디오 조각의 대응을 유지하면서 실제 오디오 길이에 따른 창 경계 의미를 보존할 수 있습니다.

Pipeline 4 는 강제 정렬 모델이 낸 시간 토큰을 `alignment.tokens` 에 저장합니다. 또한 토크나이저가 이 토큰들을 단어로 합친 묶음을 `alignment.words` 에 저장합니다. 뒤 단계는 이 단어를 사용합니다. Pipeline 8 의 `source_token_ids` 도 원래 시간 토큰 번호가 아니라 이 단어 번호를 가리킵니다.

이 묶음이 필요한 이유는 Qwen3-ForcedAligner 가 내는 토큰의 세밀함과 뒤 단계에서 쓰는 단어의 세밀함이 항상 같지 않기 때문입니다. Qwen3-ForcedAligner 에서 중국어와 한국어는 매우 잘게, 사실상 문자 단위에 가까운 시간 토큰으로 처리됩니다. 그래서 토크나이저가 여러 문자나 잘게 쪼개진 토큰을 중국어 단어 또는 한국어의 공백 / 어절 기준 단어로 합칩니다. 일본어는 조금 다릅니다. Qwen3-ForcedAligner 는 일본어 시간 토큰을 `nagisa` 토크나이저로 만들지만, MakeSense 가 `alignment.words` 를 만들 때는 프로젝트에 설정된 다른 토크나이저를 사용할 수 있습니다. 그래서 일본어도 토크나이저 경계 차이 때문에 여러 시간 토큰이 하나의 단어로 합쳐질 수 있습니다.

이 경우 MakeSense 는 일부러 보수적인 시간 처리를 사용합니다. 스트리밍 동시통역은 엄격한 시간 인과관계가 필요하므로, 하나의 시간 토큰을 잘라 여러 단어에 인위적인 더 작은 시간을 배정하지 않습니다. 대신 여러 시간 토큰이 하나의 단어로 묶이면, 그 단어는 첫 토큰의 시작 시간과 마지막 토큰의 종료 시간을 사용합니다. 이렇게 해서 불확실한 인공 시간 경계를 만들지 않고, 스트리밍 출력의 인과관계를 깨지 않도록 합니다.

## 사용법: 전체 데이터셋 파이프라인 실행

현재 워크플로는 `examples/` 아래의 단계별 스크립트로 실행합니다. 각 단계는 이전 단계 캐시를 읽고 새 단계 캐시를 기록하며, 기존 JSONL 캐시에서 이어서 실행할 수 있습니다.

실행하기 전에 **각 예시 스크립트 상단의 설정 블록**을 확인하세요. 자주 쓰는 항목에는 데이터셋 / 캐시 경로, 모델 이름, 대상 언어, `TOP_P`, 제공자별 `EXTRA_BODY`, 그리고 필요한 경우 `ENABLE_VISUALIZATION` 등이 있습니다.

`EXTRA_BODY` 는 OpenAI 호환 채팅 완성 요청에 그대로 전달되는 제공자 전용 확장 파라미터입니다. `top_k` 와 사고 / 추론 제어는 제공자마다 형식이 다를 수 있으므로, 아래에는 대표적인 제공자별 설정 예시를 정리했습니다.

```python
# vLLM / local OpenAI-compatible API 예시:
EXTRA_BODY = {"top_k": 20, "chat_template_kwargs": {"enable_thinking": False}}

# OpenRouter reasoning 예시:
EXTRA_BODY = {"reasoning": {"effort": "none"}}

# DeepSeek thinking 예시:
EXTRA_BODY = {"thinking": {"type": "disabled"}}
```

참고 문서:
- OpenRouter reasoning tokens: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens
- DeepSeek thinking mode: https://api-docs.deepseek.com/guides/thinking_mode

### 현재 제공되는 기능

현재 사용 가능:
- 최종 9단계 JSONL 내보내기까지 실행 가능한 데이터셋 구축 파이프라인.
- `src/data_loader` 를 통한 최종 데이터셋 학습 샘플 구성.
- `examples/train_lora.py` 와 `src/train` 기반의 초기 실제 오디오 LoRA 학습 시작점.
- **NEW**: [MakeSense-Emilia-Dataset](https://huggingface.co/datasets/luoxiao9231/MakeSense-Emilia-Dataset), 라이선스: cc-by-nc-4.0
  - 이 데이터셋에는 8,000개의 오디오 / 전사 레코드와, 번역 전략 학습을 위한 멀티턴 대화 궤적 레코드 24,000개가 포함됩니다.
  - [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) 을 2차 가공해 만든 데이터셋입니다. 훌륭한 다국어 오디오 데이터를 공개해 준 Emilia-Dataset 프로젝트에 감사드립니다.

할 일:
- [x] **높은 우선순위**: 아주 작은 샘플로 `examples/train_lora.py` 를 실행해 대화 템플릿, 어시스턴트 부분만의 손실, 1〜2단계 학습이 제대로 동작하는지 확인한다.
- [x] **높은 우선순위**: `google/gemma-4-E2B-it` 의 LoRA 학습을 끝까지 실행한다.
  - **완료**: 초기 `gemma-4-E2B-it` 대규모 학습과 평가가 완료되었습니다. [LoRA 는 여기에 있습니다](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000). 자세한 데이터는 아래 결과의 지표 섹션을 참고하십시오.
  - **진행 중**: 더 나은 하이퍼파라미터를 찾고 있으며, VRAM 사용량도 계속 최적화하고 있습니다.
- [ ] **두 번째 우선순위:** 학습된 스트리밍 모델을 실행하기 위한 추론 백엔드 를 추가한다.
  - **진행 중**: 추론 쪽 구현은 [MakeSense-Inference](https://github.com/LUOXIAO92/MakeSense-Inference.git) 에서 진행하고 있습니다.
- [ ] 학습 / 추론 문맥에 핫워드와 지정 번역어 지원을 추가한다.

### LoRA 학습 시작점

기본 LoRA 학습 예시는 `google/gemma-4-E2B-it` 를 대상으로 합니다. Transformers 멀티모달 모델에 PEFT LoRA 를 붙이고, 실제 오디오 조각을 학습에 사용합니다. 학습 중 지표는 프로젝트가 관리하는 TensorBoard 스칼라 로그에 기록하며, 엄격한 스트리밍 테스트 지표도 함께 출력합니다.

데이터셋, 모델, LoRA, 체크포인트, 모니터링 관련 옵션은 아래 스크립트 상단에서 설정합니다.

```text
examples/train_lora.py
```

주요 설정 항목:
- `OUTPUT_DIR`
- `CONTINUE_TYPE`: `none`, `resume`, `branch`
- `CHECKPOINT_PATH`
- `SAVE_PROCESSOR`
- `TEST_STEPS`, `TEST_MAX_NEW_TOKENS`, `TEST_RECORD_COUNT`

학습 실행:

```bash
PYTHONPATH=src python examples/train_lora.py
```

LoRA 어댑터, 체크포인트, 모니터링 파일은 설정된 `OUTPUT_DIR` 아래에 기록됩니다.

```text
outputs/makesense_lora/
├── adapter_config.json
├── adapter_model.safetensors
├── checkpoint-*/
├── runs/
│   └── <yyyy-mm-dd_hh-mm-ss>/
└── test_metrics.json
```

엄격한 스트리밍 테스트에서는 각 어시스턴트 턴을 생성할 때 그 시점까지 도착한 오디오 조각만 모델에 전달합니다. 평가에 사용할 레코드 수는 `examples/train_lora.py` 의 `TEST_RECORD_COUNT` 로 정합니다. `0` 이면 평가를 건너뛰고, `-1` 이면 테스트 분할 전체를 사용하며, 양수이면 그 개수까지만 평가합니다.

### 커스터마이징
파이프라인 수준의 비학습 설정을 조정하려면 `src/configs/config.py` 와 `src/configs/LANGUAGE_PACK_*.py` 를 참고하세요. 주로 데이터 샘플링 범위, 지원 언어, ASR / 강제 정렬 모델, 토크나이저, 대기 토큰, 스트리밍 창 크기, 최대 조각 크기, 재구성 검증기에서 사용하는 고잡음 토큰, 언어별 언어팩 / 소수 예시 등을 설정할 수 있습니다.

### 파이프라인 실행 순서

각 단계는 아래 순서로 실행합니다.

```bash
export PYTHONPATH=src

# 1. 필요한 경우 데이터셋 원본을 다운로드 / 준비합니다. (여기서는 Emilia dataset 을 사용합니다. https://huggingface.co/datasets/amphion/Emilia-Dataset 참고)
python examples/pipeline_1_download_Emilia.py

# 2. 데이터셋 메타데이터에서 PipelineRecord 캐시 샤드를 초기화합니다.
python examples/pipeline_2_initialize_cache.py

# 3a-1. 권장 ASR 경로.
# 원문 쪽 전사 결과를 캐시에 채웁니다.
python examples/pipeline_3_a1_asr.py

# 3a-2. 권장 ASR 기반 원시 번역 생성 경로.
# 실제 테스트에서는 중국어·일본어·한국어 모두에서 ASR 뒤에 옴니 모델 / 오디오 보조 번역으로 보정하는 방식이 직접 옴니 ASR보다 정확도와 안정성이 더 높습니다.
python examples/pipeline_3_a2_asr_text_translation.py

# 3b. 선택 사항: 직접 옴니 ASR + 번역 경로.
# 한 번에 수행하는 멀티모달 번역 동작을 확인할 때 사용합니다.
python examples/pipeline_3_b_asr_translation_omni.py

# 4. 원문 전사에 대한 강제 정렬.
python examples/pipeline_4_forced_alignment.py

# 5. 시간 압박 원문 의미 단위 분할.
python examples/pipeline_5_asr_segmentation.py

# 6. 번역 재구성.
python examples/pipeline_6_translation_reconstruction.py

# 7. 텍스트 기반 번역문 의미 단위 분할.
python examples/pipeline_7_pure_text_segmentation.py

# 8. 목표 언어 의미 단위를 원문 토큰 ID에 잇는 목표 중심 매핑.
python examples/pipeline_8_target_centric_mapping.py

# 9. 완료된 8단계 캐시에서 최종 데이터셋을 수집 / 내보냅니다.
python examples/pipeline_9_collect_dataset.py
```

권장 순서:

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

### 최종 데이터셋 출력

9단계는 최종 데이터셋을 다음 구조로 내보냅니다.

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

`dimensional_analysis/` 는 번역 단계에서 생성된 전체 발화 단위의 `target.shared.translation_analysis` 를 독립적으로 내보내는 영역입니다. 전사 / 번역 데이터셋 구조와는 분리되어 저장됩니다.

## 출력 형식

### 스트리밍 모델 출력

```text
<src>(transcription text)</src><tgt>(target translation text)</tgt>
```

원언어 전사나 목표 언어 번역을 안정적으로 내보내기에 정보가 부족하면, 모델은 `<|wait|>` 를 출력할 수 있습니다.

### 대화 형식

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

## 추론 프레임워크 메모: 동시 멀티모달 생성에서의 제약 디코딩

아래 대규모 검증 결과는 `batch=1` 실테스트 결과입니다. 한 샘플씩 실제 rollout 을 수행하고, 매 턴에서 생성된 모델 출력을 다음 prompt 에 다시 넣어 평가합니다. 따라서 이 결과는 동시 생성이나 배치 생성의 영향을 제외한 상태에서 모델이 프로토콜을 얼마나 지키는지를 보여 줍니다. 이는 현재 대규모 학습 단계의 검증 기록이며, 하이퍼파라미터가 이미 최적이라는 뜻은 아닙니다.

동시 생성이나 배치 생성이 존재하는 한 추가 위험이 있습니다. 같은 요청이라도 단독으로 실행할 때와 batch 안에서 실행할 때 다음 token 후보 점수가 완전히 같지 않을 수 있습니다. 후보 점수가 가까우면 첫 번째 또는 두 번째 선호 token 의 순서가 바뀔 수 있습니다. 이런 변화는 sampling 에 영향을 주고, 프로토콜 형식의 출력이 허용된 형태를 벗어나게 만들 수도 있습니다. 이번 다중 배치 vs 단일 배치 조사에서는 이 위험이 비교 모델과 순수 텍스트 기준선보다 Gemma4 음성-텍스트 입력에서 더 두드러졌습니다.

이 프로젝트의 추론 backend 를 만들 때는 vLLM guided decoding / structured outputs 또는 llama.cpp GBNF grammar 같은 제약 디코딩을 사용해, 출력을 현재 지원하는 여섯 가지 프로토콜 형식 안으로 제한할 것입니다. 자세한 내용은 [Gemma 4 multimodal batch-rank note](lessons/gemma4_multimodal_batch_rank_en.md) 를 참고하십시오.

## 대규모 검증 결과 (`google/gemma-4-E2B-it`, `train_examples: 21540`):

### 학습 파라미터

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

### 결과

#### 지표

아래 엄격한 스트리밍 테스트 지표들은 스트리밍 대화에서 모델의 프로토콜 준수와 출력 여부 판단을 확인합니다. 출력이 완전한 프로토콜 단위(ASR-only `<src>...</src>` 또는 번역 `<src>...</src><tgt>...</tgt>`)인지, 각 어시스턴트 턴에서 원문 쪽 / 번역문 쪽이 기다려야 하는지 내용을 내보내야 하는지를 평가합니다. ASR 텍스트의 글자 단위 정확도와 번역 의미 품질은 측정하지 않습니다.

**PROTOCOL_ADHERENCE_RATE**

- 의미: 모델 출력이 프로토콜을 완전히 준수한 턴의 비율입니다.
- 계산: `protocol_adherent_turns / TURN_COUNT`.
- 허용되는 출력은 완전한 `<src>...</src>` 또는 `<src>...</src><tgt>...</tgt>` 뿐입니다.
- `<src>` / `<tgt>` 내부에 프로토콜 tag 를 중첩할 수 없습니다.
- 닫힌 프로토콜 단위 바깥에는 공백이 아닌 내용을 둘 수 없습니다.
- 필드가 `<|wait|>` 를 포함하면, 앞뒤 공백을 제거한 필드 내용이 정확히 `<|wait|>` 와 같아야 합니다.
- 꼬리 텍스트, 쉼표 연결, 반복 프로토콜 블록, 순서 오류 / 빠진 tag, wait 와 다른 문자의 혼합은 모두 프로토콜 미준수로 셉니다.

모든 source / target wait/release accuracy 지표는 protocol-adherent 모델 턴만 분모의 기반으로 사용합니다. 프로토콜 미준수 모델 턴은 `PROTOCOL_ADHERENCE_RATE` 에만 영향을 줍니다. Fixed-window 와 conservative target 지표에는 record-level window eligibility filter 도 적용합니다.

**RECORD_COUNT**

- 의미: 이번 엄격한 스트리밍 테스트에서 실제로 평가한 테스트 레코드 수입니다.
- 계산: `len(records)`.

**SRC_RELEASE_ACCURACY**

- 의미: 정답에서 원문 쪽이 전사 텍스트를 내보내야 하는 턴 중, 모델도 원문 쪽에서 내용을 내보낸 비율입니다.
- 계산: `src_release_correct / SRC_RELEASE_TOTAL`. 여기서는 `<src>...</src>`가 대기 표시가 아닌지만 확인하며, 실제로 나온 전사 텍스트가 맞는지는 평가하지 않습니다.

**SRC_RELEASE_TOTAL**

- 의미: 정답에서 원문 쪽이 내용을 내보내야 하는 턴 수입니다.
- 계산: 정답의 `<src>...</src>`가 `<|wait|>`가 아닌 턴을 셉니다.

**SRC_WAIT_ACCURACY**

- 의미: 정답에서 원문 쪽이 기다려야 하는 턴 중, 모델도 원문 쪽에서 대기 표시를 낸 비율입니다.
- 계산: `src_wait_correct / SRC_WAIT_TOTAL`. 모델의 `<src>...</src>`가 `<|wait|>`인지 여부만 확인합니다.

**SRC_WAIT_TOTAL**

- 의미: 정답에서 원문 쪽이 기다려야 하는 턴 수입니다.
- 계산: 정답의 `<src>...</src>`가 앞뒤 공백을 제거한 뒤 정확히 `<|wait|>`인 턴을 셉니다.

**TGT_RELEASE_ACCURACY**

- 의미: 정답에서 번역문 쪽이 번역을 내보내야 하는 턴 중, 모델도 번역문 쪽에서 내용을 내보낸 비율입니다.
- 계산: `tgt_release_correct / TGT_RELEASE_TOTAL`. 여기서는 `<tgt>...</tgt>`가 대기 표시가 아닌지만 확인하며, 실제 번역의 의미적 정확성은 평가하지 않습니다.

**TGT_RELEASE_TOTAL**

- 의미: 정답에서 번역문 쪽이 번역을 내보내야 하는 턴 수입니다.
- 계산: 정답의 `<tgt>...</tgt>`가 `<|wait|>`가 아닌 턴을 셉니다.

**TGT_WAIT_ACCURACY**

- 의미: 정답에서 번역문 쪽이 기다려야 하는 턴 중, 모델도 번역문 쪽에서 대기 표시를 낸 비율입니다.
- 계산: `tgt_wait_correct / TGT_WAIT_TOTAL`. 모델의 `<tgt>...</tgt>`가 `<|wait|>`인지 여부만 확인합니다.

**TGT_WAIT_TOTAL**

- 의미: 정답에서 번역문 쪽이 기다려야 하는 턴 수입니다.
- 계산: 정답의 `<tgt>...</tgt>`가 앞뒤 공백을 제거한 뒤 정확히 `<|wait|>`인 턴을 셉니다.

**TURN_COUNT**

- 의미: 선택된 모든 테스트 레코드에서 실제로 평가한 어시스턴트 턴의 총수입니다.
- 계산: `records` 안에서 생성 및 평가 대상이 된 어시스턴트 출력을 모두 합산합니다.

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
