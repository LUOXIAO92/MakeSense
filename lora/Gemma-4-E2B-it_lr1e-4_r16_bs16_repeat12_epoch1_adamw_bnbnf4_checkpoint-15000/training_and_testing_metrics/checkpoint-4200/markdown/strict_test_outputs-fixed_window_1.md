# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9318
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4834
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
  - PROCESS_TIME_MS_AVG: 1390.8930
  - PROCESS_TIME_MS_P50: 1415.7900
  - PROCESS_TIME_MS_P95: 2127.2330
  - PROCESS_TIME_MS_MAX: 3021.6740

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 762 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 1024 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1183 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね</src><tgt>孩子才一年级，</tgt>` | 1595 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点でこう</src><tgt><\|wait\|></tgt>` | 1493 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src><\|wait\|></src><tgt>这时候</tgt>` | 1409 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>ミミク角線手を</src><tgt><\|wait\|></tgt>` | 1074 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>就</tgt>` | 1283 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こう退ずしてあげると</src><tgt><\|wait\|></tgt>` | 1558 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>十年経っても</src><tgt>退掉“模仿角线”这个棋步，十年后</tgt>` | 2096 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>退した。</src><tgt><\|wait\|></tgt>` | 1259 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1220 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>在相似点</src><tgt>Why</tgt>` | 853 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这里呢？这个优秀</src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src>也很大，</src><tgt>at the point of similarity? This excellence is also very high,</tgt>` | 1886 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢？我在</src><tgt><\|wait\|></tgt>` | 1553 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>放一个</src><tgt>and then? I put in</tgt>` | 1575 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>喝陶人，</src><tgt><\|wait\|></tgt>` | 1024 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>a drinking pottery man,</tgt>` | 1335 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>这里呢？</src><tgt><\|wait\|></tgt>` | 1521 |
| 10 | `<src>这种核桃</src><tgt>some walnut kernels— this kind of</tgt>` | `<src>这种喝陶人</src><tgt>here? This kind of drinking pottery man</tgt>` | 1967 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>啊。</src><tgt><\|wait\|></tgt>` | 1249 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1047 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气熟是容易的，</src><tgt>気が熟していれば簡単です。</tgt>` | 1399 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1543 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>但是只有一个师傅</src><tgt>でも、師匠が</tgt>` | 1370 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>知道，</src><tgt><\|wait\|></tgt>` | 1157 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>一人しか知らない</tgt>` | 1486 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如何处于中间，</src><tgt><\|wait\|></tgt>` | 1227 |
| 8 | `<src>所以</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、</tgt>` | `<src>所以</src><tgt>中庸の取り方を。だから</tgt>` | 1142 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反</src><tgt><\|wait\|></tgt>` | 1478 |
| 10 | `<src>要成为</src><tgt>シュ・アファンは</tgt>` | `<src><\|wait\|></src><tgt>反省が必要で、</tgt>` | 1908 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师傅。</src><tgt><\|wait\|></tgt>` | 1330 |

---

### Test Example 4 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1121 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是</src><tgt>What parents need to do is</tgt>` | 1210 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1675 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt>use</tgt>` | 1102 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水，</src><tgt><\|wait\|></tgt>` | 1442 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>our deep love to water and fertilize</tgt>` | 1729 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1558 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>培育孩子心里的营养，</src><tgt>to nurture the nourishment in their hearts,</tgt>` | 1063 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1266 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>跟耐心等</src><tgt>and to patiently wait</tgt>` | 2017 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 1436 |

---

### Test Example 5 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1224 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt>Students in the auspicious positions</tgt>` | 1077 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1358 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>were not actually that intelligent.</tgt>` | 1887 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1237 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt>They were randomly selected</tgt>` | 1589 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1644 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>였기 때문 입니다. </src><tgt>students.</tgt>` | 1098 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt>In fact,</tgt>` | 1921 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐 던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1646 |

---

### Test Example 6 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 857 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt>重要な研究を</tgt>` | 1029 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt><\|wait\|></tgt>` | 1124 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>extremely happy people? This is </src><tgt>極度に幸せな人たちについて調べましたか？これは</tgt>` | 2270 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1541 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>先端の研究です。</tgt>` | 1200 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 1668 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt>最も幸せな人々の10%の</tgt>` | 1619 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1006 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, people like </src><tgt>人々を見てみると、</tgt>` | 1959 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 2354 |

---

### Test Example 7 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 896 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I am</tgt>` | 1059 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떨 표할지 고 </src><tgt><\|wait\|></tgt>` | 2009 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>not sure how I'll react,</tgt>` | 1351 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1533 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>포모를 </src><tgt>and I'm</tgt>` | 1198 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>죽인 대로나 </src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>killing off my FOMO,</tgt>` | 1573 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1006 |
| 10 | `<src><\|wait\|></src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>같은 세대 들은 </src><tgt>the same generation as Park Han- sang,</tgt>` | 2108 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>다. </src><tgt><\|wait\|></tgt>` | 2307 |

---

### Test Example 8 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt>So, I'm</tgt>` | 1081 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>용심 이 칼 </src><tgt><\|wait\|></tgt>` | 1582 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>용심 이 </src><tgt>a righteous sword, a righteous sword,</tgt>` | 1663 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어 혹시 용심 이가 </src><tgt><\|wait\|></tgt>` | 1400 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>or rather, a righteous sword—</tgt>` | 1426 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞이는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1670 |
| 8 | `<src>야, </src><tgt>it's a mix of rice noodles and ongsimi. Man,</tgt>` | `<src><\|wait\|></src><tgt>it's getting mixed up. Hey,</tgt>` | 1598 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1160 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>this is seriously killer for a hangover,</tgt>` | `<src>해당 으로 </src><tgt>this is actually</tgt>` | 1799 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 주디 미다 인자. </src><tgt><\|wait\|></tgt>` | 2452 |

---

### Test Example 9 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>砂漠を掃除し終わった後、</tgt>` | 1515 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | 1676 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也虽然</src><tgt>内部の圧力が軽減され、エネルギーも</tgt>` | 1357 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>弱了。</src><tgt><\|wait\|></tgt>` | 1409 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>然后就停留在</src><tgt>弱まります。そして、</tgt>` | 1304 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>一个相对的低能量的运行</src><tgt>比較的低いエネルギーの</tgt>` | 1620 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态，</src><tgt><\|wait\|></tgt>` | 1104 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>稼働状態に留まります。これがいわゆる</tgt>` | 1962 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>意识状态。</src><tgt><\|wait\|></tgt>` | 2309 |

---

