# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense は、同時音声翻訳モデルのために、意味単位を意識した学習データと検証フローを構築する研究・データ生成向けプロジェクトです。ASR / 音声書き起こしにも対応します。

本プロジェクトの目的は、音声翻訳を増分的なマルチターン対話タスクとして扱えるようにすることです。音声は一定の区間ごとに入力され、モデルはその時点で、原文の書き起こしを出力すべきか、訳文を出力すべきか、あるいはまだ情報が足りないため待つべきかを学習します。

現時点では、このリポジトリは主にデータセット構築 pipeline と学習データ生成ツールを提供しています。ホットワード / 推奨訳語への対応や推論バックエンドは、今後の開発項目です。

## プロジェクト概要

目的: ストリーミング同時音声翻訳の能力を持ち、さらに ASR / 音声書き起こしにも対応できる、オムニモーダル / マルチモーダルモデルを学習すること。

本プロジェクトは、以下の研究から着想を得ています。

* 無限長入力 window / time-pressure に基づく同時翻訳: [InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
* sense-unit translation: [SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

本プロジェクトでは、次の方針を取ります。

* 意味単位検出器、音声エンコーダ、LLM backbone のアラインメントモジュールをゼロから学習することはしません。
* モデルアーキテクチャは変更しません。無限長のストリーミング翻訳は、実行時のスライディングウィンドウ型コンテキスト管理によって扱います。
* 一方で、ground truth に近い形式のデータセットを構築し、pipeline の検証に使えるインターフェースと中間結果を提供します。これにより、オムニモーダルモデルが同時翻訳の出力方針を学習できるようにします。

## 環境要件

### Python 依存パッケージ

```bash
pip install stanza jieba nagisa qwen-asr transformers peft torch torchvision torchaudio unsloth
```

### サブモジュール依存

* 単語アラインメントツール: [TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
* デフォルトのベースモデルには [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) を使用します。

## Pipeline

### 原言語 / 書き起こし側

1. metadata に基づいて cache records を初期化する
2. 必要に応じて ASR による書き起こしを行う
3. forced alignment を実行する
4. time pressure に基づいて、原言語の意味単位を分割する

### 目標言語 / 翻訳側

1. 初期翻訳を生成する
2. 翻訳を再構成する
3. 目標言語のプレーンテキストを意味単位に分割する
4. 目標言語を基準として、対応する原言語部分をマッピングする
5. 最終データセットを収集してエクスポートする

## 使い方: データセット pipeline 全体を実行する

現在のワークフローは、`examples/` ディレクトリ内の各ステージ用スクリプトによって実行されます。各ステージは前段階の cache を読み込み、新しいステージの cache を書き出します。また、既存の JSONL cache の状態から処理を再開することもできます。

実行前に、必ず**各 example スクリプト冒頭の設定ブロック**を確認してください。よく使う設定項目には、データセット / cache のルートディレクトリ、モデル名、目標言語、`ENABLE_THINKING`、`TOP_P`、`TOP_K`、また必要に応じて `ENABLE_VISUALIZATION` などがあります。

### 現在利用可能な機能

現時点で利用できる機能は以下のとおりです。

* 最終的な pipeline-9 JSONL エクスポートまで実行可能なデータセット構築 pipeline
* `src/data_loader` による、最終データセットからの学習サンプル構築
* `examples/train_lora.py` と `src/train` による軽量 LoRA SFT 学習エントリーポイント
  ただし、現時点ではテキスト dry-run のみを対象としており、`<|audio|>` はテキスト上のプレースホルダーとして扱われます。

今後の TODO:

* [ ] **高優先度:** ごく小規模なサンプルで `examples/train_lora.py` の軽量 LoRA 学習フローをテストし、conversation のレンダリング、assistant-only loss の設定、1〜2 step の学習が正常に動作することを確認する。
* [ ] **高優先度:** 学習器の sanity check が完了した後、`Qwen/Qwen2.5-Omni-3B` に対して LoRA 学習を実行する。
* [ ] **中優先度:** 学習済みストリーミングモデルを実行するための推論バックエンドを追加する。
* [ ] 学習および推論コンテキストに、ホットワードと推奨訳語のサポートを追加する。

### LoRA 学習エントリーポイント

LoRA 学習は、以下のコマンドから実行できます。

```bash
PYTHONPATH=src python examples/train_lora.py
```

### Pipeline の実行順序

各ステージは、以下の順序で実行してください。

```bash
export PYTHONPATH=src 

# 1. 必要に応じて、データセットの元データをダウンロード / 準備する。
#    ここでは Emilia データセットを使用する。詳細は https://huggingface.co/datasets/amphion/Emilia-Dataset を参照。
python examples/pipeline_1_download_Emilia.py

# 2. データセット metadata に基づいて PipelineRecord cache shards を初期化する。
python examples/pipeline_2_initialize_cache.py

# 3a. 任意: omni ASR + translation 経路。
#     ワンショットのマルチモーダル翻訳動作を検証したい場合に使用する。
python examples/pipeline_3_a_asr_translation_omni.py

# 3b-1. ASR のみを実行する経路。
#       このステップでは、cache に原言語の書き起こし結果を書き込む。
python examples/pipeline_3_b1_asr.py

# 3b-2. ASR cache に基づいて初期翻訳を生成する。
#       デフォルトはテキストのみのモード。音声補助モードはスクリプト内の設定で切り替える。
python examples/pipeline_3_b2_asr_text_translation.py

# 4. 原言語の書き起こし結果に対して forced alignment を実行する。
python examples/pipeline_4_forced_alignment.py

# 5. time pressure に基づいて原言語の意味単位を分割する。
python examples/pipeline_5_asr_segmentation.py

# 6. 翻訳を再構成する。
python examples/pipeline_6_translation_reconstruction.py

# 7. 目標言語のプレーンテキストを意味単位に分割する。
python examples/pipeline_7_pure_text_segmentation.py

# 8. 目標言語の意味単位を、原言語 token ids にマッピングする。
python examples/pipeline_8_target_centric_mapping.py

# 9. 完了済みの pipeline-8 cache 状態から、最終データセットを収集してエクスポートする。
python examples/pipeline_9_collect_dataset.py
```

推奨される実行順序は以下です。

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

### 最終データセットの出力

Pipeline 9 では、最終データセットが以下のようなディレクトリ構成でエクスポートされます。

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

## 出力形式

### ストリーミングモデルの出力

```text
<src>(書き起こしテキスト)</src><tgt>(目標言語の翻訳テキスト)</tgt>
```

原言語の書き起こし、または目標言語の翻訳を安定して生成するには情報がまだ足りない場合、モデルは `<|wait|>` を出力できます。

### Conversation 形式

```text
system
[system prompts]
[hot words / task context]
user
<|audio|>
assistant
<src>(書き起こしテキスト、または <|wait|>)</src><tgt>(目標言語の翻訳テキスト、または <|wait|>)</tgt>
user
<|audio|>
assistant
<src>(次の区間の書き起こしテキスト、または <|wait|>)</src><tgt>(次の区間の目標言語翻訳、または <|wait|>)</tgt>
...
```
