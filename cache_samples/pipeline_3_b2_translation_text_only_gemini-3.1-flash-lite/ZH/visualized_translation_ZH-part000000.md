=== ZH_VJeW1Z4n0Qc_W000018 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: none
- cutoff_risk: no
- translation_style:
  - naturalness_target: casual, conversational tone
  - delivery_feel: relaxed, informative
  - main_warning: avoid overly formal or stiff phrasing
- source_rhythm_profile:
  - span: "然后在洋馆的后面呢"
    event: background_leadin
  - span: "再加上洋馆也没有开放"
    event: detail_after_main

asr:
- Chinese
  然后在洋馆的后面呢，其实有三排的，就是可以DIY互动的工作室跟体验的店家。但是因为今天我来的时间刚好是连假的最后一天，又是礼拜一，蛮多店都没开的，再加上洋馆也没有开放，所以我今天真的就是来这里单纯的逛逛。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
然后在洋馆的后面呢，其实有三排的，就是可以DIY互动的工作室跟体验的店家。但是因为今天我来的时间刚好是连假的最后一天，又是礼拜一，蛮多店都没开的，再加上洋馆也没有开放，所以我今天真的就是来这里单纯的逛逛。
- changes: none

translation:
- English
  And behind the Western-style house, there are actually three rows of studios for DIY activities and experience shops. But since I arrived on the last day of the long weekend, and it's a Monday, quite a few shops are closed. Plus, the Western-style house isn't open either, so I'm really just here for a stroll today.
- Japanese
  洋館の裏には、DIY体験ができる工房やショップが3列並んでいます。ただ、今日は連休の最終日で月曜日ということもあって、閉まっているお店が結構多くて。それに洋館も開いていないので、今日は本当にただぶらぶら歩きに来た感じです。
- Korean
  그리고 양관 뒤편에는 사실 DIY 체험을 할 수 있는 공방과 체험 매장들이 세 줄로 늘어서 있어요. 하지만 제가 온 오늘이 마침 연휴 마지막 날인 데다 월요일이라 문을 닫은 가게가 꽤 많더라고요. 게다가 양관도 개방하지 않아서, 오늘은 그냥 가볍게 둘러보러 왔어요.

---
=== ZH_Q0a8pjeI4HA_W000054 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: pause, emphasis
- cutoff_risk: no
- translation_style:
  - naturalness_target: conversational but persuasive
  - delivery_feel: encouraging and direct, like a speaker addressing an audience
  - main_warning: avoid sounding too academic or stiff; keep the flow natural and engaging
- source_rhythm_profile:
  - span: 那你就可以变成那百分之二十的人，去成就不一样的人生
    event: pause_before_detail
  - span: 可以知命、懂命、用命、在招命喽
    event: trailing_emphasis

asr:
- Chinese
  那你就可以变成那百分之二十的人，去成就不一样的人生，可以知命、懂命、用命、在招命喽。换句话说，荧幕前的各位朋友。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
那你就可以变成那百分之二十的人，去成就不一样的人生，可以知命、懂命、用命，在造命喽。换句话说，荧幕前的各位朋友。
- changes:
  - raw: 在招命喽
    audio_supported: 在造命喽
    reason: clear_audio

translation:
- English
  Then you can become that 20% of people who achieve a different kind of life—you can know your fate, understand your fate, use your fate, and create your fate. In other words, to all my friends in front of the screen.
- Japanese
  そうすれば、あなたは人生を切り開く20%の人になれます。自分の運命を知り、理解し、活用し、そして運命を自ら創り出すのです。言い換えれば、画面の前の皆さん。
- Korean
  그럼 당신은 상위 20%가 되어 남다른 인생을 성취할 수 있습니다. 자신의 운명을 알고, 이해하고, 활용하고, 더 나아가 운명을 개척하는 것이죠. 다시 말해, 화면 앞에 계신 여러분.

---
=== ZH_Y4xRc2amPxY_W000024 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: serious
- intensity: medium
- fluency: fluent
- audio_cues: emphasis
- cutoff_risk: no
- translation_style:
  - naturalness_target: natural, conversational, but informative
  - delivery_feel: instructional, serious
  - main_warning: avoid overly formal or stiff terminology; keep it natural
- source_rhythm_profile:
  - span: 就会消耗我们身体骨骼当中的矿物质，更多的靠物矿物质
    event: pause_before_detail
  - span: 就是因为什么？就是消耗了太多的矿物质
    event: trailing_emphasis

