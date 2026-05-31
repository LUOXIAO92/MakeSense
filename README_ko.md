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
pip install git+https://github.com/LUOXIAO92/MultimodalAssistantMask.git
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
- [x] **높은 우선순위**: 아주 작은 샘플로 `examples/train_lora.py` 를 실행해 대화 템플릿, assistant-only loss, 1〜2 step 학습이 제대로 동작하는지 확인한다.
- [ ] **높은 우선순위**: `google/gemma-4-E2B-it` 의 LoRA 학습을 끝까지 실행한다.
- [ ] **두 번째 우선순위:** 학습된 streaming model 을 실행하기 위한 inference backend 를 추가한다.
- [ ] training / inference context 에 hot words 와 hot translations 지원을 추가한다.

### LoRA 학습 시작점

기본 LoRA 학습 예시는 `google/gemma-4-E2B-it` 를 대상으로 합니다. Transformers 멀티모달 모델에 PEFT LoRA 를 붙이고, 실제 오디오를 나눈 chunk 를 학습에 사용합니다. 학습 중 지표는 프로젝트가 관리하는 TensorBoard 로그에 기록하고, 스트리밍 평가 결과는 테스트 지표 파일에 저장합니다.

데이터셋, 모델, LoRA, checkpoint, 모니터링 관련 옵션은 아래 스크립트 상단에서 설정합니다.

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

학습은 LoRA adapter 와 monitoring 파일을 설정된 `OUTPUT_DIR` 아래에 기록합니다.

```text
outputs/makesense_lora/
├── adapter_config.json
├── adapter_model.safetensors
├── checkpoint-*/
├── runs/
│   └── <yyyy-mm-dd_hh-mm-ss>/
└── test_metrics.json
```

스트리밍 평가는 각 assistant turn 을 생성할 때 그 시점까지 도착한 오디오 chunk 만 모델에 전달합니다. 평가에 사용할 레코드 수는 `examples/train_lora.py` 의 `TEST_RECORD_COUNT` 로 정합니다. `0` 이면 평가를 건너뛰고, `-1` 이면 test split 전체를 사용하며, 양수이면 그 개수까지만 평가합니다.

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

## Small-scale validation results (`google/gemma-4-E2B-it`, `train_examples: 96`):

### Training paramenters

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

### Results

- tolerance window size: 1.0 s
- Following is small scale test, left is ground truth, right is model output. I have disabled the thinking, but thinking content still occurs. An in-depth check is needed.

#### Test Outputs - step 50

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


#### Final Test Outputs - step 240

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