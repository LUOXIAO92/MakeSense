[English](lora_vram_optimization_lessons_en.md) | [简体中文](lora_vram_optimization_lessons_zh-cn.md) | [日本語](lora_vram_optimization_lessons_ja.md) | 한국어

# LoRA VRAM 최적화 메모

학습 환경:
- System: WSL2
- CPU: AMD Ryzen 9 9950X
- RAM: 128GiB DDR5
- GPU: Nvidia RTX 5090

## 1. 문제 상황

### 문제 1: 학습을 시작하기 전부터 VRAM 사용량이 높았다

처음 구현에서는 k-bit LoRA 학습 준비 단계에서 PEFT의 범용 헬퍼인 `prepare_model_for_kbit_training(...)`를 사용했다. 이 헬퍼는 4bit 경로에 들어가지 않는 floating-point 파라미터를 fp32로 캐스팅한다. 텍스트 모델만 다룰 때는 괜찮을 수 있지만, 멀티모달 모델에서는 위험하다. audio encoder, vision/video encoder, embedding, LM head처럼 bf16으로 남겨 두고 싶은 큰 모듈까지 fp32로 커질 수 있다. 작은 모델에서는 embedding과 LM head가 차지하는 비중도 작지 않으므로, fp32 캐스팅 하나로 VRAM 구성이 크게 바뀐다.

Gemma 4 E2B / 4B 계열에는 별도의 큰 항목도 있다. 이 모델은 per-layer embedding lookup 모듈을 갖고 있다. 이 모듈은 Linear layer가 아니라 embedding / lookup table에 해당하므로, 일반적인 4bit Linear quantization이 처리하지 않는다. 이 weight는 약 2.3B parameters이고, bf16 상태에서도 약 4.38GiB를 차지한다. 범용 준비 함수가 이 부분까지 fp32로 바꾸면 시작 시점의 VRAM이 더 올라간다.

관측값은 이 흐름과 맞았다.
- 모델 로드 직후: allocated≈6.70GiB
- PEFT 범용 준비 함수 실행 후: allocated≈12.43GiB
- `train_lora` 진입 시점: allocated≈12.52GiB

시작 단계에서 늘어난 5GiB+는 dataset 때문이 아니었다. 모델 준비 과정에서 큰 non-4bit 파라미터를 fp32로 확대한 것이 원인이었다.

### 문제 2: 학습 중 reserved/cache가 계속 커지고 속도가 떨어졌다

학습 중에는 실제 tensor가 쓰는 VRAM과 PyTorch allocator가 예약해 둔 VRAM 사이의 차이가 컸다. 대표 관측값은 다음과 같았다.
- allocated≈12.77GiB
- max_allocated≈20.25GiB
- reserved≈32.86GiB

driver에서 보이는 30GiB+ VRAM 전체가 live tensor는 아니었다. PyTorch allocator가 cache, workspace, fragmented block 형태로 큰 메모리를 잡고 있었다. 그래도 영향은 실제로 나타났다. reserved/cache 증가를 제어하지 않으면 학습 속도가 CPU offload가 걸린 것처럼 약 `25s/it`까지 떨어졌다. cache 증가를 억제한 뒤에는 16 gradient accumulation steps 설정에서 약 `6-7s/it`로 돌아왔다.

## 2. 처리한 내용

### 처리 1: PEFT 범용 헬퍼를 제거하고 프로젝트의 멀티모달용 준비 함수로 바꿨다

PEFT의 `prepare_model_for_kbit_training(...)`를 제거하고, 프로젝트에 있는 준비 함수를 사용했다.

```python
prepare_multimodal_model_for_kbit_lora_training(...)
```

이 함수는 LoRA 학습에 필요한 준비만 수행한다.
- base model freeze
- `use_cache` 비활성화
- input gradients 활성화
- gradient checkpointing 활성화
- audio / vision encoder, embedding, LM head, Gemma 4의 큰 `embed_tokens_per_layer` lookup weight를 통째로 fp32로 캐스팅하지 않음

변경 후 시작 시점의 VRAM은 그대로 유지됐다.
- 모델 로드 직후: allocated≈6.70GiB
- 프로젝트 준비 함수 실행 후: allocated≈6.70GiB
- LoRA adapter 추가 후: allocated≈6.79GiB
- `train_lora` 진입 시점: allocated≈6.79GiB

LoRA 학습 준비를 덜 한 것이 아니다. 필요한 설정은 유지하고, 멀티모달 쪽의 큰 모듈, embedding / LM head, Gemma 4 특유의 per-layer embedding lookup을 fp32로 키우지 않게 만든 것이다.