asr:
- Chinese
  就会消耗我们身体骨骼当中的矿物质，更多的靠物矿物质。所以呢，这个肥胖人往往都会有这种关节和软组织的问题，就是因为什么？就是消耗了太多的矿物质。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
就会消耗我们身体骨骼当中的矿物质，更多地靠矿物质。所以呢，这个肥胖人往往都会有这种关节和软组织的问题，就是因为什么？就是消耗了太多的矿物质。
- changes:
  - raw: 更多的靠物矿物质
    audio_supported: 更多地靠矿物质
    reason: clear_audio

translation:
- English
  It will consume the minerals in our bones—it relies more on minerals. So, obese people often have issues with joints and soft tissues. And why is that? It's because they've consumed too many minerals.
- Japanese
  私たちの骨に含まれるミネラルを消費してしまいます。ミネラルに頼る部分が大きくなるのです。ですから、肥満の人は関節や軟部組織の問題を抱えることがよくあります。なぜかというと、ミネラルを消費しすぎているからなのです。
- Korean
  우리 몸 뼈 속의 미네랄을 소모하게 됩니다. 미네랄에 더 의존하게 되는 거죠. 그래서 비만인 사람들은 관절이나 연조직 문제를 겪는 경우가 많은데, 그 이유가 무엇일까요? 바로 미네랄을 너무 많이 소모했기 때문입니다.

---
=== ZH_sQjhyfFvfLY_W000018 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: hesitant
- audio_cues: pause, stretch
- cutoff_risk: no
- translation_style:
  - naturalness_target: natural spoken
  - delivery_feel: instructional, slightly repetitive
  - main_warning: avoid over-polishing the stuttering/repetition
- source_rhythm_profile:
  - span: "把它丢进去之后呢，它会在它会找到这一个class，把它转变成为这一个class的的class"
    event: hesitated_addition
  - span: "好，这个这一个那个物件的class，好。"
    event: detail_after_main

asr:
- Chinese
  把它丢进去之后呢，它会在它会找到这一个class，把它转变成为这一个class的的class，好，这个这一个那个物件的class，好。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
把它丢进去之后呢，它会在它会找到这一个class，把它转变成为这一个class的的class，好，这个这一个那个物件的class，好。
- changes: none

translation:
- English
  Once you put it in, it will, it will find this class, and convert it into this class's, class. Right, this, this, that object's class. Right.
- Japanese
  それを中に入れたら、それが、そのクラスを見つけて、それをこのクラスの、クラスに変換します。そう、この、この、あのオブジェクトのクラスに。はい。
- Korean
  그걸 넣고 나면, 그게, 그게 이 클래스를 찾아서, 이걸 이 클래스의, 클래스로 바꿔줘요. 자, 이, 이, 그 객체의 클래스로. 자.

---
=== ZH_Y4xRc2amPxY_W000056 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: calm
- intensity: medium
- fluency: fluent
- audio_cues: pause
- cutoff_risk: no
- translation_style:
  - naturalness_target: conversational and clear
  - delivery_feel: informative and direct
  - main_warning: avoid over-simplifying the technical aspect of the diet
- source_rhythm_profile:
  - span: 我们采用了以吃脂脂肪、肥肉和油为主的饮食结构以后呢
    event: background_leadin
  - span: 第一个好处呢，就是我们减肥了。
    event: detail_after_main

asr:
- Chinese
  我们采用了以吃脂脂肪、肥肉和油为主的饮食结构以后呢，那给我们带来了巨大的好处。第一个好处呢，就是我们减肥了。

source_anchor_review:
- status: minimal_audio_supported
- source_anchor_used: minimally_audio_adjusted
- text:
我们采用了以吃脂肪、肥肉和油为主的饮食结构以后呢，那给我们带来了巨大的好处。第一个好处呢，就是我们减肥了。
- changes:
  - raw: 脂脂肪
    audio_supported: 脂肪
    reason: clear_audio

translation:
- English
  Once we adopted a diet based on eating fats, fatty meat, and oil, it brought us huge benefits. The first benefit is that we lost weight.
- Japanese
  脂質や脂身、油を主とした食事構造を取り入れたことで、私たちに大きなメリットがもたらされました。一つ目のメリットは、減量できたことです。
- Korean
  지방과 기름진 고기, 그리고 기름을 주식으로 하는 식단 구조를 채택한 이후, 우리에게는 엄청난 이점이 생겼습니다. 첫 번째 이점은 바로 체중이 줄었다는 것입니다.

