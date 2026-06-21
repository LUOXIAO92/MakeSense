# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9623
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.2119
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 419
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 0.2714
  - TGT_RELEASE_TOTAL: 140
  - TGT_WAIT_ACCURACY: 0.7929
  - TGT_WAIT_TOTAL: 309
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1313.3160
  - PROCESS_TIME_MS_P50: 1269.9230
  - PROCESS_TIME_MS_P95: 2092.5150
  - PROCESS_TIME_MS_MAX: 11141.4750

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1087 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>的种子里面，</src><tgt><\|wait\|></tgt>` | 891 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>这个幼苗</src><tgt><\|wait\|></tgt>` | 983 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>要很大，然后</src><tgt>Why is the seed so big? The seedling needs to be big,</tgt>` | 1515 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，我在</src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>放起来</src><tgt><\|wait\|></tgt>` | 1248 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人</src><tgt><\|wait\|></tgt>` | 758 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>and when I plant it,</tgt>` | 1792 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在家里</src><tgt><\|wait\|></tgt>` | 1745 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 1549 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和陶人。</src><tgt><\|wait\|></tgt>` | 1304 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1030 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1139 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生那爱胶水</src><tgt>Parents need to use our love glue</tgt>` | 1326 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1354 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十秒，</src><tgt><\|wait\|></tgt>` | 1163 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给子孩子</src><tgt><\|wait\|></tgt>` | 820 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心里凝养。</src><tgt>for ten seconds to nurture their hearts.</tgt>` | 1890 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src>心耐心</src><tgt><\|wait\|></tgt>` | 1771 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>等他</src><tgt><\|wait\|></tgt>` | 1717 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 1163 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 937 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的，</src><tgt><\|wait\|></tgt>` | 1041 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 1231 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>気数をつけるのは簡単ですが、</tgt>` | 1226 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师父之道</src><tgt><\|wait\|></tgt>` | 1566 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1398 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如出于中坚。</src><tgt><\|wait\|></tgt>` | 777 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt>師父の道は中堅の如しです。ですから、</tgt>` | 1666 |
| 9 | `<src>虚阿凡</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>需要反</src><tgt><\|wait\|></tgt>` | 1497 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 1849 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>师父。</src><tgt><\|wait\|></tgt>` | 1031 |

---

### Test Example 4 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 708 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 922 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>仲までまだ</src><tgt><\|wait\|></tgt>` | 1310 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>1年生ですからね。</src><tgt>从一开始，尤其是仲まで还是大一，</tgt>` | 1348 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>はいはいはい、その時点で</src><tgt><\|wait\|></tgt>` | 1589 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1296 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>美学、</src><tgt><\|wait\|></tgt>` | 765 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>対数していって</src><tgt>嗯嗯嗯，当时</tgt>` | 1468 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>上げる</src><tgt><\|wait\|></tgt>` | 1688 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>と10年経っても</src><tgt><\|wait\|></tgt>` | 2023 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>対した</src><tgt><\|wait\|></tgt>` | 939 |

---

### Test Example 5 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1027 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>lastly, </src><tgt><\|wait\|></tgt>` | 902 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>he repeats </src><tgt><\|wait\|></tgt>` | 1026 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>learning to repeat </src><tgt>最后，他重复学习</tgt>` | 1207 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>by learning to repeat </src><tgt><\|wait\|></tgt>` | 1161 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>by doing more of it </src><tgt><\|wait\|></tgt>` | 1031 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and when you're not </src><tgt><\|wait\|></tgt>` | 1426 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good at it, </src><tgt>通过多做练习来重复，当你不擅长时，</tgt>` | 2079 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>it gets people around you to help you with </src><tgt><\|wait\|></tgt>` | 1894 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1840 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>in tell next time </src><tgt><\|wait\|></tgt>` | 916 |

---

### Test Example 6 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 794 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 928 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely happy </src><tgt><\|wait\|></tgt>` | 1220 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>people. This is </src><tgt>非常に幸せな人々の研究を様々なもので行いました。これは</tgt>` | 1318 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1556 |
| 6 | `<src>research, </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。</tgt>` | `<src>research. Looking </src><tgt><\|wait\|></tgt>` | 1394 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>at 10% </src><tgt><\|wait\|></tgt>` | 718 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt>研究の端緒です。最も幸せな人々の10%を見ます。</tgt>` | 1943 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people out </src><tgt><\|wait\|></tgt>` | 1408 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>there. People who live </src><tgt><\|wait\|></tgt>` | 2138 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>will we can learn from. </src><tgt><\|wait\|></tgt>` | 904 |

---

### Test Example 7 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>영심이 </src><tgt><\|wait\|></tgt>` | 951 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1311 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 웅심이 </src><tgt>I have a sword spirit, and</tgt>` | 1167 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어우칼 웅심이 가 </src><tgt><\|wait\|></tgt>` | 1773 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1400 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>석화 되는 건데요. </src><tgt><\|wait\|></tgt>` | 1834 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt>the sword spirit is becoming a stone. Wow,</tgt>` | 1654 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 837 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행동 으로도 </src><tgt><\|wait\|></tgt>` | 1966 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽입니다. </src><tgt><\|wait\|></tgt>` | 1644 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 822 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 958 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 쳐박히고 </src><tgt><\|wait\|></tgt>` | 1457 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 986 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt>I'm</tgt>` | 1553 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 겪긴 </src><tgt><\|wait\|></tgt>` | 1355 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>해야 르나 </src><tgt><\|wait\|></tgt>` | 622 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1663 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt>how I've been buried, or how I've been through it myself, or</tgt>` | 2978 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1377 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1695 |

---

### Test Example 9 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1139 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들은 </src><tgt><\|wait\|></tgt>` | 1008 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1224 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt>The NickS on the list actually don't have high intelligence,</tgt>` | 1695 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않고 </src><tgt><\|wait\|></tgt>` | 1044 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1643 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들이었기 때문 </src><tgt><\|wait\|></tgt>` | 1808 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt>they were just randomly selected.</tgt>` | 1773 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1425 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 1262 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1997 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后，</src><tgt><\|wait\|></tgt>` | 1031 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 965 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>的液体检清</src><tgt><\|wait\|></tgt>` | 1282 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt>淘撒が終わったら、内部の液体検査エネルギーも</tgt>` | 1281 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷了落了，然后就</src><tgt><\|wait\|></tgt>` | 1642 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1331 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1807 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态</src><tgt>落ちた。そして、比較的低エネルギーな動作状態に留まる。</tgt>` | 1887 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>态。</src><tgt><\|wait\|></tgt>` | 1556 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1232 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>的低语状态。</src><tgt><\|wait\|></tgt>` | 1988 |

