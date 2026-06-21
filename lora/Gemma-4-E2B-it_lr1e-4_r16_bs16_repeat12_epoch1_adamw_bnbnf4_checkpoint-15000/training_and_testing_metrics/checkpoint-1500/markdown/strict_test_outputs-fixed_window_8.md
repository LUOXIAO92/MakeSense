# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9666
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3642
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.9857
  - TGT_RELEASE_TOTAL: 70
  - TGT_WAIT_ACCURACY: 0.9987
  - TGT_WAIT_TOTAL: 799
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1354.5720
  - PROCESS_TIME_MS_P50: 1260.0490
  - PROCESS_TIME_MS_P95: 2356.9520
  - PROCESS_TIME_MS_MAX: 3450.7920

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 1056 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>是容易的，但是</src><tgt><\|wait\|></tgt>` | 1171 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个</src><tgt><\|wait\|></tgt>` | 1280 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导，</src><tgt><\|wait\|></tgt>` | 1305 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如</src><tgt><\|wait\|></tgt>` | 1149 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>初于中年，</src><tgt><\|wait\|></tgt>` | 1190 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1682 |
| 9 | `<src>虚阿凡</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>気数を気にするのは簡単ですが、師匠の指導が一つだけです。中年の頃から、だからこそ反省が必要なのです。</tgt>` | 2496 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 743 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>一个师傅，</src><tgt><\|wait\|></tgt>` | 1976 |

---

### Test Example 2 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 961 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 941 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1089 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼봉심이 </src><tgt><\|wait\|></tgt>` | 1522 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>서울봉심이가 </src><tgt><\|wait\|></tgt>` | 1326 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1440 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>석연하는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1075 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1577 |
| 9 | `<src>진짜 이거 </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>I'm actually a sword- enthusiast. I'm a Seoul- enthusiast. You know,</tgt>` | 2519 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해경으로 </src><tgt><\|wait\|></tgt>` | 679 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽입니다. </src><tgt><\|wait\|></tgt>` | 2254 |

---

### Test Example 3 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后呢，</src><tgt><\|wait\|></tgt>` | 1285 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力</src><tgt><\|wait\|></tgt>` | 1246 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能能量也</src><tgt><\|wait\|></tgt>` | 1195 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>衰弱了，然后</src><tgt><\|wait\|></tgt>` | 1174 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在</src><tgt><\|wait\|></tgt>` | 1602 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1188 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 1259 |
| 9 | `<src>状态，</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。</tgt>` | `<src>运行状态。</src><tgt>淘撒が終わると、内部の圧力とエネルギーも弱まり、相対的に低エネルギーな状態に留まります。</tgt>` | 2663 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 626 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>异域状态。</src><tgt><\|wait\|></tgt>` | 2307 |

---

### Test Example 4 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 758 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 943 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>特に仲間がまだ</src><tgt><\|wait\|></tgt>` | 1078 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1492 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>はいはいはい。</src><tgt><\|wait\|></tgt>` | 1325 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>あの時点でこう</src><tgt><\|wait\|></tgt>` | 1617 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>ミミズカ選択を</src><tgt><\|wait\|></tgt>` | 1336 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1130 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，</tgt>` | `<src>体図してあげると</src><tgt>一开始，因为队友们还都是一年级，所以我们先给他们做个体检，</tgt>` | 2747 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>一年経っても</src><tgt><\|wait\|></tgt>` | 595 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大丈夫だ。</src><tgt><\|wait\|></tgt>` | 2283 |

---

### Test Example 5 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1190 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是</src><tgt><\|wait\|></tgt>` | 1213 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1259 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们身生的爱</src><tgt><\|wait\|></tgt>` | 1428 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>交水，</src><tgt><\|wait\|></tgt>` | 955 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>十分</src><tgt><\|wait\|></tgt>` | 1970 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>可以</src><tgt><\|wait\|></tgt>` | 1391 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>住孩子心里</src><tgt><\|wait\|></tgt>` | 696 |
| 9 | `<src><\|wait\|></src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment,</tgt>` | `<src>影响，</src><tgt>What parents need to do is pour our love into the water, so that it can deeply affect the child's heart</tgt>` | 2758 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>心耐心，</src><tgt><\|wait\|></tgt>` | 514 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>等孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 2305 |

---

### Test Example 6 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1126 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>在宿舍里</src><tgt><\|wait\|></tgt>` | 831 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这样子呢？这个优生院</src><tgt><\|wait\|></tgt>` | 1169 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>很大，然后</src><tgt><\|wait\|></tgt>` | 1530 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1334 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在放假</src><tgt><\|wait\|></tgt>` | 569 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>跟陶人，</src><tgt><\|wait\|></tgt>` | 1807 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1732 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels—</tgt>` | `<src>可以吗？</src><tgt>Why is it like this in the dorm? The Institute of Biology is huge, and then I'm on vacation with Tao Ren. Can I?</tgt>` | 2995 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 448 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和陶人。</src><tgt><\|wait\|></tgt>` | 2269 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 830 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 1071 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1465 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1092 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt><\|wait\|></tgt>` | 1173 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>What is it? </src><tgt><\|wait\|></tgt>` | 1880 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 1329 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tension in your chest? </src><tgt><\|wait\|></tgt>` | 1011 |
| 9 | `<src>I ask them what </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>Or is it a </src><tgt>你的身体在做什么？把针尖点到你的身体上。紧张感从哪里开始？是什么？是头部的？胸部的？还是</tgt>` | 2917 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>lower back where you </src><tgt><\|wait\|></tgt>` | 1578 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>use it? </src><tgt><\|wait\|></tgt>` | 1186 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 990 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 1079 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1066 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管</src><tgt><\|wait\|></tgt>` | 1378 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1227 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们下了这个状况，</src><tgt><\|wait\|></tgt>` | 1632 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1107 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1415 |
| 9 | `<src>独立承担。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>你努力承担。</src><tgt>When faced with this situation, we just need to quickly report it to our supervisor or notify the other party. Don't think you have to handle everything yourself; try to take it on.</tgt>` | 3037 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | 1348 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是给做Solution。</src><tgt><\|wait\|></tgt>` | 1464 |

---

### Test Example 9 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 913 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>初めての</src><tgt><\|wait\|></tgt>` | 1074 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1498 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴホ、</src><tgt><\|wait\|></tgt>` | 1122 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 626 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1963 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザムヌ、</src><tgt><\|wait\|></tgt>` | 1780 |
| 9 | `<src>ルナールなど</src><tgt>大致是从这一带开始的，</tgt>` | `<src>ルナール</src><tgt>大概从这儿开始，第一次是“咳咳”，然后是“咕咕”，</tgt>` | 2311 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>などという人の</src><tgt><\|wait\|></tgt>` | 832 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵、</src><tgt><\|wait\|></tgt>` | 1644 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1179 |

