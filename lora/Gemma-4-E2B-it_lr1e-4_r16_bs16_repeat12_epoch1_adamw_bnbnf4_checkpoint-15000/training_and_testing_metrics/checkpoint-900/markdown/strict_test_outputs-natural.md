# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9582
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.3576
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.6303
  - TGT_RELEASE_TOTAL: 495
  - TGT_WAIT_ACCURACY: 0.7239
  - TGT_WAIT_TOTAL: 373
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1339.5380
  - PROCESS_TIME_MS_P50: 1321.9930
  - PROCESS_TIME_MS_P95: 2121.6500
  - PROCESS_TIME_MS_MAX: 11380.6420

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1127 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>在宿舍里，</src><tgt>Why in the dorm?</tgt>` | 922 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个优惠</src><tgt><\|wait\|></tgt>` | 1116 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>也很大，然后</src><tgt>The discount is huge, and then</tgt>` | 1458 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 562 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 1180 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 1479 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>和淘人，</src><tgt><\|wait\|></tgt>` | 1331 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在度假，</src><tgt><\|wait\|></tgt>` | 632 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1540 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>和淘人。</src><tgt>I'm on vacation and playing Taohun. I'm on vacation and playing Taohun.</tgt>` | 2398 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 764 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 1095 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>仲までまだ</src><tgt><\|wait\|></tgt>` | 1178 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>因为仲还没到一年级。</tgt>` | 1431 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>この時点で</src><tgt>在这个阶段，</tgt>` | 1418 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1319 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>四角線で</src><tgt><\|wait\|></tgt>` | 542 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数していった</src><tgt><\|wait\|></tgt>` | 1598 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 1489 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1862 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>対数だ。</src><tgt>就算经过十年，对数依然是。</tgt>` | 918 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1078 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>做的是</src><tgt>Parents need to</tgt>` | 1141 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1195 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱</src><tgt><\|wait\|></tgt>` | 1394 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>交水，</src><tgt><\|wait\|></tgt>` | 1433 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1322 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>使</src><tgt><\|wait\|></tgt>` | 428 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>Kids心里隐藏</src><tgt><\|wait\|></tgt>` | 1652 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1624 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>的内疚心，</src><tgt><\|wait\|></tgt>` | 1871 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>等孩子慢慢长大。</src><tgt>use our deep love to wash away the guilt in our children's hearts as they grow up.</tgt>` | 2071 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气数是容易的，</src><tgt>気数をつけるのは簡単です。</tgt>` | 1923 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1181 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt>でも、</tgt>` | 611 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导到</src><tgt>師匠が</tgt>` | 1457 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1483 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>炉火出炉中间，</src><tgt>炉の火が焚き上げられる間、</tgt>` | 1582 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>だから</tgt>` | 739 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>反転させる必要があります。</tgt>` | 1259 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt>そして、</tgt>` | 1940 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师傅。</src><tgt>師匠になる。</tgt>` | 1911 |

---

### Test Example 5 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为</src><tgt><\|wait\|></tgt>` | 860 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>这个情况，我们就是</src><tgt>Because of this situation,</tgt>` | 1319 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1098 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就感谢的</src><tgt><\|wait\|></tgt>` | 1293 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>回报主管或是通知对方</src><tgt><\|wait\|></tgt>` | 1471 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我说</src><tgt><\|wait\|></tgt>` | 1320 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>这个状况，不要想自己</src><tgt><\|wait\|></tgt>` | 545 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1666 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>苦力偿单，</src><tgt><\|wait\|></tgt>` | 1575 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>真的</src><tgt><\|wait\|></tgt>` | 1975 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>而已，</src><tgt><\|wait\|></tgt>` | 1893 |

---

### Test Example 6 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1032 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘撒完以后呢，</src><tgt>淘金が終わった後、</tgt>` | 1650 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>那内部的冶炼清</src><tgt>内部の</tgt>` | 870 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也</src><tgt>冶錬エネルギーも</tgt>` | 1194 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>衰弱了，然后就</src><tgt>衰えて、</tgt>` | 1577 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1379 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1579 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>低能量的运行状态</src><tgt><\|wait\|></tgt>` | 1489 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>态。</src><tgt>相対的に低いエネルギーの運行状態に留まってしまうんです。</tgt>` | 1008 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これが</tgt>` | 1582 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>的异于状态。</src><tgt>いわゆる異質状態です。</tgt>` | 2125 |

---

### Test Example 7 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 801 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复一下。</tgt>` | 1209 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learned to repeat </src><tgt><\|wait\|></tgt>` | 1288 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>by far, </src><tgt><\|wait\|></tgt>` | 600 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>you're good at, and you more of it </src><tgt><\|wait\|></tgt>` | 1575 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and when you're not </src><tgt><\|wait\|></tgt>` | 1441 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>good at, </src><tgt><\|wait\|></tgt>` | 1598 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 1829 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2074 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>and in tell the next time </src><tgt><\|wait\|></tgt>` | 2119 |

---

### Test Example 8 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这附近</tgt>` | 1170 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので、</src><tgt>开始的，</tgt>` | 1172 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1338 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1292 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>五減</src><tgt><\|wait\|></tgt>` | 532 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1338 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>世増。</src><tgt>五减世増。</tgt>` | 1653 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 1566 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>などという人の</src><tgt><\|wait\|></tgt>` | 1095 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>絵、</src><tgt><\|wait\|></tgt>` | 1379 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 2148 |

---

### Test Example 9 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 923 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이럴지 너무 </src><tgt><\|wait\|></tgt>` | 1165 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>이 저희 할 일 수 있지만 </src><tgt>これは</tgt>` | 1208 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 들요 </src><tgt>私たちがやるべきことでも</tgt>` | 1482 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 자기 의 </src><tgt>ありません。自分の</tgt>` | 1467 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>お坊さんなのに、</tgt>` | 1543 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>프로라고 하고 있고 </src><tgt>夢だと</tgt>` | 1638 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>言っているし、</tgt>` | 1563 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>보살 로 보이 려고 </src><tgt>私だけ</tgt>` | 1927 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>우주 가졌다 </src><tgt>お坊さんに見せようと</tgt>` | 825 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>이 보살 이란 </src><tgt>宇宙が</tgt>` | 1928 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 802 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 1123 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1171 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people? This is </src><tgt>非常に幸せな人々の研究を様々な角度から行いましたか？</tgt>` | 1735 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1315 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>research. </src><tgt>これはその研究のほんの一端に過ぎません。</tgt>` | 1542 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at 10% </src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1592 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1865 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People with </src><tgt>最も幸せな人々の10%を見てみましょう。彼らは</tgt>` | 1763 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>whom we can learn from. </src><tgt>私たちから学ぶべき人たちです。</tgt>` | 1133 |

