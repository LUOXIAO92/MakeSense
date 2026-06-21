# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9930
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.9007
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 8
  - TARGET_METRICS_FILTERED_TURN_COUNT: 123
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 52
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 131
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 615
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1282.0420
  - PROCESS_TIME_MS_P50: 1266.9980
  - PROCESS_TIME_MS_P95: 2063.3950
  - PROCESS_TIME_MS_MAX: 3865.1760

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1330 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 725 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1164 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1362 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>Students in the fated positions</tgt>` | 1107 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1486 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1334 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>어떤 분입 니다. </src><tgt><\|wait\|></tgt>` | 1456 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1035 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>사실 을 모르 았 던 </src><tgt>were not actually highly intelligent. They were students selected at random. In fact,</tgt>` | 2317 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | 1443 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1051 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 1103 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | 1125 |
| 5 | `<src><\|wait\|></src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>知道</src><tgt>気性が熟すのは簡単です。でも、師匠が</tgt>` | 1403 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如何趋于</src><tgt><\|wait\|></tgt>` | 1466 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>终点，</src><tgt><\|wait\|></tgt>` | 1490 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1364 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>虚招凡，</src><tgt><\|wait\|></tgt>` | 1028 |
| 10 | `<src>要成为</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>要成为</src><tgt>ゴールにどう近づくかを知っているのは一人だけ。だから、虚招凡、</tgt>` | 2257 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | 1471 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 818 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 818 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 1268 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1093 |
| 5 | `<src>この時点で</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>この時点で</src><tgt>从一开始，特别是现在才一年级。这个时候</tgt>` | 1318 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | 1460 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1409 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1108 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | 1415 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>十年経っても</src><tgt>剪短枝、收紧枝条，即使十年后</tgt>` | 2238 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 1471 |

---

### Test Example 4 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 925 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | 836 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | 1397 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1243 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt>I triggered a heart attack</tgt>` | 1012 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1477 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | 1574 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1443 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1225 |
| 10 | `<src><\|wait\|></src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src><\|wait\|></src><tgt>and killed my own parents,</tgt>` | 1970 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | 1522 |

---

### Test Example 5 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1145 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 786 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1032 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1215 |
| 5 | `<src>ゴッホ、</src><tgt>大致是从这一带开始的，</tgt>` | `<src>ゴッホ、</src><tgt>大概是从这里开始的，</tgt>` | 1349 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 927 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 795 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1983 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1523 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt>像高更、高安、塞尚、雷诺瓦</tgt>` | 1479 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 1161 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | 1487 |

---

### Test Example 6 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1273 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | 837 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | 1556 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1185 |
| 5 | `<src><\|wait\|></src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src><\|wait\|></src><tgt>Scoop out a bit of the peanut, the oil is quite high. Then</tgt>` | 1156 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | 1351 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>核桃仁，</src><tgt><\|wait\|></tgt>` | 1666 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1265 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>感觉这样</src><tgt><\|wait\|></tgt>` | 1172 |
| 10 | `<src>这种核桃</src><tgt>Then, I'll add some walnut kernels— this kind of</tgt>` | `<src>这种核桃</src><tgt>I'll add a few more walnuts. I feel like</tgt>` | 2122 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>仁。</src><tgt><\|wait\|></tgt>` | 1437 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1209 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | 885 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | 1384 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | 1370 |
| 5 | `<src>然后</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、</tgt>` | `<src>然后</src><tgt>散布が終わると、内部の圧力が下がり、エネルギーも衰えます。そして、</tgt>` | 1763 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | 677 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>相对的低</src><tgt><\|wait\|></tgt>` | 1998 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | 1490 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态，</src><tgt><\|wait\|></tgt>` | 985 |
| 10 | `<src>这就是所谓的</src><tgt>比較的低エネルギーの状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>比較的低いエネルギーの運行状態にとどまります。これが、いわゆる</tgt>` | 1861 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | 1474 |

---

### Test Example 8 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1284 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 793 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1338 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1500 |
| 5 | `<src>爱浇水、</src><tgt>What parents need to do is this:</tgt>` | `<src>爱浇水、</src><tgt>What parents need to do is water our love</tgt>` | 1440 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 903 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1783 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | 1258 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1082 |
| 10 | `<src>并耐心等待孩子</src><tgt>water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for</tgt>` | `<src>并耐心等待孩子</src><tgt>with it— watering, fertilizing, and providing our children with the psychological nourishment they need— and patiently waiting for them</tgt>` | 3024 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 962 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 1050 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>공심 이 </src><tgt><\|wait\|></tgt>` | 849 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1264 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 공심이</src><tgt><\|wait\|></tgt>` | 1086 |
| 5 | `<src>옹심이가 </src><tgt>I'm having the ongsimi and kal- ongsimi—</tgt>` | `<src>어 혹시 공심 이가 </src><tgt>I have a ' gongsim '— a sword gongsim. Is it that</tgt>` | 1575 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞이 는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1932 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1142 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1085 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover,</tgt>` | `<src>해당 으로 </src><tgt>gets mixed in? Wow, this is</tgt>` | 2061 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금씩 밀리 는 경우 가 </src><tgt><\|wait\|></tgt>` | 1937 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 904 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1199 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1263 |
| 5 | `<src>或是通知对方，</src><tgt>In this situation, when we encounter a problem, we should</tgt>` | `<src>或是通知对方，</src><tgt>When faced with this situation, if we run into a problem, we should quickly report it to our supervisor or notify the other party.</tgt>` | 2005 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | 868 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1957 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1693 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | 1791 |
| 10 | `<src>整体而言，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall,</tgt>` | `<src>整体而言，</src><tgt>We shouldn't try to handle everything ourselves. Overall,</tgt>` | 907 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | 1640 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1016 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 791 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1324 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | 1510 |
| 5 | `<src>This is tip of the stem </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは</tgt>` | `<src>This is tip of the stem </src><tgt>非常に幸せな人たちに関する重要な研究を行いました。これは</tgt>` | 1590 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research, looking at </src><tgt><\|wait\|></tgt>` | 879 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>the 10% </src><tgt><\|wait\|></tgt>` | 2013 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1480 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1160 |
| 10 | `<src>out there, </src><tgt>最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, </src><tgt>先端の研究で、最も幸せな人々の10%を対象に、</tgt>` | 1819 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | 1641 |

