# MakeSense: Sense Aware Simultaneous Speech Translation

MakeSense は、同時音声翻訳モデル向けに sense-aware な学習データと検証パイプラインを作るための研究・データ生成プロジェクトです。ASR / 書き起こしタスクにも対応します。

音声翻訳を、逐次的なマルチターン対話タスクとして扱うことを目指しています。音声がチャンクごとに届き、モデルはその時点で原文の書き起こしを出すか、訳文を出すか、あるいは追加の文脈を待つかを学習します。

現在のリポジトリでは、データセット構築 pipeline と学習データ生成ユーティリティを提供しています。ホットワード / 指定訳語のサポートと推論バックエンドは今後の作業です。

## プロジェクト概要

目標：ASR / 書き起こし能力も備えた、ストリーミング同時音声翻訳向けの omni / multimodal model を学習すること。

本プロジェクトは以下の論文から着想を得ています。
- 無限入力ウィンドウ / time-pressure 同時翻訳：[InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Model](https://arxiv.org/pdf/2503.02969)
- sense-unit translation：[SIMULSENSE: SENSE-DRIVEN INTERPRETING FOR EFFICIENT SIMULTANEOUS SPEECH TRANSLATION](https://arxiv.org/abs/2509.21932)

本プロジェクトでは：
- sense-unit detector、audio encoder、LLM backbone alignment をゼロから学習することは**しません**。
- モデルアーキテクチャは**変更しません**。無限時間のストリーミング翻訳は、実行時のスライディングウィンドウ型コンテキスト管理で扱います。
- ground-truth 形式に近いデータセットと pipeline 検証用の surface を作り、omni model が同時翻訳の戦略を学習できるようにします。

## 要件
### Python packages
```bash
pip install stanza jieba nagisa qwen-asr
pip install transformers peft torch torchvision torchaudio torchcodec bitsandbytes tensorboard --force-reinstall
```
- `qwen-asr` は古い `transformers` をインストールします。

### サブモジュール依存
- 単語アライナー：[TransAlign: Machine Translation Encoders are Strong Word Aligners, Too](https://github.com/bebing93/transalign)
- デフォルトのベースモデルには [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) を使います。

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

現在のワークフローは `examples/` 配下のステージスクリプトで実行します。各ステージは前段の cache を読み込み、新しいステージ cache を書き出します。既存の JSONL cache から再開することもできます。

実行前に、**各 example スクリプト冒頭の設定ブロック**を確認してください。よく使う項目は dataset/cache roots、model names、target languages、`ENABLE_THINKING`、`TOP_P`、`TOP_K`、必要に応じて `ENABLE_VISUALIZATION` です。

### 現在使えるもの

利用可能：
- 最終 pipeline-9 JSONL export まで実行できるデータセット構築 pipeline。
- `src/data_loader` による、最終データセットからの学習サンプル構築。
- `examples/train_lora.py` と `src/train` による初版 real-audio LoRA trainer。

TODO：
- [x] 高優先度：小さなサンプルで `examples/train_lora.py` の thin LoRA trainer path をテストし、conversation rendering、assistant-only loss 設定、1〜2 training steps が正しく動くことを確認する。
- [ ] `google/gemma-4-E2B-it` で full LoRA training を完了する。
- [ ] **次に高い優先度：** 学習済み streaming model を実行するための inference backend を追加する。
- [ ] training / inference context 向けに hot words と hot translations のサポートを追加する。

小規模検証結果（`google/gemma-4-E2B-it`, `train_examples: 96`）：
- tolerance window size: 1.0 s
- system prompt: Translate to Japanese, tolerance window size is 1
- 以下は小規模テストの結果です。左が ground truth、右が model output です。thinking は無効化済みですが、出力に thinking content がまだ混入しているため、追加調査が必要です。
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

デフォルトの LoRA 学習例は `google/gemma-4-E2B-it` を対象にし、Transformers multimodal model、PEFT LoRA、実音声 chunks、TensorBoard logging、JSONL metrics を使います。

dataset、model、LoRA、monitoring の設定は次のファイル冒頭で行います。

```text
examples/train_lora.py
```

学習を実行します。

```bash
PYTHONPATH=src python examples/train_lora.py
```

学習結果の LoRA adapter と monitoring ファイルは、設定した `OUTPUT_DIR` に書き込まれます。

```text
outputs/makesense_lora/
  adapter_config.json
  adapter_model.safetensors
  runs/
  train_metrics.jsonl
  sample_generations.jsonl
```

Sample generation では strict streaming evaluation を使います。各 assistant turn では、その時点までに見えている audio chunks だけを使います。評価するレコード数は `examples/train_lora.py` の `SAMPLE_EVALUATION_RECORD_COUNT` で制御します。

### Pipeline の実行順序

各ステージは次の順序で実行します。

```bash
export PYTHONPATH=src 

# 1. 必要に応じて、データセットの元データをダウンロード / 準備します。（ここでは Emilia dataset を使います。https://huggingface.co/datasets/amphion/Emilia-Dataset を参照してください）
python examples/pipeline_1_download_Emilia.py

# 2. dataset metadata から PipelineRecord cache shards を初期化します。
python examples/pipeline_2_initialize_cache.py

# 3a. 任意の omni ASR + translation 経路。
# one-pass multimodal translation の挙動を確認するときに使います。
python examples/pipeline_3_a_asr_translation_omni.py

# 3b-1. ASR-only path。
# source transcript artifacts を cache に書き込みます。
python examples/pipeline_3_b1_asr.py

# 3b-2. ASR cache から raw translation を生成します。
# デフォルトは text-only です。audio-assisted mode はスクリプト内で制御し、audio 対応 omni model が必要です。
python examples/pipeline_3_b2_asr_text_translation.py

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

# 9. 完了済み pipeline-8 cache state から最終データセットを収集 / export します。
python examples/pipeline_9_collect_dataset.py
```

推奨順序：

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

### 最終データセット出力

Pipeline 9 は次の構成で最終データセットを export します。

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