---

### Test Example 11 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body? </src><tgt>你的身体是什么？</tgt>` | 859 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>They're saying </src><tgt><\|wait\|></tgt>` | 1094 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>drop pin to your body. </src><tgt>他们说，把针头插到你的身体上。</tgt>` | 2038 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 560 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>the tension start? </src><tgt>紧张感从哪里开始？</tgt>` | 1484 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>What is it? Is it </src><tgt>是什么？</tgt>` | 1468 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>a day? </src><tgt>是某一天？</tgt>` | 1605 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it time in your chest? </src><tgt>是胸腔里的时间吗？</tgt>` | 1843 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>I have </src><tgt><\|wait\|></tgt>` | 2041 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>some language to help you </src><tgt><\|wait\|></tgt>` | 2000 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>use saying. </src><tgt>我有一些语言可以帮助你使用。</tgt>` | 940 |

---

### Test Example 12 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 </src><tgt><\|wait\|></tgt>` | 1112 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>있는 식성 들은 </src><tgt>Those with a specific diet on the list</tgt>` | 1333 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1103 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>실제로 지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1425 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1352 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>않고 무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1619 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>식성 들이었기 </src><tgt><\|wait\|></tgt>` | 1780 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>때문 입니다. </src><tgt>are actually not highly intelligent. They were selected randomly.</tgt>` | 1792 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2076 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 1884 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>모을 랐던 교사 들은 </src><tgt>The teachers who collected the sashi</tgt>` | 1126 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right, </src><tgt>好的，</tgt>` | 1128 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 1128 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>these examples, </src><tgt>这些例子之后，</tgt>` | 1218 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1316 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1230 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 643 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1333 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1475 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1449 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>它告诉我们，实际上要使用这些值。</tgt>` | 953 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1797 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>So this game.coord array </src><tgt><\|wait\|></tgt>` | 2126 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1701 |

---

### Test Example 14 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1208 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt>Advantageさん，</tgt>` | 1520 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 791 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>オーシャラーとか</src><tgt>感觉有点像</tgt>` | 1349 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>だ感じが</src><tgt>Oceaner</tgt>` | 1465 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>多いですね。海遊したい方って</src><tgt>或者喜欢在海边玩的人，</tgt>` | 1702 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐに行こう</src><tgt><\|wait\|></tgt>` | 1599 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>したい方</src><tgt>想马上</tgt>` | 1554 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 827 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>ジムで</src><tgt>去健身房</tgt>` | 1654 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>もっとトレーニングとか</src><tgt>做更多训练的人，</tgt>` | 2141 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>強いので、なので</src><tgt>所以</tgt>` | 1709 |

---

### Test Example 15 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 960 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용신이 </src><tgt><\|wait\|></tgt>` | 1170 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1169 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용신이 </src><tgt><\|wait\|></tgt>` | 1370 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설 용신이 가 </src><tgt><\|wait\|></tgt>` | 1631 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1457 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>석연 하는 건데요. </src><tgt>So, I'm a sword- element person, and the sword element is a bit awkward.</tgt>` | 2442 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1020 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 2016 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>혜경으로도 </src><tgt><\|wait\|></tgt>` | 1988 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 죽임이 되는 사람. </src><tgt>Honestly, this is a person who's a bit of a killer, even in the Hyeong-gyeong system.</tgt>` | 2166 |

---

### Test Example 16 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 865 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt><\|wait\|></tgt>` | 1033 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여 달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1286 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>죽이 려고 들어왔 수도 다. </src><tgt>They might have asked me to kill someone in a more developed country, and I might have come here to do it.</tgt>` | 2587 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 519 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 달아 </src><tgt><\|wait\|></tgt>` | 1497 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>자랑 했냐? 내가 </src><tgt>Did you brag about being in a more developed country? I</tgt>` | 1990 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt><\|wait\|></tgt>` | 1393 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>안 듣고 있는 줄 아는 거야? </src><tgt>think I'm not listening to that?</tgt>` | 2450 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1954 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1750 |

---

### Test Example 17 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 847 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>Aが</src><tgt>So, A</tgt>` | 1147 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>あるんですね。いろんな場面で</src><tgt>exists. In various situations,</tgt>` | 1378 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>静止画とか動画</src><tgt><\|wait\|></tgt>` | 1322 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>作成する時に</src><tgt>when creating still images or videos,</tgt>` | 1504 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>Aの欄を</src><tgt><\|wait\|></tgt>` | 1452 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>静止画とか動画</src><tgt><\|wait\|></tgt>` | 1655 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を生成する静止画</src><tgt><\|wait\|></tgt>` | 1374 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>ということで保証する</src><tgt><\|wait\|></tgt>` | 1152 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1968 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt>it's used to ensure that the A field is checked when generating still images or videos.</tgt>` | 1988 |

---

### Test Example 18 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 859 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1161 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>緩むと</src><tgt>기어가 헐거워지면</tgt>` | 1469 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えが</src><tgt><\|wait\|></tgt>` | 675 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>신호가 꺼져서</tgt>` | 1228 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | 1475 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1725 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1565 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt>역나사 너트가 붙어있다는 뜻입니다.</tgt>` | 2149 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>그렇죠?</tgt>` | 1892 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src>はい、</src><tgt>네,</tgt>` | 656 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | 1789 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 843 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 1078 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>在女高中生与长相不够的人之间</src><tgt><\|wait\|></tgt>` | 1657 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 956 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>有种矛盾心理，</src><tgt>If a female high school student has a contradictory feeling between being with someone who is physically attractive and someone who isn't,</tgt>` | 2562 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>is it possible that</tgt>` | 550 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1599 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天而异</src><tgt><\|wait\|></tgt>` | 1642 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>it starts from the heavens?</tgt>` | 1881 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 762 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1932 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>学历偏，</src><tgt>Yang Zisi is</tgt>` | 1921 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 679 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 1153 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1193 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>鬼岛，</src><tgt>저를 귀섬으로 데려가 주세요.</tgt>` | 1523 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1342 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>保持它安全的时候，</src><tgt>그곳에서 안전하게 지낼 수 있도록</tgt>` | 1674 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在所日</src><tgt><\|wait\|></tgt>` | 1592 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>唐日历</src><tgt>태양력으로</tgt>` | 1599 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之外，</src><tgt>날짜를</tgt>` | 1705 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时被掏出</src><tgt>빼내고</tgt>` | 785 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的小小</src><tgt><\|wait\|></tgt>` | 2087 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>的愿望哈。</src><tgt>작은 소원을 빌 수 있게 해 주세요.</tgt>` | 2034 |