### Test Example 10 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 813 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 1010 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1345 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>your body. </src><tgt>进入你的身体。</tgt>` | 1321 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 1548 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么？</tgt>` | 1850 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸闷？</tgt>` | 1691 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | 1518 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>language are you </src><tgt>我问他们，你</tgt>` | 1532 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>using. </src><tgt><\|wait\|></tgt>` | 2287 |

---

### Test Example 11 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>面对这个情况，我们就是</src><tgt>Facing this situation,</tgt>` | 1096 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1490 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的回答主管，</src><tgt>when you run into a problem, you should quickly answer your supervisor.</tgt>` | 2162 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1259 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt>Or let them know about the situation.</tgt>` | 1388 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>怎么都把它扛下来，</src><tgt>Don't try to handle everything yourself.</tgt>` | 1821 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>不理成担，</src><tgt><\|wait\|></tgt>` | 1906 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>整体而言</src><tgt>Overall,</tgt>` | 1251 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是一句就是solution。</src><tgt><\|wait\|></tgt>` | 2098 |

---

### Test Example 12 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 일었지 </src><tgt><\|wait\|></tgt>` | 1085 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>너무 이 저 </src><tgt>これ、</tgt>` | 985 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>해야럴 수 있지만 </src><tgt><\|wait\|></tgt>` | 1607 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>진짜 고사 들도요 </src><tgt>これやるのもいいけど、本当に厄介なものもあるんです。</tgt>` | 2255 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt><\|wait\|></tgt>` | 1342 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>고사 들인데 꾸밀 필요 가 </src><tgt>いや、自分の厄介事だから飾る必要は</tgt>` | 1517 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | 1383 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>ないし、私だけ</tgt>` | 1509 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>고사 를 보일 필요 가 보이 색 우주 가 </src><tgt><\|wait\|></tgt>` | 1968 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>진짜 고사 리는 </src><tgt>厄介事を見せる必要はない。宇宙が本当に厄介事なのは</tgt>` | 1790 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1645 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1209 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1043 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1501 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>就是重复。学会重复。重复练习。</tgt>` | 1874 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1948 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>找到自己擅长的，多做一些。</tgt>` | 1273 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And when you're not good </src><tgt><\|wait\|></tgt>` | 1633 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>at it, </src><tgt>不擅长的时候，</tgt>` | 1603 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 2114 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>请身边的人帮忙，</tgt>` | 1524 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and and tell next time </src><tgt><\|wait\|></tgt>` | 1679 |

---

### Test Example 14 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1072 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这里开始，</tgt>` | 1123 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めたもので、</src><tgt><\|wait\|></tgt>` | 1596 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt>我才开始的。</tgt>` | 1393 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1337 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt>高更、高冈、</tgt>` | 1699 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1455 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt>塞尚、</tgt>` | 907 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1445 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の絵</src><tgt>鲁纳尔等人的画，</tgt>` | 2223 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1395 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>は田舎の中学生でも</src><tgt>连乡下中学生</tgt>` | 1808 |

---

### Test Example 15 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>T- shirts and other items</tgt>` | 1114 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1616 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt>are also available.</tgt>` | 1652 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 1233 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ぜひご参加ください。</src><tgt>Please come join us.</tgt>` | 1496 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1239 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になりまして、</src><tgt>That's all for the contact information.</tgt>` | 1218 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1312 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>よろしくお願いします。</src><tgt>Um, thank you.</tgt>` | 1606 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | 1517 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>もう少しお待ちください。</src><tgt>We have a lunch announcement, so please wait a little longer.</tgt>` | 2393 |

---

### Test Example 16 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 689 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>나를</tgt>` | 1067 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个轨道，</src><tgt><\|wait\|></tgt>` | 1311 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>好让我</src><tgt>내 삶의 궤도로 되돌려줘서</tgt>` | 2005 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>能够好自在他</src><tgt><\|wait\|></tgt>` | 1394 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>下班的时候，</src><tgt>퇴근할 때</tgt>` | 1328 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1453 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>的时候，在做热汤</src><tgt>따뜻한 국 끓이면서</tgt>` | 1164 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的时候，我当时</src><tgt><\|wait\|></tgt>` | 1312 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>被他这样子提醒一个</src><tgt>그가</tgt>` | 2065 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>小小的小小的一个愿望</src><tgt><\|wait\|></tgt>` | 1523 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>哈。</src><tgt>작은 소망 하나를 이렇게 상기시켜 줬거든요.</tgt>` | 1886 |

---

### Test Example 17 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 873 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If a female high school student</tgt>` | 1175 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 2059 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>is paired with someone with a strange appearance,</tgt>` | 1248 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | 1732 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>难道会是</src><tgt>is there a connection between them?</tgt>` | 1081 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1594 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里</src><tgt>Could it be that</tgt>` | 1552 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1362 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>it started that night?</tgt>` | 1588 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 2366 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>连篇，</src><tgt>Yangzi's thoughts were racing,</tgt>` | 1010 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 878 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>그렇습니다. 그래서</tgt>` | 1077 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天気で</src><tgt><\|wait\|></tgt>` | 1188 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>お接待時間は</src><tgt>날씨가 좋을 때</tgt>` | 1539 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたが、</src><tgt><\|wait\|></tgt>` | 1486 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>ええ。</src><tgt>접대 시간을 가질 수 있었는데, 네.</tgt>` | 1498 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 961 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井青氏の仕組み</src><tgt>나가이 아오 씨의</tgt>` | 1760 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1350 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>もう</src><tgt>시스템은</tgt>` | 1619 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt><\|wait\|></tgt>` | 1253 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>摂食時</src><tgt>지금</tgt>` | 2233 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビです。</src><tgt><\|wait\|></tgt>` | 1125 |

---

### Test Example 19 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1328 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>And then, </src><tgt>好的。然后，</tgt>` | 1009 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1586 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | 1500 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1201 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1581 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1007 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际上</tgt>` | 1045 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1514 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>要用这些值。</tgt>` | 1502 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 1501 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>game dot sort array </src><tgt>所以这个game.sort数组</tgt>` | 2401 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1324 |

---

### Test Example 20 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 957 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Finnehatelu, I </src><tgt>제 이름은 Finnehatelu입니다.</tgt>` | 1412 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>am currently studying </src><tgt><\|wait\|></tgt>` | 1539 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src>in IT, </src><tgt>현재 IT를 공부하고 있습니다.</tgt>` | 1419 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>business, finance, </src><tgt><\|wait\|></tgt>` | 1460 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bit of psychology. </src><tgt>비즈니스, 금융, 그리고 심리학도 조금 공부하고 있고요.</tgt>` | 1866 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1442 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at the end, </src><tgt>마지막으로,</tgt>` | 1549 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1459 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go </src><tgt>앞으로</tgt>` | 1540 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>into corporate consultancy </src><tgt><\|wait\|></tgt>` | 2219 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>and. </src><tgt>기업 컨설팅 분야로 가고 싶습니다.</tgt>` | 1358 |

