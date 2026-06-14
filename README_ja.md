[English](README.md) | [简体中文](README_zh-cn.md) | 日本語 | [한국어](README_ko.md)

# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense は、同時音声翻訳モデル向けに意味単位を意識した学習データと検証パイプラインを作るための研究・データ生成プロジェクトです。ASR / 書き起こしタスクにも対応します。

このプロジェクトでは、音声翻訳を逐次的なマルチターン対話として扱います。音声がチャンクごとに届き、モデルはその時点で原文の書き起こしを出すのか、訳文を出すのか、それとももう少し文脈を待つのかを学習します。

現在のリポジトリでは、データセット構築パイプラインと学習データ生成ユーティリティを提供しています。ホットワード / 指定訳語のサポートと推論バックエンドは今後追加予定です。

## プロジェクト概要

目標：ASR / 書き起こし能力も持つオムニ / マルチモーダルモデルに、ストリーミング同時音声翻訳の振る舞いを学習させること。

本プロジェクトは以下の論文から着想を得ています。
- 無限入力ウィンドウ / time-pressure 同時翻訳：[InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation：[SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

本プロジェクトでは：
- 意味単位検出器、音声エンコーダー、LLM バックボーンアライメントをゼロから学習することは**しません**。
- モデルアーキテクチャは**変更しません**。長時間のストリーミング翻訳は、実行時のスライディングウィンドウ型コンテキスト管理で扱います。
- 正解データに近いデータセットと検証用のパイプラインを整備し、オムニモデルが同時翻訳の戦略を学習できるようにします。

## 要件

### リポジトリの取得
```bash
git clone --recursive https://github.com/LUOXIAO92/MakeSense.git 
```

### Python パッケージ

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
- 単語アライメントのベースモデルには、デフォルトで [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) を使います。
- マルチモーダル入力でアシスタント部分だけに損失をかけるため、[MultimodalAssistantMask](https://github.com/LUOXIAO92/MultimodalAssistantMask.git) を使います。

## パイプライン

### 原言語 / 書き起こし側
1. メタデータからキャッシュレコードを初期化
2. 必要に応じて ASR 書き起こし
3. 強制アライメント
4. 時間制約付きの原言語意味単位分割

### 目標言語 / 翻訳側
1. 生の訳文生成
2. 翻訳再構成
3. テキストのみの目標言語意味単位分割
4. 目標側中心の原文マッピング
5. 最終データセットの収集・書き出し

### 時刻ずれとアライメント語のグループ化

強制アライメントモデルでは、発話末尾で時刻が少し後ろにずれることがあります。そのため、最後のいくつかのアライメント用トークンの終了時刻が実際の音声長を超える場合があります。

MakeSense では、この末尾のずれを致命的なアライメントエラーではなく、想定される末尾のずれとして扱います。ストリーミング処理の出力窓は、実際の音声長と設定された窓幅によって定義されます。末尾のトークンが実際の音声長を超えている場合でも、下流段階ではそれらを最後の出力窓に含めます。そのため、この理由だけで追加の窓を作ったり、レコード全体を拒否したりはしません。

ただし、この末尾ずれの許容は、強制アライメント出力内の時間因果チェックをなくすものではありません。隣接する元の時刻付きトークンは単調である必要があります。つまり、前のトークンの終了時刻が次のトークンの開始時刻より後になってはいけません。デフォルトでは、この隣接トークンの順序が壊れているレコードは拒否されます。Pipeline 4 には、小さな境界ずれに対する任意の修復スイッチもあり、デフォルトでは無効です。有効にした場合、`next.start < prev.end < next.end` の修復可能な重なりは `next.start = prev.end` によって修正されます。`prev.end == next.start == next.end` のように接しているゼロ長の次トークンは受け入れられます。一方、修正後に次のトークンがゼロ長または負の長さになる重なり（`prev.end >= next.end` かつ `prev.end > next.start`）は、そのレコードの検証失敗として拒否されます。他のレコードの処理は継続できます。

学習データを作るとき、音声長が `window_count × window_size` より短い場合は、音声入力を対応する窓の長さまで補います。これにより、対話ターン、出力窓、音声チャンクの対応を保ちつつ、実際の音声長に基づく窓境界の意味を維持します。

Pipeline 4 は、強制アライメントモデルが出した時刻付きトークンを `alignment.tokens` に保存します。また、分かち書き器がそれらのトークンを語にまとめたグループを `alignment.words` に保存します。後続段階はこの語を使います。Pipeline 8 の `source_token_ids` も、元の時刻付きトークンではなく、この語の番号を指します。

このグループ化が必要になるのは、Qwen3-ForcedAligner が出すトークンの細かさと、後続段階で使う語の細かさが必ずしも一致しないためです。Qwen3-ForcedAligner では、中国語と韓国語は非常に細かく、実質的に文字単位に近い時刻付きトークンとして扱われます。そのため、分かち書き器が複数の文字または細かいトークンを、中国語の語や韓国語の空白 / 語節に近い語へまとめます。日本語は少し特殊です。Qwen3-ForcedAligner は日本語の時刻付きトークンを `nagisa` 分かち書き器で作りますが、MakeSense が `alignment.words` を作るときにはプロジェクト側で設定された別の分かち書き器を使うことがあります。そのため、日本語でも分かち書き境界の違いによって、複数の時刻付きトークンが一つの語にまとめられることがあります。

これらのケースに対して、MakeSense は意図的に保守的な時刻の扱いを採用しています。ストリーミング同時翻訳では厳密な時間因果関係が必要なので、処理は一つの時刻付きトークンの時間軸を切り分けて、複数の語に人工的な細かい時刻を割り当てることはしません。代わりに、複数の時刻付きトークンが一つの語にまとめられる場合、その語は最初のトークンの開始時刻と最後のトークンの終了時刻を使います。これにより、不確かな人工的時間境界を作らず、ストリーミング出力の因果関係を壊さないようにしています。

## 使い方：データセットパイプライン全体を実行する

現在のワークフローは `examples/` 配下のステージスクリプトで実行します。各ステージは前段のキャッシュを読み込み、新しいステージキャッシュを書き出します。既存の JSONL キャッシュから続きを再開することもできます。

実行前に、**各サンプルスクリプト冒頭の設定ブロック**を確認してください。よく使う項目にはデータセット / キャッシュのパス、モデル名、対象言語、`TOP_P`、提供サービス固有の `EXTRA_BODY`、必要に応じて `ENABLE_VISUALIZATION` などがあります。

`EXTRA_BODY` は OpenAI 互換のチャット補完リクエストにそのまま渡される、提供サービス固有の拡張パラメータです。`top_k` や思考 / 推論まわりの制御は提供サービスによって形式が異なるため、以下では代表的なサービス別設定例を示します。

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
- 最終第 9 ステージの JSONL 書き出しまで実行できるデータセット構築パイプライン。
- `src/data_loader` による、最終データセットからの学習サンプル構築。
- `examples/train_lora.py` と `src/train` による初版の実音声 LoRA 学習用エントリ。
- **NEW**：[MakeSense-Emilia-Dataset](https://huggingface.co/datasets/luoxiao9231/MakeSense-Emilia-Dataset)、ライセンス：cc-by-nc-4.0
  - 8,000 件の音声 / 書き起こしレコードと、同時翻訳方策を学習するためのマルチターン対話軌跡 24,000 件を含みます。
  - このデータセットは [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) を二次処理して作成しています。優れた多言語音声データを公開してくださった Emilia-Dataset プロジェクトに感謝します。

今後の作業：
- [x] **高優先度**：小さなサンプルで `examples/train_lora.py` を動かし、対話テンプレート、アシスタント部分だけの損失、1〜2 ステップの学習が正しく動くことを確認する。
- [ ] **高優先度**：`google/gemma-4-E2B-it` の LoRA 学習を最後まで実行する。
  - **進行中**：より良いハイパーパラメータを探しつつ、VRAM 使用量の最適化を続けています。
- [ ] **次に高い優先度：** 学習済みストリーミングモデルを実行するための推論バックエンドを追加する。
  - **進行中**：推論側の実装は [MakeSense-Inference](https://github.com/LUOXIAO92/MakeSense-Inference.git) で進めています。
- [ ] 学習 / 推論コンテキスト向けにホットワードと指定訳語のサポートを追加する。

### LoRA 学習エントリ

デフォルトの LoRA 学習例は `google/gemma-4-E2B-it` 向けです。Transformers のマルチモーダルモデルに PEFT LoRA を載せ、実音声チャンクを使って学習します。学習中の指標はプロジェクト側で管理する TensorBoard スカラー ログに記録し、厳密なストリーミングテストの指標も出力します。

データセット、モデル、LoRA、チェックポイント、モニタリング関連の設定は、次のスクリプト冒頭で変更できます。

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

LoRA アダプタ、チェックポイント、監視ファイルは、設定した `OUTPUT_DIR` に書き込まれます。

```text
outputs/makesense_lora/
├── adapter_config.json
├── adapter_model.safetensors
├── checkpoint-*/
├── runs/
│   └── <yyyy-mm-dd_hh-mm-ss>/
└── test_metrics.json
```

厳密なストリーミングテストでは、各アシスタントターンの生成時に、その時点までに到着している音声チャンクだけをモデルに渡します。評価に使うレコード数は `examples/train_lora.py` の `TEST_RECORD_COUNT` で指定します。`0` なら評価を行わず、`-1` ならテスト分割全体を使い、正の値ならその件数までを評価します。

### カスタマイズ
パイプラインレベルの非学習設定を調整する場合は、`src/configs/config.py` と `src/configs/LANGUAGE_PACK_*.py` を参照してください。主に、データのサンプリング範囲、対応言語、ASR / 強制アライメントモデル、トークナイザー、待機トークン、ストリーミング窓幅、最大チャンク長、再構成バリデーター用の高ノイズトークン、各言語の言語パック / 少数例 などを設定できます。

### パイプラインの実行順序

各ステージは次の順序で実行します。

```bash
export PYTHONPATH=src 

# 1. 必要に応じて、データセットの元データをダウンロード / 準備します。（ここでは Emilia dataset を使います。https://huggingface.co/datasets/amphion/Emilia-Dataset を参照してください）
python examples/pipeline_1_download_Emilia.py

# 2. データセットメタデータから PipelineRecord のキャッシュシャードを初期化します。
python examples/pipeline_2_initialize_cache.py

# 3a-1. 推奨 ASR 経路。
# 原文側の書き起こし結果をキャッシュに補完します。
python examples/pipeline_3_a1_asr.py

# 3a-2. 推奨される ASR ベースの原訳文生成経路。
# 実測では、中国語・日本語・韓国語のいずれでも、ASR の後にオムニモデル / 音声補助翻訳で補正する方が、直接オムニ ASR より精度と安定性が高くなります。
python examples/pipeline_3_a2_asr_text_translation.py

# 3b. 任意の直接オムニ ASR + 翻訳経路。
# 1 回で行うマルチモーダル翻訳の挙動を確認するときに使います。
python examples/pipeline_3_b_asr_translation_omni.py

# 4. 原文書き起こしの強制アライメント。
python examples/pipeline_4_forced_alignment.py

# 5. 時間制約付きの原文意味単位分割。
python examples/pipeline_5_asr_segmentation.py

# 6. 翻訳再構成。
python examples/pipeline_6_translation_reconstruction.py

# 7. テキストのみの訳文意味単位分割。
python examples/pipeline_7_pure_text_segmentation.py

# 8. 目標言語の意味単位から原文トークン ID への目標側中心マッピング。
python examples/pipeline_8_target_centric_mapping.py

# 9. 完了済み第 8 ステージのキャッシュから最終データセットを収集 / 書き出します。
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

Pipeline 9 は次の構成で最終データセットを書き出します。

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

`dimensional_analysis/` は、翻訳段階で生成された文全体レベルの `target.shared.translation_analysis` を独立して書き出す領域です。書き起こし / 翻訳のデータセット構造とは分けて保存されます。

## 出力形式

### ストリーミングモデルの出力

```text
<src>(transcription text)</src><tgt>(target translation text)</tgt>
```

原言語の書き起こしや目標言語の翻訳を安定して出すには情報が足りない場合、モデルは `<|wait|>` を出力できます。

### 対話形式

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

## 推論フレームワーク向けメモ：並行マルチモーダル生成での制約付きデコード

以下の大規模検証結果は、`batch=1` の実テスト結果です。1 件ずつ実際に rollout し、各ターンで生成されたモデル出力を次の prompt に戻しながら評価しています。したがって、ここで見ているのは並行生成やバッチ生成の影響を含まないプロトコル遵守の状態です。これは現在の大規模学習段階における検証記録であり、ハイパーパラメータがすでに最適であることを示すものではありません。

並行生成やバッチ生成が存在する限り、追加のリスクがあります。同じリクエストでも、単独で実行した場合と batch 内で実行した場合とで、次 token の候補スコアが完全には一致しないことがあります。候補スコアが近い場合には、1 番目または 2 番目に好まれる token が入れ替わる可能性があります。これは sampling に影響し、プロトコル形式の出力が許容される形から外れる原因にもなります。今回の多バッチ vs 単バッチ調査では、このリスクは比較モデルや純テキスト baseline よりも Gemma4 の音声テキスト入力でより目立ちました。

このプロジェクトの推論 backend を作るときは、vLLM guided decoding / structured outputs や llama.cpp GBNF grammar などの制約付きデコードを使い、出力を現在サポートしている 6 種類のプロトコル形式に制限します。詳細は [Gemma 4 multimodal batch-rank note](lessons/gemma4_multimodal_batch_rank_en.md) を参照してください。

## 大規模検証結果 (`google/gemma-4-E2B-it`, `train_examples: 21540`):

### 学習パラメータ

```text
Dataset
  - TRAIN_EXAMPLES: 21540
  - VALIDATE_EXAMPLES: 2400
  - TEST_EXAMPLES: 60

Audio
  - AUDIO_SAMPLING_RATE: 16000
  - AUDIO_CHUNK_SECONDS: 1.0

Training Steps
  - PER_DEVICE_TRAIN_BATCH_SIZE: 1
  - PER_DEVICE_EVAL_BATCH_SIZE: 5
  - GRADIENT_ACCUMULATION_STEPS: 16
  - EFFECTIVE_BATCH_SIZE: 16
    `PER_DEVICE_TRAIN_BATCH_SIZE: 1 * GRADIENT_ACCUMULATION_STEPS: 16`
  - OPTIMIZER_STEPS_PER_EPOCH: 1347
    `ceil(TRAIN_EXAMPLES: 21540 / EFFECTIVE_BATCH_SIZE: 16)`
  - CONFIGURED_NUM_TRAIN_EPOCHS: 5
  - CONFIGURED_MAX_STEPS: -1
  - TOTAL_OPTIMIZER_STEPS: 6735
    `OPTIMIZER_STEPS_PER_EPOCH: 1347 * CONFIGURED_NUM_TRAIN_EPOCHS: 5`

Hyper Parmeters
  - LEARNING_RATE: 2e-4
  - WEIGHT_DECAY: 0.0
  - ADAM_BETA1: 0.9
  - ADAM_BETA2: 0.999
  - MAX_GRAD_NORM: 1.0
  - NUM_TRAIN_EPOCHS: 5 (stop at 5400 step)
```

### 結果

#### 指標

ここで示す厳密なストリーミングテストの指標は、主にストリーミング対話における出力形式とリリース判断を確認するためのものです。具体的には、出力がプロトコル単位（ASR のみの `<src>...</src>`、または翻訳の `<src>...</src><tgt>...</tgt>`）に従っているか、生成が想定した停止トークンで止まっているか、各アシスタントターンで原文側 / 訳文側が待つべきか内容を出すべきかを見ています。ASR の文字単位の正確さや、翻訳の意味的な品質を直接測る指標ではありません。

**POSTPROCESSED_TURN_STOP_RATE**

- 意味：後処理後の出力が、閉じたプロトコルタグの境界で正しく止まっている割合です。
- 計算：`postprocessed_turn_stop_turns / TURN_COUNT`。解析されたプロトコル単位の後ろに空白、または許可された EOS / 生成停止マーカーだけが残っているターンを成功として数えます。閉じたプロトコルタグの外側に EOS 以外の内容（末尾のテキスト、カンマで区切られたタグ、繰り返されたプロトコル片など）があれば、この指標では失敗です。

**PROTOCOL_VALID_RATE**

- 意味：モデル出力の原文 / 訳文プロトコルタグが合法である割合です。
- 計算：`protocol_valid_turns / TURN_COUNT`。出力が合法な ASR のみの単位 `<src>...</src>`、または翻訳単位 `<src>...</src><tgt>...</tgt>` で始まり、タグが対応していて、順序が正しく、各フィールド内に `<src>`、`</src>`、`<tgt>`、`</tgt>` などのタグが入れ子で含まれていない場合に有効とします。この指標はタグ構造の合法性だけを見ます。閉じたプロトコル単位の後ろにタグ外の内容が続いていないかは `POSTPROCESSED_TURN_STOP_RATE` で評価します。

**RAW_TURN_STOP_RATE**

- 意味：生のデコード結果が、設定された生成停止トークンで正しく止まっている割合です。
- 計算：`raw_turn_stop_turns / TURN_COUNT`。生の出力が後処理後の出力の直後に `generation_stop` を続けている場合、そのターンは正しく停止したものとして扱います。

**RECORD_COUNT**

- 意味：今回の厳密なストリーミングテストで実際に評価したテストレコードの数です。
- 計算：`len(records)`。

**SRC_RELEASE_ACCURACY**

- 意味：正解データで原文側が書き起こしテキストを出すべきターンのうち、モデルも原文側で内容を出した割合です。
- 計算：`src_release_correct / SRC_RELEASE_TOTAL`。ここでは `<src>...</src>` が待機ではないかだけを見ており、出力された転写テキストそのものが正しいかは評価しません。

**SRC_RELEASE_TOTAL**

- 意味：正解データで原文側が内容を出すべきターンの数です。
- 計算：正解データの `<src>...</src>` が `<|wait|>` ではないターンを数えます。

**SRC_WAIT_ACCURACY**

- 意味：正解データで原文側が待つべきターンのうち、モデルも原文側で待機を出した割合です。
- 計算：`src_wait_correct / SRC_WAIT_TOTAL`。モデルの `<src>...</src>` が `<|wait|>` かどうかだけを見ます。

**SRC_WAIT_TOTAL**

- 意味：正解データで原文側が待つべきターンの数です。
- 計算：正解データの `<src>...</src>` が、前後の空白を除いたうえで `<|wait|>` と完全に一致するターンを数えます。

**TGT_RELEASE_ACCURACY**

- 意味：正解データで訳文側が翻訳を出すべきターンのうち、モデルも訳文側で内容を出した割合です。
- 計算：`tgt_release_correct / TGT_RELEASE_TOTAL`。ここでは `<tgt>...</tgt>` が待機ではないかだけを見ており、出力された翻訳の意味的な正しさは評価しません。

**TGT_RELEASE_TOTAL**

- 意味：正解データで訳文側が翻訳を出すべきターンの数です。
- 計算：正解データの `<tgt>...</tgt>` が `<|wait|>` ではないターンを数えます。

**TGT_WAIT_ACCURACY**

- 意味：正解データで訳文側が待つべきターンのうち、モデルも訳文側で待機を出した割合です。
- 計算：`tgt_wait_correct / TGT_WAIT_TOTAL`。モデルの `<tgt>...</tgt>` が `<|wait|>` かどうかだけを見ます。

**TGT_WAIT_TOTAL**

- 意味：正解データで訳文側が待つべきターンの数です。
- 計算：正解データの `<tgt>...</tgt>` が、前後の空白を除いたうえで `<|wait|>` と完全に一致するターンを数えます。

**TURN_COUNT**

- 意味：選択されたすべてのテストレコードで、実際に評価したアシスタントターンの総数です。
- 計算：`records` に含まれる、生成・評価対象となったアシスタント出力をすべて合計します。

#### ステップ 300 のテスト出力

- 許容窓幅：1.0 秒
- 以下は選択したテスト例です。左側が正解データ、右側がモデル出力です。

```text
Test Metrics
  - STEP: 300
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - POSTPROCESSED_TURN_STOP_RATE: 1.0000
  - PROTOCOL_VALID_RATE: 1.0000
  - RAW_TURN_STOP_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9443
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.2450
  - SRC_WAIT_TOTAL: 151
  - TGT_RELEASE_ACCURACY: 0.7248
  - TGT_RELEASE_TOTAL: 298
  - TGT_WAIT_ACCURACY: 0.7996
  - TGT_WAIT_TOTAL: 489
  - TURN_COUNT: 869

---

## Test Example 2 / 60

  - UID: EN_nLFyRxIRQBo_W000057
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

1. <src>These people are </src><tgt><|wait|></tgt>  -  <src>These people are </src><tgt><|wait|></tgt>
2. <src>completely rare, </src><tgt><|wait|></tgt>  -  <src>completely rare. </src><tgt><|wait|></tgt>
3. <src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>  -  <src>And they often </src><tgt>これは完全に珍しいんです。そして、</tgt>
4. <src>show up to </src><tgt><|wait|></tgt>  -  <src>show up </src><tgt><|wait|></tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>to completely revolution- </src><tgt><|wait|></tgt>
6. <src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>  -  <src>ize the world. </src><tgt>世界を完全に根底から覆す人たちがよく登場します。</tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>The personality </src><tgt><|wait|></tgt>
8. <src>Their personality is </src><tgt><|wait|></tgt>  -  <src>is something </src><tgt><|wait|></tgt>
9. <src>something of a </src><tgt>彼らの性格は</tgt>  -  <src>of a contradiction. </src><tgt>彼らの個性は、ある種の矛盾をはらんでいます。</tgt>
10. <src>contradiction. </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
11. <src>While they're </src><tgt><|wait|></tgt>  -  <src>While they're extroverted, </src><tgt><|wait|></tgt>
12. <src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>  -  <src>they also </src><tgt>外向的であるにもかかわらず、彼らは</tgt>
13. <src>they also hate </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
14. <src>meaningless conversations </src><tgt><|wait|></tgt>  -  <src>hate meaningless conversations. </src><tgt><|wait|></tgt>
15. <src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>  -  <src>And like </src><tgt>無意味な会話を嫌う、</tgt>
16. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>it gets straight to the </src><tgt><|wait|></tgt>
17. <src>get straight to the point. </src><tgt><|wait|></tgt>  -  <src>point. </src><tgt><|wait|></tgt>
18. <src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>  -  <src>They also love to </src><tgt>まっすぐ本題に入りたいのです。彼らはまた</tgt>
19. <src>play </src><tgt><|wait|></tgt>  -  <src>play the devil's advocate, </src><tgt><|wait|></tgt>
20. <src>the devil's advocate, and they </src><tgt><|wait|></tgt>  -  <src>and </src><tgt><|wait|></tgt>
21. <src><|wait|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>  -  <src>never shy away </src><tgt>逆説を好むし、</tgt>
22. <src>never shy away from a debate. </src><tgt><|wait|></tgt>  -  <src>from a debate. </src><tgt><|wait|></tgt>
23. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
24. <src><|wait|></src><tgt>議論を避けることはありません。</tgt>  -  <src>EHCPS </src><tgt>議論を避けることは決してありません。EHCPSの</tgt>
25. <src>ENTP stands for </src><tgt><|wait|></tgt>  -  <src>stand for. </src><tgt><|wait|></tgt>

---

## Test Example 9 / 60

  - UID: EN_nSOXneMb4Ec_W000365
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 3 wait windows before each target release.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>Meaningful individual </src><tgt><|wait|></tgt>  -  <src>Meaningful individual </src><tgt><|wait|></tgt>
3. <src>right, </src><tgt><|wait|></tgt>  -  <src>right, </src><tgt><|wait|></tgt>
4. <src>and the Supreme Court </src><tgt>有意义的个人权利，而最高法院</tgt>  -  <src>and the Supreme Court </src><tgt>有意义的个体权利，</tgt>
5. <src>came along </src><tgt><|wait|></tgt>  -  <src>came along last, </src><tgt><|wait|></tgt>
6. <src>last, not leading. </src><tgt><|wait|></tgt>  -  <src>not leading. </src><tgt><|wait|></tgt>
7. <src>And I don't think the courts want to be </src><tgt><|wait|></tgt>  -  <src>And I don't I don't think the courts want to be </src><tgt><|wait|></tgt>
8. <src><|wait|></src><tgt>是最后才介入的，不是引领者。我不认为</tgt>  -  <src>the </src><tgt>法院总是最后一个加入的。我个人认为，</tgt>
9. <src>the the vanguard of social </src><tgt><|wait|></tgt>  -  <src>vanard of social </src><tgt><|wait|></tgt>
10. <src>change </src><tgt><|wait|></tgt>  -  <src>change, </src><tgt><|wait|></tgt>
11. <src>these days, </src><tgt><|wait|></tgt>  -  <src>these days. </src><tgt><|wait|></tgt>
12. <src><|wait|></src><tgt>法院现在想成为社会变革的先锋，</tgt>  -  <src>But they rather </src><tgt>这些天似乎不想成为社会变革的典范。但他们更</tgt>
13. <src>but they rather reflect </src><tgt><|wait|></tgt>  -  <src>reflect the </src><tgt><|wait|></tgt>
14. <src>the consensus </src><tgt><|wait|></tgt>  -  <src>consensus. </src><tgt><|wait|></tgt>
15. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>That's already </src><tgt><|wait|></tgt>
16. <src>that's already emerged. </src><tgt>它们更倾向于反映已经形成的共识。</tgt>  -  <src>emerged. </src><tgt>选择反映已经形成的共识。</tgt>
17. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>So. </src><tgt><|wait|></tgt>
18. <src>So you have some </src><tgt><|wait|></tgt>  -  <src>You have </src><tgt><|wait|></tgt>
19. <src>federal judges </src><tgt><|wait|></tgt>  -  <src>some federal judges </src><tgt><|wait|></tgt>
20. <src><|wait|></src><tgt>所以，有些联邦法官……</tgt>  -  <src>who </src><tgt><|wait|></tgt>
21. <src>who. </src><tgt><|wait|></tgt>  -  <src>who </src><tgt><|wait|></tgt>

---

## Test Example 32 / 60

  - UID: ZH_B00041_S00155_W000028
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>家长需要</src><tgt>Parents need to</tgt>
2. <src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>  -  <src>做的是</src><tgt>do the following:</tgt>
3. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>用我们</src><tgt><|wait|></tgt>
4. <src>用我们深深的</src><tgt><|wait|></tgt>  -  <src>身上的爱</src><tgt>use the love in our own hearts</tgt>
5. <src>爱浇水、</src><tgt><|wait|></tgt>  -  <src>交世界，</src><tgt>to make love happen.</tgt>
6. <src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
7. <src>给足</src><tgt><|wait|></tgt>  -  <src>可以做</src><tgt><|wait|></tgt>
8. <src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>  -  <src>孩子心里的影响力。</src><tgt>That is the influence</tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>以内心，</src><tgt>that we want to instill in our children</tgt>
10. <src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>  -  <src>等他孩子</src><tgt><|wait|></tgt>
11. <src>慢慢长大。</src><tgt>them to grow slowly.</tgt>  -  <src>慢慢长大。</src><tgt>as they grow up: by teaching them how to share their hearts.</tgt>

---

## Test Example 40 / 60

  - UID: JA_Xv3zO_K9SuU_W000011
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>そうです。</src>  -  <src>そうですね、</src>
2. <src>そこで</src>  -  <src>そこで</src>
3. <src><|wait|></src>  -  <src>っていう</src>
4. <src>テキという設備寺が</src>  -  <src>設定</src>
5. <src>ありましたね。</src>  -  <src>済みか読みましたね</src>
6. <src>で、</src>  -  <src>って。</src>
7. <src><|wait|></src>  -  <src><|wait|></src>
8. <src>長井慶義氏の仕組み</src>  -  <src>細井親父の</src>
9. <src><|wait|></src>  -  <src>仕組みは</src>
10. <src>は五経、</src>  -  <src>元</src>
11. <src><|wait|></src>  -  <src>設定</src>
12. <src>設備寺、五比</src>  -  <src>済み？</src>
13. <src>です。</src>  -  <src>合図。</src>

---

## Test Example 48 / 60

  - UID: EN_n_COVPwr54I_W000006
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

1. <src>My name is </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>  -  <src>My name is Jinah Tree,</src><tgt>제 이름은 진아 트리예요. 저는</tgt>
3. <src>I am currently </src><tgt><|wait|></tgt>  -  <src>I am currently studying</src><tgt><|wait|></tgt>
4. <src><|wait|></src><tgt>저는 현재</tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
5. <src>studying a Bachelor of Finance </src><tgt><|wait|></tgt>  -  <src>AABX, back roll finance, and AABX</src><tgt>AABX, 배경 투자, 그리고 AABX를 지금 공부하고 있고요.</tgt>
6. <src>and a Bachelor of Psychology </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>of psychology, here at </src><tgt>심리학자들을 여기서</tgt>
8. <src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>  -  <src>Jianyu, </src><tgt><|wait|></tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt>Jianyu에서 배웠어요. 심리학자</tgt>
10. <src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>  -  <src>and in the future, </src><tgt><|wait|></tgt>
11. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>I want to go into corporate consulting </src><tgt>들도요. 미래에는 기업 자문가로</tgt>
12. <src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>  -  <src>or </src><tgt><|wait|></tgt>

---

## Test Example 54 / 60

  - UID: ZH_W0NbyT5Ak-A_W000071
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>弗洛伊德</src>  -  <src>Four in </src>
2. <src>首次觉知到</src>  -  <src>the subject had</src>
3. <src>那个现象：</src>  -  <src>solved that problem.</src>
4. <src>每当我们</src>  -  <src>But we, </src>
5. <src><|wait|></src>  -  <src>in our pursuit of </src>
6. <src>处于爱之中，</src>  -  <src>love, we</src>
7. <src>所谓的爱，</src>  -  <src>find</src>
8. <src>我们也</src>  -  <src>the other love</src>
9. <src>同时进入恨。</src>  -  <src>that has entered</src>
10. <src><|wait|></src>  -  <src>the heart</src>
11. <src>在早上的时候，</src>  -  <src>when we are seeking, that</src>
12. <src>它是爱；</src>  -  <src>is that love.</src>
13. <src>到了晚上，</src>  -  <src>The end result</src>
14. <src>它就变成恨。</src>  -  <src>is that, it turns into</src>
15. <src><|wait|></src>  -  <src>that</src>
16. <src>那个钟摆</src>  -  <src>love.</src>
17. <src><|wait|></src>  -  <src>It continues to grow</src>
18. <src>继续在移动。</src>  -  <src>and and.</src>
```


#### ステップ 5400 の最終テスト出力

```text
Test Metrics
  - STEP: 5400
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - POSTPROCESSED_TURN_STOP_RATE: 1.0000
  - PROTOCOL_VALID_RATE: 1.0000
  - RAW_TURN_STOP_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9610
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.7219
  - SRC_WAIT_TOTAL: 151
  - TGT_RELEASE_ACCURACY: 0.8725
  - TGT_RELEASE_TOTAL: 298
  - TGT_WAIT_ACCURACY: 0.8896
  - TGT_WAIT_TOTAL: 489
  - TURN_COUNT: 869

---

## Test Example 2 / 60

  - UID: EN_nLFyRxIRQBo_W000057
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

1. <src>These people are </src><tgt><|wait|></tgt>  -  <src>These people are </src><tgt><|wait|></tgt>
2. <src>completely rare, </src><tgt><|wait|></tgt>  -  <src>completely rare, </src><tgt><|wait|></tgt>
3. <src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>  -  <src>and they often </src><tgt>これらの人々は非常に稀です。そして、</tgt>
4. <src>show up to </src><tgt><|wait|></tgt>  -  <src>show up to </src><tgt><|wait|></tgt>
5. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
6. <src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>  -  <src>completely revolutionize the world. </src><tgt>世界の完全な革命を起こすためにしばしば現れます。</tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
8. <src>Their personality is </src><tgt><|wait|></tgt>  -  <src>Their personality is </src><tgt><|wait|></tgt>
9. <src>something of a </src><tgt>彼らの性格は</tgt>  -  <src>something of a contradiction. </src><tgt>彼らの性格は矛盾していることも特徴です。</tgt>
10. <src>contradiction. </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
11. <src>While they're </src><tgt><|wait|></tgt>  -  <src>While they're </src><tgt><|wait|></tgt>
12. <src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>  -  <src>extroverted, </src><tgt>外向的であるだけでなく、</tgt>
13. <src>they also hate </src><tgt><|wait|></tgt>  -  <src>they also hate </src><tgt><|wait|></tgt>
14. <src>meaningless conversations </src><tgt><|wait|></tgt>  -  <src>meaningless conversations </src><tgt><|wait|></tgt>
15. <src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>  -  <src><|wait|></src><tgt>無意味な会話を嫌い、</tgt>
16. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>and like to get straight to </src><tgt><|wait|></tgt>
17. <src>get straight to the point. </src><tgt><|wait|></tgt>  -  <src>the point. </src><tgt><|wait|></tgt>
18. <src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>  -  <src>They also love to </src><tgt>すぐ本題に入りたいと考えます。また、</tgt>
19. <src>play </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
20. <src>the devil's advocate, and they </src><tgt><|wait|></tgt>  -  <src>play the devil's advocate, </src><tgt><|wait|></tgt>
21. <src><|wait|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>  -  <src><|wait|></src><tgt>悪魔の代弁をするのも好きです。</tgt>
22. <src>never shy away from a debate. </src><tgt><|wait|></tgt>  -  <src>and they're never shy over a debate. </src><tgt><|wait|></tgt>
23. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
24. <src><|wait|></src><tgt>議論を避けることはありません。</tgt>  -  <src>ENTP stands for </src><tgt>そして議論が始まっても決して臆しません。ENTPとは、</tgt>
25. <src>ENTP stands for </src><tgt><|wait|></tgt>  -  <src>Extraverted, Intuitive, \, </src><tgt><|wait|></tgt>

---

## Test Example 9 / 60

  - UID: EN_nSOXneMb4Ec_W000365
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 3 wait windows before each target release.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
2. <src>Meaningful individual </src><tgt><|wait|></tgt>  -  <src>Meaningful, </src><tgt><|wait|></tgt>
3. <src>right, </src><tgt><|wait|></tgt>  -  <src>individual write, </src><tgt><|wait|></tgt>
4. <src>and the Supreme Court </src><tgt>有意义的个人权利，而最高法院</tgt>  -  <src>and the Supreme Court </src><tgt>有意义的个人著作，最高法院</tgt>
5. <src>came along </src><tgt><|wait|></tgt>  -  <src>came along </src><tgt><|wait|></tgt>
6. <src>last, not leading. </src><tgt><|wait|></tgt>  -  <src>last, not leading. </src><tgt><|wait|></tgt>
7. <src>And I don't think the courts want to be </src><tgt><|wait|></tgt>  -  <src>And I don't think the courts want to be </src><tgt><|wait|></tgt>
8. <src><|wait|></src><tgt>是最后才介入的，不是引领者。我不认为</tgt>  -  <src><|wait|></src><tgt>最后才跟进。我认为法院不想</tgt>
9. <src>the the vanguard of social </src><tgt><|wait|></tgt>  -  <src>the the vanguard of social </src><tgt><|wait|></tgt>
10. <src>change </src><tgt><|wait|></tgt>  -  <src>change </src><tgt><|wait|></tgt>
11. <src>these days, </src><tgt><|wait|></tgt>  -  <src>these days. </src><tgt><|wait|></tgt>
12. <src><|wait|></src><tgt>法院现在想成为社会变革的先锋，</tgt>  -  <src>But they rather </src><tgt>成为社会变革的前沿阵线。</tgt>
13. <src>but they rather reflect </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
14. <src>the consensus </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
15. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>reflect the consensus </src><tgt><|wait|></tgt>
16. <src>that's already emerged. </src><tgt>它们更倾向于反映已经形成的共识。</tgt>  -  <src>that's already emerged. </src><tgt>但它们更多是反映已经形成的共识。</tgt>
17. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>So, </src><tgt><|wait|></tgt>
18. <src>So you have some </src><tgt><|wait|></tgt>  -  <src>you have </src><tgt><|wait|></tgt>
19. <src>federal judges </src><tgt><|wait|></tgt>  -  <src>some federal judges </src><tgt><|wait|></tgt>
20. <src><|wait|></src><tgt>所以，有些联邦法官……</tgt>  -  <src>who </src><tgt>所以，你们有了一些联邦法官，</tgt>
21. <src>who. </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>

---

## Test Example 32 / 60

  - UID: ZH_B00041_S00155_W000028
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

1. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>家长需要</src><tgt>Parents need to</tgt>
2. <src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>  -  <src>做的是</src><tgt><|wait|></tgt>
3. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
4. <src>用我们深深的</src><tgt><|wait|></tgt>  -  <src>用我们深深的</src><tgt><|wait|></tgt>
5. <src>爱浇水、</src><tgt><|wait|></tgt>  -  <src>爱浇水、</src><tgt>show their love for the child, like watering a plant,</tgt>
6. <src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>  -  <src>施肥，</src><tgt>fertilizing it,</tgt>
7. <src>给足</src><tgt><|wait|></tgt>  -  <src>给足</src><tgt><|wait|></tgt>
8. <src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>  -  <src>孩子心理营养，</src><tgt>and giving them enough emotional nourishment.</tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src>并耐心</src><tgt><|wait|></tgt>
10. <src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>  -  <src>等他</src><tgt><|wait|></tgt>
11. <src>慢慢长大。</src><tgt>them to grow slowly.</tgt>  -  <src>慢慢长大。</src><tgt>And patiently waiting as they grow up.</tgt>

---

## Test Example 40 / 60

  - UID: JA_Xv3zO_K9SuU_W000011
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>そうです。</src>  -  <src>そうです。</src>
2. <src>そこで</src>  -  <src>そこで</src>
3. <src><|wait|></src>  -  <src><|wait|></src>
4. <src>テキという設備寺が</src>  -  <src>テキという設備寺が</src>
5. <src>ありましたね。</src>  -  <src>ありましたね。</src>
6. <src>で、</src>  -  <src>で、</src>
7. <src><|wait|></src>  -  <src><|wait|></src>
8. <src>長井慶義氏の仕組み</src>  -  <src>長井慶義氏の仕組み</src>
9. <src><|wait|></src>  -  <src><|wait|></src>
10. <src>は五経、</src>  -  <src>は五個</src>
11. <src><|wait|></src>  -  <src><|wait|></src>
12. <src>設備寺、五比</src>  -  <src>設備寺五個</src>
13. <src>です。</src>  -  <src>です。</src>

---

## Test Example 48 / 60

  - UID: EN_n_COVPwr54I_W000006
  - SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

1. <src>My name is </src><tgt><|wait|></tgt>  -  <src>My name is </src><tgt><|wait|></tgt>
2. <src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>  -  <src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그( Kerenath Dettig) 입니다.</tgt>
3. <src>I am currently </src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
4. <src><|wait|></src><tgt>저는 현재</tgt>  -  <src>I am currently studying </src><tgt>현재</tgt>
5. <src>studying a Bachelor of Finance </src><tgt><|wait|></tgt>  -  <src>a Bachelor of Finance </src><tgt><|wait|></tgt>
6. <src>and a Bachelor of Psychology </src><tgt><|wait|></tgt>  -  <src>and a Bachelor of Psychology </src><tgt>경영학 학사 학위와</tgt>
7. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
8. <src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>  -  <src>here at the ANU, </src><tgt>심리학 학사 학위를 안데번 대학교( ANU ) 에서</tgt>
9. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
10. <src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>  -  <src>and in the future, I want to go into </src><tgt>수강 중이고요, 나중에는</tgt>
11. <src><|wait|></src><tgt><|wait|></tgt>  -  <src><|wait|></src><tgt><|wait|></tgt>
12. <src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>  -  <src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>

---

## Test Example 54 / 60

  - UID: ZH_W0NbyT5Ak-A_W000071
  - SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

1. <src>弗洛伊德</src>  -  <src>弗洛伊德</src>
2. <src>首次觉知到</src>  -  <src>首次觉知到</src>
3. <src>那个现象：</src>  -  <src>那个现象。</src>
4. <src>每当我们</src>  -  <src>美登们</src>
5. <src><|wait|></src>  -  <src><|wait|></src>
6. <src>处于爱之中，</src>  -  <src>处于爱之中，</src>
7. <src>所谓的爱，</src>  -  <src>所谓的爱，</src>
8. <src>我们也</src>  -  <src><|wait|></src>
9. <src>同时进入恨。</src>  -  <src>我们也同时进入黑暗，</src>
10. <src><|wait|></src>  -  <src><|wait|></src>
11. <src>在早上的时候，</src>  -  <src>在早上的时候，</src>
12. <src>它是爱；</src>  -  <src>他是爱。</src>
13. <src>到了晚上，</src>  -  <src>到了晚上，</src>
14. <src>它就变成恨。</src>  -  <src>他就变成</src>
15. <src><|wait|></src>  -  <src>黑暗，</src>
16. <src>那个钟摆</src>  -  <src>那个钟表。</src>
17. <src><|wait|></src>  -  <src><|wait|></src>
18. <src>继续在移动。</src>  -  <src>继续在移动。</src>
```