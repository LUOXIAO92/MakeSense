# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9443
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5033
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.0000
  - TGT_RELEASE_TOTAL: 0
  - TGT_WAIT_ACCURACY: 0.0000
  - TGT_WAIT_TOTAL: 0
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1473.0530
  - PROCESS_TIME_MS_P50: 1472.8700
  - PROCESS_TIME_MS_P95: 2429.6790
  - PROCESS_TIME_MS_MAX: 2962.3520

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>为什么</src>` | 2162 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>得送子儿</src>` | 916 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这样子呢？这个收益很大，</src>` | 1608 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1509 |
| 5 | `<src><\|wait\|></src>` | `<src>那</src>` | 1187 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在另一方面</src>` | 608 |
| 7 | `<src>儿核桃</src>` | `<src>和陶渊</src>` | 1882 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1449 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>在一起</src>` | 1003 |
| 10 | `<src>这种核桃</src>` | `<src>这样这种</src>` | 1663 |
| 11 | `<src>仁儿。</src>` | `<src>和陶渊。</src>` | 2460 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1654 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 897 |
| 3 | `<src>これなんかまだ</src>` | `<src>子供がまだ</src>` | 1267 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね</src>` | 1801 |
| 5 | `<src>この時点で</src>` | `<src>この時点でこう</src>` | 1263 |
| 6 | `<src>こう短く</src>` | `<src>美しく</src>` | 1142 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1343 |
| 8 | `<src><\|wait\|></src>` | `<src>こうタイズして</src>` | 1535 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>あげると</src>` | 1475 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 1343 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 2224 |

---

### Test Example 3 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1934 |
| 2 | `<src>옹심이, </src>` | `<src><\|wait\|></src>` | 1027 |
| 3 | `<src><\|wait\|></src>` | `<src>봉심이 칼 </src>` | 1202 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>봉심이지 </src>` | 1831 |
| 5 | `<src>옹심이가 </src>` | `<src>봉심이가 </src>` | 1184 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1624 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이는 건데요. </src>` | 1325 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1087 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1641 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해당 으로 </src>` | 1857 |
| 11 | `<src>진짜. </src>` | `<src>조금 움직임 같은 거죠. </src>` | 1811 |

---

### Test Example 4 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1862 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1440 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 866 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 2146 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 845 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们笑这个状况，</src>` | 1916 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1474 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>怎么都把它扛下来，</src>` | 911 |
| 9 | `<src>独立承担。</src>` | `<src>你不利沉担，</src>` | 1841 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言</src>` | 2553 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该就是Solution。</src>` | 583 |

---

### Test Example 5 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2120 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1447 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 996 |
| 4 | `<src>用我们深深的</src>` | `<src><\|wait\|></src>` | 1776 |
| 5 | `<src>爱浇水、</src>` | `<src>深深的爱浇水，</src>` | 1133 |
| 6 | `<src>施肥，</src>` | `<src>所以</src>` | 1882 |
| 7 | `<src>给足</src>` | `<src><\|wait\|></src>` | 1525 |
| 8 | `<src>孩子心理营养，</src>` | `<src>给足孩子心灵营养，</src>` | 884 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1917 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>给耐心等他</src>` | 2648 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 964 |

---

### Test Example 6 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1982 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1713 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 981 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有一个师傅</src>` | 1677 |
| 5 | `<src><\|wait\|></src>` | `<src>指导道，</src>` | 906 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 2005 |
| 7 | `<src>处于中间，</src>` | `<src>如何趋于中间，</src>` | 1837 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1195 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1496 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 2427 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅，</src>` | 1203 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2031 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘沙完以后呢，</src>` | 1572 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻了</src>` | 1219 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也虽然</src>` | 1556 |
| 5 | `<src>然后</src>` | `<src>弱了，</src>` | 907 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 2400 |
| 7 | `<src>相对的低</src>` | `<src><\|wait\|></src>` | 1457 |
| 8 | `<src>能量的运行</src>` | `<src>一个相对的低能量的</src>` | 1741 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 1847 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1662 |
| 11 | `<src>抑郁状态。</src>` | `<src>易于状态。</src>` | 1407 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2196 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1098 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1051 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 2058 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1036 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 2791 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1293 |
| 8 | `<src>때문 입니다. </src>` | `<src>였기 때문 입니다. </src>` | 1730 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2547 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 791 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은 </src>` | 1368 |

---

### Test Example 9 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2120 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 975 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1184 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも用意しております</src>` | 1924 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので</src>` | 1098 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 686 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1657 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1576 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1227 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1602 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>何しろ内側がありますので</src>` | 2442 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1430 |

