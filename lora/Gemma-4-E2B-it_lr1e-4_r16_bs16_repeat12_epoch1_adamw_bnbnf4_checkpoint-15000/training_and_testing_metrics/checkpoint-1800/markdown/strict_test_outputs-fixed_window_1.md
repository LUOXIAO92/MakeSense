# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9568
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4437
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 683
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 88
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1349.1390
  - PROCESS_TIME_MS_P50: 1332.3640
  - PROCESS_TIME_MS_P95: 2080.2590
  - PROCESS_TIME_MS_MAX: 2977.1820

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1127 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>在松子这里呢？</src><tgt>Why is it at the pine nut?</tgt>` | 1248 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个油量很大，</src><tgt><\|wait\|></tgt>` | 1239 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src>然后</src><tgt>There's a lot of oil here,</tgt>` | 1351 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1321 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放点</src><tgt>and then I'm adding</tgt>` | 1546 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>核桃仁，</src><tgt><\|wait\|></tgt>` | 890 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>some walnuts,</tgt>` | 1511 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>感觉</src><tgt><\|wait\|></tgt>` | 1295 |
| 10 | `<src>这种核桃</src><tgt>some walnut kernels— this kind of</tgt>` | `<src>这些</src><tgt>and I feel</tgt>` | 1701 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>核桃仁。</src><tgt><\|wait\|></tgt>` | 656 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 760 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの</src><tgt>从一开始</tgt>` | 771 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>特に仲まだ</src><tgt><\|wait\|></tgt>` | 1370 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>，特别是我们还有一年级。</tgt>` | 1290 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1576 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう密告</src><tgt>那时候</tgt>` | 1308 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1016 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数して</src><tgt>就密告选举，</tgt>` | 1915 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>あげると</src><tgt><\|wait\|></tgt>` | 1133 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>1年経っても</src><tgt>就算过了好几年，</tgt>` | 1877 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した</src><tgt><\|wait\|></tgt>` | 1276 |

---

### Test Example 3 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1247 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>직성 들은 </src><tgt>Those on the list</tgt>` | 1328 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 980 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt>actually have high intelligence</tgt>` | 1362 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1323 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt>and were randomly selected</tgt>` | 1670 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>직성 들이 </src><tgt><\|wait\|></tgt>` | 1213 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>있었기 때문 입니다. </src><tgt>because they were not actually selected.</tgt>` | 1972 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 590 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt>In fact,</tgt>` | 1684 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1558 |

---

### Test Example 4 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1141 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>做的是</src><tgt>What parents need to do is</tgt>` | 1390 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱</src><tgt>use our deep love</tgt>` | 1450 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>交水，</src><tgt><\|wait\|></tgt>` | 1166 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十分</src><tgt>to water the plants</tgt>` | 1638 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>去</src><tgt><\|wait\|></tgt>` | 1185 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心里养养。</src><tgt>and nurture their children's hearts.</tgt>` | 1862 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 694 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>你耐心等</src><tgt>Be patient</tgt>` | 1826 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 1512 |

---

### Test Example 5 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>용심이 </src><tgt>I'm</tgt>` | 807 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1412 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용심이 </src><tgt>a sword- minded person.</tgt>` | 1228 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>새우 용심이 가 </src><tgt><\|wait\|></tgt>` | 1728 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>A shrimp- minded person</tgt>` | 1653 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1498 |
| 8 | `<src>야, </src><tgt>it's a mix of rice noodles and ongsimi. Man,</tgt>` | `<src>야 </src><tgt>is mixed in. Hey,</tgt>` | 1115 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1111 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>this is seriously killer for a hangover,</tgt>` | `<src>행동 으로 </src><tgt>this is really</tgt>` | 1792 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽기 만장 </src><tgt><\|wait\|></tgt>` | 1570 |

---

### Test Example 6 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1005 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这块</tgt>` | 811 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まった</src><tgt><\|wait\|></tgt>` | 1375 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>开始的，</tgt>` | 1122 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1365 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ごうぎゃん</src><tgt>就是</tgt>` | 718 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1652 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザムの</src><tgt>“五五五”</tgt>` | 1727 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1513 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の</src><tgt>这个“月之子”</tgt>` | 1361 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵、</src><tgt><\|wait\|></tgt>` | 872 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt>的画，</tgt>` | 1752 |

---

### Test Example 7 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1142 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1014 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1223 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learned that you repeat </src><tgt>重复一下。记住，</tgt>` | 1379 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>five or you're good at </src><tgt><\|wait\|></tgt>` | 1528 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it </src><tgt>重复五次就掌握了，</tgt>` | 1917 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and will you </src><tgt><\|wait\|></tgt>` | 1640 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>not get that </src><tgt>多做几次，</tgt>` | 1521 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>to people around you to help you with </src><tgt><\|wait\|></tgt>` | 1354 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>你会不会</tgt>` | 879 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and tell next time </src><tgt><\|wait\|></tgt>` | 1858 |

---

### Test Example 8 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气数是容易的，</src><tgt>気数を気にするのは簡単です。</tgt>` | 1857 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1043 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>但是只有</src><tgt>でも、</tgt>` | 887 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导到</src><tgt><\|wait\|></tgt>` | 1275 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>師匠に指導してもらう</tgt>` | 1872 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>卢花出于中，</src><tgt><\|wait\|></tgt>` | 1747 |
| 8 | `<src>所以</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、</tgt>` | `<src>所以</src><tgt>と、</tgt>` | 1459 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 826 |
| 10 | `<src>要成为</src><tgt>シュ・アファンは</tgt>` | `<src>要成为一个</src><tgt>反省が必要です。</tgt>` | 1462 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>师傅，</src><tgt><\|wait\|></tgt>` | 1808 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 858 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I am</tgt>` | 891 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 을 켜 버리 고 </src><tgt><\|wait\|></tgt>` | 1640 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>turning on Apple</tgt>` | 965 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1574 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모든 어 죽인 </src><tgt>and killing all of my</tgt>` | 1696 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헬레나 </src><tgt><\|wait\|></tgt>` | 1379 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>enemies, Helena.</tgt>` | 1223 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1106 |
| 10 | `<src><\|wait\|></src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>같은 세대 들인 </src><tgt>I'm in the same generation as Park Han- sang</tgt>` | 2104 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>것이다. </src><tgt><\|wait\|></tgt>` | 2044 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1037 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙玩以后呢，</src><tgt>砂を遊び終わった後、</tgt>` | 1814 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的 electrolyte</src><tgt><\|wait\|></tgt>` | 1120 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也</src><tgt>内部の電解質エネルギーも</tgt>` | 1241 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷出来了，</src><tgt><\|wait\|></tgt>` | 976 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>然后就停留在</src><tgt>刷り出されて、</tgt>` | 1810 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1676 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>一个相对的低能量的</src><tgt>比較的低エネルギーの</tgt>` | 1551 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>运行状态。</src><tgt><\|wait\|></tgt>` | 608 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是</src><tgt>稼働状態に留まります。これが</tgt>` | 1752 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>所谓的易于状态。</src><tgt><\|wait\|></tgt>` | 2390 |

