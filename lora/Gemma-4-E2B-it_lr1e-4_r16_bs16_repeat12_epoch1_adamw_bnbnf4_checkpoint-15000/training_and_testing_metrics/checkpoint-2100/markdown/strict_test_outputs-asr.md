# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9777
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.2252
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
  - PROCESS_TIME_MS_AVG: 1447.7340
  - PROCESS_TIME_MS_P50: 1392.9000
  - PROCESS_TIME_MS_P95: 2425.9110
  - PROCESS_TIME_MS_MAX: 3188.6340

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
| 1 | `<src><\|wait\|></src>` | `<src>为什么</src>` | 2042 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>在这里，</src>` | 865 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个营收</src>` | 1290 |
| 4 | `<src>然后</src>` | `<src>也很大，然后</src>` | 1008 |
| 5 | `<src><\|wait\|></src>` | `<src>那</src>` | 1241 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在面对</src>` | 1270 |
| 7 | `<src>儿核桃</src>` | `<src>和陶人，</src>` | 1265 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1138 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉</src>` | 2065 |
| 10 | `<src>这种核桃</src>` | `<src>这些</src>` | 934 |
| 11 | `<src>仁儿。</src>` | `<src>和陶人。</src>` | 2552 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要气鼠，</src>` | 1953 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>是容易的。</src>` | 1106 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1770 |
| 4 | `<src>只有一个师父</src>` | `<src>只有</src>` | 453 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导，</src>` | 1356 |
| 6 | `<src>知道如何</src>` | `<src>如喝出鱼</src>` | 1092 |
| 7 | `<src>处于中间，</src>` | `<src>中边，</src>` | 1302 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2061 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 950 |
| 10 | `<src>要成为</src>` | `<src>要成为一个</src>` | 1434 |
| 11 | `<src>一个师父。</src>` | `<src>师傅，</src>` | 2465 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1622 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1136 |
| 3 | `<src>これなんかまだ</src>` | `<src>村中まだ</src>` | 1879 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1377 |
| 5 | `<src>この時点で</src>` | `<src>その時点で</src>` | 1212 |
| 6 | `<src>こう短く</src>` | `<src>こう密告</src>` | 926 |
| 7 | `<src>剪定を</src>` | `<src>前提を</src>` | 1406 |
| 8 | `<src><\|wait\|></src>` | `<src>こう</src>` | 2170 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>立ててあげると</src>` | 1108 |
| 10 | `<src>十年経っても</src>` | `<src>受験立てても</src>` | 2472 |
| 11 | `<src>大した。</src>` | `<src>大丈夫。</src>` | 773 |

---

### Test Example 4 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1841 |
| 2 | `<src>옹심이, </src>` | `<src>용신이 </src>` | 993 |
| 3 | `<src><\|wait\|></src>` | `<src>칼 </src>` | 1539 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>용신이 </src>` | 711 |
| 5 | `<src>옹심이가 </src>` | `<src>어우시오 용신이 가 </src>` | 1932 |
| 6 | `<src><\|wait\|></src>` | `<src>섞여 </src>` | 628 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>있는 건데요. 야 </src>` | 1476 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 2420 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 673 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>행운 으로 </src>` | 1770 |
| 11 | `<src>진짜. </src>` | `<src>조금 쥐기 맞는 것 </src>` | 2453 |

---

### Test Example 5 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying </src>` | 1709 |
| 2 | `<src>Did very important research </src>` | `<src>important research </src>` | 988 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1767 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people? This is </src>` | 684 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1376 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 1072 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 1488 |
| 8 | `<src><\|wait\|></src>` | `<src>of the happiest </src>` | 2552 |
| 9 | `<src>of the happiest people </src>` | `<src>people </src>` | 425 |
| 10 | `<src>out there, </src>` | `<src>out there, people that </src>` | 2661 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1621 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2110 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>식성들은 </src>` | 1137 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1776 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1292 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1304 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 1255 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>식성들이 </src>` | 1169 |
| 8 | `<src>때문 입니다. </src>` | `<src>있었습니다. </src>` | 2124 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1386 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2414 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐던 교사 들은 </src>` | 836 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>淘沙完以后</src>` | 1951 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>呢，</src>` | 1112 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的冶炼轻</src>` | 1864 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1625 |
| 5 | `<src>然后</src>` | `<src>然后就</src>` | 1063 |
| 6 | `<src>就停留在一个</src>` | `<src>停留在</src>` | 1206 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1168 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 2104 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 1408 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2478 |
| 11 | `<src>抑郁状态。</src>` | `<src>低于状态。</src>` | 819 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>面对这个情况，</src>` | 1832 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>我们就是</src>` | 1109 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题就</src>` | 1827 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>赶紧的回报主管，</src>` | 1465 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1173 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们下了这个状况，</src>` | 1196 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1162 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 2244 |
| 9 | `<src>独立承担。</src>` | `<src>工具理性承担，</src>` | 1610 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 2369 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该做Solution。</src>` | 1164 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1723 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Apple, </src>` | 1037 |
| 3 | `<src>촉발 시키고 </src>` | `<src>축복 줍고 </src>` | 1976 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1571 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1165 |
| 6 | `<src><\|wait\|></src>` | `<src>모호 로 죽인 </src>` | 1379 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>헬레나 </src>` | 2130 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1011 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1610 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들인 </src>` | 2481 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>입니다. </src>` | 1315 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2076 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 1054 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくという</src>` | 1855 |
| 4 | `<src>といったようなものも</src>` | `<src>ようなものも</src>` | 1017 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 806 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1082 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1388 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 2402 |
| 9 | `<src>えっと</src>` | `<src>て、</src>` | 612 |
| 10 | `<src><\|wait\|></src>` | `<src>また</src>` | 1783 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>資料の案内がありますので</src>` | 2330 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>申し込ましてください。</src>` | 1274 |

