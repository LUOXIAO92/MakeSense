# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9624
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3974
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.8040
  - TGT_RELEASE_TOTAL: 495
  - TGT_WAIT_ACCURACY: 0.6364
  - TGT_WAIT_TOTAL: 374
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1363.0640
  - PROCESS_TIME_MS_P50: 1307.0750
  - PROCESS_TIME_MS_P95: 2106.0800
  - PROCESS_TIME_MS_MAX: 3840.3210

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要切肤，</src><tgt>肌に直接触れる</tgt>` | 1247 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>是容易的。</src><tgt>のは簡単です。</tgt>` | 1019 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src>但是</src><tgt>しかし、</tgt>` | 1059 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有</src><tgt><\|wait\|></tgt>` | 1064 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导</src><tgt>師匠が指導して</tgt>` | 1106 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 882 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>如何处于中间，</src><tgt>どうやって中間に立つか、</tgt>` | 2234 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>ですから</tgt>` | 1511 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>需要反</src><tgt><\|wait\|></tgt>` | 624 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt>反転して</tgt>` | 1878 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师傅。</src><tgt>師匠になる必要があります。</tgt>` | 1980 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt>从一开始</tgt>` | 814 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>仲がまだ</src><tgt><\|wait\|></tgt>` | 1210 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>他们关系还是一年级呢。</tgt>` | 1605 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>あの時点で</src><tgt>那时候</tgt>` | 1273 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう密告、</src><tgt>就密告、</tgt>` | 969 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1353 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対ずして</src><tgt>对选举</tgt>` | 1777 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>たててあげると</src><tgt>进行过对质，</tgt>` | 603 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>十年経っても</src><tgt>十年过去了，</tgt>` | 1893 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>対立した。</src><tgt>他们还是对立。</tgt>` | 1906 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我的</src><tgt><\|wait\|></tgt>` | 1242 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>送纸的地方，</src><tgt>The place I send my paper,</tgt>` | 1115 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个邮行</src><tgt><\|wait\|></tgt>` | 1246 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>很大，</src><tgt>the post office is huge,</tgt>` | 1402 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt>and then</tgt>` | 1091 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放个</src><tgt><\|wait\|></tgt>` | 681 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>热汤儿，</src><tgt>I'm putting out some hot soup,</tgt>` | 2272 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1709 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>这里，</src><tgt>here,</tgt>` | 1799 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 773 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>热汤儿。</src><tgt>these hot soups.</tgt>` | 1804 |

---

### Test Example 4 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 </src><tgt>これ、</tgt>` | 993 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt>これ、</tgt>` | 786 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>저열한 일일 수 있지만 </src><tgt>あまりにも低レベルなことかもしれないけど、</tgt>` | 1449 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt>本当に菩薩の</tgt>` | 1134 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 자기 가 </src><tgt>ことじゃなくて、</tgt>` | 1102 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>菩薩なのに夢</tgt>` | 927 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>피라고 보이 고 </src><tgt>にでも見えて、</tgt>` | 2180 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>私だけが</tgt>` | 1822 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>보살 로 보일 피라고 보이 서 </src><tgt>菩薩に見える夢だと</tgt>` | 1913 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>우주 가진다. 나한테 </src><tgt>宇宙がそう判断している。私にとって</tgt>` | 1575 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>보살 이란데. </src><tgt>菩薩とは、</tgt>` | 1047 |

---

### Test Example 5 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大抵</src><tgt>通常</tgt>` | 1021 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>从这里开始，</tgt>` | 856 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 876 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>我才开始的，</tgt>` | 792 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>方法、</src><tgt>方法、</tgt>` | 1325 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt>高根、</tgt>` | 1420 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1221 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt>塞尚、</tgt>` | 1280 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1818 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1927 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1117 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt>伦纳等人的画，</tgt>` | 1443 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>자 저는 </src><tgt>Well,</tgt>` | 974 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 843 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 682 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설프고 용심이가 </src><tgt><\|wait\|></tgt>` | 1543 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞이 는 건데요. 야 </src><tgt>I'm mixing up my sword intent and my dragon intent. Oh,</tgt>` | 2460 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1709 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 2007 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>해행으로 </src><tgt><\|wait\|></tgt>` | 1958 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 죽입니다, </src><tgt><\|wait\|></tgt>` | 915 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` | 890 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` | 1039 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop into your body </src><tgt>进入你的身体，</tgt>` | 1247 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1427 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>where does the tension </src><tgt>紧张感</tgt>` | 1340 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>从哪里开始？是什么？</tgt>` | 1310 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a head? </src><tgt>是头吗？</tgt>` | 1219 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it a tension in your chest? </src><tgt>是胸口有紧张吗？</tgt>` | 1983 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>Or is the body </src><tgt>还是身体</tgt>` | 1931 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>landing? </src><tgt>在沉？</tgt>` | 1883 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>Which way are you using? </src><tgt>你是在哪个方向使用？</tgt>` | 1939 |

---

### Test Example 8 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1191 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>砂を洗い流した後は、</tgt>` | 1714 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>内部的盐碱</src><tgt>内部の</tgt>` | 706 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了</src><tgt>塩基性のエネルギーも弱まります。</tgt>` | 1638 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>呢。然后</src><tgt>そして、</tgt>` | 1085 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在</src><tgt><\|wait\|></tgt>` | 1647 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 968 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 1637 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>运行状态。</src><tgt>比較的低エネルギーな稼働状態にとどまります。</tgt>` | 2241 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | 1843 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>抑郁状态。</src><tgt>うつ状態です。</tgt>` | 2003 |

---

### Test Example 9 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>また</src><tgt><\|wait\|></tgt>` | 1162 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>またちょっと距離が</src><tgt><\|wait\|></tgt>` | 864 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じで</src><tgt>又会有点距离感，</tgt>` | 1306 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>大将が</src><tgt>大将</tgt>` | 636 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>あるこうだとかね、</src><tgt>会说“啊，</tgt>` | 1473 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>回避したい方って</src><tgt>想躲开的话</tgt>` | 1173 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行きに行き出したが</src><tgt>会马上就跑过去，</tgt>` | 2101 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>し、</src><tgt><\|wait\|></tgt>` | 1554 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>行き始めて</src><tgt>跑起来，</tgt>` | 676 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>ととこに</src><tgt><\|wait\|></tgt>` | 1966 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>ととしかこうが強いので</src><tgt>因为跑起来很强，所以</tgt>` | 2152 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なので</src><tgt>所以</tgt>` | 1794 |

