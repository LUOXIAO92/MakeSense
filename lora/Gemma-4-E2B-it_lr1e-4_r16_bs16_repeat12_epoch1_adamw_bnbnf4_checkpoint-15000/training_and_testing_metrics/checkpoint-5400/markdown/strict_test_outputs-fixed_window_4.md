# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9610
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5762
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
  - PROCESS_TIME_MS_AVG: 1318.4570
  - PROCESS_TIME_MS_P50: 1255.5290
  - PROCESS_TIME_MS_P95: 2224.8050
  - PROCESS_TIME_MS_MAX: 3787.3560

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1111 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>怪得忪子儿一般，</src><tgt><\|wait\|></tgt>` | 941 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个尤星</src><tgt><\|wait\|></tgt>` | 1094 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>也很大。</src><tgt><\|wait\|></tgt>` | 1085 |
| 5 | `<src><\|wait\|></src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>然后呢，</src><tgt>It's a bit strange, like a sleepy child. This Youxing is also quite large. And then,</tgt>` | 1542 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在放大，</src><tgt><\|wait\|></tgt>` | 1243 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>喝汤</src><tgt><\|wait\|></tgt>` | 794 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>人，</src><tgt><\|wait\|></tgt>` | 1525 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>感觉比较，</src><tgt><\|wait\|></tgt>` | 1697 |
| 10 | `<src>这种核桃</src><tgt>Then, I'll add some walnut kernels— this kind of</tgt>` | `<src>这种</src><tgt>I've zoomed in and taken a sip. It feels like</tgt>` | 1153 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>喝汤人。</src><tgt><\|wait\|></tgt>` | 1745 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气($_314)！</src><tgt><\|wait\|></tgt>` | 1145 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的，</src><tgt><\|wait\|></tgt>` | 1321 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 685 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师傅</src><tgt><\|wait\|></tgt>` | 1245 |
| 5 | `<src><\|wait\|></src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>知道，</src><tgt>気は易しい。でも師匠が一人しか知らない。</tgt>` | 1217 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如何除于</src><tgt><\|wait\|></tgt>` | 1206 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>终身，</src><tgt><\|wait\|></tgt>` | 884 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1460 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>须要反。</src><tgt><\|wait\|></tgt>` | 2004 |
| 10 | `<src>要成为</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>要成为一个</src><tgt>一生をどうやって乗り越えるか。だから、逆らわなきゃいけない。そして、</tgt>` | 2568 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>师傅。</src><tgt><\|wait\|></tgt>` | 973 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 742 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1031 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1313 |
| 5 | `<src>この時点で</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>この時点で</src><tgt>从一开始，特别是这个，因为现在才一年级。这个时候</tgt>` | 1491 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | 1496 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1098 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 790 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | 2040 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>十年経っても</src><tgt>如果把它剪短、收紧，十年后</tgt>` | 2494 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 1028 |

---

### Test Example 4 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1011 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1023 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1073 |
| 5 | `<src>ゴッホ、</src><tgt>大致是从这一带开始的，</tgt>` | `<src>ゴッホ、</src><tgt>大概是从这之后开始的，</tgt>` | 1290 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 616 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1510 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1569 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 744 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt>比如高更、高安、塞尚、伦纳尔等人的画，</tgt>` | 2053 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 1930 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | 1126 |

---

### Test Example 5 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 940 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>저는 용심히 </src><tgt><\|wait\|></tgt>` | 1034 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1152 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심히 </src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>옹심이가 </src><tgt>I'm having the ongsimi and kal- ongsimi—</tgt>` | `<src>새우 살 용심히 가 </src><tgt>Ah, I'm a</tgt>` | 1160 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1122 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1060 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야, </src><tgt><\|wait\|></tgt>` | 1482 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1963 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover,</tgt>` | `<src>해장으로도 조금 죽입니다, </src><tgt>swordfish salad. It's mixed with shrimp. Wow, I actually cut this up a bit for the raw fish salad too.</tgt>` | 2625 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>진장. </src><tgt><\|wait\|></tgt>` | 1127 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 761 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 1099 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 990 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 1272 |
| 5 | `<src>Where does the tension </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>你的身体在做什么？进入你的身体。紧张感</tgt>` | 1462 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1576 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1402 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 637 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask </src><tgt><\|wait\|></tgt>` | 1838 |
| 10 | `<src><\|wait\|></src><tgt>开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>the language </src><tgt>从哪里开始？是什么？是头痛吗？是胸闷吗？</tgt>` | 2619 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>you use. </src><tgt><\|wait\|></tgt>` | 966 |

---

### Test Example 7 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1116 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1384 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 800 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1270 |
| 5 | `<src>爱浇水、</src><tgt>What parents need to do is this:</tgt>` | `<src>深深的爱浇水，</src><tgt>What parents need to do is water our children with deep love.</tgt>` | 1562 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 1521 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1620 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | 2011 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>给</src><tgt><\|wait\|></tgt>` | 1076 |
| 10 | `<src>并耐心等待孩子</src><tgt>water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for</tgt>` | `<src>耐心等他</src><tgt>Fertilize them with psychological nourishment, and be patient</tgt>` | 2138 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 962 |

---

### Test Example 8 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | 1486 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | 756 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | 1397 |
| 5 | `<src>然后</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、</tgt>` | `<src>然后</src><tgt>撒き終わると、内部の圧力が下がり、エネルギーも衰えます。そして、</tgt>` | 1685 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | 1245 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>相对的低</src><tgt><\|wait\|></tgt>` | 1601 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | 1924 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态，</src><tgt><\|wait\|></tgt>` | 699 |
| 10 | `<src>这就是所谓的</src><tgt>比較的低エネルギーの状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>比較的低いエネルギーの運行状態に留まります。これが、いわゆる</tgt>` | 2617 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | 964 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 821 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>에파터플러시 기고 </src><tgt><\|wait\|></tgt>` | 1241 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt>I am a member of the EPF</tgt>` | 1433 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt><\|wait\|></tgt>` | 1540 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>페르 나 </src><tgt><\|wait\|></tgt>` | 1541 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 573 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1786 |
| 10 | `<src><\|wait\|></src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>같은 세대 들이 </src><tgt>generationally the same as Park Han- sang, who killed his own parents.</tgt>` | 3044 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1039 |

---

### Test Example 10 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1184 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 1210 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 907 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>Students in the auspicious positions</tgt>` | 1301 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1535 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 536 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>어떤 분입니까? </src><tgt><\|wait\|></tgt>` | 1427 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1977 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>사실 을 모를 랐던 </src><tgt>were not actually highly intelligent. And what about the students who were selected randomly? They were actually</tgt>` | 3083 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | 1059 |

