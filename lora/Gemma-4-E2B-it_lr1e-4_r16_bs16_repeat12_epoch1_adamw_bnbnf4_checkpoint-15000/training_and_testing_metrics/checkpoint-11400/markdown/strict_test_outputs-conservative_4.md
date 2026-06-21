# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9930
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.9205
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
  - PROCESS_TIME_MS_AVG: 1323.8140
  - PROCESS_TIME_MS_P50: 1282.6350
  - PROCESS_TIME_MS_P95: 2263.7890
  - PROCESS_TIME_MS_MAX: 3119.0620

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 780 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1013 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 936 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1246 |
| 5 | `<src>この時点で</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>この時点で</src><tgt>从一开始，特别是现在才一年级呢。这时候</tgt>` | 1488 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | 1571 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1332 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 499 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | 1648 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>十年経っても</src><tgt>如果剪短一点，收紧一点，十年后</tgt>` | 2092 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 1685 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1073 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1184 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 961 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1184 |
| 5 | `<src>爱浇水、</src><tgt>What parents need to do is this:</tgt>` | `<src>爱浇水、</src><tgt>What parents need to do is water them with our deep love,</tgt>` | 1749 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 1313 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1330 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | 911 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1118 |
| 10 | `<src>并耐心等待孩子</src><tgt>water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for</tgt>` | `<src>并耐心等待孩子</src><tgt>fertilize them with sufficient psychological nourishment, and patiently wait for</tgt>` | 2159 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1670 |

---

### Test Example 3 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 992 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | 1342 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | 1068 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 953 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt>I triggered the APEX,</tgt>` | 1177 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1603 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | 1249 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 493 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1688 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt>and people of the same generation as Park Han- sang, who killed his parents,</tgt>` | 2288 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>있다. </src><tgt><\|wait\|></tgt>` | 1638 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1215 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | 1243 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | 1375 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 716 |
| 5 | `<src><\|wait\|></src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src><\|wait\|></src><tgt>Scoop out a bit of the peanut, the oil is quite high. Then</tgt>` | 1990 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | 1156 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>核桃仁，</src><tgt><\|wait\|></tgt>` | 1415 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1596 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>感觉吧？</src><tgt><\|wait\|></tgt>` | 1735 |
| 10 | `<src>这种核桃</src><tgt>Then, I'll add some walnut kernels— this kind of</tgt>` | `<src>这种核桃</src><tgt>I'll add a bit of walnut too, you know?</tgt>` | 1182 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>儿。</src><tgt><\|wait\|></tgt>` | 1568 |

---

### Test Example 5 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1167 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt><\|wait\|></tgt>` | 1014 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 930 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1393 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>The people in the auspicious location</tgt>` | 1296 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1636 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1384 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>었기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 916 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1110 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 모르 았 던 </src><tgt>actually weren't highly intelligent. They were also randomly selected. They didn't know the facts.</tgt>` | 2395 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | 2057 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 1007 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | 1246 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 982 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | 1969 |
| 5 | `<src>옹심이가 </src><tgt>I'm having the ongsimi and kal- ongsimi—</tgt>` | `<src>옹심이가 </src><tgt>Oh, I like</tgt>` | 559 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1522 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1456 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야, </src><tgt><\|wait\|></tgt>` | 1719 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1728 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover,</tgt>` | `<src>해장으로도 조금 죽입니다, </src><tgt>onion soup noodles, kal 옹심이, and rice noodles mixed together. Wow, this is actually</tgt>` | 1571 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>진짜. </src><tgt><\|wait\|></tgt>` | 1447 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1152 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | 1436 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | 1073 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | 1273 |
| 5 | `<src>然后</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、</tgt>` | `<src>然后</src><tgt>放出が終わると、内部の圧力が下がり、エネルギーも衰えます。そして、</tgt>` | 1526 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | 1040 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1391 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>相对的低能量的运行</src><tgt><\|wait\|></tgt>` | 1765 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态，</src><tgt><\|wait\|></tgt>` | 1755 |
| 10 | `<src>这就是所谓的</src><tgt>比較的低エネルギーの状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>比較的低エネルギーな稼働状態にとどまります。これが、いわゆる</tgt>` | 1491 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | 1357 |

---

### Test Example 8 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1005 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | 1331 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 686 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | 1190 |
| 5 | `<src><\|wait\|></src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>知道，</src><tgt>気性がつかむのは簡単です。しかし、師匠だけが知っているのです。</tgt>` | 2076 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1125 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如何处于中间，</src><tgt><\|wait\|></tgt>` | 1452 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1705 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>虚要反，</src><tgt><\|wait\|></tgt>` | 1865 |
| 10 | `<src>要成为</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src><\|wait\|></src><tgt>どうやってその中間に立つか。だから「虚は反る」と、</tgt>` | 1715 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师父。</src><tgt><\|wait\|></tgt>` | 1127 |

---

