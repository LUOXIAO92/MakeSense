# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9554
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4172
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 3
  - TARGET_METRICS_FILTERED_TURN_COUNT: 38
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 57
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 91
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 740
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1335.3290
  - PROCESS_TIME_MS_P50: 1363.3020
  - PROCESS_TIME_MS_P95: 2064.6040
  - PROCESS_TIME_MS_MAX: 4424.3080

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气熟</src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的，</src><tgt><\|wait\|></tgt>` | 1048 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 1048 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | 1196 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1185 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>知道如何</src><tgt><\|wait\|></tgt>` | 904 |
| 7 | `<src>处于中间，</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>处于中间，</src><tgt>気熟すれば簡単です。でも、師匠が</tgt>` | 2142 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 724 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要凡</src><tgt><\|wait\|></tgt>` | 1587 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 1526 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | 1666 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1113 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 988 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1138 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的</src><tgt><\|wait\|></tgt>` | 1261 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水，</src><tgt><\|wait\|></tgt>` | 1249 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 1321 |
| 7 | `<src>给足</src><tgt>What parents need to do is this: water and fertilize with our deep love,</tgt>` | `<src>给足</src><tgt>What parents need to do is water and fertilize with our deep love,</tgt>` | 1829 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | 1298 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>并耐心</src><tgt><\|wait\|></tgt>` | 1348 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>等孩子</src><tgt><\|wait\|></tgt>` | 1172 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1576 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 739 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1060 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>この中まだ</src><tgt><\|wait\|></tgt>` | 1071 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1436 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1611 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | 1335 |
| 7 | `<src>剪定を</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>剪定を</src><tgt>从一开始，因为这还是一年级，所以</tgt>` | 1405 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こうタイズして</src><tgt><\|wait\|></tgt>` | 1227 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>あげると</src><tgt><\|wait\|></tgt>` | 1445 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1090 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 1509 |

---

### Test Example 4 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 849 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 1046 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt><\|wait\|></tgt>` | 1054 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>extremely happy people. This is </src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking at </src><tgt><\|wait\|></tgt>` | 1397 |
| 7 | `<src>looking at the ten percent </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。</tgt>` | `<src>10% </src><tgt>非常に幸せな人々の研究を少し行いました。これはあくまで端緒の研究です。</tgt>` | 1679 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1146 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1222 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people who have </src><tgt><\|wait\|></tgt>` | 1512 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>been able to learn from. </src><tgt><\|wait\|></tgt>` | 1571 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>怪得</src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>嵩子儿这儿，</src><tgt><\|wait\|></tgt>` | 997 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个游行也很大，</src><tgt><\|wait\|></tgt>` | 1181 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1268 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 1242 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在旁边</src><tgt><\|wait\|></tgt>` | 1166 |
| 7 | `<src>儿核桃</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add</tgt>` | `<src>喝汤儿，</src><tgt>It's strange, it's so crowded here. The parade is huge. And I'm drinking soup over here,</tgt>` | 2415 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1721 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>感觉挺累的。</src><tgt><\|wait\|></tgt>` | 1442 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1691 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>这种喝汤儿。</src><tgt><\|wait\|></tgt>` | 1579 |

---

### Test Example 6 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘撒完以</src><tgt><\|wait\|></tgt>` | 1077 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>后呢，</src><tgt><\|wait\|></tgt>` | 1241 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力</src><tgt><\|wait\|></tgt>` | 975 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也Swan了</src><tgt><\|wait\|></tgt>` | 1447 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>了，</src><tgt><\|wait\|></tgt>` | 1652 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>然后就停留在</src><tgt><\|wait\|></tgt>` | 1626 |
| 7 | `<src>相对的低</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的</tgt>` | `<src>一个相对的</src><tgt>淘洗が終わると、内部の圧力エネルギーも収まり、</tgt>` | 1322 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态。</src><tgt><\|wait\|></tgt>` | 1917 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>这</src><tgt><\|wait\|></tgt>` | 1247 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>就是所谓的</src><tgt><\|wait\|></tgt>` | 1638 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>低于状态。</src><tgt><\|wait\|></tgt>` | 1666 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1082 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1268 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 857 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1293 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 1408 |
| 7 | `<src><\|wait\|></src><tgt>大致是从这一带开始的，</tgt>` | `<src><\|wait\|></src><tgt>大概是从这方面开始的，</tgt>` | 1399 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 775 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1822 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1336 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1644 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも。</src><tgt><\|wait\|></tgt>` | 1897 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=6)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 868 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Aptitude </src><tgt><\|wait\|></tgt>` | 1388 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축발시키고 </src><tgt><\|wait\|></tgt>` | 863 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1316 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1682 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>버무로 죽인 </src><tgt><\|wait\|></tgt>` | 1629 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt>I am Aptitude, and I'm going to kill my own servant, Hernan,</tgt>` | 1503 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1735 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1362 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1706 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1820 |

---

### Test Example 9 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=6)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1165 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt><\|wait\|></tgt>` | 1289 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 879 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1426 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1687 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>않았고 무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1831 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt>The people in the auspicious spots were not actually highly intelligent. They were just randomly selected</tgt>` | 1356 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>였기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 1850 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1301 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1583 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐 던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1927 |

---

### Test Example 10 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 700 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 905 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1085 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>的一个轨道哦，</src><tgt><\|wait\|></tgt>` | 439 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1232 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>好自在的</src><tgt><\|wait\|></tgt>` | 1684 |
| 7 | `<src>在做热汤</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>时候在工作</src><tgt>제 삶의 궤도로 돌아가게 해줘요. 그래야 편안하게</tgt>` | 2467 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>和谈热爱的，所以子女们，</src><tgt><\|wait\|></tgt>` | 1673 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我只是</src><tgt><\|wait\|></tgt>` | 1669 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被掏着做作业</src><tgt><\|wait\|></tgt>` | 865 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的小愿望</src><tgt><\|wait\|></tgt>` | 1358 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 1938 |

---