---

### Test Example 10 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>あとなんか</src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が</src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じで</src><tgt><\|wait\|></tgt>` | 1170 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オーシャラーとかで</src><tgt><\|wait\|></tgt>` | 1385 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>パパおいでですね</src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>海遊したい方って</src><tgt><\|wait\|></tgt>` | 1777 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ海に行こう</src><tgt><\|wait\|></tgt>` | 1231 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>してください。</src><tgt><\|wait\|></tgt>` | 1015 |
| 9 | `<src>自分で</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且</tgt>` | `<src>で、ジュネーズで</src><tgt>还有，像Oceaner这样的船，如果想去海边，就快点去吧。然后，</tgt>` | 2516 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>トントンと</src><tgt><\|wait\|></tgt>` | 690 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>シャワーが強ので</src><tgt><\|wait\|></tgt>` | 2231 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 704 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 864 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1094 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 1626 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem. </src><tgt><\|wait\|></tgt>` | 1274 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>Research. Looking at </src><tgt><\|wait\|></tgt>` | 2060 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1637 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 541 |
| 9 | `<src>of the happiest people </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>非常に幸せな人たちを対象に研究したことは？これはほんの入り口に過ぎません。研究です。最も幸せな人々の10%を</tgt>` | 3019 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People like </src><tgt><\|wait\|></tgt>` | 2274 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1782 |

---

### Test Example 12 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 941 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 산줄에 </src><tgt><\|wait\|></tgt>` | 1160 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1583 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이기로 하도 록 하도 록 </src><tgt><\|wait\|></tgt>` | 1744 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>하도 록 </src><tgt><\|wait\|></tgt>` | 627 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔줄에 죽여달라고 </src><tgt><\|wait\|></tgt>` | 2160 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해자나 내가 </src><tgt><\|wait\|></tgt>` | 1659 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt><\|wait\|></tgt>` | 1795 |
| 9 | `<src><\|wait\|></src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room?</tgt>` | `<src>안 듣고 있는 줄 알았느냐? </src><tgt>You asked me to kill someone on another mountain, so I decided to do it. Did you think I wouldn't do it? I didn't hear that kind of talk from you.</tgt>` | 2209 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아 </src><tgt><\|wait\|></tgt>` | 1672 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1636 |

---

### Test Example 13 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1048 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 로 슉빠르 시키고 </src><tgt><\|wait\|></tgt>` | 1911 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1199 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 835 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>머리 를 </src><tgt><\|wait\|></tgt>` | 1970 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>조깅 해려나 </src><tgt><\|wait\|></tgt>` | 1902 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1868 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt>I'm making Apple go fast, and I'm going to jog my own head.</tgt>` | 1418 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들인 </src><tgt><\|wait\|></tgt>` | 2396 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>가입니다. </src><tgt><\|wait\|></tgt>` | 1683 |

---

### Test Example 14 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1262 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스들은 </src><tgt><\|wait\|></tgt>` | 1176 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1276 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1509 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 947 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 2155 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스들이 </src><tgt><\|wait\|></tgt>` | 1735 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>있었기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 2062 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt>The Nics on the list were actually not highly intelligent; they were just randomly selected.</tgt>` | 1276 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 2276 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐 던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1802 |

---

### Test Example 15 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 696 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到</src><tgt><\|wait\|></tgt>` | 928 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活在一个</src><tgt><\|wait\|></tgt>` | 1079 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>轨道，让我</src><tgt><\|wait\|></tgt>` | 1527 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>能够好好的</src><tgt><\|wait\|></tgt>` | 1313 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>扎下根的时候，</src><tgt><\|wait\|></tgt>` | 807 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日航</src><tgt><\|wait\|></tgt>` | 1541 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>研发</src><tgt><\|wait\|></tgt>` | 1744 |
| 9 | `<src><\|wait\|></src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>阶段的</src><tgt>제가 제 삶의 궤도 안으로 돌아가서, 뿌리를 단단히 내릴 수 있도록 해 주세요. 그리고</tgt>` | 2840 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 508 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>被动做自我总结</src><tgt><\|wait\|></tgt>` | 2358 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>一个小小的一个愿望好。</src><tgt><\|wait\|></tgt>` | 1869 |

---

### Test Example 16 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 </src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>너무 </src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>이 절여야 될 수 있지만 </src><tgt><\|wait\|></tgt>` | 1388 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1629 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 </src><tgt><\|wait\|></tgt>` | 838 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>자기 의 보살 인데 꿈일 </src><tgt><\|wait\|></tgt>` | 2029 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 보이 고 </src><tgt><\|wait\|></tgt>` | 1503 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 673 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>이 보살 로 보이 려고 보이 세 우주 가 </src><tgt>これは、あまり崇めるべきではないかもしれないけれど、本当に菩薩だ。いや、自分の菩薩だ。夢だと思っているだけだ。私だけがこの菩薩に見えるように見せている。宇宙が</tgt>` | 3451 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>있다. 이 보살이 </src><tgt><\|wait\|></tgt>` | 2170 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>아닌데. </src><tgt><\|wait\|></tgt>` | 1825 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 852 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 803 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天気</src><tgt><\|wait\|></tgt>` | 995 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>を7.8</src><tgt><\|wait\|></tgt>` | 1452 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>度ありましたね。</src><tgt><\|wait\|></tgt>` | 1260 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 591 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1977 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井平市の</src><tgt><\|wait\|></tgt>` | 1827 |
| 9 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>仕組みは</src><tgt>맞아요. 거기서 기온이 7.8도였죠. 그리고 나가이 평시의</tgt>` | 2382 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>もうコン</src><tgt><\|wait\|></tgt>` | 845 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7.8</src><tgt><\|wait\|></tgt>` | 2115 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 621 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>度です。</src><tgt><\|wait\|></tgt>` | 1760 |