### Test Example 9 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1121 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 887 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | 1259 |
| 5 | `<src>This is tip of the stem </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは</tgt>` | `<src>This is tip of the stem </src><tgt>非常に幸せな人たちについて重要な研究を行いました。これが</tgt>` | 2004 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research, looking at </src><tgt><\|wait\|></tgt>` | 1122 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>the 10% </src><tgt><\|wait\|></tgt>` | 1470 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1620 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1745 |
| 10 | `<src>out there, </src><tgt>最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, </src><tgt>「先端の枝」の研究で、最も幸せな人々の10%を対象としています。</tgt>` | 1555 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | 1490 |

---

### Test Example 10 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1079 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 911 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1011 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1205 |
| 5 | `<src>ゴッホ、</src><tgt>大致是从这一带开始的，</tgt>` | `<src>ゴッホ、</src><tgt>大概是从这里开始的，</tgt>` | 1301 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 1243 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 816 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1436 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1711 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt>像高更、高安、塞尚、雷诺瓦</tgt>` | 2121 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 1750 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | 934 |

---

### Test Example 11 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1059 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 802 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1237 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>We have items like T- shirts available, so please feel free to</tgt>` | 1655 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 1524 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1347 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | 917 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1077 |
| 10 | `<src><\|wait\|></src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src><\|wait\|></src><tgt>join us. That's all for the contact information.</tgt>` | 2116 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | 1777 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | 928 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 968 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 907 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 888 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 1182 |
| 5 | `<src>Where does the tension </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>你的身体在做什么呢？进入你的身体里。紧张感</tgt>` | 1705 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1469 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1461 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 1818 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | 1871 |
| 10 | `<src><\|wait\|></src><tgt>开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src><\|wait\|></src><tgt>从哪里开始？是什么感觉？是头痛吗？还是胸闷？我问他们</tgt>` | 2335 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | 634 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1011 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 942 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | 1311 |
| 5 | `<src>Find what you're good at </src><tgt>最后，要重复。学会不断重复。找到你的长处，</tgt>` | `<src>Find what you're good at </src><tgt>最后，就是重复。学会复习，不断重复。找到你擅长的事情，</tgt>` | 2399 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 848 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1377 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | 1799 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | 2079 |
| 10 | `<src><\|wait\|></src><tgt>多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src>And </src><tgt>多做一些。而你不擅长的事情，就请周围的人来帮你。</tgt>` | 2459 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>until next time. </src><tgt><\|wait\|></tgt>` | 1325 |

---

### Test Example 14 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1423 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | 1254 |
| 5 | `<src>多いですね。</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。</tgt>` | `<src>多いですね。</src><tgt>嗯，渐渐地距离会拉开，感觉这样的话，选择“Oshareru”的人确实比较多。</tgt>` | 2334 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | 615 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい</src><tgt><\|wait\|></tgt>` | 1325 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | 1768 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>自分で</src><tgt><\|wait\|></tgt>` | 1722 |
| 10 | `<src>全部ちょっと次の投資</src><tgt>想创业的人自我意识都很强，而且</tgt>` | `<src>全部ちょっと次の投資</src><tgt>想开店的人自我意识很强，</tgt>` | 1202 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | 1718 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので。</src><tgt><\|wait\|></tgt>` | 1301 |

---

### Test Example 15 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 918 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1138 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1283 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 952 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>If there's some kind of connection between a high school girl and someone with a strange appearance,</tgt>` | 2309 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 708 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1388 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | 1814 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1829 |
| 10 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src><\|wait\|></src><tgt>could it have started that night?</tgt>` | 1638 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 1107 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇。</src><tgt><\|wait\|></tgt>` | 1411 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1196 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 901 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1048 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1199 |
| 5 | `<src>the instruction </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>the instruction </src><tgt>好的，这些例子之后，</tgt>` | 1291 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1455 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 608 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1346 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1723 |
| 10 | `<src>these values. So </src><tgt>说明告诉我们要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>说明我们要用这些值。所以</tgt>` | 2029 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1731 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | 945 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1446 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | 1436 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | 963 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1620 |
| 5 | `<src>다른 잔찜에 </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>다른 잔찜에 </src><tgt>They told me to go get another one, so I came to kill them.</tgt>` | 1413 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 915 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | 1448 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1858 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1847 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh?</tgt>` | `<src>있는 줄 알았느냐? 응? </src><tgt>Didn't I ask them to kill them? Did they think I didn't hear that? Huh?</tgt>` | 2722 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | 1711 |

---

### Test Example 18 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 1431 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 771 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1351 |
| 5 | `<src>或是通知对方，</src><tgt>In this situation, when we encounter a problem, we should</tgt>` | `<src>或是通知对方，</src><tgt>When faced with this situation, if we run into a problem, we should quickly report it to our supervisor or notify the other party.</tgt>` | 2603 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1729 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1718 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | 677 |
| 10 | `<src>整体而言，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall,</tgt>` | `<src>整体而言，</src><tgt>We shouldn't think of it as something we have to handle all on our own. Overall,</tgt>` | 2496 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | 1844 |

---

### Test Example 19 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1096 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1010 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1300 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1050 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、</tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt>これ、ちょっと地味なことかもしれないけど、本当に菩薩だよ。いや、</tgt>` | 2368 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | 801 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | 1229 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | 1875 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | 2013 |
| 10 | `<src>지금 나한테 </src><tgt>自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に</tgt>` | `<src>지금 나한테 </src><tgt>自分で菩薩なのに飾る必要はないし、誰かに菩薩に見せる必要もない。宇宙が今、私に</tgt>` | 2593 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | 2045 |