### Test Example 11 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 917 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 1128 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 961 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1501 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1622 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt><\|wait\|></tgt>` | 1546 |
| 7 | `<src>不要想自己</src><tgt>In this situation, when we encounter a problem, we should</tgt>` | `<src>不要想自己</src><tgt>When we face such a situation, we should quickly report it to our supervisor or let them know about the situation. Don't think</tgt>` | 2401 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1807 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>不理成担，</src><tgt><\|wait\|></tgt>` | 862 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言</src><tgt><\|wait\|></tgt>` | 1441 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是应该做的事情。</src><tgt><\|wait\|></tgt>` | 2065 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 755 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 1229 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into your body. </src><tgt><\|wait\|></tgt>` | 994 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does the </src><tgt><\|wait\|></tgt>` | 1374 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>tension </src><tgt><\|wait\|></tgt>` | 1623 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1621 |
| 7 | `<src>Is it a headache? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？</tgt>` | `<src>Is it a head? </src><tgt>你的身体在做什么？进入你的身体。紧张感从哪里开始？是什么？是头吗？</tgt>` | 2059 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tension in your chest? </src><tgt><\|wait\|></tgt>` | 1975 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is the body </src><tgt><\|wait\|></tgt>` | 893 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>landing pitch </src><tgt><\|wait\|></tgt>` | 1523 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>you are using? </src><tgt><\|wait\|></tgt>` | 2049 |

---

### Test Example 13 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1128 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1031 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1357 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1584 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 1374 |
| 7 | `<src>ご連絡としては</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt>We also have T- shirts and other items available for you to receive, so please feel free to join us. For contact,</tgt>` | 1870 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1665 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、</src><tgt><\|wait\|></tgt>` | 1432 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>よろしく</src><tgt><\|wait\|></tgt>` | 1653 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>お応じがある</src><tgt><\|wait\|></tgt>` | 1038 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ものでしょう</src><tgt><\|wait\|></tgt>` | 1414 |

---

### Test Example 14 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>너무 의 절여야 </src><tgt><\|wait\|></tgt>` | 1074 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>할 수 있지만 </src><tgt><\|wait\|></tgt>` | 1070 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1456 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기가 </src><tgt><\|wait\|></tgt>` | 1735 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 프로 </src><tgt><\|wait\|></tgt>` | 2016 |
| 7 | `<src>뭐 있고 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？</tgt>` | `<src>보이 고 </src><tgt>これはあまりに崇めるべきですが、本当に菩薩です。いや、彼自身が菩薩なのに、夢のように見えて、</tgt>` | 2305 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1696 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 프로 보이 서 우주 가 </src><tgt><\|wait\|></tgt>` | 1711 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 이라는 </src><tgt><\|wait\|></tgt>` | 1101 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>거지. </src><tgt><\|wait\|></tgt>` | 1416 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1175 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1155 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 961 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | 1355 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1877 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1963 |
| 7 | `<src><\|wait\|></src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>And what you're not good </src><tgt>最后，就是重复。学会重复练习。找到你擅长的，多做一些。你</tgt>` | 2191 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>at, give to people </src><tgt><\|wait\|></tgt>` | 1818 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1707 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 654 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and tell the next time. </src><tgt><\|wait\|></tgt>` | 1939 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1200 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 930 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1185 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1371 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1246 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1511 |
| 7 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们</tgt>` | `<src><\|wait\|></src><tgt>好的。然后，在这些例子之后，说明</tgt>` | 1511 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 864 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1615 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 1307 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 1591 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>game dot sort array. </src><tgt><\|wait\|></tgt>` | 1873 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 993 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 924 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜줄에 </src><tgt><\|wait\|></tgt>` | 1395 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 890 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1572 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜줄에 </src><tgt><\|wait\|></tgt>` | 1639 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 1838 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room?</tgt>` | `<src>해쳐낸다. 내가 </src><tgt>Someone asked me to kill someone else, so I came to kill them. I'm going to kill them. I'm</tgt>` | 2437 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1659 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주변 은요, </src><tgt><\|wait\|></tgt>` | 1729 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1906 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1041 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そう</src><tgt><\|wait\|></tgt>` | 840 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>です。そこで</src><tgt><\|wait\|></tgt>` | 880 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>定期といえば</src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>節収時間</src><tgt><\|wait\|></tgt>` | 449 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>が過ぎましたね。</src><tgt><\|wait\|></tgt>` | 1318 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1608 |
| 7 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src><\|wait\|></src><tgt>맞아요. 그래서 ' 정기 ' 라면 절수 시간이 지났죠. 그래서</tgt>` | 2457 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井江義の仕組み</src><tgt><\|wait\|></tgt>` | 1428 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1404 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>元</src><tgt><\|wait\|></tgt>` | 980 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>節収時間</src><tgt><\|wait\|></tgt>` | 1600 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1936 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビズ。</src><tgt><\|wait\|></tgt>` | 1218 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 781 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1286 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 981 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间有着某种</src><tgt><\|wait\|></tgt>` | 1382 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>联系，</src><tgt><\|wait\|></tgt>` | 1671 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1532 |
| 7 | `<src><\|wait\|></src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src><\|wait\|></src><tgt>If a female high school student has some kind of connection with someone with a strange appearance,</tgt>` | 1476 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | 2280 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1094 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1543 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 1929 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇。</src><tgt><\|wait\|></tgt>` | 1197 |

---

### Test Example 20 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 927 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Finley Butler, </src><tgt><\|wait\|></tgt>` | 1171 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 978 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a BA in </src><tgt><\|wait\|></tgt>` | 1252 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance </src><tgt><\|wait\|></tgt>` | 1212 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a BSc in Psychology. </src><tgt><\|wait\|></tgt>` | 1722 |
| 7 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src><\|wait\|></src><tgt>제 이름은 핀리 버틀러입니다. 현재 비즈니스 재무학 학사 과정과 심리학 학사 과정을 동시에 공부하고 있습니다.</tgt>` | 2043 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 1815 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1281 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 1748 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy </src><tgt><\|wait\|></tgt>` | 1968 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1193 |

---