---

### Test Example 11 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 805 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>body doing? </src><tgt>你的身体在做什么？</tgt>` | 1321 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1435 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does </src><tgt>把针尖点在你的身体上。</tgt>` | 1237 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1060 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么？</tgt>` | 1961 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 1765 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it tension in your chest? </src><tgt>是头？还是胸部紧张？</tgt>` | 1689 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I have </src><tgt><\|wait\|></tgt>` | 1764 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>a lot of </src><tgt>我</tgt>` | 1403 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>things I use. </src><tgt><\|wait\|></tgt>` | 1885 |

---

### Test Example 12 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 849 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>산줄에 </src><tgt>The other mountain range</tgt>` | 963 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여달라고 해가지고 </src><tgt><\|wait\|></tgt>` | 1503 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>내가 죽이기로 하도 </src><tgt>asked me to kill it,</tgt>` | 1682 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 </src><tgt><\|wait\|></tgt>` | 1082 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>메주를 </src><tgt>so I decided to</tgt>` | 1723 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여달라고 하잖아. 내가 </src><tgt><\|wait\|></tgt>` | 1788 |
| 8 | `<src>그 소리 안 듣고 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt>kill the other mountain range too. I'm not even listening to the big</tgt>` | 1897 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주자네. </src><tgt><\|wait\|></tgt>` | 1888 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아, </src><tgt>man. Ah,</tgt>` | 1748 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1500 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 828 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt>重要な研究を</tgt>` | 894 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1307 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people? </src><tgt>行いましたか？極度に幸せな人たちについて、</tgt>` | 2085 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>This is tip of the stem. </src><tgt><\|wait\|></tgt>` | 1046 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>Research looking at </src><tgt>これは枝の先端です。研究は</tgt>` | 1818 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1766 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>10%の</tgt>` | 1480 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1809 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, </src><tgt>最も幸せな人たちを対象にしています。</tgt>` | 1344 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | 2160 |

---

### Test Example 14 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 879 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If a female high school student</tgt>` | 1439 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相怪的人之间</src><tgt><\|wait\|></tgt>` | 1417 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>is attracted to someone with a strange appearance,</tgt>` | 1442 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>有着某种心理，</src><tgt><\|wait\|></tgt>` | 872 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>难道会是</src><tgt>is it possible that</tgt>` | 1652 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1640 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天夜里</src><tgt>they're falling in love overnight?</tgt>` | 1548 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 585 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1785 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思维</src><tgt>Yang Zi's mind</tgt>` | 1820 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>连篇。</src><tgt><\|wait\|></tgt>` | 1453 |

---

### Test Example 15 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对</src><tgt><\|wait\|></tgt>` | 809 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>这种情况，我们就是</src><tgt>When faced with this situation,</tgt>` | 1347 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1019 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>if you encounter a problem, quickly report it to your supervisor.</tgt>` | 2269 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 732 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt>Or let them know we've seen this situation.</tgt>` | 2008 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1700 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't think you have to handle everything yourself.</tgt>` | 1673 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>扛得不理成本。</src><tgt><\|wait\|></tgt>` | 1865 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>责任而已，</src><tgt>It's just a responsibility.</tgt>` | 2408 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是个解决方案。</src><tgt><\|wait\|></tgt>` | 924 |

---

### Test Example 16 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>あとなんか</src><tgt><\|wait\|></tgt>` | 1145 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>ちょっと距離が離れてくる</src><tgt>还有，</tgt>` | 945 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1271 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>大将が</src><tgt>大将好像有点想拉开距离，</tgt>` | 1461 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>たがれっぽいですね。</src><tgt><\|wait\|></tgt>` | 1491 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>回避したい方って</src><tgt>好像有点想躲开。</tgt>` | 1712 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ生き生きして다가 </src><tgt><\|wait\|></tgt>` | 1626 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src><\|wait\|></src><tgt>想躲开的人</tgt>` | 1277 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>し、生き返りて</src><tgt><\|wait\|></tgt>` | 833 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>ととんこんよとしゃぐ</src><tgt>马上就活泼起来，</tgt>` | 2103 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>これが強いので。</src><tgt><\|wait\|></tgt>` | 2289 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので</src><tgt>然后就拼命地</tgt>` | 992 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 827 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>그렇습니다. 거기서</tgt>` | 1088 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 1135 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>という設定が</src><tgt>think라는 설정이</tgt>` | 1176 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 1569 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>で、</src><tgt>있었죠. 그리고</tgt>` | 763 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1299 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井英雄氏の仕組み</src><tgt>나가이 히데오 씨의</tgt>` | 1907 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1375 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>五個。</src><tgt>구조는 다섯 가지입니다.</tgt>` | 1782 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 727 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設定が</src><tgt>설정은</tgt>` | 2667 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>五つ。</src><tgt><\|wait\|></tgt>` | 750 |

---

### Test Example 18 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1135 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>があの</src><tgt>There are T- shirts and</tgt>` | 1406 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただこうという</src><tgt><\|wait\|></tgt>` | 1101 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ものも用意して</src><tgt>other items you can get</tgt>` | 1352 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>おりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 1265 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ご参加ください。</src><tgt>like T- shirts. Please come and join us.</tgt>` | 1929 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1634 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>That's all for the contact information.</tgt>` | 1612 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1725 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>えっと、</src><tgt>Um,</tgt>` | 639 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>内側なん内側がありますので</src><tgt><\|wait\|></tgt>` | 2723 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>お心お持ちください。</src><tgt>please keep your inner side in mind.</tgt>` | 802 |

---