---

### Test Example 21 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 </src><tgt>I'm going to</tgt>` | 1086 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>주겨 달라 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 2038 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>주길 넣어두고 나. </src><tgt>put in another dose of medicine because someone asked for it.</tgt>` | 1975 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 </src><tgt><\|wait\|></tgt>` | 1318 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>주겨 달라 해가지고 내가 </src><tgt>Someone else asked for another dose, so I</tgt>` | 1307 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>안 되나. 내가 </src><tgt><\|wait\|></tgt>` | 1500 |
| 8 | `<src>그 소리 안 듣고 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>그걸이 안 듣고 있는 </src><tgt>said I couldn't. I was</tgt>` | 1910 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주르르르르르르르르르나. </src><tgt><\|wait\|></tgt>` | 2318 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아. </src><tgt>trying to give it to them, but they weren't listening. Ah.</tgt>` | 2503 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1247 |

---

### Test Example 22 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 842 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAアンデスにですね</src><tgt>Um, in the A A Andes,</tgt>` | 1339 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1669 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>映像とかどうかっていうの</src><tgt>how it's used in various situations,</tgt>` | 1590 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに</src><tgt><\|wait\|></tgt>` | 1526 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAAの乱交を</src><tgt>when we look into the A A</tgt>` | 1414 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べることであの</src><tgt><\|wait\|></tgt>` | 1588 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>そのその生生息稼働っていうの</src><tgt>and study its network,</tgt>` | 1823 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>強調する生生息で</src><tgt><\|wait\|></tgt>` | 2020 |
| 10 | `<src>ことを保証する</src><tgt>This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>いうことを保証する</src><tgt>which emphasizes its ecological function,</tgt>` | 1521 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような使い方を</src><tgt><\|wait\|></tgt>` | 1728 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されてます。</src><tgt>and ensures its ecological nature.</tgt>` | 1734 |

---

### Test Example 23 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだん</src><tgt><\|wait\|></tgt>` | 1339 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>ちょっと距離が</src><tgt>嗯，</tgt>` | 993 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じで</src><tgt><\|wait\|></tgt>` | 1604 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>おしゃれルカだけがね</src><tgt>感觉距离在慢慢拉开，</tgt>` | 1751 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | 1303 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>海遊したい方って</src><tgt>只有OshareLuca一个人特别多。想去海游的人</tgt>` | 1827 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい行き来おきて다가</src><tgt><\|wait\|></tgt>` | 1696 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>シー</src><tgt>总是来来回回，</tgt>` | 1562 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ジュレ見て</src><tgt><\|wait\|></tgt>` | 1628 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>とトモンチェニアトボトシャグ</src><tgt>看ジュ雷，然后</tgt>` | 1683 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>結構強いので</src><tgt><\|wait\|></tgt>` | 1948 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので</src><tgt>Tomoncheniatopotoshagu也挺厉害的，所以</tgt>` | 1837 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1181 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src><\|wait\|></src><tgt>이게</tgt>` | 868 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアです。ギアが</src><tgt><\|wait\|></tgt>` | 1126 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>緩むと芯が</src><tgt>기어입니다. 기어가 헐거워지면</tgt>` | 2112 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>上げ上げできなくなって</src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>しまうので、</src><tgt>심이 올라가지 못합니다. 그래서</tgt>` | 1727 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1636 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>ヤクネ紙の</src><tgt>기어 앞에</tgt>` | 1107 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1010 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>付いているっていうこと</src><tgt>야쿠네지 너트가</tgt>` | 2162 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1293 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>붙어 있는 거죠.</tgt>` | 1817 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンブレーキを。</src><tgt><\|wait\|></tgt>` | 1735 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 918 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>늘어난 고무줄처럼,</tgt>` | 1170 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1842 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. And when those </src><tgt>화학 결합도 에너지를 저장합니다. 그리고</tgt>` | 1852 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1441 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 결합이 끊어지면, 그 잠재 에너지가</tgt>` | 1460 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1414 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt>다른 종류의 에너지로 변환됩니다. 예를 들어</tgt>` | 1956 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>heat or light, </src><tgt><\|wait\|></tgt>` | 2043 |
| 10 | `<src><\|wait\|></src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src><\|wait\|></src><tgt>열이나 빛,</tgt>` | 1587 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | 1484 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1799 |

---

### Test Example 26 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt>Vanadium and these things</tgt>` | 1515 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 인슐린과 </src><tgt><\|wait\|></tgt>` | 1778 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 유사 한 </src><tgt>are like insulin,</tgt>` | 1121 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>작용 이긴 </src><tgt><\|wait\|></tgt>` | 1545 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>하나 라든 경우 가 굉장히 </src><tgt>or at least have a very similar effect.</tgt>` | 1515 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt>In cases of diabetes, minerals</tgt>` | 1737 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1412 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt>are even talked about</tgt>` | 1557 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 2287 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt>like that. And then,</tgt>` | 1510 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 679 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1166 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt>19차 수정헌법의</tgt>` | 1216 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>and, </src><tgt><\|wait\|></tgt>` | 1504 |
| 4 | `<src>and to explore its </src><tgt>수정헌법 제19조의 의미를 살펴보고,</tgt>` | `<src>and to explore its </src><tgt>의미와</tgt>` | 1497 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1249 |
| 6 | `<src>to how political </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src><\|wait\|></src><tgt>역사를 살펴볼 때, 이것이</tgt>` | 1799 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change can </src><tgt><\|wait\|></tgt>` | 1668 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>정치적 변화가</tgt>` | 1582 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>happen in the United States, </src><tgt><\|wait\|></tgt>` | 1401 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침이 될 수 있습니다.</tgt>` | 2108 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>the meanings of </src><tgt><\|wait\|></tgt>` | 2038 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, I'm </src><tgt>물론</tgt>` | 1804 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Meiriel. </src><tgt><\|wait\|></tgt>` | 696 |

---

### Test Example 28 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1091 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>呢，</src><tgt>皆さん、</tgt>` | 1009 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1137 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是意味着</src><tgt>このローマのことは、</tgt>` | 1578 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>造成了所以呢，</src><tgt><\|wait\|></tgt>` | 1579 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>つまり、今</tgt>` | 1428 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 958 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>危机啊</src><tgt>直面している危機や</tgt>` | 1484 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风险</src><tgt><\|wait\|></tgt>` | 1400 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是你事业之间就</src><tgt>リスクが、あなたのキャリアが</tgt>` | 1798 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1331 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的一</src><tgt>その中で</tgt>` | 2289 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1336 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>属鸡的朋友呢。</src><tgt>どうなるか、それはまだ先の話です。だから、酉年生まれの方には、</tgt>` | 1429 |