---

### Test Example 11 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 너무 </src><tgt><\|wait\|></tgt>` | 985 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이 저희 에 </src><tgt><\|wait\|></tgt>` | 967 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>일수 있지만 </src><tgt>これは</tgt>` | 1238 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1176 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기가 </src><tgt><\|wait\|></tgt>` | 1571 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>あまりにも</tgt>` | 1542 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>필요 로 보이 고 </src><tgt><\|wait\|></tgt>` | 1807 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 이 보살 로 </src><tgt><\|wait\|></tgt>` | 1124 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보일 필요 로 보이 세 우주 가 </src><tgt>必要で、本当に菩薩であるのに夢が必要に見える。私だけが菩薩に見える</tgt>` | 2557 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>있다. 이 보살 이란 </src><tgt><\|wait\|></tgt>` | 1311 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>그런데. </src><tgt><\|wait\|></tgt>` | 1785 |

---

### Test Example 12 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 843 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 967 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただきたいようなものも</src><tgt>I'd like you to have things like T-shirts,</tgt>` | 1528 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1437 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ぜひご参考ください。</src><tgt><\|wait\|></tgt>` | 1283 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 748 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt>so please refer to them. As for contact,</tgt>` | 1889 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>で、えっと</src><tgt><\|wait\|></tgt>` | 1788 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>何ていうか</src><tgt><\|wait\|></tgt>` | 1929 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>何ていうか</src><tgt><\|wait\|></tgt>` | 960 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>何ていうか</src><tgt><\|wait\|></tgt>` | 1827 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 853 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt><\|wait\|></tgt>` | 997 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여 달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1458 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 길리 고 들어왔어. </src><tgt>I came here because someone on the advanced side told me to kill him.</tgt>` | 2219 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 826 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>전진 쪽에 달아차는 </src><tgt><\|wait\|></tgt>` | 1344 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>거야. 내가 </src><tgt><\|wait\|></tgt>` | 1802 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt>I wasn't listening to the other front lines.</tgt>` | 2390 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>중요한 거야. </src><tgt><\|wait\|></tgt>` | 1937 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>하. </src><tgt><\|wait\|></tgt>` | 1893 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 514 |

---

### Test Example 14 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 648 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 894 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1115 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>鬼道号，</src><tgt>저를 귀도호로 돌아가게 해 주세요.</tgt>` | 1366 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够好好的</src><tgt><\|wait\|></tgt>` | 1465 |
| 6 | `<src>在他下班的时候，</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在它下面的时候，</src><tgt><\|wait\|></tgt>` | 1272 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日</src><tgt><\|wait\|></tgt>` | 738 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>唐日令夜</src><tgt>그 아래에서 잘 지내게 해 주세요. 그날은</tgt>` | 2031 |
| 9 | `<src><\|wait\|></src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>的日，我当时</src><tgt><\|wait\|></tgt>` | 1692 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被痛痛的</src><tgt><\|wait\|></tgt>` | 2087 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的小小的一个愿望</src><tgt><\|wait\|></tgt>` | 1003 |
| 12 | `<src>哈。</src><tgt>그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>哦。</src><tgt>그날, 저는 그 작은 소원을</tgt>` | 1720 |

---

### Test Example 15 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1092 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1189 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が</src><tgt>好像Advantageさん有点离得远了，</tgt>` | 1253 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱりですね、</src><tgt><\|wait\|></tgt>` | 1489 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>囲いしたい方って</src><tgt><\|wait\|></tgt>` | 1485 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ囲いこしけたい</src><tgt><\|wait\|></tgt>` | 1869 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>のが</src><tgt><\|wait\|></tgt>` | 988 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>ですね、でも</src><tgt>果然是想围住对方的人，马上想围住对方，</tgt>` | 2102 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と本気で</src><tgt><\|wait\|></tgt>` | 1472 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>シャグが強いので、</src><tgt><\|wait\|></tgt>` | 1881 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 532 |

---

### Test Example 16 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 959 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src>始まったもので</src><tgt><\|wait\|></tgt>` | 1208 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 985 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご方法</src><tgt>大概是从这里开始的，</tgt>` | 1389 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 809 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ご言やん</src><tgt><\|wait\|></tgt>` | 1370 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt><\|wait\|></tgt>` | 1793 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1806 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ルナールなどという人の</src><tgt>比如“Go-Yan”或“Cezanne”这样的</tgt>` | 2653 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵は田舎の</src><tgt><\|wait\|></tgt>` | 1881 |
| 12 | `<src>中学生でも。</src><tgt>像梵高、高更、塞尚、雷诺阿他们的画，连乡下的中学生都……</tgt>` | `<src>中学生でも</src><tgt><\|wait\|></tgt>` | 612 |

---

### Test Example 17 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 721 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>body saying? </src><tgt><\|wait\|></tgt>` | 980 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1394 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt>你的身体在说什么？把针头插到你的身体上。身体</tgt>` | 1736 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt><\|wait\|></tgt>` | 1068 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>What is it? Is it </src><tgt><\|wait\|></tgt>` | 1480 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>a day? </src><tgt><\|wait\|></tgt>` | 1782 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it tension in your chest? </src><tgt>开始紧张的地方在哪里？是什么？是身体？是胸部紧张吗？</tgt>` | 2855 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>Or is the body </src><tgt><\|wait\|></tgt>` | 1591 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>lacking in which are you </src><tgt><\|wait\|></tgt>` | 2090 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>using? </src><tgt><\|wait\|></tgt>` | 632 |

---

### Test Example 18 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1100 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 972 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 1304 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>好的，在这些例子之后，</tgt>` | 1191 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1499 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1351 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 565 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>指令告诉我们</tgt>` | 1606 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1772 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 1572 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>实际使用这些值。</tgt>` | 1369 |
| 12 | `<src>this game dot scored array. </src><tgt>要使用这些值。也就是这个game.scored数组。</tgt>` | `<src>So this game.board array </src><tgt><\|wait\|></tgt>` | 1868 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 858 |

---