---

### Test Example 21 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个</src><tgt>二つ目は</tgt>` | 880 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是指</src><tgt><\|wait\|></tgt>` | 1109 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>二吉时，</src><tgt>二吉時、</tgt>` | 1217 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会福</src><tgt><\|wait\|></tgt>` | 1319 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一吉一线</src><tgt><\|wait\|></tgt>` | 1256 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>平安的大牛们。</src><tgt>平安の大牛たちです。</tgt>` | 636 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说，</src><tgt>例えば、</tgt>` | 1260 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1534 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>维信运动好事期间，</src><tgt>維信運動の好事期間に</tgt>` | 1703 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt>すると、</tgt>` | 692 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>维信运动</src><tgt><\|wait\|></tgt>` | 1808 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>和平分的星棒</src><tgt>維信運動の星棒が</tgt>` | 2272 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>反而活了。</src><tgt>逆に活きてくるんです。</tgt>` | 2096 |

---

### Test Example 22 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 1097 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1150 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただくというようなものも</src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 1456 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ご参加ください。</src><tgt>We also have T-shirts and other items available for you to pick up, so please feel free to join us.</tgt>` | 1722 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt>For contact,</tgt>` | 1633 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>that's all.</tgt>` | 1590 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1913 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>何しろ</src><tgt><\|wait\|></tgt>` | 776 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>何しろ内側がありますので、</src><tgt>Also, since there's an inner layer,</tgt>` | 2182 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>少々お待ちください。</src><tgt>please wait a moment.</tgt>` | 2134 |

---

### Test Example 23 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 923 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこ</src><tgt>자, 여기</tgt>` | 1109 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt>에서</tgt>` | 1137 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>think to set up 7.8GB </src><tgt>7.8GB를</tgt>` | 1543 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>가 </src><tgt>설정해 두면</tgt>` | 1377 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>되었습니다. </src><tgt>됩니다.</tgt>` | 1469 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1446 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>ハセキエヨシの</src><tgt>하세키에요시의</tgt>` | 898 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>仕組みは</src><tgt>구조는</tgt>` | 1222 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>もうコン、</src><tgt>이미</tgt>` | 1848 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1179 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>セツビジージー</src><tgt><\|wait\|></tgt>` | 1526 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>ゴビです。</src><tgt>컨, 세츠비지이지 고비입니다.</tgt>` | 2331 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 971 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Chunah Terug. </src><tgt>제 이름은 츄나 테루입니다.</tgt>` | 1895 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1291 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 602 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in international business finance </src><tgt><\|wait\|></tgt>` | 1476 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a major of psychology. </src><tgt>현재 국제 비즈니스 금융과 심리학을 전공하고 있습니다.</tgt>` | 1710 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1559 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yenju, </src><tgt>여기 옌주에서</tgt>` | 1691 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 2014 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>미래에는</tgt>` | 2186 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1381 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1404 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Or or if you have </src><tgt>あるいは、</tgt>` | 995 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何か書く必要がある場合、</tgt>` | 1308 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>テキストを書く、</tgt>` | 1371 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt>そして</tgt>` | 1344 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>全く</tgt>` | 1498 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt>スペルが</tgt>` | 1731 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>just like oh, </src><tgt>わからない、</tgt>` | 1575 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>is this word </src><tgt>「ああ、この単語は</tgt>` | 871 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with a double </src><tgt><\|wait\|></tgt>` | 1703 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>p, </src><tgt>pが二つで始まる</tgt>` | 2173 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double l, </src><tgt>double l、</tgt>` | 1828 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src>I don't know. </src><tgt>わからない、</tgt>` | 1053 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber </src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>band, </src><tgt>고무줄처럼</tgt>` | 1147 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt>화학 결합도</tgt>` | 1297 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. And when those </src><tgt>에너지를 저장합니다. 그리고</tgt>` | 1346 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>bonds are broken, </src><tgt>결합이 끊어지면</tgt>` | 1487 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy gets </src><tgt>그 잠재 에너지가</tgt>` | 1526 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1588 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>converted to other types of energy, </src><tgt>다른 종류의 에너지로</tgt>` | 1823 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>변환됩니다. 예를 들어 열이나 빛 같은 것들이죠.</tgt>` | 2432 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>또는</tgt>` | 1932 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make different bonds, </src><tgt>다른 결합을 만드는 데 사용되기도 합니다.</tgt>` | 2351 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 802 |

---

### Test Example 27 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 968 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then,</tgt>` | 1273 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>毫无波澜，</src><tgt><\|wait\|></tgt>` | 1155 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1194 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>坚持不懈的</src><tgt><\|wait\|></tgt>` | 1461 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>开到七千八百</src><tgt><\|wait\|></tgt>` | 1363 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>甚至</src><tgt><\|wait\|></tgt>` | 409 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>一万以内生存一段，</src><tgt><\|wait\|></tgt>` | 1601 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 1671 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一打提腿，</src><tgt><\|wait\|></tgt>` | 1891 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>so there were no waves, no problems. So I kept going, and I survived for over 7,800, even up to 10,000. And I kept pounding the ground, and it was all fine.</tgt>` | 2954 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他能</src><tgt><\|wait\|></tgt>` | 1783 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>都很疑惑的离开。</src><tgt>He left with a lot of confusion.</tgt>` | 1008 |

---