---

### Test Example 18 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 858 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAがですね</src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 964 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>いい制服かどうか</src><tgt><\|wait\|></tgt>` | 1492 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>メディアで使う</src><tgt><\|wait\|></tgt>` | 1325 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>ときにまあAAの</src><tgt><\|wait\|></tgt>` | 1628 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ランクを調べたことで</src><tgt><\|wait\|></tgt>` | 1443 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あのその制服かどうか</src><tgt><\|wait\|></tgt>` | 1086 |
| 9 | `<src>保証する、生息である</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence—</tgt>` | `<src>の調査する制服で</src><tgt>When AA is used in various situations, we've been looking into their ranks in the media to see if they're a good uniform.</tgt>` | 2950 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうこと保証するといった</src><tgt><\|wait\|></tgt>` | 1297 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>使い方をされています</src><tgt><\|wait\|></tgt>` | 1478 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1848 |

---

### Test Example 19 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1026 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunato Teru. </src><tgt><\|wait\|></tgt>` | 1330 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1325 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1218 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in actuarial finance </src><tgt><\|wait\|></tgt>` | 957 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of psychology. </src><tgt><\|wait\|></tgt>` | 2041 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1675 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 545 |
| 9 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>and in the </src><tgt>제 이름은 테루 츠나토입니다. 현재 Yale에서 보험 계리 및 심리학 학사 학위를 공부하고 있습니다.</tgt>` | 2796 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 1335 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1442 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | 1829 |

---

### Test Example 20 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1202 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 989 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あのいただく</src><tgt><\|wait\|></tgt>` | 920 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>というようなものも</src><tgt><\|wait\|></tgt>` | 1523 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 1372 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1607 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1096 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1338 |
| 9 | `<src>えっと</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements,</tgt>` | `<src>て、えっと</src><tgt>We have T-shirts and other items available for you to pick up, so please feel free to join us. That's all for the contact information.</tgt>` | 3083 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>皆さん</src><tgt><\|wait\|></tgt>` | 1141 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>の案内がありますので、</src><tgt><\|wait\|></tgt>` | 1656 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1878 |

---

### Test Example 21 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 899 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1243 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不够的人之间，</src><tgt><\|wait\|></tgt>` | 1746 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>又这么重要</src><tgt><\|wait\|></tgt>` | 1184 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>的人系？</src><tgt><\|wait\|></tgt>` | 769 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道</src><tgt><\|wait\|></tgt>` | 1938 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>会是</src><tgt><\|wait\|></tgt>` | 1666 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天际</src><tgt><\|wait\|></tgt>` | 509 |
| 9 | `<src><\|wait\|></src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night?</tgt>` | `<src>里开始的？</src><tgt>Is it really that important to have a relationship with someone who is less attractive than you, if you're a high school girl? Could it really start from the sky?</tgt>` | 3002 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2232 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 963 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>与年篇。</src><tgt><\|wait\|></tgt>` | 1408 |

---

### Test Example 22 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1223 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1189 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1273 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned and to repeat </src><tgt><\|wait\|></tgt>` | 1518 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out what you're good at. </src><tgt><\|wait\|></tgt>` | 974 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>And do more of it. </src><tgt><\|wait\|></tgt>` | 2117 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good </src><tgt><\|wait\|></tgt>` | 1838 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>at it. </src><tgt><\|wait\|></tgt>` | 1747 |
| 9 | `<src>get the people around you to help you with. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src>People around you to help you with </src><tgt>最后，重复。学习并重复，找出你擅长什么。多做一些。嗯，你并不擅长这一点。让周围的人来帮助你</tgt>` | 1900 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1986 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and and tell them next time </src><tgt><\|wait\|></tgt>` | 2118 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1262 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 1085 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1391 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1299 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1029 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 2057 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1644 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 541 |
| 9 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们</tgt>` | `<src><\|wait\|></src><tgt>好的。然后，在这些例子之后，指令告诉我们</tgt>` | 2158 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. So </src><tgt><\|wait\|></tgt>` | 853 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2281 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot sort array </src><tgt><\|wait\|></tgt>` | 1769 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1304 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1123 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1074 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと</src><tgt><\|wait\|></tgt>` | 1526 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消え</src><tgt><\|wait\|></tgt>` | 1359 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>なくなってしまうので、</src><tgt><\|wait\|></tgt>` | 1153 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1183 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1740 |
| 9 | `<src>ナットが</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>ナットが</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가 꺼져버리니까, 기어 끝에 역나사 너트가</tgt>` | 2782 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついているっていうこと</src><tgt><\|wait\|></tgt>` | 591 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 2251 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1715 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文型完了を</src><tgt><\|wait\|></tgt>` | 1290 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 934 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1193 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1358 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1428 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 962 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 2064 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1744 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 922 |
| 9 | `<src>like heat or light, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>고무줄처럼 늘어난 화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 형태의 에너지로 변환됩니다.</tgt>` | 2641 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 2219 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds. </src><tgt><\|wait\|></tgt>` | 1865 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1189 |

---

### Test Example 26 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1226 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>of the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1347 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1016 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore its </src><tgt><\|wait\|></tgt>` | 1182 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1259 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1590 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 987 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt><\|wait\|></tgt>` | 1502 |
| 9 | `<src>in the United States. </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>United States. </src><tgt>19세 개정안의 의미와 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 그 역사를 탐구하는 것입니다.</tgt>` | 3013 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1140 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1538 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of course I'm </src><tgt><\|wait\|></tgt>` | 1843 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Maryed. </src><tgt><\|wait\|></tgt>` | 1231 |

---

