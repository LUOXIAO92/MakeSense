[English](lora_vram_optimization_lessons_en.md) | [简体中文](lora_vram_optimization_lessons_zh-cn.md) | 日本語 | [한국어](lora_vram_optimization_lessons_ko.md)

# LoRA VRAM 最適化メモ

学習環境:
- System: WSL2
- CPU: AMD Ryzen 9 9950X
- RAM: 128GiB DDR5
- GPU: Nvidia RTX 5090

## 1. 起きていたこと

### 問題 1: 学習に入る前から VRAM 使用量が高すぎた

最初の実装では、k-bit LoRA 学習の準備に PEFT の汎用ヘルパー `prepare_model_for_kbit_training(...)` を使っていた。このヘルパーは、4bit 化の対象外にある浮動小数点パラメータを fp32 にキャストする。テキストだけの小さな構成ならまだ扱える場面もあるが、マルチモーダルモデルでは危ない。audio encoder、vision/video encoder、embedding、LM head など、bf16 のまま置きたい大きなモジュールまで広がる可能性がある。小さめのモデルでは embedding と LM head の比率も無視できないので、fp32 化すると VRAM の内訳が一気に変わる。

Gemma 4 E2B / 4B 系には、もう一つ大きな要素がある。各層用の embedding lookup モジュールを持っていて、これは Linear ではなく embedding / lookup table に分類される。そのため、通常の 4bit Linear quantization では処理されない。この重みは約 2.3B parameters あり、bf16 の時点で約 4.38GiB を使う。汎用の準備関数がこれを fp32 に広げると、起動直後の VRAM がさらに増える。

観測値はこの説明と合っていた。
- モデル読み込み直後: allocated≈6.70GiB
- PEFT 汎用準備関数の実行後: allocated≈12.43GiB
- `train_lora` に入った時点: allocated≈12.52GiB

起動段階で増えた 5GiB+ は、dataset 由来ではなかった。モデル準備の段階で、大きな非 4bit パラメータを fp32 に広げたことが原因だった。

### 問題 2: 学習中に reserved/cache が膨らみ続け、速度が落ちた

学習中は、実際に tensor が使っている VRAM と PyTorch が allocator 側で予約している VRAM の差が大きかった。典型的な値は次の通り。
- allocated≈12.77GiB
- max_allocated≈20.25GiB
- reserved≈32.86GiB

つまり、driver から 30GiB+ に見えていた VRAM の全部が live tensor ではなかった。大きな部分を PyTorch allocator が cache、workspace、断片化したブロックとして保持していた。ただし、これは見かけだけの問題ではない。reserved/cache の増加を抑えない場合、学習は CPU offload が起きたような遅さになり、約 `25s/it` まで落ちた。cache の膨張を抑えると、16 gradient accumulation steps の設定で約 `6-7s/it` まで戻った。

## 2. 対応

### 対応 1: PEFT 汎用ヘルパーを外し、プロジェクト側のマルチモーダル用ヘルパーに切り替えた

PEFT の `prepare_model_for_kbit_training(...)` を使うのをやめ、プロジェクト側の関数に切り替えた。

```python
prepare_multimodal_model_for_kbit_lora_training(...)
```

この関数は LoRA 学習に必要な準備だけを行う。
- base model を freeze する
- `use_cache` を無効にする
- input gradients を有効にする
- gradient checkpointing を有効にする
- audio / vision encoder、embedding、LM head、Gemma 4 の巨大な `embed_tokens_per_layer` lookup 重みをまとめて fp32 化しない

変更後、起動時の VRAM は増えなくなった。
- モデル読み込み直後: allocated≈6.70GiB
- プロジェクト側の準備関数の実行後: allocated≈6.70GiB
- LoRA adapter 追加後: allocated≈6.79GiB
- `train_lora` に入った時点: allocated≈6.79GiB