### Test Example 19 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>이걸 너무 </src><tgt>これ、</tgt>` | 1011 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>절여 야 </src><tgt><\|wait\|></tgt>` | 1213 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>할 수 있지만 진짜 보살 도요 </src><tgt>すごく崇めるべきだけど、本当に菩薩様は</tgt>` | 2332 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 </src><tgt><\|wait\|></tgt>` | 732 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 의 보살 인데 꾸밀 필요 가 </src><tgt>ないよ。自分の菩薩なんだから、飾る必要なんて</tgt>` | 2319 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보이 고 </src><tgt><\|wait\|></tgt>` | 1506 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>ないで、私だけ</tgt>` | 1376 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | 2064 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>없어요. 우주 가지 다 </src><tgt>菩薩に見える必要なんてない。宇宙が</tgt>` | 2891 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>이 보살 이란데. </src><tgt><\|wait\|></tgt>` | 1064 |

---

### Test Example 20 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 807 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1397 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>緩むと、</src><tgt>기어가 풀리면</tgt>` | 1197 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えなくなって</src><tgt><\|wait\|></tgt>` | 1693 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>しまうので、</src><tgt>신호가 꺼지기 때문에</tgt>` | 1305 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 979 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>逆ネジの</src><tgt>기어 끝에</tgt>` | 1746 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1284 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>ついているっていうこと</src><tgt>역나사 너트가</tgt>` | 1877 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1181 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>있다는 거죠.</tgt>` | 2149 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイ分解完了。</src><tgt><\|wait\|></tgt>` | 1400 |

---

### Test Example 21 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1140 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>And then, </src><tgt>好的。然后，</tgt>` | 1075 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1275 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | 1201 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1540 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1315 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1030 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际上</tgt>` | 1490 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1449 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>使用这些值。</tgt>` | 1790 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>So this game.board array </src><tgt>所以这个game.board数组</tgt>` | 2668 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1574 |

---

### Test Example 22 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1005 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Chunhataru. </src><tgt>제 이름은 츄나타루입니다.</tgt>` | 1850 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1056 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src>a B.A. in </src><tgt>현재</tgt>` | 1194 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance </src><tgt><\|wait\|></tgt>` | 962 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a B.S. in Psychology. </src><tgt>경영금융학 학사 학위와 심리학 학사 학위를</tgt>` | 2436 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1544 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Yeah, here at Yale. </src><tgt>Yale에서 공부하고 있습니다.</tgt>` | 1413 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And in the </src><tgt><\|wait\|></tgt>` | 1776 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>앞으로는</tgt>` | 1661 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1584 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt>기업 컨설팅 분야로 가고 싶습니다.</tgt>` | 1763 |

---

### Test Example 23 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 836 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>就是进入到</src><tgt>2つ目は、</tgt>` | 1218 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二classList，</src><tgt><\|wait\|></tgt>` | 1143 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>并服务</src><tgt>二つのクラスに</tgt>` | 1147 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1580 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>参加する大牛たちです。</tgt>` | 1716 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 915 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做</src><tgt>例えば、</tgt>` | 1396 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>维新攻总后期</src><tgt><\|wait\|></tgt>` | 1438 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>技能，你会发现</src><tgt>「維新攻総后期」のスキルを</tgt>` | 2051 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维新攻平分的</src><tgt><\|wait\|></tgt>` | 2042 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>星棒</src><tgt>使って維新攻を</tgt>` | 1381 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1630 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 903 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼 늘어나서</tgt>` | 1447 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1201 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. </src><tgt>에너지를 저장해요.</tgt>` | 889 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>And when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1538 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 결합이 끊어지면</tgt>` | 1940 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted </src><tgt><\|wait\|></tgt>` | 1671 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>to other types of energy, </src><tgt>그 잠재 에너지는</tgt>` | 1719 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 1845 |
| 10 | `<src><\|wait\|></src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>Or gets used </src><tgt>열이나 빛 같은 다른 에너지로 바뀌죠.</tgt>` | 1760 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 1611 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용되기도 해요.</tgt>` | 1903 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 669 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>나를</tgt>` | 940 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个</src><tgt><\|wait\|></tgt>` | 1362 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt>내 삶의 궤도로 돌아가게 해줘요.</tgt>` | 1936 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够好好的</src><tgt><\|wait\|></tgt>` | 990 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>扎根的时候，</src><tgt>뿌리내릴 수 있도록, 그때</tgt>` | 1933 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日</src><tgt><\|wait\|></tgt>` | 1702 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>塘热饭，</src><tgt>정성껏 밥을 짓고</tgt>` | 1725 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就这么</src><tgt><\|wait\|></tgt>` | 1814 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>被它照耀，</src><tgt>그렇게 따뜻하게 지켜주세요.</tgt>` | 2043 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>做了一个小小的愿望哈，</src><tgt><\|wait\|></tgt>` | 1582 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src><\|wait\|></src><tgt>작은 소망을 하나</tgt>` | 1691 |

---

### Test Example 26 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐 이라는 </src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이런 것들은 </src><tgt>These things, like vanadium,</tgt>` | 1367 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유실 이 일어날 수가 </src><tgt><\|wait\|></tgt>` | 1566 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt>they can be lost</tgt>` | 1155 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 경우 인 경우 를 </src><tgt><\|wait\|></tgt>` | 1118 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>굉장히 </src><tgt>in cases that are very similar.</tgt>` | 1714 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1652 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다 </src><tgt>They are naturally minerals,</tgt>` | 1647 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1775 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이제 </src><tgt>so</tgt>` | 653 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>지금 이 그런 거죠 </src><tgt><\|wait\|></tgt>` | 2691 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>이제 그 후에다가 </src><tgt>it's like this now,</tgt>` | 1014 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아니면 </src><tgt><\|wait\|></tgt>` | 1255 |

---