### Test Example 19 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为这个情况</src><tgt><\|wait\|></tgt>` | 884 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 920 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1308 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就感谢</src><tgt>Because of this situation, we've run into a problem, and we're grateful</tgt>` | 1882 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>各位的回报主管</src><tgt><\|wait\|></tgt>` | 1075 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1424 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt><\|wait\|></tgt>` | 1775 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>不要想自己怎么都把它扛下来，</src><tgt>to the reward supervisors, or to the person we're notifying, we're just laughing at the situation. Don't think you have to carry it all.</tgt>` | 3417 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>工具理性</src><tgt><\|wait\|></tgt>` | 1270 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>承当责任，</src><tgt><\|wait\|></tgt>` | 1916 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>责任是给属人。</src><tgt><\|wait\|></tgt>` | 923 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 724 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 998 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间，</src><tgt><\|wait\|></tgt>` | 1450 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>又</src><tgt>If you're a high school girl and you're with someone who's not unattractive,</tgt>` | 2035 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>有这么重要性，</src><tgt><\|wait\|></tgt>` | 1008 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1212 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1820 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里开始的</src><tgt>does it really matter?</tgt>` | 1830 |
| 9 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1719 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1162 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1824 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>系列篇。</src><tgt>It's the Yang Zisi series.</tgt>` | 975 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 845 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>so here, </src><tgt><\|wait\|></tgt>` | 970 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src>you have to </src><tgt><\|wait\|></tgt>` | 1308 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>do 7.2 GB </src><tgt>자, 여기서는 7.2GB를</tgt>` | 1474 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>already, right? </src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1303 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 657 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>the base of the </src><tgt>이미 사용하고 계시죠? 그리고</tgt>` | 1639 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>iOS </src><tgt><\|wait\|></tgt>` | 1679 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>of the </src><tgt><\|wait\|></tgt>` | 1761 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7.2 GB </src><tgt><\|wait\|></tgt>` | 1140 |
| 12 | `<src>設備寺、五比</src><tgt>파생 형용사의 구조는 어근, 접미사, 어미로</tgt>` | `<src>GB. </src><tgt>iOS 7.2GB의 기본입니다.</tgt>` | 1852 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 1458 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1057 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 886 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアが緩むと</src><tgt>이것이 기어입니다. 기어가 헐거워지면</tgt>` | 1790 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 761 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>逆にできなくなってしまう</src><tgt><\|wait\|></tgt>` | 1608 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1201 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt>신호가 오히려 안 되게 되니까, 기어 끝에</tgt>` | 1030 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1379 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt><\|wait\|></tgt>` | 1860 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 1932 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt>역나사 너트가 붙어 있다는 거죠.</tgt>` | 1138 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1667 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文部会完了を</src><tgt><\|wait\|></tgt>` | 1590 |

---

### Test Example 23 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 862 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>二期市场，</src><tgt>2つ目は第2期市場です。</tgt>` | 1605 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会服务</src><tgt><\|wait\|></tgt>` | 860 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一期一线</src><tgt><\|wait\|></tgt>` | 1565 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>第1期の一線大牛たちを支援します。</tgt>` | 1720 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1766 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt><\|wait\|></tgt>` | 1664 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>沟通好事期间，</src><tgt>例えば、微信で</tgt>` | 1011 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1607 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>微信好</src><tgt><\|wait\|></tgt>` | 1063 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>平分的星棒</src><tgt><\|wait\|></tgt>` | 1519 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt>良い星棒がうまく回るんです。</tgt>` | 1760 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 805 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A Aが</src><tgt><\|wait\|></tgt>` | 950 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>あるんですね。</src><tgt><\|wait\|></tgt>` | 1305 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>色々な場面で</src><tgt>There's an A A, you see. In various situations,</tgt>` | 1509 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>清掃活動とか</src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>でAの欄を</src><tgt><\|wait\|></tgt>` | 1564 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べてそこで</src><tgt><\|wait\|></tgt>` | 1784 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あの清掃活動とか</src><tgt>like cleaning activities, you look up the A column, and there's also</tgt>` | 2760 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>清掃する清掃で</src><tgt><\|wait\|></tgt>` | 1728 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>こと保証するって言った</src><tgt><\|wait\|></tgt>` | 2086 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>使い方をされました。</src><tgt>a guarantee for cleaning activities.</tgt>` | 971 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1164 |

---

### Test Example 25 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 942 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1181 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是以前造成的</src><tgt>皆さんにお伝えしたいのですが、このローマでは以前の</tgt>` | 1310 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1449 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1233 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 769 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt>危機は、</tgt>` | 1684 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>跟丰收</src><tgt><\|wait\|></tgt>` | 1785 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1574 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间就演变出来。</src><tgt><\|wait\|></tgt>` | 1396 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src>的</src><tgt>豊作と危機が同時に起こることはありません。</tgt>` | 1866 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1018 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>我的朋友呢，</src><tgt><\|wait\|></tgt>` | 1052 |

---

### Test Example 26 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1091 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1086 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1179 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore </src><tgt>19세기 수정헌법의 의미와</tgt>` | 1231 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>it as a guide </src><tgt><\|wait\|></tgt>` | 1574 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to help political </src><tgt><\|wait\|></tgt>` | 1436 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change </src><tgt><\|wait\|></tgt>` | 1315 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>정치적 변화를 돕는 지침으로</tgt>` | 958 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1764 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1864 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 946 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, </src><tgt>미국에서 어떻게 정치적 변화를 돕는 지침이 되는지 살펴보겠습니다. 수정헌법의 의미는</tgt>` | 2458 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>of course I'm </src><tgt><\|wait\|></tgt>` | 1366 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 849 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 974 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1282 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy, </src><tgt>고무줄처럼 늘어나면 화학 결합도 에너지를 저장해요. 그 에너지가</tgt>` | 2296 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1425 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy gets </src><tgt><\|wait\|></tgt>` | 779 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to other </src><tgt><\|wait\|></tgt>` | 1688 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>types of energy, </src><tgt>끊어지면 다른 종류의 에너지로 바뀌게 되는데,</tgt>` | 2046 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 2173 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>or gets used </src><tgt><\|wait\|></tgt>` | 1066 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds </src><tgt><\|wait\|></tgt>` | 1496 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src><\|wait\|></src><tgt>열이나 빛 같은 에너지로 바뀌거나, 다른 결합을 만드는 데 사용되죠.</tgt>` | 1907 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 901 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切都正常，</src><tgt><\|wait\|></tgt>` | 1032 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>我甭乱跳，</src><tgt><\|wait\|></tgt>` | 1293 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt>Everything was normal back then. I shouldn't jump to conclusions,</tgt>` | 1422 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1437 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>起见大概</src><tgt><\|wait\|></tgt>` | 1398 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生来</src><tgt><\|wait\|></tgt>` | 1800 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来审段，</src><tgt>so I stuck to the plan. It was probably twelve years of review,</tgt>` | 1670 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 855 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 1950 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1090 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>当然都很</src><tgt>and I didn't have any problems with the legwork or the leg-raising. Of course, they were all</tgt>` | 2018 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一会一会打开。</src><tgt><\|wait\|></tgt>` | 1235 |