---

### Test Example 10 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1790 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptroller, </src>` | 1181 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽팔리 시키고 </src>` | 1580 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1666 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 914 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 2454 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>헬레나 </src>` | 1461 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1624 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1527 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들은 </src>` | 2062 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>이다. </src>` | 1442 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying important </src>` | 1823 |
| 2 | `<src>Did very important research </src>` | `<src>research </src>` | 962 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1180 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 2070 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem, </src>` | 1096 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 2330 |
| 7 | `<src>looking at the ten percent </src>` | `<src>a 10% </src>` | 1562 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1608 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1367 |
| 10 | `<src>out there, </src>` | `<src>out there, people like </src>` | 2217 |
| 11 | `<src>people that we can learn from. </src>` | `<src>what we can learn from. </src>` | 1656 |

---

### Test Example 12 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1781 |
| 2 | `<src>映画でですね、</src>` | `<src>AAアンデスに</src>` | 912 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1268 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>円生速度が</src>` | 1785 |
| 5 | `<src>調べるときに、</src>` | `<src>どうかっていう場面</src>` | 1284 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>でAの乱交調べ</src>` | 1523 |
| 7 | `<src>ことで、あの</src>` | `<src>ということであの</src>` | 948 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生生速度が</src>` | 1679 |
| 9 | `<src>保証する、生息である</src>` | `<src>等しい生速度である</src>` | 1749 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 2542 |
| 11 | `<src>といったような</src>` | `<src>といってあの使い方を</src>` | 892 |
| 12 | `<src>使い方をされます。</src>` | `<src>されます。</src>` | 1762 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1907 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜을 </src>` | 1280 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 2370 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주길 넣어두고 내가 주길 넣어두고 </src>` | 1529 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜을 </src>` | 741 |
| 6 | `<src>죽여 달라 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 2224 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>안되나 내가 </src>` | 1234 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>이런 소리 안 듣고 </src>` | 1818 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐 </src>` | 2918 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아 </src>` | 483 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1950 |

---

### Test Example 14 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1717 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1091 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1088 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1864 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1168 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 2163 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1731 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1896 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 2461 |
| 10 | `<src><\|wait\|></src>` | `<src>language are you </src>` | 1020 |
| 11 | `<src>language are you using? </src>` | `<src>using? </src>` | 2145 |

---

### Test Example 15 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2009 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1026 |
| 3 | `<src>始めた</src>` | `<src>始めたもので、</src>` | 1189 |
| 4 | `<src>もので、</src>` | `<src><\|wait\|></src>` | 1753 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 1268 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1521 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1039 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1597 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1651 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の絵</src>` | 2504 |
| 11 | `<src>は、田舎の</src>` | `<src><\|wait\|></src>` | 1037 |
| 12 | `<src>中学生でも。</src>` | `<src>は田舎の中学生でも</src>` | 2231 |

---

### Test Example 16 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2153 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1128 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1171 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to dance, </src>` | 1921 |
| 5 | `<src>Find what you're good at </src>` | `<src>repeat, find what you're good at, </src>` | 1141 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 2033 |
| 7 | `<src><\|wait\|></src>` | `<src>And when you're not good </src>` | 1829 |
| 8 | `<src>And what you're not good at, </src>` | `<src>at dance, </src>` | 1631 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get to people around you to help you with </src>` | 2421 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1222 |
| 11 | `<src>And until next time. </src>` | `<src>and and tell next time. </src>` | 2351 |

---

### Test Example 17 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 요걸지 </src>` | 1999 |
| 2 | `<src><\|wait\|></src>` | `<src>너무 이 저열하는 </src>` | 1267 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>일 수 있지만 </src>` | 1122 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 2004 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 878 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 프로 </src>` | 2737 |
| 7 | `<src>뭐 있고 </src>` | `<src>하고 있고 나만 </src>` | 1319 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>뒤 보살 로 </src>` | 1710 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 프로 하고 있어요 우주 가 </src>` | 2962 |
| 10 | `<src>지금 나한테 </src>` | `<src>이제 나한테 보살 이란 </src>` | 675 |
| 11 | `<src>보살 이라는데. </src>` | `<src>그냥. </src>` | 2136 |