---

### Test Example 12 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1078 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 852 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1068 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | 1386 |
| 5 | `<src>Find what you're good at </src><tgt>最后，要重复。学会不断重复。找到你的长处，</tgt>` | `<src>Find what you're good at </src><tgt>最后，就是重复。学会复习，反复练习。找到你擅长</tgt>` | 1569 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1310 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2024 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | 1784 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | 2079 |
| 10 | `<src><\|wait\|></src><tgt>多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>的事情，多做这些。而你不擅长的，就请身边的人帮忙。</tgt>` | 1601 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | 1207 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1408 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 684 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | 1493 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | 1420 |
| 5 | `<src>多いですね。</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。</tgt>` | `<src>多いですね。</src><tgt>嗯，渐渐地距离会拉开，感觉时尚的人反而更多。</tgt>` | 1568 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | 881 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい</src><tgt><\|wait\|></tgt>` | 1785 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | 1275 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>自分で</src><tgt><\|wait\|></tgt>` | 829 |
| 10 | `<src>全部ちょっと次の投資</src><tgt>想创业的人自我意识都很强，而且</tgt>` | `<src>全部ちょっと次の投資</src><tgt>想开店的人自我意识很强，</tgt>` | 2106 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | 1503 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので。</src><tgt><\|wait\|></tgt>` | 1114 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1241 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 742 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1161 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1143 |
| 5 | `<src>the instruction </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>the instruction </src><tgt>好的，这些例子之后，</tgt>` | 1282 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 987 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 800 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1633 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1267 |
| 10 | `<src>these values. So </src><tgt>说明告诉我们要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>说明我们要用这些值。所以</tgt>` | 1373 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1771 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | 1537 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1158 |

---

### Test Example 15 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 941 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 675 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1163 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 1129 |
| 5 | `<src>Where does the tension </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>你的身体在做什么？进入你的身体。紧张感</tgt>` | 1431 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1512 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 2131 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 1791 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | 2012 |
| 10 | `<src><\|wait\|></src><tgt>开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src><\|wait\|></src><tgt>从哪里开始？是什么感觉？是头痛吗？还是胸闷？</tgt>` | 1555 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | 1331 |

---

### Test Example 16 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1184 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 789 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1224 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1179 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>We also have items like T- shirts available,</tgt>` | 1316 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 1496 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1452 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | 1441 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1100 |
| 10 | `<src><\|wait\|></src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src><\|wait\|></src><tgt>so please do join us. That's all for the contact information.</tgt>` | 2197 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | 1560 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1233 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1102 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | 903 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1325 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1509 |
| 5 | `<src>다른 잔찜에 </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>다른 잔찜에 </src><tgt>He asked me to be killed by another method, so I came in to kill him.</tgt>` | 1812 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 689 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | 1946 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1598 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1990 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh?</tgt>` | `<src>있는 줄 알았느냐? 응? </src><tgt>Didn't I ask him to be killed by another method? Did he think I didn't hear that? Huh?</tgt>` | 1943 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | 1226 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 807 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 821 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天気</src><tgt><\|wait\|></tgt>` | 932 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>豊穣祈願が</src><tgt><\|wait\|></tgt>` | 1128 |
| 5 | `<src>ありましたね。</src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>ありましたね。</src><tgt>그렇군요. 거기서 풍요를 기원하는 의식이 있었죠.</tgt>` | 1536 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 615 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1183 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | 2123 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1457 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>は五経、</src><tgt>그리고 나가이 요시노 시크미는 5경,</tgt>` | 1720 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 908 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>摂取一時、五比</src><tgt><\|wait\|></tgt>` | 1734 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 1178 |

---

### Test Example 19 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 783 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1091 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1530 |
| 5 | `<src>調べるときに、</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area,</tgt>` | `<src>調べるときに、</src><tgt>In movies, when you're looking into whether something's native to an area in various scenes,</tgt>` | 1623 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | 1128 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | 1747 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1544 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | 951 |
| 10 | `<src>ことを保証する</src><tgt>you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>ことを保証する</src><tgt>you can guarantee it's native— you can guarantee it's native—</tgt>` | 2227 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1317 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | 1340 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 975 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 764 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1451 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>If there's some kind of connection between a high school girl and someone with a strange appearance,</tgt>` | 1970 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 690 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1813 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | 1611 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1634 |
| 10 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src><\|wait\|></src><tgt>could it have started that night?</tgt>` | 892 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 1666 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇。</src><tgt><\|wait\|></tgt>` | 1255 |