---

### Test Example 11 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要做</src>` | 2049 |
| 2 | `<src>家长需要做的是，</src>` | `<src>的是，</src>` | 1133 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们身身</src>` | 1842 |
| 4 | `<src>用我们深深的</src>` | `<src><\|wait\|></src>` | 1512 |
| 5 | `<src>爱浇水、</src>` | `<src>的那爱交水，</src>` | 1239 |
| 6 | `<src>施肥，</src>` | `<src>所以</src>` | 1212 |
| 7 | `<src>给足</src>` | `<src>跟住</src>` | 1335 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心里影响，</src>` | 1921 |
| 9 | `<src><\|wait\|></src>` | `<src>跟耐心</src>` | 2300 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>等他</src>` | 1909 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 1260 |

---

### Test Example 12 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2103 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1898 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1038 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learned to repeat. </src>` | 1513 |
| 5 | `<src>Find what you're good at </src>` | `<src>Finally, we're good to go. </src>` | 1309 |
| 6 | `<src>and do more of it. </src>` | `<src>And do more of it. </src>` | 1504 |
| 7 | `<src><\|wait\|></src>` | `<src>And we'll be </src>` | 2676 |
| 8 | `<src>And what you're not good at, </src>` | `<src>not going to get to </src>` | 567 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>people around you to help you with </src>` | 3084 |
| 10 | `<src><\|wait\|></src>` | `<src>and </src>` | 771 |
| 11 | `<src>And until next time. </src>` | `<src>in tell next time. </src>` | 1350 |

---

### Test Example 13 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1916 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1193 |
| 3 | `<src>始めた</src>` | `<src>始めたもので</src>` | 1805 |
| 4 | `<src>もので、</src>` | `<src>ご</src>` | 442 |
| 5 | `<src>ゴッホ、</src>` | `<src>法を</src>` | 1112 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ごうぎゃん</src>` | 1211 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1293 |
| 8 | `<src>セザンヌ、</src>` | `<src>生産の</src>` | 1906 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1375 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の絵</src>` | 2075 |
| 11 | `<src>は、田舎の</src>` | `<src>は</src>` | 2019 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生でも</src>` | 1393 |

---

### Test Example 14 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあ</src>` | 2033 |
| 2 | `<src>距離が</src>` | `<src>なんとなくちょっと距離が離れてくる</src>` | 1161 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>みたいな感じで</src>` | 1845 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オーシャラーとかタタガネバ</src>` | 1134 |
| 5 | `<src>多いですね。</src>` | `<src>っぽいですね</src>` | 969 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊したい方って</src>` | 771 |
| 7 | `<src>すごい</src>` | `<src>すぐ行き来しきたり</src>` | 1429 |
| 8 | `<src>自己意識高いし、</src>` | `<src>し、</src>` | 2409 |
| 9 | `<src>自分で</src>` | `<src>でいうねでいうと</src>` | 678 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>多分その辺だと</src>` | 1722 |
| 11 | `<src>傾向が強いので、</src>` | `<src>シャグが強いので</src>` | 2353 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1373 |

---

### Test Example 15 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1697 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1096 |
| 3 | `<src>Drop into </src>` | `<src>Drop into your body </src>` | 1846 |
| 4 | `<src>your body. </src>` | `<src>where does </src>` | 1153 |
| 5 | `<src>Where does the tension </src>` | `<src>the tension </src>` | 1094 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 632 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 1935 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 2426 |
| 9 | `<src>I ask them what </src>` | `<src>Or is it </src>` | 1882 |
| 10 | `<src><\|wait\|></src>` | `<src>a block in your UY </src>` | 2413 |
| 11 | `<src>language are you using? </src>` | `<src>using? </src>` | 1604 |

---

