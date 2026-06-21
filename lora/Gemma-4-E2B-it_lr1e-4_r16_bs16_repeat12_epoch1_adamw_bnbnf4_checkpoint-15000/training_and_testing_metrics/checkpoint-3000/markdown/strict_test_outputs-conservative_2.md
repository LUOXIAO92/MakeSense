# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9931
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9621
  - SRC_RELEASE_TOTAL: 713
  - SRC_WAIT_ACCURACY: 0.4200
  - SRC_WAIT_TOTAL: 150
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 420
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 0.9708
  - TGT_RELEASE_TOTAL: 137
  - TGT_WAIT_ACCURACY: 0.9967
  - TGT_WAIT_TOTAL: 306
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1315.8810
  - PROCESS_TIME_MS_P50: 1278.3480
  - PROCESS_TIME_MS_P95: 2035.2070
  - PROCESS_TIME_MS_MAX: 12918.0160

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 705 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1033 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>子供がまだ</src><tgt>从一开始，</tgt>` | 1020 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1034 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1199 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>こう密告、</src><tgt>孩子还是小学一年级。那时候</tgt>` | 850 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1412 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう退ずして</src><tgt><\|wait\|></tgt>` | 1613 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>あげると</src><tgt>如果直接剪掉枝条，</tgt>` | 1653 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1273 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 1357 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 956 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气鼠是容易的，</src><tgt><\|wait\|></tgt>` | 1224 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>但是</src><tgt>鼠を追い払うのは簡単ですが、</tgt>` | 1328 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个</src><tgt><\|wait\|></tgt>` | 898 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导，</src><tgt><\|wait\|></tgt>` | 1322 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如喝出由</src><tgt>師匠の指導が一つだけあります。</tgt>` | 1536 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>终间，</src><tgt><\|wait\|></tgt>` | 477 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1704 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt>終間に出るように、反転させる必要があります。</tgt>` | 1866 |
| 10 | `<src>要成为</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 956 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>一个师傅，</src><tgt><\|wait\|></tgt>` | 1287 |

---

### Test Example 3 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 926 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 1035 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt>I have</tgt>` | 864 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1149 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설 어설 용심이가 </src><tgt><\|wait\|></tgt>` | 1337 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 785 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt>a bit of sword intent mixed in. Oh,</tgt>` | 1617 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1868 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1539 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해형으로 </src><tgt><\|wait\|></tgt>` | 1106 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 쥐기 맞는 것 </src><tgt><\|wait\|></tgt>` | 1463 |

---

### Test Example 4 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 901 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src>始めた</src><tgt>大概从这附近开始</tgt>` | 991 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 915 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴホ、</src><tgt><\|wait\|></tgt>` | 812 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src>ゴーギャン、</src><tgt>做起，</tgt>` | 1276 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 418 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 2027 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1664 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1604 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 870 |

---

### Test Example 5 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 823 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Abbot, </src><tgt><\|wait\|></tgt>` | 1114 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축발시키고 </src><tgt>I am Abbot, I'm excommunicating</tgt>` | 1656 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 805 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1294 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>범어록인 </src><tgt><\|wait\|></tgt>` | 1580 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 352 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1909 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1649 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt><\|wait\|></tgt>` | 1436 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>이다. </src><tgt>the same generation as my own, the same generation as the patriarch Herona Park.</tgt>` | 1352 |

---

### Test Example 6 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 829 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 1013 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt>重要な研究を</tgt>` | 1015 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>extremely happy people. This is </src><tgt><\|wait\|></tgt>` | 1088 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1199 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking at </src><tgt>行いました。極度に幸せな人たちに関するものです。これは研究の最先端です。</tgt>` | 1761 |
| 7 | `<src>looking at the ten percent </src><tgt>これは最先端の研究です。</tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 639 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1862 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt>最も幸せな人々の10%を</tgt>` | 1909 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, people that </src><tgt><\|wait\|></tgt>` | 1663 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1120 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 981 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后呢，</src><tgt><\|wait\|></tgt>` | 1147 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>内部的冶力减轻，</src><tgt>淘洗が終わると、内部の冶力は弱まります。</tgt>` | 1947 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了。</src><tgt><\|wait\|></tgt>` | 1257 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 704 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>就停留在</src><tgt>エネルギーも衰えます。そして、</tgt>` | 1560 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1668 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 1363 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>运行状态，</src><tgt>比較的低エネルギーな稼働状態に留まります。</tgt>` | 1686 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1167 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>蚁居状态。</src><tgt><\|wait\|></tgt>` | 1626 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1126 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt><\|wait\|></tgt>` | 1093 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt>The people in the auspicious spots</tgt>` | 1172 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1226 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt>actually weren't that intelligent,</tgt>` | 1722 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1548 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt><\|wait\|></tgt>` | 1549 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>and they were just randomly selected.</tgt>` | 1483 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1364 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교수 아들은 </src><tgt><\|wait\|></tgt>` | 1649 |

---

### Test Example 9 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1147 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>怪在嵩子寺附近，</src><tgt><\|wait\|></tgt>` | 1141 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>这个游行也很大，</src><tgt>It's near Songzi Temple, and the procession is huge.</tgt>` | 1928 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1266 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 753 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt>So, I'm on vacation</tgt>` | 1553 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶渊，</src><tgt><\|wait\|></tgt>` | 1645 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1320 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在礼器，</src><tgt>and I'm reading Tao Yuanming in the library.</tgt>` | 1873 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 1169 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和陶渊。</src><tgt><\|wait\|></tgt>` | 1646 |

---

### Test Example 10 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1090 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1165 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src><\|wait\|></src><tgt>What parents need to do is</tgt>` | 1194 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱</src><tgt><\|wait\|></tgt>` | 1247 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>浇水，</src><tgt><\|wait\|></tgt>` | 1250 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>water it with our deep love and fertilize it</tgt>` | 1730 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1831 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>培育孩子心灵营养，</src><tgt><\|wait\|></tgt>` | 1547 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src><\|wait\|></src><tgt>to nurture their spiritual nourishment.</tgt>` | 1365 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>冷心等他</src><tgt><\|wait\|></tgt>` | 1374 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1632 |

---