### Test Example 27 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 887 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是</src><tgt><\|wait\|></tgt>` | 921 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>进入二吉星</src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会福，</src><tgt><\|wait\|></tgt>` | 1510 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一吉一线</src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>平安的大牛们。</src><tgt><\|wait\|></tgt>` | 1256 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1056 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1714 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>维兴运动好事期间，</src><tgt>2つ目は二吉星に入り、福が訪れること。一吉星の平安な牛たちとの一吉の交差。例えば、維興運動の好事期間中に</tgt>` | 3101 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 934 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维兴运动好平分的</src><tgt><\|wait\|></tgt>` | 1938 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>星膀</src><tgt><\|wait\|></tgt>` | 1767 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1189 |

---

### Test Example 28 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 958 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>아일 겉은 </src><tgt><\|wait\|></tgt>` | 1248 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 융수리늄과 </src><tgt><\|wait\|></tgt>` | 1859 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1264 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산탄중인기나를 </src><tgt><\|wait\|></tgt>` | 826 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>중요 하게 </src><tgt><\|wait\|></tgt>` | 1849 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아들 </src><tgt><\|wait\|></tgt>` | 1720 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1664 |
| 9 | `<src>이렇게 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where</tgt>` | `<src>이리 </src><tgt>The outer layer of the vanadium is mainly composed of yttrium and uranium. The inner layer is mainly composed of</tgt>` | 1554 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 잘 </src><tgt><\|wait\|></tgt>` | 1876 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 899 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그 후에다가 </src><tgt><\|wait\|></tgt>` | 1825 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아현. </src><tgt><\|wait\|></tgt>` | 1159 |

---

### Test Example 29 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 975 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>我当时一切正常，</src><tgt><\|wait\|></tgt>` | 1262 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无负担，</src><tgt><\|wait\|></tgt>` | 1275 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1066 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>可以坚持不开档，</src><tgt><\|wait\|></tgt>` | 1283 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1693 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二星</src><tgt><\|wait\|></tgt>` | 1204 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来选择，</src><tgt><\|wait\|></tgt>` | 1156 |
| 9 | `<src>一下敲腿，</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>以下敲腿，</src><tgt>Everything was fine back then. No pressure at all, so I could keep it off the grid. The duration was about twelve stars, and you could choose from below. If you're tired of it,</tgt>` | 3213 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下打腿，</src><tgt><\|wait\|></tgt>` | 2267 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1410 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>当然</src><tgt><\|wait\|></tgt>` | 827 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很愉快的一开。</src><tgt><\|wait\|></tgt>` | 1172 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1055 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1071 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1263 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1290 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1153 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1637 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1278 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like oh, </src><tgt><\|wait\|></tgt>` | 1321 |
| 9 | `<src>is this word </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt>あるいは、何かを書くとき、文章を書くとき、単語のスペルが全くわからないことに気づく。まるで「あ、この単語は</tgt>` | 2943 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>started with a double P. </src><tgt><\|wait\|></tgt>` | 1786 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 956 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>Double L. I don't know </src><tgt><\|wait\|></tgt>` | 2067 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1013 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1113 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 1087 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1281 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1413 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1041 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1587 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所见的一些</src><tgt><\|wait\|></tgt>` | 1207 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>世界气啊</src><tgt><\|wait\|></tgt>` | 1253 |
| 9 | `<src>也不可能是</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、</tgt>` | `<src>跟风景</src><tgt><\|wait\|></tgt>` | 1588 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt>皆さんにお伝えしたいのは、このローマが一日でできたわけではないということです。ですから、今あなたが目にしている世界や風景が、</tgt>` | 1641 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>现变出来</src><tgt><\|wait\|></tgt>` | 2312 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>来的</src><tgt><\|wait\|></tgt>` | 1686 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>引起会建议</src><tgt><\|wait\|></tgt>` | 1291 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>一位的朋友呢。</src><tgt><\|wait\|></tgt>` | 584 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 835 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个天头，</src><tgt><\|wait\|></tgt>` | 1258 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1209 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了天头之后，</src><tgt><\|wait\|></tgt>` | 1529 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 957 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就要先</src><tgt><\|wait\|></tgt>` | 1953 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt><\|wait\|></tgt>` | 1747 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着</src><tgt><\|wait\|></tgt>` | 413 |
| 9 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。</tgt>` | `<src>哎，</src><tgt>天頂に達したなら、必ず守り抜いてください。そうしないと、</tgt>` | 2481 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>闹在我</src><tgt><\|wait\|></tgt>` | 609 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>着急哦，</src><tgt><\|wait\|></tgt>` | 2278 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1743 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1275 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 925 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new </src><tgt><\|wait\|></tgt>` | 957 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1051 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there was </src><tgt><\|wait\|></tgt>` | 928 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such interests before, </src><tgt><\|wait\|></tgt>` | 1520 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>net future TC </src><tgt><\|wait\|></tgt>` | 1358 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 988 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>is just </src><tgt><\|wait\|></tgt>` | 1729 |
| 9 | `<src>one another place </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个</tgt>` | `<src>one another place </src><tgt>以前就没有过这样的兴趣，NetFutureTC只是</tgt>` | 2069 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at </src><tgt><\|wait\|></tgt>` | 973 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 775 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but </src><tgt><\|wait\|></tgt>` | 1848 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1689 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>would like to </src><tgt><\|wait\|></tgt>` | 1265 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>have a pair of them. </src><tgt><\|wait\|></tgt>` | 1195 |

---