---

### Test Example 10 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1243 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is</tgt>` | 1342 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 997 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱</src><tgt><\|wait\|></tgt>` | 1537 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>浇水，</src><tgt>water them with our deep love.</tgt>` | 1404 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 2096 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1542 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>给足孩子心灵营养，</src><tgt>So provide your child with the nourishment they need for their spirit,</tgt>` | 1081 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1717 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>跟耐心等</src><tgt><\|wait\|></tgt>` | 1889 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>孩子慢慢长大。</src><tgt>and be patient as they grow.</tgt>` | 2051 |

---

### Test Example 11 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1265 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1049 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复一下。</tgt>` | 1167 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learn the answer </src><tgt>记住答案</tgt>` | 1115 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>to repeat. Find what you're good at. </src><tgt>来重复。找到你擅长的地方。</tgt>` | 1757 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>And do more of </src><tgt>多做</tgt>` | 609 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it. And while you're not </src><tgt>它。虽然你</tgt>` | 2073 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>good at it, </src><tgt>还不够好，</tgt>` | 1751 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>get the people around you to help you with </src><tgt>让周围的人来帮你</tgt>` | 2280 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1877 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>it, and and tell the next time </src><tgt>，下次</tgt>` | 2052 |

---

### Test Example 12 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>そうです。</src><tgt>맞아요.</tgt>` | 914 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこで</src><tgt>거기서</tgt>` | 794 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天啓</src><tgt><\|wait\|></tgt>` | 1064 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>という設定が</src><tgt>천계라는 설정이</tgt>` | 721 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | 1340 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt>그래서</tgt>` | 1302 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1484 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井英雄氏の仕組み</src><tgt>나가이 히데오 씨의</tgt>` | 1281 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>구조는</tgt>` | 1533 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>五項、</src><tgt>5단계,</tgt>` | 1919 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1385 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設定ビジュアル</src><tgt>설정 비주얼,</tgt>` | 1093 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>ゴビース。</src><tgt>고비스입니다.</tgt>` | 1929 |

---

### Test Example 13 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これが</src><tgt>이게</tgt>` | 1151 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>ギアです。</src><tgt>기어입니다.</tgt>` | 816 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが</src><tgt>기어가</tgt>` | 781 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>遊ぶと、</src><tgt>돌면</tgt>` | 886 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えなくなってしまう</src><tgt>신호가</tgt>` | 1536 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>ので、</src><tgt>꺼지니까</tgt>` | 1299 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | 1573 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt>역나사</tgt>` | 974 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>ナットが</src><tgt>너트가</tgt>` | 1682 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt>붙어 있는 거예요.</tgt>` | 1871 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>그렇죠?</tgt>` | 984 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1554 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>ハイ分解完了。</src><tgt>하이 분해 완료.</tgt>` | 1942 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right. </src><tgt>好的。</tgt>` | 1217 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>And then, </src><tgt>接下来，</tgt>` | 883 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | 1217 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 645 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1175 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1437 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1850 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 787 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1616 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>实际上使用这些值。</tgt>` | 2004 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1901 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>So this game.board </src><tgt>所以，</tgt>` | 1510 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>array. </src><tgt>game.board数组。</tgt>` | 836 |

---

### Test Example 15 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 911 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt>非常に重要な研究を</tgt>` | 1086 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1215 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. This is </src><tgt>行いました。極めて幸せな人々に関するものです。これは</tgt>` | 2125 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>tip of the stem. </src><tgt>まさにその先端です。</tgt>` | 912 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>Research. </src><tgt>研究です。</tgt>` | 2075 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at 10% </src><tgt>10%の</tgt>` | 1645 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 672 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>最も幸せな人々の</tgt>` | 2038 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People that </src><tgt>うち10%を見ています。人々は</tgt>` | 2104 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>私たちから学ぶことができます。</tgt>` | 1931 |

---

### Test Example 16 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1335 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>The people in the auspicious spots</tgt>` | 1298 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 986 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>actually weren't that intelligent.</tgt>` | 1771 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1168 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 2156 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1881 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>있었기 때문 입니다. </src><tgt>They were just randomly selected.</tgt>` | 656 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1762 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1918 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교사 들은 </src><tgt>The teachers who didn't know the truth</tgt>` | 2195 |

---

### Test Example 17 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt>When faced with this situation,</tgt>` | 1120 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>我们就是</src><tgt>we</tgt>` | 908 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1180 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>should quickly report it to our supervisor.</tgt>` | 1709 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt>Or, if you're</tgt>` | 1355 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们学校</src><tgt><\|wait\|></tgt>` | 2055 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>这个状况，不要想</src><tgt>notifying the school about the situation,</tgt>` | 1651 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>自己什么</src><tgt><\|wait\|></tgt>` | 629 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>都把它扛下来，</src><tgt>don't try to handle it all on your own.</tgt>` | 2211 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>你無理承担。</src><tgt>Don't take on an unreasonable burden.</tgt>` | 1990 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>整体而言，是建议属下</src><tgt>Overall, it's recommended that subordinates</tgt>` | 2019 |

---

### Test Example 18 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1262 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1033 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt><\|wait\|></tgt>` | 1167 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt>We also have items like T- shirts available.</tgt>` | 1347 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 1142 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ご参加ください。</src><tgt>So please come join us.</tgt>` | 756 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1964 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>That's all for the contact information.</tgt>` | 2016 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>けど、</src><tgt><\|wait\|></tgt>` | 2002 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>またね、</src><tgt>And hey,</tgt>` | 1954 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>うちの案内があります</src><tgt>we have some information.</tgt>` | 1233 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>ので、ぜひ商品もチェックください。</src><tgt>So please check out the products too.</tgt>` | 1298 |

---