### Test Example 11 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1087 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 906 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただこうもらう</src><tgt><\|wait\|></tgt>` | 980 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt>We also have items like T- shirts available for you to take home.</tgt>` | 1565 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 1313 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 1201 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 614 |
| 8 | `<src>以上になりまして、</src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>So please come join us. For contact information,</tgt>` | 2147 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1739 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>連絡の</src><tgt><\|wait\|></tgt>` | 1567 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>案内があります</src><tgt>we have contact details</tgt>` | 709 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ので、そちらも</src><tgt><\|wait\|></tgt>` | 1772 |

---

### Test Example 12 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1113 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1125 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>is repeat. </src><tgt>最后，重复一下。</tgt>` | 1138 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | 1297 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1392 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>学会重复。学会洗涤和重复。找到你擅长的，多做一些。</tgt>` | 1823 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And what you're not good </src><tgt><\|wait\|></tgt>` | 2159 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>at, get to people </src><tgt><\|wait\|></tgt>` | 1624 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>around you to help you with </src><tgt>你不太擅长的，找身边的人</tgt>` | 1847 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1589 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and and tell them next time </src><tgt><\|wait\|></tgt>` | 1608 |

---

### Test Example 13 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 712 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 1071 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>Drop into your body </src><tgt>你的身体在做什么？进入你的身体，</tgt>` | 1552 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>where does it </src><tgt><\|wait\|></tgt>` | 864 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>intension </src><tgt><\|wait\|></tgt>` | 1299 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>它从哪里开始？它是什么？</tgt>` | 1766 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 2026 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tension in your chest? </src><tgt><\|wait\|></tgt>` | 1945 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>Or is it a </src><tgt>是头部的紧张吗？是胸部的紧张吗？还是</tgt>` | 1927 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>lower pitch </src><tgt><\|wait\|></tgt>` | 1618 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>you are using? </src><tgt><\|wait\|></tgt>` | 1513 |

---

### Test Example 14 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 905 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 를 </src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주게 달래 자가 주고 내가 </src><tgt>I'll give you another feast, I'll give you a feast,</tgt>` | 2021 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이려고 들어왔으러서다. </src><tgt><\|wait\|></tgt>` | 1528 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 </src><tgt><\|wait\|></tgt>` | 463 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>미 죽여 달래 자 </src><tgt>I came to kill you.</tgt>` | 1485 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>안 되나? 내가 </src><tgt><\|wait\|></tgt>` | 1976 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1912 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>주자 는이야. </src><tgt>Can't you just let me kill you? You're not even listening to me, you know.</tgt>` | 2282 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1640 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1369 |

---

### Test Example 15 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个</src><tgt><\|wait\|></tgt>` | 851 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>情况，我们就是</src><tgt><\|wait\|></tgt>` | 1124 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>遇到问题，</src><tgt>When faced with this situation, we just encounter a problem,</tgt>` | 1754 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 892 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1081 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>我们笑了这个状况，</src><tgt>so we quickly report it to our supervisor or notify the other party about the situation.</tgt>` | 1911 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1944 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1834 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>不离心担当。</src><tgt>Don't think you have to handle everything on your own; don't be heartless in your responsibility.</tgt>` | 2334 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | 1622 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业属顺。</src><tgt><\|wait\|></tgt>` | 1622 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1158 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 1091 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>好的。然后，这些例子之后，</tgt>` | 1367 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1034 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1332 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1712 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1529 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1443 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>实际上</tgt>` | 1223 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 1454 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 961 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>game.record array. </src><tgt>要用这些值。所以这个game.record数组。</tgt>` | 2075 |
| 13 | `<src><\|wait\|></src><tgt>这个game.scored数组。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1012 |

---

### Test Example 17 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1090 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 865 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアが</src><tgt>이게 기어입니다. 기어가</tgt>` | 1106 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>遊ぶと、</src><tgt><\|wait\|></tgt>` | 1102 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>シンガアギアが</src><tgt><\|wait\|></tgt>` | 1329 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>돌면 싱가아 기어가 안 맞게 되니까,</tgt>` | 1602 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 643 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1807 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>ヤクネジのナットが</src><tgt>기어 앞에 야쿠네지 너트가</tgt>` | 2220 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 1566 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 906 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>달려 있는 거죠.</tgt>` | 1452 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンブレーキを</src><tgt><\|wait\|></tgt>` | 1689 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 777 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1152 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt>If a female high school student</tgt>` | 1592 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间有着某种</src><tgt><\|wait\|></tgt>` | 805 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>联系，</src><tgt><\|wait\|></tgt>` | 1266 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>has some kind of connection with someone who looks strange,</tgt>` | 1739 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天涯里开始的</src><tgt><\|wait\|></tgt>` | 1672 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>？</src><tgt>could it start from the edge of the world?</tgt>` | 1522 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1269 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 1696 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇。</src><tgt>Yangzi's thoughts were running on.</tgt>` | 1837 |

---

### Test Example 19 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 918 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Shiranami Tsuruta. </src><tgt><\|wait\|></tgt>` | 1196 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>I am currently studying </src><tgt>제 이름은 시라나미 츠루타입니다. 현재</tgt>` | 1849 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1210 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>a business and finance </src><tgt><\|wait\|></tgt>` | 760 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of science </src><tgt>경영 및 금융학 학사 학위를</tgt>` | 1669 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1781 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at Yaenju, </src><tgt><\|wait\|></tgt>` | 1655 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt>야엔주에서 공부하고 있습니다.</tgt>` | 1511 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 1147 |
| 11 | `<src><\|wait\|></src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1638 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt>앞으로는 기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1961 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 828 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>chemical bonds </src><tgt>고무줄처럼,</tgt>` | 1121 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>also store energy. And when those </src><tgt><\|wait\|></tgt>` | 1305 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1326 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면,</tgt>` | 1896 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted </src><tgt><\|wait\|></tgt>` | 1757 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>to other types of energy, </src><tgt><\|wait\|></tgt>` | 1753 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>그 위치 에너지는 열이나 빛 같은 다른 에너지로 변환됩니다.</tgt>` | 2035 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 1666 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 976 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1476 |

---

### Test Example 21 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>またまたちょっと</src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1110 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>みたいな感じで</src><tgt>又又有点像距离在拉开</tgt>` | 1256 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 1098 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>あるこうだてがねポイですね。</src><tgt><\|wait\|></tgt>` | 1508 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>海遊したい方って</src><tgt>的那种，大将会放掉的。想海游的话，</tgt>` | 1811 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐポイ行き越し行き違い</src><tgt><\|wait\|></tgt>` | 2164 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>し、</src><tgt><\|wait\|></tgt>` | 1519 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>行き違いで</src><tgt>马上就放掉，</tgt>` | 1716 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>またトモンツに</src><tgt><\|wait\|></tgt>` | 1040 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>登ってシャグが強いので</src><tgt><\|wait\|></tgt>` | 1445 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので</src><tgt>因为会因为错开而又登到トモンツ，而且シャグ很强，所以</tgt>` | 2188 |