---

### Test Example 21 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 994 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kerenath Dilo. </src><tgt><\|wait\|></tgt>` | 978 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently </src><tgt><\|wait\|></tgt>` | 1340 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>studying a Bachelor of Finance </src><tgt>제 이름은 케레나스 디로입니다. 현재</tgt>` | 1593 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | 840 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1984 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | 1632 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1131 |
| 10 | `<src>and in the future, I want to go into </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>and in the future, I want to go into </src><tgt>ANU에서 금융학 학사 과정과 심리학 학사 과정을 공부하고 있습니다. 앞으로</tgt>` | 2655 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 995 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | 1554 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1107 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 795 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 932 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | 1207 |
| 5 | `<src><\|wait\|></src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이</tgt>` | `<src><\|wait\|></src><tgt>이게 기어입니다. 기어가 헐거워지면 심이</tgt>` | 1463 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | 1046 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 832 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | 2054 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1480 |
| 10 | `<src>ついているっていうことです</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>ついているっていうことです</src><tgt>위아래로 움직이지 못하게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거예요.</tgt>` | 2416 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1412 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1046 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンブレーキ完了。</src><tgt><\|wait\|></tgt>` | 1656 |

---

### Test Example 23 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1029 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 830 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1555 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1342 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、</tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt>これ、ちょっと低すぎるかもしれないけど、本当に菩薩だよ。いや、</tgt>` | 1925 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | 1038 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | 1502 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | 1824 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | 2081 |
| 10 | `<src>지금 나한테 </src><tgt>自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に</tgt>` | `<src>지금 나한테 </src><tgt>自分は菩薩なのに飾る必要はないし、誰かに菩薩に見せる必要もない。宇宙が今、私に</tgt>` | 2216 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | 1912 |

---

### Test Example 24 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 676 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 858 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1084 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | 1244 |
| 5 | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가고 싶어요.</tgt>` | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가서</tgt>` | 1446 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | 1529 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | 1530 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1044 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그가 퇴근하고 오면 뜨거운 국이나 밥을 해줘도 좋았을 텐데. 정말 그때 슬픔에 빠져 있을 때, 그게</tgt>` | 3621 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | 1305 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 1240 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1085 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 858 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | 1069 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1238 |
| 5 | `<src>history as a guide </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>제19조 수정안의 의미와</tgt>` | 1461 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1472 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1439 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 1331 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1141 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지 이해하는 가이드로서 그 역사를 살펴보겠습니다.</tgt>` | 2429 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 1471 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | 1438 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 1409 |

---

### Test Example 26 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 860 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1145 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1131 |
| 5 | `<src>坚持不开刀。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery.</tgt>` | `<src>坚持不开刀。</src><tgt>Everything was normal back then, I was full of energy, so I insisted on not having the surgery.</tgt>` | 1599 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间</src><tgt><\|wait\|></tgt>` | 1372 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | 1490 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | 1420 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | 1120 |
| 10 | `<src>一下提腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>一下提腿，</src><tgt>About ten doctors came to diagnose me during that time. They'd tap my leg, then lift it,</tgt>` | 2552 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1434 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们</src><tgt><\|wait\|></tgt>` | 1264 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1430 |

---

### Test Example 27 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 들은 거진 </src><tgt><\|wait\|></tgt>` | 865 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린 과 </src><tgt><\|wait\|></tgt>` | 1357 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1397 |
| 5 | `<src>유사 한 작용 이 </src><tgt>Things like vanadium</tgt>` | `<src>유사 한 작용 이 </src><tgt>These vanadium compounds</tgt>` | 998 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1357 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1763 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1369 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 864 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt>are so similar to insulin that they are essentially called ' diabetes minerals '.</tgt>` | 2269 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1763 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1471 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연 </src><tgt><\|wait\|></tgt>` | 1144 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 1232 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 670 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1344 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1451 |
| 5 | `<src>you realize that </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>you realize that </src><tgt>あるいは、何かを文章にする必要があるとき、つまりテキストを書く必要があるとき、</tgt>` | 1638 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | 991 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1874 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 1682 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1583 |
| 10 | `<src>spelled with a double </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>spelled with a double </src><tgt>単語の綴りが全くわからないことがありますよね。「あ、この単語、</tgt>` | 1546 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1206 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | 1899 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 793 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 1216 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | 1517 |
| 5 | `<src>and when those bonds are broken, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면</tgt>` | `<src>and when those bonds are broken, </src><tgt>늘어난 고무줄처럼 화학 결합도 에너지를 저장합니다. 그리고 그 결합이 끊어지면</tgt>` | 2318 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 2043 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1538 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1110 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 1518 |
| 10 | `<src><\|wait\|></src><tgt>잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src><\|wait\|></src><tgt>그 위치 에너지는 열이나 빛 같은 다른 에너지 형태로 바뀌는데,</tgt>` | 2126 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | 1826 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 908 |

---