---

### Test Example 18 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1812 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1113 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1095 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 2010 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1093 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1962 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1596 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, like </src>` | 878 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light, </src>` | 1883 |
| 10 | `<src><\|wait\|></src>` | `<src>or gets used </src>` | 2477 |
| 11 | `<src>or gets used to make </src>` | `<src>to make </src>` | 584 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 2162 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1761 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1275 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人之间</src>` | 2375 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 800 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>有着某种联系，</src>` | 892 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1956 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1702 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里</src>` | 1022 |
| 9 | `<src><\|wait\|></src>` | `<src>开始的？</src>` | 1742 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2443 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 897 |
| 12 | `<src>连篇。</src>` | `<src>连篇，</src>` | 1941 |

---

### Test Example 20 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1826 |
| 2 | `<src><\|wait\|></src>` | `<src>涉及到</src>` | 829 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二classList</src>` | 1145 |
| 4 | `<src>服务</src>` | `<src>和父</src>` | 1722 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 806 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 923 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说</src>` | 1742 |
| 8 | `<src><\|wait\|></src>` | `<src>在做维向</src>` | 1651 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>运动好事几点，你会</src>` | 875 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 1728 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维向运动好拼分的</src>` | 2863 |
| 12 | `<src>的新榜反而</src>` | `<src>辛膀反而</src>` | 1052 |
| 13 | `<src>火了。</src>` | `<src>活了。</src>` | 1764 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1697 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到</src>` | 958 |
| 3 | `<src>回到我生活</src>` | `<src>我生活的一个轨道，</src>` | 1251 |
| 4 | `<src>的一个轨道哈，</src>` | `<src><\|wait\|></src>` | 1796 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1170 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好自在的</src>` | 1514 |
| 7 | `<src>在做热汤</src>` | `<src>时候在做热汤</src>` | 1364 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃的，</src>` | 1408 |
| 9 | `<src><\|wait\|></src>` | `<src>就这么个</src>` | 1810 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我只是备餐的时候一个</src>` | 2930 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望哈，</src>` | 1141 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 1810 |

---

### Test Example 22 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだん</src>` | 2244 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が</src>` | 1230 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1445 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>おしゃれルカだけがね</src>` | 1934 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 668 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊したい方って</src>` | 2346 |
| 7 | `<src>すごい</src>` | `<src>すごい居心地高い</src>` | 1471 |
| 8 | `<src>自己意識高いし、</src>` | `<src>し、</src>` | 1483 |
| 9 | `<src>自分で</src>` | `<src>居心地がいいと</src>` | 1471 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>多分次に</src>` | 2165 |
| 11 | `<src>傾向が強いので、</src>` | `<src>遊ぶと喋る力強いので</src>` | 1245 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1848 |

---

### Test Example 23 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1882 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 896 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1327 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1726 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 1259 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 507 |
| 7 | `<src>大概有十位医生</src>` | `<src>十位医生</src>` | 1980 |
| 8 | `<src>来诊断，</src>` | `<src>来侦断，</src>` | 1499 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿、</src>` | 1543 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 1459 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 2151 |
| 12 | `<src>他们</src>` | `<src>他们都很疑惑。</src>` | 1235 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>我才离开。</src>` | 2034 |

---

### Test Example 24 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1807 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 825 |
| 3 | `<src><\|wait\|></src>` | `<src>天気で</src>` | 1112 |
| 4 | `<src>テキという設備寺が</src>` | `<src>と設備が</src>` | 1774 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 737 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 884 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2138 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井青氏の仕組み</src>` | 1813 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 1618 |
| 10 | `<src>は五経、</src>` | `<src>もうこんな</src>` | 1515 |
| 11 | `<src><\|wait\|></src>` | `<src>設備</src>` | 1946 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 1332 |
| 13 | `<src>です。</src>` | `<src>ゴビです。</src>` | 2022 |