### Test Example 19 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 886 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAアンデスに</src><tgt><\|wait\|></tgt>` | 1090 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>その場面で</src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>A生息かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1165 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>調べるときに</src><tgt><\|wait\|></tgt>` | 1053 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>まあAの乱行を</src><tgt><\|wait\|></tgt>` | 908 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、</src><tgt><\|wait\|></tgt>` | 1650 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あのその生息かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1676 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を調べる</src><tgt><\|wait\|></tgt>` | 907 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>生息であることが保証する</src><tgt><\|wait\|></tgt>` | 2052 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方をされています。</src><tgt>When you're checking whether A is actually living in the AA Andes, you'll often see it used to check for A's presence. It's used to confirm that it's actually living there.</tgt>` | 3840 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 586 |

---

### Test Example 20 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 937 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1084 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떨 표식 기고 </src><tgt><\|wait\|></tgt>` | 1300 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1476 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1351 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보호 지역 인 </src><tgt><\|wait\|></tgt>` | 1763 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 997 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1573 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 2018 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt><\|wait\|></tgt>` | 1963 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>이다. </src><tgt>I am a member of the ' Eopryeok ' group. I'm in the same generation as Park Han- sang, who is in my home region.</tgt>` | 2525 |

---

### Test Example 21 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1043 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔을 </src><tgt><\|wait\|></tgt>` | 1115 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주게 달라 이거 주고 내가 </src><tgt>Give me another glass.</tgt>` | 1350 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>주길 내용 으로 와서 </src><tgt>I'll come over and</tgt>` | 1650 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>주다. 다른 잔쯤에 </src><tgt>fill it up.</tgt>` | 1198 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>주게 달라 </src><tgt><\|wait\|></tgt>` | 2064 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>해줘야 되나? 내가 </src><tgt>Should I give it to me? I'll</tgt>` | 2042 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt>not hear</tgt>` | 2105 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주자는요. </src><tgt>the one who's not listening.</tgt>` | 2071 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아, </src><tgt>Ah,</tgt>` | 1896 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1563 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 899 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt><\|wait\|></tgt>` | 1063 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活的一个</src><tgt><\|wait\|></tgt>` | 1209 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt>제 삶의 궤도로 돌아가게 해줘요.</tgt>` | 1931 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 995 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>好自在的</src><tgt><\|wait\|></tgt>` | 1681 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>时候，在做热汤</src><tgt>편안하게 지낼 수 있게 해줘요.</tgt>` | 1938 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭的，就是</src><tgt>뜨거운 국이나 밥을 먹는 게</tgt>` | 989 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我的当时</src><tgt><\|wait\|></tgt>` | 1809 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>背驼着</src><tgt><\|wait\|></tgt>` | 1848 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>这么一个小小的小小的一个愿望哈。</src><tgt>제 그때의 작은 소망이었어요.</tgt>` | 2221 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1475 |

---

### Test Example 23 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个就是</src><tgt>2つ目は</tgt>` | 969 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>二classList，</src><tgt>二つのクラスに</tgt>` | 1269 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>并服务</src><tgt>入り、</tgt>` | 1227 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一级一线</src><tgt>第一層の</tgt>` | 1211 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>トッププレイヤーたちをサポートするものです。</tgt>` | 840 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说，</src><tgt>例えば、</tgt>` | 1855 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做维生</src><tgt>V-Life</tgt>` | 1696 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>魔兽小时几点，你可以</src><tgt>の魔獣戦で、</tgt>` | 766 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>发现</src><tgt><\|wait\|></tgt>` | 1733 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维生好拼分的</src><tgt>V-Lifeのスコアを</tgt>` | 2038 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>新棒</src><tgt>大きく伸ばす</tgt>` | 1948 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>反而活了。</src><tgt>ための新しい棒を見つけることができます。</tgt>` | 1641 |

---

### Test Example 24 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 820 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间</src><tgt><\|wait\|></tgt>` | 1252 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有着某种</src><tgt><\|wait\|></tgt>` | 1271 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>心理，</src><tgt>If there's a certain psychological dynamic between high school girls and people who don't look particularly attractive,</tgt>` | 1784 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>could it be</tgt>` | 2106 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1537 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天黎尔</src><tgt><\|wait\|></tgt>` | 763 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>starting with Tian Li'er?</tgt>` | 2103 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1831 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1952 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>与年篇。</src><tgt>Yang Zisi and Nianpian.</tgt>` | 1713 |

---

### Test Example 25 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt>제 이름은</tgt>` | 1039 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Finley Matthews, </src><tgt>피니 매튜스입니다.</tgt>` | 1450 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently studying </src><tgt>현재</tgt>` | 869 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in aviation. </src><tgt>항공 분야를 공부하고 있습니다.</tgt>` | 1511 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>My background in finance </src><tgt>제 금융 배경은</tgt>` | 1347 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of psychology. </src><tgt>심리학 학사입니다.</tgt>` | 1763 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 996 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at the airline, </src><tgt>여기 항공사에서는</tgt>` | 1616 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1954 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>앞으로</tgt>` | 2052 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 2203 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1532 |

---

