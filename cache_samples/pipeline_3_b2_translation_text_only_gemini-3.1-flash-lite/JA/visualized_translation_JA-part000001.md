=== JA_B00001_S00527_W000010 ===

scratchpad:
- register: neutral
- speaker_mode: narration
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: none
- cutoff_risk: no
- translation_style:
  - naturalness_target: conversational and narrative
  - delivery_feel: clear and steady
  - main_warning: over-formalizing the casual dialogue
- source_rhythm_profile:
  - span: 岩瀬氏の部下が牢屋に入ったとき
    event: background_leadin

asr:
- Japanese
  すみません、さなえさん、入りますよ。今空気を入れ替えますからね。岩瀬氏の部下が牢屋に入ったとき、さなえさんの姿は消えていた。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
すみません、さなえさん、入りますよ。今空気を入れ替えますからね。岩瀬氏の部下が牢屋に入ったとき、さなえさんの姿は消えていた。
- changes: none

translation:
- Chinese
  不好意思，早苗小姐，我进来了。我现在要通一下风。当岩濑先生的部下走进牢房时，早苗小姐的身影已经消失了。
- English
  Excuse me, Sanae-san, I'm coming in. I'm going to air out the room now. When Mr. Iwase's subordinate entered the cell, Sanae-san was gone.
- Korean
  죄송합니다, 사나에 씨, 들어갈게요. 지금 공기 좀 환기할게요. 이와세 씨의 부하가 감옥에 들어갔을 때, 사나에 씨의 모습은 사라지고 없었다.

---
=== JA_C9lAGdq4pM8_W000001 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: none
- cutoff_risk: possible
- translation_style:
  - naturalness_target: natural spoken
  - delivery_feel: informative and clear
  - main_warning: Do not over-correct the source or finish the sentence prematurely.
- source_rhythm_profile:
  - span: 内閣府は19日
    event: pause_before_detail

asr:
- Japanese
  どうも政治いろいろの学ぶです。内閣府が行った外交に関する世論調査の結果について、自立通信が記事にしています。自立通信の記事を引用します。内閣府は19日。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
どうも政治いろいろの学ぶです。内閣府が行った外交に関する世論調査の結果について、時事通信が記事にしています。時事通信の記事を引用します。内閣府は19日。
- changes:
  - raw: 自立通信
    audio_supported: 時事通信
    reason: clear_audio
  - raw: 自立通信
    audio_supported: 時事通信
    reason: clear_audio

translation:
- Chinese
  大家好，我是“政治种种”的Manabu。关于内阁府进行的有关外交的民意调查结果，时事通信社刊登了相关报道。我来引用一下时事通信社的报道。内阁府于19日……
- English
  Hello, this is Manabu from 'Seiji Iroiro' (Politics Various). Jiji Press has published an article regarding the results of a public opinion poll on diplomacy conducted by the Cabinet Office. I will quote from the Jiji Press article. On the 19th, the Cabinet Office...
- Korean
  안녕하세요, '정치 이모저모'의 마나부입니다. 내阁부가 실시한 외교 관련 여론조사 결과에 대해 지지통신이 기사를 실었습니다. 지지통신의 기사를 인용하겠습니다. 내阁부는 19일...

---
=== JA_B00001_S01637_W000020 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: none
- cutoff_risk: no
- translation_style:
  - naturalness_target: natural, conversational tone
  - delivery_feel: clear and informative, like a friendly teacher
  - main_warning: do not over-formalize the term "mono" (things/genre)
- source_rhythm_profile:
  - span: 例えばホラーもの、S.F.もの、アクションものなどなど。
    event: detail_after_main

asr:
- Japanese
  漫画にもいろいろなジャンル、種類がありますね。これを砕けた会話ではなんとかものと言います。例えばホラーもの、S.F.もの、アクションものなどなど。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
漫画にもいろいろなジャンル、種類がありますね。これを砕けた会話ではなんとかものと言います。例えばホラーもの、S.F.もの、アクションものなどなど。
- changes: none

translation:
- Chinese
  漫画也有各种各样的类型和种类呢。在随意的谈话中，我们通常会用“某某物”来称呼它们。比如恐怖物、科幻物、动作物等等。
- English
  There are many different genres and types of manga, aren't there? In casual conversation, we often refer to them with the suffix '-mono' (thing). For example, horror-mono, sci-fi-mono, action-mono, and so on.
- Korean
  만화에도 여러 장르와 종류가 있죠. 이걸 편한 대화에서는 '뭐뭐물'이라고 부릅니다. 예를 들면 호러물, SF물, 액션물 등등이 있죠.

---