---

### Test Example 29 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src><\|wait\|></src><tgt>二つ目は、</tgt>` | 1066 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>涉及到二classList</src><tgt><\|wait\|></tgt>` | 1472 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src><\|wait\|></src><tgt>二つのクラスリストが</tgt>` | 1501 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一集一线</src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>一集一線で殺し合う大牛たちです。</tgt>` | 2127 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 1393 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做维向</src><tgt>例えば、</tgt>` | 1544 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>运动好事几点，</src><tgt><\|wait\|></tgt>` | 1409 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>「維向運動」の好事几点をする時、</tgt>` | 1837 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维向运动好平分的</src><tgt><\|wait\|></tgt>` | 2438 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>新绑</src><tgt>維向運動の</tgt>` | 1671 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 937 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>我当时一切正常，</src><tgt>Everything was fine with me at the time.</tgt>` | 1443 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1671 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src><\|wait\|></src><tgt>I was lively and energetic,</tgt>` | 1193 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀。</src><tgt><\|wait\|></tgt>` | 1457 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>期间大概有</src><tgt>so I insisted on not having the surgery. During that time,</tgt>` | 1650 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1579 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>十位医生来诊，</src><tgt>about ten doctors came to see me,</tgt>` | 1831 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | 1967 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一下提腿，</src><tgt>they'd tap my leg, then lift it,</tgt>` | 1653 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1568 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>and it was all fine. They were all</tgt>` | 1781 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1265 |

---

### Test Example 31 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you have </src><tgt><\|wait\|></tgt>` | 1131 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt>あるいは、</tgt>` | 896 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1388 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何かを書き出す必要がある場合、テキストを入力する、</tgt>` | 1977 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1548 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt>でも、</tgt>` | 1255 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1612 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. Like, oh, </src><tgt>スペルがどう書けるかさえわからないことに気づく。例えば、「あ、</tgt>` | 1971 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1916 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>spelled with a double </src><tgt>この単語は</tgt>` | 1323 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2041 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam? I don't know </src><tgt>doublep？ダブルl？わからない、</tgt>` | 1905 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>it. </src><tgt><\|wait\|></tgt>` | 1206 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 839 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到了一个甜头，</src><tgt>いい兆しが訪れました。</tgt>` | 1336 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1412 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了甜头之后，</src><tgt>もしいい兆しを得た後、</tgt>` | 1643 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1704 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src><\|wait\|></src><tgt>必ず</tgt>` | 887 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1496 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想着哎，那我再继续</src><tgt>守り抜いてください。そうして</tgt>` | 1198 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1229 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>操作下去哦，</src><tgt>また操作を続けようと考えるのはやめてください。</tgt>` | 2301 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1950 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのか？</tgt>` | 1103 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1664 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>因为呢。</src><tgt>なぜなら……</tgt>` | 1205 |

---

### Test Example 33 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>授業</src><tgt><\|wait\|></tgt>` | 998 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一日二日とか</src><tgt>一天两三天</tgt>` | 879 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>でした。おそらく</src><tgt><\|wait\|></tgt>` | 1102 |
| 4 | `<src>十秒で。</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>十秒で</src><tgt>的课。大概十秒</tgt>` | 1686 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 966 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一日一に</src><tgt>一秒</tgt>` | 1380 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1143 |
| 8 | `<src>計算ですか</src><tgt>一秒一手多一点</tgt>` | `<src>してたんですが、</src><tgt>一天的课，大概一天的课吧，</tgt>` | 1788 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>でも</src><tgt><\|wait\|></tgt>` | 1307 |
| 10 | `<src>でなんか</src><tgt>这样算。然后</tgt>` | `<src>でなんか</src><tgt>但</tgt>` | 608 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1456 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一日二日</src><tgt>大概一天两三天</tgt>` | 1428 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 2212 |
| 14 | `<src>あの</src><tgt>十一二手的时候，</tgt>` | `<src>あの</src><tgt>的课，</tgt>` | 981 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮内馬とかが</src><tgt><\|wait\|></tgt>` | 1295 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>还有宫内马之类的。</tgt>` | 1350 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 943 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>我们看到的是</src><tgt>이 사진의 부분은</tgt>` | 1025 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 1677 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>的人，但是</src><tgt>낚시를 하는 사람을 보여주는데,</tgt>` | 1597 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1856 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src>所以</src><tgt>이건 역방향이에요.</tgt>` | 973 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>汤浅很多，</src><tgt><\|wait\|></tgt>` | 1640 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>这样这个状况的教学</src><tgt>물이 많이 얕아서</tgt>` | 1600 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>去特别注意的是</src><tgt><\|wait\|></tgt>` | 1266 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>它能不能够</src><tgt>이 상황에서 특히 주의할 점은</tgt>` | 1822 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | 2315 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>它钓不到</src><tgt>물고기를 잡을 수 있느냐,</tgt>` | 1205 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>鱼的意识</src><tgt><\|wait\|></tgt>` | 1033 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>喽。</src><tgt>물고기의 의식을 잡을 수 있느냐는 거예요.</tgt>` | 1555 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 856 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>백오십만 개가 중화 벌고 </src><tgt>そのうちの150万個が</tgt>` | 1841 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>일백위만으로 </src><tgt><\|wait\|></tgt>` | 1662 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>中国で製造され、100億で</tgt>` | 1821 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1562 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くの小規模企業ができていました。一般的には、</tgt>` | 1838 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1612 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>혹은 해외 로 </src><tgt>中小企業は成長するか、あるいは海外に</tgt>` | 1345 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>익을 꺾게 되는데 </src><tgt><\|wait\|></tgt>` | 1773 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>일본 에 보기 없기 </src><tgt>進出するケースが多いのですが、日本で</tgt>` | 2475 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>없던 성장 도 </src><tgt><\|wait\|></tgt>` | 1283 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>패 업도 하지 않는 </src><tgt>見られなかった成長も、失敗もしていない</tgt>` | 1092 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들만 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1382 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 740 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt>呃，</tgt>` | 919 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HCL이라고 하는 </src><tgt><\|wait\|></tgt>` | 1087 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피터도 이해 할 수 </src><tgt>计算机也</tgt>` | 1659 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1221 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>있고 사람 도 </src><tgt>能理解HCL，</tgt>` | 1548 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 977 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt>人也能理解的计算机语言，</tgt>` | 1940 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1510 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 뭐 같게 우리 가 이제 </src><tgt>就像语法一样，</tgt>` | 1990 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1428 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>我们得写代码，</tgt>` | 1949 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1725 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>写代码的程序</tgt>` | 1324 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 824 |