### Test Example 26 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1307 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在这</src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>个罗马呢，</src><tgt>このローマでは、</tgt>` | 1274 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 1240 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>造成了，所以呢，</src><tgt>それが原因で</tgt>` | 1393 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt>今、</tgt>` | 475 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>所面临的一些</src><tgt>皆さんが直面している</tgt>` | 2118 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt>危機や</tgt>` | 1760 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>风险</src><tgt>リスクは、</tgt>` | 566 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也可能是你</src><tgt>も</tgt>` | 1719 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>事业就已经</src><tgt>キャリアの</tgt>` | 1873 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>变坏了。</src><tgt>悪化を意味するかもしれません。</tgt>` | 2000 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>因此，</src><tgt>ですから、</tgt>` | 1298 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>会建议属鸡的朋友呢，</src><tgt>酉年生まれの皆さんには、</tgt>` | 892 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 896 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼 늘어나서</tgt>` | 1098 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt>화학 결합도</tgt>` | 1278 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy. </src><tgt>에너지를 저장해요.</tgt>` | 1617 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>And when those bonds are broken, </src><tgt>그 결합이 끊어지면</tgt>` | 1485 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 잠재 에너지가</tgt>` | 2158 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted </src><tgt><\|wait\|></tgt>` | 1791 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>to other types of energy, </src><tgt>다른 형태의 에너지로 바뀌는데,</tgt>` | 2138 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>열이나 빛 같은 거죠.</tgt>` | 2006 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or </src><tgt><\|wait\|></tgt>` | 1918 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>gets used to make </src><tgt><\|wait\|></tgt>` | 789 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>아니면 다른 결합을 만드는 데 쓰이기도 하고요.</tgt>` | 1680 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1031 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>已婚正常，</src><tgt>I was married at the time,</tgt>` | 1239 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>和我伴侣跳</src><tgt><\|wait\|></tgt>` | 1146 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1425 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>所以坚持不开档，</src><tgt>and my partner and I were dancing, so we didn't take a break.</tgt>` | 1684 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间大概有</src><tgt>During that time,</tgt>` | 2050 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1864 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>十二生来生段，</src><tgt>we had about twelve birth segments,</tgt>` | 1911 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 1271 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>已打提腿，</src><tgt>with the kicks, the leg kicks, and the foot kicks,</tgt>` | 1501 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>everything was fine.</tgt>` | 1683 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1481 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>依乎的离开。</src><tgt>They all left as they pleased.</tgt>` | 1437 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Well, or if you have </src><tgt>ええ、あるいは</tgt>` | 1218 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 961 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何かを書きたい場合、</tgt>` | 1232 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>テキストを書く、</tgt>` | 1523 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt>気づくでしょう。</tgt>` | 1313 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1924 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 970 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the word. </src><tgt>その単語のスペルすら知らないなんて。</tgt>` | 1529 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>Like, oh, is this word </src><tgt>「あ、この単語は</tgt>` | 2220 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>started with </src><tgt><\|wait\|></tgt>` | 1870 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a double p, </src><tgt>ダブルPで始まるの？</tgt>` | 2062 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double l? I don't know. </src><tgt>ダブルL？わからない。</tgt>` | 1821 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1166 |

---

### Test Example 30 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 894 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>백오십만 개가 중화 볼 수 </src><tgt>150万個が</tgt>` | 1803 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>100명 미만 으로 </src><tgt>100人未満で</tgt>` | 1144 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな企業が</tgt>` | 1067 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>多くありました。</tgt>` | 1165 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | 1602 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 </src><tgt>中小企業は</tgt>` | 1068 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>成長するか、あるいは</tgt>` | 1665 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>폐업해 길도 되는데 </src><tgt>廃業することもありますが、</tgt>` | 2287 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>これは</tgt>` | 1815 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>성기 없던 것은 </src><tgt>成長も廃業も</tgt>` | 2061 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>しない</tgt>` | 1628 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt>現象だと考えられます。</tgt>` | 1453 |

---

### Test Example 31 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1323 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 1190 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment </src><tgt>19차 수정안의 의미는</tgt>` | 1232 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore its </src><tgt>19차 수정안을 살펴보고</tgt>` | 1642 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>그 역사를</tgt>` | 1163 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how </src><tgt><\|wait\|></tgt>` | 2057 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt>정치적 변화가</tgt>` | 1524 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>어떻게 일어날 수 있는지</tgt>` | 840 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 이해하는 데 도움이 될 것입니다.</tgt>` | 2139 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1859 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1922 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>수정안의 의미는 물론</tgt>` | 1806 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>are Miriam's. </src><tgt>미리암의 것입니다.</tgt>` | 1347 |

---

### Test Example 32 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new, </src><tgt>没什么新鲜事，</tgt>` | 1103 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1110 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there are </src><tgt>有</tgt>` | 1060 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such instances before </src><tgt>很多类似的情况，</tgt>` | 1169 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1102 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>that future TC </src><tgt>所以</tgt>` | 701 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 1653 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src>this is just </src><tgt>未来TC</tgt>` | 969 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>one another place </src><tgt>只是另一个地方</tgt>` | 1640 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>to look at </src><tgt>来看</tgt>` | 1941 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1987 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>what </src><tgt><\|wait\|></tgt>` | 739 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1650 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>would like to </src><tgt><\|wait\|></tgt>` | 1523 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>bug reports should be available for. </src><tgt>开发者或工程师可以提交Bug报告的地方。</tgt>` | 1498 |

---

### Test Example 33 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 1018 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이런 것들은 </src><tgt>Things like vanadium</tgt>` | 1142 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유실 이 일어날 뻔 </src><tgt><\|wait\|></tgt>` | 1299 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>과거 6.3. </src><tgt>almost went missing back in June 2006.</tgt>` | 2177 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 사건 이긴 </src><tgt><\|wait\|></tgt>` | 788 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>여러분 께 굉장히 </src><tgt><\|wait\|></tgt>` | 2090 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>바로 </src><tgt><\|wait\|></tgt>` | 1815 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연 업 미네랄이다. </src><tgt>It's a very obvious example of a natural mineral.</tgt>` | 2186 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이것 이 </src><tgt><\|wait\|></tgt>` | 1913 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>기계 가 가져가 줘요. </src><tgt>The machine just takes it.</tgt>` | 2066 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1566 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1147 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아연. </src><tgt>Now, add zinc to it.</tgt>` | 625 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src>这一张的部分</src><tgt>이 부분은</tgt>` | 884 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1049 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1248 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>一个戴旧的人，但是</src><tgt>낡은 옷을 입은 사람입니다. 하지만</tgt>` | 1878 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>它是属于逆向的，</src><tgt>역방향입니다.</tgt>` | 1173 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2037 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>这通场嘛，这样的一个状况</src><tgt>이런 상황이</tgt>` | 1845 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>会说教</src><tgt><\|wait\|></tgt>` | 504 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>要去特别注意的是</src><tgt>특별히 주의해야 할 점은</tgt>` | 2121 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1857 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到于他</src><tgt><\|wait\|></tgt>` | 1909 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>掉不到</src><tgt><\|wait\|></tgt>` | 1566 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1156 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>于你的意识上。</src><tgt>그의 의식이 당신에게 영향을 미치지 않도록 하는지 여부입니다.</tgt>` | 1043 |

---

### Test Example 35 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 897 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알거니와 </src><tgt>知っているでしょう。</tgt>` | 1081 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 </src><tgt>ここが</tgt>` | 1173 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인으로 있을 때에 </src><tgt>異邦人としていた時、</tgt>` | 1716 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src>말 못하 는 </src><tgt>話せない</tgt>` | 1263 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>우상에게로 </src><tgt>偶像に</tgt>` | 1693 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>그대로 </src><tgt>そのまま</tgt>` | 890 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>連れて行かれたのです。</tgt>` | 1814 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1913 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>ですから、私が</tgt>` | 1893 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちに</tgt>` | 1230 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>知らせるのです。</tgt>` | 1162 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님의 영으로 </src><tgt>神の霊によって</tgt>` | 1605 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>語る者は</tgt>` | 1344 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1112 |