---

### Test Example 20 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1108 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 807 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1154 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | 1241 |
| 5 | `<src><\|wait\|></src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이</tgt>` | `<src><\|wait\|></src><tgt>이게 기어입니다. 기어가 헐거워지면 심이</tgt>` | 1645 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | 1587 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1424 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | 1698 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1729 |
| 10 | `<src>ついているっていうことです</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>ついているっていうことです</src><tgt>위아래로 움직이지 못하게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | 1689 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1224 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 359 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 2100 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 860 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 801 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1172 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src>ありましたね。</src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>ありましたね。</src><tgt>그렇습니다. 거기서 테키라는 시설이 있었죠.</tgt>` | 1577 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1475 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1348 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | 571 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1515 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>は五経、</src><tgt>그리고 나오이 케이요시 씨의 구조는 오경,</tgt>` | 2152 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1691 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | 925 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 2137 |

---

### Test Example 22 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 881 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1758 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 1182 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1080 |
| 5 | `<src>유사 한 작용 이 </src><tgt>Things like vanadium</tgt>` | `<src>유사 한 작용 이 </src><tgt>Vanadium and these things</tgt>` | 887 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1441 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1453 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1737 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1689 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt>act almost like insulin— they're so similar in their action that you could call them</tgt>` | 1389 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1627 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1374 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1415 |

---

### Test Example 23 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 693 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 863 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1127 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | 1231 |
| 5 | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가고 싶어요.</tgt>` | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가서</tgt>` | 1491 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | 1657 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1407 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | 1851 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1865 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그가 퇴근하고 나서 뜨거운 국이나 밥을 해주는 그런 시간을 가질 수 있길 바라요. 정말 그때 슬픔에 잠겨 있을 때, 그런</tgt>` | 2898 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | 1611 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 1098 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 965 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 1437 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 772 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | 1240 |
| 5 | `<src>and when those bonds are broken, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면</tgt>` | `<src>and when those bonds are broken, </src><tgt>늘어난 고무줄처럼 화학 결합도 에너지를 저장합니다. 그리고 그 결합이 끊어지면,</tgt>` | 2767 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1393 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1700 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 485 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 1872 |
| 10 | `<src><\|wait\|></src><tgt>잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src><\|wait\|></src><tgt>그 위치 에너지는 열이나 빛 같은 다른 에너지 형태로 바뀌게 됩니다.</tgt>` | 2454 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | 1491 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1322 |

---

### Test Example 25 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 953 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | 1535 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently </src><tgt><\|wait\|></tgt>` | 874 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1054 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>studying a Bachelor of Finance </src><tgt>제 이름은 케레나스 데티그입니다. 현재</tgt>` | 1887 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | 1124 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1388 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | 1786 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1846 |
| 10 | `<src>and in the future, I want to go into </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>and in the future, I want to go into </src><tgt>ANU에서 금융학 학사 과정과 심리학 학사 과정을 밟고 있습니다. 앞으로는</tgt>` | 2736 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1431 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | 1372 |

---

### Test Example 26 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 839 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | 966 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1040 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1512 |
| 5 | `<src>調べるときに、</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area,</tgt>` | `<src>調べるときに、</src><tgt>In movies, when you're looking into whether a creature is native to an area in various scenes,</tgt>` | 2321 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | 786 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | 1322 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1873 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | 2004 |
| 10 | `<src>ことを保証する</src><tgt>you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>ことを保証する</src><tgt>you can guarantee that it is native to that area by checking the movie's origin.</tgt>` | 2499 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1396 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | 1384 |

---

### Test Example 27 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 985 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1006 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1066 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1053 |
| 5 | `<src>坚持不开刀。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery.</tgt>` | `<src>坚持不开刀。</src><tgt>Everything was normal back then, I was full of energy, so I insisted on not having the surgery.</tgt>` | 2144 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间</src><tgt><\|wait\|></tgt>` | 1110 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | 1445 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | 1698 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | 1838 |
| 10 | `<src>一下提腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>一下提腿，</src><tgt>About ten doctors came to see me during that time. They'd knock on my leg, then lift it,</tgt>` | 2093 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 899 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们</src><tgt><\|wait\|></tgt>` | 1817 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | 892 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 1291 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 913 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 996 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1235 |
| 5 | `<src>you realize that </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>you realize that </src><tgt>あるいは、何かを書き、文章を書く必要があるとき、</tgt>` | 1670 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | 1253 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1433 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 1813 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1858 |
| 10 | `<src>spelled with a double </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>spelled with a double </src><tgt>単語の綴りが全くわからないことに気づくかもしれません。「あ、この単語、</tgt>` | 2071 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 908 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | 2569 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 1164 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1156 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1119 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | 996 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1103 |
| 5 | `<src>所以呢，</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、</tgt>` | `<src>所以呢，</src><tgt>皆さんにお伝えしたいのは、このローマは一日にしてできたものではないということです。ですから、</tgt>` | 2119 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 980 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1416 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | 1728 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1753 |
| 10 | `<src>一夕之间就</src><tgt>今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>一夕之间就</src><tgt>今皆さんが直面している危機やリスクも、一晩で</tgt>` | 1375 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1490 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | 1301 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1532 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | 1185 |