---

### Test Example 29 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunah Teru, </src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1193 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in AI, </src><tgt>제 이름은 츠나 테루입니다. 현재 AI를 공부하고 있습니다.</tgt>` | 2026 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>back-end finance, </src><tgt><\|wait\|></tgt>` | 977 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bit of psychology. </src><tgt><\|wait\|></tgt>` | 1422 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 1719 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>you're into AI, </src><tgt>백엔드 금융과 심리학도 조금 공부하고 있어요. AI에 관심이 많으신 것 같아요.</tgt>` | 2873 |
| 9 | `<src><\|wait\|></src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1540 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 1837 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consulting, </src><tgt><\|wait\|></tgt>` | 668 |
| 12 | `<src>corporate consultancy. </src><tgt>밟고 있고요, 앞으로는 기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src><\|wait\|></src><tgt>미래에는 기업 컨설팅 쪽으로 가고 싶어요.</tgt>` | 1916 |

---

### Test Example 30 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 946 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>there's </src><tgt><\|wait\|></tgt>` | 974 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1254 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such instances before </src><tgt>没有新东西，以前</tgt>` | 1116 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1608 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>net future TC </src><tgt><\|wait\|></tgt>` | 1385 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>there. </src><tgt><\|wait\|></tgt>` | 558 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>So this is just </src><tgt>有这样的情况。所以这只是</tgt>` | 1753 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1698 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>for uket </src><tgt><\|wait\|></tgt>` | 1848 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1039 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src>but </src><tgt>另一个uket，</tgt>` | 1775 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developer or engineer </src><tgt><\|wait\|></tgt>` | 893 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>should be </src><tgt><\|wait\|></tgt>` | 1203 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 1019 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 759 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>前头，</src><tgt><\|wait\|></tgt>` | 975 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1253 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了前头之后</src><tgt>彼は前方に到達しました。もし前方に到達したら、</tgt>` | 1569 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1283 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src>就要先守住</src><tgt><\|wait\|></tgt>` | 1523 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>，不要想</src><tgt><\|wait\|></tgt>` | 1783 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>就按那我在</src><tgt>必ず守り、</tgt>` | 1629 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src>继续操作</src><tgt><\|wait\|></tgt>` | 735 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 1834 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 886 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>私を操作し続けるつもりでいると、なぜそう言うのでしょうか？</tgt>` | 2096 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1547 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1027 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>低张的部分</src><tgt><\|wait\|></tgt>` | 815 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 985 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1197 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>带吊的人，但是</src><tgt>저장된 부분은 끈이 달린 사람입니다. 하지만</tgt>` | 1607 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1385 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src>这通场</src><tgt><\|wait\|></tgt>` | 1428 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>场像是一个</src><tgt><\|wait\|></tgt>` | 1769 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>壮观的show，就要去特别</src><tgt>역방향입니다. 이 장면은 장엄한 쇼와 같습니다. 특별히</tgt>` | 2149 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>注意是</src><tgt><\|wait\|></tgt>` | 1845 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>它能不能</src><tgt><\|wait\|></tgt>` | 928 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到与它</src><tgt><\|wait\|></tgt>` | 1734 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>掉不到与</src><tgt><\|wait\|></tgt>` | 923 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>带的意识</src><tgt>주의할 점은, 그와 함께</tgt>` | 1363 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>的。</src><tgt><\|wait\|></tgt>` | 905 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 778 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개 가 </src><tgt><\|wait\|></tgt>` | 1040 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>중호보서 100만으로 </src><tgt>そのうち150個が中号書100万で</tgt>` | 2094 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업들이 </src><tgt><\|wait\|></tgt>` | 1326 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 813 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>非常に小さな企業が多くありました。一般的には</tgt>` | 1490 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1886 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 </src><tgt><\|wait\|></tgt>` | 1679 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>해화백이 겹겨 </src><tgt>中小企業は成長するか、あるいは</tgt>` | 2495 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>되는데, 예번에 </src><tgt><\|wait\|></tgt>` | 1249 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업 들은 성장 도 </src><tgt><\|wait\|></tgt>` | 1375 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>폐업도 하지 않는 </src><tgt>廃業もしていません。前年度の</tgt>` | 1865 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1277 |

---

### Test Example 34 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 894 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手</src><tgt><\|wait\|></tgt>` | 753 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>とかですか。</src><tgt>因为是二手车之类的，</tgt>` | 1036 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 810 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>10秒で</src><tgt><\|wait\|></tgt>` | 927 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>まあ1秒に</src><tgt><\|wait\|></tgt>` | 1556 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt>大概10秒，</tgt>` | 1544 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>速度なんですかね。</src><tgt><\|wait\|></tgt>` | 1807 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1002 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1121 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>遅く</src><tgt>大概每秒1秒左右的速度吧。</tgt>` | 2364 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src>11</src><tgt><\|wait\|></tgt>` | 1437 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>二で</src><tgt><\|wait\|></tgt>` | 1020 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1484 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>見合う馬とかが</src><tgt>然后，如果速度慢一点，11二，那</tgt>` | 1290 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 980 |

---