---

### Test Example 37 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니와 너희 가 </src><tgt>あなたたちも知っているだろう、</tgt>` | 1456 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 1563 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>異邦人であった時に、</tgt>` | 1352 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1411 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>말 못하 는 우상에게로 </src><tgt>言葉を持たない偶像へと</tgt>` | 1512 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1548 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>引きずられて行ったのだ。</tgt>` | 1627 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1518 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>だから、私は</tgt>` | 1487 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 2324 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>あなたたちに告げる。私は</tgt>` | 1058 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1265 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는. </src><tgt>神の霊によって語る者である。</tgt>` | 1508 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 943 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1238 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>まだ始まったばかりの</tgt>` | 1005 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get. </src><tgt><\|wait\|></tgt>` | 1730 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt>人には、まずやるべきことがあります。</tgt>` | 1548 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>And I have ten of them </src><tgt><\|wait\|></tgt>` | 1703 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src><\|wait\|></src><tgt>そして、</tgt>` | 1024 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>that are really important. </src><tgt><\|wait\|></tgt>` | 1703 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt>そのうち10個、本当に重要なものがあります。</tgt>` | 1652 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | 1420 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src><\|wait\|></src><tgt>これから</tgt>` | 1534 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>I have about one minute videos </src><tgt><\|wait\|></tgt>` | 2416 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>1分程度の動画をいくつか紹介します。この動画の後に</tgt>` | 1309 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1069 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src><\|wait\|></src><tgt>それぞれ解説するものです。</tgt>` | 1375 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>You know, a little more detail, </src><tgt><\|wait\|></tgt>` | 1058 |

---

### Test Example 39 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt>没什么新意。</tgt>` | 1017 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>There were such </src><tgt><\|wait\|></tgt>` | 1576 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>interposes before, </src><tgt>以前也有过这种东西，</tgt>` | 1713 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1463 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>like the Flutter TC, </src><tgt>比如FlutterTC，</tgt>` | 1320 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1662 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>and so this is just </src><tgt>所以这只是</tgt>` | 1600 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1081 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>one another place to look at. </src><tgt>另一个可以看的地方。</tgt>` | 2010 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2301 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>But </src><tgt>但</tgt>` | 638 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1616 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>developers or engineers working on Bug Repositories should be </src><tgt>在Bug仓库上工作的开发者或工程师</tgt>` | 1680 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 922 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1033 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>金運については、今月は</tgt>` | 1433 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 1556 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src><\|wait\|></src><tgt>悪くないですね。でも、</tgt>` | 1305 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>比较正财的部分</src><tgt><\|wait\|></tgt>` | 1572 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>尤其是在事业方面</src><tgt>特に正財面、キャリア面では</tgt>` | 1455 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长的动力</src><tgt><\|wait\|></tgt>` | 1654 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>以及收入的提升</src><tgt>業績の伸びや収入アップの</tgt>` | 1746 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1630 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>如果它的投资理财方面</src><tgt>モチベーションが</tgt>` | 1561 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 2023 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错的，</src><tgt>今月も悪くないんです。投資や資産運用面でも</tgt>` | 1860 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对正财来说，</src><tgt><\|wait\|></tgt>` | 1287 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>いいですが、正財面と比べると少し</tgt>` | 1110 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt><\|wait\|></tgt>` | 484 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1126 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment: </src><tgt>교육 수준:</tgt>` | 1039 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1508 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt>실제로</tgt>` | 1186 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? Did you </src><tgt><\|wait\|></tgt>` | 1631 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>교육은 어느 정도까지 마치셨나요? 고등학교 졸업하셨나요?</tgt>` | 2179 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt><\|wait\|></tgt>` | 1623 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>of attainment. Did you </src><tgt>그건 한 단계의 교육 수준입니다.</tgt>` | 1801 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>go to college? </src><tgt><\|wait\|></tgt>` | 1961 |
| 10 | `<src>and if so, did you graduate? </src><tgt>대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>And if so, did you graduate? </src><tgt>대학까지 가셨나요? 그렇다면 졸업하셨나요?</tgt>` | 2170 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level </src><tgt><\|wait\|></tgt>` | 1202 |
| 12 | `<src>attainment. </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>of attainment. </src><tgt>그건 또 다른 단계의 교육 수준입니다.</tgt>` | 1799 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1412 |
| 14 | `<src>now. I'll see you </src><tgt>그럼 오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>자, 여기까지입니다. 여러분은</tgt>` | 1023 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 297 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1153 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어떻게 보면 </src><tgt>嗯，怎么说呢，</tgt>` | 1133 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 2001 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 또래 </src><tgt>和二十岁的人一起</tgt>` | 1347 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>정성 이자 그래도 </src><tgt><\|wait\|></tgt>` | 1648 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>가족 같은 </src><tgt>一起度过了最美好的时光，也是一种</tgt>` | 1398 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동성이잖아 </src><tgt><\|wait\|></tgt>` | 1536 |
| 8 | `<src>그러니까 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>그러니까 </src><tgt>亲情，就像是家人一样，所以</tgt>` | 1677 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1418 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생 만보다는 </src><tgt>比起再生，</tgt>` | 1497 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 2276 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt>还是多一点</tgt>` | 883 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1281 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 것을 </src><tgt>靠自己</tgt>` | 1163 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | 1001 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt>放下很多东西，希望你也能幸福。</tgt>` | 686 |

---