---

### Test Example 25 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2204 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1266 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1298 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1647 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1015 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1795 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1230 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 968 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1638 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1862 |
| 11 | `<src><\|wait\|></src>` | `<src>So this </src>` | 1667 |
| 12 | `<src>this game dot scored array. </src>` | `<src>game dot sort array </src>` | 1465 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2028 |

---

### Test Example 26 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1917 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Finnehatelu, </src>` | 1425 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1265 |
| 4 | `<src><\|wait\|></src>` | `<src>in IT, </src>` | 1671 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>Business Finance, </src>` | 897 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology. </src>` | 2636 |
| 7 | `<src><\|wait\|></src>` | `<src>I hear </src>` | 1298 |
| 8 | `<src>here at the ANU, </src>` | `<src>that you're in </src>` | 1729 |
| 9 | `<src><\|wait\|></src>` | `<src>in </src>` | 1795 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>the future. I want to go into </src>` | 1832 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate consultancy </src>` | 1876 |
| 12 | `<src>corporate consultancy. </src>` | `<src>and. </src>` | 1447 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2182 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1123 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment </src>` | 1558 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1750 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 891 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1769 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1369 |
| 8 | `<src>change can happen </src>` | `<src><\|wait\|></src>` | 888 |
| 9 | `<src>in the United States. </src>` | `<src>happen in the United States. </src>` | 1906 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2590 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 635 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 1931 |
| 13 | `<src>myriad. </src>` | `<src>I'm Maryed. </src>` | 1666 |

---