### Test Example 35 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 962 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 959 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>to produce something written, </src><tgt><\|wait\|></tgt>` | 1300 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt>あるいは、何か書く必要がある場合、テキストを作成する場合、</tgt>` | 1656 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1142 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1556 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1797 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the word. It's like, oh, </src><tgt>単語のスペルが全くわからないことに気づく。なんていうか、「あ、</tgt>` | 2993 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1412 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1632 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>start with a double p, </src><tgt><\|wait\|></tgt>` | 976 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double l, and I don't know </src><tgt>この単語は「pp」で始まるのか、「ll」で始まるのか、全くわからない。そして</tgt>` | 2595 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>it. </src><tgt><\|wait\|></tgt>` | 1078 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 733 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 966 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src>Hiemel이라고 하는 </src><tgt><\|wait\|></tgt>` | 1353 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터도 </src><tgt>哦，Hiemel</tgt>` | 1195 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있고 </src><tgt><\|wait\|></tgt>` | 1627 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>사람도 </src><tgt><\|wait\|></tgt>` | 1383 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있는 </src><tgt><\|wait\|></tgt>` | 1559 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터의 언어에 </src><tgt>也能理解，</tgt>` | 862 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1532 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법이 맞게 </src><tgt><\|wait\|></tgt>` | 2051 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>우리가 이제 그것들을 </src><tgt><\|wait\|></tgt>` | 937 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>也能理解计算机的语言，语法正确，我们现在需要</tgt>` | 2111 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1601 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>그것들을 작성 하는 프로그램 이 필요 합니다. </src><tgt><\|wait\|></tgt>` | 1170 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 960 |

---

### Test Example 37 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1035 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어차피 보면 </src><tgt><\|wait\|></tgt>` | 906 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1180 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt>反正看，</tgt>` | 1058 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이런 인생 이자 </src><tgt><\|wait\|></tgt>` | 1355 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt><\|wait\|></tgt>` | 862 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt>你就是和20岁一起度过的人生，</tgt>` | 1554 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1629 |
| 9 | `<src><\|wait\|></src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1743 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인감모다는 </src><tgt><\|wait\|></tgt>` | 1625 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금은 자기 스스로 </src><tgt>所以，你就是个弟弟。所以，</tgt>` | 1563 |
| 12 | `<src>자기 스스로 </src><tgt>比起责任感，</tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1716 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1447 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 592 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>你把一些责任留给自己，</tgt>` | 1205 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 </src><tgt><\|wait\|></tgt>` | 936 |

---

### Test Example 38 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 925 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个餐饮可以说是</src><tgt><\|wait\|></tgt>` | 998 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1257 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正餐的部分</src><tgt>食事に関しては、かなり良いと言えますが、正餐の部分は</tgt>` | 1940 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 983 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>以及在西餐方面的</src><tgt><\|wait\|></tgt>` | 1462 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长</src><tgt><\|wait\|></tgt>` | 1766 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>所带来的红利</src><tgt>西食の業績成長による恩恵も</tgt>` | 1921 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>以及收入的提升，</src><tgt><\|wait\|></tgt>` | 1909 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果是在投资领域</src><tgt><\|wait\|></tgt>` | 1053 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1763 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>収入の増加も良いですが、投資分野では今月も良いです。ただ</tgt>` | 1930 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说就</src><tgt><\|wait\|></tgt>` | 754 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了</src><tgt><\|wait\|></tgt>` | 686 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>那么一点点。</src><tgt><\|wait\|></tgt>` | 876 |

---

### Test Example 39 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational </src><tgt><\|wait\|></tgt>` | 957 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>containment. How far </src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1309 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt>교육적 격리. 실제로 얼마나</tgt>` | 1186 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1556 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1400 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 759 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>containment. Did you </src><tgt>교육을 받았나요? 고등학교를 졸업했나요? 그건 한 단계의 격리입니다. </tgt>` | 2329 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>go to college, </src><tgt><\|wait\|></tgt>` | 1079 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and so did you graduate </src><tgt><\|wait\|></tgt>` | 2290 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>that's another level of </src><tgt><\|wait\|></tgt>` | 1420 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>containment. </src><tgt>대학까지 갔나요? 그건 또 다른 단계의 격리입니다.</tgt>` | 1408 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 1564 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 1181 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>지금은 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 1033 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1003 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>黙らせてやれ、</src><tgt><\|wait\|></tgt>` | 1079 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>俺は</src><tgt>그럼 그냥 조용히 해, 나는</tgt>` | 1503 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 833 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>火事を見ている。</src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1212 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt>이미 한계가 다 왔어. 불이 붙은 걸 보고 있는 거야.</tgt>` | 1206 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1327 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不れる不規則。</src><tgt><\|wait\|></tgt>` | 1788 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1758 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1062 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>のブナデイコを</src><tgt>오랜 부나데이코를</tgt>` | 1932 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 1452 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 612 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>すごい快則線を見た</src><tgt><\|wait\|></tgt>` | 1194 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt>하고 있어. 이렇게 엄청난 카이소쿠센을 본 적이 없어.</tgt>` | 1184 |

---

### Test Example 41 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희도 </src><tgt><\|wait\|></tgt>` | 826 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니마는 </src><tgt><\|wait\|></tgt>` | 1017 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1360 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt>あなたたちも知っているでしょう。ここに異邦人として</tgt>` | 1641 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1065 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1534 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그리는 그대로 </src><tgt><\|wait\|></tgt>` | 1824 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>그려야 한다는 일이라 </src><tgt>描けない偶像に描く、その通りに描かなければならないのです。</tgt>` | 2514 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>그러고 </src><tgt><\|wait\|></tgt>` | 1719 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼으로 내가 </src><tgt><\|wait\|></tgt>` | 909 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1594 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리노니 </src><tgt><\|wait\|></tgt>` | 1569 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영으로 </src><tgt>そうすれば、私はあなたたちに、神の霊で</tgt>` | 1286 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 1084 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 629 |

---

