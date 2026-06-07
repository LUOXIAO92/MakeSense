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
- 의미 단위 감지기, 오디오 인코더, LLM 백본 정렬 를 처음부터 학습하지 **않습니다**.
- 모델 아키텍처를 수정하지 **않습니다**. 긴 시간의 스트리밍 번역은 런타임의 슬라이딩 창 문맥 관리 로 처리합니다.
- 정답에 가까운 데이터셋과 파이프라인 검증 체계를 만들어 옴니 모델 이 동시 번역 전략을 학습할 수 있게 합니다.

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
- 기본 베이스 모델은 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) 입니다.
- 멀티모달 입력의 어시스턴트 부분만의 손실 구성에는 [MultimodalAssistantMask](https://github.com/LUOXIAO92/MultimodalAssistantMask.git) 를 사용합니다.

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

할 일:
- [x] **높은 우선순위**: 아주 작은 샘플로 `examples/train_lora.py` 를 실행해 대화 템플릿, 어시스턴트 부분만의 손실, 1〜2단계 학습이 제대로 동작하는지 확인한다.
- [ ] **높은 우선순위**: `google/gemma-4-E2B-it` 의 LoRA 학습을 끝까지 실행한다.
  - **진행 중**: 지금은 더 큰 규모의 학습 데이터를 준비하고 있습니다. 공개 예정인 데이터셋에는 약 8,000개의 오디오·전사 샘플과, 번역 전략 학습에 쓰일 멀티턴 대화 궤적 데이터 약 24,000개가 포함됩니다. 이 데이터는 [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) 을 바탕으로 2차 가공한 것입니다. 좋은 다국어 오디오 데이터를 공개해 준 Emilia-Dataset 프로젝트에 감사드립니다.
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

## 소규모 검증 결과 (`google/gemma-4-E2B-it`, `train_examples: 96`):

### 학습 파라미터

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

### 결과

#### 지표

아래 엄격한 스트리밍 테스트 지표들은 주로 스트리밍 대화에서 모델의 출력 형식과 출력 여부 판단을 확인하기 위한 것입니다. 출력이 `<src>...</src><tgt>...</tgt>` 프로토콜을 지키는지, 생성이 의도한 정지 토큰에서 멈추는지, 각 어시스턴트 턴에서 원문 쪽 / 번역문 쪽이 기다려야 하는지 아니면 내용을 내보내야 하는지를 평가합니다. ASR 텍스트가 글자 단위로 맞는지, 번역 의미가 정확한지를 직접 측정하는 지표는 아닙니다.

**POSTPROCESSED_TURN_STOP_RATE**

- 의미: 후처리된 출력이 불필요한 꼬리 문자열 없이 완전한 프로토콜 출력으로 남아 있는 비율입니다.
- 계산: `postprocessed_turn_stop_turns / TURN_COUNT`. 후처리된 텍스트가 프로토콜상 유효하고, 정규화된 `<src>...</src><tgt>...</tgt>` 출력과 정확히 일치하면 해당 턴을 성공으로 셉니다.

**PROTOCOL_VALID_RATE**

- 의미: 모델 출력이 요구된 프로토콜을 지킨 비율입니다.
- 계산: `protocol_valid_turns / TURN_COUNT`. 출력은 `<src>...</src><tgt>...</tgt>` 형식과 일치해야 하며, 원문 쪽 / 번역문 쪽 내용 안에 `<src>`, `</src>`, `<tgt>`, `</tgt>` 같은 태그가 다시 중첩되어 있으면 안 됩니다.

**RAW_TURN_STOP_RATE**

- 의미: 원시 디코드 결과가 설정된 생성 정지 토큰에서 정상적으로 멈춘 비율입니다.
- 계산: `raw_turn_stop_turns / TURN_COUNT`. 원시 출력에서 후처리 출력 뒤에 바로 `generation_stop`이 이어지면 해당 턴은 정상적으로 멈춘 것으로 봅니다.

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

#### 50단계 테스트 출력

- 허용 창 크기: 1.0초
- 아래는 소규모 테스트 결과입니다. 왼쪽은 정답, 오른쪽은 모델 출력입니다.

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


#### 240단계 최종 테스트 출력

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