### Test Example 28 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 864 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알 거니 뭐? </src><tgt>知っているでしょう？</tgt>` | 1247 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt>ここは異邦人</tgt>` | 1384 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>の</tgt>` | 1024 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src>말 못하는 </src><tgt>言葉が</tgt>` | 1408 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>우상에게로 </src><tgt>偶像に</tgt>` | 1233 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>거늘은 그대로 </src><tgt>なり、</tgt>` | 499 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 </src><tgt><\|wait\|></tgt>` | 1499 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>갔느니라. </src><tgt>そのまま連れて行かれてしまったのです。</tgt>` | 1667 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그럼 으로 내가 </src><tgt>そうすると、</tgt>` | 751 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너희에게 </src><tgt>私があなたたちに</tgt>` | 1789 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>知らせるのです。</tgt>` | 1940 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님의 영으로 </src><tgt>神の霊によって</tgt>` | 1159 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>話す者は</tgt>` | 1433 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 879 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 789 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>砸到了一个铁头，</src><tgt>鉄の頭にぶつかって、</tgt>` | 1896 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1072 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>打到了铁头之后，</src><tgt>鉄の頭にぶつかったら、</tgt>` | 1038 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你务必</src><tgt>必ず</tgt>` | 1143 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>主要先</src><tgt>まず</tgt>` | 1454 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>守住，</src><tgt>守ってから、</tgt>` | 381 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着</src><tgt>考えないでください。</tgt>` | 1547 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>哎，那我在</src><tgt><\|wait\|></tgt>` | 1654 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>去操作下去哦。</src><tgt>操作を続けようとしないでください。</tgt>` | 2293 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1989 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt>なぜなら、</tgt>` | 1458 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？因为呢，</src><tgt>そう言うのはなぜか？それは、</tgt>` | 1361 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1096 |

---

### Test Example 30 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 797 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150만 개가 </src><tgt>150万個が</tgt>` | 1777 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>중오분에서 1000만으로 </src><tgt>中5分から1000万で</tgt>` | 1709 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな企業が</tgt>` | 1142 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>多くありました。</tgt>` | 642 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的には</tgt>` | 1514 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>자건 업계 들은 성장 하거나 </src><tgt>財政業界は成長したり、</tgt>` | 2074 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>혹은 </src><tgt>あるいは</tgt>` | 1253 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>해화법이 </src><tgt>海洋法が</tgt>` | 1898 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>거셌다는데 일본 에 </src><tgt>強かったと聞きますが、</tgt>` | 2043 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>소기업 들은 성장 도 </src><tgt>中小企業は成長も</tgt>` | 896 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>폐업 도 하지 않는 </src><tgt>廃業もせず、</tgt>` | 2102 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>현상 들도 보이 게 된 거죠. </src><tgt>そういった現象も見られるようになったのです。</tgt>` | 1675 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1176 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>大家</src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>このローマでは、</tgt>` | 1320 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是一定要</src><tgt>必ずしも</tgt>` | 1199 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>存在的，所以呢，</src><tgt>存在するわけではありません。ですから、</tgt>` | 1536 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1487 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>所念的一些</src><tgt><\|wait\|></tgt>` | 1569 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>网页、</src><tgt><\|wait\|></tgt>` | 967 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>跟粉丝</src><tgt><\|wait\|></tgt>` | 1059 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1904 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一世之间就</src><tgt><\|wait\|></tgt>` | 1924 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的</src><tgt><\|wait\|></tgt>` | 819 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>一切会建议</src><tgt><\|wait\|></tgt>` | 1855 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>给你的朋友呢。</src><tgt>今あなたが閲覧しているウェブサイトやファンとの関係が、一世で変化するわけではないということを覚えておいてください。すべては、あなたの友人へのアドバイスとして</tgt>` | 2055 |

---

### Test Example 32 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1165 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of the </src><tgt><\|wait\|></tgt>` | 1221 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>nineteenth amendment, </src><tgt>19차 수정헌법의 의미는</tgt>` | 1765 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore </src><tgt><\|wait\|></tgt>` | 795 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>its history as a guide </src><tgt><\|wait\|></tgt>` | 1492 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help political </src><tgt><\|wait\|></tgt>` | 1499 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change </src><tgt><\|wait\|></tgt>` | 1663 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 1582 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 정치적 변화를 돕는 지침서로서, 19차 수정헌법의 의미와 역사를 탐구해 보겠습니다.</tgt>` | 2687 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1911 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt>이 수정헌법의 의미는</tgt>` | 1727 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of course I'm </src><tgt><\|wait\|></tgt>` | 1156 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>Mary Reed. </src><tgt>제가 메리 리드입니다.</tgt>` | 1358 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 845 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>这章的部分，我们看到的是</src><tgt>이 장의 부분은</tgt>` | 1764 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 684 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>个戴庙的人，但是</src><tgt>사원 모자를 쓴 사람을 보는데,</tgt>` | 1529 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>他是属于逆向的。</src><tgt>그는 역방향에 속합니다.</tgt>` | 1385 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1407 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>这通场嘛，</src><tgt>이 통장(통장)이</tgt>` | 1877 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>这样一个状况</src><tgt>이런 상황을</tgt>` | 1536 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>需要去特别注意</src><tgt>특별히 주의해야 할</tgt>` | 2014 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能</src><tgt>점은,</tgt>` | 1947 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 734 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>得到与他</src><tgt><\|wait\|></tgt>` | 1850 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>掉不到与你</src><tgt><\|wait\|></tgt>` | 839 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>的意识。</src><tgt>그가 당신의 의식을</tgt>` | 1272 |

---