---

### Test Example 22 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 827 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是问子二</src><tgt><\|wait\|></tgt>` | 1125 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>次师，</src><tgt>次は子二次師です。</tgt>` | 1186 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>还服务</src><tgt><\|wait\|></tgt>` | 1156 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1326 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>そして、一級一线で戦う大牛たちを支援しています。</tgt>` | 1481 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 541 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做维向</src><tgt><\|wait\|></tgt>` | 2049 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>运动好事几点，你会</src><tgt>例えば、維向運動の好事几点、</tgt>` | 2233 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>发现</src><tgt><\|wait\|></tgt>` | 1247 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维向运动</src><tgt><\|wait\|></tgt>` | 1677 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>平分的星棒，</src><tgt>維向運動の星棒を均等に分ける</tgt>` | 1724 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1144 |

---

### Test Example 23 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1118 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 1173 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment, </src><tgt>19차 수정안의 의미는</tgt>` | 1388 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 966 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1316 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to how political </src><tgt>어떻게</tgt>` | 1475 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 468 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt><\|wait\|></tgt>` | 2049 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>United States. </src><tgt>미국에서 정치적 변화가 일어날 수 있는지 살펴보는 것입니다.</tgt>` | 2257 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1392 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1574 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>물론</tgt>` | 1541 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Miriam. </src><tgt><\|wait\|></tgt>` | 1285 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 799 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAアンデスに</src><tgt><\|wait\|></tgt>` | 1125 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>それならば</src><tgt>If it's AA Andes,</tgt>` | 1166 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>メインで生生刻刀かっていうのも</src><tgt><\|wait\|></tgt>` | 1388 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに</src><tgt><\|wait\|></tgt>` | 1229 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAAの乱交を</src><tgt><\|wait\|></tgt>` | 1656 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1521 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生生刻刀かっていうのも</src><tgt><\|wait\|></tgt>` | 1628 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>調書する生生で</src><tgt><\|wait\|></tgt>` | 1438 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt><\|wait\|></tgt>` | 1424 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1582 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>されています。</src><tgt>they've been using it to check the AA Andes main engraving tools. They've been using it to verify that they are indeed the main engraving tools.</tgt>` | 2761 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 702 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt><\|wait\|></tgt>` | 1089 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活的一个</src><tgt>제 삶의</tgt>` | 1127 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt><\|wait\|></tgt>` | 1208 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1331 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>好自在的时候，</src><tgt>궤도로 돌아가게 해 주세요. 편안하게 지낼 수 있는 시간을</tgt>` | 1932 |
| 7 | `<src>在做热汤</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1913 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热饭一样的吃，</src><tgt><\|wait\|></tgt>` | 1830 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么</src><tgt>주식처럼 편안하게 즐기게 해 주세요. 그러면</tgt>` | 1835 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>我暂时被动交易的</src><tgt><\|wait\|></tgt>` | 1701 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>这个小小的一个小小的愿望哈，</src><tgt><\|wait\|></tgt>` | 1604 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>제가 잠시 수동 거래를 하는 이 작은 소망이</tgt>` | 1391 |

---

### Test Example 26 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 838 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt><\|wait\|></tgt>` | 1278 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>거진 인슐린과 </src><tgt>Vanadium and these things are</tgt>` | 1470 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 793 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1394 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 굉장히 </src><tgt><\|wait\|></tgt>` | 1594 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1597 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1366 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1402 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt>so similar to insulin that they cause very similar actions. That's why they're called diabetes minerals. Now,</tgt>` | 2873 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 924 |
| 13 | `<src>아연. </src><tgt>And on top of that, there's zinc.</tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 771 |

---

### Test Example 27 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうですよ。</src><tgt><\|wait\|></tgt>` | 864 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 1038 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src>テイク、</src><tgt>맞아요. 거기서 텍을</tgt>` | 1225 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>今日7億8000万</src><tgt><\|wait\|></tgt>` | 1377 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたがね。</src><tgt><\|wait\|></tgt>` | 1221 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>で、</src><tgt>7억 8천만 있었는데,</tgt>` | 1696 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1563 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井英雄氏の仕組み</src><tgt><\|wait\|></tgt>` | 1684 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>나가이 히데오 씨의 시스템은</tgt>` | 1508 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>冒険、</src><tgt><\|wait\|></tgt>` | 1292 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1683 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>7億8000万</src><tgt>모험, 7억 8천만</tgt>` | 2024 |
| 13 | `<src>です。</src><tgt>어근, 접미사, 어미로 이루어져 있습니다.</tgt>` | `<src>ゴビです。</src><tgt><\|wait\|></tgt>` | 799 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 921 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>我当时已很正常，</src><tgt><\|wait\|></tgt>` | 1199 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>活蹦乱跳，</src><tgt>I was perfectly normal back then— lively and full of energy.</tgt>` | 1887 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1158 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>可以坚持不开档，</src><tgt><\|wait\|></tgt>` | 727 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>期间大概</src><tgt>So I could keep it off, and for about</tgt>` | 1651 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十万医生</src><tgt><\|wait\|></tgt>` | 1771 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | 1524 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>以下挑腿</src><tgt>ten doctors came to diagnose me. I had to</tgt>` | 1976 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 831 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1569 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>pick and lift my legs— no problem at all. They were all</tgt>` | 2079 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 788 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 950 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>あるいは、何かを書き出す必要がある場合、</tgt>` | 1308 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1128 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1323 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know </src><tgt>テキストを書くとき、</tgt>` | 1685 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1530 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like, oh, is </src><tgt><\|wait\|></tgt>` | 1796 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>this word </src><tgt>スペルが全くわからないことに気づくかもしれません。「あ、この単語は</tgt>` | 2212 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 788 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1698 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double l, I don't know </src><tgt>pが二つ、lが二つで書かれてるんだ」って</tgt>` | 2385 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>it. </src><tgt><\|wait\|></tgt>` | 1125 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 791 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>最长的部分呢？</src><tgt><\|wait\|></tgt>` | 1143 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src>我们看到的是一个</src><tgt>가장 긴 부분은요? 우리가 보는 건</tgt>` | 1813 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>戴雪的人，但是他是</src><tgt><\|wait\|></tgt>` | 1019 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的，</src><tgt><\|wait\|></tgt>` | 959 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src>所以</src><tgt>눈을 찌푸린 사람인데, 그 사람은 역방향이에요. 그래서</tgt>` | 1783 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通场我们像</src><tgt><\|wait\|></tgt>` | 1970 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>这样一个状况，</src><tgt><\|wait\|></tgt>` | 1654 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>需要去特别注意的是</src><tgt>통장 상황에서 특별히 주의해야 할 점이</tgt>` | 1880 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1570 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>能够得到</src><tgt><\|wait\|></tgt>` | 709 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>与他吊不到</src><tgt>그 사람이</tgt>` | 1658 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 807 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>了。</src><tgt><\|wait\|></tgt>` | 1163 |