### Test Example 16 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>다른 </src>` | 1766 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>선지 를 </src>` | 1223 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주게 달라 이거 주고 내가 </src>` | 1951 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 2141 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜이 </src>` | 587 |
| 6 | `<src>죽여 달라 </src>` | `<src>주게 달라 </src>` | 1681 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해줘야 되냐? 내가 </src>` | 2570 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 있는 </src>` | 1258 |
| 9 | `<src><\|wait\|></src>` | `<src>줄 거냐? </src>` | 2714 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아, </src>` | 646 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1671 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうですね。</src>` | 1764 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1023 |
| 3 | `<src><\|wait\|></src>` | `<src>天気</src>` | 1618 |
| 4 | `<src>テキという設備寺が</src>` | `<src>という設定が</src>` | 598 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1329 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1149 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1292 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井氏の仕組み</src>` | 1597 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 1533 |
| 10 | `<src>は五経、</src>` | `<src>五個、</src>` | 1379 |
| 11 | `<src><\|wait\|></src>` | `<src>設定が</src>` | 2419 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 818 |
| 13 | `<src>です。</src>` | `<src>五つです。</src>` | 1985 |

---

### Test Example 18 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2008 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 972 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 1574 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと信号が</src>` | 737 |
| 5 | `<src><\|wait\|></src>` | `<src>消えなくなって</src>` | 1542 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 1102 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1291 |
| 8 | `<src>役ねじの</src>` | `<src>逆ネジの</src>` | 2164 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 924 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうこと</src>` | 1669 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 2231 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1090 |
| 13 | `<src>分解完了。</src>` | `<src>分解完了。</src>` | 1761 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果在女高中</src>` | 1764 |
| 2 | `<src>如果在女高中生</src>` | `<src>生与长相</src>` | 1918 |
| 3 | `<src>与长相古怪的人</src>` | `<src>不怪的人之间，</src>` | 1134 |
| 4 | `<src><\|wait\|></src>` | `<src>有着某种</src>` | 1405 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>心理，</src>` | 1200 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1254 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1297 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从天帝这里开始的</src>` | 1988 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1812 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2243 |
| 11 | `<src>杨子思绪</src>` | `<src>养子思虑</src>` | 1354 |
| 12 | `<src>连篇。</src>` | `<src>连篇，</src>` | 1456 |

---

### Test Example 20 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 이럴지 너무 </src>` | 1946 |
| 2 | `<src><\|wait\|></src>` | `<src>인절요열이야 </src>` | 2005 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>내일 수 있지만 </src>` | 1021 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1813 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 고생 </src>` | 897 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>하린데 꿈일 </src>` | 1919 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 보이 고 </src>` | 2344 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 진짜 보살 로 </src>` | 1402 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 피라고 보이 세 우주 가 </src>` | 2895 |
| 10 | `<src>지금 나한테 </src>` | `<src>이제 보살이라 는 </src>` | 1323 |
| 11 | `<src>보살 이라는데. </src>` | `<src><\|wait\|></src>` | 1410 |

---

### Test Example 21 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1787 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1129 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1838 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1627 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1184 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1694 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 2486 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 581 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 2978 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets used </src>` | 965 |
| 11 | `<src>or gets used to make </src>` | `<src>to make </src>` | 1334 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1374 |

---

### Test Example 22 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1884 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Frenkel, and I </src>` | 2158 |
| 3 | `<src>I am currently </src>` | `<src>am currently studying </src>` | 887 |
| 4 | `<src><\|wait\|></src>` | `<src>in a PhD </src>` | 1526 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>in finance </src>` | 1064 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a B.S. of </src>` | 1559 |
| 7 | `<src><\|wait\|></src>` | `<src>psychology. </src>` | 2512 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at Yale, </src>` | 540 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 1836 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 2412 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate </src>` | 1347 |
| 12 | `<src>corporate consultancy. </src>` | `<src>consultancy. </src>` | 1551 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2151 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1902 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1047 |
| 4 | `<src><\|wait\|></src>` | `<src>the </src>` | 1198 |
| 5 | `<src>the instruction </src>` | `<src>instruction </src>` | 1148 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 520 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1667 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2224 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 546 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 2139 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1945 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game dot sort array </src>` | 1582 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1605 |

---

### Test Example 24 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2112 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 2036 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment </src>` | 884 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1103 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1042 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 728 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1534 |
| 8 | `<src>change can happen </src>` | `<src>happen in the </src>` | 2622 |
| 9 | `<src>in the United States. </src>` | `<src>United States. </src>` | 560 |
| 10 | `<src><\|wait\|></src>` | `<src>The meanings </src>` | 2296 |
| 11 | `<src>The meanings </src>` | `<src>of the </src>` | 1549 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>amendments, of course, </src>` | 1576 |
| 13 | `<src>myriad. </src>` | `<src>I'mared. </src>` | 1749 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1766 |
| 2 | `<src><\|wait\|></src>` | `<src>进入到二GIS</src>` | 1221 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>场，</src>` | 1787 |
| 4 | `<src>服务</src>` | `<src>还服务于</src>` | 1165 |
| 5 | `<src>在一级一线</src>` | `<src>在一集一线</src>` | 1118 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 624 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1353 |
| 8 | `<src><\|wait\|></src>` | `<src>在做维信</src>` | 2544 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>沟通好事几点，</src>` | 560 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1997 |
| 11 | `<src>给微信公众号评分</src>` | `<src>维信好平分的</src>` | 2211 |
| 12 | `<src>的新榜反而</src>` | `<src>新棒，</src>` | 1732 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1616 |

---

### Test Example 26 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1588 |
| 2 | `<src><\|wait\|></src>` | `<src>回到我</src>` | 1161 |
| 3 | `<src>回到我生活</src>` | `<src>生活的一个</src>` | 1865 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，</src>` | 1381 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1207 |
| 6 | `<src>在他下班的时候，</src>` | `<src>保持它稳定的时候，</src>` | 682 |
| 7 | `<src>在做热汤</src>` | `<src>在做日谈</src>` | 1749 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>的时候，在做的时候，</src>` | 2267 |
| 9 | `<src><\|wait\|></src>` | `<src>我当时</src>` | 2266 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>背对朝西面一个</src>` | 2055 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望哈，</src>` | 1797 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 1595 |