### Test Example 42 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1049 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうだけじゃなくて</src><tgt><\|wait\|></tgt>` | 1269 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt>This isn't just a visual development environment,</tgt>` | 1266 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1403 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアル</src><tgt><\|wait\|></tgt>` | 1566 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>の書いてあとそれは</src><tgt>it's a visual Python development environment.</tgt>` | 1010 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードなんそっから生成される</src><tgt><\|wait\|></tgt>` | 1624 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつやそれが実行</src><tgt><\|wait\|></tgt>` | 2170 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>されることで信号処理</src><tgt><\|wait\|></tgt>` | 1171 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>It's also a visual flow graph. And that's Python code that gets generated from it, and when it runs, signal processing is performed.</tgt>` | 2209 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>いうことになっているから</src><tgt><\|wait\|></tgt>` | 955 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 1007 |
| 15 | `<src>はい。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 1021 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 895 |

---

### Test Example 43 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 956 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和关于</src><tgt><\|wait\|></tgt>` | 901 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>针对对手的感情</src><tgt><\|wait\|></tgt>` | 1375 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真实意图的。</src><tgt>伝聞や、相手の感情や真意に関するもの。</tgt>` | 1496 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1334 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1396 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>包括经常会</src><tgt><\|wait\|></tgt>` | 1575 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说，</src><tgt>多くは、人々がそう言うのをよく聞く。</tgt>` | 1093 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>啊。</src><tgt><\|wait\|></tgt>` | 1263 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看。</src><tgt><\|wait\|></tgt>` | 1751 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1093 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>躲黄了。</src><tgt>ね。この人はまた逃げ出した。</tgt>` | 1861 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 935 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 1136 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1022 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt>つまり、彼の目は全てを物語っているということです。</tgt>` | 1110 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是说。</src><tgt><\|wait\|></tgt>` | 978 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1079 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매 니다. </src><tgt><\|wait\|></tgt>` | 1121 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>이 운전 을 </src><tgt><\|wait\|></tgt>` | 1230 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt>进去的时候，我真是太迷茫了。因为</tgt>` | 1656 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1140 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>있으면은 뭐 </src><tgt><\|wait\|></tgt>` | 1448 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북으로 가면 </src><tgt><\|wait\|></tgt>` | 1752 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt>我走的是步行路线，如果去江南的话，那更是无话可说。</tgt>` | 1708 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가면 또 장려 리요. </src><tgt><\|wait\|></tgt>` | 1538 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1155 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>진짜 꽤네요. </src><tgt><\|wait\|></tgt>` | 1155 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>如果出国的话，那更是鼓励。真的挺大的。不如现在</tgt>` | 1743 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 열심히 </src><tgt><\|wait\|></tgt>` | 1470 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>노가요. </src><tgt><\|wait\|></tgt>` | 1045 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 아닌 거 같아요. </src><tgt><\|wait\|></tgt>` | 1100 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>예. </src><tgt>努力一下吧。我觉得不是那个意思。对。</tgt>` | 1080 |

---

### Test Example 45 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1118 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세모라 </src><tgt><\|wait\|></tgt>` | 938 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>빌고야 </src><tgt><\|wait\|></tgt>` | 1299 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 내 소름이 </src><tgt>目を閉じて、セモラを</tgt>` | 1236 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 차리 돋은 </src><tgt><\|wait\|></tgt>` | 1718 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>내 느낌 이온이야. </src><tgt><\|wait\|></tgt>` | 1507 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들어서 </src><tgt><\|wait\|></tgt>` | 1753 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt>もう鳥肌が立って、ゾクゾクしてる。その感覚を揺らして、一緒に遊ぼうっていうんだ。</tgt>` | 2786 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1632 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>오면 물릴 거고 </src><tgt><\|wait\|></tgt>` | 1220 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오면이야 </src><tgt><\|wait\|></tgt>` | 1361 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>너 지켜주고 </src><tgt>鬼神が来たら、怯えるし、神が来たら、守ってくれるんだ。</tgt>` | 2245 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 761 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에. </src><tgt><\|wait\|></tgt>` | 918 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>だから、安心して。目を閉じて。</tgt>` | 1083 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 909 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인상 하는 </src><tgt><\|wait\|></tgt>` | 978 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인다면 </src><tgt><\|wait\|></tgt>` | 1329 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주도 </src><tgt>If the stock index is rising,</tgt>` | 1279 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1617 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1748 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt>these large-cap stocks will also see a sharp rise,</tgt>` | 1873 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1744 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1194 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1849 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt>because these variable-interest stocks move the market first,</tgt>` | 1675 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시총이 </src><tgt><\|wait\|></tgt>` | 868 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 온종목 을 </src><tgt><\|wait\|></tgt>` | 1000 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 같습니다. </src><tgt>we should keep an eye on the variable-interest stocks' market cap.</tgt>` | 1149 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 698 |

---