### Test Example 43 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1119 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手的</src><tgt>相手の</tgt>` | 1068 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>感情或</src><tgt><\|wait\|></tgt>` | 1357 |
| 4 | `<src>真实意图的，</src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src>真实意图的</src><tgt>感情や本心を見抜く</tgt>` | 1840 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1142 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>ことは、多くの場合、</tgt>` | 1543 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1229 |
| 8 | `<src>会听到人们</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>好经常会听到人们这样说：</src><tgt>よく聞かれます。</tgt>` | 1326 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1379 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 1974 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1341 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>说谎了，</src><tgt>この人はまた嘘をついている。</tgt>` | 1989 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1702 |
| 14 | `<src>已经说明了一切。”</src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>その目つきだけで全てを物語っている。</tgt>` | 1414 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 764 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 570 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 836 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>So, this is, well,</tgt>` | 1164 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 1959 |
| 4 | `<src><\|wait\|></src><tgt>This isn't just a visual development environment;</tgt>` | `<src><\|wait\|></src><tgt>not just a visual development environment,</tgt>` | 1221 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1961 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのもフローグラフは</src><tgt>but a visual Python development environment. That's because FlowGraph</tgt>` | 1452 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビザング書いてあと</src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それ自体はPythonコード</src><tgt>writes the visualization, and it's</tgt>` | 1804 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>なんそこから</src><tgt><\|wait\|></tgt>` | 1996 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>generated from Python code, which then</tgt>` | 1823 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1228 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われる</src><tgt>runs and performs signal processing</tgt>` | 1711 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>っていう構造になっているからです。</src><tgt><\|wait\|></tgt>` | 1276 |
| 14 | `<src><\|wait\|></src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src><\|wait\|></src><tgt>in that structure.</tgt>` | 774 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 698 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ</src><tgt>Yes. So,</tgt>` | 895 |

---

### Test Example 45 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 811 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>そして、これについて多くの人が</tgt>` | 1164 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놨습니다. </src><tgt><\|wait\|></tgt>` | 2065 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 로쿠 자의 </src><tgt>分析をしています。ロクジャの</tgt>` | 1417 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>연속 을 보시면 </src><tgt><\|wait\|></tgt>` | 1461 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>連続を見ると、ソニーが</tgt>` | 1131 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>UHD에 </src><tgt><\|wait\|></tgt>` | 1596 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FHD 파이 를 </src><tgt>UHDにFHDパイプを</tgt>` | 1676 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1589 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>낮춘 것을 로프 인다. </src><tgt>128ビットに下げています。</tgt>` | 1808 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 </src><tgt><\|wait\|></tgt>` | 2096 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>시리즈 X에서도 없는 </src><tgt>XboxシリーズXにはない</tgt>` | 1793 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1290 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>SI </src><tgt>インフィニットキャッシュSIが</tgt>` | 803 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 725 |
| 16 | `<src><\|wait\|></src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src><\|wait\|></src><tgt>ここにもありません。</tgt>` | 879 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt>The stock market index is now rising,</tgt>` | 1143 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 2175 |
| 4 | `<src>이런 대형주 도 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src>이런 대형주 도 </src><tgt>so these large- cap stocks</tgt>` | 1302 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1368 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 </src><tgt>are also seeing sharp gains</tgt>` | 1223 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 </src><tgt><\|wait\|></tgt>` | 1582 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 가벼운 </src><tgt>at first,</tgt>` | 1536 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1154 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt>but the smaller stocks</tgt>` | 1876 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 </src><tgt><\|wait\|></tgt>` | 2258 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이기 때문 에 </src><tgt>move the market first,</tgt>` | 640 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1792 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt>so the market cap is always lighter</tgt>` | 1502 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1001 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt>and you should always look at the market cap.</tgt>` | 931 |

---

### Test Example 47 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 간고 </src><tgt><\|wait\|></tgt>` | 1287 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>새 못 알아 </src><tgt>目が見えない</tgt>` | 1056 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1595 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>옛날 서름이 </src><tgt>なら、新しいものを買うしかない。昔の</tgt>` | 1812 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 자식 이 돋은 내 </src><tgt><\|wait\|></tgt>` | 2136 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>기미 오며 </src><tgt>子孫が目につくもの、目につくもの、</tgt>` | 1290 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1490 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>それを揺らして一緒に遊ぼうってことよ。</tgt>` | 1861 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1984 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>너무 밀릴 거고 </src><tgt>気性が引っ張られてしまうし、</tgt>` | 2084 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>시눈이 너무 연 너 </src><tgt><\|wait\|></tgt>` | 999 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>지켜 주라고 </src><tgt>目も引っ張られる。だから、お前を守って、</tgt>` | 2022 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주려 하니까 </src><tgt><\|wait\|></tgt>` | 1337 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>刺そうとしているんだ。だから、気持ちを楽にして、</tgt>` | 1045 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 간다. </src><tgt><\|wait\|></tgt>` | 878 |

---

### Test Example 48 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1089 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう蒸らせてあれ。</src><tgt>그럼 그냥 끓여버려.</tgt>` | 1147 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1485 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>今ひきてる。</src><tgt>난 지금 끓이고 있어.</tgt>` | 1730 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>もう</src><tgt>이제</tgt>` | 1427 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>限界なんか</src><tgt><\|wait\|></tgt>` | 838 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>とうに超えてる</src><tgt>한계는 이미</tgt>` | 1603 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈の気性よ。</src><tgt><\|wait\|></tgt>` | 1726 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>넘었어, 부렬의 기성.</tgt>` | 2255 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1629 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなでいくを</src><tgt>오래전부터</tgt>` | 1413 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってるが、</src><tgt><\|wait\|></tgt>` | 1717 |
| 14 | `<src>俺は</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>俺はこんなにすごい</src><tgt>부나데이쿠를 해왔지만, 난 이렇게 대단한</tgt>` | 1693 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>海賊船を見た</src><tgt><\|wait\|></tgt>` | 931 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>ことがない。</src><tgt>해적선을 본 적이 없어.</tgt>` | 946 |

---

### Test Example 49 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1098 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>だから、もちろん</tgt>` | 878 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1307 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>こういうケースもあります。Aさんと</tgt>` | 1691 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1553 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 컨텐츠예요, </src><tgt>Bさんがコンテンツを共有している場合、</tgt>` | 1887 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 컨텐츠 를 </src><tgt><\|wait\|></tgt>` | 1634 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>해주고 A라는 </src><tgt>Aさんがコンテンツを共有して、</tgt>` | 1596 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 1195 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aさんが悪意のあるコードを</tgt>` | 1917 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 2315 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>B라는 사람 이 </src><tgt>与えたとき、Bさんが</tgt>` | 1336 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스사이트 </src><tgt><\|wait\|></tgt>` | 947 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크리 에러 에서 </src><tgt>クロスサイトクリエールエラーで</tgt>` | 1558 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>계시 파일까지 </src><tgt><\|wait\|></tgt>` | 920 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>感染する可能性があるか。</tgt>` | 955 |

---