### Test Example 28 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2114 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 857 |
| 3 | `<src>ギアが</src>` | `<src>ギアです。ギアが</src>` | 1370 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 2068 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなって</src>` | 1077 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 2203 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1491 |
| 8 | `<src>役ねじの</src>` | `<src>ヤクネ字の</src>` | 1326 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1473 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いているっていうこと</src>` | 2454 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 1105 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1864 |
| 13 | `<src>分解完了。</src>` | `<src>はい分解を。</src>` | 1474 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家</src>` | 2020 |
| 2 | `<src>要提醒大家，</src>` | `<src>呢，</src>` | 977 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1191 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是意味着</src>` | 1751 |
| 5 | `<src>所以呢，</src>` | `<src>造成了所以呢，</src>` | 1316 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1578 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1099 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊</src>` | 1313 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 1497 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你事业之间就</src>` | 1743 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1897 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来</src>` | 1268 |
| 13 | `<src>因此会建议</src>` | `<src>的因此会建议</src>` | 2005 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1467 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1851 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 1810 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 인슐린과 </src>` | 2037 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 1308 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 </src>` | 1286 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1460 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 1427 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1754 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2284 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 를 좀 해 요. </src>` | 1174 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2154 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1942 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 965 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1728 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，</src>` | 1430 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 869 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 2070 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 954 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1947 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1700 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想着哎，那我再继续</src>` | 1038 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1613 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>操作下去哦，</src>` | 2583 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1130 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1810 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1526 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1039 |

---

### Test Example 32 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you have </src>` | 1974 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 1084 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1085 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1873 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1155 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 2663 |
| 7 | `<src>to spell </src>` | `<src><\|wait\|></src>` | 1318 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>how to spell the words. Like, oh, </src>` | 2052 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2590 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 679 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2219 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't know </src>` | 2146 |
| 13 | `<src>know. </src>` | `<src>it. </src>` | 1054 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>第一张的部分</src>` | 1776 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们看到的是</src>` | 1134 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1312 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1635 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的</src>` | 1206 |
| 6 | `<src>所以</src>` | `<src>。这种场景</src>` | 2118 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>吗这样的一个状况呢？</src>` | 1797 |
| 8 | `<src>时候，就要去</src>` | `<src>需要我们就要去</src>` | 1625 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意的是，</src>` | 1352 |
| 10 | `<src>是它能不能够</src>` | `<src>它能不能够</src>` | 2192 |
| 11 | `<src>钓到鱼，</src>` | `<src>得到与它</src>` | 1293 |
| 12 | `<src>它钓不到鱼</src>` | `<src>钓不到</src>` | 1977 |
| 13 | `<src><\|wait\|></src>` | `<src>与你的意识</src>` | 1337 |
| 14 | `<src>的意思哦。</src>` | `<src>一样。</src>` | 983 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1727 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>백 오십만 개가 중화 벌고서 </src>` | 1926 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>연평 이만 으로 </src>` | 1948 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1315 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 862 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1873 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 1582 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 해외 에 </src>` | 1681 |
| 9 | `<src>걷게 되는데 </src>` | `<src>익을 꺾게 되는데 </src>` | 2940 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 에 상기 </src>` | 705 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>업들은 성장 도 </src>` | 2076 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>패 업도 하지 않을 </src>` | 1791 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1298 |

---

### Test Example 35 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1943 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1393 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不好的，但是</src>` | 1266 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src><\|wait\|></src>` | 1674 |
| 5 | `<src>也就是</src>` | `<src>比较正财的部分，也就是</src>` | 974 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面</src>` | 1710 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>的业绩增长是</src>` | 1416 |
| 8 | `<src>与收入的</src>` | `<src>不太好的，属于</src>` | 999 |
| 9 | `<src>提升。如果是在</src>` | `<src>收入的提升。如果</src>` | 1796 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面</src>` | 2766 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 559 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不足，</src>` | 2019 |
| 13 | `<src>相对正财来说就</src>` | `<src>只是相对整体来说，就</src>` | 1740 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微若了一点点</src>` | 1263 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1172 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>授業</src>` | 1928 |
| 2 | `<src>十一二手とか</src>` | `<src>一日二日とか</src>` | 848 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 1193 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1896 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 964 |
| 6 | `<src>一秒に</src>` | `<src>一日一に</src>` | 508 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一今日ぐらいの</src>` | 2337 |
| 8 | `<src>計算ですか</src>` | `<src>してたんですかね。</src>` | 1468 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 1535 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1404 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2114 |
| 12 | `<src><\|wait\|></src>` | `<src>一日二日</src>` | 1247 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1807 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1429 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1190 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 1068 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1745 |
| 2 | `<src>HTML이라고 </src>` | `<src>而h期望</src>` | 1151 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1166 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>里라고 하는 컴퓨터 도 이해 할 수 </src>` | 2339 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 680 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 </src>` | 1804 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1621 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 888 |
| 9 | `<src>문법 에 </src>` | `<src><\|wait\|></src>` | 1828 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>문법 의 뭐랄게 우리 가 이제 </src>` | 2909 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 </src>` | 1246 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 2050 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1330 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1023 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1044 |

---

### Test Example 38 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1948 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1240 |
| 3 | `<src><\|wait\|></src>` | `<src>There was such </src>` | 1177 |
| 4 | `<src>such interfaces before, </src>` | `<src>interest before, </src>` | 1777 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1021 |
| 6 | `<src>netfilter, TC. </src>` | `<src>and future TC </src>` | 2043 |
| 7 | `<src>Yeah, so </src>` | `<src><\|wait\|></src>` | 1708 |
| 8 | `<src>this is just </src>` | `<src>is just </src>` | 1096 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1704 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2437 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1248 |
| 12 | `<src><\|wait\|></src>` | `<src>But develop </src>` | 1855 |
| 13 | `<src>developers or engineers </src>` | `<src>or engineers were </src>` | 1419 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on bug reports should be </src>` | 1230 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1092 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1790 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1595 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1105 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1745 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 874 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하 는 우상에게로 </src>` | 2432 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1465 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 1818 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2123 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1265 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1243 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 2018 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1507 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 960 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 940 |

---

