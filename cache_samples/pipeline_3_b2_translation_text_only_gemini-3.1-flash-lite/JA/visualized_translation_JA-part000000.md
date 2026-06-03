=== JA_ACoDViff5So_W000029 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: hesitant
- audio_cues: pause, stretch
- cutoff_risk: yes
- translation_style:
  - naturalness_target: conversational and natural
  - delivery_feel: hesitant, explanatory, and trailing off
  - main_warning: avoid over-smoothing the hesitation and the trailing off
- source_rhythm_profile:
  - span: まあえっとこれがいくつかの特別な状態があるんですけれども
    event: background_leadin
  - span: 例えば重要なポイントは
    event: trailing_emphasis

asr:
- Japanese
  まあえっとこれがいくつかの特別な状態があるんですけれども、性格あるんですけれども、例えば重要なポイントは。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
まあ、えっと、これがいくつかの特別な状態があるんですけれども、性格があるんですけれども、例えば重要なポイントは。
- changes:
  - raw: 性格あるんですけれども
    audio_supported: 性格があるんですけれども
    reason: clear_audio

translation:
- Chinese
  嗯，那个，这有一些特殊的状态，也有一些性格，比如重要的点是……
- English
  Well, um, there are some special states, and some personalities, for example, the important point is...
- Korean
  음, 그러니까 이게 몇 가지 특별한 상태가 있는데요, 성격이 있는데요, 예를 들어 중요한 포인트는요.

---
=== JA__gKKQYSi4mg_W000178 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: hesitant
- audio_cues: pause, emphasis
- cutoff_risk: no
- translation_style:
  - naturalness_target: casual, conversational
  - delivery_feel: encouraging, informative
  - main_warning: avoid over-smoothing the speaker's hesitation and natural self-correction
- source_rhythm_profile:
  - span: 例えば災害の時たあのあこんなデータあればなって思ってたものとか
    event: pause_before_detail

asr:
- Japanese
  と今までのオープンデータだけだと、例えば災害の時たあのあこんなデータあればなって思ってたものとかももしかしたらあるかもしれないのでぜひ探してみてください。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
今までのオープンデータだけだと、例えば災害の時、あんなデータあればなって思ってたものとかももしかしたらあるかもしれないので、ぜひ探してみてください。
- changes:
  - raw: と今までの
    audio_supported: 今までの
    reason: clear_audio
  - raw: たあのあこんな
    audio_supported: あんな
    reason: clear_audio

translation:
- Chinese
  如果仅靠现有的开放数据，可能还会有你曾经在比如灾害发生时，心想“要是能有那种数据就好了”的东西，所以请务必试着找找看。
- English
  If you only look at the open data we've had so far, you might actually find something that you once wished existed, for instance, during a disaster. So please, take a look and see what you can find.
- Korean
  지금까지의 오픈 데이터만으로는, 예를 들어 재난 시에 '이런 데이터가 있었으면 좋았을 텐데'라고 생각했던 것이 어쩌면 있을지도 모르니 꼭 한번 찾아보세요.

---
=== JA_055Z9Ti9z9Y_W000045 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: none
- cutoff_risk: no
- translation_style:
  - naturalness_target: natural spoken
  - delivery_feel: clear and instructional
  - main_warning: do not over-interpret technical terms
- source_rhythm_profile:
  - span: ギアの先に役ねじのナットがついているっていうことですね
    event: pause_before_detail

asr:
- Japanese
  これがギアです。ギアが緩むと芯が上げ下げできなくなってしまうので、ギアの先に役ねじのナットがついているっていうことですね。はい、分解完了。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
これがギアです。ギアが緩むと芯が上げ下げできなくなってしまうので、ギアの先に逆ねじのナットがついているっていうことですね。はい、分解完了。
- changes:
  - raw: 役ねじ
    audio_supported: 逆ねじ
    reason: clear_audio

translation:
- Chinese
  这是齿轮。如果齿轮松了，笔芯就没法上下移动，所以齿轮尖端装有一个反向螺纹的螺母。好了，拆解完成。
- English
  This is the gear. If the gear loosens, the lead won't move up and down, so there's a reverse-threaded nut at the end of the gear. Alright, disassembly complete.
- Korean
  이게 기어입니다. 기어가 느슨해지면 심이 오르내릴 수 없게 되기 때문에, 기어 끝에 역나사 너트가 달려 있다는 거죠. 네, 분해 완료.

---
=== JA__gKKQYSi4mg_W000167 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: pause
- cutoff_risk: possible
- translation_style:
  - naturalness_target: conversational and clear
  - delivery_feel: informative and professional
  - main_warning: avoid over-completing the sentence structure
- source_rhythm_profile:
  - span: あの測量したデータになります
    event: background_leadin
  - span: これは奈良県の工事なんですけど
    event: detail_after_main

asr:
- Japanese
  あの測量したデータになります。こういったデータであったり、これは奈良県の工事なんですけど。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