### Test Example 50 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1325 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>进入的时候，会非常迷失方向。</tgt>` | 1540 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1331 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt>因为开车过来，</tgt>` | 1374 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1623 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>있건 뭐 </src><tgt>走路、走着走着，</tgt>` | 1355 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1591 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>去江北就不用说了，去外国</tgt>` | `<src>말할 것도 없고요. </src><tgt>要是去江北，那更是不用说了。</tgt>` | 1846 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 장렬이에요. </src><tgt><\|wait\|></tgt>` | 1975 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>좀 </src><tgt>要是出国，那就更惨了。</tgt>` | 1338 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>힘치하네요. </src><tgt><\|wait\|></tgt>` | 2103 |
| 12 | `<src>대신 에 </src><tgt>真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>有点累啊。不如现在</tgt>` | 1730 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1249 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>모르 바요. 그거 는 </src><tgt>努力学习吧。那</tgt>` | 1063 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>내일 있는 것 같아요. </src><tgt><\|wait\|></tgt>` | 587 |
| 16 | `<src><\|wait\|></src><tgt>这一点倒是做得还行。</tgt>` | `<src><\|wait\|></src><tgt>好像是明天的事。</tgt>` | 875 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1022 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1077 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1869 |
| 4 | `<src>the standard is because you're </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is, </src><tgt>自分自身で基準を定義すること。つまり、自分たちが基準だと思っているものを。</tgt>` | 2254 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1501 |
| 6 | `<src>but the reality </src><tgt>完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>その通りです。</tgt>` | 946 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is is that </src><tgt><\|wait\|></tgt>` | 1601 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt>でも現実には、私たちは</tgt>` | 1814 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block, and because this </src><tgt><\|wait\|></tgt>` | 2080 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>standard has </src><tgt>新しい世代だからです。そして、この基準は</tgt>` | 1637 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1419 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt>20年前に変わったんです。</tgt>` | 1779 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1347 |
| 14 | `<src>a higher standard because </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard </src><tgt>だから、私たちはより高い基準を求められていて、</tgt>` | 1016 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point is </src><tgt><\|wait\|></tgt>` | 537 |
| 16 | `<src>held to a higher standard. </src><tgt>今はすべてがより高い基準を求められているからです。</tgt>` | `<src>being held to a higher standard. </src><tgt>今、すべてがより高い基準で評価されているんです。</tgt>` | 1053 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 863 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>Furor一的首知觉</src><tgt>Furor의</tgt>` | 1097 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>觉知到了那个现象，</src><tgt><\|wait\|></tgt>` | 2024 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src><\|wait\|></src><tgt>첫 번째 지각이 그 현상을 감지했습니다.</tgt>` | 1523 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>但在我们处于</src><tgt><\|wait\|></tgt>` | 1356 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src><\|wait\|></src><tgt>하지만 우리가</tgt>` | 1031 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>爱之中所位的爱，</src><tgt><\|wait\|></tgt>` | 1690 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt>사랑 속에 있는 사랑은</tgt>` | 1157 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>我们也同时进入</src><tgt><\|wait\|></tgt>` | 1071 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>동시에</tgt>` | 1988 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨在长上的时候，</src><tgt><\|wait\|></tgt>` | 1546 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>它是不爱。</src><tgt>증오가 생겨날 때, 그것은 사랑이 아닙니다.</tgt>` | 1906 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1644 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>它就变成</src><tgt>밤이 되면</tgt>` | 1270 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>恨，</src><tgt><\|wait\|></tgt>` | 706 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个中百，</src><tgt>증오로 변합니다. 그 중백, 그</tgt>` | 680 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | 848 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src><\|wait\|></src><tgt>중백이 계속 움직입니다.</tgt>` | 578 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1065 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 1015 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to move </src><tgt><\|wait\|></tgt>` | 1643 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src><\|wait\|></src><tgt>你将无法移动</tgt>` | 1382 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1311 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>资源之间的媒体对象。</tgt>` | 1598 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 1238 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into a </src><tgt>所以，如果你进入了</tgt>` | 1192 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation </src><tgt><\|wait\|></tgt>` | 1354 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize </src><tgt>一个情况，意识到</tgt>` | 1563 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | 1573 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>把错误的媒体文件加到了某个资源上，</tgt>` | 2469 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>we'll </src><tgt><\|wait\|></tgt>` | 1712 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>now, and we can see about </src><tgt>我们现在会……</tgt>` | 1502 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 862 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files </src><tgt>看看</tgt>` | 366 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure they get back up </src><tgt><\|wait\|></tgt>` | 917 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>怎么把那些媒体文件移回去，确保它们能正常显示。</tgt>` | 590 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1391 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt>私は</tgt>` | 940 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>on the first section </src><tgt><\|wait\|></tgt>` | 1188 |
| 4 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src><\|wait\|></src><tgt>最初のセクションで少し混乱して</tgt>` | 1708 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1472 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src><\|wait\|></src><tgt>AHRの分野について</tgt>` | 1586 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1416 |
| 8 | `<src>versus variant </src><tgt>決定的な重要性と、</tgt>` | `<src>versus </src><tgt>、それが非常に重要であることと、</tgt>` | 1015 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1473 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt>バリアントデータベースとの対比で、</tgt>` | 2242 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously the one of my loves. </src><tgt><\|wait\|></tgt>` | 1652 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt>それは明らかに私が大好きなものです。つまり、</tgt>` | 1618 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1784 |
| 14 | `<src>upon the fields that need </src><tgt>つまり、</tgt>` | `<src>the fields </src><tgt>フィールドについて合意できていない</tgt>` | 1445 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1034 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>データソースに必要なフィールドが</tgt>` | 908 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from? There's nothing </src><tgt><\|wait\|></tgt>` | 520 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt>どこにあるのか？そこから引き出せるものはない、でしょ？</tgt>` | 497 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 426 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1294 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | 1059 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1263 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>个人权利，最高法院</tgt>` | 1599 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1380 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt>最后才出现，而不是引领。</tgt>` | 1662 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 1857 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt>我不认为法院想成为</tgt>` | 1588 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1087 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>社会变革的先锋。</tgt>` | 1881 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days, </src><tgt><\|wait\|></tgt>` | 1949 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src><\|wait\|></src><tgt>如今，</tgt>` | 853 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | 1653 |
| 14 | `<src>the consensus </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt>它们更多反映的是</tgt>` | 947 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 800 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>that's already emerged. </src><tgt>已经形成的共识。</tgt>` | 1054 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 812 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>you have some </src><tgt>所以，</tgt>` | 356 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges </src><tgt><\|wait\|></tgt>` | 412 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>你有一些联邦法官，</tgt>` | 434 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 458 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1074 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片</src><tgt>그럼 사진을 한번</tgt>` | 1020 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>哦，图片</src><tgt><\|wait\|></tgt>` | 1582 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>的右边呢，</src><tgt>봐요. 사진 오른쪽에는</tgt>` | 1708 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1351 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>一个是客厅的部分，</src><tgt>거실 부분과</tgt>` | 1337 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1443 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>都是属于</src><tgt>거실은 보통</tgt>` | 840 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1395 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>在休息的地方，</src><tgt>쉴 때 쓰는 공간이에요.</tgt>` | 1641 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1332 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分</src><tgt>그래서 이건 몸의</tgt>` | 2297 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>会反映的是</src><tgt><\|wait\|></tgt>` | 1392 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt>부분이라, 여러분이</tgt>` | 774 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间可以</src><tgt><\|wait\|></tgt>` | 1384 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>好好地做</src><tgt>충분히</tgt>` | 788 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>一下洗去，</src><tgt><\|wait\|></tgt>` | 489 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们可以看到这边是</src><tgt>씻을 시간을 가지라는 뜻이에요. 여기는</tgt>` | 1007 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>仿佛一人的嘛，</src><tgt><\|wait\|></tgt>` | 396 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>啊，</src><tgt>혼자 있는 것 같네요. 아,</tgt>` | 423 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以意思是说。</src><tgt><\|wait\|></tgt>` | 447 |