### 처리 2: `CUDA_EMPTY_CACHE_STEPS = 1`을 유지해 학습 중 reserved/cache 증가를 눌렀다

학습 중 reserved/cache가 커지는 문제에는 optimizer step 이후 일정 간격으로 `torch.cuda.empty_cache()`를 호출하는 방식으로 대응했다. 현재 설정은 다음과 같다.

```python
CUDA_EMPTY_CACHE_STEPS = 1
```

이 설정은 live tensor가 실제로 쓰는 VRAM을 줄이지 않는다. PyTorch가 더 쓰지 않지만 allocator cache에 들고 있는 메모리를 반환해서, driver에서 보이는 reserved VRAM 압력을 낮춘다. 이번 구성에서는 속도 차이로 효과를 확인했다.
- reserved/cache를 제한하지 않은 경우: 약 `25s/it`
- `CUDA_EMPTY_CACHE_STEPS=1`: 약 `6-7s/it`

현재의 full LoRA 학습 설정에서는 `CUDA_EMPTY_CACHE_STEPS = 1`을 유지하는 편이 맞다.

## 3. 최종 상태

| 항목 | 결과 | 근거 |
| --- | --- | --- |
| PEFT 범용 준비 함수로 인한 fp32 확장 | **해결됨** | 준비 함수 실행 전후 allocated가 `6.70GiB`로 유지됨 |
| LoRA adapter VRAM 사용량 | **문제 아님** | adapter 추가분은 약 `0.09GiB` |
| 학습 중 reserved/cache 증가로 인한 속도 저하 | **실사용 가능한 수준까지 해결됨** | `CUDA_EMPTY_CACHE_STEPS=1` 적용 후 약 `25s/it`에서 `6-7s/it`로 회복 |
| 남아 있는 기본 VRAM 사용량 | **이번 범위 밖** | 대부분 bf16 lookup / embedding 같은 모델 resident parameter에서 나옴 |

시작 시점의 비정상적인 VRAM 증가는 사라졌다. 학습 중 cache 증가는 현재 설정에서 학습을 진행할 수 있는 수준으로 제어된다. 남아 있는 VRAM 사용량은 주로 모델 구조 자체가 요구하는 resident memory이므로, 이번 bug로 보지 않는다.

## 4. 원인에서 제외한 것들

### dataset 전체가 GPU로 올라간 문제는 아니었다

dataset 구성, rows materialization, Trainer 초기화 전후로 GPU VRAM은 늘지 않았다. dataset rows도 오래 살아 있는 tensor를 들고 있지 않았다.

### `MAX_SEQ_LENGTH=16000`까지 padding된 문제는 아니었다

현재 collator는 dynamic padding을 사용한다. 각 sample을 전부 `MAX_SEQ_LENGTH=16000`까지 pad하지 않는다. 실제로 본 sample 길이는 대략 `1.6k-1.8k` tokens였다.

### audio features 크기로는 설명되지 않았다

processor가 만든 audio features는 MiB 단위였다. GiB 단위가 아니므로, 10GiB+ VRAM 압력을 설명할 수 없다.

### `use_cache=True`가 주원인은 아니었다

현재 학습 준비 함수는 `use_cache`를 끈다. 학습 설정으로는 맞는 처리다. 다만 이번 관측값은 `use_cache=True`가 VRAM 급증의 주원인이라고 말해 주지 않았다.

### 남아 있는 큰 embedding / lookup weight는 별도 과제다

Gemma 4 E2B / 4B 계열에는 큰 per-layer embedding lookup weight가 있다.

```text
embed_tokens_per_layer.weight ≈ 2.3B parameters ≈ 4.38GiB bf16
```

이 weight는 embedding / lookup table이지 Linear layer가 아니다. 따라서 현재 4bit Linear quantization 경로에서는 양자화되지 않는다. 이 부분을 더 줄이려면 embedding / lookup용 custom quantization이나 모델 구조 차원의 처리가 필요하다. 이번 조사에서 안전하게 다룰 범위를 넘어간다.

## 정리

이번에 실제로 해결한 문제는 두 가지다.
- PEFT 범용 준비 함수가 만든 fp32 VRAM 확장을 제거했고, 시작 시점 allocated를 `12.52GiB`에서 `6.79GiB`로 낮췄다
- `CUDA_EMPTY_CACHE_STEPS=1`로 학습 중 reserved/cache 증가를 제어했고, 속도를 약 `25s/it`에서 `6-7s/it`로 되돌렸다