### Test Example 40 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2136 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1231 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1174 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1628 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1188 |
| 6 | `<src>that I think are </src>` | `<src>that I think </src>` | 2025 |
| 7 | `<src>really important. </src>` | `<src>are really important. </src>` | 1700 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1025 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 1904 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 2318 |
| 11 | `<src>one minute videos </src>` | `<src>I have about one minute videos </src>` | 1248 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 2068 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one. </src>` | 1442 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1117 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>In a little more detail, </src>` | 1072 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2038 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう蒸らせてあれ、</src>` | 1052 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1139 |
| 4 | `<src><\|wait\|></src>` | `<src>今ひきてる</src>` | 1800 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>見てる。</src>` | 1238 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 608 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1890 |
| 8 | `<src><\|wait\|></src>` | `<src>とうに超えてる</src>` | 1578 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>船の奇跡よ。</src>` | 1804 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2254 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1115 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなでいくを</src>` | 1333 |
| 13 | `<src>が、</src>` | `<src>やってるが、</src>` | 2039 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1598 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 980 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 915 |

---

### Test Example 42 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수가 </src>` | 1904 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 1094 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 1567 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이러 다행 주도 </src>` | 1863 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 762 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 </src>` | 1705 |
| 7 | `<src>먼저 </src>` | `<src>하겠지만 </src>` | 1027 |
| 8 | `<src>이 가벼운 </src>` | `<src>먼저 가벼운 </src>` | 1387 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1747 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2681 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 635 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이기 때문 에 </src>` | 1667 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 시총이 </src>` | 1751 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1577 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 1123 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 802 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2042 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment: </src>` | 1142 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1327 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1546 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 1256 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 2660 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1459 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you </src>` | 1715 |
| 9 | `<src>to college, </src>` | `<src>go to college? </src>` | 2629 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, did you </src>` | 825 |
| 11 | `<src>That's another level of </src>` | `<src>graduate? </src>` | 1986 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 1803 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now. </src>` | 1366 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you </src>` | 1224 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 851 |

---

### Test Example 44 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 2135 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어, 어찌 보면 </src>` | 1330 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1494 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 또래 </src>` | 1754 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>생명이자 그래도 </src>` | 778 |
| 6 | `<src>그래도 가족 </src>` | `<src>가족 같은 </src>` | 1880 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>동생 이잖아. </src>` | 1765 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 618 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1825 |
| 10 | `<src>책임감 보다는 </src>` | `<src>어 책임감 보다는 </src>` | 2759 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 786 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1887 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1806 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 것을 </src>` | 950 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1240 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1199 |

---

### Test Example 45 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 간고 </src>` | 2201 |
| 2 | `<src><\|wait\|></src>` | `<src>새 못 알아 </src>` | 993 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 1179 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 </src>` | 2059 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋든 자식 이 돋든 </src>` | 1141 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>내 기명응이야. 이게 </src>` | 2712 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>걸 흔들 어서 </src>` | 1425 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1877 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 </src>` | 2618 |
| 10 | `<src>물릴 거고 </src>` | `<src>어미 를 밀릴 거고 </src>` | 612 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 어미야. </src>` | 2108 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1952 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주라니까 </src>` | 1146 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1266 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 간다. </src>` | 1029 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어 가면 </src>` | 2135 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 해맨입니다. </src>` | 1329 |
| 3 | `<src>운전 을 </src>` | `<src>이 운전을 </src>` | 1181 |
| 4 | `<src><\|wait\|></src>` | `<src>하려고 은 </src>` | 1552 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>거러 거러 다 </src>` | 1239 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>이 공감 에 뭐 </src>` | 1861 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 1486 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 907 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장려 리예요. </src>` | 1971 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 2402 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>튕기 아네요. </src>` | 698 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 2194 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1897 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모르 바요. 그거 는 </src>` | 1147 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>내일 있는 것 같아요. </src>` | 1267 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1023 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1986 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1247 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1551 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, because you're </src>` | 2117 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 398 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1898 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 1462 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1197 |
| 9 | `<src>block and because the </src>` | `<src>block, and because this </src>` | 1865 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 2443 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1287 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1953 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1466 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1060 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point is being </src>` | 1143 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 1033 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2066 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手的</src>` | 1411 |
| 3 | `<src>的感情或</src>` | `<src>感情或</src>` | 866 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 2066 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 908 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1789 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 1192 |
| 8 | `<src>会听到人们</src>` | `<src>好经常会听到人们这样说：</src>` | 1329 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1728 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2665 |
| 11 | `<src>这个人</src>` | `<src>这个人又在</src>` | 571 |
| 12 | `<src>又在说谎了，</src>` | `<src>说谎了，</src>` | 1979 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1465 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1538 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1239 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 812 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 584 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2069 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1396 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうだけじゃなくて、</src>` | 1257 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1670 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 999 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローグラフは</src>` | 2303 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 1691 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあとはPythonコード</src>` | 1677 |
| 9 | `<src>にそこから</src>` | `<src>が</src>` | 1911 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成されて、それが</src>` | 1572 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 2028 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるっていう</src>` | 1711 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているから</src>` | 1292 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1214 |
| 15 | `<src>はい。</src>` | `<src>ですね。</src>` | 811 |
| 16 | `<src>じゃあ。</src>` | `<src>はい。じゃあ、</src>` | 646 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1677 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1142 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놨습니다. </src>` | 1692 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠 자의 </src>` | 1745 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 788 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1872 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 칩의 </src>` | 1662 |
| 8 | `<src>파이프 를 </src>` | `<src>FP 파이프 를 </src>` | 749 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2101 |
| 10 | `<src>것으로 보인다. </src>` | `<src>나중 에서 로프인다. </src>` | 2637 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1686 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈 엑스에서도 없는 </src>` | 2077 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1399 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 M3가 </src>` | 1406 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>여기 도 없다. </src>` | 1011 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 274 |