### Test Example 34 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 887 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HJM이라고 하는 </src><tgt><\|wait\|></tgt>` | 1071 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1482 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1378 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1593 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1439 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 어노 에 </src><tgt><\|wait\|></tgt>` | 1167 |
| 9 | `<src>문법 에 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>문법 을 </src><tgt>嗯，计算机也能理解HJM，</tgt>` | 2139 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>아깝 게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 938 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>초도들을 </src><tgt><\|wait\|></tgt>` | 2243 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 1443 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 946 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1126 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1368 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 854 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150인가 </src><tgt><\|wait\|></tgt>` | 1210 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중호보에서 100미만 으로 </src><tgt><\|wait\|></tgt>` | 1948 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들만 </src><tgt><\|wait\|></tgt>` | 1260 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>남았습니다. </src><tgt><\|wait\|></tgt>` | 624 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 2035 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 기업 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1837 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 </src><tgt><\|wait\|></tgt>` | 1852 |
| 9 | `<src>걷게 되는데 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>해화법이 이렇게 되는데 </src><tgt>その中で150から100未満の企業は、非常に小さな企業しか残っていません。一般的に小さな企業は成長するか、あるいは海運法がこうなっていますが、</tgt>` | 2223 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>해화법이 </src><tgt><\|wait\|></tgt>` | 1677 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성기 없다는 성장 도 </src><tgt><\|wait\|></tgt>` | 1944 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>폐업도 하지 않은 </src><tgt><\|wait\|></tgt>` | 1230 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1485 |

---

### Test Example 36 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 889 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1106 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1267 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>一个戴雪的人，但是他是</src><tgt><\|wait\|></tgt>` | 1635 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的</src><tgt><\|wait\|></tgt>` | 962 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1985 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这种场嘛，这样的一个状况</src><tgt><\|wait\|></tgt>` | 1892 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>会需要去</src><tgt><\|wait\|></tgt>` | 1932 |
| 9 | `<src>特别注意，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>特别的注意是</src><tgt>이 사진의 일부를 보면, 눈을 가린 사람이 보이는데, 그는 역방향적인 유형에 속합니다. 이런 유형의 상황에서는 특별히 주의해야 할 점이</tgt>` | 1929 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1848 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>能够得到</src><tgt><\|wait\|></tgt>` | 1739 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他掉不到</src><tgt><\|wait\|></tgt>` | 1212 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1222 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>了。</src><tgt><\|wait\|></tgt>` | 808 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1030 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | 1256 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>ですけど、</src><tgt><\|wait\|></tgt>` | 1170 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく十秒で</src><tgt><\|wait\|></tgt>` | 1295 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1160 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ一秒に</src><tgt><\|wait\|></tgt>` | 1620 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1401 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね</src><tgt><\|wait\|></tgt>` | 1059 |
| 9 | `<src>ね。</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。</tgt>` | `<src>ね。</src><tgt>十一二手或者十二手，大概十秒内，一秒内大概一秒左右吧。</tgt>` | 2357 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 747 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1626 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一二手</src><tgt><\|wait\|></tgt>` | 1059 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1727 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1118 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | 1221 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 820 |

---

### Test Example 38 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1049 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らせてやる。</src><tgt><\|wait\|></tgt>` | 916 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1027 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt><\|wait\|></tgt>` | 1394 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き締めを見せる。</src><tgt><\|wait\|></tgt>` | 1213 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 629 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 2009 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に</src><tgt><\|wait\|></tgt>` | 1707 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>超えてる不自由気勢。</src><tgt>그럼 젖게 해줄게. 나는 지금부터 힘을 보여줄게. 이미 한계를 넘어선 불가능한 기세야.</tgt>` | 2743 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 591 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 2214 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなデイクーを</src><tgt><\|wait\|></tgt>` | 1353 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 960 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1175 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい階則線を</src><tgt><\|wait\|></tgt>` | 1343 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | 739 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1025 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1323 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 1325 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏向</src><tgt><\|wait\|></tgt>` | 1230 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>正财的部分。</src><tgt><\|wait\|></tgt>` | 934 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>也就是在事业方面的</src><tgt><\|wait\|></tgt>` | 1986 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长所带来的</src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>红利，</src><tgt><\|wait\|></tgt>` | 707 |
| 9 | `<src>提升。如果是在</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>收入的提升。</src><tgt>金運については、今月はかなり良いと言えますが、正財に偏っています。つまり、仕事の業績向上による恩恵や収入の増加です。</tgt>` | 3017 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果是在投资理财方面，</src><tgt><\|wait\|></tgt>` | 2281 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1325 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1046 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说，</src><tgt><\|wait\|></tgt>` | 1116 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了</src><tgt><\|wait\|></tgt>` | 1368 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt><\|wait\|></tgt>` | 774 |

---

### Test Example 40 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1178 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1192 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1165 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1284 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I got ten of them </src><tgt><\|wait\|></tgt>` | 1197 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 2024 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1546 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>um </src><tgt><\|wait\|></tgt>` | 631 |
| 9 | `<src>I'm going to go into. </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>これから始めようとしている人たち、そのうち10人くらいは本当に大事な人たちです。えーと、</tgt>` | 2911 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1331 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1382 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>at the fall this video </src><tgt><\|wait\|></tgt>` | 1925 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1250 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>And a little more </src><tgt><\|wait\|></tgt>` | 1359 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>detail, </src><tgt><\|wait\|></tgt>` | 832 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1138 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새로 </src><tgt><\|wait\|></tgt>` | 826 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>밝을 거야. </src><tgt><\|wait\|></tgt>` | 1045 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1406 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>서름이 돋은 차리 돋은 </src><tgt><\|wait\|></tgt>` | 1558 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 너무 야. </src><tgt><\|wait\|></tgt>` | 705 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 </src><tgt><\|wait\|></tgt>` | 1661 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>한들어서 같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1822 |
| 9 | `<src>귀신 이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>귀신이 </src><tgt>目を閉じて、新しい光が差し込むんだ。今、寒気がするような感覚がすごくね。それを手にとって、一緒に遊ぼうって言うんだ。</tgt>` | 2977 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>오밀리 끌고 </src><tgt><\|wait\|></tgt>` | 697 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>오밀리 끌고 </src><tgt><\|wait\|></tgt>` | 2013 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1852 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>진들어주니까 </src><tgt><\|wait\|></tgt>` | 1305 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에. </src><tgt><\|wait\|></tgt>` | 1435 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 927 |

---

### Test Example 42 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1178 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 </src><tgt><\|wait\|></tgt>` | 947 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>해매입니다. </src><tgt><\|wait\|></tgt>` | 1075 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전 을 하고 </src><tgt><\|wait\|></tgt>` | 1492 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있거나 </src><tgt><\|wait\|></tgt>` | 1439 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북으로 가면 </src><tgt><\|wait\|></tgt>` | 996 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1662 |
| 9 | `<src><\|wait\|></src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国</tgt>` | `<src>외국 에게 나가 는 것도 </src><tgt>进去的时候非常危险。开车、走路，或者去江南区，</tgt>` | 2394 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>작렬이에요. </src><tgt><\|wait\|></tgt>` | 799 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 챙기 네요. </src><tgt><\|wait\|></tgt>` | 2325 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1777 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1255 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>뭐해봐요. </src><tgt><\|wait\|></tgt>` | 752 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 안인 것 같아요. </src><tgt><\|wait\|></tgt>` | 1204 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 731 |