LoRA 学習の準備を省いたわけではない。必要な準備は残しつつ、マルチモーダル系の大きなモジュール、embedding / LM head、Gemma 4 固有の per-layer embedding lookup を fp32 に広げないようにした。

### 対応 2: `CUDA_EMPTY_CACHE_STEPS = 1` を維持し、学習中の reserved/cache を抑えた

学習中の reserved/cache 膨張には、optimizer step の後に一定間隔で `torch.cuda.empty_cache()` を呼ぶ方法を使った。現在の設定は次の通り。

```python
CUDA_EMPTY_CACHE_STEPS = 1
```

この設定は live tensor が使う VRAM を減らさない。PyTorch がすでに使い終わったが allocator cache に残している領域を解放し、driver から見える予約済み VRAM の圧力を下げる。今回の構成では速度差として効果を確認できた。
- reserved/cache を制限しない場合: 約 `25s/it`
- `CUDA_EMPTY_CACHE_STEPS=1`: 約 `6-7s/it`

今回のフル LoRA 学習設定では、`CUDA_EMPTY_CACHE_STEPS = 1` を残す価値がある。

## 3. 解決状況

| 項目 | 結果 | 根拠 |
| --- | --- | --- |
| PEFT 汎用準備関数による fp32 膨張 | **解決済み** | 準備関数の前後で allocated が `6.70GiB` のまま増えない |
| LoRA adapter の VRAM 使用量 | **問題なし** | adapter の増加分は約 `0.09GiB` |
| 学習中の reserved/cache 膨張による速度低下 | **実用できる状態まで解決済み** | `CUDA_EMPTY_CACHE_STEPS=1` で約 `25s/it` から `6-7s/it` へ戻った |
| 残っている基礎 VRAM 使用量 | **今回の対象外** | 主に bf16 lookup / embedding など、モデル本体の resident parameter が占めている |

起動時の異常な VRAM 増加は消えた。学習中の cache 膨張も、現在の設定では通常に学習できる水準まで抑えられている。残っている VRAM は主にモデル構造そのものが要求する resident memory なので、今回の bug として扱わない。

## 4. 原因ではないと確認したもの

### dataset 全体が GPU に載ったわけではない

dataset 構築、rows materialization、Trainer 初期化の前後で GPU VRAM は増えなかった。dataset rows も長時間生きる tensor を保持していなかった。

### `MAX_SEQ_LENGTH=16000` まで padding されたわけではない

現在の collator は dynamic padding を使っている。各 sample をすべて `MAX_SEQ_LENGTH=16000` まで pad しているわけではない。実測した sample 長はおおむね `1.6k-1.8k` tokens だった。

### audio features は大きすぎなかった

processor が作る audio features は MiB 単位だった。GiB 単位ではないので、10GiB+ の VRAM 圧力を説明できない。

### `use_cache=True` は主原因ではなかった

現在の学習準備関数は `use_cache` を無効にする。これは学習時の設定として正しい。ただし今回の観測値は、`use_cache=True` が VRAM 急増の主原因だったとは示していない。

### 残っている巨大な embedding / lookup 重みは別課題

Gemma 4 E2B / 4B 系には、大きな per-layer embedding lookup 重みがある。

```text
embed_tokens_per_layer.weight ≈ 2.3B parameters ≈ 4.38GiB bf16
```

この重みは embedding / lookup table であり、Linear layer ではない。そのため、現在の 4bit Linear quantization では量子化されない。ここをさらに削るには、embedding / lookup 用の独自 quantization か、モデル構造レベルの対応が必要になる。今回の調査で安全に扱う範囲を超える。

## まとめ

今回直した問題は二つある。
- PEFT 汎用準備関数による fp32 VRAM 膨張をなくし、起動時の allocated を `12.52GiB` から `6.79GiB` まで下げた
- `CUDA_EMPTY_CACHE_STEPS=1` で学習中の reserved/cache 膨張を抑え、速度を約 `25s/it` から `6-7s/it` まで戻した