### Test Example 47 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1091 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 979 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1279 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1075 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and like ten of them </src><tgt>何かを始めようとしている人、例えば</tgt>` | 1832 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1828 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to them. </src><tgt><\|wait\|></tgt>` | 1799 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>本当に重要な10個あります。それについて</tgt>` | 2550 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1386 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1115 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at the end of this video. </src><tgt><\|wait\|></tgt>` | 1728 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It'll cover each one, </src><tgt>1分程度の動画をいくつか作ります。この動画の最後にまとめています。それぞれについて</tgt>` | 1603 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>and a little more </src><tgt><\|wait\|></tgt>` | 753 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, but </src><tgt><\|wait\|></tgt>` | 1069 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>ケソ</src><tgt><\|wait\|></tgt>` | 999 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 이런 경우 들을 </src><tgt><\|wait\|></tgt>` | 1099 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>수도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1359 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt>ケソ、もちろんこういうケースもあります。Aという人と</tgt>` | 1563 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 1089 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>서로 懇意 タン ト へ </src><tgt><\|wait\|></tgt>` | 1677 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Biki コンサルタント へ </src><tgt><\|wait\|></tgt>` | 1863 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>거라고 </src><tgt>懇意タントへBikiコンサルタントという関係で、</tgt>` | 2297 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>A라는 사람이 </src><tgt><\|wait\|></tgt>` | 1824 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1209 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>들었을 때 </src><tgt><\|wait\|></tgt>` | 1411 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt>Aという人が悪性コードを</tgt>` | 1713 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로사이트스 </src><tgt><\|wait\|></tgt>` | 1051 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>CT에서 </src><tgt><\|wait\|></tgt>` | 1039 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>엑스파이까지 </src><tgt><\|wait\|></tgt>` | 547 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까? </src><tgt><\|wait\|></tgt>` | 818 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 868 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>then </src><tgt><\|wait\|></tgt>` | 772 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self defining </src><tgt><\|wait\|></tgt>` | 992 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>what we think the standard is, </src><tgt>活動、そして自分自身で定義する基準、つまり</tgt>` | 1425 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1479 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 974 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1084 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid </src><tgt>完全に正しい。でも現実には、</tgt>` | 2033 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the block </src><tgt><\|wait\|></tgt>` | 1768 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed </src><tgt><\|wait\|></tgt>` | 2376 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>from </src><tgt><\|wait\|></tgt>` | 1175 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>私たちはブロックの新しいメンバーだから、20年前から基準が変わってしまったんだ。</tgt>` | 1761 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1420 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard because </src><tgt><\|wait\|></tgt>` | 1035 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>everything at this point </src><tgt><\|wait\|></tgt>` | 1036 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to our standard. </src><tgt>今のところ、私たちの基準に沿って行動させられているんだ。</tgt>` | 1277 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 742 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>말하는 사람들이 </src><tgt><\|wait\|></tgt>` | 983 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>분석을 해 놓았습니다. </src><tgt>そして、それについて話している人々は分析を済ませていました。</tgt>` | 2054 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 969 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자이의 분석을 보시면 </src><tgt><\|wait\|></tgt>` | 1405 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>손이 가 </src><tgt>このロクジャイの分析を見ると、</tgt>` | 1338 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이요르크트의 </src><tgt><\|wait\|></tgt>` | 1815 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPP 파이프를 </src><tgt><\|wait\|></tgt>` | 1854 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 2153 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮추어서 로포인다. </src><tgt>イヨルクートのFPPパイプを128ビットに下げてローポインダ。</tgt>` | 2097 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 773 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1602 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>Xboxにもない</tgt>` | 1082 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>S2가 </src><tgt><\|wait\|></tgt>` | 1025 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>여기도 없다. </src><tgt><\|wait\|></tgt>` | 897 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 450 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 888 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 889 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 997 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt>另外，您将无法移动媒体对象，</tgt>` | 1298 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1126 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 875 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>either, </src><tgt><\|wait\|></tgt>` | 1346 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into the situation </src><tgt>或者</tgt>` | 1015 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>where you </src><tgt><\|wait\|></tgt>` | 1121 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1937 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 2077 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>to a particular resource </src><tgt>如果您在某个资源上添加了错误的媒体文件，</tgt>` | 1314 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>to impede the load. </src><tgt><\|wait\|></tgt>` | 1460 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>Now, and we can see </src><tgt><\|wait\|></tgt>` | 1684 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>about giving those media files </src><tgt><\|wait\|></tgt>` | 1052 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>loads and then making sure </src><tgt>这会阻碍加载。现在，我们可以看到这些媒体文件加载了，然后确保</tgt>` | 1392 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>to get back up </src><tgt><\|wait\|></tgt>` | 980 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 502 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 795 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the sorts </src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>that are </src><tgt><\|wait\|></tgt>` | 1271 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>not the same, </src><tgt>모든 종류의 그 점들은 다릅니다.</tgt>` | 1309 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but we are </src><tgt><\|wait\|></tgt>` | 1483 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>in the midst of </src><tgt><\|wait\|></tgt>` | 1496 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>love. </src><tgt><\|wait\|></tgt>` | 1554 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>We are also </src><tgt>하지만 우리는 사랑의 한가운데에 있습니다.</tgt>` | 980 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>in the process of </src><tgt><\|wait\|></tgt>` | 1485 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>entering </src><tgt><\|wait\|></tgt>` | 1758 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the world. </src><tgt><\|wait\|></tgt>` | 1057 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>That is love. </src><tgt>우리는 세상으로 들어가는 과정에 있습니다. 그것이 사랑입니다.</tgt>` | 2093 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It is </src><tgt><\|wait\|></tgt>` | 1624 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>the end. That is </src><tgt><\|wait\|></tgt>` | 1115 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>that sort of </src><tgt><\|wait\|></tgt>` | 1048 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>the whole thing. </src><tgt>그것이 전부입니다. 그것이 바로 그 모든 것입니다.</tgt>` | 1257 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt><\|wait\|></tgt>` | 517 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>to evolve. </src><tgt><\|wait\|></tgt>` | 491 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1219 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 992 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1259 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt>最初のセクションで少し間違った道を進んでしまって、</tgt>` | 1530 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1230 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1397 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance versus </src><tgt><\|wait\|></tgt>` | 600 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt>AHRの重要性について</tgt>` | 1527 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 1724 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt><\|wait\|></tgt>` | 1828 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt>バリアントデータベースの変種について、これは私のお気に入りの一つです。</tgt>` | 1685 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1436 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1538 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 821 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>that need to be in these </src><tgt>そのフィールドに同意しない場合、</tgt>` | 1091 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 692 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 1100 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 536 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>これらのデータソースから引き出す必要のあるデータソースは、ありませんよね？</tgt>` | 721 |

---

### Test Example 54 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1107 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 903 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt>有意义的个人权利，</tgt>` | 1166 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1314 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I I I don't I don't </src><tgt><\|wait\|></tgt>` | 1626 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>have the courts want to be </src><tgt>而最高法院最后才加入，不是领导者。我我我并不希望法院</tgt>` | 1639 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 877 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>the vanguard of social change </src><tgt><\|wait\|></tgt>` | 1809 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1839 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days. </src><tgt>成为社会变革的先锋。</tgt>` | 1185 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1785 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1569 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 797 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>that's already </src><tgt>但他们更多地反映的是已经形成的共识。</tgt>` | 1198 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged </src><tgt><\|wait\|></tgt>` | 644 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>so. </src><tgt><\|wait\|></tgt>` | 964 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 398 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 415 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 324 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 365 |

---