---

### Test Example 31 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 890 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1051 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src>there were </src><tgt>没什么新意，</tgt>` | 1167 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such instances before </src><tgt><\|wait\|></tgt>` | 1195 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1168 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>netFilterTC, </src><tgt>在netFilterTC之前就发生过类似的情况，</tgt>` | 1345 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>and so </src><tgt><\|wait\|></tgt>` | 641 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1850 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>this is just one another place </src><tgt>所以这只是</tgt>` | 1591 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>where it </src><tgt><\|wait\|></tgt>` | 1191 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1353 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src>bad developed </src><tgt>另一个地方，</tgt>` | 1571 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>or engineered with </src><tgt><\|wait\|></tgt>` | 1514 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>unknown bug reports should be </src><tgt><\|wait\|></tgt>` | 1265 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt>应该知道这个bug报告的来源。</tgt>` | 1346 |

---

### Test Example 32 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1032 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个</src><tgt><\|wait\|></tgt>` | 1052 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>罗马呢，</src><tgt>皆さんにお伝えしたいのですが、このローマでは</tgt>` | 1376 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1068 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>一日のうちにできることではありません。ですから、今</tgt>` | 1739 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所建立的一些</src><tgt><\|wait\|></tgt>` | 1837 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>位基啊</src><tgt><\|wait\|></tgt>` | 1401 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>跟丰盛</src><tgt>築き上げた基盤や豊かさの</tgt>` | 1858 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 1049 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一夜之间就眼变出来。</src><tgt><\|wait\|></tgt>` | 1810 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src><\|wait\|></src><tgt>変化も、一晩で目の前に現れるものではありません。</tgt>` | 1944 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 680 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢，</src><tgt><\|wait\|></tgt>` | 1244 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 754 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>백오십만 개가 중고 번에서 </src><tgt><\|wait\|></tgt>` | 1480 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>1,200미만 으로 </src><tgt>そのうち150万個は中古販売で1200万未満で</tgt>` | 1903 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>4,000여 원 </src><tgt><\|wait\|></tgt>` | 1370 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>기업 들이 많았습니다. </src><tgt><\|wait\|></tgt>` | 1441 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>4000ウォン程度の企業が多かったんです。一般的には</tgt>` | 1288 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1368 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 혹은 </src><tgt><\|wait\|></tgt>` | 1685 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>폐업해 길게 되는데 </src><tgt>中小企業は成長したり、あるいは廃業したりして、長く続かないことが多いんですが、</tgt>` | 2257 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>이거 는 </src><tgt><\|wait\|></tgt>` | 1690 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업 들은 </src><tgt><\|wait\|></tgt>` | 1717 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>これに対して、中小企業は成長も廃業もせず、</tgt>` | 1422 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들을 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 781 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 729 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>砸到了一个铁头，</src><tgt><\|wait\|></tgt>` | 1152 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>那如果你</src><tgt>鉄の塊にぶつかって、</tgt>` | 1283 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>打到了铁头之后，</src><tgt><\|wait\|></tgt>` | 1155 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src>抓前</src><tgt>鉄の塊に当たった後は、</tgt>` | 1647 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>手阻，</src><tgt><\|wait\|></tgt>` | 1667 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说哎，那我</src><tgt><\|wait\|></tgt>` | 1571 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src>再继续操作</src><tgt>必ず前腕でガードしてください。そうすると、「あ、また</tgt>` | 2314 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦，</src><tgt><\|wait\|></tgt>` | 841 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1538 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>操作しなきゃ」なんて思わないでください。なぜそんな言い方をするのか、</tgt>` | 2346 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1079 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 600 |

---

### Test Example 35 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十日、</src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>二日手とかですか。</src><tgt>十日、二日手之类的吗？</tgt>` | 1559 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく十秒で</src><tgt><\|wait\|></tgt>` | 902 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1249 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>一秒に</src><tgt>大概十秒，</tgt>` | 1461 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 516 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>ススンスかな。</src><tgt><\|wait\|></tgt>` | 2035 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>ね。</src><tgt>一秒左右吧。嗯。</tgt>` | 1696 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1605 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらくする</src><tgt><\|wait\|></tgt>` | 866 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src>十一日に</src><tgt>然后，大概十一日</tgt>` | 1546 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1485 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 831 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮馬とかが</src><tgt>的时候，宫马</tgt>` | 1118 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 739 |

---