---

### Test Example 27 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1723 |
| 2 | `<src>映画でですね、</src>` | `<src>A、Aアンデスに</src>` | 2160 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 998 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>生生刻画を行う</src>` | 1819 |
| 5 | `<src>調べるときに、</src>` | `<src>場合で、その時に</src>` | 920 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>Aの乱交調べ</src>` | 1677 |
| 7 | `<src>ことで、あの</src>` | `<src>ということで、あの</src>` | 2481 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生生刻画を行う</src>` | 541 |
| 9 | `<src>保証する、生息である</src>` | `<src>生生刻画する</src>` | 2701 |
| 10 | `<src>ことを保証する</src>` | `<src>生刻画ということで保証する</src>` | 1471 |
| 11 | `<src>といったような</src>` | `<src>といったら、使い方を</src>` | 2013 |
| 12 | `<src>使い方をされます。</src>` | `<src>定めました。</src>` | 1445 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1803 |
| 2 | `<src>一切正常，</src>` | `<src>已经正常</src>` | 980 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>波动跳，</src>` | 1784 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 476 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀，</src>` | 1580 |
| 6 | `<src>期间</src>` | `<src>期限大概有</src>` | 1058 |
| 7 | `<src>大概有十位医生</src>` | `<src>十二星</src>` | 1873 |
| 8 | `<src>来诊断，</src>` | `<src>以内生来设定，</src>` | 2391 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 1274 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 2704 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 677 |
| 12 | `<src>他们</src>` | `<src>当然都很</src>` | 1934 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>一手打开。</src>` | 1487 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or or if you have </src>` | 1925 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 1083 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1823 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1469 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1162 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1298 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 1282 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. </src>` | 1980 |
| 9 | `<src>is this word </src>` | `<src>It's like oh, is this word </src>` | 1774 |
| 10 | `<src>spelled with a double </src>` | `<src>starting with </src>` | 2244 |
| 11 | `<src><\|wait\|></src>` | `<src>a double P, </src>` | 1193 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double L, I don't know </src>` | 1758 |
| 13 | `<src>know. </src>` | `<src>it. </src>` | 1331 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 1797 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>이루 어뜨는 거든 </src>` | 2400 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 100일인가 </src>` | 882 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1322 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유산 자 한 100일 정도 </src>` | 1385 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>굉장히 </src>` | 1726 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 2323 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연히 미네랄이다 </src>` | 1159 |
| 9 | `<src>이렇게 </src>` | `<src>이기 때문에 </src>` | 2423 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이제 </src>` | 788 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>그렇 던 거죠. 이제 </src>` | 1415 |
| 12 | `<src>그거 에다가 </src>` | `<src>그 후에다가 </src>` | 1424 |
| 13 | `<src>아연. </src>` | `<src>아멘. </src>` | 1531 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>砸到了一个</src>` | 1734 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>钱包，</src>` | 1094 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1802 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>拿到了钱包之后，</src>` | 1121 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必</src>` | 1164 |
| 6 | `<src><\|wait\|></src>` | `<src>就要先</src>` | 606 |
| 7 | `<src>先守住，</src>` | `<src>守住，</src>` | 1311 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想着那</src>` | 2376 |
| 9 | `<src><\|wait\|></src>` | `<src>我在去操作</src>` | 738 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦，</src>` | 2058 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2099 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1465 |
| 13 | `<src><\|wait\|></src>` | `<src>因为呢，</src>` | 1538 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1484 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1748 |
| 2 | `<src>我们可以看到的是</src>` | `<src>这一张的部分，我们看到的是</src>` | 2290 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个</src>` | 699 |
| 4 | `<src>的人，但是</src>` | `<src>带吊耳的人，但是</src>` | 1433 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1270 |
| 6 | `<src>所以</src>` | `<src>这通场</src>` | 1293 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>好像这样一个状况</src>` | 1706 |
| 8 | `<src>时候，就要去</src>` | `<src>会需要去特别</src>` | 1507 |
| 9 | `<src>特别注意，</src>` | `<src>的注意是</src>` | 1516 |
| 10 | `<src>是它能不能够</src>` | `<src>它能不能</src>` | 2337 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够得到</src>` | 652 |
| 12 | `<src>它钓不到鱼</src>` | `<src>于它吊不到</src>` | 1878 |
| 13 | `<src><\|wait\|></src>` | `<src>于一个易事</src>` | 1553 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 1293 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒</src>` | 1878 |
| 2 | `<src>要提醒大家，</src>` | `<src>大家，</src>` | 1141 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1908 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1518 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1165 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1188 |
| 7 | `<src>所面临的一些</src>` | `<src>说明你的一些</src>` | 1132 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>委气啊跟夫妻</src>` | 2228 |
| 9 | `<src>也不可能是</src>` | `<src>也不可能是</src>` | 1600 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 2355 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1201 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来</src>` | 1605 |
| 13 | `<src>因此会建议</src>` | `<src>的，因此会建议</src>` | 1309 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1394 |

---

### Test Example 34 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who just </src>` | 2014 |
| 2 | `<src>just getting going </src>` | `<src>getting going </src>` | 1135 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1831 |
| 4 | `<src><\|wait\|></src>` | `<src>and </src>` | 1216 |
| 5 | `<src>and I have ten of them </src>` | `<src>like ten of them </src>` | 1351 |
| 6 | `<src>that I think are </src>` | `<src>that are really </src>` | 1038 |
| 7 | `<src>really important. </src>` | `<src>important </src>` | 1295 |
| 8 | `<src><\|wait\|></src>` | `<src>to </src>` | 2163 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go and do </src>` | 1035 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 2670 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 766 |
| 12 | `<src>that follow this video </src>` | `<src>about this video. </src>` | 1532 |
| 13 | `<src><\|wait\|></src>` | `<src>It'll cover each one </src>` | 1772 |
| 14 | `<src>that cover each one </src>` | `<src>in a little more </src>` | 1377 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>detail, </src>` | 852 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1718 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개 가 </src>` | 2067 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중화 벌써 100만 미만 으로 </src>` | 1294 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1652 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 782 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1587 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 기업 들은 성장 하거나 </src>` | 2697 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 해외 에 </src>` | 1119 |
| 9 | `<src>걷게 되는데 </src>` | `<src>익을 겪게 되는데 </src>` | 2905 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>이거 는 </src>` | 822 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성기 없던 것은 </src>` | 2047 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>성장 도 </src>` | 1367 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>표해 보하지 않을 현상 들 보이 게 된 거죠. </src>` | 1703 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>十</src>` | 1848 |
| 2 | `<src>十一二手とか</src>` | `<src>二日で</src>` | 975 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>解けた。</src>` | 1686 |
| 4 | `<src>十秒で。</src>` | `<src>おそらく十秒で</src>` | 619 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1229 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1169 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1295 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですかね。</src>` | 1216 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 2035 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1456 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2271 |
| 12 | `<src><\|wait\|></src>` | `<src>十</src>` | 687 |
| 13 | `<src>十一二手で</src>` | `<src>二日であの</src>` | 1782 |
| 14 | `<src>あの</src>` | `<src><\|wait\|></src>` | 1595 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1490 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 833 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 1801 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1196 |
| 3 | `<src><\|wait\|></src>` | `<src>there was </src>` | 1810 |
| 4 | `<src>such interfaces before, </src>` | `<src>such instances before. </src>` | 1280 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1299 |
| 6 | `<src>netfilter, TC. </src>` | `<src>Next future TC </src>` | 472 |
| 7 | `<src>Yeah, so </src>` | `<src>there. </src>` | 1787 |
| 8 | `<src>this is just </src>` | `<src>So this is just </src>` | 2273 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1171 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2638 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 823 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 1747 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1567 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on Bug Repositories </src>` | 1457 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1178 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1799 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 </src>` | 2040 |
| 3 | `<src>이방인으로 </src>` | `<src>너희 가 이방인으로 </src>` | 1087 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1578 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1092 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1559 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 그대로 </src>` | 2470 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그려 갔느니라. </src>` | 453 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1659 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2238 |
| 11 | `<src>너희 에게 </src>` | `<src>너희에게 </src>` | 1243 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1619 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1442 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1250 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1023 |

