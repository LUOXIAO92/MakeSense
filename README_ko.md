# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense는 동시 음성 번역 모델을 위해 의미 단위를 인식하는 학습 데이터와 검증 플로를 구축하는 연구 및 데이터 생성용 프로젝트입니다. ASR / 음성 전사 기능도 함께 지원합니다.

이 프로젝트의 목표는 음성 번역을 점진적인 멀티턴 대화 과제로 재구성하는 것입니다. 오디오는 여러 구간으로 나뉘어 순차적으로 입력되며, 모델은 각 시점마다 원문의 전사를 출력할지, 목표 언어 번역을 출력할지, 아니면 정보가 아직 부족하므로 더 기다릴지를 학습합니다.

현재 이 저장소는 주로 데이터셋 구축 pipeline 과 학습 데이터 생성 도구를 제공합니다. 핫워드 / 선호 번역어 지원 및 추론 백엔드는 향후 개발 항목입니다.

## 프로젝트 개요

목표: 스트리밍 동시 음성 번역 능력을 갖추고, 추가로 ASR / 음성 전사까지 지원하는 옴니모달 / 멀티모달 모델을 학습하는 것.

본 프로젝트는 다음 연구에서 영감을 받았습니다.

* 무제한 입력 window / time-pressure 기반 동시 번역: [InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
* sense-unit translation: [SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

본 프로젝트에서는 다음과 같은 방침을 따릅니다.

* 의미 단위 탐지기, 오디오 인코더, 또는 LLM backbone 의 alignment 모듈을 처음부터 학습하지 않습니다.
* 모델 아키텍처를 변경하지 않습니다. 무제한 길이의 스트리밍 번역은 실행 시점의 슬라이딩 윈도우 기반 컨텍스트 관리로 처리합니다.
* 대신 ground truth 에 가까운 형태의 데이터셋을 구축하고, pipeline 검증을 위한 인터페이스와 중간 결과를 제공합니다. 이를 통해 옴니모달 모델이 동시 번역 전략을 학습할 수 있도록 합니다.

## 환경 요구 사항

### Python 의존 패키지

```bash
pip install stanza jieba nagisa qwen-asr transformers peft torch torchvision torchaudio unsloth
```

### 서브모듈 의존성

* 단어 alignment 도구: [TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
* 기본 베이스 모델로는 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) 를 사용합니다.

## Pipeline

### 원언어 / 전사 측

1. metadata 를 기반으로 cache records 를 초기화합니다.
2. 필요에 따라 ASR 전사를 수행합니다.
3. forced alignment 를 실행합니다.
4. time pressure 를 기준으로 원언어 의미 단위를 분할합니다.

### 목표 언어 / 번역 측

1. 초기 번역을 생성합니다.
2. 번역을 재구성합니다.
3. 목표 언어의 일반 텍스트를 의미 단위로 분할합니다.
4. 목표 언어를 중심으로 원언어 구간을 매핑합니다.
5. 최종 데이터셋을 수집하고 내보냅니다.

## 사용 방법: 전체 데이터셋 pipeline 실행

현재 워크플로는 `examples/` 디렉터리에 있는 단계별 스크립트를 통해 실행됩니다. 각 단계는 이전 단계의 cache 를 읽고, 새로운 단계의 cache 를 기록합니다. 또한 기존 JSONL cache 상태를 기반으로 중단된 지점부터 이어서 실행할 수 있습니다.

실행하기 전에 반드시 **각 example 스크립트 상단의 설정 블록**을 확인하세요. 자주 사용하는 설정에는 데이터셋 / cache 루트 디렉터리, 모델 이름, 목표 언어, `ENABLE_THINKING`, `TOP_P`, `TOP_K`, 그리고 필요한 경우 `ENABLE_VISUALIZATION` 등이 포함됩니다.

### 현재 사용 가능한 기능

현재 제공되는 기능은 다음과 같습니다.

* 최종 pipeline-9 JSONL 내보내기까지 실행 가능한 데이터셋 구축 pipeline
* `src/data_loader` 를 통해 최종 데이터셋에서 학습 샘플 생성
* `examples/train_lora.py` 와 `src/train` 을 통한 경량 LoRA SFT 학습 진입점
  현재는 텍스트 dry-run 시나리오만 지원하며, 이때 `<|audio|>` 는 실제 오디오가 아니라 텍스트 placeholder 로 취급됩니다.

향후 작업:

* [ ] **높은 우선순위:** 아주 작은 샘플에서 `examples/train_lora.py` 의 경량 LoRA 학습 경로를 테스트하고, conversation 렌더링, assistant-only loss 설정, 1〜2 step 학습이 정상적으로 동작하는지 확인합니다.
* [ ] **높은 우선순위:** 학습기의 sanity check 가 끝난 뒤 `Qwen/Qwen2.5-Omni-3B` 에 대해 LoRA 학습을 실행합니다.
* [ ] **중간 우선순위:** 학습된 스트리밍 모델을 실행하기 위한 추론 백엔드를 추가합니다.
* [ ] 학습 및 추론 컨텍스트에 핫워드와 선호 번역어 지원을 추가합니다.

### LoRA 학습 진입점

LoRA 학습은 다음 명령으로 실행할 수 있습니다.

```bash
PYTHONPATH=src python examples/train_lora.py
```

### Pipeline 실행 순서

각 단계는 아래 순서대로 실행하세요.

```bash
export PYTHONPATH=src 

# 1. 필요한 경우 데이터셋 원본 데이터를 다운로드 / 준비합니다.
#    여기서는 Emilia 데이터셋을 사용합니다. 자세한 내용은 https://huggingface.co/datasets/amphion/Emilia-Dataset 를 참고하세요.
python examples/pipeline_1_download_Emilia.py

# 2. 데이터셋 metadata 를 기반으로 PipelineRecord cache shards 를 초기화합니다.
python examples/pipeline_2_initialize_cache.py

# 3a. 선택 사항: omni ASR + translation 경로.
#     일회성 멀티모달 번역 동작을 테스트할 때 사용합니다.
python examples/pipeline_3_a_asr_translation_omni.py

# 3b-1. ASR 전용 경로.
#       이 단계에서는 cache 에 원언어 전사 결과를 기록합니다.
python examples/pipeline_3_b1_asr.py

# 3b-2. ASR cache 를 기반으로 초기 번역을 생성합니다.
#       기본값은 텍스트 전용 모드입니다. 오디오 보조 모드는 스크립트 내부 설정으로 제어합니다.
python examples/pipeline_3_b2_asr_text_translation.py

# 4. 원언어 전사 결과에 대해 forced alignment 를 실행합니다.
python examples/pipeline_4_forced_alignment.py

# 5. time pressure 를 기준으로 원언어 의미 단위를 분할합니다.
python examples/pipeline_5_asr_segmentation.py

# 6. 번역을 재구성합니다.
python examples/pipeline_6_translation_reconstruction.py

# 7. 목표 언어 일반 텍스트를 의미 단위로 분할합니다.
python examples/pipeline_7_pure_text_segmentation.py

# 8. 목표 언어 의미 단위를 원언어 token ids 에 매핑합니다.
python examples/pipeline_8_target_centric_mapping.py

# 9. 완료된 pipeline-8 cache 상태에서 최종 데이터셋을 수집하고 내보냅니다.
python examples/pipeline_9_collect_dataset.py
```

권장 실행 순서는 다음과 같습니다.

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

### 최종 데이터셋 출력

Pipeline 9 는 최종 데이터셋을 아래와 같은 디렉터리 구조로 내보냅니다.

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

## 출력 형식

### 스트리밍 모델 출력

```text
<src>(전사 텍스트)</src><tgt>(목표 언어 번역 텍스트)</tgt>
```

원언어 전사나 목표 언어 번역을 안정적으로 생성하기에 정보가 아직 부족한 경우, 모델은 `<|wait|>` 를 출력할 수 있습니다.

### Conversation 형식

```text
system
[system prompts]
[hot words / task context]
user
<|audio|>
assistant
<src>(전사 텍스트 또는 <|wait|>)</src><tgt>(목표 언어 번역 텍스트 또는 <|wait|>)</tgt>
user
<|audio|>
assistant
<src>(다음 구간의 전사 텍스트 또는 <|wait|>)</src><tgt>(다음 구간의 목표 언어 번역 또는 <|wait|>)</tgt>
...
```