### Test Example 36 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1056 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어디 를 보면 </src><tgt><\|wait\|></tgt>` | 871 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>가장 20대를 </src><tgt>你看，</tgt>` | 1059 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 이런 </src><tgt><\|wait\|></tgt>` | 1137 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>동생 이자 </src><tgt><\|wait\|></tgt>` | 1199 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 </src><tgt>最年轻的弟弟，</tgt>` | 759 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1586 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1566 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>也是家人，也是家族的一份子。所以，</tgt>` | 1836 |
| 10 | `<src>책임감 보다는 </src><tgt>所以比起责任感，</tgt>` | `<src>재생 감 보다는 </src><tgt><\|wait\|></tgt>` | 1375 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1363 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>쓰는 </src><tgt>比起依赖他，</tgt>` | 1640 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1436 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 것을 </src><tgt><\|wait\|></tgt>` | 1077 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt>多做些自己能做的事，</tgt>` | 1193 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 1027 |

---

### Test Example 37 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1098 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | 910 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>운전 을 </src><tgt>进去之后会迷路。开车</tgt>` | 1159 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하려고 은 </src><tgt><\|wait\|></tgt>` | 1009 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1317 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>있으면 </src><tgt>想开车就走路，</tgt>` | 792 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>막굴 가면 </src><tgt><\|wait\|></tgt>` | 1402 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1592 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가 면 또 </src><tgt>走得越远越难，</tgt>` | 1878 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. </src><tgt><\|wait\|></tgt>` | 1331 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 챙겨 내려. </src><tgt><\|wait\|></tgt>` | 1388 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>更别提出国了。得好好照顾自己。不如现在</tgt>` | 2325 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1128 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>무뤄봐요. 그거 는 </src><tgt><\|wait\|></tgt>` | 830 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>잘 아는 것 같아요. </src><tgt>努力做个无聊的事吧，好像挺熟悉的。</tgt>` | 1482 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 910 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 802 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와, </src><tgt><\|wait\|></tgt>` | 1144 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>너희 가 </src><tgt>あなたたちも知っているでしょう。あなたたちが</tgt>` | 1496 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 있을 때에 </src><tgt><\|wait\|></tgt>` | 1002 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1195 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>말 못 하는 우선에게로 </src><tgt>言葉を話せない異邦人たちに</tgt>` | 1773 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1612 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>그리 와 갔느니라. </src><tgt><\|wait\|></tgt>` | 1763 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src><\|wait\|></src><tgt>そのまま、そのまま行ってしまったのです。</tgt>` | 1584 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1125 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 1727 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>だから、私があなたたちに知らせるのです。</tgt>` | 1883 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 </src><tgt><\|wait\|></tgt>` | 795 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>영으로 </src><tgt><\|wait\|></tgt>` | 1180 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는. </src><tgt>神の霊によって語る者は……</tgt>` | 1132 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1051 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1110 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>needs to get </src><tgt>「今から</tgt>` | 1134 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1189 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I got ten of them </src><tgt><\|wait\|></tgt>` | 1408 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt>動き出したい人、</tgt>` | 1662 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1012 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to </src><tgt><\|wait\|></tgt>` | 1108 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go into </src><tgt>本当に大事なこと10個あります。そのうちの10個について、</tgt>` | 2580 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one </src><tgt><\|wait\|></tgt>` | 1420 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 1638 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>この動画の続きとして1分程度の動画を</tgt>` | 1981 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 780 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>You know, </src><tgt><\|wait\|></tgt>` | 1220 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>a little more detail, </src><tgt>用意しています。それぞれを解説します。もう少し詳しく、</tgt>` | 1200 |

---

### Test Example 40 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 780 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>呃，XJML</src><tgt><\|wait\|></tgt>` | 1097 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt>呃，</tgt>` | 1108 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 컴피트도 </src><tgt><\|wait\|></tgt>` | 1250 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>사람 도 </src><tgt>Compit，也就是XJML，大家</tgt>` | 1730 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 2018 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴피트 언어 의 </src><tgt><\|wait\|></tgt>` | 1763 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src><\|wait\|></src><tgt>都能理解，</tgt>` | 1521 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 말하기. 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1062 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1488 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>我们现在需要编写代码，</tgt>` | 1806 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 745 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1344 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>所以需要一个程序来编写这些代码。</tgt>` | 1100 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 920 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1161 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>还不错的，但是</src><tgt>金運については、今月はかなり良いと言えます。ただ、</tgt>` | 1879 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正财</src><tgt><\|wait\|></tgt>` | 1272 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>的部分，</src><tgt><\|wait\|></tgt>` | 695 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>也就是在事业方面</src><tgt>正財に偏っています。つまり、仕事面では</tgt>` | 1669 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长</src><tgt><\|wait\|></tgt>` | 1884 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>带来的红利</src><tgt><\|wait\|></tgt>` | 1650 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>与收入的提升。</src><tgt>業績アップによる恩恵や収入の増加が期待できます。</tgt>` | 1948 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果说投资理财方面，</src><tgt><\|wait\|></tgt>` | 1790 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1325 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错的，</src><tgt>投資・資産運用面では、今月も良いでしょう。</tgt>` | 1274 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对正财来说，</src><tgt><\|wait\|></tgt>` | 767 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微落了那么一点</src><tgt><\|wait\|></tgt>` | 1058 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>点。</src><tgt>ただ、正財に比べると少しだけ控えめかもしれません。</tgt>` | 1064 |

---