---

### Test Example 39 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2177 |
| 2 | `<src><\|wait\|></src>` | `<src>새 머리 빌 걸 </src>` | 2015 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>봐야 </src>` | 911 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>이제 서름이 </src>` | 1210 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋은 자태 돋은 </src>` | 1466 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>내 기매움이야 </src>` | 1285 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1755 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야 </src>` | 1540 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 </src>` | 1598 |
| 10 | `<src>물릴 거고 </src>` | `<src>너무 울릴 거고 </src>` | 2387 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 너무 </src>` | 1243 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>지켜 주라고 </src>` | 1610 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>이제 찔러 주다 보니까 </src>` | 1526 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 마음 에 </src>` | 1318 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 941 |

---

### Test Example 40 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Educational </src>` | 1899 |
| 2 | `<src>Educational attainment. </src>` | `<src>entertainment. How far </src>` | 1236 |
| 3 | `<src>How far did you </src>` | `<src>did you </src>` | 1787 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go in your </src>` | 1552 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>education? </src>` | 1153 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1345 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 2299 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>entertainment. </src>` | 846 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 1661 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And so, did you </src>` | 2482 |
| 11 | `<src>That's another level of </src>` | `<src>graduate? </src>` | 1201 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of entertainment. </src>` | 1826 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now. </src>` | 1782 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you </src>` | 954 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 901 |

---

### Test Example 41 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1960 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어디 보면 </src>` | 710 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1807 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 688 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>통생 의자 </src>` | 1655 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 도 가족 같은 </src>` | 1067 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>통생 의자나 </src>` | 1965 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 2252 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 955 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생모다는 </src>` | 2542 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 1008 |
| 12 | `<src>자기 스스로 </src>` | `<src>그 </src>` | 1713 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1567 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1358 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려 놓고 </src>` | 864 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했습니다 이렇게 </src>` | 912 |

---