---
=== ZH_NWf8Wc2GVvM_W000007 ===

scratchpad:
- register: neutral
- speaker_mode: explanation
- emotion: serious
- intensity: medium
- fluency: fluent
- audio_cues: none
- cutoff_risk: no
- translation_style:
  - naturalness_target: natural spoken English, Japanese, and Korean
  - delivery_feel: informative and steady
  - main_warning: do not over-interpret the terminology
- source_rhythm_profile:
  - span: 启示录和翡翠石板都曾经预测到
    event: background_leadin

asr:
- Chinese
  启示录和翡翠石板都曾经预测到，这十四万四千名光之工作者的到来，会在卡利年代结束时，将地球从黑暗势力的手中拯救出来。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
启示录和翡翠石板都曾经预测到，这十四万四千名光之工作者的到来，会在卡利年代结束时，将地球从黑暗势力的手中拯救出来。
- changes: none

translation:
- English
  The Book of Revelation and the Emerald Tablets both predicted that the arrival of these 144,000 lightworkers would save the Earth from the hands of dark forces at the end of the Kali Yuga.
- Japanese
  『ヨハネの黙示録』と『エメラルド・タブレット』はどちらも、14万4000人のライトワーカーの到来が、カリ・ユガの終わりに地球を闇の勢力の手から救い出すだろうと予言していました。
- Korean
  요한계시록과 에메랄드 타블렛은 모두 14만 4천 명의 빛의 일꾼들이 도래하여 칼리 유가의 끝에 지구를 어둠의 세력으로부터 구할 것이라고 예언했습니다.

---
=== ZH_Yu84L6YIP6A_W000010 ===

scratchpad:
- register: neutral
- speaker_mode: narration
- emotion: amused
- intensity: medium
- fluency: fluent
- audio_cues: laughter
- cutoff_risk: no
- translation_style:
  - naturalness_target: conversational and vivid
  - delivery_feel: storytelling, informal, lively
  - main_warning: avoid making the master's response sound too formal or polite; it needs to be blunt and funny.
- source_rhythm_profile:
  - span: “他说你成了个屁，哈哈哈哈哈！”
    event: trailing_emphasis

asr:
- Chinese
  说，我当时我只是看到月轮，我就跟师傅熊老师嘛，是我的师傅，我就汇报。二师傅，我成了。他说你成了什么了？我说我看到一个大月亮了，亮亮的，你看啊，一堂光。他说你成了个屁，哈哈哈哈哈！他就跟我说话不客气啊，你那个叫成了。

source_anchor_review:
- status: none
- source_anchor_used: raw_text
- text:
说，我当时我只是看到月轮，我就跟师傅熊老师嘛，是我的师傅，我就汇报。二师傅，我成了。他说你成了什么了？我说我看到一个大月亮了，亮亮的，你看啊，一堂光。他说你成了个屁，哈哈哈哈哈！他就跟我说话不客气啊，你那个叫成了。
- changes: none

translation:
- English
  So, at the time, I just saw the moon wheel, and I reported it to my master, Master Xiong. He's my master. I said, 'Master, I've succeeded!' He asked, 'Succeeded at what?' I said, 'I saw a big moon, bright and shining, look, a whole hall of light.' He said, 'You've succeeded at nothing, my foot!' Hahahaha! He doesn't hold back when he talks to me. 'You call that success?'
- Japanese
  その時私はただ月輪が見えただけで、師匠の熊先生、私の師匠なんですが、報告したんです。「師匠、できました！」と。すると師匠が「何ができたんだ？」とおっしゃるので、「大きな月が見えたんです。キラキラしてて、見てください、光に満ち溢れています」と答えました。すると師匠は「できたなんてお前、ちゃんちゃらおかしいわ！」と大笑いして。私に対してはいつも遠慮がないんです。「そんなの、できたのうちに入らないぞ」と。
- Korean
  그때 전 그냥 달무리를 보고는 제 스승님이신 슝 선생님께 보고를 드렸죠. 스승님께 '스승님, 저 해냈습니다!'라고요. 그러니 스승님이 '뭘 해냈다는 거냐?' 하시더군요. 그래서 '커다란 달을 봤습니다. 아주 밝게 빛나는, 보세요, 온 방이 빛으로 가득합니다'라고 했죠. 그랬더니 스승님이 '뭘 해내긴 개뿔, 하하하하!' 하시더군요. 저한테는 말씀을 참 가차 없이 하세요. '그걸 해냈다고 하는 거냐?' 하시면서요.

---