### Test Example 42 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1024 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう蒸らせてやるよ。</src><tgt><\|wait\|></tgt>` | 1088 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>俺は</src><tgt>그럼 그냥 끓여버릴 거야. 난</tgt>` | 1232 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt><\|wait\|></tgt>` | 1145 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き地を見ている。</src><tgt><\|wait\|></tgt>` | 1346 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>지금 끓는 거 보고 있어.</tgt>` | 1461 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 549 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えている</src><tgt><\|wait\|></tgt>` | 2066 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不烈火勢気よ。</src><tgt>이건 진짜, 진짜 한계가 넘어서는 불꽃이야.</tgt>` | 2285 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1375 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1579 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船内で</src><tgt>오랫동안 배 안에서</tgt>` | 1532 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>クーヤやってる</src><tgt><\|wait\|></tgt>` | 1270 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1078 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい海賊船を</src><tgt>쿠야를 해온 나한테는</tgt>` | 1103 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | 446 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1140 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>색인 보라 </src><tgt><\|wait\|></tgt>` | 1075 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>目を閉じて、色を紫にしてみよう。</tgt>` | 1320 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 </src><tgt><\|wait\|></tgt>` | 1175 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋든 댄 차리 돋든 댄 </src><tgt><\|wait\|></tgt>` | 1440 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 오면 </src><tgt>昔の書物が浮かんでくる感じがしたら、</tgt>` | 1750 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 2106 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1726 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>귀신 이 </src><tgt>それを振って一緒に遊ぼうってこと。</tgt>` | 1753 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>너무 굴릴 거고 </src><tgt><\|wait\|></tgt>` | 1700 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>시니 이움이야. </src><tgt><\|wait\|></tgt>` | 1581 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>お化けがすごく邪魔してくるから、守ってくれって</tgt>` | 1412 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>해 주니까 </src><tgt><\|wait\|></tgt>` | 1310 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 1062 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>言ってるんだから、リラックスして目を閉じて。</tgt>` | 784 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1035 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1147 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうやつでやって、</src><tgt>This is a visual development environment.</tgt>` | 1488 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルパイソン</src><tgt><\|wait\|></tgt>` | 913 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1275 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのも、</src><tgt>It's a Visual Python development environment.</tgt>` | 1712 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルに書いて</src><tgt><\|wait\|></tgt>` | 2159 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>あとそれは</src><tgt><\|wait\|></tgt>` | 1531 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードがそっから生成される</src><tgt>The reason is that you write it in FlowGraph Visual, and then Python code is generated from there.</tgt>` | 2350 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>っていうそれが</src><tgt><\|wait\|></tgt>` | 1584 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1582 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われる</src><tgt>When that runs, signal processing happens.</tgt>` | 1148 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>っていう工程になっているから</src><tgt><\|wait\|></tgt>` | 1109 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 732 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>That's the process it goes through.</tgt>` | 715 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt><\|wait\|></tgt>` | 792 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1027 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1111 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>How far did you </src><tgt>학력 수준. 얼마나</tgt>` | 1210 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1134 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>교육을 마쳤나요? 고등학교를 졸업했나요?</tgt>` | 1895 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 2021 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1640 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>그게 한 단계의 학력 수준입니다. 대학에 갔나요?</tgt>` | 1975 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, </src><tgt><\|wait\|></tgt>` | 1673 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>did you graduate? </src><tgt><\|wait\|></tgt>` | 1550 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of attainment. </src><tgt>그렇다면 졸업했나요? 그게 또 다른 단계의 학력 수준입니다.</tgt>` | 1637 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1194 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. </src><tgt><\|wait\|></tgt>` | 974 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>I'll see you online. </src><tgt>자, 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 897 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1020 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 884 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt>ですので、もちろんこういうケースもあります。私たちが</tgt>` | 1386 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>서로 콘텐츠 예요. </src><tgt>AさんとBさんがお互いにコンテンツを共有している場合です。</tgt>` | 1886 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 콘텐츠 예요 </src><tgt><\|wait\|></tgt>` | 1994 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 되고 </src><tgt><\|wait\|></tgt>` | 1440 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | 1116 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1435 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1698 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람 이 </src><tgt>悪意のあるコードを送ったとき、Bさんが</tgt>` | 1898 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 720 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스 사이트 크리티에서 </src><tgt><\|wait\|></tgt>` | 1406 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>JSP까지 </src><tgt>クロスサイトクリティカルからJSPまで</tgt>` | 1038 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까 </src><tgt><\|wait\|></tgt>` | 837 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 </src><tgt><\|wait\|></tgt>` | 896 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인 다면 </src><tgt>If the stock index is showing an upward trend,</tgt>` | 1870 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러 면 대형 주도 </src><tgt><\|wait\|></tgt>` | 1129 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 </src><tgt><\|wait\|></tgt>` | 856 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>상승 을 </src><tgt><\|wait\|></tgt>` | 1529 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 먼저 </src><tgt><\|wait\|></tgt>` | 1543 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 </src><tgt><\|wait\|></tgt>` | 1474 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1553 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1421 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 </src><tgt><\|wait\|></tgt>` | 1586 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 1554 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1279 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1338 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 994 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>we'll see a large- cap lead. But since smaller stocks usually lead the market first, we should always keep an eye on the small- cap stocks.</tgt>` | 1112 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 705 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1108 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>분석 을 해놨습니다. </src><tgt>これについて多くの人が分析をしています。</tgt>` | 1645 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 722 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠 자의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1475 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>このロクジャの分析を見ると、ソニーが</tgt>` | 1740 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>UHD에 </src><tgt><\|wait\|></tgt>` | 1794 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FP 파이프 를 </src><tgt><\|wait\|></tgt>` | 1537 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>UHDにFPパイプを128ビットに</tgt>` | 2157 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나충가서 로 포인트 된다. </src><tgt><\|wait\|></tgt>` | 1789 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1554 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>엑스 박스 시리즈, </src><tgt>増強してポイントになっています。Xboxシリーズ、</tgt>` | 1384 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1229 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt><\|wait\|></tgt>` | 990 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>LSI가 여기 도 없다. </src><tgt>Xboxにもないインフィニットキャッシュ、LSIもありません。</tgt>` | 736 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 468 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 928 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt>活動、そして</tgt>` | 1212 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, because you're </src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | 1259 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>but the reality </src><tgt>自分たちで基準を定義することです。なぜなら、あなたたちは完全に正しいからです。しかし、</tgt>` | 1910 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1833 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt><\|wait\|></tgt>` | 1940 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>on the block, and because </src><tgt>現実とは、私たちが新しい猫のブロックだからです。そして、</tgt>` | 2065 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt><\|wait\|></tgt>` | 1639 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1459 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前から基準が変わってきたからこそ、</tgt>` | 1270 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1262 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our own standard, </src><tgt><\|wait\|></tgt>` | 1015 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt>私たちは自分たちの基準に照らされているのです。なぜなら、今の状況では、</tgt>` | 814 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められています。なぜなら、今はすべてがより高い基準を求められているからです。</tgt>` | `<src>is being held to </src><tgt><\|wait\|></tgt>` | 517 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1020 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感觉</src><tgt><\|wait\|></tgt>` | 1131 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt>相手の感情を</tgt>` | 1143 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真性的意图的，</src><tgt><\|wait\|></tgt>` | 1301 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1300 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>很多是</src><tgt>推し量ったり、感じ取ったりする。</tgt>` | 1702 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1672 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>后经场会提到</src><tgt><\|wait\|></tgt>` | 1573 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>人们这样说：“</src><tgt>多くの人が、後世の場ではこう言います。</tgt>` | 1846 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1049 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1586 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>又在说谎了。”</src><tgt>「見て、この人はまた嘘をついている」と。</tgt>` | 2070 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 751 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1211 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>彼の目はすべてを物語っているのです。</tgt>` | 1076 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 707 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说：“</src><tgt><\|wait\|></tgt>` | 507 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1010 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 1133 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src>be able to move </src><tgt>另外，你将无法</tgt>` | 1284 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1001 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt>在资源之间移动媒体对象，</tgt>` | 1675 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>unless </src><tgt><\|wait\|></tgt>` | 410 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 1923 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>a situation where you </src><tgt>除非</tgt>` | 1549 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1817 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1219 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource. </src><tgt>你意识到把错误的媒体文件添加到了某个资源中。</tgt>` | 1908 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>Then we'll </src><tgt><\|wait\|></tgt>` | 942 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>now and we can see about </src><tgt><\|wait\|></tgt>` | 904 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src><\|wait\|></src><tgt>接下来，我们来看看</tgt>` | 1188 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure </src><tgt><\|wait\|></tgt>` | 1076 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>you get back up </src><tgt><\|wait\|></tgt>` | 823 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt>移动这些媒体文件，并确保它们能正确恢复。</tgt>` | 660 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 768 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>ForallE的首制</src><tgt><\|wait\|></tgt>` | 1134 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>截止到那个现象，</src><tgt>ForallE의 첫 번째</tgt>` | 1497 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 869 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>美登们处于</src><tgt><\|wait\|></tgt>` | 1341 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>暧昧中，</src><tgt>정점까지는 미정 상태였고,</tgt>` | 1735 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>属位的爱，</src><tgt><\|wait\|></tgt>` | 1800 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>我们也</src><tgt><\|wait\|></tgt>` | 1227 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>同时进入</src><tgt>그때는 애매한 관계였죠. 동시에</tgt>` | 1695 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1312 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨在掌上的时候，</src><tgt><\|wait\|></tgt>` | 1880 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>他才爱。</src><tgt>그들이 ' 恨' 의 손에 들렸을 때 비로소 사랑을 느꼈습니다.</tgt>` | 2364 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1264 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>他就变成</src><tgt><\|wait\|></tgt>` | 797 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>恨，</src><tgt>밤이 되면 그는 ' 恨' 이 되고,</tgt>` | 553 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个钟摆。</src><tgt><\|wait\|></tgt>` | 809 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续</src><tgt><\|wait\|></tgt>` | 412 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>在移动。</src><tgt>그 钟摆은 계속 움직입니다.</tgt>` | 386 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1246 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 956 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section </src><tgt>最初のセクションで少し混乱してしまって、</tgt>` | 1211 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1207 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the EHR </src><tgt><\|wait\|></tgt>` | 1346 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src>field being of critical </src><tgt>EHRの重要性について</tgt>` | 1436 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 544 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1676 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src><\|wait\|></src><tgt>「</tgt>` | 1152 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 1493 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously to my loves. </src><tgt><\|wait\|></tgt>` | 1561 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt>バリアントデータベースとの比較」という部分で、少し戸惑いました。もちろん、それは私の愛する人たちにとって明らかです。つまり、</tgt>` | 3090 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1197 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1059 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>that need to be in these </src><tgt>これらの</tgt>` | 863 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 574 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from. </src><tgt><\|wait\|></tgt>` | 754 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, right? </src><tgt>データソースに含めるべきフィールドについて合意できていないなら、そこから引き出すものはないですよね？</tgt>` | 888 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 447 |