---

### Test Example 11 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 1554 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 627 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1385 |
| 5 | `<src>或是通知对方，</src><tgt>In this situation, when we encounter a problem, we should</tgt>` | `<src>或是通知对方，</src><tgt>When we run into a problem like this, we should quickly report it to our supervisor or let them know.</tgt>` | 2154 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现有的这个状况，</src><tgt><\|wait\|></tgt>` | 979 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1590 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 2003 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | 1665 |
| 10 | `<src>整体而言，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall,</tgt>` | `<src>整体而言，</src><tgt>Don't try to handle everything on your own. Overall,</tgt>` | 1743 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业是</src><tgt><\|wait\|></tgt>` | 1131 |

---

### Test Example 12 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 808 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | 862 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1150 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1208 |
| 5 | `<src>調べるときに、</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area,</tgt>` | `<src>調べるときに、</src><tgt>When we're looking into whether a movie is alive in various situations,</tgt>` | 1372 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | 1417 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | 772 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1671 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | 2006 |
| 10 | `<src>ことを保証する</src><tgt>you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>ことを保証する</src><tgt>we can confirm that it's actually alive by checking its eggs.</tgt>` | 2287 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1040 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | 1188 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1357 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 816 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | 1376 |
| 5 | `<src>This is tip of the stem </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは</tgt>` | `<src>This is Tip the Stem. </src><tgt>非常に幸せな人たちに関する重要な研究を行いました。これが「Tip the Stem」です。</tgt>` | 2165 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>Research. </src><tgt><\|wait\|></tgt>` | 826 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at 10% </src><tgt><\|wait\|></tgt>` | 1668 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1932 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1750 |
| 10 | `<src>out there, </src><tgt>最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there—people that </src><tgt>研究です。最も幸せな人たちの10%を見てみると、</tgt>` | 1905 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1554 |

---

### Test Example 14 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 829 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1369 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 889 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1272 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>If there's some kind of connection between a female high school student and someone with a strange appearance,</tgt>` | 2094 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会使</src><tgt><\|wait\|></tgt>` | 921 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1586 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里开始的</src><tgt><\|wait\|></tgt>` | 1948 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 838 |
| 10 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src><\|wait\|></src><tgt>could it be that</tgt>` | 1801 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 1140 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇？</src><tgt><\|wait\|></tgt>` | 1602 |

---

### Test Example 15 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 677 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1029 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1142 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | 1196 |
| 5 | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가고 싶어요.</tgt>` | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가서, 제가</tgt>` | 1227 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | 1490 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 699 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热饭给他吃，</src><tgt><\|wait\|></tgt>` | 1595 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就这么</src><tgt><\|wait\|></tgt>` | 1853 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>我只是备餐的时候</src><tgt>그가 퇴근할 때 뜨거운 국이나 밥을 끓여 먹여주는 것만으로도</tgt>` | 2585 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的小愿望</src><tgt><\|wait\|></tgt>` | 1176 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 1592 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1151 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 1153 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1020 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1238 |
| 5 | `<src>the instruction </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>the instruction </src><tgt>好的。然后，在这些例子之后，</tgt>` | 1175 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1457 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 651 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1465 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1803 |
| 10 | `<src>these values. So </src><tgt>说明告诉我们要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>说明我们实际上要使用这些值。所以</tgt>` | 1046 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1752 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot scored array, </src><tgt><\|wait\|></tgt>` | 1263 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1615 |

---

### Test Example 17 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツ</src><tgt><\|wait\|></tgt>` | 1100 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>などがあの</src><tgt><\|wait\|></tgt>` | 1038 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1109 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1271 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>We have things like T- shirts available for you to pick up,</tgt>` | 1466 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 1435 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 520 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | 1526 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1978 |
| 10 | `<src><\|wait\|></src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src>よろしくお願いします。</src><tgt>so please do join us. That's all for the contact information. Uh, thank you.</tgt>` | 2478 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | 1142 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1742 |

---

### Test Example 18 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 965 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | 1629 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | 622 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1491 |
| 5 | `<src>다른 잔찜에 </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>다른 잔찜에 </src><tgt>He said to let me go to another room, so I came in to kill him.</tgt>` | 1671 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 1102 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | 1751 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 2016 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 줄 알았느냐? </src><tgt><\|wait\|></tgt>` | 1863 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh?</tgt>` | `<src>아, </src><tgt>He asked, ' Didn't you say to let me go to another room? Didn't you think I wasn't listening to that? Oh,</tgt>` | 2299 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | 1839 |

---

### Test Example 19 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1124 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1256 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 907 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | 1401 |
| 5 | `<src>Find what you're good at </src><tgt>最后，要重复。学会不断重复。找到你的长处，</tgt>` | `<src>Find what you're good at </src><tgt>最后，是重复。学会重复练习。找到你擅长</tgt>` | 1611 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1448 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1555 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | 2192 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | 2439 |
| 10 | `<src><\|wait\|></src><tgt>多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>的事情，多做一些。而你不太擅长的，就请周围的人来帮助你。</tgt>` | 1647 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | 1881 |

---

### Test Example 20 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1073 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 843 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアです。ギアが</src><tgt><\|wait\|></tgt>` | 1184 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと、シンガーが</src><tgt><\|wait\|></tgt>` | 1152 |
| 5 | `<src><\|wait\|></src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이</tgt>` | `<src>上げ下げできなくなってしまう</src><tgt>이것이 기어입니다. 기어가 헐거워지면 싱거가</tgt>` | 1469 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1164 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 895 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1553 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>逆ネジのナットが</src><tgt><\|wait\|></tgt>` | 1984 |
| 10 | `<src>ついているっていうことです</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>付いているっていうこと</src><tgt>위아래로 움직이지 않게 됩니다. 그래서 기어 끝에 역나사 캡이</tgt>` | 2080 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1213 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1029 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンブレーキを。</src><tgt><\|wait\|></tgt>` | 1866 |

---