### Test Example 34 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 918 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이런 것들은 </src><tgt><\|wait\|></tgt>` | 1180 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유전 실링과 </src><tgt><\|wait\|></tgt>` | 1436 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 거진 </src><tgt><\|wait\|></tgt>` | 1137 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산 한 적인 </src><tgt><\|wait\|></tgt>` | 1489 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>물질 들은 굉장히 </src><tgt><\|wait\|></tgt>` | 1498 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다. </src><tgt>These things, like vanadium, are very rich in genetic sealing and are naturally very rich in minerals.</tgt>` | 2286 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1771 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>굉장히 잘 들어와요. </src><tgt>They are also very well-formed.</tgt>` | 2292 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이거 그런 거죠. </src><tgt>That's what it is.</tgt>` | 2278 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>이제 그 후에다가 </src><tgt>And then,</tgt>` | 979 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 932 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 835 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃，</src><tgt>呃，</tgt>` | 1076 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HJM이라고 하는 </src><tgt><\|wait\|></tgt>` | 1272 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1288 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt>计算机也能理解，</tgt>` | 1478 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt>人</tgt>` | 1303 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt>也能理解</tgt>` | 547 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt>计算机语言，</tgt>` | 1622 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1569 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 역할. 우리가 이제 </src><tgt>语法的作用。我们现在</tgt>` | 2141 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1982 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>要写代码，</tgt>` | 787 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1873 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 965 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要一个程序来编写这些代码。</tgt>` | 1148 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1115 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>is just getting going </src><tgt><\|wait\|></tgt>` | 1217 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1324 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and I have ten of them </src><tgt>誰かがこれから始める必要がある、そして</tgt>` | 1656 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that are really </src><tgt>本当に</tgt>` | 1358 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>important. </src><tgt>重要な10個あると、</tgt>` | 1670 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1476 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>やってみる。</tgt>` | 811 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1908 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt>1分間の動画を</tgt>` | 2052 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video. </src><tgt>作ります。これはこの動画の続きです。</tgt>` | 1880 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage of </src><tgt><\|wait\|></tgt>` | 1016 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>each one </src><tgt><\|wait\|></tgt>` | 1077 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, </src><tgt>それぞれの内容をもう少し詳しく</tgt>` | 617 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new, </src><tgt>没什么新意，</tgt>` | 993 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>there </src><tgt><\|wait\|></tgt>` | 1074 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1214 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>was such an episode before. </src><tgt>以前也有过这样的节目。</tgt>` | 1477 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1355 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>Netflix, </src><tgt><\|wait\|></tgt>` | 1486 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>True, </src><tgt><\|wait\|></tgt>` | 1321 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src>so this is just </src><tgt><\|wait\|></tgt>` | 655 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1569 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>Netflix，没错，所以这只是另一个地方看。它</tgt>` | 2373 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2038 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1698 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 940 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>at Google should be </src><tgt><\|wait\|></tgt>` | 1209 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt>但谷歌的开发者或工程师应该知道这一点。</tgt>` | 766 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt><\|wait\|></tgt>` | 1216 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>あったら</src><tgt><\|wait\|></tgt>` | 1107 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>恐らく10秒で</src><tgt><\|wait\|></tgt>` | 1390 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ1秒</src><tgt>比如12手，大概10秒，</tgt>` | 1588 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>後に</src><tgt>然后</tgt>` | 1333 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>1秒ぐらいの</src><tgt>大概1秒钟</tgt>` | 1600 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間</src><tgt><\|wait\|></tgt>` | 1456 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>なんですかね。</src><tgt>左右，对吧？</tgt>` | 750 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1818 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1951 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>12手</src><tgt><\|wait\|></tgt>` | 794 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt>大概12手，</tgt>` | 1966 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 826 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮沼とかが</src><tgt>宫沼他们</tgt>` | 1152 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから</src><tgt>那边</tgt>` | 898 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>財運についてですが、</tgt>` | 1065 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个财运可以说是</src><tgt>この財運は</tgt>` | 1259 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>很难的，但是</src><tgt>難しいと言っても過言ではありませんが、</tgt>` | 1485 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分</src><tgt>正財の部分が</tgt>` | 937 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>尤其是在事业方面的</src><tgt>特に仕事面では、</tgt>` | 1608 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩长达数代的红利，</src><tgt>数代にわたる業績の恩恵があります。</tgt>` | 2287 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>以及收入的</src><tgt>また、収入の</tgt>` | 1169 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>提升，</src><tgt>向上、</tgt>` | 1911 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>如果是在投资理财方面</src><tgt>投資や資産運用に関しては、</tgt>` | 2122 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 721 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是相对</src><tgt>悪くないですが、</tgt>` | 2070 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>增财来说，</src><tgt>財運を増やすという点では、</tgt>` | 1333 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>少し弱めです。</tgt>` | 711 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt>少しだけです。</tgt>` | 872 |

---

### Test Example 40 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 1252 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1110 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt><\|wait\|></tgt>` | 1292 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1474 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>학력 수준. 실제로 교육을 얼마나 받았나요? 고등학교를 졸업했나요?</tgt>` | 1858 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1670 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>attainment. </src><tgt>그건 한 단계의 학력입니다.</tgt>` | 1592 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>대학에 갔나요?</tgt>` | 2214 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>And so, did you graduate </src><tgt>그래서</tgt>` | 1969 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>that's another level of </src><tgt>졸업했나요? 그건 또 다른 단계의</tgt>` | 1621 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment? </src><tgt>학력인가요?</tgt>` | 1004 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for now. </src><tgt>지금은 여기까지입니다.</tgt>` | 1213 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>I'll see you </src><tgt>다음에 뵙겠습니다.</tgt>` | 831 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서요.</tgt>` | 883 |

---

### Test Example 41 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 932 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1125 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining </src><tgt><\|wait\|></tgt>` | 1182 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>what we think that standard is, </src><tgt>自分たちがその基準をどう考えているか、</tgt>` | 1653 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>because you're absolutely correct </src><tgt>なぜなら</tgt>` | 1399 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src>but the reality </src><tgt>その基準は完全に正しいけれど、</tgt>` | 1471 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt>現実には</tgt>` | 1479 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>私たちは</tgt>` | 1455 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the box, </src><tgt>箱の中の新しい猫だから、</tgt>` | 922 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed. </src><tgt>そして基準が変わったから。</tgt>` | 1911 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1798 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>From twenty years ago, </src><tgt>20年前に</tgt>` | 904 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt>私たちは</tgt>` | 1794 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>our standard </src><tgt>自分たちの基準に縛られている。</tgt>` | 964 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>なぜなら、今の時点では</tgt>` | 1109 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 896 |

---