あの測量したデータになります。こういったデータであったり、これは奈良県の工事なんですけど。
- changes: none

translation:
- Chinese
  这是测量数据。像这样的数据，或者说，这是奈良县的一个工程项目。
- English
  This is the survey data. Data like this, or, this is a construction project in Nara Prefecture.
- Korean
  이것은 측량한 데이터입니다. 이런 데이터라든가, 이건 나라현의 공사 현장인데요.

---
=== JA_B8if86uiSic_W000033 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: none
- cutoff_risk: no
- translation_style:
  - naturalness_target: natural, spoken
  - delivery_feel: instructional and clear
  - main_warning: avoid over-formality
- source_rhythm_profile:
  - span: えっとケースから紙を引き出し、お好みの長さに切ってご使用くださいと書いてあります。
    event: pause_before_detail

asr:
- Japanese
  じゃあ戻したロール紙をここに入れます。えっとケースから紙を引き出し、お好みの長さに切ってご使用くださいと書いてあります。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
じゃあ戻したロール紙をここに入れます。えっとケースから紙を引き出し、お好みの長さに切ってご使用くださいと書いてあります。
- changes: none

translation:
- Chinese
  那么，把卷回去的卷纸放进这里。嗯，上面写着“从盒子里拉出纸张，切成您喜欢的长度后使用”。
- English
  Okay, I'll put the rolled paper back in here. Uh, it says, "pull the paper out of the case and cut to your preferred length before use."
- Korean
  자, 되감은 롤지를 여기 넣을게요. 음, 케이스에서 종이를 꺼내 원하는 길이로 잘라서 사용하라고 적혀 있네요.

---
=== JA_Y-0K120KsxA_W000042 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: excited
- intensity: medium
- fluency: fluent
- audio_cues: emphasis
- cutoff_risk: yes
- translation_style:
  - naturalness_target: conversational and enthusiastic
  - delivery_feel: energetic, like a product recommendation or tech review
  - main_warning: do not over-smooth the cut-off at the end
- source_rhythm_profile:
  - span: 1100円でまあ使えてしまうということで
    event: background_leadin
  - span: この車内ワイファイとエアボックスを連携することによって
    event: pause_before_detail

asr:
- Japanese
  1100円でまあ使えてしまうということで、この車内ワイファイとエアボックスを連携することによって、もう最強のオーディオができるようになるとまあいうことで、今まで。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
1100円でまあ使えてしまうということで、この車内ワイファイとエアボックスを連携することによって、もう最強のオーディオができるようになるとまあいうことで、今まで。
- changes: none

translation:
- Chinese
  只要1100日元就能用，通过把车载Wi-Fi和AirBox联动起来，就能打造出最强的音频系统，所以说，直到现在……
- English
  For just 1100 yen, you can actually use it, and by linking this in-car Wi-Fi with the AirBox, you can create the ultimate audio setup, so, up until now...
- Korean
  1100엔으로 사용할 수 있다는 건데, 이 차량용 와이파이랑 에어박스를 연동하면 최강의 오디오 시스템을 만들 수 있게 된다는 거죠. 그래서 지금까지...

---
=== JA_B4lnt-FtXPy_W000004 ===

scratchpad:
- register: formal
- speaker_mode: narration
- emotion: serious
- intensity: medium
- fluency: fluent
- audio_cues: pause
- cutoff_risk: yes
- translation_style:
  - naturalness_target: professional broadcast style
  - delivery_feel: clear and informative
  - main_warning: avoid over-completing the sentence where it cuts off
- source_rhythm_profile:
  - span: 文在寅大統領の革新となる経済政策基本路線、所得主導成長について。
    event: pause_before_detail

asr:
- Japanese
  5年間の国債運営成果を報告した。青瓦台のパクスヒョン国民総統秘書官は、文在寅大統領の革新となる経済政策基本路線、所得主導成長について。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
5年間の国政運営成果を報告した。青瓦台のパク・スヒョン国民疎通首席秘書官は、文在寅大統領の核心となる経済政策基本路線、所得主導成長について。
- changes:
  - raw: 国債
    audio_supported: 国政
    reason: clear_audio
  - raw: パクスヒョン国民総統秘書官
    audio_supported: パク・スヒョン国民疎通首席秘書官
    reason: clear_audio
  - raw: 革新
    audio_supported: 核心
    reason: clear_audio

translation:
- Chinese
  报告了五年来的国政运营成果。青瓦台国民沟通首席秘书朴洙贤就文在寅总统的核心经济政策基本路线——收入主导增长进行了说明。
- English
  The results of the five-year state administration were reported. Park Soo-hyun, Senior Presidential Secretary for Public Communication at the Blue House, addressed the core economic policy line of President Moon Jae-in, income-led growth.
- Korean
  5년간의 국정 운영 성과를 보고했습니다. 청와대 박수현 국민소통수석비서관은 문재인 대통령의 핵심 경제 정책 기본 노선인 소득주도성장에 대해 (말했습니다).

---