### Test Example 27 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 799 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAがですね</src><tgt>Um, A. A.</tgt>` | 1469 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 982 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>生生刻画か</src><tgt>It's used in various situations</tgt>` | 1685 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>っていうジャベるときに</src><tgt><\|wait\|></tgt>` | 1096 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAのRankを</src><tgt>when you're doing a Jave, you know,</tgt>` | 2149 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べてで</src><tgt><\|wait\|></tgt>` | 1593 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あの生生刻画か</src><tgt>you look up the rank of A,</tgt>` | 1614 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>っていう条件する生生刻画で</src><tgt><\|wait\|></tgt>` | 2048 |
| 10 | `<src>ことを保証する</src><tgt>This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>いうことを保証するといった</src><tgt>and then you guarantee that it's a Jave.</tgt>` | 2896 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>こう使い方を</src><tgt><\|wait\|></tgt>` | 932 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>定めました。</src><tgt>We've defined how to use it.</tgt>` | 1343 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 964 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then.</tgt>` | 1398 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>胡波乱跳，</src><tgt><\|wait\|></tgt>` | 1317 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src><\|wait\|></src><tgt>I was just jumping around,</tgt>` | 1019 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1394 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>切肩大概</src><tgt>so I didn't insist on cutting it.</tgt>` | 1925 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1646 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>来剪断，</src><tgt>I had about twelve cuts to make.</tgt>` | 1700 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 1919 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>I had to kick and lift my legs</tgt>` | 1832 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1575 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>without any problems.</tgt>` | 1516 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 582 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1171 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>19세기</tgt>` | 1145 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1369 |
| 4 | `<src>and to explore its </src><tgt>수정헌법 제19조의 의미를 살펴보고,</tgt>` | `<src>and to explore its </src><tgt>수정헌법의 의미와</tgt>` | 1547 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>utility as a guide </src><tgt><\|wait\|></tgt>` | 1081 |
| 6 | `<src>to how political </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src><\|wait\|></src><tgt>그 유용성을 탐구해 보겠습니다.</tgt>` | 1939 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change </src><tgt><\|wait\|></tgt>` | 1765 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>정치적 변화가 어떻게</tgt>` | 1527 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1808 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 일어날 수 있는지 살펴보겠습니다.</tgt>` | 1643 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1762 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>이 수정헌법의 의미는 물론</tgt>` | 1964 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Mary. </src><tgt><\|wait\|></tgt>` | 1142 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1125 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在这</src><tgt>皆さん、</tgt>` | 699 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>个罗马呢，</src><tgt><\|wait\|></tgt>` | 1407 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>このローマは一日にしてできたわけではありません。</tgt>` | 1673 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1241 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>ですから、</tgt>` | 1401 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>熟悉了</src><tgt><\|wait\|></tgt>` | 872 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>你的一些遗迹啊、</src><tgt>今、皆さんが</tgt>` | 2122 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景</src><tgt><\|wait\|></tgt>` | 993 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是你市之间</src><tgt>この遺跡や風景が、</tgt>` | 2050 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就演变出来</src><tgt><\|wait\|></tgt>` | 2028 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src><\|wait\|></src><tgt>一瞬で</tgt>` | 1316 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因此会建议</src><tgt><\|wait\|></tgt>` | 1672 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>属火的朋友呢，</src><tgt>変化したわけではないので、火の年生まれの皆さんは、</tgt>` | 1298 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>扎了一个</src><tgt><\|wait\|></tgt>` | 753 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>线头，</src><tgt>糸を一本結んで、</tgt>` | 1462 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1066 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>找到了线头之后，</src><tgt>糸の端を見つけたら、</tgt>` | 1654 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请务必</src><tgt><\|wait\|></tgt>` | 980 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>抓住</src><tgt>必ず</tgt>` | 1535 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>手，</src><tgt><\|wait\|></tgt>` | 918 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想着</src><tgt>手で掴んでください。</tgt>` | 1643 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>哎，</src><tgt><\|wait\|></tgt>` | 1167 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>那我再去操作下去哦。</src><tgt>そうすると、また操作を続けようとして</tgt>` | 2107 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2043 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>「あ、じゃあまた操作しよう」って言われる理由が分かりますか？</tgt>` | 1810 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1315 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt>なぜなら、</tgt>` | 1237 |

---

### Test Example 32 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 886 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>if you have to produce </src><tgt>ええと、</tgt>` | 1462 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1121 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何か書く必要があるなら、テキストを書く、</tgt>` | 1863 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize </src><tgt><\|wait\|></tgt>` | 783 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>that you don't even know </src><tgt>その時、</tgt>` | 1840 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1652 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. It's like, oh, </src><tgt>単語のスペルすら知らないことに気づくんです。「あ、</tgt>` | 2012 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1836 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>start with a double </src><tgt>この単語、</tgt>` | 1975 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1329 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double m? I don't know. </src><tgt>pが二つ、mが二つで始まるの？わからない。</tgt>` | 2027 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1242 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 845 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150개가 </src><tgt>そのうち150個が</tgt>` | 1581 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중화 버스로 유명 미만 으로 </src><tgt><\|wait\|></tgt>` | 1374 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>中国バスで有名ではない、非常に小さな企業が</tgt>` | 1837 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 709 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くありました。一般的には</tgt>` | 1570 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1858 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>中小企業は成長するか、あるいは</tgt>` | 1507 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>해화법에 그껴도 되는데 </src><tgt><\|wait\|></tgt>` | 2015 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>海運法に収まってもいいのですが、これは</tgt>` | 2423 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업 들은 </src><tgt><\|wait\|></tgt>` | 980 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>中小企業は成長も廃業もしない</tgt>` | 1764 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1420 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 876 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>我们看到的是</src><tgt>이 부분은</tgt>` | 1077 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1139 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>一个戴雪的人，但是他是</src><tgt>눈을 덮은 사람입니다. 하지만</tgt>` | 2097 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的</src><tgt><\|wait\|></tgt>` | 872 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src><\|wait\|></src><tgt>역방향에 속합니다.</tgt>` | 1802 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这种场景一个状况</src><tgt><\|wait\|></tgt>` | 1745 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>需要去</src><tgt>이런 상황은</tgt>` | 1508 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别的注意</src><tgt><\|wait\|></tgt>` | 1781 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能</src><tgt>특별히 주의해야 합니다. 그가</tgt>` | 979 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 2398 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>与他跳不到</src><tgt>그에게</tgt>` | 981 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1265 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>哦。</src><tgt>당신의 의식에 닿을 수 있는지 여부입니다.</tgt>` | 1482 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事，</tgt>` | 1208 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there was </src><tgt><\|wait\|></tgt>` | 1021 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such instances </src><tgt>以前也发生过</tgt>` | 1138 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>before. </src><tgt><\|wait\|></tgt>` | 1586 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>Next future TC </src><tgt>这种情况。</tgt>` | 1295 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>here. </src><tgt><\|wait\|></tgt>` | 980 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>So this is just </src><tgt>接下来是TC。所以这只是</tgt>` | 2192 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1019 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>另一个地方看。</tgt>` | 1952 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1844 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>But </src><tgt>但</tgt>` | 1296 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1510 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>working on Bug Repos </src><tgt>在BugRepo工作</tgt>` | 733 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 1363 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>is just getting going </src><tgt>「</tgt>` | 882 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1316 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt>ただ、</tgt>` | 1144 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1739 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are </src><tgt>やる気を出して、</tgt>` | 1529 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>really important. </src><tgt><\|wait\|></tgt>` | 845 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt>本当に重要な人が10人いるんです。</tgt>` | 2158 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 956 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I have about </src><tgt>それで、</tgt>` | 1850 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1708 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at follow this video. </src><tgt>この動画の続きとして、1分程度の動画を撮って、</tgt>` | 1981 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage </src><tgt><\|wait\|></tgt>` | 1543 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>each one </src><tgt>それぞれを</tgt>` | 1233 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 815 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 880 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃，</src><tgt>呃，</tgt>` | 798 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>hterm이라고 하는 </src><tgt><\|wait\|></tgt>` | 1347 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피터도 </src><tgt>Hterm</tgt>` | 1140 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1698 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt>这个计算机也是可以理解的，</tgt>` | 1626 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 956 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 어 </src><tgt>也是</tgt>` | 1474 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>언어 의 문법 을 </src><tgt><\|wait\|></tgt>` | 1399 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>알게 우리 가 이제 </src><tgt>可以理解计算机语言的语法。我们现在</tgt>` | 2035 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 1924 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>需要编写这些，</tgt>` | 1464 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 1633 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>编写这些的程序</tgt>` | 1314 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 911 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>実は</src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手とか</src><tgt>其实</tgt>` | 786 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>ですかね</src><tgt><\|wait\|></tgt>` | 1400 |
| 4 | `<src>十秒で。</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>恐らく十秒で</src><tgt>一二手的话，大概十秒</tgt>` | 1270 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1649 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ一秒に</src><tgt>就能</tgt>` | 1271 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1008 |
| 8 | `<src>計算ですか</src><tgt>一秒一手多一点</tgt>` | `<src>せつなんですかね</src><tgt>做一秒左右的</tgt>` | 2066 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1044 |
| 10 | `<src>でなんか</src><tgt>这样算。然后</tgt>` | `<src>でなんか</src><tgt>动作吧。</tgt>` | 1719 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 840 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一</src><tgt>大概</tgt>` | 2416 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>二で</src><tgt><\|wait\|></tgt>` | 762 |
| 14 | `<src>あの</src><tgt>十一二手的时候，</tgt>` | `<src>あの</src><tgt>十一二，</tgt>` | 1501 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1312 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>因为要匹配马的动作。</tgt>` | 1079 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 994 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>金運についてですが、今月は</tgt>` | 1848 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 1054 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏正财的部分</src><tgt>かなり良いと言えます。ただ、正財の部分は</tgt>` | 1877 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 709 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>一直是在事业方面的</src><tgt>仕事面で</tgt>` | 1444 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩相当的</src><tgt><\|wait\|></tgt>` | 1668 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>红利收入的</src><tgt>業績の恩恵が</tgt>` | 1622 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果</src><tgt><\|wait\|></tgt>` | 1700 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>在投资理财方面，</src><tgt>かなり上がっています。投資や資産運用に関しては、</tgt>` | 934 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 2517 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>今月も良いですが、</tgt>` | 1169 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说</src><tgt><\|wait\|></tgt>` | 1083 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>少し弱めです。</tgt>` | 1371 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一点。</src><tgt><\|wait\|></tgt>` | 1029 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1075 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어치 보면 </src><tgt>你看，</tgt>` | 799 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1509 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt>最年轻的</tgt>` | 1117 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>동생 이자 </src><tgt><\|wait\|></tgt>` | 1714 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt>弟弟，</tgt>` | 1437 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 993 |
| 8 | `<src>그러니까 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>그러니까 </src><tgt>也是我们家里的弟弟。所以</tgt>` | 1875 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1025 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생 한 거다 는 </src><tgt>我播放的，</tgt>` | 1927 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1520 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt>我自己</tgt>` | 1712 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1517 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt>有点</tgt>` | 658 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 1325 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>생각 했습니다. </src><tgt>多放了点，想着</tgt>` | 1103 |

---

### Test Example 41 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니와 </src><tgt>あなたたちも知っているでしょう。</tgt>` | 1441 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 </src><tgt><\|wait\|></tgt>` | 1010 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인 으로 있을 때에 </src><tgt>異邦人としてここにいるとき、</tgt>` | 1911 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 810 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>말 못하는 우상 에게로 </src><tgt>言葉を話せない偶像に</tgt>` | 1927 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그는 그대로 </src><tgt><\|wait\|></tgt>` | 1761 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>そのまま連れて行かれてしまったのです。</tgt>` | 1607 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1793 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | 1649 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1669 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>あなたたちに知らせます。私は</tgt>` | 1805 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 398 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>神の霊で語る者は、</tgt>` | 1348 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 998 |

---

### Test Example 42 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1225 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>새로 </src><tgt>目を閉じて、</tgt>` | 1011 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>밝을 거야. </src><tgt><\|wait\|></tgt>` | 1274 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>이제 </src><tgt>新しい光が差し込むよ。</tgt>` | 1144 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>서름이 </src><tgt><\|wait\|></tgt>` | 1590 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>돋은 자태 로 </src><tgt>今、</tgt>` | 1298 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>길게 </src><tgt><\|wait\|></tgt>` | 1021 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>흔들 어서 같이 놀자는 거야. </src><tgt>この光に照らされて、長い影を揺らして、一緒に遊ぼうっていうんだ。</tgt>` | 2977 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 1697 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>너무 많이 </src><tgt>お化けが</tgt>` | 724 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>울릴 거고 쓰니 </src><tgt><\|wait\|></tgt>` | 2646 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>요미야 너 지켜 주라고 </src><tgt>泣きすぎて、</tgt>` | 1000 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주라고 </src><tgt><\|wait\|></tgt>` | 1297 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>그러니까 편안 한 마음 에 </src><tgt>「守ってくれ」って刺してくるから、安心して</tgt>` | 1511 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 1070 |

---

### Test Example 43 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감에 </src><tgt><\|wait\|></tgt>` | 1187 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 해매 입니다. </src><tgt>进入的时候非常困惑。</tgt>` | 1526 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1086 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 </src><tgt>开车</tgt>` | 741 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1748 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>그러면 </src><tgt>走走停停，</tgt>` | 1601 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 </src><tgt><\|wait\|></tgt>` | 956 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>去江北就不用说了，去外国</tgt>` | `<src>가면 말을 할 것도 </src><tgt>如果去江南的话，</tgt>` | 2065 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>왜구 에게 나가 는 것도 </src><tgt><\|wait\|></tgt>` | 824 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>장려 리요. </src><tgt>去外地也算是鼓励。</tgt>` | 2004 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 치안 이요. </src><tgt><\|wait\|></tgt>` | 2744 |
| 12 | `<src>대신 에 </src><tgt>真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>治安呢，</tgt>` | 654 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1622 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>모여 봐요. </src><tgt>不如努力聚在一起。</tgt>` | 1297 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 된 것 같아요. </src><tgt><\|wait\|></tgt>` | 552 |
| 16 | `<src><\|wait\|></src><tgt>这一点倒是做得还行。</tgt>` | `<src><\|wait\|></src><tgt>我觉得这样应该就没问题了。</tgt>` | 906 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1076 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1148 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1170 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt>실제로</tgt>` | 1048 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 1686 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>어디까지 교육을 받았나요? 고등학교를 졸업했나요?</tgt>` | 2080 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1861 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>attainment. </src><tgt>그게 한 단계의 학력 수준입니다.</tgt>` | 1504 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1913 |
| 10 | `<src>and if so, did you graduate? </src><tgt>대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>And if so, </src><tgt>대학에 갔나요? 만약 그렇다면,</tgt>` | 1962 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>did you graduate? </src><tgt><\|wait\|></tgt>` | 1501 |
| 12 | `<src>attainment. </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of attainment. </src><tgt>졸업했나요? 또 다른 단계의 학력 수준입니다.</tgt>` | 1841 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1338 |
| 14 | `<src>now. I'll see you </src><tgt>그럼 오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>그게 전부입니다. 이제</tgt>` | 1144 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 740 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 990 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, </src><tgt>活動、</tgt>` | 878 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>then self-defining </src><tgt><\|wait\|></tgt>` | 1353 |
| 4 | `<src>the standard is because you're </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>what we think that standard is, </src><tgt>その基準を自分たちで定義するんです。</tgt>` | 2038 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1046 |
| 6 | `<src>but the reality </src><tgt>完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>その通りです。</tgt>` | 1589 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is that </src><tgt><\|wait\|></tgt>` | 1729 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>でも、現実には、</tgt>` | 1599 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the block, </src><tgt><\|wait\|></tgt>` | 1739 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards </src><tgt>私たちは新しいブロックの猫なんです。そして基準は</tgt>` | 758 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>have changed </src><tgt><\|wait\|></tgt>` | 2440 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>from twenty years ago, </src><tgt>20年前に変わってから、</tgt>` | 887 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1600 |
| 14 | `<src>a higher standard because </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、</tgt>` | `<src>higher standard </src><tgt>より高い基準を</tgt>` | 1252 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 1082 |
| 16 | `<src>held to a higher standard. </src><tgt>今はすべてがより高い基準を求められているからです。</tgt>` | `<src>is being held to higher standard. </src><tgt>求められているんです。なぜなら、今、すべてがより高い基準を求められているからです。</tgt>` | 998 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 </src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인증 상승 하는 </src><tgt>The stock index</tgt>` | 1130 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인다면 </src><tgt><\|wait\|></tgt>` | 1332 |
| 4 | `<src>이런 대형주 도 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src>이런 대형주 도 </src><tgt>is showing an upward trend, so these large- cap stocks</tgt>` | 2045 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 715 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 </src><tgt>are also likely to rise sharply.</tgt>` | 1800 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 </src><tgt><\|wait\|></tgt>` | 1692 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt>But first,</tgt>` | 1378 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 들이 </src><tgt><\|wait\|></tgt>` | 1818 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt>lightweight stocks</tgt>` | 764 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 2712 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt>move first, so</tgt>` | 1435 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 861 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt>the market cap of lightweight stocks</tgt>` | 1357 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1088 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt>seems worth keeping an eye on.</tgt>` | 879 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1033 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>だから、もちろん</tgt>` | 818 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. </src><tgt><\|wait\|></tgt>` | 1552 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>저희 가 A라는 사람 과 </src><tgt>こういうケースもあります。Aという人と</tgt>` | 1891 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 962 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 컨턴트 예요. </src><tgt>Bという人が相互にコンテントを</tgt>` | 2073 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이게 컨설턴트 </src><tgt><\|wait\|></tgt>` | 1917 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>여가지고 </src><tgt>持っているんです。それがコンサルタントで、</tgt>` | 1432 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1780 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aという人が悪意のあるコードを</tgt>` | 1956 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 1480 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt>渡したとき、Bという人が</tgt>` | 1791 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1297 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크로 사이트 스크트에서 </src><tgt>実際にクロスサイトスクリプトで</tgt>` | 822 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>예시 파일 까지 </src><tgt><\|wait\|></tgt>` | 575 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까 </src><tgt>感染する可能性があるか、</tgt>` | 944 |

---

### Test Example 48 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1045 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう蒸らせてやれ。</src><tgt>그럼 그냥 쪄버려.</tgt>` | 1836 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 965 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src><\|wait\|></src><tgt>나는</tgt>` | 654 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>火勢見ている。</src><tgt><\|wait\|></tgt>` | 1683 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>불길이 치솟는 걸 보고 있어.</tgt>` | 1753 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1536 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超に超えている</src><tgt>이제 한계가</tgt>` | 1371 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈火勢。</src><tgt><\|wait\|></tgt>` | 806 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>아주, 아주 넘어서는 불길이야.</tgt>` | 2040 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 2048 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなでいくを</src><tgt>오랫동안</tgt>` | 1336 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やっている。</src><tgt><\|wait\|></tgt>` | 1623 |
| 14 | `<src>俺は</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>俺はこんなに</src><tgt>이런 불길을 다루고 있어. 나는</tgt>` | 1469 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい海賊線を</src><tgt><\|wait\|></tgt>` | 1148 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>이렇게 엄청난 해적선은 본 적이 없어.</tgt>` | 1024 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1138 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉</src><tgt>相手の</tgt>` | 1077 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>真实意图的，</src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src>或真实意图的。</src><tgt>感情や本心を探る、あるいは相手の意図を感じ取る。</tgt>` | 2307 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 723 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1552 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1479 |
| 8 | `<src>会听到人们</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>听到人们这样说：</src><tgt>よく</tgt>` | 1139 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1032 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 1928 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1630 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了。</src><tgt>この人はまた嘘をついているよ」って言われる。</tgt>` | 1988 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1582 |
| 14 | `<src>已经说明了一切。”</src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>彼の目はすべてを物語っている。</tgt>` | 1329 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1060 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 760 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 549 |

---

### Test Example 50 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1138 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>This is, you know,</tgt>` | 1430 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>と言だったりして、</src><tgt><\|wait\|></tgt>` | 1318 |
| 4 | `<src><\|wait\|></src><tgt>This isn't just a visual development environment;</tgt>` | `<src><\|wait\|></src><tgt>it's a visual development environment,</tgt>` | 1235 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1182 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのも</src><tgt>a visual Python development environment.</tgt>` | 1655 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルンを書いた</src><tgt><\|wait\|></tgt>` | 1782 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>後、とりあえずは</src><tgt>Because after writing the flow graph visually,</tgt>` | 1721 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードを</src><tgt><\|wait\|></tgt>` | 1778 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成させて、それが</src><tgt>we just generate the Python code from that,</tgt>` | 1784 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1717 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるっていう</src><tgt>and that runs, that's how the signal processing happens.</tgt>` | 1977 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているから</src><tgt><\|wait\|></tgt>` | 1291 |
| 14 | `<src><\|wait\|></src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>です。</src><tgt>That's the structure it's built on.</tgt>` | 1107 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 797 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay,</tgt>` | 550 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 824 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>そして、これについて多くの人が</tgt>` | 1439 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1447 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 </src><tgt>分析をしています。ここで</tgt>` | 991 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자 의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1293 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니 가 </src><tgt>ロクジャの分析を見ると、ソニーが</tgt>` | 1956 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 칩에 </src><tgt><\|wait\|></tgt>` | 1826 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FPD 파이프 를 </src><tgt>イエレクトロニクスチップにFPDパイプを</tgt>` | 1713 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1780 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>나충가서 로 보인 다. </src><tgt>128ビットで構成されていると見えます。</tgt>` | 2922 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 931 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈, </src><tgt>Xboxシリーズ、</tgt>` | 1316 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1368 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt>XboxにはないInfinityCache、</tgt>` | 1223 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>LSi가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 921 |
| 16 | `<src><\|wait\|></src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src><\|wait\|></src><tgt>LSiもありません。</tgt>` | 391 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>Fourth of </src><tgt><\|wait\|></tgt>` | 772 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>the month </src><tgt>4월 4일</tgt>` | 1161 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>is the day </src><tgt><\|wait\|></tgt>` | 1150 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>that </src><tgt>은</tgt>` | 1033 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>we </src><tgt><\|wait\|></tgt>` | 1552 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>exclusively dedicate to </src><tgt>우리가</tgt>` | 723 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>love. </src><tgt><\|wait\|></tgt>` | 1297 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src>我们</src><tgt>오직 사랑에 전념하는 날입니다.</tgt>` | 1787 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>也同时</src><tgt><\|wait\|></tgt>` | 1520 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>우리는 동시에</tgt>` | 1128 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>进入恨在早上</src><tgt><\|wait\|></tgt>` | 1215 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>的时候他爱。</src><tgt>아침에 분노를 품고 있을 때도 사랑을 느낍니다.</tgt>` | 2943 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上。</src><tgt><\|wait\|></tgt>` | 1174 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>他就变成恨。</src><tgt>밤이 되면 분노로 변합니다.</tgt>` | 1179 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1293 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆。</src><tgt>그 시계추처럼요.</tgt>` | 1117 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 776 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>继续在移动。</src><tgt>계속 움직입니다.</tgt>` | 568 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 948 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>also, </src><tgt>嗯，另外，</tgt>` | 947 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to move </src><tgt><\|wait\|></tgt>` | 1501 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>meedia objects </src><tgt>你将无法移动媒体对象，</tgt>` | 1583 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1164 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt>因为</tgt>` | 1613 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though, </src><tgt><\|wait\|></tgt>` | 1076 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>if you get into </src><tgt>资源之间</tgt>` | 1442 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt><\|wait\|></tgt>` | 1153 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize </src><tgt>出现这种情况，</tgt>` | 1763 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong </src><tgt><\|wait\|></tgt>` | 1028 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>media files </src><tgt>你发现</tgt>` | 2268 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>to a particular resource, </src><tgt><\|wait\|></tgt>` | 1281 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt>把错误的媒体文件添加到了某个资源上，</tgt>` | 1107 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1278 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files </src><tgt>我们就可以</tgt>` | 1050 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 841 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>they get back up properly. </src><tgt>移动这些媒体文件，并确保它们能正确恢复。</tgt>` | 742 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 912 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>and it warns Jesus </src><tgt>ある時、イエス様は</tgt>` | 1503 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>of hunger. </src><tgt><\|wait\|></tgt>` | 1074 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>He knows that </src><tgt>飢えについて警告されました。</tgt>` | 1019 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1387 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>be in the wilderness </src><tgt>彼は、</tgt>` | 1624 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days </src><tgt><\|wait\|></tgt>` | 1295 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>that he's hungry, </src><tgt>40日間荒野にいることになるでしょう。その間、彼は飢えを</tgt>` | 2268 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>and so he says to Jesus, </src><tgt><\|wait\|></tgt>` | 1945 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>If you're the Son of God, prove it </src><tgt>知っているのです。だからイエス様はこう言われたのです。「もしあなたが神の子なら、</tgt>` | 2453 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1158 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>turn these stones to bread. </src><tgt>この石をパンに変えてみせなさい。」</tgt>` | 1805 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did </src><tgt><\|wait\|></tgt>` | 1294 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>Jesus deal with that </src><tgt>イエス様は</tgt>` | 1059 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 785 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src><\|wait\|></src><tgt>その誘惑にどう対処されたのでしょうか。</tgt>` | 718 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan </src><tgt><\|wait\|></tgt>` | 404 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>lead by bread alone. </src><tgt>パンだけで生きるJonathanは、</tgt>` | 427 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1245 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful </src><tgt>有意义的</tgt>` | 868 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual write </src><tgt><\|wait\|></tgt>` | 1270 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>个人著作，</tgt>` | 1172 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1630 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't know </src><tgt>最高法院最后才介入，而不是作为领导者。我不知道</tgt>` | 1555 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1031 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt>法院是否想</tgt>` | 1596 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1272 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>成为社会变革的先锋。</tgt>` | 1938 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 1732 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>But they rather </src><tgt>但现在，他们更倾向于</tgt>` | 1858 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1634 |
| 14 | `<src>the consensus </src><tgt>它们更倾向于</tgt>` | `<src>reflect the consensus </src><tgt>反映</tgt>` | 1036 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 549 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>已经形成的共识。</tgt>` | 1032 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 752 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt>所以，</tgt>` | 506 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 355 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>你有一些联邦法官</tgt>` | 495 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 379 |

---

### Test Example 56 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1337 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt>最初の数マイルは</tgt>` | 1369 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1147 |
| 4 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src><\|wait\|></src><tgt>少し間違って、</tgt>` | 998 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1491 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src><\|wait\|></src><tgt>AHRフィールドの</tgt>` | 1599 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1010 |
| 8 | `<src>versus variant </src><tgt>決定的な重要性と、</tgt>` | `<src>versus </src><tgt>重要性について</tgt>` | 1339 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1336 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt>バリアントデータベースと</tgt>` | 1890 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | 1710 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that </src><tgt>バリアントデータベースの比較について、これは私の好きな分野の一つです。その</tgt>` | 2091 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>if we don't agree </src><tgt><\|wait\|></tgt>` | 1604 |
| 14 | `<src>upon the fields that need </src><tgt>つまり、</tgt>` | `<src>upon the fields </src><tgt>フィールドについて合意できなければ、</tgt>` | 1365 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in </src><tgt><\|wait\|></tgt>` | 1036 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>these data sources </src><tgt>これらのデータソースに</tgt>` | 843 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from. </src><tgt><\|wait\|></tgt>` | 626 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, right? </src><tgt>取り込むべきフィールドを合意できません。取り込むべきものがないわけですよね？</tgt>` | 796 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 377 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 974 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1521 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1084 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>사진 부분은</tgt>` | 1003 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1407 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>一个是克汀的部分，</src><tgt>크레틴 부분, 그리고</tgt>` | 1307 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>克汀一般</src><tgt><\|wait\|></tgt>` | 1049 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>都是属于</src><tgt>크레틴은 보통</tgt>` | 1753 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1276 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>我们在吸收</src><tgt>우리가</tgt>` | 1709 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的地方，</src><tgt><\|wait\|></tgt>` | 711 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>所以呢，</src><tgt>흡수하는 곳에 있는 거예요. 그래서</tgt>` | 2736 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分会反应的是</src><tgt><\|wait\|></tgt>` | 1668 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给</src><tgt>우리 몸에서 반응하는 건</tgt>` | 597 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 1311 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好好的</src><tgt>우리가</tgt>` | 1041 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做下</src><tgt><\|wait\|></tgt>` | 739 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>来吸收，可以看到</src><tgt>흡수할 시간을 좀 줘야 해요. 흡수할 때</tgt>` | 696 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是五个一人的嘛。</src><tgt><\|wait\|></tgt>` | 453 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt>이 다섯 명의 사람들을 볼 수 있네요. 자,</tgt>` | 555 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 295 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 900 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>彼らは完全に</tgt>` | 1070 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1146 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up </src><tgt>珍しく、</tgt>` | 1073 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1641 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するよう現れることが多いんです。</tgt>` | 1750 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その性格は</tgt>` | 1329 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1157 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾をはらんでいます。</tgt>` | 1923 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>Well, they're </src><tgt><\|wait\|></tgt>` | 1819 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted. </src><tgt>外向的で、</tgt>` | 1661 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>They also hate </src><tgt><\|wait\|></tgt>` | 1658 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 1370 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1056 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>And like to get straight to the </src><tgt>そして</tgt>` | 804 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 575 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>要点をまっすぐ言うのが好きなんです。また、</tgt>` | 492 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 415 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>to play the devil's advocate, </src><tgt>悪魔の代弁者になるのも好きで、</tgt>` | 532 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 308 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることは決してありません。</tgt>` | 380 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 320 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. stands for </src><tgt>E.T.P.は</tgt>` | 388 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for. </src><tgt><\|wait\|></tgt>` | 330 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 1175 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>경무를 거부 한 </src><tgt>Lee Jun- seok previously</tgt>` | 1432 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1211 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt>claimed he was running for the People Power Party on the grounds of refusing to take office,</tgt>` | 2049 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1306 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>and that he was running for the party's nomination,</tgt>` | 1380 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1775 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>even putting on a show for the nomination. But now</tgt>` | 1223 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1838 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt>Yoon Suk- yeol is</tgt>` | 2505 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간, </src><tgt><\|wait\|></tgt>` | 893 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석 은 들은 해놓고 </src><tgt>removing Kim Jong- in, Lee Jun- seok</tgt>` | 1883 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1248 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리 겠다는 </src><tgt>said he would</tgt>` | 1043 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼 를 품은 </src><tgt><\|wait\|></tgt>` | 825 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt>attack him with a axe,</tgt>` | 655 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 442 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>and was determined to</tgt>` | 448 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 297 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt>attack Yoon Suk- yeol. His heart</tgt>` | 391 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 성상납건 </src><tgt><\|wait\|></tgt>` | 370 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt>was a scandal</tgt>` | 311 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 337 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt>that the Democratic Party</tgt>` | 358 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 321 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>で、まあ</src><tgt><\|wait\|></tgt>` | 1090 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt>So, after</tgt>` | 1016 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってみたいな</src><tgt><\|wait\|></tgt>` | 1280 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>です。なので、</src><tgt>dinner, I'd like to make something now. So,</tgt>` | 2083 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのねゴルフスロホテル</src><tgt><\|wait\|></tgt>` | 989 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>も朝食が</src><tgt>the breakfast at this Golf Suro Hotel</tgt>` | 1846 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になっている</src><tgt>is a place where you can eat breakfast.</tgt>` | 1536 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっているので、</src><tgt><\|wait\|></tgt>` | 1855 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt>So, going forward,</tgt>` | 1691 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1758 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいな</src><tgt>I'd like to stay here at the Golf Suro Hotel</tgt>` | 1893 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>という方はですね、</src><tgt><\|wait\|></tgt>` | 1392 |
| 14 | `<src>検討なさってみて</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>検討なさって</src><tgt>if you're considering staying here,</tgt>` | 1048 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 815 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと、はい。</src><tgt>just take a look and see if it's a good fit.</tgt>` | 839 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 357 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>ここホテルからですね。</src><tgt>I think it's fine.</tgt>` | 410 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 283 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>And from here, you can walk to Busan Station</tgt>` | 380 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本かかる</src><tgt><\|wait\|></tgt>` | 312 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんないか</src><tgt>in about a minute.</tgt>` | 367 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 333 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地ね、まあホテル</src><tgt>The location is pretty good,</tgt>` | 392 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので、</src><tgt><\|wait\|></tgt>` | 263 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>and it's a hotel, so if you'd like,</tgt>` | 244 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 189 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>みてください。それでは</src><tgt>please consider it.</tgt>` | 214 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね、今回は。</src><tgt><\|wait\|></tgt>` | 198 |