---

### Test Example 30 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1102 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 853 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | 1287 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1176 |
| 5 | `<src>history as a guide </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>제19조 수정안의 의미를 살펴보고, 그것이</tgt>` | 1978 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1128 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1445 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 1828 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1870 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침서로서 그 역사를 탐구해 보겠습니다.</tgt>` | 2674 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 972 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | 1915 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 1195 |

---

### Test Example 31 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | 1207 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>服务</src><tgt><\|wait\|></tgt>` | 981 |
| 5 | `<src>在一级一线</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で</tgt>` | `<src>在一级一线</src><tgt>次は、2次市場を選ぶことです。ええと、</tgt>` | 1589 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | 1549 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | 1479 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1752 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | 2028 |
| 10 | `<src>发现</src><tgt>戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>发现</src><tgt>1次市場で激しく戦っている大口トレーダーたちにサービスを提供することです。例えば、えー、WeChat公式アカウントを10年以上やってると、</tgt>` | 2755 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | 1995 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | 765 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>火了。</src><tgt><\|wait\|></tgt>` | 1178 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 1088 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | 1158 |
| 5 | `<src>它是属于逆向的，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요.</tgt>` | `<src>它是属于逆向的，</src><tgt>이 부분은 낚시를 하고 있는 사람을 보여주는데, 역방향으로 되어 있습니다.</tgt>` | 2541 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 502 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | 1465 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | 1709 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | 1829 |
| 10 | `<src>是它能不能够</src><tgt>그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>是它能不能够</src><tgt>그래서 보통 이런 상황을 마주했을 때는 특별히 주의해야 합니다. 바로</tgt>` | 2053 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | 916 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | 2067 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 637 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | 1405 |

---

### Test Example 33 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 753 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | 853 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1339 |
| 5 | `<src><\|wait\|></src><tgt>HTML是一种</tgt>` | `<src><\|wait\|></src><tgt>嗯，</tgt>` | 1180 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1701 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 378 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1379 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1701 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>맞게 우리 가 이제 </src><tgt>我们</tgt>` | 1878 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1258 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 1430 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | 539 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | 2268 |
| 15 | `<src>필요 합니다. </src><tgt>我们需要按照它的语法来编写代码，而编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要编写代码，因为HTML这种计算机语言的语法是人类也能理解的。而编写这些代码的程序呢，</tgt>` | 1679 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | 1342 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt><\|wait\|></tgt>` | 635 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1259 |
| 5 | `<src>请你务必就要</src><tgt>うまくいったなと思ったらね。その時は必ず利益を</tgt>` | `<src>请你务必就要</src><tgt>いい兆しがつきました。もしいい兆しがついたら、</tgt>` | 1945 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1120 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | 1925 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1910 |
| 10 | `<src>继续操作下去哦。</src><tgt>確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>继续操作下去哦。</src><tgt>まずはしっかり守りましょう。そして、「あ、もっと操作を続けよう」なんて考えないでくださいね。</tgt>` | 2610 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1505 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1287 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1203 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 859 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 887 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | 1668 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | 1204 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1321 |
| 5 | `<src>많았습니다. </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。</tgt>` | `<src>많았습니다. </src><tgt>その中で、従業員数が10人未満の非常に小さな企業が150万件ありました。</tgt>` | 1988 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1812 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | 1965 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | 1285 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は</tgt>` | `<src>일본 의 소기업들은 </src><tgt>一般的に小さな企業は成長するか、あるいは廃業するかのどちらかになります。しかし、日本の小規模企業は</tgt>` | 1803 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | 2419 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | 1202 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 933 |

---