### Test Example 21 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1232 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | 972 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1364 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 </src><tgt>これ、あまりにも低俗なことかもしれません。でも、本当に菩薩様ですね。</tgt>` | 1582 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>자기 가 보살 인데 꿈일 프로 </src><tgt><\|wait\|></tgt>` | 1548 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>아보이 고 </src><tgt><\|wait\|></tgt>` | 1580 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1884 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보일 프로 </src><tgt><\|wait\|></tgt>` | 1748 |
| 10 | `<src>지금 나한테 </src><tgt>自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に</tgt>` | `<src>보이 서 우주 가신다 한 뒤 </src><tgt>菩薩様は自分自身が菩薩だと知っているからこそ、夢に見えるんです。私だけが菩薩に見えて、宇宙が動くんです。そして、</tgt>` | 2781 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이라는 거. </src><tgt><\|wait\|></tgt>` | 1787 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 850 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 1015 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1163 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | 1326 |
| 5 | `<src>ありましたね。</src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>ありましたね。</src><tgt>맞아요. 그래서 테키라는 시설이 있었죠.</tgt>` | 1420 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1531 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 497 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | 1485 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1939 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>は五コン、</src><tgt>그리고 나가이 케이요 씨의 시스템은</tgt>` | 2450 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1119 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>設備寺、五ビ</src><tgt><\|wait\|></tgt>` | 1736 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 912 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 1542 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 655 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1334 |
| 5 | `<src>and when those bonds are broken, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면</tgt>` | `<src>bonds are broken, </src><tgt>고무줄처럼, 화학 결합도 에너지를 저장합니다. 그리고 그 결합이 끊어지면,</tgt>` | 2468 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 659 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1619 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt><\|wait\|></tgt>` | 1999 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>heat or light. </src><tgt><\|wait\|></tgt>` | 1675 |
| 10 | `<src><\|wait\|></src><tgt>잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>It gets </src><tgt>그 잠재 에너지는 열이나 빛 같은 다른 에너지 형태로 바뀝니다.</tgt>` | 1920 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>used to make </src><tgt><\|wait\|></tgt>` | 1630 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1050 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kiran Patel. </src><tgt><\|wait\|></tgt>` | 1353 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently </src><tgt><\|wait\|></tgt>` | 805 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>studying IEEE Baxter </src><tgt><\|wait\|></tgt>` | 1303 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>Finance </src><tgt>제 이름은 키란 파텔입니다. 현재</tgt>` | 1444 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Ph.D. of Psychology. </src><tgt><\|wait\|></tgt>` | 1774 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1634 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at the IEEE N </src><tgt><\|wait\|></tgt>` | 2023 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1764 |
| 10 | `<src>and in the future, I want to go into </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go </src><tgt>IEEE 금융과 심리학 박사 과정을 밟고 있습니다. IEEE N에서</tgt>` | 1981 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>into corporate consultancy </src><tgt><\|wait\|></tgt>` | 1673 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>and. </src><tgt><\|wait\|></tgt>` | 883 |

---

### Test Example 25 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1197 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 997 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じで、</src><tgt><\|wait\|></tgt>` | 1163 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将から五月五日、</src><tgt><\|wait\|></tgt>` | 1444 |
| 5 | `<src>多いですね。</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。</tgt>` | `<src>多いですね。</src><tgt>嗯，距离好像渐渐拉开了，大将和五月五日，感觉挺远的。</tgt>` | 1811 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>海遊して二、三って</src><tgt><\|wait\|></tgt>` | 1264 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい行き来しき</src><tgt><\|wait\|></tgt>` | 1642 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>ただい、じ、</src><tgt><\|wait\|></tgt>` | 2035 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>で、で、で、多分</src><tgt><\|wait\|></tgt>` | 2288 |
| 10 | `<src>全部ちょっと次の投資</src><tgt>想创业的人自我意识都很强，而且</tgt>` | `<src>その時に</src><tgt>在海游和二三之间来回穿梭，然后，然后，然后，大概就是那时候，</tgt>` | 1777 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>顔が強いので、</src><tgt><\|wait\|></tgt>` | 1874 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので。</src><tgt><\|wait\|></tgt>` | 802 |

---

### Test Example 26 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1240 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 969 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1337 |
| 5 | `<src>坚持不开刀。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery.</tgt>` | `<src>所以坚持不开刀，</src><tgt>I was perfectly fine back then, full of energy, so I insisted on not having surgery.</tgt>` | 1994 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间大概有</src><tgt><\|wait\|></tgt>` | 1013 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>十位医生</src><tgt><\|wait\|></tgt>` | 1615 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来审断，</src><tgt><\|wait\|></tgt>` | 1903 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿、</src><tgt><\|wait\|></tgt>` | 865 |
| 10 | `<src>一下提腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>以下提腿，</src><tgt>About ten doctors came to examine me. They had to kick and lift my legs</tgt>` | 2521 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1097 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1781 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1000 |

---