### Test Example 30 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 972 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 844 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>选择二级市场，</src><tgt><\|wait\|></tgt>` | 1379 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>在一级</src><tgt><\|wait\|></tgt>` | 1026 |
| 5 | `<src>在一级一线</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で</tgt>` | `<src><\|wait\|></src><tgt>次に2つ目は、二次市場を選ぶことです。一次市場の</tgt>` | 1316 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>一级线拼杀的大牛们</src><tgt><\|wait\|></tgt>` | 1515 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | 2108 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1549 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | 1618 |
| 10 | `<src>发现</src><tgt>戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>发现</src><tgt>トップトレーダーたちは、例えば、えーと、WeChat公式アカウントを10年以上やってきた人たちです。そういった人たちは、</tgt>` | 2251 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信公众号评分的</src><tgt><\|wait\|></tgt>` | 1346 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>新榜，然后</src><tgt><\|wait\|></tgt>` | 1452 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>火了。</src><tgt><\|wait\|></tgt>` | 814 |

---

### Test Example 31 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 934 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | 1160 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | 1191 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1309 |
| 5 | `<src>많았습니다. </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。</tgt>` | `<src>많았습니다. </src><tgt>そのうち150万件は従業員数が10人未満の非常に小さな企業でした。</tgt>` | 1951 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 784 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1851 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | 1556 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | 2009 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は</tgt>` | `<src>일본 의 소기업들은 </src><tgt>一般的に小さな企業は成長するか、あるいは廃業するかのどちらかです。日本の小企業は</tgt>` | 1700 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | 1368 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | 1523 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 915 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 924 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | 869 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt><\|wait\|></tgt>` | 1033 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1235 |
| 5 | `<src>请你务必就要</src><tgt>うまくいったなと思ったらね。その時は必ず利益を</tgt>` | `<src>请你务必就要</src><tgt>良い兆しが得られたら、</tgt>` | 1257 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1461 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1367 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | 1560 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1105 |
| 10 | `<src>继续操作下去哦。</src><tgt>確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>继续操作下去哦。</src><tgt>まずはしっかり守りましょう。そうして「あ、もっと操作しよう」なんて考えないでください。</tgt>` | 2402 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1491 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1343 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1411 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 859 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1209 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 787 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | 1332 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1514 |
| 5 | `<src>所以呢，</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、</tgt>` | `<src>所以呢，</src><tgt>皆さんに忠告したいのですが、このローマは一日にしてできたものではありません。ですから、</tgt>` | 1908 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 661 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1894 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | 1575 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1205 |
| 10 | `<src>一夕之间就</src><tgt>今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>一夕之间就</src><tgt>今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | 1783 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1425 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | 1488 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1111 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | 1114 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 662 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 1346 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | 1235 |
| 5 | `<src>它是属于逆向的，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요.</tgt>` | `<src>它是属于逆向的，</src><tgt>이 사진의 이 부분은 낚시를 하는 사람인데, 역방향으로 되어 있습니다.</tgt>` | 1812 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 825 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | 2084 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | 1544 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | 1225 |
| 10 | `<src>是它能不能够</src><tgt>그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>是它能不能够</src><tgt>그래서 보통 이런 상황을 마주했을 때는 특별히 주의해야 합니다. 바로</tgt>` | 1813 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | 1453 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | 1741 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 925 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | 1030 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There were </src><tgt><\|wait\|></tgt>` | 791 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1205 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | 1190 |
| 5 | `<src><\|wait\|></src><tgt>没什么新鲜的。以前就有过这样的接口，</tgt>` | `<src><\|wait\|></src><tgt>没什么新意。以前就有这样的接口了，</tgt>` | 1323 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | 1496 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 1481 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>this is just </src><tgt><\|wait\|></tgt>` | 1471 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1053 |
| 10 | `<src>to look at. </src><tgt>比如netfilter和 TC。所以这只是另一个需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>比如netfilter、TC。所以这只是看的地方而已。</tgt>` | 2176 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1427 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1192 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1471 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | 941 |
| 15 | `<src>should be aware of that. </src><tgt>但开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>但那些在做BugRepo的开发者或工程师应该知道这一点。</tgt>` | 1350 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 735 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>H개월에 </src><tgt><\|wait\|></tgt>` | 844 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1059 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 컴퓨터 도 </src><tgt><\|wait\|></tgt>` | 1245 |
| 5 | `<src><\|wait\|></src><tgt>HTML是一种</tgt>` | `<src>이해 할 수 있고 </src><tgt>计算机也能理解“H个月”这个概念，</tgt>` | 1488 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1458 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1503 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1633 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1091 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>맞게 우리 가 이제 </src><tgt>人也能理解。所以我们按照计算机语言的语法，</tgt>` | 2191 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1611 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 1264 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1397 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1115 |
| 15 | `<src>필요 합니다. </src><tgt>我们需要按照它的语法来编写代码，而编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要写代码。写代码需要一个程序。</tgt>` | 844 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1073 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | 779 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | 1064 |
| 5 | `<src>まあ</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>まあ</src><tgt>大概是十一二手吧。十秒内。嗯，</tgt>` | 1450 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1468 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一定回というくらいの</src><tgt><\|wait\|></tgt>` | 1500 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>回転数</src><tgt><\|wait\|></tgt>` | 1415 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>みたいな</src><tgt><\|wait\|></tgt>` | 1084 |
| 10 | `<src>でなんか</src><tgt>一秒一手多一点这样算。然后</tgt>` | `<src>で、なんか</src><tgt>大概每秒有一圈左右的转速，</tgt>` | 2142 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1408 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1103 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | 1576 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 779 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮馬とかが</src><tgt>大概是十一二手，</tgt>` | 1265 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>あるから。</src><tgt><\|wait\|></tgt>` | 531 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 1003 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 925 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 1297 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1409 |
| 5 | `<src>말 못하 는 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない</tgt>` | `<src>말 못하 는 </src><tgt>あなたたちも知っているだろう。異邦人としていた時、言葉も話せなかった</tgt>` | 1950 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 753 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1758 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1669 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1911 |
| 10 | `<src>그러므로 내가 </src><tgt>偶像に引かれるままに連れて行かれました。ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>偶像へと引きずられて行った。だから、私は</tgt>` | 796 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 1527 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1426 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1244 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 1125 |
| 15 | `<src><\|wait\|></src><tgt>あなたがたに教えます。神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>あなたたちに告げます。神の霊によって語る者は……</tgt>` | 1106 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1317 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 726 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | 1437 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1356 |
| 5 | `<src>and I have ten of them </src><tgt>それは始めたばかりの人が手に入れるべきもので、</tgt>` | `<src>and I have ten of them </src><tgt>これから動き出す人には、</tgt>` | 1194 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that I think are </src><tgt><\|wait\|></tgt>` | 1207 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>really important. </src><tgt><\|wait\|></tgt>` | 1909 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1515 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | 1057 |
| 10 | `<src>I have about </src><tgt>私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I have about </src><tgt>本当に大事なこと10個くらいあると思うんです。その中から、</tgt>` | 2063 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1476 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | 1336 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1267 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | 1102 |
| 15 | `<src>in a little more detail, but. </src><tgt>この動画の後に、それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, but. </src><tgt>この動画の後に1分程度の動画をいくつか用意しました。それぞれをもう少し詳しく解説するものです。でも、</tgt>` | 1406 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 817 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1360 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | 1428 |
| 5 | `<src>也就是</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり</tgt>` | `<src>也就是</src><tgt>金運についてですが、今月はとても良いと言えます。ただ、正の収入に</tgt>` | 1846 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | 626 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | 2045 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>与收入的</src><tgt><\|wait\|></tgt>` | 1447 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | 1370 |
| 10 | `<src>投资理财方面呢，</src><tgt>仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>投资理财方面呢，</src><tgt>関連するものです。つまり、仕事の業績向上や収入アップによる恩恵ですね。投資や資産運用に関しては、</tgt>` | 2469 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1180 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1536 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | 1022 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | 994 |
| 15 | `<src><\|wait\|></src><tgt>悪くはないんですが、本業の収入に比べると少し弱めですね。</tgt>` | `<src><\|wait\|></src><tgt>今月も悪くありません。ただ、正の収入と比べると少しだけ弱めかもしれません。</tgt>` | 944 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1247 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 769 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1439 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1356 |
| 5 | `<src>actually go in your education? Did you </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>actually go in your education? Did you </src><tgt>학력. 학업을 얼마나 마쳤나요?</tgt>` | 1500 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 926 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1752 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | 1702 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>to college, </src><tgt><\|wait\|></tgt>` | 1000 |
| 10 | `<src>and if so, did you graduate? </src><tgt>고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>and if so, did you graduate? </src><tgt>고등학교 졸업은 하셨나요? 그건 한 단계의 학력입니다. 대학교에 다녔다면 졸업하셨나요?</tgt>` | 3050 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | 1336 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1421 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | 1016 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | 1014 |
| 15 | `<src>online. </src><tgt>그게 또 다른 단계입니다. 그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>그건 또 다른 단계의 학력입니다. 자, 이제 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 848 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1035 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | 897 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1087 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1226 |
| 5 | `<src>함께 한 동생 이자 </src><tgt>怎么说呢，</tgt>` | `<src>함께 한 동생 이자 </src><tgt>嗯，怎么说呢，</tgt>` | 1463 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 1497 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>같은 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1742 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1219 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1225 |
| 10 | `<src>책임감 보다는 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>책임감 보다는 </src><tgt>他算是和我们一起经历过二十岁的人，也是一个家里的弟弟。所以，比起责任感，</tgt>` | 2815 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1182 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1406 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1137 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | 1099 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt>他更应该放下一些东西，</tgt>` | 884 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 589 |

---

### Test Example 43 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1218 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | 844 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1183 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1052 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>一进去就会晕头转向。不管是开车还是走路，</tgt>` | `<src>하건 거로 </src><tgt>进去的话会迷路的。开车的话，</tgt>` | 1452 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>거리 다니 고간에 뭐 </src><tgt><\|wait\|></tgt>` | 1534 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | 1930 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | 1567 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | 972 |
| 10 | `<src>또 장렬이에요. </src><tgt>去江北就不用说了，去外国就更惨了。</tgt>` | `<src>좀 </src><tgt>在路上，去江北是不可能，出国的话，那就太惨了。</tgt>` | 2018 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>신기 하네요. </src><tgt><\|wait\|></tgt>` | 1571 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1435 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1177 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모바일 을 </src><tgt><\|wait\|></tgt>` | 1084 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>真有点丢人。不过，我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>쓰는 것 같아요. </src><tgt>挺神奇的。不过，现在好像都在努力用手机。</tgt>` | 1043 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 513 |