### Test Example 21 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだん</src><tgt><\|wait\|></tgt>` | 1239 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が</src><tgt><\|wait\|></tgt>` | 1367 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じ</src><tgt><\|wait\|></tgt>` | 882 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>をシャワーで</src><tgt><\|wait\|></tgt>` | 1359 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>受けた感じですね。</src><tgt><\|wait\|></tgt>` | 1693 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>回避したい方って</src><tgt><\|wait\|></tgt>` | 1667 |
| 7 | `<src>すごい</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人</tgt>` | `<src>すごい息苦しが</src><tgt>感觉距离在慢慢拉开，就像被淋浴喷水一样。想躲避的人</tgt>` | 1845 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>きし、</src><tgt><\|wait\|></tgt>` | 1386 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>呼吸でもっと</src><tgt><\|wait\|></tgt>` | 1320 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>遠回りして</src><tgt><\|wait\|></tgt>` | 1613 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>しゃがむ方が強いので、</src><tgt><\|wait\|></tgt>` | 2045 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので。</src><tgt><\|wait\|></tgt>` | 1230 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 867 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1123 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>遊ぶと、</src><tgt><\|wait\|></tgt>` | 462 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>シンガーが起き上がれなくなってしまう</src><tgt><\|wait\|></tgt>` | 1470 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1517 |
| 7 | `<src>ギアの先に</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>이게 기어예요. 기어가 돌아가면 싱어가 일어날 수 없게 되니까, 기어 앞에</tgt>` | 2807 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1521 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1637 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついてるっていうこと</src><tgt><\|wait\|></tgt>` | 1693 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 470 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2012 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>はい文法完了。</src><tgt><\|wait\|></tgt>` | 1480 |

---

### Test Example 23 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 </src><tgt><\|wait\|></tgt>` | 976 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>저는 용심히 </src><tgt><\|wait\|></tgt>` | 1301 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심히 </src><tgt><\|wait\|></tgt>` | 1251 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>새우 </src><tgt><\|wait\|></tgt>` | 1687 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>용심히가 </src><tgt><\|wait\|></tgt>` | 1303 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데요. 야, </src><tgt>So, there's some ' yongsimi ' (용심히) mixed in— it's like ' kal yongsimi ' (칼 용심히) and ' saeu yongsimi ' (새우 용심히 ). Wow,</tgt>` | 4424 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 835 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1604 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해행으로 </src><tgt><\|wait\|></tgt>` | 2090 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽임바야. </src><tgt><\|wait\|></tgt>` | 1556 |

---

### Test Example 24 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1072 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1085 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1336 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1753 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间大概有</src><tgt><\|wait\|></tgt>` | 1411 |
| 7 | `<src>大概有十位医生</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors</tgt>` | `<src>十位医生</src><tgt>I was doing great back then, so I didn't have to have surgery. During that time,</tgt>` | 1610 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | 1715 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿、</src><tgt><\|wait\|></tgt>` | 1461 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 1705 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1830 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 944 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1207 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 890 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>选择二击</src><tgt><\|wait\|></tgt>` | 1286 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>状态，</src><tgt><\|wait\|></tgt>` | 866 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>排除了</src><tgt><\|wait\|></tgt>` | 1228 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一击一线</src><tgt><\|wait\|></tgt>` | 1238 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | 1529 |
| 7 | `<src>比如说，呃，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、</tgt>` | `<src>比如说</src><tgt>二つ目の選択肢は「二撃」ステータスです。一対一の戦いで大牛たちを排除します。例えば、</tgt>` | 2122 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微</src><tgt><\|wait\|></tgt>` | 1709 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>性价比极低的一击</src><tgt><\|wait\|></tgt>` | 1463 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>机会，你会发现</src><tgt><\|wait\|></tgt>` | 1708 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微性价比平平的</src><tgt><\|wait\|></tgt>` | 1896 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>心棒反而</src><tgt><\|wait\|></tgt>` | 1102 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>活了。</src><tgt><\|wait\|></tgt>` | 1046 |

---

### Test Example 26 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 848 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AA面ですね。</src><tgt><\|wait\|></tgt>` | 1402 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 865 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>霊性速度かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1553 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | 1649 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>AAの乱交調べ</src><tgt><\|wait\|></tgt>` | 1935 |
| 7 | `<src>ことで、あの</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>ということで、あの</src><tgt>It's the AA face. When you're checking if it's a spiritual speed in various situations, you're looking for AA interference,</tgt>` | 2686 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その霊性速度かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1603 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>をすること、</src><tgt><\|wait\|></tgt>` | 1523 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>霊速度であることを保証する</src><tgt><\|wait\|></tgt>` | 1910 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような使い方をされます。</src><tgt><\|wait\|></tgt>` | 1249 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 931 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1162 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1535 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>and, </src><tgt><\|wait\|></tgt>` | 742 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore its </src><tgt><\|wait\|></tgt>` | 1377 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1734 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1719 |
| 7 | `<src><\|wait\|></src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>change can </src><tgt>19조 수정헌법의 의미와 그 역사를 탐구하며, 정치적 변화가</tgt>` | 1651 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt><\|wait\|></tgt>` | 1548 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>United States, </src><tgt><\|wait\|></tgt>` | 1292 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1583 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>the meanings of </src><tgt><\|wait\|></tgt>` | 1933 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>the amendment, of course, are </src><tgt><\|wait\|></tgt>` | 1419 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 798 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1067 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1359 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1635 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1379 |
| 7 | `<src>to spell </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>how to spell </src><tgt>あるいは、何かを書き出す必要がある場合、文章を書く必要がある場合、</tgt>` | 1681 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 1950 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1349 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 1696 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1885 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>p, double lam? I don't know. </src><tgt><\|wait\|></tgt>` | 1465 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 984 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 891 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1431 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 787 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 유사 한 </src><tgt><\|wait\|></tgt>` | 1457 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>작용 이 </src><tgt><\|wait\|></tgt>` | 1657 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1852 |
| 7 | `<src>굉장히 아주 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where</tgt>` | `<src>굉장히 아주 </src><tgt>These vanadium compounds are so similar to insulin that they cause a very, very</tgt>` | 1390 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1983 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1002 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1652 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 2039 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1329 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1033 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 845 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1257 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 995 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1449 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1771 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1835 |
| 7 | `<src>gets converted to </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>gets converted to </src><tgt>늘어난 고무줄처럼, 화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면, 그 잠재 에너지는</tgt>` | 2970 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1384 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 1643 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2061 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | 1504 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1371 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>达到了一个</src><tgt><\|wait\|></tgt>` | 750 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>极端，</src><tgt><\|wait\|></tgt>` | 1171 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 951 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了极端之后，</src><tgt><\|wait\|></tgt>` | 1286 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1248 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1281 |
| 7 | `<src>先守住，</src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。</tgt>` | `<src>先守走，</src><tgt>極端に達した場合は、必ず守り、</tgt>` | 1813 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说哎，那我再</src><tgt><\|wait\|></tgt>` | 1387 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1572 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | 1028 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1603 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 2205 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1447 |
| 14 | `<src>因为呢。</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、それはですね。</tgt>` | `<src>因为呢。</src><tgt>「あ、じゃあ、もっと操作しよう」なんて考えないでください。なぜそう言うかというと……</tgt>` | 1706 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 788 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>백오십만 개가 중고 번에서 </src><tgt><\|wait\|></tgt>` | 1837 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>1,200미만 으로 </src><tgt><\|wait\|></tgt>` | 530 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1383 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1623 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1924 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt>そのうち150万社は中古車市場で1,200万円未満の非常に小さな企業でした。一般的に、中小企業は成長するか、</tgt>` | 3384 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 에 </src><tgt><\|wait\|></tgt>` | 1045 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>익숙 해 그겁에 </src><tgt><\|wait\|></tgt>` | 1613 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>일본 에 </src><tgt><\|wait\|></tgt>` | 2025 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업들은 성장 도 </src><tgt><\|wait\|></tgt>` | 1419 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>표해 보하지 않을 </src><tgt><\|wait\|></tgt>` | 1448 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들만 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 802 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1075 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个</src><tgt><\|wait\|></tgt>` | 1136 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，</src><tgt><\|wait\|></tgt>` | 969 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1350 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1694 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1320 |
| 7 | `<src>所面临的一些</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している</tgt>` | `<src>所面临的一些</src><tgt>皆さんにお伝えしたいのですが、このローマは一日にしてできたものではありません。ですから、今皆さんが直面している</tgt>` | 1812 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊、跟风险</src><tgt><\|wait\|></tgt>` | 1921 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1251 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>你一时之间就</src><tgt><\|wait\|></tgt>` | 1677 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1865 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | 1120 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1063 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>危機やリスクも、一朝一夕で生まれたわけじゃありません。そこで、酉年生まれの皆さんには…</tgt>` | `<src>属鸡的朋友呢。</src><tgt>危機やリスクも、一瞬で生じたものではないということです。そのため、酉年生まれの方には、</tgt>` | 1903 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 934 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1288 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there are such </src><tgt><\|wait\|></tgt>` | 959 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>instances before </src><tgt><\|wait\|></tgt>` | 1247 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1684 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>next future TC, </src><tgt><\|wait\|></tgt>` | 1368 |
| 7 | `<src>Yeah, so </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以</tgt>` | `<src>and so </src><tgt>没什么新意，之前就有过类似的情况，接下来会</tgt>` | 1381 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1133 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>this is just one another place </src><tgt><\|wait\|></tgt>` | 1853 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at, </src><tgt><\|wait\|></tgt>` | 887 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1541 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but </src><tgt><\|wait\|></tgt>` | 2038 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1384 |
| 14 | `<src>working on BugRepo </src><tgt>这只是另一个需要关注的地方。但开发人员或在BugRepo工作的工程师</tgt>` | `<src>who work on Kubernetes should be </src><tgt>再看一个地方，但</tgt>` | 1600 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 946 |

---

### Test Example 35 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう寝かせている</src><tgt><\|wait\|></tgt>` | 906 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>より俺は</src><tgt><\|wait\|></tgt>` | 1089 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 414 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>火事を見ている</src><tgt><\|wait\|></tgt>` | 1332 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1667 |
| 7 | `<src>もう限界なんか</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미</tgt>` | `<src>もう限界なんか</src><tgt>그럼 이미 잠든 것보다 내가 불을 보고 있는 게</tgt>` | 2362 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えている</src><tgt><\|wait\|></tgt>` | 703 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈火勢気</src><tgt><\|wait\|></tgt>` | 1857 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1288 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1583 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船出を行っている</src><tgt><\|wait\|></tgt>` | 1939 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1237 |
| 14 | `<src>俺は</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야. 오랫동안 배를 만들어왔지만,</tgt>` | `<src>俺はこんなにすごい</src><tgt>한계가 넘어서, 불길한 기운이</tgt>` | 1407 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>海賊船を見た</src><tgt><\|wait\|></tgt>` | 713 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 964 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 767 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | 984 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1447 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1676 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>있고 사람 도 </src><tgt><\|wait\|></tgt>` | 1545 |
| 7 | `<src><\|wait\|></src><tgt>HTML是一种</tgt>` | `<src>이해 할 수 있는 </src><tgt>HTML，</tgt>` | 1077 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1440 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1483 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1019 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1546 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 2090 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1456 |
| 14 | `<src>프로그램 이 </src><tgt>计算机语言，计算机能理解，人类也能理解。我们需要按照它的语法来编写代码，而编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>计算机和人都能理解的计算机语言，我们得按照它的语法来写代码。写代码</tgt>` | 1722 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 846 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1195 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1277 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1545 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that I think are </src><tgt><\|wait\|></tgt>` | 1382 |
| 7 | `<src>really important. </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。</tgt>` | `<src>really important </src><tgt>今まさに動き出そうとしている人たち、そのうち10人くらいは、</tgt>` | 1574 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>and I'm going to go into. </src><tgt><\|wait\|></tgt>` | 2144 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one </src><tgt><\|wait\|></tgt>` | 795 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 1362 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | 2067 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1488 |
| 14 | `<src>that cover each one </src><tgt>それについてお話ししていきます。この動画の後に、それぞれを</tgt>` | `<src>You know, </src><tgt>すごく重要だと思うんです。これから見ていきます。この動画の後に、1分程度の動画が1つずつあります。そう、</tgt>` | 1925 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>a little more detail, </src><tgt><\|wait\|></tgt>` | 631 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>授業</src><tgt><\|wait\|></tgt>` | 1005 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一日二日とか</src><tgt><\|wait\|></tgt>` | 1441 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>ですと恐らく</src><tgt><\|wait\|></tgt>` | 823 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 1311 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1557 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1318 |
| 7 | `<src>一定強ぐらいの</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点</tgt>` | `<src>一秒ぐらいの</src><tgt>如果一天两节课的话，大概十秒，也就是一秒左右</tgt>` | 1748 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt><\|wait\|></tgt>` | 1659 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1547 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1661 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐ろしく</src><tgt><\|wait\|></tgt>` | 934 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一日二日</src><tgt><\|wait\|></tgt>` | 1575 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1427 |
| 14 | `<src>あの</src><tgt>这样算。然后十一二手的时候，</tgt>` | `<src>あの</src><tgt>吧。然后，</tgt>` | 1368 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮内馬とかが</src><tgt><\|wait\|></tgt>` | 959 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 422 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 835 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1608 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 655 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1376 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1726 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1720 |
| 7 | `<src>끄는 그대로 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに</tgt>` | `<src>끄는 그대로 </src><tgt>あなたたちも知っているでしょう。異邦人としていた時、言葉を持たない偶像に</tgt>` | 1641 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1969 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 979 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1554 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 2043 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1328 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1039 |
| 14 | `<src>말하는 자는. </src><tgt>連れて行かれました。ですから、あなたがたに教えます。神の霊によって語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>引き寄せられていった。ですから、私があなたたちに告げます。神の霊によって語る者は、</tgt>` | 1502 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 604 |