### Test Example 27 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 860 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1848 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 725 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1000 |
| 5 | `<src>유사 한 작용 이 </src><tgt>Things like vanadium</tgt>` | `<src>유사 한 작용 이 </src><tgt>Vanadium and these things</tgt>` | 1372 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1550 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1529 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다. </src><tgt><\|wait\|></tgt>` | 849 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이것 이 굉장히 잘 </src><tgt><\|wait\|></tgt>` | 1633 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>잘 존재 를 </src><tgt>act almost like insulin— it's a very, very good diabetes mineral. It's very well</tgt>` | 3009 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. </src><tgt><\|wait\|></tgt>` | 1155 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>이제 그 후에다가 </src><tgt><\|wait\|></tgt>` | 1772 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1357 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 1202 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 938 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1277 |
| 5 | `<src>you realize that </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>you realize that </src><tgt>あるいは、あるいは何かを書き起こす必要がある場合、文章を書く場合、</tgt>` | 1569 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | 1591 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1524 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 1949 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1040 |
| 10 | `<src>spelled with a double </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>spelled with a double </src><tgt>単語の綴りが全く分からないことに気づくかもしれません。「ああ、この単語は</tgt>` | 2391 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>p, </src><tgt><\|wait\|></tgt>` | 1135 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double lam? I don't </src><tgt><\|wait\|></tgt>` | 1781 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 1405 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1153 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1125 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | 1077 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1342 |
| 5 | `<src>history as a guide </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>제19조 수정헌법의 의미와</tgt>` | 1416 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1503 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1552 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 744 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1715 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지 이해하는 지침으로서 그 역사를 탐구해 보겠습니다.</tgt>` | 3107 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 1209 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | 1863 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 1286 |

---

### Test Example 30 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 907 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1258 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | 974 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1326 |
| 5 | `<src>在一级一线</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で</tgt>` | `<src>如果在一级一项</src><tgt>2つ目は、セカンダリーマーケットを選ぶことです。あ、もし</tgt>` | 1533 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | 1540 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 1538 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1878 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>微信公众号十几年，</src><tgt><\|wait\|></tgt>` | 791 |
| 10 | `<src>发现</src><tgt>戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>プライマリーマーケットで激しく戦っている大口投資家たち、例えばWeChat公式アカウントを10年以上運営している人たちなら、</tgt>` | 3074 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | 1712 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>的新榜，然后</src><tgt><\|wait\|></tgt>` | 1095 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>回了个。</src><tgt><\|wait\|></tgt>` | 1479 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 860 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 1205 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 952 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | 1345 |
| 5 | `<src>它是属于逆向的，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요.</tgt>` | `<src>它是属于逆向的，</src><tgt>이 사진의 이 부분은 낚시를 하는 사람인데, 역방향으로</tgt>` | 2000 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 938 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通常我们这样一个状况</src><tgt><\|wait\|></tgt>` | 1579 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>的视频就要去</src><tgt><\|wait\|></tgt>` | 1668 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | 813 |
| 10 | `<src>是它能不能够</src><tgt>그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>是它能不能够</src><tgt>촬영된 거라, 이런 상황의 영상은 특히 주의해야 합니다. 바로</tgt>` | 2885 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | 1054 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>它钓不到鱼，</src><tgt><\|wait\|></tgt>` | 1870 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它也</src><tgt><\|wait\|></tgt>` | 986 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>意思了。</src><tgt><\|wait\|></tgt>` | 903 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 802 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | 1828 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | 1037 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 806 |
| 5 | `<src>많았습니다. </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。</tgt>` | `<src>많았습니다. </src><tgt>そのうち150万件は従業員数10人未満の非常に小さな企業でした。</tgt>` | 1948 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1082 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1633 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | 2135 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | 2183 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は</tgt>` | `<src>일본 의 소기업들은 </src><tgt>一般的に小さな企業は成長するか、あるいは廃業するかのどちらかになります。日本の小企業は</tgt>` | 1783 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1888 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>폐업 도 하지 않는 </src><tgt><\|wait\|></tgt>` | 1119 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들만 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1135 |

---

### Test Example 33 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>授業</src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一日一日の</src><tgt><\|wait\|></tgt>` | 905 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>予定だった。</src><tgt><\|wait\|></tgt>` | 1106 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく十秒で</src><tgt><\|wait\|></tgt>` | 1122 |
| 5 | `<src>まあ</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>まあ</src><tgt>原定是每天一次。大概十秒，嗯，</tgt>` | 1335 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一日分に</src><tgt><\|wait\|></tgt>` | 564 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1518 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>予定だったんですね。</src><tgt><\|wait\|></tgt>` | 1571 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>そうやって。</src><tgt><\|wait\|></tgt>` | 1371 |
| 10 | `<src>でなんか</src><tgt>一秒一手多一点这样算。然后</tgt>` | `<src>でなんか</src><tgt>大概是按一天来算，今天左右的计划。就这样。然后</tgt>` | 1287 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1690 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一日</src><tgt><\|wait\|></tgt>` | 1108 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1217 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1705 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮川とかが</src><tgt>大概十一号，宫川他们</tgt>` | 1506 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>から。</src><tgt><\|wait\|></tgt>` | 836 |

---

### Test Example 34 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个上，</src><tgt><\|wait\|></tgt>` | 1238 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在《这个罗马》呢，</src><tgt><\|wait\|></tgt>` | 1030 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 1207 |
| 5 | `<src>所以呢，</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、</tgt>` | `<src>造成了，所以呢，</src><tgt>皆さんにお伝えしたいのですが、『このローマ』という作品において、それは</tgt>` | 1596 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1400 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1564 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>遗迹啊、跟风景</src><tgt><\|wait\|></tgt>` | 1665 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 788 |
| 10 | `<src>一夕之间就</src><tgt>今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>你历史之间，就</src><tgt>過去の出来事によって生じたものではありません。ですから、今皆さんが直面している遺跡や風景は、皆さんの歴史と</tgt>` | 3319 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1342 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 1370 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的，因此会建议</src><tgt><\|wait\|></tgt>` | 1422 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | 1006 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>达到了一个</src><tgt><\|wait\|></tgt>` | 758 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>甜头，那</src><tgt><\|wait\|></tgt>` | 1393 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt><\|wait\|></tgt>` | 772 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1334 |
| 5 | `<src>请你务必就要</src><tgt>うまくいったなと思ったらね。その時は必ず利益を</tgt>` | `<src>请你务必就要</src><tgt>良い兆しを得ました。その兆しを得た後は、必ず</tgt>` | 1592 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1463 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1615 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，</src><tgt><\|wait\|></tgt>` | 2146 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我再继续操作，</src><tgt><\|wait\|></tgt>` | 1819 |
| 10 | `<src>继续操作下去哦。</src><tgt>確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>守り抜いてください。そうして「あ、じゃあまた操作を続けよう」なんて考えないでください。</tgt>` | 2125 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1551 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 939 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为</src><tgt><\|wait\|></tgt>` | 1409 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>呢。</src><tgt><\|wait\|></tgt>` | 844 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 748 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1076 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HTML이라고 하는 </src><tgt><\|wait\|></tgt>` | 1125 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1249 |
| 5 | `<src><\|wait\|></src><tgt>HTML是一种</tgt>` | `<src>컴퓨터 도 이해 할 수 있고 </src><tgt>嗯，</tgt>` | 1186 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1248 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 895 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 에 </src><tgt><\|wait\|></tgt>` | 1634 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1990 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>맞게 우리 가 이제 </src><tgt>计算机语言，也就是HTML，</tgt>` | 2038 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1127 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 1197 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1728 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1439 |
| 15 | `<src>필요 합니다. </src><tgt>我们需要按照它的语法来编写代码，而编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要按照语法来编写代码。编写这些代码需要一个程序。</tgt>` | 1168 |

---