---

### Test Example 51 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 2028 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 919 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 1596 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1780 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1085 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨턴트예요. </src>` | 2359 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트 가 </src>` | 1670 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>여기 있고, A라는 </src>` | 1753 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 2296 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1180 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>줬을 때 </src>` | 2098 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1880 |
| 13 | `<src>실제 </src>` | `<src>실제 크로스사이트 </src>` | 1171 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>CT에서 </src>` | 1153 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>계시 파일까지 </src>` | 905 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 456 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1773 |
| 2 | `<src>首次觉知到</src>` | `<src>佛罗伊的寿子觉知道</src>` | 1838 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象，</src>` | 1774 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 808 |
| 5 | `<src><\|wait\|></src>` | `<src>美登我们处于</src>` | 880 |
| 6 | `<src>处于爱之中，</src>` | `<src>爱之中</src>` | 1804 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱。</src>` | 1355 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 895 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入</src>` | 1691 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2430 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨在早上的时候，</src>` | 1020 |
| 12 | `<src>它是爱；</src>` | `<src>他撒爱，</src>` | 2105 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1839 |
| 14 | `<src>它就变成恨。</src>` | `<src>他就变成</src>` | 1075 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1149 |
| 16 | `<src>那个钟摆</src>` | `<src>恨那个中百，</src>` | 889 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 616 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 504 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1986 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 978 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to move </src>` | 1483 |
| 4 | `<src>move media objects </src>` | `<src>me directly. </src>` | 1622 |
| 5 | `<src><\|wait\|></src>` | `<src>Objects between the </src>` | 1177 |
| 6 | `<src>between the resources. </src>` | `<src>resources. </src>` | 2158 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1579 |
| 8 | `<src>you get into </src>` | `<src>you get into a </src>` | 903 |
| 9 | `<src>a situation </src>` | `<src>situation where you </src>` | 1749 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2645 |
| 11 | `<src>you've added the wrong media </src>` | `<src><\|wait\|></src>` | 1211 |
| 12 | `<src>files to a particular resource, </src>` | `<src>the wrong media files </src>` | 2019 |
| 13 | `<src>you need to let us know, </src>` | `<src>to a particular resource, and that is, now </src>` | 1762 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1083 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 910 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files </src>` | 872 |
| 17 | `<src>get backed up </src>` | `<src>and then making sure they get backed up </src>` | 540 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 572 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2283 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 933 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1207 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1791 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the HR field </src>` | 1227 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1515 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1199 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 1229 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1395 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 1447 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously the one of my loves. </src>` | 2551 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if you </src>` | 1894 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>don't agree upon </src>` | 1483 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 1477 |
| 15 | `<src>to be in these </src>` | `<src>to be in these data </src>` | 1207 |
| 16 | `<src>data sources that we can </src>` | `<src>sources that we can </src>` | 712 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 900 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 513 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 545 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1772 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1087 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1168 |
| 4 | `<src>He knows that </src>` | `<src>He knows that he's </src>` | 2148 |
| 5 | `<src>he's been without food, </src>` | `<src>good, </src>` | 830 |
| 6 | `<src><\|wait\|></src>` | `<src>that for He's in the wilderness, </src>` | 2642 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>body is hungry. </src>` | 1427 |
| 8 | `<src>And so he says </src>` | `<src>And so he says to </src>` | 1692 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 2242 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it </src>` | 1305 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2070 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>turn these stones to bread. </src>` | 2014 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1038 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>say to deal with </src>` | 1154 |
| 15 | `<src>temptation? </src>` | `<src>that temptation? </src>` | 758 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 569 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lived by </src>` | 497 |
| 18 | `<src>by bread alone. </src>` | `<src>rain alone. </src>` | 571 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1941 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片</src>` | 1135 |
| 3 | `<src><\|wait\|></src>` | `<src>哦，</src>` | 1039 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 1853 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1222 |
| 6 | `<src>的部分。</src>` | `<src>客厅的部分，</src>` | 1690 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般都会</src>` | 1213 |
| 8 | `<src>都是属于</src>` | `<src>是属于</src>` | 1196 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 1488 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 1642 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 1935 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的部分</src>` | 1335 |
| 13 | `<src>也会反映的是</src>` | `<src>会反映的是</src>` | 2057 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1496 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 928 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 968 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 931 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 368 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 251 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 518 |
| 21 | `<src>所以是说。</src>` | `<src>所以意思是说。</src>` | 328 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2233 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1149 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1028 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1842 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1174 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1632 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1943 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 798 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1759 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2671 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 588 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1960 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1585 |
| 14 | `<src>the consensus </src>` | `<src><\|wait\|></src>` | 1400 |
| 15 | `<src><\|wait\|></src>` | `<src>the consensus </src>` | 1061 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 983 |
| 17 | `<src><\|wait\|></src>` | `<src>So, </src>` | 610 |
| 18 | `<src>So you have some </src>` | `<src>you have some </src>` | 498 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 517 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 346 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 278 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1800 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1262 |
| 3 | `<src>and they often </src>` | `<src><\|wait\|></src>` | 1168 |
| 4 | `<src>show up to </src>` | `<src>and they often show up </src>` | 1991 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 865 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 2608 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1424 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1596 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 2217 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 1262 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1316 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 2028 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1517 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations, </src>` | 947 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 880 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to the </src>` | 1034 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 449 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 172 |
| 19 | `<src>play </src>` | `<src><\|wait\|></src>` | 506 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>play the devil's advocate, </src>` | 335 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 241 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 229 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 295 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. stands for </src>` | 307 |
| 25 | `<src>ENTP stands for </src>` | `<src>strong. </src>` | 286 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1876 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>정무를 거부 한 </src>` | 1395 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보를 </src>` | 2197 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 921 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 805 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1855 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1777 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1327 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1652 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2405 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1617 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 드러내 놓고 </src>` | 1907 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 를 </src>` | 1608 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1180 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 865 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 609 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 498 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 508 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 339 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 263 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 청상답군 </src>` | 301 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 296 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 257 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 학이 얼마나 </src>` | 320 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 272 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2003 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今</src>` | 913 |
| 3 | `<src>今作ってる</src>` | `<src>作ってみたいなの</src>` | 1312 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>で、ここのね</src>` | 1921 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>もっとすごい人のホテル</src>` | 1181 |
| 6 | `<src>も</src>` | `<src>で朝食が</src>` | 1970 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 1527 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 740 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1690 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2439 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドーストーンホテル</src>` | 920 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいなと</src>` | 1911 |
| 13 | `<src>なっていう方はですね</src>` | `<src>いう方はですね</src>` | 1533 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1520 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>まあいいんじゃないか</src>` | 1174 |
| 16 | `<src><\|wait\|></src>` | `<src>なと、はい。</src>` | 871 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。ここ</src>` | 628 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね</src>` | 511 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 532 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 332 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 253 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかからないか</src>` | 261 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 322 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあホテル</src>` | 262 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 289 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 249 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 173 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 143 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね、今回は。</src>` | 150 |