### Test Example 55 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 </src><tgt><\|wait\|></tgt>` | 888 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이것들은 </src><tgt><\|wait\|></tgt>` | 969 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>거진 유니트 링과 </src><tgt><\|wait\|></tgt>` | 1597 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거는 거진 </src><tgt>These are basically unit rings,</tgt>` | 955 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산 한 링이 </src><tgt><\|wait\|></tgt>` | 1632 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>거진 굉장히 </src><tgt><\|wait\|></tgt>` | 1347 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1552 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄이다. </src><tgt>and this is basically a unit ring that is very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very` | 11141 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이게 다 </src><tgt><\|wait\|></tgt>` | 1012 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>기대 가 </src><tgt>and that's all the expectation</tgt>` | 541 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>될 정도예요. 이제 </src><tgt><\|wait\|></tgt>` | 472 |
| 12 | `<src>그거 에다가 </src><tgt>you could call them diabetes minerals. And on top of that,</tgt>` | `<src>그거에다가 </src><tgt><\|wait\|></tgt>` | 361 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 370 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 788 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 950 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>is a hungry </src><tgt>ある時、彼はイエスが</tgt>` | 1351 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>and he knows that </src><tgt><\|wait\|></tgt>` | 1079 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1550 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>for he's been in the wilderness </src><tgt>飢えていることを知っている。そして、</tgt>` | 1685 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for a sporty day </src><tgt><\|wait\|></tgt>` | 1796 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>that he's hungry, and so he says to </src><tgt><\|wait\|></tgt>` | 2117 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus, say, </src><tgt>イエスよ、</tgt>` | 2264 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the son of God, </src><tgt><\|wait\|></tgt>` | 1777 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt><\|wait\|></tgt>` | 752 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread, </src><tgt>神の子なら証明してみせなさい。この石をパンに変えなさい、</tgt>` | 2299 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 794 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>how did Jesus deal with that? </src><tgt><\|wait\|></tgt>` | 953 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>That temptation. </src><tgt>イエスはどのようにその誘惑に対処したのか？</tgt>` | 1103 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 486 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 472 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>Jonathan lived by the law alone. </src><tgt>いや、ジョナサンは律法だけで生きていた。</tgt>` | 576 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>一下</src><tgt><\|wait\|></tgt>` | 873 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 1369 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分</src><tgt>그럼 사진을 한번 볼까요? 사진 부분은</tgt>` | 1263 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1508 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>一个是客汀的部分，</src><tgt><\|wait\|></tgt>` | 1497 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客汀一般</src><tgt><\|wait\|></tgt>` | 1726 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt>객티(客汀) 부분이 보입니다. 객티는 보통</tgt>` | 1029 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src>我们再</src><tgt><\|wait\|></tgt>` | 1227 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>收集的地方</src><tgt><\|wait\|></tgt>` | 1799 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，所以呢</src><tgt><\|wait\|></tgt>` | 1087 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src>这是身体的部分</src><tgt>수집하는 곳에 있는 부분입니다. 그래서</tgt>` | 2025 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1658 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>我们需要给</src><tgt><\|wait\|></tgt>` | 1014 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 995 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地</src><tgt>이것은 우리 스스로에게 시간을 충분히 주어야 하는 신체 부분입니다.</tgt>` | 671 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做下来收集</src><tgt><\|wait\|></tgt>` | 757 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可从我们看到</src><tgt><\|wait\|></tgt>` | 552 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是包含五一人的嘛。</src><tgt><\|wait\|></tgt>` | 535 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，所以</src><tgt>수집을 잘 하려면, 여기는 51인분입니다. 자, 그럼</tgt>` | 671 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>是说</src><tgt><\|wait\|></tgt>` | 301 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 829 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 974 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1274 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt>この人々は全く珍しく、よく</tgt>` | 1190 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize </src><tgt><\|wait\|></tgt>` | 1505 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>the world. </src><tgt><\|wait\|></tgt>` | 1403 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 542 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>personality is </src><tgt>世界を完全に変革します。その個性は</tgt>` | 1762 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1776 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1917 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 965 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>矛盾したものです。外向的である一方で、</tgt>` | 2124 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1594 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 1056 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src>And like to </src><tgt><\|wait\|></tgt>` | 1038 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt>無意味な会話を嫌い、</tgt>` | 955 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 417 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 489 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 555 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and they </src><tgt><\|wait\|></tgt>` | 429 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>never shy away </src><tgt>本題に入ります。また、彼らは反対意見を述べたり、</tgt>` | 530 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate </src><tgt><\|wait\|></tgt>` | 314 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 276 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src>in an E&P </src><tgt><\|wait\|></tgt>` | 360 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>standoff or. </src><tgt><\|wait\|></tgt>` | 318 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이전 </src><tgt><\|wait\|></tgt>` | 871 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>성공 을 거부 한 </src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>명분 이 후부 를 </src><tgt><\|wait\|></tgt>` | 1287 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 하면서 </src><tgt>The previous pretext for the previous one was to reject the success of the previous one,</tgt>` | 1935 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후부의 당수를 </src><tgt><\|wait\|></tgt>` | 970 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1332 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색 까지 </src><tgt><\|wait\|></tgt>` | 1784 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제는 </src><tgt>and to advance the position of the previous one, they even made a show of it. But now,</tgt>` | 2169 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2236 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정은을 </src><tgt><\|wait\|></tgt>` | 1045 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제관 순간 </src><tgt><\|wait\|></tgt>` | 1390 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석 은 들은 에 놓고 </src><tgt>Yoon Suk-yeol, the former candidate for the presidency, was in the middle of taking the oath of office for Kim Jong Un,</tgt>` | 2504 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 767 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 869 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독끼를 품은 </src><tgt><\|wait\|></tgt>` | 919 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 468 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt>and was ready to attack the Yoon Suk-yeol candidate,</tgt>` | 613 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 433 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 360 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가 신발 </src><tgt><\|wait\|></tgt>` | 313 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석 성상납금 </src><tgt>and was ready to make a move. The amount of money he received for the election campaign was</tgt>` | 608 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가 </src><tgt><\|wait\|></tgt>` | 332 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 352 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 에 얼마나 </src><tgt><\|wait\|></tgt>` | 247 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재입니까? </src><tgt>a big boon for the Democratic Party?</tgt>` | 330 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 975 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 890 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt>Well, I'd like to make something after a meal now. So,</tgt>` | 1393 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1479 |
| 6 | `<src>も</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ホテルも</src><tgt><\|wait\|></tgt>` | 1208 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる</src><tgt><\|wait\|></tgt>` | 804 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>場所になってる</src><tgt><\|wait\|></tgt>` | 1702 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってる</src><tgt>this hotel is also a place where you can have breakfast,</tgt>` | 2099 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>ので今後ね</src><tgt><\|wait\|></tgt>` | 1967 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここ五五五</src><tgt><\|wait\|></tgt>` | 829 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>このドストンホテル泊まってみたい</src><tgt><\|wait\|></tgt>` | 1897 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なという方はですね</src><tgt>so if you're thinking about staying at this Doston Hotel in the future,</tgt>` | 2015 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 971 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>見てみてまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 956 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 972 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>はい思います。</src><tgt>I think it's a good idea to check it out.</tgt>` | 595 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>このホテルからですね</src><tgt><\|wait\|></tgt>` | 383 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 339 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt><\|wait\|></tgt>` | 408 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 389 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんな </src><tgt>From this hotel, you can walk to Busan Station in just a minute,</tgt>` | 429 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>かかんな</src><tgt><\|wait\|></tgt>` | 321 |
| 24 | `<src>立地のいいねまあ</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>そのね立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 502 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 270 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt>and the location is great. So if you're interested,</tgt>` | 330 |
| 27 | `<src>ご検討なさってみて</src><tgt>If you'd like,</tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 242 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それなら</src><tgt><\|wait\|></tgt>` | 211 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt>please consider it. Then,</tgt>` | 198 |