### Test Example 37 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1039 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | 844 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1207 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1096 |
| 5 | `<src>함께 한 동생 이자 </src><tgt>怎么说呢，</tgt>` | `<src>동생 이자 </src><tgt>嗯，怎么说呢，</tgt>` | 1270 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 617 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>같은 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1595 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1549 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1685 |
| 10 | `<src>책임감 보다는 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>책임감 보다는 </src><tgt>他其实是和我们一起经历过二十岁的人，也是家人。所以，比起责任感，</tgt>` | 2152 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1460 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 895 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1679 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것 </src><tgt><\|wait\|></tgt>` | 777 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>他更看重自己能做的事情，</tgt>` | 1591 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>응모 했습니다. </src><tgt><\|wait\|></tgt>` | 849 |

---

### Test Example 38 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 976 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There were </src><tgt><\|wait\|></tgt>` | 1105 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1016 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | 1292 |
| 5 | `<src><\|wait\|></src><tgt>没什么新鲜的。以前就有过这样的接口，</tgt>` | `<src><\|wait\|></src><tgt>没什么新意。以前确实有这样的接口，</tgt>` | 1480 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | 1541 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 1247 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 606 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>this is just one another place </src><tgt><\|wait\|></tgt>` | 2041 |
| 10 | `<src>to look at. </src><tgt>比如netfilter和 TC。所以这只是另一个需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>比如netfilter、TC。嗯，所以这只是看的地方之一。</tgt>` | 2493 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 963 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1427 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1336 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | 1383 |
| 15 | `<src>should be aware of that. </src><tgt>但开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>但那些在BugRepo工作、做开发或工程的人应该知道这一点。</tgt>` | 1225 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1207 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get. </src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1296 |
| 5 | `<src>and I have ten of them </src><tgt>それは始めたばかりの人が手に入れるべきもので、</tgt>` | `<src>And at ten of them, </src><tgt>これから何かを始めようとしている人には、まず準備が必要なんです。その10人中、</tgt>` | 2138 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that is really </src><tgt><\|wait\|></tgt>` | 924 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important </src><tgt><\|wait\|></tgt>` | 1512 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1657 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go </src><tgt><\|wait\|></tgt>` | 975 |
| 10 | `<src>I have about </src><tgt>私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>into, I have about one </src><tgt>本当に重要なことなんです。今から</tgt>` | 2357 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute of videos </src><tgt><\|wait\|></tgt>` | 838 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | 1661 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one, </src><tgt><\|wait\|></tgt>` | 1146 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1259 |
| 15 | `<src>in a little more detail, but. </src><tgt>この動画の後に、それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>and a little more detail, </src><tgt>動画を1本見ていきます。この動画の後に、それぞれを解説する動画が1本あります。もう少し詳しく、</tgt>` | 1435 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 828 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1575 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 657 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1256 |
| 5 | `<src>말 못하 는 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない</tgt>` | `<src>말 못하 는 </src><tgt>あなたたちも知っているだろう。あなたがたが異邦人として</tgt>` | 1542 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1524 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그들 의 </src><tgt><\|wait\|></tgt>` | 1540 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>그 일화 </src><tgt><\|wait\|></tgt>` | 1678 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>갔느니라. </src><tgt><\|wait\|></tgt>` | 933 |
| 10 | `<src>그러므로 내가 </src><tgt>偶像に引かれるままに連れて行かれました。ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>いたとき、彼らは言葉を持たない偶像へと向かった。だから、私は</tgt>` | 2737 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 1028 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1872 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1041 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 1052 |
| 15 | `<src><\|wait\|></src><tgt>あなたがたに教えます。神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>あなたたちに告げます。神の霊によって語る者は……</tgt>` | 1065 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1045 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>蒸らせてやれ</src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1096 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1170 |
| 5 | `<src>今奇跡を見てる。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어.</tgt>` | `<src>今引き締めよう</src><tgt>그럼 그냥 쪄버려. 난 지금</tgt>` | 1228 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1225 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>っていうもう限界なんか</src><tgt><\|wait\|></tgt>` | 949 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>遠い越えている</src><tgt><\|wait\|></tgt>` | 1607 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>船長貴勢気</src><tgt><\|wait\|></tgt>` | 1994 |
| 10 | `<src><\|wait\|></src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>힘을 줄일 생각은 없어. 그 정도 한계는 이미 저 멀리</tgt>` | 2369 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1004 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長年にわたる大工を</src><tgt><\|wait\|></tgt>` | 1315 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やっている。</src><tgt><\|wait\|></tgt>` | 1470 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1436 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>こんなにすごい海賊船を見た</src><tgt>넘어선 선장 기세기. 나는 몇 년 동안 대장장이를 해온 사람이야. 난 이렇게 대단한 해적선을</tgt>` | 1515 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 684 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1060 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1253 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 950 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1254 |
| 5 | `<src>actually go in your education? Did you </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? Did you </src><tgt>학력. 교육은 어느 정도까지 마쳤나요?</tgt>` | 1501 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1584 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt><\|wait\|></tgt>` | 1638 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>of attainment. Did you go </src><tgt><\|wait\|></tgt>` | 2042 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>to college, </src><tgt><\|wait\|></tgt>` | 1706 |
| 10 | `<src>and if so, did you graduate? </src><tgt>고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>and if so, did you graduate? </src><tgt>고등학교 졸업은 한 단계의 학력입니다. 대학까지 다녔다면 졸업했나요?</tgt>` | 2225 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level </src><tgt><\|wait\|></tgt>` | 1803 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>of attainment. </src><tgt><\|wait\|></tgt>` | 759 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1398 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt><\|wait\|></tgt>` | 994 |
| 15 | `<src>online. </src><tgt>그게 또 다른 단계입니다. 그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>그것도 또 다른 단계의 학력입니다. 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 1014 |

---