### Test Example 42 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1897 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 2133 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 900 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较稳定</src>` | 1399 |
| 5 | `<src>也就是</src>` | `<src>的部分。也就是</src>` | 1169 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面</src>` | 1334 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>的业绩增长所带来的</src>` | 2037 |
| 8 | `<src>与收入的</src>` | `<src>流动收入的</src>` | 1224 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果</src>` | 1908 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面</src>` | 2345 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1830 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错的，只是</src>` | 1607 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对整体来说，</src>` | 1477 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了那么一点</src>` | 882 |
| 15 | `<src><\|wait\|></src>` | `<src>。</src>` | 1066 |

---

### Test Example 43 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 1968 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>蒸らせてやる。</src>` | 1225 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1778 |
| 4 | `<src><\|wait\|></src>` | `<src>今</src>` | 1199 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>火勢みて</src>` | 1350 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 370 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1813 |
| 8 | `<src><\|wait\|></src>` | `<src>超に超えてる</src>` | 2394 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈火勢気。</src>` | 1531 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2510 |
| 11 | `<src>長年</src>` | `<src>流れに</src>` | 821 |
| 12 | `<src>船大工をやってる</src>` | `<src>ぶなだいくを</src>` | 2047 |
| 13 | `<src>が、</src>` | `<src>やってる。</src>` | 1299 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなに</src>` | 1366 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>すごい海賊船を見た</src>` | 1000 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 918 |

---

### Test Example 44 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1742 |
| 2 | `<src>HTML이라고 </src>` | `<src>어 H T M L </src>` | 2054 |
| 3 | `<src><\|wait\|></src>` | `<src>이라고 하는 </src>` | 918 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 </src>` | 1437 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1255 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1255 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1513 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 1824 |
| 9 | `<src>문법 에 </src>` | `<src>문법 과 </src>` | 2226 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>말하기 우리 가 이제 </src>` | 2029 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>그것 들을 </src>` | 1934 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 1641 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그것 들을 </src>` | 1347 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1007 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1116 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1989 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 2043 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうのが出ていればいいです。</src>` | 1095 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルPython</src>` | 1445 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね。</src>` | 1110 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも</src>` | 1271 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルン</src>` | 2307 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>書いてあとそれは</src>` | 953 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコード</src>` | 1714 |
| 10 | `<src>生成されて、それが</src>` | `<src>それから生成される</src>` | 2302 |
| 11 | `<src>実行されることで</src>` | `<src>やつそれが実行されることで信号処理</src>` | 1398 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われるっていう</src>` | 1446 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ことをしている</src>` | 1324 |
| 14 | `<src><\|wait\|></src>` | `<src>からですね。</src>` | 1215 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 1022 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ</src>` | 894 |

---