---

### Test Example 57 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 894 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼はイエスを</tgt>` | 1113 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1715 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>He knows that </src><tgt>飢えていると知っています。彼は、</tgt>` | 1467 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1666 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>be in the wilderness </src><tgt>荒野に</tgt>` | 1136 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry. </src><tgt><\|wait\|></tgt>` | 1728 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>And so he says to </src><tgt>40日間飢えながら過ごすことになるのだと知っています。だから彼は</tgt>` | 2121 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus," Hey, if you </src><tgt><\|wait\|></tgt>` | 2216 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>are the Son of God, prove it." </src><tgt>イエスに言いました。「おい、もしお前が神の御子なら、証明してみろよ」と。</tgt>` | 3022 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1665 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えろ」と。</tgt>` | 1545 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 773 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>How did Jesus deal with that? </src><tgt>イエスはどう対処したのでしょうか？</tgt>` | 721 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>The temptation. </src><tgt><\|wait\|></tgt>` | 662 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src><\|wait\|></src><tgt>誘惑。彼は</tgt>` | 520 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan lead by </src><tgt><\|wait\|></tgt>` | 416 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>great alone. </src><tgt>偉大な一人で立ち向かいました。</tgt>` | 513 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 889 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>彼らは全く珍しく、</tgt>` | 1092 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1668 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>and they often show up </src><tgt>よく</tgt>` | 1232 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1327 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するんです。</tgt>` | 1881 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1637 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その個性は</tgt>` | 1532 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1140 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾をはらんでいます。</tgt>` | 1845 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 2195 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的で、</tgt>` | 724 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1659 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations, </src><tgt>無意味な会話も嫌い。</tgt>` | 1428 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 778 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>and like to get straight to the </src><tgt>そして</tgt>` | 544 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 854 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love to </src><tgt>要点をズバッと伝えるのが好きなんです。</tgt>` | 628 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 403 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>play the devil's advocate, </src><tgt>悪魔の代弁もします。</tgt>` | 530 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and they never shy away </src><tgt><\|wait\|></tgt>` | 294 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 397 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 286 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Any VP stands for </src><tgt>VPは</tgt>` | 359 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for. </src><tgt><\|wait\|></tgt>` | 349 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1058 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>강물 을 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1329 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보를 </src><tgt><\|wait\|></tgt>` | 1775 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt>claimed he was rejecting the river for the sake of the candidacy,</tgt>` | 1751 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당슬을 </src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>for the sake of the party's main candidate,</tgt>` | 1160 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1554 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>even putting on quite a show. But now</tgt>` | 1772 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2074 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt>with Yoon Suk- yeol</tgt>` | 1815 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1241 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석은 드러내 놓고 </src><tgt>removing Kim Jong- in, Lee Jun- seok</tgt>` | 2009 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 1396 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt>has openly declared he intends to knock Yoon Suk- yeol out</tgt>` | 1131 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 867 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt>and has shown his aggressive intent</tgt>` | 609 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 406 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>to take down the candidate.</tgt>` | 462 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 326 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt>He is determined to</tgt>` | 272 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상납권 </src><tgt><\|wait\|></tgt>` | 339 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt>make his own sexual favors</tgt>` | 314 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 241 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 </src><tgt>for the Democratic Party</tgt>` | 327 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 375 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1076 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt>Well,</tgt>` | 850 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってるみたいです。なるほど。</src><tgt><\|wait\|></tgt>` | 1330 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>でここのね</src><tgt>it looks like they're making it right now at the cafeteria. I see.</tgt>` | 2348 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ホルモン温泉ホテル</src><tgt><\|wait\|></tgt>` | 1611 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>で朝食が</src><tgt>And the breakfast at the Horumon Onsen Hotel</tgt>` | 1469 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1525 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt>is a place where you can eat breakfast.</tgt>` | 1732 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1758 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ねここ</src><tgt>So, I'm planning to go here later</tgt>` | 1518 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴゴゴドストンホテル</src><tgt><\|wait\|></tgt>` | 2110 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいな</src><tgt>and stay at the Gogo Gogo Dosto Hotel.</tgt>` | 1801 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>っていう方はですね</src><tgt><\|wait\|></tgt>` | 1217 |
| 14 | `<src>検討なさってみて</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>検討なさってみて</src><tgt>If you're thinking about it,</tgt>` | 1049 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 523 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt>I think it might be a good idea. Yeah.</tgt>` | 975 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。ここ</src><tgt><\|wait\|></tgt>` | 469 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>のホテルからですね</src><tgt>From this hotel,</tgt>` | 415 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 458 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>you can walk to Busan Station</tgt>` | 341 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt><\|wait\|></tgt>` | 315 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt>in about an hour or so.</tgt>` | 364 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルでのね</src><tgt><\|wait\|></tgt>` | 378 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>リッチの一ねまあホテル</src><tgt>It's just that level of</tgt>` | 429 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt><\|wait\|></tgt>` | 301 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>a hotel, so if you'd like,</tgt>` | 243 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 205 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それでは</src><tgt>please consider it. Well,</tgt>` | 212 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は。</src><tgt><\|wait\|></tgt>` | 188 |