### Test Example 36 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1072 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There were </src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | 1246 |
| 5 | `<src><\|wait\|></src><tgt>没什么新鲜的。以前就有过这样的接口，</tgt>` | `<src><\|wait\|></src><tgt>没什么新意。以前就有这样的接口了，</tgt>` | 1457 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | 1540 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 1390 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>this is just </src><tgt><\|wait\|></tgt>` | 1706 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1428 |
| 10 | `<src>to look at. </src><tgt>比如netfilter和 TC。所以这只是另一个需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>netfilter、TC。对，所以这只是看个地方。</tgt>` | 1064 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1641 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 889 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 2110 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | 674 |
| 15 | `<src>should be aware of that. </src><tgt>但开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>但那些在做BugRepo的开发者或工程师应该知道这一点。</tgt>` | 1942 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1320 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1017 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | 1080 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and I </src><tgt><\|wait\|></tgt>` | 1020 |
| 5 | `<src>and I have ten of them </src><tgt>それは始めたばかりの人が手に入れるべきもので、</tgt>` | `<src>have ten of them </src><tgt>始めたばかりの人には、</tgt>` | 1306 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that I think are </src><tgt><\|wait\|></tgt>` | 1636 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>really important. </src><tgt><\|wait\|></tgt>` | 1347 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 533 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | 1610 |
| 10 | `<src>I have about </src><tgt>私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I have about </src><tgt>本当に大事なこと10個くらいあると思うんです。その中身を話しますね。</tgt>` | 2295 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1793 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | 615 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2096 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | 658 |
| 15 | `<src>in a little more detail, but. </src><tgt>この動画の後に、それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, but. </src><tgt>この動画の後に1分程度の動画をいくつか用意しました。それぞれをもう少し詳しく解説しています。ただ……</tgt>` | 2100 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1139 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | 1026 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | 1098 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | 1106 |
| 5 | `<src>まあ</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>まあ</src><tgt>大概是十一二手吧？十秒内。嗯，</tgt>` | 1569 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1414 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | 1490 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | 1673 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src>でなんか</src><tgt>一秒一手多一点这样算。然后</tgt>` | `<src>でなんか</src><tgt>大概每秒有一点强度的计算吧。然后</tgt>` | 940 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1618 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 740 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | 1949 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 695 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮馬とかが</src><tgt>大概是十一二手，那个，宫马</tgt>` | 1539 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>あるから。</src><tgt><\|wait\|></tgt>` | 656 |

---

### Test Example 39 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1056 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | 844 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1207 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1200 |
| 5 | `<src>함께 한 동생 이자 </src><tgt>怎么说呢，</tgt>` | `<src>함께 한 동생 이자 </src><tgt>嗯，怎么说呢，</tgt>` | 1481 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 1604 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>같은 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1395 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 515 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1519 |
| 10 | `<src>책임감 보다는 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>책임감 보다는 </src><tgt>他也是和我一起走过最20岁的人，也是一个像家人的弟弟。所以，比起责任感，</tgt>` | 2692 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1723 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 391 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1948 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | 738 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt>他反而更要放下一些东西，</tgt>` | 1541 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 846 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 851 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1542 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 969 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1044 |
| 5 | `<src>말 못하 는 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない</tgt>` | `<src>말 못하 는 </src><tgt>あなたたちも知っているだろう。異邦人としていた頃、言葉も話せなかった</tgt>` | 2225 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 715 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1361 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1666 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1954 |
| 10 | `<src>그러므로 내가 </src><tgt>偶像に引かれるままに連れて行かれました。ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>偶像に引きずり込まれたのと同じように、引きずり込まれたのだ。だから、私は</tgt>` | 2064 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 902 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1983 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 800 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 1481 |
| 15 | `<src><\|wait\|></src><tgt>あなたがたに教えます。神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>あなたたちに告げます。神の霊によって語る者は……</tgt>` | 920 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1256 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 967 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | 1477 |
| 5 | `<src>也就是</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり</tgt>` | `<src>也就是</src><tgt>金運についてですが、今月はとても良いと言えます。ただ、その恩恵は主に本業の収入にあります。</tgt>` | 2256 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | 378 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | 1397 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>与收入的</src><tgt><\|wait\|></tgt>` | 1702 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | 1867 |
| 10 | `<src>投资理财方面呢，</src><tgt>仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>投资理财方面呢，</src><tgt>具体的には、仕事での業績向上によるボーナスや収入アップです。投資や資産運用に関しては、</tgt>` | 2728 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1232 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1581 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | 1209 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | 936 |
| 15 | `<src><\|wait\|></src><tgt>悪くはないんですが、本業の収入に比べると少し弱めですね。</tgt>` | `<src><\|wait\|></src><tgt>今月も悪くありません。ただ、本業の収入と比べると少しだけ劣るかもしれません。</tgt>` | 1131 |

---

### Test Example 42 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1200 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 918 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | 1405 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | 1573 |
| 5 | `<src>닭살이 돋든 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり</tgt>` | `<src>닭살이 돋든 </src><tgt>目を閉じて、先生が何か祈る言葉を</tgt>` | 1432 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | 1156 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1438 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1654 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | 1906 |
| 10 | `<src>물릴 거고 </src><tgt>何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>祈るんだ。あなたに背筋が寒くなったり、鳥肌が立ったり、何か感じたりしたら、これを振って一緒に遊ぼうってこと。鬼が来たら噛まれるし、</tgt>` | 2868 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | 1950 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 789 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | 1340 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 859 |
| 15 | `<src>눈 감아. </src><tgt>神様が来たら守ってくれるように突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>神様が来たら守ってくれるってことだから、安心して目を閉じて。</tgt>` | 1029 |

---

### Test Example 43 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1342 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 800 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | 1496 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1165 |
| 5 | `<src>큰 폭의 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src>큰 폭의 </src><tgt>If the stock index is rising,</tgt>` | 802 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1618 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1349 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1651 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 464 |
| 10 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>먼저 </src><tgt>these large- cap stocks will likely see a significant increase. But first,</tgt>` | 2142 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 1825 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | 764 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 2261 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 504 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt>the lighter- weight stocks will lead the market. So you should always keep an eye on the market cap of those lighter- weight stocks.</tgt>` | 2319 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | 839 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1276 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1226 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | 972 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1045 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>So this isn't just a visual development environment; it's a visual Python development environment.</tgt>` | 2432 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | 675 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1415 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | 1765 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>にそこから</src><tgt><\|wait\|></tgt>` | 1848 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>You write a flowchart visually, and then it generates Python code from that,</tgt>` | 1971 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 873 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 1978 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 749 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1319 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt>and that code is executed to perform signal processing. That's how it works. Right.</tgt>` | 1116 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | 833 |