### Test Example 43 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1511 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 615 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1273 |
| 5 | `<src>也就是</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり</tgt>` | `<src>比较偏向正财的部分，也就是</src><tgt>金運についてですが、今月はかなり良いと言えます。ただ、正財の面が</tgt>` | 2378 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | 787 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长</src><tgt><\|wait\|></tgt>` | 1519 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>所带来的红利，</src><tgt><\|wait\|></tgt>` | 2011 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>也就是收入的提升。如果是在</src><tgt><\|wait\|></tgt>` | 1759 |
| 10 | `<src>投资理财方面呢，</src><tgt>仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>投资理财方面呢，</src><tgt>事業の業績向上による恩恵、つまり収入の増加です。投資や資産運用に関しては、</tgt>` | 2281 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月也是</src><tgt><\|wait\|></tgt>` | 1896 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>不错，只是相对于</src><tgt><\|wait\|></tgt>` | 571 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>正财来说，就</src><tgt><\|wait\|></tgt>` | 1490 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | 889 |
| 15 | `<src><\|wait\|></src><tgt>悪くはないんですが、本業の収入に比べると少し弱めですね。</tgt>` | `<src><\|wait\|></src><tgt>今月も悪くはありません。ただ、正財と比べると少しだけ弱めです。</tgt>` | 1052 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 </src><tgt><\|wait\|></tgt>` | 989 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>해맨입니다. </src><tgt><\|wait\|></tgt>` | 1153 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전 을 할 건 </src><tgt><\|wait\|></tgt>` | 1326 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>一进去就会晕头转向。不管是开车还是走路，</tgt>` | `<src><\|wait\|></src><tgt>进入的时候非常危险。开车的话，</tgt>` | 1228 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>거로 거로 다니 고는 </src><tgt><\|wait\|></tgt>` | 1585 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 617 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1482 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 이야 나도 </src><tgt><\|wait\|></tgt>` | 2010 |
| 10 | `<src>또 장렬이에요. </src><tgt>去江北就不用说了，去外国就更惨了。</tgt>` | `<src>장려 력이요. 좀 </src><tgt>主要还是开Goro，去江北那更是不用说了，外国人也欢迎。不过</tgt>` | 3123 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>신기 하네요. </src><tgt><\|wait\|></tgt>` | 1089 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1793 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1125 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모르 바요. 그거 는 </src><tgt><\|wait\|></tgt>` | 1042 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>真有点丢人。不过，我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>내인 것 같아요. </src><tgt>挺神奇的。相比之下，现在要努力学习了。那个好像是内因的。</tgt>` | 1288 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 352 |

---

### Test Example 45 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 </src><tgt><\|wait\|></tgt>` | 1047 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1231 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>인증 상승 하는 흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1184 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1087 |
| 5 | `<src>큰 폭의 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src><\|wait\|></src><tgt>If the stock index is rising,</tgt>` | 1276 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1641 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1584 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 가벼운 </src><tgt><\|wait\|></tgt>` | 1943 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1037 |
| 10 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>먼저 </src><tgt>these large- cap stocks will likely rise sharply. But first,</tgt>` | 2257 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 1179 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1804 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1385 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 834 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>눈여겨봐야 </src><tgt>since lighter stocks move the market first, you should always keep an eye on the stocks with lower market capitalization.</tgt>` | 1272 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 525 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계서 </src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 1257 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1050 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1276 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに</tgt>` | `<src>B라는 사람 이 </src><tgt>旧約聖書にも、もちろんこのようなケースはあります。AさんとBさんが</tgt>` | 1731 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨설턴트예요 </src><tgt><\|wait\|></tgt>` | 1371 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 컨설턴트여야 </src><tgt><\|wait\|></tgt>` | 1687 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>되고 A라는 </src><tgt><\|wait\|></tgt>` | 1875 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 1679 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>コンサルタントで、Aさんが悪意のあるコードを</tgt>` | 1958 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 1488 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 </src><tgt><\|wait\|></tgt>` | 1289 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1274 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스사이트 스키티에서 </src><tgt><\|wait\|></tgt>` | 1028 |
| 15 | `<src>EX 파일 까지 </src><tgt>配布したとします。その場合、Bさんは実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>EX 파일까지 </src><tgt>与えた場合、Bさんが実際にクロスサイトスクリプティングでEXファイルまで</tgt>` | 907 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 560 |

---