### Test Example 42 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt>그렇다면</tgt>` | 1072 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>濡らせてやる</src><tgt>젖게 해줄게.</tgt>` | 1232 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1114 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1295 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>引き締めを見ても</src><tgt>나는</tgt>` | 1235 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 560 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>이미 한계가</tgt>` | 1422 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1519 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>ふれふれ奇跡を</src><tgt>넘어선 기적을</tgt>` | 1816 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1846 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 749 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船出を</src><tgt><\|wait\|></tgt>` | 1918 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってる。</src><tgt>오랫동안 배를 몰고 다녔어.</tgt>` | 2313 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 841 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい海賊船を</src><tgt><\|wait\|></tgt>` | 1194 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>나는 이렇게 대단한 해적선을 본 적이 없어.</tgt>` | 1064 |

---

### Test Example 43 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>けそ</src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>もちろん、</tgt>` | 844 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt>このようなケースもあります。私たちは</tgt>` | 1470 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>Aという人と</tgt>` | 1336 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>비란 사람 이 </src><tgt>Bという人が</tgt>` | 1243 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 퀀텀 텐트예요. </src><tgt>お互いに量子テントです。</tgt>` | 1364 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이게 컨설턴트 </src><tgt><\|wait\|></tgt>` | 651 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>이어가지고 </src><tgt>これがコンサルタントに繋がって、</tgt>` | 1832 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aという人が</tgt>` | 1556 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 2264 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>들었을 때 </src><tgt>悪性コードを</tgt>` | 2122 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비란 사람이 </src><tgt>受けた人が</tgt>` | 1716 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1028 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로 사이트 스크립트에서 </src><tgt>実際にクロスサイトスクリプトで</tgt>` | 1468 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>XSP까지 </src><tgt><\|wait\|></tgt>` | 791 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>가능히 될까? </src><tgt>XSPまで</tgt>` | 527 |

---

### Test Example 44 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어, 어찌 보면 </src><tgt>嗯，从某种角度看，</tgt>` | 1787 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 975 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 952 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1473 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그리고 가족 같은 </src><tgt><\|wait\|></tgt>` | 1470 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>他就是我们一起度过二十岁的弟弟，也是我们像家人一样的弟弟。</tgt>` | 2135 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt>所以</tgt>` | 1336 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt>呃，</tgt>` | 1840 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생감모다는 </src><tgt>“再生感”</tgt>` | 887 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1875 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt>是自己</tgt>` | 1740 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1014 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1247 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 내려놓고 </src><tgt>放下很多东西，</tgt>` | 680 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt>希望自己能</tgt>` | 735 |

---

### Test Example 45 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知</src><tgt><\|wait\|></tgt>` | 1291 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1149 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>真实意图的。</src><tgt>相手の感情や真意を察知すること。</tgt>` | 1520 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1286 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1473 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt>よく</tgt>` | 1583 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>听到人们这样说：</src><tgt>人々がこう言っているのを聞きます。</tgt>` | 1575 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 688 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>見てください。</tgt>` | 1927 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt>この人は</tgt>` | 1873 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>躲黄了。</src><tgt>黄連れになっているんです。</tgt>` | 900 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>彼の目は</tgt>` | 1654 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>すべてを物語っています。</tgt>` | 837 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1216 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是</src><tgt>つまり、</tgt>` | 920 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt>そう言っているんです。</tgt>` | 660 |

---

### Test Example 46 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて</tgt>` | 1210 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세모라 </src><tgt><\|wait\|></tgt>` | 1166 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>セモラを</tgt>` | 1194 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이게 </src><tgt><\|wait\|></tgt>` | 1254 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>소름이 돋는 차리 돋는 </src><tgt>見ます。鳥肌が</tgt>` | 1680 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>느낌 이 온다. </src><tgt>立つような感覚が来ます。</tgt>` | 1546 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 </src><tgt><\|wait\|></tgt>` | 1580 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>흔들어서 같이 놀자는 거야. </src><tgt>これを揺らして一緒に遊ぼうというのです。</tgt>` | 1967 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 2025 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>오면 올릴 거고 </src><tgt>お化けが来たら</tgt>` | 2206 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>시니 오면 </src><tgt>上がって、</tgt>` | 1682 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>너 지켜주라고 </src><tgt>お化けが来たら「お前を守ってくれ」</tgt>` | 1451 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>인찔러주라고 하니까 </src><tgt>って言われるから、</tgt>` | 1277 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안한 마음 에 </src><tgt>気持ちが</tgt>` | 887 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>楽になるよ。目を閉じて。</tgt>` | 738 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 957 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인상 하는 </src><tgt><\|wait\|></tgt>` | 1134 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1344 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1287 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1351 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>어 큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1591 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 먼저 </src><tgt><\|wait\|></tgt>` | 1579 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1618 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 705 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt>If the stock market index is showing an upward trend, we might see some large- cap stocks lead the way with a big surge. But first, these lighter stocks</tgt>` | 3235 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt>move the market first.</tgt>` | 911 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1823 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시 총이 </src><tgt><\|wait\|></tgt>` | 964 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1335 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 될 것 같습니다. </src><tgt>So, it seems we need to look at the total liquidity of these lighter stocks.</tgt>` | 1306 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 462 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>드러가 면 </src><tgt><\|wait\|></tgt>` | 1210 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 해명 이다. </src><tgt>这简直是天大的辩解。</tgt>` | 1891 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1073 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 802 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1391 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1459 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1728 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1625 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가면 또 장렬 이요. </src><tgt>说他们开车过来，然后走路过来，那去江南区，更是无话可说，去国外，更是惨烈。</tgt>` | 2541 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2060 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>좀 챙기 냐요? </src><tgt>他们要多注意点吗？</tgt>` | 2027 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>대신 에 이제 </src><tgt>不如</tgt>` | 857 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 열심히 </src><tgt>现在</tgt>` | 1289 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>노래 봐요. </src><tgt>好好看个歌吧。</tgt>` | 759 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>그거 는 </src><tgt>那</tgt>` | 529 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>말한 것 같아요. </src><tgt>好像是这么说的。</tgt>` | 646 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt>And this is,</tgt>` | 1067 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1259 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうのが</src><tgt>the visual development environment.</tgt>` | 1098 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>出じゃなくて</src><tgt><\|wait\|></tgt>` | 1279 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>It's not called Visual Python development environment; it's just Visual Python.</tgt>` | 1824 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1338 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアル</src><tgt><\|wait\|></tgt>` | 1636 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>の書いて後、それから</src><tgt><\|wait\|></tgt>` | 1749 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードを</src><tgt><\|wait\|></tgt>` | 1931 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成させるっていうのが</src><tgt><\|wait\|></tgt>` | 1764 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 874 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1865 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことをしている</src><tgt><\|wait\|></tgt>` | 866 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 1233 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt>So, this is what it's called. It's a visual Python development environment. It's not called Visual Python development environment; it's just Visual Python. This is where you write a flow graph, then write Python code, and it generates it, which then executes and performs signal processing.</tgt>` | 1933 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ</src><tgt>So,</tgt>` | 557 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そして、これについて</tgt>` | 784 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>多くの人が</tgt>` | 1137 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석 을 해놓았습니다. </src><tgt>分析をしています。</tgt>` | 1343 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 1142 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>이 로쿠자 앱 분석 을 보시면 </src><tgt>このロクザアプリの分析を見ると、</tgt>` | 1727 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니 가 </src><tgt>ソニーが</tgt>` | 1394 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>이오렉트의 </src><tgt><\|wait\|></tgt>` | 1779 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>FPP 파이프 를 </src><tgt><\|wait\|></tgt>` | 1677 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 2101 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>나충가서 로 포인트 다. </src><tgt>iORECTのFPPパイプを128ビットに変換してポイント化しています。</tgt>` | 2662 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 2039 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt>Xboxにもない</tgt>` | 1296 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 787 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>S2 </src><tgt><\|wait\|></tgt>` | 868 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>가 여기 도 없다. </src><tgt>インフィニットキャッシュS2もありません。ここにもありません。</tgt>` | 846 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 452 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1019 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, you will not </src><tgt>另外，</tgt>` | 1219 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1166 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1282 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1433 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1306 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>though, </src><tgt>虽然你不能在资源之间移动媒体对象，</tgt>` | 603 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 1578 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where you </src><tgt><\|wait\|></tgt>` | 1599 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1939 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1409 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular </src><tgt><\|wait\|></tgt>` | 1204 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>resource, we'll let us know. </src><tgt>但如果你发现把错误的媒体文件添加到了某个资源中，我们会通知你。</tgt>` | 2692 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>And we can see about </src><tgt>我们也可以</tgt>` | 1251 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those media </src><tgt><\|wait\|></tgt>` | 452 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>files and then making sure </src><tgt>看看如何移动这些媒体文件，</tgt>` | 1052 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 510 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>确保它们被正确备份。</tgt>` | 600 |