---

### Test Example 54 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful, </src><tgt><\|wait\|></tgt>` | 866 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>individual right, </src><tgt>有意义的、个人的权利，</tgt>` | 1197 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1075 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1260 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't know </src><tgt>最高法院最后才跟上。我不知道</tgt>` | 1655 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 701 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the the van </src><tgt><\|wait\|></tgt>` | 1790 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>ard of </src><tgt>法院是否想成为</tgt>` | 1467 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1235 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days, </src><tgt><\|wait\|></tgt>` | 1338 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>but they rather </src><tgt>社会变革的先锋。但现在，他们更倾向于</tgt>` | 2110 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 1483 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 760 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>that's already </src><tgt>反映已经形成的共识，</tgt>` | 1149 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 964 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 488 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src>You have </src><tgt>已经浮现出来的共识。</tgt>` | 870 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 441 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 284 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who. </src><tgt>你有一些联邦法官，他们……</tgt>` | 465 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 764 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 1039 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>is a son of Henry, </src><tgt>ある時、彼はイエスがヘンリーの息子だと知りました。</tgt>` | 2000 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1241 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's a Judah </src><tgt><\|wait\|></tgt>` | 802 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>before the wilderness </src><tgt>彼は、イエスが</tgt>` | 1453 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>spurtiday, that he's hungry, </src><tgt><\|wait\|></tgt>` | 2364 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he sends </src><tgt><\|wait\|></tgt>` | 1612 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>to Jesus. Hey, if you're </src><tgt>荒野の祭りの前にユダヤ人だったこと、そして飢えていることを知っていました。だから、イエスに送りました。「おい、</tgt>` | 3071 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>Jesus, hey, if you're a son of God, prove it. </src><tgt><\|wait\|></tgt>` | 1906 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn these </src><tgt><\|wait\|></tgt>` | 943 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>stones to bread. </src><tgt>イエスよ、もし神の息子なら証明してみろ。この石をパンに変えろ。</tgt>` | 1482 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 747 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that </src><tgt><\|wait\|></tgt>` | 710 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>彼はその誘惑にどう対処したのでしょうか？</tgt>` | 935 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 411 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by </src><tgt><\|wait\|></tgt>` | 314 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>barrel alone. </src><tgt>いやはや、ジョナタンは樽を一人で運んだ。</tgt>` | 574 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 961 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1100 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src><\|wait\|></src><tgt>자, 사진을 한번 볼게요.</tgt>` | 1226 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，</src><tgt><\|wait\|></tgt>` | 1129 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1341 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>客订的部分，</src><tgt>사진 부분에는 ' 주문 ' 이라는 항목이 보이네요.</tgt>` | 1796 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客订一般</src><tgt><\|wait\|></tgt>` | 1773 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是</src><tgt><\|wait\|></tgt>` | 1166 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src>属于我们要</src><tgt>보통 ' 주문 ' 은</tgt>` | 1524 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>收集</src><tgt><\|wait\|></tgt>` | 1326 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的地方，</src><tgt><\|wait\|></tgt>` | 1588 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src>所以呢，</src><tgt>우리가 수집해야 하는 항목이에요. 그래서</tgt>` | 1689 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>这身体的部分呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1232 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 1109 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>一点时间</src><tgt>이 신체 부분은</tgt>` | 978 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 475 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来收集</src><tgt><\|wait\|></tgt>` | 772 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可做，我们可以看到</src><tgt>자신을 위해 앉아서 잘 수집할 수 있는 시간이에요. 여기</tgt>` | 679 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是空五椅人的嘛。</src><tgt><\|wait\|></tgt>` | 408 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 347 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>빈 의자 다섯 개가 있는 걸 볼 수 있죠. 자, 그러니까...</tgt>` | 535 |