---

### Test Example 40 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 836 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1352 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 864 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>一个戴雪的人，但是他是</src><tgt><\|wait\|></tgt>` | 1472 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的，</src><tgt><\|wait\|></tgt>` | 1722 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1763 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을</tgt>` | `<src>这通场吗这样的一个状况</src><tgt>이 부분은 눈을 찌르는 사람을 보고 있습니다. 하지만 그는 역방향적인 사람입니다. ' 통장마처럼 ' 이라는 상황이</tgt>` | 3012 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>的，需要去特别</src><tgt><\|wait\|></tgt>` | 1373 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>注意的是</src><tgt><\|wait\|></tgt>` | 1552 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能够</src><tgt><\|wait\|></tgt>` | 1860 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 943 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>于他掉不到</src><tgt><\|wait\|></tgt>` | 1251 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1235 |
| 14 | `<src>的意思哦。</src><tgt>만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는 뜻이거든요.</tgt>` | `<src>于你的益处哦。</src><tgt>있는데, 특별히 주의할 점은 그가 당신에게 이익을 주지 못할까 하는 점입니다.</tgt>` | 1552 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1080 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1162 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 980 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1262 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? Did you </src><tgt><\|wait\|></tgt>` | 1321 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school, </src><tgt><\|wait\|></tgt>` | 1512 |
| 7 | `<src><\|wait\|></src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>that's one level </src><tgt>학력. 당신은 실제로 학업을 얼마나 마쳤나요? 고등학교를 졸업했나요? 그건</tgt>` | 2007 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>of attainment. Did you </src><tgt><\|wait\|></tgt>` | 1985 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>go to college </src><tgt><\|wait\|></tgt>` | 1308 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and, so, did you </src><tgt><\|wait\|></tgt>` | 1697 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>graduate? That's another level </src><tgt><\|wait\|></tgt>` | 2095 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>of attainment. </src><tgt><\|wait\|></tgt>` | 1327 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1300 |
| 14 | `<src>now. I'll see you </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다. 그럼 오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>학력의 한 단계입니다. 대학에 갔나요? 그리고, 그래서, 졸업했나요? 그건 또 다른 단계입니다. 이제 그만으로 할게요.</tgt>` | 1549 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 695 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1096 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1281 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 이제 </src><tgt><\|wait\|></tgt>` | 1304 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>동생 이자 </src><tgt><\|wait\|></tgt>` | 1251 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 </src><tgt><\|wait\|></tgt>` | 1475 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>같은 동생 이잖아 </src><tgt>嗯，怎么说呢，他就是我们20岁那一代的，也是家人，就是个弟弟。</tgt>` | 2108 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1592 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1522 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생 한 거라 는 </src><tgt><\|wait\|></tgt>` | 1725 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1482 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 941 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1384 |
| 14 | `<src>좀 많은 것을 </src><tgt>所以比起责任感，</tgt>` | `<src>좀 많은 거 </src><tgt>所以，嗯，因为是自己重新制作的，所以</tgt>` | 1510 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | 1033 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다 </src><tgt><\|wait\|></tgt>` | 779 |

---

### Test Example 43 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 954 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1428 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 784 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏正财的部分</src><tgt><\|wait\|></tgt>` | 1467 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1645 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>又注意财运方面的</src><tgt><\|wait\|></tgt>` | 1846 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長による</tgt>` | `<src>业绩成果</src><tgt>金運についてですが、今月は悪くないと言えます。ただ、特に正財の部分は、金運の業績成果</tgt>` | 2306 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>带来的红利，</src><tgt><\|wait\|></tgt>` | 1811 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>又收入的提升。</src><tgt><\|wait\|></tgt>` | 1609 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果涉及到投资理财方面</src><tgt><\|wait\|></tgt>` | 438 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>呢，这个月</src><tgt><\|wait\|></tgt>` | 2103 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错的，只是</src><tgt><\|wait\|></tgt>` | 1444 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说，</src><tgt><\|wait\|></tgt>` | 1426 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>ボーナスや昇給の運気が強めです。投資や資産運用についても、悪くはないんですが、本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微弱了一点点</src><tgt>や収入の増加といった恩恵に注意が必要です。投資や資産運用に関しては、今月も悪くないですが、正財に比べると少し弱めです。</tgt>` | 1677 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>。</src><tgt><\|wait\|></tgt>` | 459 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1220 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해 </src><tgt><\|wait\|></tgt>` | 1257 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>엄입니다. </src><tgt><\|wait\|></tgt>` | 931 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전 을 하고 </src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1743 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>간에 </src><tgt><\|wait\|></tgt>` | 1505 |
| 7 | `<src>강북 을 가면 </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北</tgt>` | `<src>막굴러가 면 </src><tgt>进去的时候非常厉害。开车、走路、随便走走，</tgt>` | 1492 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1823 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 </src><tgt><\|wait\|></tgt>` | 1476 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. </src><tgt><\|wait\|></tgt>` | 1583 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 챙겨 야 </src><tgt><\|wait\|></tgt>` | 1874 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1193 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 947 |
| 14 | `<src>열심히 물어봐요. </src><tgt>就不用说了，去外国就更惨了。真有点丢人。不过，我会努力去问路。</tgt>` | `<src>모르 바요. 그거 는 </src><tgt>那更是没法说了。出国的话，又是一场灾难。得好好照顾一下，</tgt>` | 1916 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>나인 것 같아요. </src><tgt><\|wait\|></tgt>` | 644 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 798 |

---

### Test Example 45 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 877 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1308 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1285 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1431 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨설턴트 예요. </src><tgt><\|wait\|></tgt>` | 1657 |
| 7 | `<src><\|wait\|></src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに</tgt>` | `<src>이게 컨설턴트 예요. </src><tgt>ですから、もちろんこういうケースもあります。AさんとBさんがコンサルタントで、これがコンサルタントです。</tgt>` | 2240 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>그리고 A라는 </src><tgt><\|wait\|></tgt>` | 1470 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 1275 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1741 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>들여 쓸 때 </src><tgt><\|wait\|></tgt>` | 2106 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 </src><tgt><\|wait\|></tgt>` | 1373 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스사이트 </src><tgt><\|wait\|></tgt>` | 1356 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、Bさんは実際のクロスサイトスクリプティングから</tgt>` | `<src>크리티에서 </src><tgt>そして、Aさんが悪意のあるコードを仕込むと、Bさんが実際クロスサイトクリティカルで</tgt>` | 1105 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>픽스 파일까지 </src><tgt><\|wait\|></tgt>` | 602 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 46 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉对手的</src><tgt><\|wait\|></tgt>` | 1457 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>感情或</src><tgt><\|wait\|></tgt>` | 803 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真性图片的，</src><tgt><\|wait\|></tgt>` | 1377 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1678 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1533 |
| 7 | `<src>很多时候经常</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、</tgt>` | `<src><\|wait\|></src><tgt>相手の感情や本心を見抜くこと、</tgt>` | 1394 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>后经常会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 2167 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1189 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你看，</src><tgt><\|wait\|></tgt>` | 1554 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1804 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>作谎了，</src><tgt><\|wait\|></tgt>` | 953 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1204 |
| 14 | `<src>已经说明了一切。”</src><tgt>よく耳にするのが「ほら、また嘘をついている。目がすべてを物語っているよ」という言葉です。</tgt>` | `<src>说明了一切。</src><tgt>よく聞く言葉があります。「見て、この人は嘘をついている。その目はすべてを物語っている」</tgt>` | 1727 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 602 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 732 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 491 |

---

### Test Example 47 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1238 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>사인 몰라 빌 거야 </src><tgt><\|wait\|></tgt>` | 999 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 돋든 </src><tgt><\|wait\|></tgt>` | 1464 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>가시 리 돋든 </src><tgt><\|wait\|></tgt>` | 1794 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 너무 야 </src><tgt><\|wait\|></tgt>` | 1845 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。</tgt>` | `<src>이걸 흔들 어서 </src><tgt>目を閉じて、サインを忘れて、昔の虫が這い出てくるような、あの感じを揺さぶって、</tgt>` | 2552 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야 </src><tgt><\|wait\|></tgt>` | 1616 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | 1705 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | 1470 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오면 야 </src><tgt><\|wait\|></tgt>` | 1073 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1554 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주잖아 그러니까 </src><tgt><\|wait\|></tgt>` | 1224 |
| 14 | `<src>편안 한 마음 에 </src><tgt>一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら守ってくれるように突いてくれるから、安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>一緒に遊ぼうってこと。お化けが来たら噛まれて、神様が来たら「守ってくれ」って刺されるんだから、リラックスして</tgt>` | 1795 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 521 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 973 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>상승 하는 흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1012 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1445 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1663 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1827 |
| 7 | `<src>먼저 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>하겠지만 먼저 </src><tgt>If the stock index is on an upward trend, we'll see large- cap stocks rise sharply. But first,</tgt>` | 2209 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1777 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt><\|wait\|></tgt>` | 1301 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 832 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 2264 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1441 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1367 |
| 14 | `<src>가벼운 종목 을 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>가벼운 종목 을 </src><tgt>these smaller stocks move the market first, so</tgt>` | 1096 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨봐야 </src><tgt><\|wait\|></tgt>` | 777 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 572 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=6)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1074 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1408 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 845 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルパイソン開発</src><tgt><\|wait\|></tgt>` | 1443 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>環境なんですね。</src><tgt><\|wait\|></tgt>` | 1657 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも、フローグラフは</src><tgt><\|wait\|></tgt>` | 2006 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>ビジュアルの書いてあと</src><tgt>So, this isn't just a visual development environment; it's a visual Python development environment. Because you write the flow graph visually,</tgt>` | 2692 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それ自体は</src><tgt><\|wait\|></tgt>` | 1359 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>パイソンコードが</src><tgt><\|wait\|></tgt>` | 1711 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成されるってやつで、それが</src><tgt><\|wait\|></tgt>` | 2062 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1388 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 962 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからだ</src><tgt><\|wait\|></tgt>` | 897 |
| 14 | `<src><\|wait\|></src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>なです。</src><tgt>it automatically generates Python code from that, and that code is executed to perform signal processing.</tgt>` | 1249 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 732 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はいじゃあ、</src><tgt><\|wait\|></tgt>` | 568 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 751 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1159 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놨습니다. </src><tgt><\|wait\|></tgt>` | 1069 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠 자의 </src><tgt><\|wait\|></tgt>` | 1404 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1742 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 1823 |
| 7 | `<src>26비트 FP </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビット</tgt>` | `<src>UHD, </src><tgt>これについて多くの人が分析しています。ロクジャの分析を見ると、ソニーは</tgt>` | 1529 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPD 패입을 </src><tgt><\|wait\|></tgt>` | 1673 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1379 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮춘 것을 보여 줍니다. </src><tgt><\|wait\|></tgt>` | 1578 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 </src><tgt><\|wait\|></tgt>` | 2052 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>시리즈 X에서도 없는 </src><tgt><\|wait\|></tgt>` | 1503 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1445 |
| 14 | `<src>인피니트 캐시 </src><tgt>FPパイプを128ビットに下げたようです。</tgt>` | `<src>PSI </src><tgt>UHDFPDインターフェースを128ビットに下げていることがわかります。XboxSeriesXにはないInfinityCachePSIも</tgt>` | 1407 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 843 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 663 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>Fourth of the </src><tgt><\|wait\|></tgt>` | 801 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>month, </src><tgt><\|wait\|></tgt>` | 1035 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>the first day of the month, </src><tgt><\|wait\|></tgt>` | 1210 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but we </src><tgt><\|wait\|></tgt>` | 1306 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1683 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>in our life, </src><tgt><\|wait\|></tgt>` | 1593 |
| 7 | `<src>所谓的爱，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위</tgt>` | `<src>love is the way </src><tgt>4일, 즉 한 달의 첫날이지만, 우리 삶에서 사랑은</tgt>` | 1466 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1805 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>we enter </src><tgt><\|wait\|></tgt>` | 1342 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>into </src><tgt><\|wait\|></tgt>` | 1621 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the time of waiting </src><tgt><\|wait\|></tgt>` | 1783 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>for love. </src><tgt><\|wait\|></tgt>` | 731 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It comes to an end. </src><tgt><\|wait\|></tgt>` | 1580 |
| 14 | `<src>它就变成恨。</src><tgt>사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다.</tgt>` | `<src>It becomes </src><tgt>사랑을 기다리는 시간으로 들어가는 길입니다. 그것은 끝이 납니다.</tgt>` | 1511 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 763 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>the waiting of the empty. </src><tgt><\|wait\|></tgt>` | 829 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt><\|wait\|></tgt>` | 565 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>to end. </src><tgt><\|wait\|></tgt>` | 444 |

---

### Test Example 52 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1279 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 981 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1388 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1803 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1754 |
| 7 | `<src>is is that </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>but the reality is is that </src><tgt>活動、そして自分自身で「標準」を定義することです。なぜなら、あなたは完全に正しいからです。しかし、現実には、</tgt>` | 2351 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on </src><tgt><\|wait\|></tgt>` | 1839 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, and because </src><tgt><\|wait\|></tgt>` | 1685 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have changed, </src><tgt><\|wait\|></tgt>` | 1593 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 882 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>from twenty years ago, </src><tgt><\|wait\|></tgt>` | 1479 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1359 |
| 14 | `<src>a higher standard because </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard </src><tgt>私たちは新しい子なんです。そして、20年前に比べて基準が変わったので、より高い基準を求められています。</tgt>` | 1363 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 849 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to a higher standard </src><tgt><\|wait\|></tgt>` | 743 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also you will not </src><tgt><\|wait\|></tgt>` | 1444 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 812 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>me directly </src><tgt><\|wait\|></tgt>` | 1236 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>objects </src><tgt><\|wait\|></tgt>` | 1367 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | 1392 |
| 7 | `<src>So, if </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果</tgt>` | `<src>So, if </src><tgt>嗯，你也不能直接在资源之间移动对象。所以，</tgt>` | 1557 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into a </src><tgt><\|wait\|></tgt>` | 1349 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation where you </src><tgt><\|wait\|></tgt>` | 1562 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1107 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1512 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | 2272 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>meant to let us know. </src><tgt><\|wait\|></tgt>` | 1521 |
| 14 | `<src>and we can see about </src><tgt>你发现自己给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>Now, and we can see about </src><tgt>如果你发现把错误的媒体文件加到了某个资源上，那我们就知道。现在，</tgt>` | 1847 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those media </src><tgt><\|wait\|></tgt>` | 502 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>files and then making sure </src><tgt><\|wait\|></tgt>` | 829 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 693 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 533 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1285 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 889 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>on the first section </src><tgt><\|wait\|></tgt>` | 1184 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1215 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the HR field </src><tgt><\|wait\|></tgt>` | 1282 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1226 |
| 7 | `<src>being of critical importance </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、</tgt>` | `<src>being of critical importance </src><tgt>HR分野の重要性について、最初のセクションで少し混乱していました。</tgt>` | 1966 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1045 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1371 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, which is obviously </src><tgt><\|wait\|></tgt>` | 1471 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>not my love. </src><tgt><\|wait\|></tgt>` | 1633 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 2013 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1436 |
| 14 | `<src>upon the fields that need </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、</tgt>` | `<src>the fields </src><tgt>バリアントデータベースは、もちろん私の好みではありません。つまり、</tgt>` | 1602 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 940 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 536 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 722 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 778 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 278 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point </src><tgt><\|wait\|></tgt>` | 801 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>in those Jesus </src><tgt><\|wait\|></tgt>` | 1351 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>was hungry, </src><tgt><\|wait\|></tgt>` | 855 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1321 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1749 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1671 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>for forty days that he's hungry, </src><tgt>ある時、イエスは飢えを経験しました。彼は、40日間飢えを過ごす荒野に身を置くことになると知っていました。</tgt>` | 3085 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 1472 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, </src><tgt><\|wait\|></tgt>` | 1602 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the Son of God, prove it </src><tgt><\|wait\|></tgt>` | 2049 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>by the things </src><tgt><\|wait\|></tgt>` | 1234 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>these stones to bread. </src><tgt><\|wait\|></tgt>` | 927 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1085 |
| 14 | `<src>How did Jesus deal with that </src><tgt>で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。イエスは</tgt>` | `<src>just deal with that </src><tgt>そこで彼はイエスに言いました。「もしあなたが神の御子なら、この石をパンに変えてみせなさい」。彼はどうやって</tgt>` | 1716 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>imitation? </src><tgt><\|wait\|></tgt>` | 518 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 568 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lived by </src><tgt><\|wait\|></tgt>` | 326 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>rain alone. </src><tgt><\|wait\|></tgt>` | 388 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1266 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful, </src><tgt><\|wait\|></tgt>` | 944 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1141 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court came </src><tgt><\|wait\|></tgt>` | 1528 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>along last, </src><tgt><\|wait\|></tgt>` | 1666 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I don't want to </src><tgt><\|wait\|></tgt>` | 2095 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为</tgt>` | `<src>give the courts want to be </src><tgt>有意义的、个人的权利，最高法院是最后出面的，而不是引领。我不想让法院</tgt>` | 2170 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the the van </src><tgt><\|wait\|></tgt>` | 1753 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>ard of social change </src><tgt><\|wait\|></tgt>` | 1586 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>engine. </src><tgt><\|wait\|></tgt>` | 457 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days, </src><tgt><\|wait\|></tgt>` | 2065 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but they rather </src><tgt><\|wait\|></tgt>` | 1468 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 1216 |
| 14 | `<src>the consensus </src><tgt>法院现在想成为社会变革的先锋，它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt>成为社会变革的引擎。虽然现在是这样，但它们更多的是反映了</tgt>` | 1030 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 582 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged </src><tgt><\|wait\|></tgt>` | 844 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>soam. </src><tgt><\|wait\|></tgt>` | 502 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 439 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 431 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 369 |
| 21 | `<src>who. </src><tgt>反映已经形成的共识。所以，有些联邦法官……</tgt>` | `<src>who. </src><tgt>已经形成的共识。你还有一些联邦法官，他们……</tgt>` | 431 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1374 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 880 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1467 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是克汀，</src><tgt><\|wait\|></tgt>` | 1755 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>的部分，</src><tgt><\|wait\|></tgt>` | 1737 |
| 7 | `<src>那客厅一般</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통</tgt>` | `<src>那克汀一般都</src><tgt>그럼 사진을 한번 볼까요? 사진 부분에는 크틴이라는 게 보이는데요, 크틴은 보통</tgt>` | 2199 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>是属于我们</src><tgt><\|wait\|></tgt>` | 687 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在修习的</src><tgt><\|wait\|></tgt>` | 1513 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>地方，</src><tgt><\|wait\|></tgt>` | 2013 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>所以呢，是身体的部分</src><tgt><\|wait\|></tgt>` | 1428 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，反映的是</src><tgt><\|wait\|></tgt>` | 1352 |
| 14 | `<src>你需要给自己</src><tgt>우리가 쉬는 곳이잖아요. 그래서 이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt>우리가 수련하는 부분이에요. 그래서 신체 부분은</tgt>` | 972 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 568 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 723 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt><\|wait\|></tgt>` | 610 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们可以看到这边是</src><tgt><\|wait\|></tgt>` | 561 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>双耳人的嘛。</src><tgt><\|wait\|></tgt>` | 444 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 369 |
| 21 | `<src>所以是说。</src><tgt>시간을 내서 편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는 아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>잠시 앉아서 쉬어야 할 때라는 걸 보여줘요. 여기는 쌍이인 거고요. 그래서 말이죠.</tgt>` | 535 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 811 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1282 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 953 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1242 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1477 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>to completely revolutionize the world </src><tgt><\|wait\|></tgt>` | 1483 |
| 7 | `<src><\|wait\|></src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src><\|wait\|></src><tgt>彼らは極めて稀な存在で、世界を完全に変革することがよくあります。</tgt>` | 1751 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>Their personality is something </src><tgt><\|wait\|></tgt>` | 1782 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>that'll contradict </src><tgt><\|wait\|></tgt>` | 1499 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1662 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>while they're extroverted, </src><tgt><\|wait\|></tgt>` | 1891 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1155 |
| 14 | `<src>meaningless conversations </src><tgt>彼らの性格は矛盾しています。外交的である一方、無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations, </src><tgt>外向的であるにもかかわらず、その性格は矛盾しています。また、無意味な会話も嫌い、</tgt>` | 1921 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 606 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to </src><tgt><\|wait\|></tgt>` | 857 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 612 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love to </src><tgt><\|wait\|></tgt>` | 372 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 404 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 505 |
| 21 | `<src><\|wait\|></src><tgt>そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and never shy away </src><tgt>要点をまっすぐ言うタイプです。また、悪魔の代弁者になるのも好きで、</tgt>` | 431 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 287 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 328 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Any VP stands for </src><tgt><\|wait\|></tgt>` | 296 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for </src><tgt><\|wait\|></tgt>` | 310 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>경무를 거부 한 </src><tgt><\|wait\|></tgt>` | 1314 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 761 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1368 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1802 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1873 |
| 7 | `<src>제법 생색까지 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>제법 생색까지 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1059 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1833 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1386 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1642 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1911 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해 놓고. </src><tgt><\|wait\|></tgt>` | 1508 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 1332 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt>and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>떨어뜨리 겠다는 </src><tgt>had put on quite a show, claiming he was running for the candidate's sake when he rejected the nomination. But now, the moment Yoon Suk- yeol removed Kim Jong- in, Lee Jun- seok was already saying he was going to knock down Yoon Suk- yeol.</tgt>` | 2199 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 534 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 568 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 309 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 386 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt><\|wait\|></tgt>` | 432 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 275 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석의 성상납건. </src><tgt>He was determined to show his aggressive intent. Lee Jun- seok's sexual scandal.</tgt>` | 460 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 323 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 303 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 339 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 352 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1066 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | 843 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってるみたいな</src><tgt><\|wait\|></tgt>` | 1138 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>です。なのでここのね</src><tgt><\|wait\|></tgt>` | 663 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>プロフェッショナルホテル</src><tgt><\|wait\|></tgt>` | 1114 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も朝食が</src><tgt><\|wait\|></tgt>` | 1702 |
| 7 | `<src>朝食が食べれる場所</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>食べれる場所</src><tgt>Well, it's like we're making it up as we go. So, the breakfast at this professional hotel</tgt>` | 2756 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1581 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1595 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | 1675 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 539 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいなって</src><tgt><\|wait\|></tgt>` | 1975 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>いう方はですね</src><tgt><\|wait\|></tgt>` | 1429 |
| 14 | `<src>検討なさってみて</src><tgt>is also planning to have breakfast available. So, for anyone thinking about staying here in the future,</tgt>` | `<src>検討なさってみて</src><tgt>is a place where you can have breakfast. So, if you're thinking of staying at the Goldston Hotel here in the future,</tgt>` | 2104 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>まあいいんじゃない</src><tgt><\|wait\|></tgt>` | 584 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なとはい。</src><tgt><\|wait\|></tgt>` | 723 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。ここ</src><tgt><\|wait\|></tgt>` | 588 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>のホテルからですね</src><tgt><\|wait\|></tgt>` | 518 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 418 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 341 |
| 21 | `<src>歩いて一分</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>一分かかる</src><tgt>I think it's a good idea to consider it. From this hotel, you can walk to Busan Station in just a minute,</tgt>` | 616 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんないか</src><tgt><\|wait\|></tgt>` | 310 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 390 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>リッチのねまあホテル</src><tgt><\|wait\|></tgt>` | 267 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 309 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 292 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 206 |
| 28 | `<src>ください</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good. If you'd like, please consider it.</tgt>` | `<src>ください</src><tgt>so it's a really convenient hotel. So please give it a try.</tgt>` | 267 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね</src><tgt><\|wait\|></tgt>` | 203 |