---

### Test Example 45 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 928 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1205 |
| 5 | `<src>今奇跡を見てる。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어.</tgt>` | `<src>今奇跡を見てる。</src><tgt>그럼 그냥 재워버려. 난 지금 기적을 보고 있는 거야.</tgt>` | 2129 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1115 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1417 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1803 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | 2058 |
| 10 | `<src><\|wait\|></src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>이제 한계는 아득히 넘어선 배의 기적이야.</tgt>` | 2292 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 493 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | 2132 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>が、</src><tgt><\|wait\|></tgt>` | 594 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt><\|wait\|></tgt>` | 1466 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>海賊船を見た</src><tgt>오래전부터 배를 만들던 나였는데, 이렇게 대단한 해적선을</tgt>` | 1018 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 803 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1179 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | 1234 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 854 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1126 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>一进去就会晕头转向。不管是开车还是走路，</tgt>` | `<src>하건 걸어 걸어다니 </src><tgt>进去的话会走很多弯路。</tgt>` | 1532 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | 1572 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | 1490 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | 1862 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1832 |
| 10 | `<src>또 장렬이에요. </src><tgt>去江北就不用说了，去外国就更惨了。</tgt>` | `<src>또 장렬이에요. </src><tgt>开车还是走路，在江北那儿更是难上车，出国的话更是惨。</tgt>` | 2053 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | 944 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | 2145 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 514 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | 1435 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>真有点丢人。不过，我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 다인 것 같아요. </src><tgt>有点丢人呢。不如现在努力去问吧。我觉得那都是可以的。</tgt>` | 1141 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 811 |

---

### Test Example 47 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 870 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | 1444 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | 1064 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | 1044 |
| 5 | `<src>분석 을 보시면 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、</tgt>` | `<src>분석 을 보시면 </src><tgt>これについて多くの人が分析を挙げています。ロクジャの分析を見ると、</tgt>` | 1895 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 915 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이러 블리드 PDP 파이프 </src><tgt><\|wait\|></tgt>` | 1511 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1671 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>를 128비트 로 </src><tgt><\|wait\|></tgt>` | 1960 |
| 10 | `<src>것으로 보인다. </src><tgt>ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>낮춘 것을 보여 줍니다. </src><tgt>ソニーがこのBluePDPパイプを128ビットに下げたことがわかります。</tgt>` | 2646 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1573 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | 1231 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1165 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 959 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L3가 여기 도 없다. </src><tgt>XboxSeriesXにはないインフィニットキャッシュL3もありません。</tgt>` | 951 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 498 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | 1123 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | 1430 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 865 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1451 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに</tgt>` | `<src>B라는 사람 이 서로 </src><tgt>ですから、もちろん、このようなケースもあります。AさんとBさんがお互いに</tgt>` | 1690 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | 1057 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1359 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | 1914 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1982 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>コンサルタントで、ペネトレーションテスターで、Aさんが悪意のあるコードを</tgt>` | 2593 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | 1995 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 765 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1223 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | 933 |
| 15 | `<src>EX 파일 까지 </src><tgt>配布したとします。その場合、Bさんは実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>EX 파일 까지 </src><tgt>仕掛けたとして、Bさんが実際にクロスサイトスクリプティングで</tgt>` | 903 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 487 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | 1223 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>的感情或</src><tgt><\|wait\|></tgt>` | 858 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | 1245 |
| 5 | `<src><\|wait\|></src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt>相手の感情や真意を推し量ったり感じ取ったりする、</tgt>` | 1996 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | 1425 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | 1765 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | 1865 |
| 10 | `<src>你们看，</src><tgt>するとき、よく耳にするのが「ほら、</tgt>` | `<src>你们看，</src><tgt>という場合がよくあります。よく耳にするのですが、「ねえ、</tgt>` | 1898 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 860 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | 1488 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1304 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | 1208 |
| 15 | `<src><\|wait\|></src><tgt>また嘘をついている。目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>この人また嘘をついているよ、目が全部話してやっているよ」と言うんです。</tgt>` | 1330 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | 744 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 364 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt><\|wait\|></tgt>` | 926 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1201 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | 1433 |
| 5 | `<src>absolutely correct, </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>absolutely correct, </src><tgt>活動、つまり自分自身で基準を定義することです。なぜなら、あなたが完全に正しい</tgt>` | 1891 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 915 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is is that </src><tgt><\|wait\|></tgt>` | 1375 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 1917 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt><\|wait\|></tgt>` | 1917 |
| 10 | `<src>standards have </src><tgt>しかし現実には、</tgt>` | `<src>standards have </src><tgt>ことでも、現実には、私たちは新しいブロックの新しい子だからです。そして基準が</tgt>` | 2520 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1044 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt><\|wait\|></tgt>` | 1763 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1102 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | 954 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>everything at this point is being </src><tgt>20年前に変わったので、今、より高い基準を求められているのです。なぜなら、今のすべてが</tgt>` | 1209 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | 414 |

---