---

### Test Example 44 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | 956 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1039 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1224 |
| 5 | `<src>今奇跡を見てる。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어.</tgt>` | `<src>今奇跡を見てる。</src><tgt>그럼 그냥 재워버려. 난 지금 기적을 보고 있는 거야.</tgt>` | 1539 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1479 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 2038 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1523 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | 1254 |
| 10 | `<src><\|wait\|></src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>이제 한계도 없는, 저 멀리 사라져버린 배의 기적이야.</tgt>` | 1894 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1368 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | 1463 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>が、</src><tgt><\|wait\|></tgt>` | 1147 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt><\|wait\|></tgt>` | 1125 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>海賊船を見た</src><tgt>오랫동안 배를 만들던 나였지만, 이렇게 대단한 해적선을</tgt>` | 1198 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 435 |

---

### Test Example 45 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | 1042 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | 943 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1184 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1460 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに</tgt>` | `<src>B라는 사람 이 서로 </src><tgt>ですから、もちろんこのようなケースもあります。AさんとBさんがお互いに</tgt>` | 1194 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | 1410 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1685 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | 1800 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 959 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>コンサルタントで、Aさんが悪性コードを</tgt>` | 2077 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1532 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1355 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1222 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | 1156 |
| 15 | `<src>EX 파일 까지 </src><tgt>配布したとします。その場合、Bさんは実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>EX 파일 까지 </src><tgt>渡したとして、BさんがクロスサイトスクリプティングでEXファイルまで</tgt>` | 1112 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까, </src><tgt><\|wait\|></tgt>` | 647 |