---

### Test Example 36 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>砸到</src><tgt><\|wait\|></tgt>` | 876 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>一个铁头，</src><tgt>鉄の頭にぶつかって、</tgt>` | 1550 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt>もし</tgt>` | 705 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>打到了铁头之后，</src><tgt>鉄の頭にぶつかったら、</tgt>` | 1844 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1180 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2108 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>抓前守，</src><tgt>必ず前をしっかり守ってください。</tgt>` | 2005 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要像说，哎，那我</src><tgt>「あ、</tgt>` | 2034 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>再继续操作</src><tgt>もう一度操作を</tgt>` | 1968 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>続けよう」なんて言わないでくださいね。</tgt>` | 1864 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 516 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのか？</tgt>` | 1730 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt>それは、</tgt>` | 1223 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1142 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1329 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>まさに今動き出している</tgt>` | 1124 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1103 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt>人には、</tgt>` | 1330 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>that ten of them </src><tgt>その10人には</tgt>` | 1430 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that are </src><tgt><\|wait\|></tgt>` | 769 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>really important </src><tgt>本当に重要な</tgt>` | 1535 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1700 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>that I'm going to go into </src><tgt>10人います。彼らは</tgt>` | 827 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1751 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1841 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video. </src><tgt>この動画の後に1分程度の動画をいくつか紹介します。</tgt>` | 2263 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>They cover each one </src><tgt>それぞれについて</tgt>` | 1544 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>in a little more </src><tgt><\|wait\|></tgt>` | 1398 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, </src><tgt>もう少し詳しく解説します。</tgt>` | 1301 |

---

### Test Example 38 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt>그렇다면</tgt>` | 1083 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>蒸らせてやる。</src><tgt>물에 흠뻑 적셔주지.</tgt>` | 1131 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt>나는</tgt>` | 1088 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今、</src><tgt>지금</tgt>` | 447 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>ひき手を見ている。</src><tgt>손잡이를 잡고 있다.</tgt>` | 1594 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1145 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>더 이상</tgt>` | 1856 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えている</src><tgt>한계가</tgt>` | 830 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不烈の奇跡よ。</src><tgt>넘어버린 불멸의 기적이야.</tgt>` | 1683 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1959 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt>오랫동안</tgt>` | 1884 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなでいくを</src><tgt>부나데이쿠를</tgt>` | 2018 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってるんだ。</src><tgt>하고 있었어.</tgt>` | 1625 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt>나는 이렇게 대단한</tgt>` | 1180 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>海賊線を</src><tgt>해적선을</tgt>` | 575 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>본 적이 없어.</tgt>` | 1253 |

---

### Test Example 39 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1177 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어찌 보면 </src><tgt>嗯，从另一个角度看，</tgt>` | 1062 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1287 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1305 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1304 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt><\|wait\|></tgt>` | 581 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>他就是和我们同龄的，也是我们同龄的弟弟。</tgt>` | 2734 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt>所以</tgt>` | 1247 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1868 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생 한 거보다는 </src><tgt>比起我录的视频，</tgt>` | 1647 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 858 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로. </src><tgt>他自己</tgt>` | 1861 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1487 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 1149 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>잘해놓고. </src><tgt>做得更好了。</tgt>` | 586 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠어. </src><tgt>希望他能过得更幸福。</tgt>` | 1660 |

---

### Test Example 40 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて、</tgt>` | 1237 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새 영화 를 </src><tgt>新しい映画を</tgt>` | 881 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>見てみよう。</tgt>` | 1026 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 </src><tgt>昔の</tgt>` | 675 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>돋든 자차 리 돋든 </src><tgt>ソレミドテン、チャチャリドテン、</tgt>` | 2214 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>내 기분 이 너무야 </src><tgt>その気持ち、すごく</tgt>` | 761 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 </src><tgt><\|wait\|></tgt>` | 1965 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>한들 어서 같이 놀자는 거야. </src><tgt>楽しんで、一緒に遊ぼうって話なんだ。</tgt>` | 2180 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>기신이 너무 </src><tgt>気心は</tgt>` | 2055 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>すごく引っかかるだろうし、</tgt>` | 1939 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>기신이 너무 </src><tgt>気心は</tgt>` | 1992 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>지켜 주라고 </src><tgt>すごく守ってくれって</tgt>` | 1703 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>찔러 주다 보니까 </src><tgt>刺されて、</tgt>` | 1387 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>気持ちが楽になって、</tgt>` | 1094 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감음. </src><tgt>目を閉じるんだ。</tgt>` | 833 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>金運についてですが、</tgt>` | 1182 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | 1185 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>还不错的，但是</src><tgt>かなり良いでしょう。ただ、</tgt>` | 1133 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较稳定</src><tgt>安定している</tgt>` | 1296 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src>的部分，也就是</src><tgt>部分です。つまり、</tgt>` | 1390 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>在事业方面</src><tgt>仕事面では</tgt>` | 1450 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>的业绩增长</src><tgt>業績の伸びが</tgt>` | 1107 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>所带来的红利</src><tgt>少ないでしょう。</tgt>` | 1725 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>与收入的提升，</src><tgt>収入の増加という恩恵は、</tgt>` | 2279 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>如果说投资领域方面</src><tgt>投資面では</tgt>` | 1967 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 1910 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错的，只是</src><tgt>良いでしょう。ただ、</tgt>` | 1704 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>相对整体来说，</src><tgt>全体的に見ると、</tgt>` | 1421 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>少し弱くなっています。</tgt>` | 1063 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt>それだけです。</tgt>` | 827 |

---