### Test Example 46 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1695 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1926 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해 놓았습니다. </src>` | 1151 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 1223 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>로쿠자 에 분석 을 보시면 </src>` | 1351 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1219 |
| 7 | `<src>26비트 FP </src>` | `<src>이오 6K </src>` | 1228 |
| 8 | `<src>파이프 를 </src>` | `<src>to FPD 파이 프를 </src>` | 2163 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128bit로 </src>` | 1750 |
| 10 | `<src>것으로 보인다. </src>` | `<src>나충가서 로 포인트 한다. </src>` | 2495 |
| 11 | `<src><\|wait\|></src>` | `<src>엑스 박스 </src>` | 1506 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>시리즈, X에서도 없는 </src>` | 1710 |
| 13 | `<src><\|wait\|></src>` | `<src>인피니트 캐시 </src>` | 1545 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>C, </src>` | 753 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>S2가 여기 도 없다. </src>` | 997 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 658 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수가 </src>` | 1820 |
| 2 | `<src><\|wait\|></src>` | `<src>인상 하는 </src>` | 1161 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 1928 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1926 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 791 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1394 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2314 |
| 8 | `<src>이 가벼운 </src>` | `<src>가벼운 종목 </src>` | 773 |
| 9 | `<src>종목 들이 </src>` | `<src>들이 </src>` | 1689 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2297 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 1352 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 </src>` | 1612 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요식초기 </src>` | 1693 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1096 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 1011 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 666 |

---

### Test Example 48 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1900 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1154 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1920 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 1669 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 1108 |
| 6 | `<src>but the reality </src>` | `<src>But the reality </src>` | 1753 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 2373 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new cat </src>` | 576 |
| 9 | `<src>block and because the </src>` | `<src>in the box, and because </src>` | 3189 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 793 |
| 11 | `<src>changed from 20 </src>` | `<src>chains from </src>` | 1578 |
| 12 | `<src>years ago, </src>` | `<src>twenty years ago, </src>` | 1696 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1478 |
| 14 | `<src>a higher standard because </src>` | `<src>our own standard </src>` | 877 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 1205 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to </src>` | 355 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2015 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感觉对手的</src>` | 2143 |
| 3 | `<src>的感情或</src>` | `<src>感情或真实</src>` | 892 |
| 4 | `<src>真实意图的，</src>` | `<src>意图的，</src>` | 1670 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1078 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1843 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常会</src>` | 2371 |
| 8 | `<src>会听到人们</src>` | `<src>听到人们这样说：</src>` | 1279 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 2539 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 704 |
| 11 | `<src>这个人</src>` | `<src>这个人又在</src>` | 1386 |
| 12 | `<src>又在说谎了，</src>` | `<src>躲躲藏藏了，</src>` | 1605 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛已经</src>` | 1378 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>说明了一切。</src>` | 982 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 936 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 828 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 486 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 1931 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1166 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 2092 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1566 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1077 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트예요. </src>` | 1716 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이 컨설턴트 이 </src>` | 2563 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>어갑고 </src>` | 1137 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2818 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 675 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>들었을 때 </src>` | 1932 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1527 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1279 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스 사이트 스크트에서 </src>` | 1236 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>API까지 </src>` | 909 |
| 16 | `<src>감염 이 될까. </src>` | `<src>가능 이 될까? </src>` | 597 |

---

### Test Example 51 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 으면 </src>` | 2129 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 해매입니다. </src>` | 2169 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 882 |
| 4 | `<src><\|wait\|></src>` | `<src>하고 온 거로 </src>` | 1658 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 다니 고 </src>` | 1100 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>있거나 </src>` | 1650 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 으로 가면 </src>` | 2551 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 1529 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장려 리요. </src>` | 2950 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 1741 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1594 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1447 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 862 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모여 봐요. </src>` | 1331 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다인 것 같아요. </src>` | 628 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 515 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>Fourth in the </src>` | 1731 |
| 2 | `<src>首次觉知到</src>` | `<src>source code </src>` | 1120 |
| 3 | `<src>那个现象：</src>` | `<src>readability. </src>` | 1828 |
| 4 | `<src>每当我们</src>` | `<src>But when </src>` | 1230 |
| 5 | `<src><\|wait\|></src>` | `<src>we go to </src>` | 1338 |
| 6 | `<src>处于爱之中，</src>` | `<src>I2C, </src>` | 551 |
| 7 | `<src>所谓的爱，</src>` | `<src>the I2C is </src>` | 1881 |
| 8 | `<src>我们也</src>` | `<src>the same as </src>` | 2114 |
| 9 | `<src>同时进入恨。</src>` | `<src>the time </src>` | 1274 |
| 10 | `<src><\|wait\|></src>` | `<src>we enter </src>` | 2393 |
| 11 | `<src>在早上的时候，</src>` | `<src>at the start </src>` | 793 |
| 12 | `<src>它是爱；</src>` | `<src>of the I2C. </src>` | 1649 |
| 13 | `<src>到了晚上，</src>` | `<src>It's the same as </src>` | 1673 |
| 14 | `<src>它就变成恨。</src>` | `<src>the end. </src>` | 1438 |
| 15 | `<src><\|wait\|></src>` | `<src>That's </src>` | 966 |
| 16 | `<src>那个钟摆</src>` | `<src>the same thing. </src>` | 1243 |
| 17 | `<src><\|wait\|></src>` | `<src>It's </src>` | 612 |
| 18 | `<src>继续在移动。</src>` | `<src>the same thing. </src>` | 548 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2173 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1105 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1857 |
| 4 | `<src><\|wait\|></src>` | `<src>about the </src>` | 1160 |
| 5 | `<src>about the EHR fields </src>` | `<src>HR field </src>` | 1347 |
| 6 | `<src><\|wait\|></src>` | `<src>being of </src>` | 359 |
| 7 | `<src>being of critical importance </src>` | `<src>critical importance </src>` | 1280 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 2059 |
| 9 | `<src><\|wait\|></src>` | `<src>variant data </src>` | 960 |
| 10 | `<src>databases, </src>` | `<src>bases, which is obviously </src>` | 1561 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>not my loves. </src>` | 2464 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 1271 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree upon </src>` | 1640 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 1367 |
| 15 | `<src>to be in these </src>` | `<src>to be in these data </src>` | 1308 |
| 16 | `<src>data sources that we can </src>` | `<src>sources that we can </src>` | 1024 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 948 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 495 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 540 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Um, </src>` | 1849 |
| 2 | `<src>Also, </src>` | `<src>also, you will not </src>` | 2010 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 1057 |
| 4 | `<src>move media objects </src>` | `<src>meadia objects </src>` | 1515 |
| 5 | `<src><\|wait\|></src>` | `<src>between the </src>` | 1150 |
| 6 | `<src>between the resources. </src>` | `<src>resources </src>` | 1271 |
| 7 | `<src>So, if </src>` | `<src>though, </src>` | 1237 |
| 8 | `<src>you get into </src>` | `<src>if you get into the </src>` | 2037 |
| 9 | `<src>a situation </src>` | `<src>situation where you </src>` | 2629 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 1719 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 1555 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular </src>` | 1633 |
| 13 | `<src>you need to let us know, </src>` | `<src>resource, you can do let us know. </src>` | 1607 |
| 14 | `<src>and we can see about </src>` | `<src>And we can see about </src>` | 915 |
| 15 | `<src><\|wait\|></src>` | `<src>moving those media </src>` | 1231 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>files and then making sure </src>` | 612 |
| 17 | `<src>get backed up </src>` | `<src>you get back up </src>` | 504 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 234 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1757 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1096 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1801 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1374 |
| 5 | `<src>he's been without food, </src>` | `<src>he knows that </src>` | 1262 |
| 6 | `<src><\|wait\|></src>` | `<src>before he went to the wilderness </src>` | 1309 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>to study, he's hungry. </src>` | 1555 |
| 8 | `<src>And so he says </src>` | `<src>And so he says to </src>` | 1785 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 1856 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 2608 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn these </src>` | 1794 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>stones to bread. </src>` | 1612 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1338 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with that </src>` | 841 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 1256 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 597 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead by bread. </src>` | 622 |
| 18 | `<src>by bread alone. </src>` | `<src>Alone. </src>` | 348 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2159 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1141 |
| 3 | `<src>right, </src>` | `<src>right, and </src>` | 1799 |
| 4 | `<src>and the Supreme Court </src>` | `<src>the Supreme Court </src>` | 1143 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 1237 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And I don't know </src>` | 705 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1921 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2128 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1248 |
| 10 | `<src>change </src>` | `<src>social change, </src>` | 2713 |
| 11 | `<src>these days, </src>` | `<src>these days. </src>` | 652 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 2169 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect </src>` | 1300 |
| 14 | `<src>the consensus </src>` | `<src><\|wait\|></src>` | 1373 |
| 15 | `<src><\|wait\|></src>` | `<src>the consensus that's already </src>` | 1127 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 903 |
| 17 | `<src><\|wait\|></src>` | `<src>So. </src>` | 576 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 510 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 202 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 330 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 358 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1936 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 2028 |
| 3 | `<src><\|wait\|></src>` | `<src>图片</src>` | 880 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>的图片呢，</src>` | 1548 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1199 |
| 6 | `<src>的部分。</src>` | `<src>客订的部分，</src>` | 1356 |
| 7 | `<src>那客厅一般</src>` | `<src>而客订一般</src>` | 2246 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 943 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 2093 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 2056 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 1282 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的部分。</src>` | 1436 |
| 13 | `<src>也会反映的是</src>` | `<src>它会反映的是</src>` | 1468 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给</src>` | 1167 |
| 15 | `<src>一点时间，</src>` | `<src>自己一点时间</src>` | 998 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好地做</src>` | 924 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>下来休息，</src>` | 518 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 606 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛。</src>` | 415 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 347 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 295 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1800 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare. </src>` | 1109 |
| 3 | `<src>and they often </src>` | `<src>And they often </src>` | 1810 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 1355 |
| 5 | `<src><\|wait\|></src>` | `<src>to completely </src>` | 1216 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>revolutionize the world. </src>` | 1168 |
| 7 | `<src><\|wait\|></src>` | `<src>The personality </src>` | 1190 |
| 8 | `<src>Their personality is </src>` | `<src>is something </src>` | 2154 |
| 9 | `<src>something of a </src>` | `<src>that have a contradiction. </src>` | 1103 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2476 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 936 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, they also </src>` | 1639 |
| 13 | `<src>they also hate </src>` | `<src>hate </src>` | 1512 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations. </src>` | 1342 |
| 15 | `<src>and like to </src>` | `<src>And like </src>` | 881 |
| 16 | `<src><\|wait\|></src>` | `<src>to get straight to </src>` | 925 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 830 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 503 |
| 19 | `<src>play </src>` | `<src>to play </src>` | 561 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, </src>` | 339 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 168 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 322 |
| 23 | `<src><\|wait\|></src>` | `<src>E. </src>` | 266 |
| 24 | `<src><\|wait\|></src>` | `<src>N. </src>` | 222 |
| 25 | `<src>ENTP stands for </src>` | `<src>T. S. Stanford. </src>` | 286 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1915 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>경무를 거부 한 </src>` | 2059 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>맹병이 후보 를 </src>` | 905 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1639 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선을 </src>` | 1092 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1886 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2369 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1377 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2655 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 907 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1945 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들은 해놓고 </src>` | 1478 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 </src>` | 1309 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>를 떨어뜨리 겠다는 </src>` | 1026 |
| 15 | `<src><\|wait\|></src>` | `<src>뜻끼를 품은 </src>` | 919 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 523 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 556 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 409 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 359 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 266 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석 성상급건. </src>` | 301 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 226 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당이 </src>` | 242 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기 얼마나 </src>` | 250 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재 입니까? </src>` | 263 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1916 |
| 2 | `<src>食堂ね</src>` | `<src>食後ね今作って</src>` | 2025 |
| 3 | `<src>今作ってる</src>` | `<src>みたいなの</src>` | 1019 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>でここのね</src>` | 1355 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>フォールボスノンホテル</src>` | 1364 |
| 6 | `<src>も</src>` | `<src>も朝食が</src>` | 1445 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 2387 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 748 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 2582 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 1555 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドストンホテル</src>` | 1468 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいな</src>` | 1380 |
| 13 | `<src>なっていう方はですね</src>` | `<src>っていう方はですね</src>` | 1341 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさって</src>` | 1260 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てみるとまあいいんじゃない</src>` | 1019 |
| 16 | `<src><\|wait\|></src>` | `<src>なと</src>` | 811 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います</src>` | 493 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここホテルからですね</src>` | 598 |
| 19 | `<src>駅ももう</src>` | `<src>プサン駅も</src>` | 433 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 369 |
| 21 | `<src>歩いて一分</src>` | `<src>一本かかるか</src>` | 292 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かからないか</src>` | 229 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね立地の</src>` | 279 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>いいねまあホテル</src>` | 227 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 243 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 224 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 163 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 130 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではね</src>` | 140 |