---

### Test Example 52 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1161 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 ` | 11381 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1903 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 779 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 죠깅 </src><tgt><\|wait\|></tgt>` | 1826 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>해르나 </src><tgt><\|wait\|></tgt>` | 1043 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 910 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한성 과 </src><tgt><\|wait\|></tgt>` | 887 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 714 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt>I am Apple. I am a generation like Haruna, Park Han-seong, and others.</tgt>` | 745 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 817 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>for all the sorts </src><tgt><\|wait\|></tgt>` | 1201 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>that we've just discussed, </src><tgt>방금 논의한 모든 종류의</tgt>` | 1986 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 604 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but when we study </src><tgt>것들을 살펴보면,</tgt>` | 1475 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>the relationship, </src><tgt><\|wait\|></tgt>` | 1380 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>the kind of love </src><tgt><\|wait\|></tgt>` | 1664 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1514 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>that we often</src><tgt><\|wait\|></tgt>` | 648 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>often enter </src><tgt><\|wait\|></tgt>` | 1927 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>in our lives </src><tgt><\|wait\|></tgt>` | 1889 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>as love. </src><tgt>우리가 종종 사랑에 빠지는 관계를 연구해 보면, 우리가 사랑에 빠지는 방식은</tgt>` | 1997 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>It comes to the end. </src><tgt>결국에는 다들 똑같습니다.</tgt>` | 1388 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>It becomes </src><tgt><\|wait\|></tgt>` | 1120 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that kind of </src><tgt><\|wait\|></tgt>` | 1037 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>love. </src><tgt>그것이 바로 그런 사랑이 됩니다.</tgt>` | 755 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 602 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>It continues to evolve. </src><tgt>그리고 계속해서 발전해 나갑니다.</tgt>` | 586 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1265 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt>最初の数マイルは</tgt>` | 1239 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1148 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt><\|wait\|></tgt>` | 1232 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>AHR field, </src><tgt><\|wait\|></tgt>` | 1442 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1319 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 434 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1470 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant </src><tgt><\|wait\|></tgt>` | 1397 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>databases, </src><tgt><\|wait\|></tgt>` | 680 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously for my loves. </src><tgt>AHR分野の最初の数マイルは、バリアントデータベースの重要性についてでした。もちろん、これは私の愛する人たちのためのものです。</tgt>` | 3379 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt>それは、</tgt>` | 882 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1907 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that </src><tgt>フィールドについて合意できない場合、</tgt>` | 1139 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>need to be in these </src><tgt><\|wait\|></tgt>` | 1211 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>これらのデータソースに含める必要があるフィールドについて合意できない場合、</tgt>` | 1181 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from. </src><tgt>それらはどこから取得できるのか、という問題です。</tgt>` | 789 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, right? </src><tgt>そこから取得できるものがない、ということですよね？</tgt>` | 690 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 358 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point, </src><tgt>ある時点で、</tgt>` | 820 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>He knows Jesus </src><tgt><\|wait\|></tgt>` | 1135 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is a hungry </src><tgt>イエスが</tgt>` | 1150 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>and knows that </src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he's supposed to </src><tgt>飢えていることを知っている。そして、</tgt>` | 1535 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1497 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>for forty days that he's hungry, </src><tgt>40日間飢え続けていることを知っている。</tgt>` | 2054 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>and so he says to </src><tgt>だから彼は</tgt>` | 1512 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>Jesus, say, </src><tgt>イエスにこう言ったんだ。</tgt>` | 2272 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, </src><tgt>「もしあなたが</tgt>` | 2269 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt>神の子なら証明してみせろ。」</tgt>` | 2284 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread. </src><tgt>「この石をパンに変えろ。」</tgt>` | 1302 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt>イエスは</tgt>` | 730 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>deal with that </src><tgt><\|wait\|></tgt>` | 856 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>その誘惑にどう対処したのか？</tgt>` | 758 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 586 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Man, </src><tgt>いやあ、</tgt>` | 450 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>Jonathan led by the stone. </src><tgt>ジョナサンが石で導いたんだ。</tgt>` | 544 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1215 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1107 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1173 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt>有意义的个人权利，而最高法院则最后介入。</tgt>` | 1562 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I I don't know </src><tgt><\|wait\|></tgt>` | 1640 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>if the courts want to be </src><tgt>我不知道法院是否想</tgt>` | 1728 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1572 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1848 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change, </src><tgt>成为社会变革的先锋。</tgt>` | 886 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>these days. </src><tgt>如今，</tgt>` | 1808 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt>但他们更倾向于</tgt>` | 1898 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 948 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1275 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 709 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged </src><tgt><\|wait\|></tgt>` | 561 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>so. </src><tgt>反映已经形成的共识。</tgt>` | 627 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt>你</tgt>` | 550 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt>有</tgt>` | 467 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 362 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 338 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我們看一下</src><tgt>자, 그럼</tgt>` | 936 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>一下</src><tgt>이 그림을</tgt>` | 1122 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它的图片呢？</src><tgt>한번 살펴볼게요.</tgt>` | 1254 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>그림 부분은</tgt>` | 1391 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我們可以看到的一个是</src><tgt>클래식한</tgt>` | 1460 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>克汀的部分，</src><tgt>부분이 보입니다.</tgt>` | 1492 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>而克汀一般</src><tgt>그리고</tgt>` | 1535 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是属于</src><tgt><\|wait\|></tgt>` | 881 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1112 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>在修饰的地方，</src><tgt>보통 우리가</tgt>` | 1972 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt>장식하는 부분에 사용되는데,</tgt>` | 2038 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分。</src><tgt>이건 신체 부분입니다.</tgt>` | 930 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>它会反映的是</src><tgt>이것은</tgt>` | 1906 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你想要给</src><tgt><\|wait\|></tgt>` | 1142 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 843 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好的</src><tgt><\|wait\|></tgt>` | 858 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>做下来修饰，</src><tgt><\|wait\|></tgt>` | 727 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>可以看到</src><tgt><\|wait\|></tgt>` | 580 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>这边是五个人的嘛。</src><tgt>자신에게 시간을 들여 장식할 수 있도록 하기 위해 사용됩니다. 여기 다섯 명의 사람입니다.</tgt>` | 778 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt>자,</tgt>` | 323 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>그래서</tgt>` | 238 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 858 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare. </src><tgt>彼らは全く珍しい人々です。</tgt>` | 1502 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 853 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1270 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1459 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>そして彼らは世界を完全に変革するために現れることがよくあります。</tgt>` | 1712 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 1599 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>personality is </src><tgt>その個性は</tgt>` | 1606 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾したものです。</tgt>` | 1692 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 795 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 1954 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的ですが、</tgt>` | 1258 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1310 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>hate meaningless conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 1513 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 541 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it gets straight to the </src><tgt><\|wait\|></tgt>` | 856 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>point. </src><tgt>そして要点をまっすぐ伝えます。</tgt>` | 720 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 594 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 546 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>and they </src><tgt><\|wait\|></tgt>` | 303 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 361 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>彼らは議論を恐れることはありません。また、</tgt>` | 449 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 323 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E&P </src><tgt><\|wait\|></tgt>` | 287 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stands for. </src><tgt>E&Pは</tgt>` | 367 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 의 이준석은 </src><tgt>Lee Jun-seok, before this,</tgt>` | 1142 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>정무를 거부 한 </src><tgt><\|wait\|></tgt>` | 1115 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1085 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1199 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1468 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1509 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1645 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1696 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 776 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제관 순간 </src><tgt><\|wait\|></tgt>` | 1968 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석 은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1903 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1137 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 1324 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기 를 품은 </src><tgt><\|wait\|></tgt>` | 1023 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 684 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 506 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 277 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>것입니다. </src><tgt>He used the excuse of refusing political duties to win the nomination, and even showed off a bit. But now, Yoon Suk-yeol, the presidential candidate, has taken Kim Jong-in as his own. Lee Jun-seok, after hearing this, is plotting to defeat Yoon Suk-yeol, harboring malice and showing an aggressive intent.</tgt>` | 1367 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 285 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석 성상납금 </src><tgt><\|wait\|></tgt>` | 330 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 244 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당의 </src><tgt><\|wait\|></tgt>` | 369 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 에 얼마나 </src><tgt><\|wait\|></tgt>` | 300 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 입니까? </src><tgt>How much of a boon is Lee Jun-seok's personal income? How much of a boon is the Democratic Party's attack?</tgt>` | 541 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt>Well, right now</tgt>` | 789 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt>I want to make something after dinner.</tgt>` | 1458 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt>So,</tgt>` | 955 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 684 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスローンホテルも</src><tgt><\|wait\|></tgt>` | 1483 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1528 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1532 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので、</src><tgt>I've heard that Golf Sloan Hotel is a place where you can have breakfast, so</tgt>` | 2011 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt>from now on,</tgt>` | 1992 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルフスローンホテル</src><tgt><\|wait\|></tgt>` | 2116 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 755 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt>if you're thinking of staying at Golf Sloan Hotel,</tgt>` | 1989 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1164 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみて、まあいいんじゃない</src><tgt>take a look— I mean, it's not a bad idea.</tgt>` | 1140 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt>So,</tgt>` | 503 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt>I think so.</tgt>` | 635 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>ここホテルからですね</src><tgt>From this hotel,</tgt>` | 604 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 487 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 373 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 352 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんな</src><tgt><\|wait\|></tgt>` | 343 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>かそんなレベルのね</src><tgt><\|wait\|></tgt>` | 332 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいね、まあホテル</src><tgt>the Busan Station is just a minute away on foot. It's a great location.</tgt>` | 465 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt>So,</tgt>` | 289 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>if you'd like,</tgt>` | 316 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさって</src><tgt>please consider it.</tgt>` | 326 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>みてください。それなら</src><tgt>If that's the case,</tgt>` | 292 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>ね今回は</src><tgt>this time,</tgt>` | 177 |