---

### Test Example 43 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 805 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>이또 알 거니 뭐. </src><tgt><\|wait\|></tgt>` | 1326 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1683 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1291 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 759 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상 에게로 </src><tgt><\|wait\|></tgt>` | 2063 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그려지는 그대로 </src><tgt><\|wait\|></tgt>` | 1797 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>걸려 갔느라 </src><tgt><\|wait\|></tgt>` | 1876 |
| 9 | `<src><\|wait\|></src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。</tgt>` | `<src>그럼 </src><tgt>また、知ってるだろう。異邦人としてここにいるとき、言葉を話せない偶像に描かれて、そのまま描かれて、</tgt>` | 1588 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>으로 내가 </src><tgt><\|wait\|></tgt>` | 2219 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1691 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 는 것이 </src><tgt><\|wait\|></tgt>` | 1281 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>아니 며 </src><tgt><\|wait\|></tgt>` | 1164 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>영으로 말하는 </src><tgt><\|wait\|></tgt>` | 698 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>자는. </src><tgt><\|wait\|></tgt>` | 776 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1072 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 1277 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1350 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>go in your education? </src><tgt><\|wait\|></tgt>` | 1138 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 2131 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1829 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1884 |
| 9 | `<src>to college, </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>학력 수준. 교육 과정에서 얼마나 나아갔나요? 고등학교를 졸업했나요? 그건 한 단계의 학력 수준입니다. 대학에 갔나요?</tgt>` | 1922 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, </src><tgt><\|wait\|></tgt>` | 1871 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>did you graduate? </src><tgt><\|wait\|></tgt>` | 1861 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt><\|wait\|></tgt>` | 1264 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 1487 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 854 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 652 |

---

### Test Example 45 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 814 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1219 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1572 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 1000 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자 의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1163 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 1957 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 62, </src><tgt><\|wait\|></tgt>` | 1902 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FFP 파이프 를 </src><tgt><\|wait\|></tgt>` | 1665 |
| 9 | `<src>128비트로 낮춘 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트로 </src><tgt>これについて多くの人が分析しています。ここでロクジャの分析を見ると、ソニーが</tgt>` | 1517 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮춘 것을 로 포인트. </src><tgt><\|wait\|></tgt>` | 2302 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 </src><tgt><\|wait\|></tgt>` | 759 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>시리즈, </src><tgt><\|wait\|></tgt>` | 1621 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1159 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt><\|wait\|></tgt>` | 1455 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>S기가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 957 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 462 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 절수가 </src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt><\|wait\|></tgt>` | 1193 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 </src><tgt><\|wait\|></tgt>` | 1175 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>보인 다음에 </src><tgt><\|wait\|></tgt>` | 1289 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 2086 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 먼저 </src><tgt><\|wait\|></tgt>` | 1709 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 </src><tgt><\|wait\|></tgt>` | 651 |
| 9 | `<src>종목 들이 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>종목 들이 </src><tgt>After seeing the stock price drop and then seeing a large- cap- led rise, we'll see a big surge. But first,</tgt>` | 2534 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1293 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 </src><tgt><\|wait\|></tgt>` | 1528 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>때문 에 </src><tgt><\|wait\|></tgt>` | 1824 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요식초기 </src><tgt><\|wait\|></tgt>` | 1239 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 종목 을 </src><tgt><\|wait\|></tgt>` | 1368 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈줄을 봐야 </src><tgt><\|wait\|></tgt>` | 838 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 681 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1278 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1275 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>But the reality </src><tgt><\|wait\|></tgt>` | 1959 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1705 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat and </src><tgt><\|wait\|></tgt>` | 670 |
| 9 | `<src>block and because the </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>the block, </src><tgt>活動、そして自分自身で基準を定義すること。なぜなら、あなたは完全に正しいからです。しかし、現実は、私たちが新しい猫で、ブロックが新しいブロックだからです。</tgt>` | 2805 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have </src><tgt><\|wait\|></tgt>` | 2296 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1740 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>changed from twenty years ago, </src><tgt><\|wait\|></tgt>` | 1324 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 929 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard </src><tgt><\|wait\|></tgt>` | 813 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 838 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to a higher standard. </src><tgt><\|wait\|></tgt>` | 736 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1067 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉</src><tgt><\|wait\|></tgt>` | 1153 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1166 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真实意图的。</src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1157 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 2050 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1500 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：“</src><tgt><\|wait\|></tgt>` | 691 |
| 9 | `<src>这样说：“</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt>相手の感情や本当の意図を察知したり、感じ取ったりすることです。よく、人々がこう言います。「</tgt>` | 2839 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1168 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1502 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在躲藏了。”</src><tgt><\|wait\|></tgt>` | 1916 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1106 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1245 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 911 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 783 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 625 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1129 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1243 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 1528 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1219 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 958 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt><\|wait\|></tgt>` | 1985 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルの</src><tgt><\|wait\|></tgt>` | 1885 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとそれは</src><tgt><\|wait\|></tgt>` | 1857 |
| 9 | `<src>にそこから</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>Pythonコードがそっから生成される</src><tgt>This is not just a visual development environment; it's a visual Python development environment. This is because you write the visual flow graph, and then Python code is generated from it.</tgt>` | 2114 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>っていうそれが</src><tgt><\|wait\|></tgt>` | 1752 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1954 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1175 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことをしているから</src><tgt><\|wait\|></tgt>` | 1216 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 841 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 800 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 702 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1066 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 989 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1592 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1424 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1044 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 콘텐츠예요. </src><tgt><\|wait\|></tgt>` | 2125 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>B가 컨설턴트 </src><tgt><\|wait\|></tgt>` | 1813 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>여가지고 A라는 </src><tgt><\|wait\|></tgt>` | 2015 |
| 9 | `<src>A라는 사람 이 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>사람 이 </src><tgt>ですから、もちろんこういうケースもあります。AさんとBさんがコンテンツを共有しているんです。Bさんがコンサルタントで、Aさんが</tgt>` | 1475 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 2290 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 1767 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 1153 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1201 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로 사이트 스크립트 에서 </src><tgt><\|wait\|></tgt>` | 1012 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>XRP까지 </src><tgt><\|wait\|></tgt>` | 813 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까 </src><tgt><\|wait\|></tgt>` | 702 |

---

### Test Example 51 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1235 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어, 어째 보면 </src><tgt><\|wait\|></tgt>` | 1243 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1634 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1187 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 853 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 2120 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1780 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1932 |
| 9 | `<src><\|wait\|></src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>어 </src><tgt>嗯，怎么说呢，他是我和二十岁那一代一起经历的弟弟，也是像家人一样的弟弟。所以</tgt>` | 1501 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인감 못하 다는 </src><tgt><\|wait\|></tgt>` | 2399 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1726 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로. </src><tgt><\|wait\|></tgt>` | 1130 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1243 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 946 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 내려놓고 </src><tgt><\|wait\|></tgt>` | 829 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠 다. </src><tgt><\|wait\|></tgt>` | 792 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 930 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1098 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1465 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between </src><tgt><\|wait\|></tgt>` | 1201 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>the resources </src><tgt><\|wait\|></tgt>` | 470 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though, </src><tgt><\|wait\|></tgt>` | 1969 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 1780 |
| 9 | `<src>a situation </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果</tgt>` | `<src>a situation where you </src><tgt>嗯，另外，即使在资源之间移动媒体对象时也无法做到，</tgt>` | 2133 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 964 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1293 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular </src><tgt><\|wait\|></tgt>` | 1491 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, we'll do our best </src><tgt><\|wait\|></tgt>` | 2109 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>to </src><tgt><\|wait\|></tgt>` | 969 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>give them </src><tgt><\|wait\|></tgt>` | 1228 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>media files and then making sure </src><tgt><\|wait\|></tgt>` | 843 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 848 |
| 18 | `<src>properly. </src><tgt>你发现自己给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt>但如果你发现将错误的媒体文件添加到某个资源时，我们会尽力提供媒体文件，并确保它们得到正确备份。</tgt>` | 981 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 874 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>フローイーの所得主義</src><tgt><\|wait\|></tgt>` | 1251 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>决做到那个现象，</src><tgt><\|wait\|></tgt>` | 1530 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>美当中</src><tgt><\|wait\|></tgt>` | 1104 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 946 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | 2044 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>属位的爱</src><tgt><\|wait\|></tgt>` | 1664 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>能够</src><tgt><\|wait\|></tgt>` | 510 |
| 9 | `<src>同时进入恨。</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>也同时进入</src><tgt>플로이의 소득주의가 그 현상을 실현할 수 있습니다. 하지만 우리는 사랑 안에 있습니다. 그리고 해당 위치의 사랑은</tgt>` | 2894 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1283 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨在掌上的时候，</src><tgt><\|wait\|></tgt>` | 1574 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>它才爱。</src><tgt><\|wait\|></tgt>` | 1804 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上。</src><tgt><\|wait\|></tgt>` | 1130 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | 1390 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 755 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个钟摆。</src><tgt><\|wait\|></tgt>` | 780 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt><\|wait\|></tgt>` | 655 |
| 18 | `<src>继续在移动。</src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다. 그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>一动。</src><tgt>증오가 손에 쥐어져 있을 때 비로소 사랑이 됩니다. 밤이 되면 증오로 변합니다. 그 시계추는 계속 움직입니다.</tgt>` | 841 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1317 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1173 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1282 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1308 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1064 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1662 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 994 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1326 |
| 9 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、</tgt>` | `<src><\|wait\|></src><tgt>最初のセクションで、AHRの重要性について少しズレていました。</tgt>` | 2098 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 934 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously to my loves. </src><tgt><\|wait\|></tgt>` | 1124 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt><\|wait\|></tgt>` | 1569 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>if we don't agree upon </src><tgt><\|wait\|></tgt>` | 1935 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields </src><tgt><\|wait\|></tgt>` | 1152 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in </src><tgt><\|wait\|></tgt>` | 1278 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>these data sources </src><tgt><\|wait\|></tgt>` | 853 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from. </src><tgt><\|wait\|></tgt>` | 853 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, right? </src><tgt>私の愛する人たちにとって、バリアントデータベースの方が重要だというわけです。つまり、データソースに含めるべき項目について合意できなければ、そこから引き出すこともできないということですよね？</tgt>` | 1372 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 286 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1170 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1073 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1522 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1362 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I don't I don't </src><tgt><\|wait\|></tgt>` | 1771 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>believe the courts want to be </src><tgt><\|wait\|></tgt>` | 1527 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 862 |
| 9 | `<src>the the vanguard of social </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为</tgt>` | `<src>the the vanguard of </src><tgt>有意义的个人权利，而最高法院却姗姗来迟，而不是引领者。我不认为法院想成为</tgt>` | 2563 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 635 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 2190 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 631 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1699 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1131 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1311 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 760 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 789 |
| 18 | `<src>So you have some </src><tgt>法院现在想成为社会变革的先锋，它们更倾向于反映已经形成的共识。所以，</tgt>` | `<src>You have </src><tgt>社会变革的先锋。如今，但他们更像是反映已经形成的共识。所以，</tgt>` | 938 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 298 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 314 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 373 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 1099 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a son of Henry, </src><tgt><\|wait\|></tgt>` | 1581 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1205 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's a Jew </src><tgt><\|wait\|></tgt>` | 953 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in the wilderness </src><tgt><\|wait\|></tgt>` | 2072 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>spurtied day, that he's hungry, </src><tgt><\|wait\|></tgt>` | 1898 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 1867 |
| 9 | `<src>to Jesus," Hey, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus, hey, </src><tgt>ある時、彼はイエスがヘロンの息子だと知っていました。また、イエスが荒野の日にユダヤ人であり、飢えていることを知っていました。だから、イエスに言いました。「おい、</tgt>` | 2399 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're a son of God, prove it. </src><tgt><\|wait\|></tgt>` | 1675 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn </src><tgt><\|wait\|></tgt>` | 1640 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>these stones to bread. </src><tgt><\|wait\|></tgt>` | 1267 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1289 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that </src><tgt><\|wait\|></tgt>` | 818 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 807 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 639 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 402 |
| 18 | `<src>by bread alone. </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？人はパンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>神の息子なら、それを証明しろ。この石をパンに変えろ。彼はその誘惑にどう対処したのか？いやはや、ヨハネはパンによって導かれた。一人で。</tgt>` | 933 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 996 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1250 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1292 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，</src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 951 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>一个是克汀的部分，</src><tgt><\|wait\|></tgt>` | 2049 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>而克汀一般</src><tgt><\|wait\|></tgt>` | 1759 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 422 |
| 9 | `<src>我们</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가</tgt>` | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분에서 크틴이 보이는데요, 크틴은 보통</tgt>` | 2533 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>我们在收集的地方</src><tgt><\|wait\|></tgt>` | 585 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>啊，所以呢，</src><tgt><\|wait\|></tgt>` | 2373 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>它是身体的部分</src><tgt><\|wait\|></tgt>` | 1836 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢会反映的是</src><tgt><\|wait\|></tgt>` | 1187 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1197 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 944 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好</src><tgt><\|wait\|></tgt>` | 746 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>的做下来，休息</src><tgt><\|wait\|></tgt>` | 664 |
| 18 | `<src>我们可以看到这边是</src><tgt>쉬는 곳이잖아요. 그래서 이 신체 부위도 여러분이 자신에게 시간을 내서 편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可由我们可以看到</src><tgt>우리가 수집하는 곳에서 나오기 때문에, 몸의 부분은 우리가 충분한 시간을 갖고 잘 쉬어야 합니다. 그리고</tgt>` | 612 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是双五一人</src><tgt><\|wait\|></tgt>` | 421 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>的嘛，好，</src><tgt><\|wait\|></tgt>` | 427 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以也是说。</src><tgt><\|wait\|></tgt>` | 334 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 918 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 1195 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1277 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1175 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1153 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>revolutionize the world. </src><tgt><\|wait\|></tgt>` | 2004 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 1215 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>personality is </src><tgt><\|wait\|></tgt>` | 854 |
| 9 | `<src>something of a </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は</tgt>` | `<src>something of a contradiction. </src><tgt>彼らは全く珍しい人々です。そして、彼らはしばしば世界を完全に変革するために現れます。その性格は矛盾したものです。</tgt>` | 3048 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1245 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>Well, they're extroverted. </src><tgt><\|wait\|></tgt>` | 1650 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>They also </src><tgt><\|wait\|></tgt>` | 1772 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate </src><tgt><\|wait\|></tgt>` | 1085 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1324 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 803 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like it </src><tgt><\|wait\|></tgt>` | 803 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>gets straight to the point. </src><tgt><\|wait\|></tgt>` | 714 |
| 18 | `<src>They also love to </src><tgt>矛盾しています。外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>まあ、彼らは外向的です。また、意味のない会話を嫌います。そして、要点をまっすぐ言うのが好きです。彼らは</tgt>` | 819 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 504 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and they </src><tgt><\|wait\|></tgt>` | 272 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 354 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 341 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 329 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. stands for </src><tgt><\|wait\|></tgt>` | 400 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stand for. </src><tgt><\|wait\|></tgt>` | 358 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>정무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1234 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1442 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1311 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 847 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 2114 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1787 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1790 |
| 9 | `<src>윤석열 후보 가 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt>Lee Jun- seok previously claimed he was running for the sake of the party's leadership, even going to great lengths to make it look like he was running for the party's victory. But now, Yoon Suk- yeol</tgt>` | 2429 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정은을 </src><tgt><\|wait\|></tgt>` | 1584 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제간 순간 </src><tgt><\|wait\|></tgt>` | 1758 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석을 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1234 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1251 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 </src><tgt><\|wait\|></tgt>` | 851 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 떡기를 </src><tgt><\|wait\|></tgt>` | 879 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt><\|wait\|></tgt>` | 714 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 408 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>has been making a big show of wanting to defeat Yoon Suk- yeol, even after he had already made his move against Kim Jong- un.</tgt>` | 720 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 430 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 367 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 청상납건 </src><tgt><\|wait\|></tgt>` | 387 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 332 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 344 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt><\|wait\|></tgt>` | 372 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 355 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 8.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1021 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt><\|wait\|></tgt>` | 825 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってるみたいです。</src><tgt><\|wait\|></tgt>` | 1062 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1219 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ホテルも朝食が</src><tgt><\|wait\|></tgt>` | 719 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1970 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1752 |
| 9 | `<src>予定になってるので</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>Well, it looks like they're making it right after the meal. So, the hotel here is supposed to be a place where you can have breakfast,</tgt>` | 2908 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 469 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 2348 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1798 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なという方はですね</src><tgt><\|wait\|></tgt>` | 1163 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1206 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>みてもまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 997 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 727 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います</src><tgt><\|wait\|></tgt>` | 431 |
| 18 | `<src>のホテルからですね釜山</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel,</tgt>` | `<src>ここホテルからですね</src><tgt>so if you're thinking about staying at the Goldston Hotel here in the future, I think it's worth considering. From the hotel,</tgt>` | 833 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 435 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 357 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>1分かかる</src><tgt><\|wait\|></tgt>` | 419 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんないか</src><tgt><\|wait\|></tgt>` | 382 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 345 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 362 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt><\|wait\|></tgt>` | 312 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 360 |
| 27 | `<src>ご検討なさってみて</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good. If you'd like,</tgt>` | `<src>ご検討なさって</src><tgt>the Busan station is just a one- minute walk away. It's a great location, so if you're interested,</tgt>` | 480 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>みてください</src><tgt><\|wait\|></tgt>` | 188 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね</src><tgt><\|wait\|></tgt>` | 187 |