### Test Example 42 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10 </src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt><\|wait\|></tgt>` | 1053 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>でした。恐らく</src><tgt>应该是10、12手吧。大概</tgt>` | 1450 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>10秒で</src><tgt>10秒</tgt>` | 1410 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1255 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>1秒に</src><tgt><\|wait\|></tgt>` | 1374 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1088 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt>，可能1秒左右吧。</tgt>` | 1923 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2020 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1897 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐ろしく</src><tgt><\|wait\|></tgt>` | 1829 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>12手</src><tgt><\|wait\|></tgt>` | 516 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt>12手，</tgt>` | 1529 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1365 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt>宫马他们</tgt>` | 1180 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>就……</tgt>` | 767 |

---

### Test Example 43 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 858 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃Xiamen</src><tgt>呃，</tgt>` | 1022 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>일라고 하는 </src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1083 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt>XiamenDay这个计算机也能理解，</tgt>` | 1410 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 642 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 2188 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1955 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 </src><tgt><\|wait\|></tgt>` | 2081 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>말깨 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1982 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1936 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성해야 되는데 </src><tgt><\|wait\|></tgt>` | 644 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1243 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1415 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>我们需要编写代码，而编写代码需要一个程序。这个程序，无论是计算机还是人，都能理解，它就是计算机语言的语法。</tgt>` | 1870 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt>So, this is</tgt>` | 1295 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1097 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうだけじゃなくて、</src><tgt>not just a visual development environment,</tgt>` | 1250 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルパイソン</src><tgt><\|wait\|></tgt>` | 1452 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt>but also a Visual Python development environment.</tgt>` | 1360 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも、</src><tgt>That's because</tgt>` | 2087 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルの書いて</src><tgt><\|wait\|></tgt>` | 1720 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>後、それ自体は</src><tgt>you write a flow graph in Visual FlowGraph,</tgt>` | 776 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードが</src><tgt><\|wait\|></tgt>` | 1817 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成されて、それが</src><tgt>and then Python code is generated from it.</tgt>` | 2136 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt>When that runs, it performs</tgt>` | 1965 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1493 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことをしている</src><tgt>signal processing.</tgt>` | 1119 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ところになっているから</src><tgt><\|wait\|></tgt>` | 474 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1202 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はい。じゃあ</src><tgt>Okay.</tgt>` | 734 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1195 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. How far </src><tgt>학력. 얼마나</tgt>` | 1224 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you </src><tgt><\|wait\|></tgt>` | 1094 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1437 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? </src><tgt>교육을 마쳤나요?</tgt>` | 1397 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>고등학교를 졸업했나요?</tgt>` | 1829 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1291 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>attainment. </src><tgt>그게 한 단계의 학력입니다.</tgt>` | 1329 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>대학에 다녔나요?</tgt>` | 2174 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>And so, </src><tgt>그래서</tgt>` | 1813 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>졸업했나요?</tgt>` | 2007 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt>또 다른 단계의 학력입니다.</tgt>` | 1849 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>자, 이제</tgt>` | 1301 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. </src><tgt>그만입니다.</tgt>` | 1219 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>I'll see you online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 904 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계속 </src><tgt><\|wait\|></tgt>` | 1180 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>もちろん、</tgt>` | 1013 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt>こういうケースもあります。私たちが</tgt>` | 1382 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>Aという人と</tgt>` | 1479 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람 이 </src><tgt>Bという人が</tgt>` | 1347 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 콘텐츠예요. </src><tgt>お互いにコンテンツを共有している場合です。</tgt>` | 2158 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 </src><tgt>例えば、</tgt>` | 1520 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>콘텐츠 여가지고 A라는 </src><tgt>Aという人が</tgt>` | 849 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>사람 이 </src><tgt>Aという人が</tgt>` | 1887 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪意のあるコードを</tgt>` | 2046 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>줬을 때 </src><tgt>送ったとき、</tgt>` | 1963 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비란 사람 이 </src><tgt>Bという人が</tgt>` | 1602 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt>実際に</tgt>` | 1083 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로스 사이트 크리티 에서 </src><tgt>クロスサイトクリティカル（XSS）で</tgt>` | 860 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>계시 파까지 </src><tgt>XSPまで</tgt>` | 1049 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>感染してしまうか、という話です。</tgt>` | 727 |

---

### Test Example 47 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대 </src><tgt>そして、これに対して</tgt>` | 965 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>多くの人々が</tgt>` | 1077 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석 을 해 놓았습니다. </src><tgt>分析をしています。</tgt>` | 1273 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt>ここで</tgt>` | 1103 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>로쿠 자의 분석 을 보시면 </src><tgt>ロクジャの分析を見ると、</tgt>` | 1559 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니가 </src><tgt>ソニーが</tgt>` | 1293 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>이력 제품 </src><tgt>イオパック製品</tgt>` | 1125 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>FPD 파이 를 </src><tgt>FPDパイを</tgt>` | 1913 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128 BT를 </src><tgt>128BTに</tgt>` | 2098 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>나중 에서 로 포인 다. </src><tgt>後からローファイにするという分析です。</tgt>` | 2183 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1932 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈, </src><tgt>Xboxシリーズ、</tgt>` | 1656 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt>Xboxにもない</tgt>` | 1368 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュ</tgt>` | 1099 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>S가 여기 도 없다. </src><tgt>Sもありません。</tgt>` | 848 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 552 |

---

### Test Example 48 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So </src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>also, you will not </src><tgt>另外，</tgt>` | 1075 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>be able to move </src><tgt>你无法</tgt>` | 1227 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1292 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1156 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt>在资源之间移动媒体对象，</tgt>` | 744 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>though, </src><tgt>但是</tgt>` | 1922 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 1631 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where </src><tgt>如果你遇到</tgt>` | 616 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>you realize </src><tgt>意识到</tgt>` | 1902 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong </src><tgt>添加了错误的</tgt>` | 1986 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>media files to a particular </src><tgt>媒体文件到某个</tgt>` | 2058 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>resource, </src><tgt>资源中，</tgt>` | 1551 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt>我们就可以</tgt>` | 1176 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>giving those </src><tgt><\|wait\|></tgt>` | 569 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>media files and then making sure </src><tgt>给那些媒体文件，然后确保</tgt>` | 1540 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt>它们被正确备份</tgt>` | 471 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>了。</tgt>` | 606 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1169 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感觉</src><tgt>推測や感覚で</tgt>` | 1191 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt>相手の気持ちを</tgt>` | 1153 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>或真实意图的，</src><tgt>読み取ったり、</tgt>` | 1635 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1284 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>本当の意図を</tgt>` | 2070 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1526 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>后经场会提到，</src><tgt>後でよく言われていますが、</tgt>` | 947 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>人们这样说：“</src><tgt>人々はこう言います。</tgt>` | 1996 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 1944 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt>この人は</tgt>` | 1820 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在作谎了。”</src><tgt>また嘘をついているよ」と。</tgt>` | 1825 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>彼の目は</tgt>` | 1276 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>すべてを物語っている。</tgt>` | 1039 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 848 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 515 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt>言っているのです。</tgt>` | 424 |

