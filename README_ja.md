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
- [x] **高優先度**：`google/gemma-4-E2B-it` の LoRA 学習を最後まで実行する。
  - **完了**：初期の `gemma-4-E2B-it` 大規模学習と評価は完了しています。[LoRA はここにあります](lora/Gemma-4-E2B-it_lr1e-4_r16_bs16_repeat12_epoch1_adamw_bnbnf4_checkpoint-15000)。詳細データは後半の結果にある指標セクションを参照してください。
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

## 大規模検証結果 (`google/gemma-4-E4B-it`, `train_examples: 21540`):

<!-- 
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

### 結果

#### 指標

ここで示す厳密なストリーミングテストの指標は、ストリーミング対話におけるプロトコル遵守とリリース判断を確認するためのものです。出力が完全なプロトコル単位（ASR のみの `<src>...</src>`、または翻訳の `<src>...</src><tgt>...</tgt>`）になっているか、各アシスタントターンで原文側 / 訳文側が待つべきか内容を出すべきかを見ます。ASR の文字単位の正確さや、翻訳の意味的な品質は測りません。

**PROTOCOL_ADHERENCE_RATE**

- 意味：モデル出力がプロトコルを完全に守ったターンの割合です。
- 計算：`protocol_adherent_turns / TURN_COUNT`。
- 合格する出力は、完全な `<src>...</src>` または `<src>...</src><tgt>...</tgt>` だけです。
- `<src>` / `<tgt>` の中にプロトコル tag を入れ子で含めてはいけません。
- 閉じたプロトコル単位の外側に空でない内容を置いてはいけません。
- フィールドが `<|wait|>` を含む場合、前後の空白を除いたフィールド内容は `<|wait|>` と完全に一致する必要があります。
- 末尾テキスト、カンマ連結、繰り返しプロトコルブロック、順序違い / 欠損 tag、wait と他の文字の混在は、すべてプロトコル非遵守として数えます。

すべての source / target wait/release accuracy 指標は、protocol-adherent なモデルターンだけを分母の基礎にします。プロトコル非遵守のモデルターンは `PROTOCOL_ADHERENCE_RATE` だけに影響します。Fixed-window と conservative の target 指標では、record-level window eligibility filter も使います。

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
  | 11 | `<src>saying. </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | -->