---

### Test Example 46 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 911 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | 891 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | 1388 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | 1363 |
| 5 | `<src>분석 을 보시면 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、</tgt>` | `<src>분석 을 보시면 </src><tgt>そしてこれについて、多くの人が分析を投稿しました。ここにロクジャの分析を見ると、</tgt>` | 1958 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 690 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | 1819 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | 1553 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | 1812 |
| 10 | `<src>것으로 보인다. </src><tgt>ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>것으로 보인다. </src><tgt>ソニーが26ビットFPファームを128ビットに下げたようです。</tgt>` | 1549 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1078 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | 1750 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 929 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1231 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L3가 여기 도 없다. </src><tgt>XboxSeriesXにもないインフィニットキャッシュL3もありません。</tgt>` | 1059 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 567 |

---

### Test Example 47 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1146 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 853 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | 1152 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | 1474 |
| 5 | `<src>닭살이 돋든 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり</tgt>` | `<src>닭살이 돋든 </src><tgt>目を閉じて、先生が何か祈る言葉を</tgt>` | 1207 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | 1493 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1913 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1240 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | 1050 |
| 10 | `<src>물릴 거고 </src><tgt>何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>祈るんだよ。君に背筋が寒くなったり、鳥肌が立ったり、何か感じたら、これを振りながら一緒に遊ぼうってこと。鬼が来たら噛まれるし、</tgt>` | 3865 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | 1503 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1211 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | 1178 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 함 마음 에. </src><tgt><\|wait\|></tgt>` | 802 |
| 15 | `<src>눈 감아. </src><tgt>神様が来たら守ってくれるように突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>神様が来たら守ってくれるってことだよ。だから安心して心を開いて。目を閉じて。</tgt>` | 952 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1239 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | 854 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>的感情或</src><tgt><\|wait\|></tgt>` | 1258 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | 1514 |
| 5 | `<src><\|wait\|></src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt>相手の感情や真意を察知したり、感じ取ったりすること。</tgt>` | 1665 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 746 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | 2045 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1624 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1534 |
| 10 | `<src>你们看，</src><tgt>するとき、よく耳にするのが「ほら、</tgt>` | `<src>你们看，</src><tgt>よく耳にするのは、</tgt>` | 948 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1441 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | 1346 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1267 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 939 |
| 15 | `<src><\|wait\|></src><tgt>また嘘をついている。目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>「見て、この人また嘘をついているよ。目がすべてを物語っている」</tgt>` | 1291 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | 608 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 612 |

---

### Test Example 49 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1175 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 667 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | 1608 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1269 |
| 5 | `<src>큰 폭의 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src>큰 폭의 </src><tgt>If the stock index is rising,</tgt>` | 1005 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1327 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1889 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1528 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 873 |
| 10 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>먼저 </src><tgt>these large- cap stocks will likely see a significant increase. But first,</tgt>` | 2039 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 1698 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | 1661 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 1061 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1115 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt>these lighter- weight stocks will lead the market and move first. So you should always keep an eye on the market cap of those lighter- weight stocks.</tgt>` | 1447 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | 523 |

---

### Test Example 50 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1270 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 820 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | 1361 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1391 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>So this isn't just a visual development environment; it's a visual Python development environment.</tgt>` | 2225 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | 1461 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | 1354 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>にそこから</src><tgt><\|wait\|></tgt>` | 1834 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>You write a flowchart visually, and then it generates Python code from that,</tgt>` | 2062 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1522 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 1142 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 1073 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 670 |
| 15 | `<src>はい。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>はい。</src><tgt>which is then executed to perform signal processing. That's how it works. Right.</tgt>` | 865 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | 442 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt><\|wait\|></tgt>` | 793 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1427 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | 1460 |
| 5 | `<src>absolutely correct, </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>absolutely correct, </src><tgt>活動、つまり自分自身で基準を定義することです。なぜなら、あなたが完全に正しい</tgt>` | 1636 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 839 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is is that </src><tgt><\|wait\|></tgt>` | 1936 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 1732 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt><\|wait\|></tgt>` | 1632 |
| 10 | `<src>standards have </src><tgt>しかし現実には、</tgt>` | `<src>standards have </src><tgt>ことだからです。しかし現実として、私たちは新しいブロックの子供のようなものです。そして基準は</tgt>` | 1553 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1285 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt><\|wait\|></tgt>` | 1661 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 983 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | 1186 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>everything at this point is being </src><tgt>20年前に変わりました。そのため、私たちはより高い基準を求められています。なぜなら、今の時代にはすべてが</tgt>` | 1235 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | 635 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | 996 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | 737 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | 1342 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>每当我们</src><tgt><\|wait\|></tgt>` | 1228 |
| 5 | `<src><\|wait\|></src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가</tgt>` | `<src><\|wait\|></src><tgt>프로이트는 그 현상을 처음 깨달았습니다. 우리가</tgt>` | 1105 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | 1497 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | 1923 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1561 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>我们也同时进入恨。</src><tgt><\|wait\|></tgt>` | 1063 |
| 10 | `<src><\|wait\|></src><tgt>사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>사랑을 느낄 때, 소위 말하는 사랑 속에서, 동시에 증오를 느끼게 된다는 것입니다.</tgt>` | 2618 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | 999 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | 1546 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1013 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | 1079 |
| 15 | `<src><\|wait\|></src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다.</tgt>` | `<src><\|wait\|></src><tgt>아침에는 사랑이고, 밤이 되면 증오로 변합니다.</tgt>` | 1061 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | 514 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 484 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | 564 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 1076 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, </src><tgt><\|wait\|></tgt>` | 790 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | 1532 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1359 |
| 5 | `<src><\|wait\|></src><tgt>另外，你没法</tgt>` | `<src><\|wait\|></src><tgt>嗯，另外，您也无法</tgt>` | 972 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | 1403 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 1799 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 1213 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt><\|wait\|></tgt>` | 1103 |
| 10 | `<src>where you realize </src><tgt>在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>where you realize </src><tgt>在资源之间移动媒体对象。所以，如果您遇到这种情况，发现</tgt>` | 2168 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | 1854 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | 1630 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | 1161 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1215 |
| 15 | `<src><\|wait\|></src><tgt>给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法</tgt>` | `<src><\|wait\|></src><tgt>把错误的媒体文件加到了某个资源上，请务必告知我们，我们会</tgt>` | 1001 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | 630 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 489 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 453 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1040 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 670 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1344 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1447 |
| 5 | `<src>he's been without food, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに</tgt>` | `<src>he's been without food, </src><tgt>ある時、彼はイエスが飢えていることを知ります。イエスが食べ物がない</tgt>` | 2018 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>been in the wilderness </src><tgt><\|wait\|></tgt>` | 758 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | 1968 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>And so he says </src><tgt><\|wait\|></tgt>` | 1356 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | 1437 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it. </src><tgt>40日間荒野で過ごしたせいで飢えていることを知っているのです。だから彼はイエスに言います。「おい、もしお前が神の御子なら、証明してみろ」と。</tgt>` | 3358 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1488 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | 991 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1111 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | 678 |
| 15 | `<src>temptation? </src><tgt>この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>「この石をパンに変えろ」と。</tgt>` | 739 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 401 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | 524 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | 449 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1456 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 680 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1123 |
| 5 | `<src>about the EHR fields </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの</tgt>` | `<src>about the EHR fields, </src><tgt>EHRの項目について、最初のセクションで少し混乱していました。</tgt>` | 1253 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1428 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1591 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus variant </src><tgt><\|wait\|></tgt>` | 1329 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1124 |
| 10 | `<src>databases, </src><tgt>決定的な重要性と、</tgt>` | `<src>databases, </src><tgt>重要な点として、バリアントデータベースと比較して、</tgt>` | 2113 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | 1630 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1306 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | 1589 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | 1113 |
| 15 | `<src>to be in these </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、</tgt>` | `<src>to be in these </src><tgt>これは私が大好きなバリアントデータベースの1つです。つまり、</tgt>` | 1096 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 641 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 366 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 651 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 364 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1289 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 782 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1033 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1244 |
| 5 | `<src>came along </src><tgt>有意义的个人权利，而最高法院</tgt>` | `<src>came along </src><tgt>有意义的个人权利，最高法院</tgt>` | 1408 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | 1489 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 1614 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1399 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | 1236 |
| 10 | `<src>change </src><tgt>是最后才介入的，不是引领者。我不认为</tgt>` | `<src>change </src><tgt>是最后跟进的，而不是引领。我不认为法院想成为</tgt>` | 2143 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days, </src><tgt><\|wait\|></tgt>` | 1534 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1287 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | 1457 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 991 |
| 15 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt>社会变革的最前沿，但它们更多地反映的是</tgt>` | 923 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged </src><tgt><\|wait\|></tgt>` | 685 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>soam. </src><tgt><\|wait\|></tgt>` | 608 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have some </src><tgt><\|wait\|></tgt>` | 469 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges </src><tgt><\|wait\|></tgt>` | 444 |
| 20 | `<src><\|wait\|></src><tgt>反映已经形成的共识。所以，有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>已经形成的共识。你还有一些联邦法官，</tgt>` | 502 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 270 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1023 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 903 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1326 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1538 |
| 5 | `<src>的一个是客厅</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면</tgt>` | `<src>的一个是客厅</src><tgt>그럼 사진을 한번 볼까요? 사진 부분에서</tgt>` | 1523 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>的部分。</src><tgt><\|wait\|></tgt>` | 796 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1909 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1569 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们再</src><tgt><\|wait\|></tgt>` | 939 |
| 10 | `<src>在休息的地方，</src><tgt>거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt>거실 부분이 보이네요. 거실은 보통 우리가 쉬는 공간이라서</tgt>` | 2097 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1414 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>所以呢，是身体的部分</src><tgt><\|wait\|></tgt>` | 1348 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>会反映的是</src><tgt><\|wait\|></tgt>` | 1338 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 1081 |
| 15 | `<src>一点时间，</src><tgt>그래서 이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>一点时间，</src><tgt>몸의 부분은 우리가 자신에게</tgt>` | 816 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的做</src><tgt><\|wait\|></tgt>` | 652 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>一下洗去，</src><tgt><\|wait\|></tgt>` | 659 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们可以看到这边是</src><tgt><\|wait\|></tgt>` | 604 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空污衣人的嘛，</src><tgt><\|wait\|></tgt>` | 459 |
| 20 | `<src>啊，</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는 아무도 없네요.</tgt>` | `<src>啊，所以</src><tgt>시간을 내서 제대로 샤워할 수 있는지를 반영해요. 여기 보면 ' 오염의 사자 ' 가 있네요. 그래서</tgt>` | 663 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>是说。</src><tgt><\|wait\|></tgt>` | 295 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 974 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 734 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1264 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1022 |
| 5 | `<src><\|wait\|></src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src><\|wait\|></src><tgt>これらの人々は極めて稀で、</tgt>` | 1365 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1498 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1492 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | 1418 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a </src><tgt><\|wait\|></tgt>` | 1007 |
| 10 | `<src>contradiction. </src><tgt>世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>contradiction. </src><tgt>世界の常識を完全に覆すことがあります。彼らの性格は矛盾しているように見えます。</tgt>` | 2372 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1471 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | 1196 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1349 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | 927 |
| 15 | `<src>and like to </src><tgt>外交的である一方、無意味な会話は嫌います。そして、</tgt>` | `<src>and like to </src><tgt>外向的ですが、無意味な会話を嫌い、</tgt>` | 1326 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 668 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | 647 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love to </src><tgt><\|wait\|></tgt>` | 595 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>play </src><tgt><\|wait\|></tgt>` | 336 |
| 20 | `<src>the devil's advocate, and they </src><tgt>要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, and they </src><tgt>要点をズバリ言うのが好きです。また、悪魔の肩を借りて議論を仕掛けるのも好きです。</tgt>` | 669 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 327 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | 320 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 339 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 326 |
| 25 | `<src>ENTP stands for </src><tgt>議論を避けることはありません。ENTPとは</tgt>` | `<src>ENTP stands for </src><tgt>議論を避けることは決してありません。ENTPは</tgt>` | 412 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1280 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 641 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1386 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1358 |
| 5 | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1328 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1017 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 2009 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1586 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1213 |
| 10 | `<src>김종인 을 </src><tgt>for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>김종인 을 </src><tgt>put on a show, claiming he was rejecting his party duties for the sake of the candidate and the party's victory. But now, with Yoon Suk- yeol as the candidate and Kim Jong- in</tgt>` | 3307 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1745 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | 943 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>드러내 놓고 윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 1407 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 634 |
| 15 | `<src><\|wait\|></src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>뜻끼를 </src><tgt>being removed, Lee Jun- seok revealed his intent to bring down Yoon Suk- yeol.</tgt>` | 868 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt><\|wait\|></tgt>` | 482 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 471 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 381 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 266 |
| 20 | `<src><\|wait\|></src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's</tgt>` | `<src>가슴 발 </src><tgt>He is determined to show his aggressive stance.</tgt>` | 475 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | 274 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 298 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 337 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 얼마나 </src><tgt><\|wait\|></tgt>` | 338 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute— what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재입니까? </src><tgt>How much of a boon is Lee Jun- seok's alleged ' bride- buying ' scandal to the Democratic Party?</tgt>` | 441 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 984 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | 841 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | 942 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | 1250 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ゴールドストーンホテル</src><tgt>Well, it looks like they're making it up in the dining hall right now. So, this Goldstone Hotel</tgt>` | 1693 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1414 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1594 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1384 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1089 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ねここ</src><tgt>is also planned to have breakfast.</tgt>` | 2067 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | 1450 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1188 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | 1522 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 898 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>もまあいいんじゃないか</src><tgt>If you're thinking of staying at the Goldstone Hotel in the future, I'd suggest you give it a look.</tgt>` | 1618 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 508 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | 635 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | 615 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | 401 |
| 20 | `<src><\|wait\|></src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src><\|wait\|></src><tgt>I think it's a good idea. From this hotel,</tgt>` | 437 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | 362 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | 341 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | 324 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | 327 |
| 25 | `<src>ホテルになってますので</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>ホテルになってますので</src><tgt>you can walk to Busan Station in about a minute or so. The location is really great.</tgt>` | 524 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 253 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 202 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 175 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | 190 |