### Test Example 51 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1177 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1032 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1087 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1041 |
| 5 | `<src>actually go in your education? Did you </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>actually go in your education? Did you </src><tgt>학력. 실제로 학력이 어느 정도 되나요?</tgt>` | 1978 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1147 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | 1941 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>to college, </src><tgt><\|wait\|></tgt>` | 1911 |
| 10 | `<src>and if so, did you graduate? </src><tgt>고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>and if so, did you graduate? </src><tgt>고등학교 졸업은 했나요? 그건 한 단계의 학력입니다. 대학교에 다녔다면 졸업했나요?</tgt>` | 2785 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | 2533 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1065 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | 1018 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | 574 |
| 15 | `<src>online. </src><tgt>그게 또 다른 단계입니다. 그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>그건 또 다른 단계의 학력입니다. 자, 이제 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 1083 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | 1020 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | 1111 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | 898 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>每当我们</src><tgt><\|wait\|></tgt>` | 1038 |
| 5 | `<src><\|wait\|></src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가</tgt>` | `<src><\|wait\|></src><tgt>프로이트는 그 현상을 처음 깨달았습니다. 우리가</tgt>` | 1645 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | 1420 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | 1400 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>我们也</src><tgt><\|wait\|></tgt>` | 1685 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | 633 |
| 10 | `<src><\|wait\|></src><tgt>사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>사랑 속에 있을 때, 소위 말하는 사랑 속에 있을 때, 동시에 증오를 느끼게 된다는 것입니다.</tgt>` | 2260 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | 1872 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | 814 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 2002 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | 1147 |
| 15 | `<src><\|wait\|></src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다.</tgt>` | `<src><\|wait\|></src><tgt>아침에는 사랑이고, 밤이 되면 증오로 변합니다.</tgt>` | 1132 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | 536 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 786 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | 506 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 962 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, </src><tgt><\|wait\|></tgt>` | 861 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | 1207 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1187 |
| 5 | `<src><\|wait\|></src><tgt>另外，你没法</tgt>` | `<src><\|wait\|></src><tgt>嗯，另外，</tgt>` | 1253 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 678 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 1368 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt><\|wait\|></tgt>` | 1653 |
| 10 | `<src>where you realize </src><tgt>在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>where you realize </src><tgt>你将无法在资源之间移动媒体对象。所以，如果你遇到这种情况，发现</tgt>` | 2217 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | 1804 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | 925 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | 2289 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 472 |
| 15 | `<src><\|wait\|></src><tgt>给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法</tgt>` | `<src><\|wait\|></src><tgt>把错误的媒体文件加到了某个资源上，请务必通知我们，我们会</tgt>` | 1990 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | 701 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 679 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 534 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1457 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 904 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1103 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1038 |
| 5 | `<src>about the EHR fields </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの</tgt>` | `<src>about the EHR fields </src><tgt>EHRの項目について説明した最初のセクションで、少し混乱していました。</tgt>` | 2014 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1113 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1404 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus variant </src><tgt><\|wait\|></tgt>` | 1663 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1729 |
| 10 | `<src>databases, </src><tgt>決定的な重要性と、</tgt>` | `<src>databases, </src><tgt>その重要性は、バリアントデータベースと比べて、</tgt>` | 960 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | 2107 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1363 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | 1455 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | 1265 |
| 15 | `<src>to be in these </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、</tgt>` | `<src>to be in these </src><tgt>それが私の大好きな分野の一つであることは明らかです。つまり、</tgt>` | 1219 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 786 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 335 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 611 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 384 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1002 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 854 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1137 |
| 5 | `<src>he's been without food, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに</tgt>` | `<src>he's been without food, </src><tgt>ある時、彼はイエスが飢えているのを知りました。イエスが食べ物がない状態で</tgt>` | 2569 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 739 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | 1573 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>And so he says </src><tgt><\|wait\|></tgt>` | 1584 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | 1934 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it. </src><tgt>40日間荒野にいたことを知っていました。だから彼はイエスに言いました。「おい、もしお前が神の御子なら、証明してみろ」と。</tgt>` | 3016 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2348 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | 879 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1173 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | 566 |
| 15 | `<src>temptation? </src><tgt>この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>そして「この石をパンに変えてみろ」と言いました。イエスはこの誘惑にどう対処したのでしょうか？</tgt>` | 1141 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 483 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | 457 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | 391 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1143 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 995 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1328 |
| 5 | `<src>的一个是客厅</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면</tgt>` | `<src>的一个是客厅</src><tgt>그럼 사진을 한번 볼까요? 사진 부분에서</tgt>` | 1573 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>的部分。</src><tgt><\|wait\|></tgt>` | 1177 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1355 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1616 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 463 |
| 10 | `<src>在休息的地方，</src><tgt>거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>在休息的地方，</src><tgt>거실 부분이 보이네요. 거실은 보통 우리가 쉬는 공간이라서</tgt>` | 2264 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1738 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | 752 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | 2098 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 584 |
| 15 | `<src>一点时间，</src><tgt>그래서 이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>一点时间，</src><tgt>몸의 부분도 마찬가지예요. 그러니까</tgt>` | 1581 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 641 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | 523 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | 699 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | 559 |
| 20 | `<src>啊，</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는 아무도 없네요.</tgt>` | `<src>啊，</src><tgt>잠시 시간을 내서 편안하게 앉아 쉬어야 한다는 뜻이죠. 그런데 여기는 아무도 없는 것 같네요.</tgt>` | 709 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以也是说。</src><tgt><\|wait\|></tgt>` | 272 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1236 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1021 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1269 |
| 5 | `<src>came along </src><tgt>有意义的个人权利，而最高法院</tgt>` | `<src>came along </src><tgt>有意义的个人权利，最高法院</tgt>` | 1416 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | 1631 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1839 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | 1950 |
| 10 | `<src>change </src><tgt>是最后才介入的，不是引领者。我不认为</tgt>` | `<src>change </src><tgt>最后才介入，而不是引领。我不认为法院想成为</tgt>` | 1881 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days, </src><tgt><\|wait\|></tgt>` | 964 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1959 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | 776 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1412 |
| 15 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt>社会变革的最前沿，但它们更多地反映的是</tgt>` | 987 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | 874 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 346 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>So you have some </src><tgt><\|wait\|></tgt>` | 443 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges </src><tgt><\|wait\|></tgt>` | 418 |
| 20 | `<src><\|wait\|></src><tgt>反映已经形成的共识。所以，有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>已经形成的共识。所以，你会有一些联邦法官，</tgt>` | 507 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 335 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 939 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1020 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 891 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1182 |
| 5 | `<src><\|wait\|></src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src><\|wait\|></src><tgt>これらの人々は非常に稀です。そして、彼らはしばしば</tgt>` | 1589 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1542 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1400 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | 1753 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a </src><tgt><\|wait\|></tgt>` | 1728 |
| 10 | `<src>contradiction. </src><tgt>世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>contradiction. </src><tgt>世界の常識を完全に覆すような出来事を引き起こします。彼らの性格は、ある種の矛盾をはらんでいます。</tgt>` | 1657 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1366 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | 1649 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1169 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | 1180 |
| 15 | `<src>and like to </src><tgt>外交的である一方、無意味な会話は嫌います。そして、</tgt>` | `<src>and like to </src><tgt>外向的である一方で、無意味な会話を嫌い、</tgt>` | 1124 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 489 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | 798 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love to </src><tgt><\|wait\|></tgt>` | 538 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>play </src><tgt><\|wait\|></tgt>` | 444 |
| 20 | `<src>the devil's advocate, and they </src><tgt>要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, and they </src><tgt>要点をズバリ言うことを好みます。また、彼らは悪魔の肩を持つことを楽しむこともあります。</tgt>` | 693 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 260 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | 316 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 343 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 344 |
| 25 | `<src>ENTP stands for </src><tgt>議論を避けることはありません。ENTPとは</tgt>` | `<src>ENTP stands for </src><tgt>そして、議論を避けることは決してありません。ENTPとは、</tgt>` | 455 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1303 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1075 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1042 |
| 5 | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1358 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1327 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1499 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1801 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1868 |
| 10 | `<src>김종인 을 </src><tgt>for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>김종인 을 </src><tgt>even went to lengths to seem like he was rejecting his party duties for the sake of the candidate, even going so far as to seem like he was rejecting the candidate's victory. But now, with Yoon Suk- yeol's candidate Kim Jong- in</tgt>` | 3119 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 2358 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | 1133 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>드러내 놓고 윤석열 </src><tgt><\|wait\|></tgt>` | 1003 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>후보 를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 539 |
| 15 | `<src><\|wait\|></src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>독기를 품은 </src><tgt>being removed, Lee Jun- seok</tgt>` | 941 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 523 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 386 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 334 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 261 |
| 20 | `<src><\|wait\|></src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's</tgt>` | `<src>가슴 발 </src><tgt>is showing his aggressive nature— he's determined to expose him and attack Yoon Suk- yeol's candidate with venom.</tgt>` | 616 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상납 건. </src><tgt><\|wait\|></tgt>` | 336 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 228 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 313 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 306 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute— what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt>Lee Jun- seok's alleged child bride scandal. How much of a boost is that for the Democratic Party?</tgt>` | 458 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1013 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | 819 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | 1171 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ゴールドストーンホテル</src><tgt>Well, it looks like they're making it up in the dining hall right now. So,</tgt>` | 2193 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1000 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1741 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1863 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ねここ</src><tgt>Goldstone Hotel is also planned to be a place where you can have breakfast. So</tgt>` | 2033 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | 918 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1952 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | 737 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1290 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>もまあいいんじゃないか</src><tgt>if you're thinking about staying at Goldstone Hotel in the future, you might want to consider it.</tgt>` | 1313 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 767 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | 382 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | 382 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | 412 |
| 20 | `<src><\|wait\|></src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src><\|wait\|></src><tgt>I think it's a good idea. From this hotel,</tgt>` | 474 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | 363 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | 363 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | 348 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | 331 |
| 25 | `<src>ホテルになってますので</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>ホテルになってますので</src><tgt>you can walk to Busan Station in about a minute or so— it's really well- located.</tgt>` | 529 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 245 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 207 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 187 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | 203 |