---

### Test Example 50 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어가 면 </src><tgt>进入后</tgt>` | 1255 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>会非常迷路。</tgt>` | 1071 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하려고 </src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 걸어다니 고 </src><tgt><\|wait\|></tgt>` | 1384 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있거나 </src><tgt><\|wait\|></tgt>` | 572 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 2113 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1861 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 </src><tgt><\|wait\|></tgt>` | 1985 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>장렬이에요. </src><tgt>想开车的话，走走停停，或者去江北，那更是没法说了，出国的话，那就更惨了。</tgt>` | 2558 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>좀 시간 이 </src><tgt><\|wait\|></tgt>` | 1791 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>있어야 되시 니까 </src><tgt>您得留点时间，</tgt>` | 1713 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 열심히 </src><tgt><\|wait\|></tgt>` | 1255 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>모여 봐요. </src><tgt>好好努力一下吧。</tgt>` | 1305 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>그거 는 나중 에 할 때 </src><tgt>那之后再来</tgt>` | 853 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 620 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1107 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1191 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1276 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is, </src><tgt>自分たちで基準を定義することです。</tgt>` | 1668 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>because you're absolutely correct </src><tgt>なぜなら、</tgt>` | 1161 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2097 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>but the reality is </src><tgt>その通りですが、現実には</tgt>` | 1919 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>that because we're the new cat </src><tgt>私たちが新しい猫だから、</tgt>` | 1620 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>on the block, and because </src><tgt>新しい猫だから、</tgt>` | 878 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>基準が</tgt>` | 1815 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1939 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前に変わってから、</tgt>` | 1750 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt>私たちは</tgt>` | 1399 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>our standard </src><tgt>基準を</tgt>` | 1127 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>守らなければなりません。なぜなら、今のところ、</tgt>` | 1033 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 649 |

---

