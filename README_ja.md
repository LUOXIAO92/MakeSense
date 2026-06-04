[English](README.md) | [简体中文](README_zh-cn.md) | 日本語 | [한국어](README_ko.md)

# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense は、同時音声翻訳モデル向けに sense-aware な学習データと検証パイプラインを作るための研究・データ生成プロジェクトです。ASR / 書き起こしタスクにも対応します。

このプロジェクトでは、音声翻訳を逐次的なマルチターン対話として扱います。音声がチャンクごとに届き、モデルはその時点で原文の書き起こしを出すのか、訳文を出すのか、それとももう少し文脈を待つのかを学習します。

現在のリポジトリでは、データセット構築 pipeline と学習データ生成ユーティリティを提供しています。ホットワード / 指定訳語のサポートと推論バックエンドは今後追加予定です。

## プロジェクト概要

目標：ASR / 書き起こし能力も持つ omni / multimodal model に、ストリーミング同時音声翻訳の振る舞いを学習させること。

本プロジェクトは以下の論文から着想を得ています。
- 無限入力ウィンドウ / time-pressure 同時翻訳：[InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation：[SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

本プロジェクトでは：
- sense-unit detector、audio encoder、LLM backbone alignment をゼロから学習することは**しません**。
- モデルアーキテクチャは**変更しません**。長時間のストリーミング翻訳は、実行時のスライディングウィンドウ型コンテキスト管理で扱います。
- ground-truth に近いデータセットと pipeline 検証の仕組みを作り、omni model が同時翻訳の戦略を学習できるようにします。

## 要件

### Clone repository
```bash
git clone --recursive https://github.com/LUOXIAO92/MakeSense.git 
```

### Python packages

データセット準備用：
- データセット準備には専用の Python 環境を使うことを推奨します。`qwen-asr` は新しい `transformers` と互換性がないため、学習用環境とは分けてください。
- Flash Attention は、必要に応じてこちらの prebuilt wheel を参照してください：[Flash attention prebuild wheels](https://github.com/mjun0812/flash-attention-prebuild-wheels)
```bash
pip install whisper openai stanza
pip install qwen-asr --force-reinstall
pip install torch==2.10 torchaudio==2.10.0 torchvision --force-reinstall # --index-url https://download.pytorch.org/whl/cu130
```

学習用：
- 学習環境では Python 3.13 を使っても問題ありません。
```bash
pip install stanza jieba nagisa transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard
pip install git+https://github.com/LUOXIAO92/MultimodalAssistantMask.git
```

### サブモジュール依存
- 単語アライナー：[TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- デフォルトのベースモデルには [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) を使います。
- マルチモーダル入力に対する assistant-only loss の構築には [MultimodalAssistantMask](https://github.com/LUOXIAO92/MultimodalAssistantMask.git) を使います。

## Pipeline

### 原言語 / 書き起こし側
1. metadata から cache records を初期化
2. 必要に応じて ASR 書き起こし
3. forced alignment
4. time-pressure 原言語 sense-unit segmentation

### 目標言語 / 翻訳側
1. raw translation
2. translation reconstruction
3. pure-text target sense-unit segmentation
4. target-centric source mapping
5. final dataset collection/export

## 使い方：データセット pipeline 全体を実行する

現在のワークフローは `examples/` 配下のステージスクリプトで実行します。各ステージは前段の cache を読み込み、新しいステージ cache を書き出します。既存の JSONL cache から続きを再開することもできます。

実行前に、**各 example スクリプト冒頭の設定ブロック**を確認してください。よく使う項目には dataset/cache のパス、モデル名、対象言語、`TOP_P`、provider 固有の `EXTRA_BODY`、必要に応じて `ENABLE_VISUALIZATION` などがあります。

`EXTRA_BODY` は OpenAI-compatible Chat Completions request にそのまま渡される、provider 固有の拡張パラメータです。`top_k` や thinking/reasoning の制御は provider によって schema が異なるため、以下では代表的な provider-specific 設定例を示します。

```python
# vLLM / local OpenAI-compatible API の例:
EXTRA_BODY = {"top_k": 20, "chat_template_kwargs": {"enable_thinking": False}}

# OpenRouter reasoning の例:
EXTRA_BODY = {"reasoning": {"effort": "none"}}

# DeepSeek thinking の例:
EXTRA_BODY = {"thinking": {"type": "disabled"}}
```

参考ドキュメント:
- OpenRouter reasoning tokens: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens
- DeepSeek thinking mode: https://api-docs.deepseek.com/guides/thinking_mode

### 現在使えるもの

利用可能：
- 最終 pipeline-9 JSONL export まで実行できるデータセット構築 pipeline。
- `src/data_loader` による、最終データセットからの学習サンプル構築。
- `examples/train_lora.py` と `src/train` による初版 real-audio LoRA trainer。

TODO：
- [x] **高優先度**：小さなサンプルで `examples/train_lora.py` を動かし、対話テンプレート、assistant-only loss、1〜2 step の学習が正しく動くことを確認する。
- [ ] **高優先度**：`google/gemma-4-E2B-it` の LoRA 学習を最後まで実行する。
  - **Ongoing**：現在は、より大規模な学習データの整備を進めています。公開予定のデータセットには、約 8,000 件の音声・書き起こしサンプルと、翻訳方策を学習するためのマルチターン会話の軌跡データ約 24,000 件が含まれます。このデータは [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) をもとに二次処理したものです。質の高い多言語音声データを公開してくださっている Emilia-Dataset プロジェクトに感謝します。
- [ ] **次に高い優先度：** 学習済み streaming model を実行するための inference backend を追加する。
  - **Ongoing**：推論側の実装は [MakeSense-Inference](https://github.com/LUOXIAO92/MakeSense-Inference.git) で進めています。
- [ ] training / inference context 向けに hot words と hot translations のサポートを追加する。

### LoRA 学習エントリ

デフォルトの LoRA 学習例は `google/gemma-4-E2B-it` 向けです。Transformers のマルチモーダルモデルに PEFT LoRA を載せ、実音声チャンクを使って学習します。学習中の指標はプロジェクト側で管理する TensorBoard scalar ログに記録し、strict streaming test の指標も出力します。

データセット、モデル、LoRA、checkpoint、モニタリング関連の設定は、次のスクリプト冒頭で変更できます。

```text
examples/train_lora.py
```

主な設定項目：
- `OUTPUT_DIR`
- `CONTINUE_TYPE`：`none`、`resume`、`branch`
- `CHECKPOINT_PATH`
- `SAVE_PROCESSOR`
- `TEST_STEPS`、`TEST_MAX_NEW_TOKENS`、`TEST_RECORD_COUNT`

学習を実行します：

```bash
PYTHONPATH=src python examples/train_lora.py
```

LoRA adapter、checkpoint、monitoring ファイルは、設定した `OUTPUT_DIR` に書き込まれます。

```text
outputs/makesense_lora/
├── adapter_config.json
├── adapter_model.safetensors
├── checkpoint-*/
├── runs/
│   └── <yyyy-mm-dd_hh-mm-ss>/
└── test_metrics.json
```

strict streaming test では、各 assistant turn の生成時に、その時点までに到着している音声チャンクだけをモデルに渡します。評価に使うレコード数は `examples/train_lora.py` の `TEST_RECORD_COUNT` で指定します。`0` なら評価を行わず、`-1` なら test split 全体を使い、正の値ならその件数までを評価します。

### カスタマイズ
pipeline レベルの非学習設定を調整する場合は、`src/configs/config.py` と `src/configs/LANGUAGE_PACK_*.py` を参照してください。主に、データのサンプリング範囲、対応言語、ASR / forced-alignment モデル、tokenizer、wait token、ストリーミング window size、最大 chunk size、reconstruction validator 用の high-noise tokens、各言語の language pack / few-shot examples などを設定できます。

### Pipeline の実行順序

各ステージは次の順序で実行します。

```bash
export PYTHONPATH=src 

# 1. 必要に応じて、データセットの元データをダウンロード / 準備します。（ここでは Emilia dataset を使います。https://huggingface.co/datasets/amphion/Emilia-Dataset を参照してください）
python examples/pipeline_1_download_Emilia.py

# 2. dataset metadata から PipelineRecord cache shards を初期化します。
python examples/pipeline_2_initialize_cache.py

# 3a-1. 推奨 ASR 経路。
# source 側の書き起こし結果を cache に補完します。
python examples/pipeline_3_a1_asr.py

# 3a-2. 推奨される ASR ベースの raw translation 経路。
# 実測では、中国語・日本語・韓国語のいずれでも、ASR の後に omni/audio-assisted translation で補正する方が、direct omni ASR より精度と安定性が高くなります。
python examples/pipeline_3_a2_asr_text_translation.py

# 3b. 任意の direct omni ASR + translation 経路。
# one-pass multimodal translation の挙動を確認するときに使います。
python examples/pipeline_3_b_asr_translation_omni.py

# 4. source transcription の forced alignment。
python examples/pipeline_4_forced_alignment.py

# 5. time-pressure source sense-unit segmentation。
python examples/pipeline_5_asr_segmentation.py

# 6. translation reconstruction。
python examples/pipeline_6_translation_reconstruction.py

# 7. pure-text target sense-unit segmentation。
python examples/pipeline_7_pure_text_segmentation.py

# 8. target sense units から source token ids への target-centric mapping。
python examples/pipeline_8_target_centric_mapping.py

# 9. 完了済み pipeline-8 cache から最終データセットを収集 / export します。
python examples/pipeline_9_collect_dataset.py
```

推奨順序：

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

### 最終データセット出力

Pipeline 9 は次の構成で最終データセットを export します。

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

`dimensional_analysis/` は、翻訳段階で生成された文全体レベルの `target.shared.translation_analysis` を独立して export する領域です。transcription / translation のデータセット schema とは分けて保存されます。

## 出力形式

### Streaming model output

```text
<src>(transcription text)</src><tgt>(target translation text)</tgt>
```

原言語の書き起こしや目標言語の翻訳を安定して出すには情報が足りない場合、モデルは `<|wait|>` を出力できます。

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

#### Metrics

ここで示す strict streaming test の指標は、主にストリーミング対話における出力形式とリリース判断を確認するためのものです。具体的には、出力が `<src>...</src><tgt>...</tgt>` のプロトコルに従っているか、生成が想定した stop token で止まっているか、各 assistant turn で source / target 側が待つべきか内容を出すべきかを見ています。ASR の文字単位の正確さや、翻訳の意味的な品質を直接測る指標ではありません。

**POSTPROCESSED_TURN_STOP_RATE**

- 意味：後処理後の出力が、余計な文字列を含まない完全なプロトコル出力になっている割合です。
- 計算：`postprocessed_turn_stop_turns / TURN_COUNT`。後処理後のテキストがプロトコルとして正しく、正規化された `<src>...</src><tgt>...</tgt>` 出力と一致する turn を成功として数えます。

**PROTOCOL_VALID_RATE**

- 意味：モデル出力が指定されたプロトコルに従っている割合です。
- 計算：`protocol_valid_turns / TURN_COUNT`。出力は `<src>...</src><tgt>...</tgt>` に一致する必要があり、source / target の中に `<src>`、`</src>`、`<tgt>`、`</tgt>` などのタグが入れ子で含まれていてはいけません。

**RAW_TURN_STOP_RATE**

- 意味：raw decode された生成結果が、設定された generation stop token で正しく止まっている割合です。
- 計算：`raw_turn_stop_turns / TURN_COUNT`。raw output が postprocessed output の直後に `generation_stop` を続けている場合、その turn は正しく停止したものとして扱います。

**RECORD_COUNT**

- 意味：今回の strict streaming test で実際に評価した test record の数です。
- 計算：`len(records)`。

**SRC_RELEASE_ACCURACY**

- 意味：ground truth で source 側が転写テキストを出すべき turn のうち、モデルも source 側で内容を出した割合です。
- 計算：`src_release_correct / SRC_RELEASE_TOTAL`。ここでは `<src>...</src>` が wait ではないかだけを見ており、出力された転写テキストそのものが正しいかは評価しません。

**SRC_RELEASE_TOTAL**

- 意味：ground truth で source 側が内容を出すべき turn の数です。
- 計算：ground truth の `<src>...</src>` が `<|wait|>` ではない turn を数えます。

**SRC_WAIT_ACCURACY**

- 意味：ground truth で source 側が待つべき turn のうち、モデルも source 側で wait を出した割合です。
- 計算：`src_wait_correct / SRC_WAIT_TOTAL`。モデルの `<src>...</src>` が `<|wait|>` かどうかだけを見ます。

**SRC_WAIT_TOTAL**

- 意味：ground truth で source 側が待つべき turn の数です。
- 計算：ground truth の `<src>...</src>` が、前後の空白を除いたうえで `<|wait|>` と完全に一致する turn を数えます。

**TGT_RELEASE_ACCURACY**

- 意味：ground truth で target 側が翻訳を出すべき turn のうち、モデルも target 側で内容を出した割合です。
- 計算：`tgt_release_correct / TGT_RELEASE_TOTAL`。ここでは `<tgt>...</tgt>` が wait ではないかだけを見ており、出力された翻訳の意味的な正しさは評価しません。

**TGT_RELEASE_TOTAL**

- 意味：ground truth で target 側が翻訳を出すべき turn の数です。
- 計算：ground truth の `<tgt>...</tgt>` が `<|wait|>` ではない turn を数えます。

**TGT_WAIT_ACCURACY**

- 意味：ground truth で target 側が待つべき turn のうち、モデルも target 側で wait を出した割合です。
- 計算：`tgt_wait_correct / TGT_WAIT_TOTAL`。モデルの `<tgt>...</tgt>` が `<|wait|>` かどうかだけを見ます。

**TGT_WAIT_TOTAL**

- 意味：ground truth で target 側が待つべき turn の数です。
- 計算：ground truth の `<tgt>...</tgt>` が、前後の空白を除いたうえで `<|wait|>` と完全に一致する turn を数えます。

**TURN_COUNT**

- 意味：選択されたすべての test record で、実際に評価した assistant turn の総数です。
- 計算：`records` に含まれる、生成・評価対象となった assistant 出力をすべて合計します。

#### Test Outputs - step 50

- tolerance window size: 1.0 s
- 以下は小規模テストの結果です。左側が ground truth、右側がモデル出力です。

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