### Test Example 47 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1019 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | 1233 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 에 서름이 돋든 </src><tgt><\|wait\|></tgt>` | 1493 |
| 5 | `<src>닭살이 돋든 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり</tgt>` | `<src>가자리 돋든 </src><tgt>目を閉じて、先生は「何と祈るのか」と。昔、寒さで</tgt>` | 2240 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 너무 </src><tgt><\|wait\|></tgt>` | 760 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어사 </src><tgt><\|wait\|></tgt>` | 1642 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 2009 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | 1670 |
| 10 | `<src>물릴 거고 </src><tgt>何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>寒さで体が震えるような感覚。それを振り払って一緒に遊ぼうというんだ。幽霊が来たら噛みつくし、</tgt>` | 2439 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | 1865 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1017 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주려 하니까 </src><tgt><\|wait\|></tgt>` | 1104 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 773 |
| 15 | `<src>눈 감아. </src><tgt>神様が来たら守ってくれるように突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>神様が来たら「守るから刺してやろう」と言うんだ。だから心に余裕を持って目を閉じて。</tgt>` | 1349 |

---

### Test Example 48 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1047 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1458 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | 748 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1277 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>So, this isn't just a visual development environment; it's a visual Python development environment.</tgt>` | 2244 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | 952 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1676 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | 2114 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>にそこから</src><tgt><\|wait\|></tgt>` | 1916 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>You write a flowchart visually, and then it generates Python code from that.</tgt>` | 1652 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1658 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 1059 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 1514 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 886 |
| 15 | `<src>はい。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>はい。</src><tgt>And that code is executed, which performs signal processing. Yes.</tgt>` | 931 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | 637 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1048 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉对手</src><tgt><\|wait\|></tgt>` | 1469 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>的感情或</src><tgt><\|wait\|></tgt>` | 737 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的。</src><tgt><\|wait\|></tgt>` | 1278 |
| 5 | `<src><\|wait\|></src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt>相手の感情や真の意図を推し量ったり感じ取ったりすること。</tgt>` | 1606 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1448 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>很多时候，经常</src><tgt><\|wait\|></tgt>` | 1619 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1935 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 898 |
| 10 | `<src>你们看，</src><tgt>するとき、よく耳にするのが「ほら、</tgt>` | `<src>你们看，</src><tgt>よく、よく耳にする言葉があります。皆さんも見ての通り、</tgt>` | 2442 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1027 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了。</src><tgt><\|wait\|></tgt>` | 1908 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1173 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 920 |
| 15 | `<src><\|wait\|></src><tgt>また嘘をついている。目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>この人はまた嘘をついている。その目はすべてを物語っている。</tgt>` | 1002 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | 608 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>是说。</src><tgt><\|wait\|></tgt>` | 665 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 757 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1369 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 내놓았습니다. </src><tgt><\|wait\|></tgt>` | 923 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 </src><tgt><\|wait\|></tgt>` | 1277 |
| 5 | `<src>분석 을 보시면 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、</tgt>` | `<src>의 분석 을 보시면 </src><tgt>これについて多くの人が分析を提出しました。ロクジャの分析を見ると、</tgt>` | 1727 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 1221 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 제품 에 </src><tgt><\|wait\|></tgt>` | 1560 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FP 파이프 를 </src><tgt><\|wait\|></tgt>` | 1864 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 817 |
| 10 | `<src>것으로 보인다. </src><tgt>ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>낮춘 것을 보입니다. </src><tgt>ソニーが過去の製品でFPパイプを128ビットに下げたことがわかります。</tgt>` | 2897 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1171 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈 X에서도 없는. </src><tgt><\|wait\|></tgt>` | 1914 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1371 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 977 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>SD가 여기 도 없다. </src><tgt>XboxSeriesXにもない。インフィニットキャッシュSDもここにはありません。</tgt>` | 1021 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 642 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 998 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1068 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | 1481 |
| 5 | `<src>absolutely correct, </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>absolutely correct, </src><tgt>活動や自己定義は、基準はこうあるべきだと思っているからだ。なぜなら、君は完全に正しいからだ。</tgt>` | 2573 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 561 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is is that </src><tgt><\|wait\|></tgt>` | 1511 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 2149 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt><\|wait\|></tgt>` | 2043 |
| 10 | `<src>standards have </src><tgt>しかし現実には、</tgt>` | `<src>standards have </src><tgt>でも現実の問題は、私たちが新しい世代だからだ。そして基準が</tgt>` | 1517 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1743 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt><\|wait\|></tgt>` | 941 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1394 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard because. </src><tgt><\|wait\|></tgt>` | 976 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>Everything at this point is being </src><tgt>20年前に変わってから、私たちはより高い基準を求められている。なぜなら、今の時代はすべてが</tgt>` | 1218 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>by a higher standard. </src><tgt><\|wait\|></tgt>` | 489 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 813 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>为了以的首知觉</src><tgt><\|wait\|></tgt>` | 1445 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>知道那个现象，</src><tgt><\|wait\|></tgt>` | 745 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |
| 5 | `<src><\|wait\|></src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>每当我们处于</src><tgt>어떤 현상을 먼저 인지하기 위해,</tgt>` | 1435 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1498 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>爱之中，所谓的爱，</src><tgt><\|wait\|></tgt>` | 697 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1206 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>我们也同时进入</src><tgt><\|wait\|></tgt>` | 2002 |
| 10 | `<src><\|wait\|></src><tgt>사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>우리가 사랑 속에 있을 때, 소위 말하는 사랑도 동시에</tgt>` | 2882 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨，在长上的时候，</src><tgt><\|wait\|></tgt>` | 894 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>它是</src><tgt><\|wait\|></tgt>` | 1576 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>爱到了晚上，</src><tgt><\|wait\|></tgt>` | 1022 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 1270 |
| 15 | `<src><\|wait\|></src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다.</tgt>` | `<src><\|wait\|></src><tgt>증오로 변합니다. 그리고 사랑이 절정에 달하면 증오로 변합니다.</tgt>` | 1241 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>恨那个钟摆，</src><tgt><\|wait\|></tgt>` | 831 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt><\|wait\|></tgt>` | 578 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>一动，</src><tgt><\|wait\|></tgt>` | 403 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 995 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, </src><tgt><\|wait\|></tgt>` | 1143 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | 1071 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src><\|wait\|></src><tgt>另外，你没法</tgt>` | `<src><\|wait\|></src><tgt>嗯，另外，</tgt>` | 1218 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | 1253 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 694 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the </src><tgt><\|wait\|></tgt>` | 1618 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation where you </src><tgt><\|wait\|></tgt>` | 2005 |
| 10 | `<src>where you realize </src><tgt>在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>realize you've added </src><tgt>你将无法在资源之间移动媒体对象。所以，如果你遇到这种情况，意识到你</tgt>` | 3086 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1054 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | 1881 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | 1473 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 762 |
| 15 | `<src><\|wait\|></src><tgt>给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>moving those </src><tgt>把错误的媒体文件添加到了某个资源中，你需要告诉我们，我们就能</tgt>` | 985 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>media files and then making sure they </src><tgt><\|wait\|></tgt>` | 567 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 611 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 529 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1242 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 981 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1136 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1288 |
| 5 | `<src>about the EHR fields </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの</tgt>` | `<src>about the EHR field, </src><tgt>EHRの分野について、最初のセクションで少し混乱していました。</tgt>` | 1503 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and having </src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>critical importance </src><tgt><\|wait\|></tgt>` | 1005 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 845 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1934 |
| 10 | `<src>databases, </src><tgt>決定的な重要性と、</tgt>` | `<src>variant databases, </src><tgt>変異データベースと比べて、EHRの分野が非常に重要であるという点です。</tgt>` | 2178 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | 1320 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1374 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1645 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1288 |
| 15 | `<src>to be in these </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、</tgt>` | `<src>to be in these </src><tgt>これは明らかに私の大好きな分野の一つです。つまり、</tgt>` | 1124 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 874 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 560 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 493 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 506 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 918 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 1232 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 811 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1263 |
| 5 | `<src>he's been without food, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに</tgt>` | `<src>he's going to </src><tgt>ある時、彼はイエスが飢えていることを知っています。そして、</tgt>` | 1564 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1512 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry. </src><tgt><\|wait\|></tgt>` | 1820 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>And so he sends </src><tgt><\|wait\|></tgt>` | 1950 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>to Jesus. </src><tgt><\|wait\|></tgt>` | 1652 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>Hey, if you're the Son of God, prove it. </src><tgt>40日間、荒野で飢え続けることになることを知っています。だから彼はイエスに送ります。「おい、もしお前が神の御子なら、証明してみろ」と。</tgt>` | 3086 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn </src><tgt><\|wait\|></tgt>` | 1419 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>these stones to bread. </src><tgt><\|wait\|></tgt>` | 1468 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 868 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that? </src><tgt><\|wait\|></tgt>` | 478 |
| 15 | `<src>temptation? </src><tgt>この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>That temptation. </src><tgt>彼はどうやってそれを乗り越えたのか？その誘惑にどう立ち向かったのか？</tgt>` | 1161 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 337 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 609 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>Alone. </src><tgt><\|wait\|></tgt>` | 312 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1189 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 1144 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 995 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1262 |
| 5 | `<src>came along </src><tgt>有意义的个人权利，而最高法院</tgt>` | `<src>came along </src><tgt>有意义的个人权利，最高法院</tgt>` | 1134 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | 1403 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 950 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1453 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1972 |
| 10 | `<src>change </src><tgt>是最后才介入的，不是引领者。我不认为</tgt>` | `<src>social change </src><tgt>最后才跟进，而不是引领。我不认为法院想成为</tgt>` | 1937 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 1267 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1155 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>But they rather reflect </src><tgt><\|wait\|></tgt>` | 1764 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1242 |
| 15 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt>社会变革的先锋。但它们更多地反映的是</tgt>` | 1088 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | 557 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 750 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>you have some </src><tgt><\|wait\|></tgt>` | 645 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges </src><tgt><\|wait\|></tgt>` | 398 |
| 20 | `<src><\|wait\|></src><tgt>反映已经形成的共识。所以，有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>已经形成的共识。所以，</tgt>` | 529 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 409 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 961 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1399 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 816 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的不分分呢，</src><tgt><\|wait\|></tgt>` | 1372 |
| 5 | `<src>的一个是客厅</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면</tgt>` | `<src>我们可以看到的一个是</src><tgt>그럼 사진을 한번 살펴볼게요. 사진의 구분은</tgt>` | 1455 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>课听的部分，</src><tgt><\|wait\|></tgt>` | 1498 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>课听一般都</src><tgt><\|wait\|></tgt>` | 1564 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1665 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>是属于我们在</src><tgt><\|wait\|></tgt>` | 801 |
| 10 | `<src>在休息的地方，</src><tgt>거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src><\|wait\|></src><tgt>보니까 ' 강의 듣기 ' 부분이 있네요. 강의 듣기는 보통</tgt>` | 2865 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>休息的地方，所以</src><tgt><\|wait\|></tgt>` | 1048 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>呢是身体的部分</src><tgt><\|wait\|></tgt>` | 1890 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1139 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 855 |
| 15 | `<src>一点时间，</src><tgt>그래서 이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>一点时间</src><tgt>쉬는 시간이에요. 그래서 신체적인 부분은</tgt>` | 954 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 772 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt><\|wait\|></tgt>` | 694 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们可以看到这边是</src><tgt><\|wait\|></tgt>` | 595 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>小朋友</src><tgt><\|wait\|></tgt>` | 298 |
| 20 | `<src>啊，</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는 아무도 없네요.</tgt>` | `<src>一个人的人，好，</src><tgt>잠시 앉아서 쉬면서 시간을 갖는 걸 의미해요. 여기 보면 아이 한 명 있는 걸 볼 수 있네요. 네,</tgt>` | 707 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以意思是说。</src><tgt><\|wait\|></tgt>` | 344 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 821 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1259 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 930 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1264 |
| 5 | `<src><\|wait\|></src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src><\|wait\|></src><tgt>これらの人々は極めて稀で、</tgt>` | 1447 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize the world </src><tgt><\|wait\|></tgt>` | 1525 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1024 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>the personality is something that </src><tgt><\|wait\|></tgt>` | 924 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>have a contradiction, </src><tgt><\|wait\|></tgt>` | 1978 |
| 10 | `<src>contradiction. </src><tgt>世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>世界を完全に変革することがよくあります。その性格には矛盾があり、</tgt>` | 2867 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>while they're </src><tgt><\|wait\|></tgt>` | 799 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | 1697 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1012 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations, </src><tgt><\|wait\|></tgt>` | 1469 |
| 15 | `<src>and like to </src><tgt>外交的である一方、無意味な会話は嫌います。そして、</tgt>` | `<src><\|wait\|></src><tgt>外向的である一方で、無意味な会話も嫌い、</tgt>` | 1071 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to </src><tgt><\|wait\|></tgt>` | 824 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 640 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love to </src><tgt><\|wait\|></tgt>` | 490 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 412 |
| 20 | `<src>the devil's advocate, and they </src><tgt>要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>play the devil's advocate, </src><tgt>要点をまっすぐ言うことを好みます。また、悪魔の代弁者になるのも好きで、</tgt>` | 710 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 369 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 331 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 359 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Any AP </src><tgt><\|wait\|></tgt>` | 343 |
| 25 | `<src>ENTP stands for </src><tgt>議論を避けることはありません。ENTPとは</tgt>` | `<src>stands for. </src><tgt>議論を避けることは決してありません。APとは、</tgt>` | 456 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1010 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>강물 을 거부 한 </src><tgt><\|wait\|></tgt>` | 1507 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 713 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1208 |
| 5 | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1379 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1520 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1571 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1477 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 966 |
| 10 | `<src>김종인 을 </src><tgt>for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>김종인 을 </src><tgt>put forward his reason for rejecting the candidate— that it was for the sake of the candidate's victory— and even seemed to be trying to look good. But now, Yoon Suk- yeol</tgt>` | 3787 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1896 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | 584 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>더러내놓고 </src><tgt><\|wait\|></tgt>` | 1524 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 874 |
| 15 | `<src><\|wait\|></src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>떨어뜨리 겠다는 뚜끼를 </src><tgt>removed Kim Jong- in, and Lee Jun- seok</tgt>` | 1151 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt><\|wait\|></tgt>` | 473 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 548 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 358 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 377 |
| 20 | `<src><\|wait\|></src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's</tgt>` | `<src>가슴 발 </src><tgt>is determined to attack Yoon Suk- yeol, showing his aggressive nature.</tgt>` | 607 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상급언 </src><tgt><\|wait\|></tgt>` | 388 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 349 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 477 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 320 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute— what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까. </src><tgt>How much of a boon is this for the Democratic Party's attack?</tgt>` | 402 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 4.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後ね今</src><tgt><\|wait\|></tgt>` | 900 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいな</src><tgt><\|wait\|></tgt>` | 1120 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>ですね。なので</src><tgt><\|wait\|></tgt>` | 1113 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ここの木彫サロンホテル</src><tgt>Well, I'd like to make something after a meal. So,</tgt>` | 1471 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1011 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1160 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1591 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっているので</src><tgt><\|wait\|></tgt>` | 1938 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt>since this Mokuro Hotel Salon also has breakfast, I'm planning to</tgt>` | 2008 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1276 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいなと</src><tgt><\|wait\|></tgt>` | 1193 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>いう方はですね</src><tgt><\|wait\|></tgt>` | 1711 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1373 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>まあいいんじゃないか</src><tgt>consider staying at the Goldston Hotel in the future. I think it might be a good option.</tgt>` | 1211 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt><\|wait\|></tgt>` | 456 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>と思います。</src><tgt><\|wait\|></tgt>` | 600 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここのホテルからですね。</src><tgt><\|wait\|></tgt>` | 662 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 490 |
| 20 | `<src><\|wait\|></src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>もう歩いて</src><tgt>Yes, I think so. From this hotel, you can also walk to Busan Station.</tgt>` | 603 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分</src><tgt><\|wait\|></tgt>` | 261 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 490 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 344 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 320 |
| 25 | `<src>ホテルになってますので</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>なってますので</src><tgt>The location is really good— it's about a one- minute walk, or maybe less.</tgt>` | 468 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>行きたらですね</src><tgt><\|wait\|></tgt>` | 385 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 282 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それならあの</src><tgt><\|wait\|></tgt>` | 269 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は。</src><tgt><\|wait\|></tgt>` | 185 |