---

### Test Example 57 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 791 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1094 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>and they often </src><tgt>彼らは非常に稀で、</tgt>` | 1208 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1127 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するような存在です。</tgt>` | 1783 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>The personality is </src><tgt><\|wait\|></tgt>` | 1364 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>something of a contradiction. </src><tgt>その性格は矛盾をはらんでいます。</tgt>` | 1686 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1311 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1773 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ではありますが、</tgt>` | 1828 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 766 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | 1300 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src><\|wait\|></src><tgt>無意味な会話を嫌い、</tgt>` | 1084 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to </src><tgt><\|wait\|></tgt>` | 739 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 490 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>要点を直接言いたいタイプです。また、</tgt>` | 499 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 399 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>playing the devil's advocate, </src><tgt><\|wait\|></tgt>` | 380 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and never </src><tgt>悪魔の代弁者になるのも好きで、</tgt>` | 413 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>shy away from a debate. </src><tgt><\|wait\|></tgt>` | 325 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 343 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src>E and T P </src><tgt>議論を避けることはありません。</tgt>` | 374 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for. </src><tgt><\|wait\|></tgt>` | 335 |

---

### Test Example 58 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 847 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt><\|wait\|></tgt>` | 1191 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>거부 한 멤버 이 </src><tgt>Lee Jun- seok was a member who rejected the government</tgt>` | 1858 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>후보 를 위해서 하며서 </src><tgt><\|wait\|></tgt>` | 1303 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 771 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1419 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색까지 </src><tgt><\|wait\|></tgt>` | 1820 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt>for his candidacy, and even offered a humble apology for his candidacy. But now</tgt>` | 2262 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1537 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1434 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 910 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석은 들은 해놓고 </src><tgt>Lee Jun- seok was heard about</tgt>` | 2053 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 707 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 1104 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 974 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 714 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 508 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 430 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt>and was determined to attack Lee Jun- seok with the venom to overthrow the Yoon Suk- yeol candidate the moment he removed Kim Jong- in.</tgt>` | 833 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 336 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석의 성상납건 </src><tgt><\|wait\|></tgt>` | 349 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 295 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 323 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 얼마나 </src><tgt><\|wait\|></tgt>` | 302 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재입니까? </src><tgt>How big of a boon is the Minjoo Party's attack on Lee Jun- seok's sexual scandal?</tgt>` | 525 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>で、まあ</src><tgt><\|wait\|></tgt>` | 1047 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 1081 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので、</src><tgt>So, I want to make something after the meal now. So,</tgt>` | 1943 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>でここのね</src><tgt><\|wait\|></tgt>` | 1263 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>プロフェッショナルホテル</src><tgt><\|wait\|></tgt>` | 755 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も朝食が</src><tgt>the breakfast at this professional hotel</tgt>` | 1548 |
| 7 | `<src>朝食が食べれる場所</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1580 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1374 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので、</src><tgt>is supposed to be a place where you can have breakfast. So,</tgt>` | 2039 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1049 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1761 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>I'd like to stay at the Goldston Hotel here in the future.</tgt>` | 2136 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>な方がですね、</src><tgt><\|wait\|></tgt>` | 737 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1061 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見て、まあいいんじゃないか</src><tgt>If you're considering staying there,</tgt>` | 1106 |
| 16 | `<src><\|wait\|></src><tgt>thinking about staying here in the future,</tgt>` | `<src>なと、はい、</src><tgt><\|wait\|></tgt>` | 866 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 375 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここのホテルからですね。</src><tgt>and you think, ' Hmm, that sounds good. Yes, I think so. ' From this hotel...</tgt>` | 689 |
| 19 | `<src>駅ももう</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 346 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 388 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt>it takes</tgt>` | 256 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 298 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 346 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいね、まあホテル</src><tgt>about a kilometer to walk to Busan Station, or maybe not. It's a really well- located hotel.</tgt>` | 594 |
| 25 | `<src>ホテルになってますので</src><tgt>so the location is really good.</tgt>` | `<src>なってますので、</src><tgt><\|wait\|></tgt>` | 262 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 251 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt>So if you're interested,</tgt>` | 291 |
| 28 | `<src>ください</src><tgt>If you'd like, please consider it.</tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 255 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね、今回は。</src><tgt><\|wait\|></tgt>` | 291 |

---

### Test Example 60 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 888 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이거 이 저 </src><tgt><\|wait\|></tgt>` | 1074 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>얘를 쓸 수 있지만 </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ` | 12918 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요. </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ` | 7556 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt><\|wait\|></tgt>` | 344 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보세요, 근데 꾸밀 필요 가 </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、` | 2828 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>없고 나만 </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、` | 1616 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보여줄 수 </src><tgt><\|wait\|></tgt>` | 168 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>있지만 보이 색이 우주 가 </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、` | 1521 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>지다. 안테 보살 이러는 </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ` | 1527 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 167 |