### Test Example 52 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 1050 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt><\|wait\|></tgt>` | 1102 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인 다면 </src><tgt>If the stock price index is showing an upward trend,</tgt>` | 1599 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형주도 </src><tgt>these large- cap stocks</tgt>` | 1360 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1152 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt>will likely rise sharply,</tgt>` | 2361 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1747 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1826 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 864 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1741 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 </src><tgt><\|wait\|></tgt>` | 1921 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이기 때문 에 </src><tgt>but first, the lighter- weight stocks will lead the market.</tgt>` | 1935 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요수 희총이 </src><tgt><\|wait\|></tgt>` | 1110 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1302 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 767 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>So you should keep an eye on the lighter- weight stocks.</tgt>` | 837 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src>For all of the </src><tgt><\|wait\|></tgt>` | 888 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>shortrices, </src><tgt>모든 단기적인</tgt>` | 1196 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>we've just discussed. </src><tgt>사항에 대해 방금 논의했습니다.</tgt>` | 1298 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src>But </src><tgt>하지만</tgt>` | 1183 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>within our study, </src><tgt>우리 연구 내에서</tgt>` | 533 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>the role of </src><tgt><\|wait\|></tgt>` | 1954 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src>love, </src><tgt>사랑의 역할은</tgt>` | 1894 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>as we've seen, </src><tgt>보시다시피</tgt>` | 1891 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>enters into </src><tgt><\|wait\|></tgt>` | 800 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>action. </src><tgt>행동으로 이어집니다.</tgt>` | 1727 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>When we love, </src><tgt>사랑할 때</tgt>` | 1944 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>we reach the end. </src><tgt>우리는 끝에 도달합니다.</tgt>` | 1776 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>It becomes </src><tgt>그것은</tgt>` | 1187 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the end. </src><tgt>끝이 됩니다.</tgt>` | 1069 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>That's the point. </src><tgt>그게 바로 요점입니다.</tgt>` | 934 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>We'll keep </src><tgt><\|wait\|></tgt>` | 555 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>on with the video. </src><tgt>영상 계속 보시죠.</tgt>` | 538 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt>少し</tgt>` | 1349 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 1053 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section </src><tgt>動揺していました。</tgt>` | 1272 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the AHR field </src><tgt>AHR分野の最初のセクションについて、</tgt>` | 1499 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1529 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>being of critical importance </src><tgt>それが</tgt>` | 935 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1738 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant data </src><tgt><\|wait\|></tgt>` | 1798 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>bases, </src><tgt>変異データバンクよりも重要であるという点に、少し戸惑っていました。</tgt>` | 1508 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously, my loves. </src><tgt>もちろん、皆さんご存知の通りです。</tgt>` | 1316 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt>それは</tgt>` | 1664 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>if we don't agree </src><tgt>私たちが</tgt>` | 1621 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1221 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 446 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 1173 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>that we can draw from? </src><tgt>これらのデータソースに含めるべき分野について合意できなければ、</tgt>` | 1121 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, right? </src><tgt>参照できるものがないということですよね？</tgt>` | 637 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 502 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point </src><tgt>ある時点では、</tgt>` | 1011 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>in Noah's Genesis </src><tgt>ノアの創世記の</tgt>` | 1528 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>sinuary, </src><tgt>シヌアリーという箇所で、</tgt>` | 829 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1380 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he's supposed to </src><tgt>彼は</tgt>` | 1315 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt>荒野にいるはずだと知っています。</tgt>` | 1929 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>a short day's day, that he's hungry, </src><tgt>彼は飢えていると知っています。</tgt>` | 1802 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>and so he says to </src><tgt>そこで彼は</tgt>` | 780 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>Jesus, </src><tgt>イエスに言います。</tgt>` | 1992 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it </src><tgt>「もしあなたが神の御子なら、</tgt>` | 2269 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1791 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>turn these stones to bread. </src><tgt>この石をパンに変えてみせなさい。」</tgt>` | 2024 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 972 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>How did Jesus deal with that </src><tgt>イエスはどのように対処したのでしょうか。</tgt>` | 1456 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>その誘惑にどう対処したのでしょうか。</tgt>` | 723 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man </src><tgt>男は</tgt>` | 540 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Jonathan led by </src><tgt>ヨナタンが</tgt>` | 455 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>a lone. </src><tgt>一人で進みました。</tgt>` | 486 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1347 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful, </src><tgt>有意义的，</tgt>` | 1151 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>individual right, </src><tgt>个人权利，</tgt>` | 1170 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>最高法院</tgt>` | 1437 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt>最后才介入，</tgt>` | 1365 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't know </src><tgt>不是领导者。我不知道</tgt>` | 1815 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>if the courts want to be </src><tgt>法院是否想</tgt>` | 1345 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1234 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 2023 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>成为社会变革的先锋。</tgt>` | 1943 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>如今，</tgt>` | 1939 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but they rather </src><tgt>他们更倾向于</tgt>` | 555 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1358 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1321 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 611 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | 1091 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt>所以。</tgt>` | 463 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 610 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt>你有一些联邦法官</tgt>` | 489 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 474 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>……</tgt>` | 331 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>자, 그럼</tgt>` | 1089 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그림을 한번 볼까요?</tgt>` | 1457 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 880 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>그림 부분은</tgt>` | 1500 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt>보시다시피</tgt>` | 1362 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>客厅的部分，</src><tgt>거실 부분이에요.</tgt>` | 1686 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | 1062 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是</src><tgt><\|wait\|></tgt>` | 1487 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>属于我们</src><tgt><\|wait\|></tgt>` | 1956 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt>쉴 때 쓰는 공간이죠.</tgt>` | 1995 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt>그래서</tgt>` | 607 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分</src><tgt>이건</tgt>` | 1763 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>呢，会反映的是</src><tgt>몸의 부분이라서</tgt>` | 1672 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1271 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 1051 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 827 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>坐下来休息，</src><tgt>잠시 앉아서 쉴 시간이 필요하다는 걸 보여주는 거예요.</tgt>` | 851 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>可如果我们看到</src><tgt>그런데</tgt>` | 459 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>这边是空无一人的吗？</src><tgt>여기 아무도 없는 것 같은데?</tgt>` | 561 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt>네,</tgt>` | 354 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>所以意思是说。</src><tgt>그러니까.</tgt>` | 332 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>これらの人々は</tgt>` | 888 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>全く珍しく、</tgt>` | 1090 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>and they often </src><tgt>しばしば</tgt>` | 1206 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1251 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1177 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>世界を完全に変革するために現れます。</tgt>` | 858 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1949 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その性格は</tgt>` | 1865 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾をはらんでいます。</tgt>` | 1842 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 798 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 1795 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ですが、</tgt>` | 1932 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1495 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 1461 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1046 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like it </src><tgt><\|wait\|></tgt>` | 842 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>gets straight to the point. </src><tgt>要点をまっすぐ突きます。</tgt>` | 725 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love </src><tgt>また、</tgt>` | 464 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 236 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, </src><tgt>悪魔の代弁者になるのも好きです。</tgt>` | 509 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never </src><tgt>そして決して</tgt>` | 318 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 436 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 343 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. stands for </src><tgt>E.T.P.は</tgt>` | 428 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stand for. </src><tgt>「stand for」です。</tgt>` | 362 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 970 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1755 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 명분 이 후보 를 </src><tgt>rejected the nomination</tgt>` | 882 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt>for the sake of the candidate,</tgt>` | 1376 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1263 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>for the sake of the candidate's victory,</tgt>` | 2193 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1915 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>he even put on quite a show. But now</tgt>` | 2144 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt>Yoon Suk- yeol</tgt>` | 2017 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1978 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>removing Kim Jong- in</tgt>` | 1625 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석은 들은 해놓고 </src><tgt>was Lee Jun- seok, who had been talking,</tgt>` | 1603 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 </src><tgt><\|wait\|></tgt>` | 1261 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>후보 를 </src><tgt><\|wait\|></tgt>` | 793 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 돛길을 </src><tgt><\|wait\|></tgt>` | 679 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt><\|wait\|></tgt>` | 453 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 478 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 406 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>것입니다. </src><tgt>set to attack Yoon Suk- yeol's campaign.</tgt>` | 448 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 328 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석의 성상 납권. </src><tgt>The image of Lee Jun- seok's chest and face.</tgt>` | 469 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 297 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt>The Democratic Party</tgt>` | 254 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 얼마나 </src><tgt><\|wait\|></tgt>` | 303 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 입니까? </src><tgt>is the attack's biggest advantage?</tgt>` | 356 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1057 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂で今</src><tgt><\|wait\|></tgt>` | 847 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってるみたいです。なので</src><tgt>It looks like they're making it in the cafeteria right now. So,</tgt>` | 1570 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>ここで</src><tgt><\|wait\|></tgt>` | 1239 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>このホルモンホテル</src><tgt><\|wait\|></tgt>` | 1205 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 609 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>焼魚が食べれる場所</src><tgt><\|wait\|></tgt>` | 2174 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1863 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>the Horumon Hotel is also supposed to be a place where you can get grilled fish.</tgt>` | 2310 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1837 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1960 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいな</src><tgt><\|wait\|></tgt>` | 1402 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>っていう方はですね</src><tgt>If you're thinking of staying at the Goldston Hotel here in the future,</tgt>` | 1377 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさ</src><tgt><\|wait\|></tgt>` | 600 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>てもいいかも</src><tgt>you might want to consider it.</tgt>` | 1334 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>まあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 685 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>と思います。ここ</src><tgt>I think it's a good place.</tgt>` | 661 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>のホテルからですね</src><tgt><\|wait\|></tgt>` | 404 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 490 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 405 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt><\|wait\|></tgt>` | 317 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 325 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルでのね</src><tgt><\|wait\|></tgt>` | 262 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 274 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt><\|wait\|></tgt>` | 324 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 280 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 312 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 298 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>それではね今回は。</src><tgt>The location is really great— you can walk to Busan Station in about a kilometer. So please give it some thought. That's all for this time.</tgt>` | 374 |
