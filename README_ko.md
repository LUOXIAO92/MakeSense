# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense는 동시 음성 번역 모델을 위한 sense-aware 학습 데이터와 검증 파이프라인을 만드는 연구·데이터 생성 프로젝트입니다. ASR / 전사 작업도 함께 다룹니다.

목표는 음성 번역을 점진적인 멀티턴 대화 과제로 바꾸는 것입니다. 오디오가 chunk 단위로 들어오면, 모델은 언제 원문 전사를 내보낼지, 언제 목표 언어 번역을 내보낼지, 언제 더 많은 문맥을 기다릴지를 학습합니다.

현재 이 저장소는 데이터셋 구축 pipeline 과 학습 데이터 구성 도구를 제공합니다. 핫워드 / 지정 번역어 지원과 추론 백엔드는 향후 작업입니다.

## 프로젝트 개요

목표: ASR / 전사 기능을 함께 갖춘 streaming simultaneous speech translation 용 omni / multimodal model 을 학습하는 것.

이 프로젝트는 다음 논문에서 아이디어를 얻었습니다.
- 무제한 입력 window / time-pressure 동시 번역: [InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation: [SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

이 프로젝트에서는:
- sense-unit detector, audio encoder, LLM backbone alignment 를 처음부터 학습하지 **않습니다**.
- 모델 아키텍처를 수정하지 **않습니다**. 무제한 길이의 스트리밍 번역은 런타임의 sliding-window context management 로 처리합니다.
- ground-truth 에 가까운 데이터셋과 pipeline 검증 surface 를 만들어 omni model 이 동시 번역 전략을 학습할 수 있게 합니다.

## 요구 사항
### Python packages
```bash
pip install stanza jieba nagisa qwen-asr
pip install transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard --force-reinstall
```
- `qwen-asr` 는 오래된 `transformers` 를 설치합니다.

### 서브모듈 의존성
- 단어 aligner: [TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- 기본 베이스 모델은 [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) 입니다.

## Pipeline

### 원언어 / 전사 측
1. metadata 에서 cache records 초기화
2. 필요 시 ASR 전사
3. forced alignment
4. time-pressure 원언어 sense-unit segmentation

### 목표 언어 / 번역 측
1. raw translation
2. translation reconstruction
3. pure-text target sense-unit segmentation
4. target-centric source mapping
5. final dataset collection/export

## 사용법: 전체 데이터셋 pipeline 실행

현재 워크플로는 `examples/` 아래의 단계별 스크립트로 실행합니다. 각 단계는 이전 단계 cache 를 읽고 새 단계 cache 를 기록하며, 기존 JSONL cache 상태에서 이어서 실행할 수 있습니다.

실행하기 전에 **각 example 스크립트 상단의 설정 블록**을 확인하세요. 자주 쓰는 항목은 dataset/cache roots, model names, target languages, `ENABLE_THINKING`, `TOP_P`, `TOP_K`, 그리고 필요한 경우 `ENABLE_VISUALIZATION` 입니다.

### 현재 제공되는 기능

현재 사용 가능:
- 최종 pipeline-9 JSONL export 까지 실행 가능한 데이터셋 구축 pipeline.
- `src/data_loader` 를 통한 최종 데이터셋 학습 샘플 구성.
- `examples/train_lora.py` 와 `src/train` 기반의 초기 real-audio LoRA trainer.

TODO:
- [x] 높은 우선순위: 아주 작은 샘플로 `examples/train_lora.py` 의 thin LoRA trainer path 를 테스트하고, conversation rendering, assistant-only loss 설정, 1〜2 training steps 가 제대로 동작하는지 확인한다.
- [ ] `google/gemma-4-E2B-it` 로 full LoRA training 을 완료한다.
- [ ] **두 번째 우선순위:** 학습된 streaming model 을 실행하기 위한 inference backend 를 추가한다.
- [ ] training / inference context 에 hot words 와 hot translations 지원을 추가한다.

소규모 검증 결과 (`google/gemma-4-E2B-it`, `train_examples: 96`):
- tolerance window size: 1.0 s
- system prompt: Translate to Japanese, tolerance window size is 1
- 아래는 소규모 테스트 결과입니다. 왼쪽은 ground truth, 오른쪽은 model output 입니다. thinking 은 꺼 두었지만 출력에 thinking content 가 여전히 섞여 있어 추가 확인이 필요합니다.
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

기본 LoRA 학습 예시는 `google/gemma-4-E2B-it` 를 대상으로 하며, Transformers multimodal model, PEFT LoRA, 실제 오디오 chunks, TensorBoard logging, JSONL metrics 를 사용합니다.

dataset, model, LoRA, monitoring 옵션은 아래 파일 상단에서 설정합니다.

```text
examples/train_lora.py
```

학습 실행:

```bash
PYTHONPATH=src python examples/train_lora.py
```

학습은 LoRA adapter 와 monitoring 파일을 설정된 `OUTPUT_DIR` 아래에 기록합니다.

```text
outputs/makesense_lora/
  adapter_config.json
  adapter_model.safetensors
  runs/
  train_metrics.jsonl
  sample_generations.jsonl
```

Sample generation 은 strict streaming evaluation 을 사용합니다. 각 assistant turn 은 그 시점까지 볼 수 있는 audio chunks 만 사용합니다. 평가할 레코드 수는 `examples/train_lora.py` 의 `SAMPLE_EVALUATION_RECORD_COUNT` 로 제어합니다.

### Pipeline 실행 순서

각 단계는 아래 순서로 실행합니다.

```bash
export PYTHONPATH=src 

# 1. 필요한 경우 데이터셋 원본을 다운로드 / 준비합니다. (여기서는 Emilia dataset 을 사용합니다. https://huggingface.co/datasets/amphion/Emilia-Dataset 참고)
python examples/pipeline_1_download_Emilia.py

# 2. dataset metadata 에서 PipelineRecord cache shards 를 초기화합니다.
python examples/pipeline_2_initialize_cache.py

# 3a. 선택 사항: omni ASR + translation 경로.
# one-pass multimodal translation 동작을 확인할 때 사용합니다.
python examples/pipeline_3_a_asr_translation_omni.py

# 3b-1. ASR-only path.
# source transcript artifacts 를 cache 에 채웁니다.
python examples/pipeline_3_b1_asr.py

# 3b-2. ASR cache 에서 raw translation 을 생성합니다.
# 기본값은 text-only 입니다. audio-assisted mode 는 스크립트에서 제어하며, audio 를 지원하는 omni model 이 필요합니다.
python examples/pipeline_3_b2_asr_text_translation.py

# 4. source transcription 에 대한 forced alignment.
python examples/pipeline_4_forced_alignment.py

# 5. time-pressure source sense-unit segmentation.
python examples/pipeline_5_asr_segmentation.py

# 6. translation reconstruction.
python examples/pipeline_6_translation_reconstruction.py

# 7. pure-text target sense-unit segmentation.
python examples/pipeline_7_pure_text_segmentation.py

# 8. target sense units 를 source token ids 로 잇는 target-centric mapping.
python examples/pipeline_8_target_centric_mapping.py

# 9. 완료된 pipeline-8 cache state 에서 최종 데이터셋을 수집 / export 합니다.
python examples/pipeline_9_collect_dataset.py
```

권장 순서:

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

Pipeline 9 는 최종 데이터셋을 다음 구조로 export 합니다.

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

### Streaming model output

```text
<src>(transcription text)</src><tgt>(target translation text)</tgt>
```

원언어 전사나 목표 언어 번역을 안정적으로 내보내기에 정보가 부족하면, 모델은 `<|wait|>` 를 출력할 수 있습니다.

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
