# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9177
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.5497
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
  - PROCESS_TIME_MS_AVG: 1463.2800
  - PROCESS_TIME_MS_P50: 1483.9600
  - PROCESS_TIME_MS_P95: 2403.8180
  - PROCESS_TIME_MS_MAX: 3054.5510

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1801 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1293 |
| 3 | `<src>これなんかまだ</src>` | `<src>この中まだ1年</src>` | 1072 |
| 4 | `<src>一年生ですからね。</src>` | `<src>年ですからね。</src>` | 1268 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1307 |
| 6 | `<src>こう短く</src>` | `<src>こうミミク枠</src>` | 963 |
| 7 | `<src>剪定を</src>` | `<src>先天性を</src>` | 940 |
| 8 | `<src><\|wait\|></src>` | `<src>こう退ず</src>` | 1739 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>していただく</src>` | 1077 |
| 10 | `<src>十年経っても</src>` | `<src>と1年経っても</src>` | 1324 |
| 11 | `<src>大した。</src>` | `<src>退した。</src>` | 1770 |

---

### Test Example 2 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 2040 |
| 2 | `<src>옹심이, </src>` | `<src>공심이 </src>` | 1368 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 902 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 공심이 </src>` | 1361 |
| 5 | `<src>옹심이가 </src>` | `<src>그래서 </src>` | 1311 |
| 6 | `<src><\|wait\|></src>` | `<src>공심이 가 </src>` | 1302 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. </src>` | 752 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 2402 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 644 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>행위 으로도 조금 </src>` | 2187 |
| 11 | `<src>진짜. </src>` | `<src>주극입니다, 진짜. </src>` | 1937 |

---

### Test Example 3 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1977 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1291 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 774 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1279 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1129 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 486 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 1742 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 2569 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1102 |
| 10 | `<src><\|wait\|></src>` | `<src>language are you </src>` | 1958 |
| 11 | `<src>language are you using? </src>` | `<src>using? </src>` | 1656 |

---

### Test Example 4 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1910 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptrude. </src>` | 1484 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽발시 뀌고 </src>` | 1240 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1034 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1247 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 1676 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>배르나 </src>` | 949 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1881 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1042 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 1983 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>입니다. </src>` | 1652 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2380 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>乖的忪子儿，</src>` | 1696 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这里这个游星</src>` | 1549 |
| 4 | `<src>然后</src>` | `<src>也很大。</src>` | 839 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 892 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我再放大。</src>` | 1720 |
| 7 | `<src>儿核桃</src>` | `<src>喝汤儿，</src>` | 1396 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1425 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉吧？</src>` | 1262 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 1685 |
| 11 | `<src>仁儿。</src>` | `<src>喝汤儿。</src>` | 1682 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2384 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1409 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 757 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1436 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1199 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1680 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1081 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1871 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1223 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 1722 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은. </src>` | 1746 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2112 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1368 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 665 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1230 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 1051 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 810 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1616 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1211 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1708 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1431 |
| 11 | `<src>は、田舎の</src>` | `<src>は、</src>` | 1725 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生</src>` | 1980 |

---

### Test Example 8 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2155 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要器术是容易的，</src>` | 1750 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 1394 |
| 4 | `<src>只有一个师父</src>` | `<src>但是</src>` | 749 |
| 5 | `<src><\|wait\|></src>` | `<src>只有一个师傅指导到</src>` | 1103 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1740 |
| 7 | `<src>处于中间，</src>` | `<src>突破于中年，</src>` | 1725 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1064 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反</src>` | 1503 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 1859 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅。</src>` | 1898 |

---

### Test Example 9 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>It did </src>` | 1887 |
| 2 | `<src>Did very important research </src>` | `<src>vary important research </src>` | 1375 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 889 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1496 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1322 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 1661 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 1049 |
| 8 | `<src><\|wait\|></src>` | `<src>of the happiest </src>` | 1862 |
| 9 | `<src>of the happiest people </src>` | `<src>people </src>` | 1492 |
| 10 | `<src>out there, </src>` | `<src>out there, people that </src>` | 1885 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1981 |

---

### Test Example 10 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2265 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1677 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1477 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1056 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水，</src>` | 809 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1706 |
| 7 | `<src>给足</src>` | `<src><\|wait\|></src>` | 1521 |
| 8 | `<src>孩子心理营养，</src>` | `<src>给子女心灵营养，</src>` | 1447 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1672 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>给内心等家</src>` | 2371 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 1501 |

---

### Test Example 11 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2196 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘沙完以后呢，</src>` | 1709 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的冶铁矿</src>` | 1661 |
| 4 | `<src>能量也衰弱了，</src>` | `<src><\|wait\|></src>` | 948 |
| 5 | `<src>然后</src>` | `<src>能量也衰弱了，</src>` | 703 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 1733 |
| 7 | `<src>相对的低</src>` | `<src><\|wait\|></src>` | 2063 |
| 8 | `<src>能量的运行</src>` | `<src>一个相对的低能量的运行</src>` | 897 |
| 9 | `<src>状态，</src>` | `<src>状态。</src>` | 1885 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就</src>` | 2056 |
| 11 | `<src>抑郁状态。</src>` | `<src>是所谓的易于状态。</src>` | 1689 |

---

### Test Example 12 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2059 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1702 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1314 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1305 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 670 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有的这个状况。</src>` | 1754 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1833 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1118 |
| 9 | `<src>独立承担。</src>` | `<src>等于</src>` | 1905 |
| 10 | `<src>整体而言，</src>` | `<src>你承担。整体而言，</src>` | 2336 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该就是Solution。</src>` | 2082 |

---

### Test Example 13 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 2159 |
| 2 | `<src>あの</src>` | `<src>などがあの</src>` | 1372 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 893 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1368 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので、ぜひ</src>` | 1377 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 1599 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 451 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりますし、</src>` | 2424 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 879 |
| 10 | `<src><\|wait\|></src>` | `<src>ご不明な点が</src>` | 1960 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ありましたら</src>` | 1721 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>お知らせがおりますので、ご参照ください。</src>` | 2184 |

---

### Test Example 14 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1890 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到我</src>` | 1513 |
| 3 | `<src>回到我生活</src>` | `<src>生活的一个轨道，</src>` | 983 |
| 4 | `<src>的一个轨道哈，</src>` | `<src><\|wait\|></src>` | 1121 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1265 |
| 6 | `<src>在他下班的时候，</src>` | `<src>照他下班的时候，</src>` | 1671 |
| 7 | `<src>在做热汤</src>` | `<src>在工作</src>` | 482 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>和餐厅</src>` | 2343 |
| 9 | `<src><\|wait\|></src>` | `<src>认识了，所以这个</src>` | 1196 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时被他作为知音</src>` | 2119 |
| 11 | `<src>小小的愿望</src>` | `<src>的一个小小的愿望</src>` | 1874 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 2208 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2289 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1491 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. Learn to </src>` | 1423 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>sentence repeat, </src>` | 971 |
| 5 | `<src>Find what you're good at </src>` | `<src>find out if you're good at </src>` | 1153 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1842 |
| 7 | `<src><\|wait\|></src>` | `<src>And what you </src>` | 2485 |
| 8 | `<src>And what you're not good at, </src>` | `<src>are not good at, </src>` | 1077 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>give the people around you to help you with. </src>` | 2231 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1677 |
| 11 | `<src>And until next time. </src>` | `<src>And in telling next time, </src>` | 2693 |

---

### Test Example 16 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 2135 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1496 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>저열한 일일 수 있지만 </src>` | 1903 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1252 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>진짜 보살 도요. 아니 </src>` | 394 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 가 보살 인데 꿈일 프로 </src>` | 1878 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 이거. </src>` | 2443 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 1245 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보살 로 보일 프로 요. </src>` | 2090 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 가 지금 나한테 보살 이라는 </src>` | 2179 |
| 11 | `<src>보살 이라는데. </src>` | `<src>얘기. </src>` | 2321 |

---

### Test Example 17 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2524 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 1183 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1241 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>おしゃれルカダがね、</src>` | 1287 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1068 |
| 6 | `<src>開業したい方って</src>` | `<src>海泳じたい方って</src>` | 1712 |
| 7 | `<src>すごい</src>` | `<src>すごいよく</src>` | 1084 |
| 8 | `<src>自己意識高いし、</src>` | `<src>行き来おきて다가、シー、</src>` | 1939 |
| 9 | `<src>自分で</src>` | `<src>ジムで</src>` | 1665 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>トレーニングを</src>` | 2243 |
| 11 | `<src>傾向が強いので、</src>` | `<src>すると喋る力強くなるので、</src>` | 1583 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 2125 |

---

### Test Example 18 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 2322 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 1380 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 986 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1217 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1264 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1490 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 460 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2048 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 790 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 1707 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2251 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array. </src>` | 1596 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2330 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1967 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1616 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1807 |
| 4 | `<src><\|wait\|></src>` | `<src>之间有着某种</src>` | 1395 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>联系，</src>` | 758 |
| 6 | `<src>难道会是</src>` | `<src><\|wait\|></src>` | 1189 |
| 7 | `<src><\|wait\|></src>` | `<src>难道会使童年</src>` | 2404 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src><\|wait\|></src>` | 515 |
| 9 | `<src><\|wait\|></src>` | `<src>夜里开始的</src>` | 2062 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2115 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1740 |
| 12 | `<src>连篇。</src>` | `<src>连篇？</src>` | 1990 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1996 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1718 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1315 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy. </src>` | 1064 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>And when those bonds are broken, </src>` | 945 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1692 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted </src>` | 1331 |
| 8 | `<src>other types of energy, </src>` | `<src>to other types of energy, </src>` | 1646 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 1987 |
| 10 | `<src><\|wait\|></src>` | `<src>Or, </src>` | 2097 |
| 11 | `<src>or gets used to make </src>` | `<src>gets used to make </src>` | 1807 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1995 |

---

### Test Example 21 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2099 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜을 </src>` | 1620 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주겨 달라 이거 주고 내가 </src>` | 1877 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주질 못하 도록 한다. </src>` | 1475 |
| 5 | `<src>다른 잔찜에 </src>` | `<src><\|wait\|></src>` | 1592 |
| 6 | `<src>죽여 달라 </src>` | `<src>다른 잔찜을 주겨 달라 </src>` | 1198 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐. 내가 </src>` | 1948 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 2194 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알느냐? </src>` | 2067 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>어? </src>` | 2105 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1567 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1927 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1284 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 768 |
| 4 | `<src>テキという設備寺が</src>` | `<src>定規という接尾辞</src>` | 1655 |
| 5 | `<src>ありましたね。</src>` | `<src>が来ましたね。</src>` | 1313 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1604 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 450 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>激い酔いを</src>` | 2425 |
| 9 | `<src><\|wait\|></src>` | `<src>の仕組みは、</src>` | 1195 |
| 10 | `<src>は五経、</src>` | `<src>僕、</src>` | 1867 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1625 |
| 12 | `<src>設備寺、五比</src>` | `<src>接尾辞、</src>` | 2390 |
| 13 | `<src>です。</src>` | `<src>合います。</src>` | 1221 |

---

### Test Example 23 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个</src>` | 1931 |
| 2 | `<src><\|wait\|></src>` | `<src>就是能源物资</src>` | 1315 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二级市场，</src>` | 968 |
| 4 | `<src>服务</src>` | `<src>へ服务于</src>` | 1280 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1391 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>生产的大牛们。</src>` | 1192 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，呃，</src>` | 789 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2519 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做维辛运动</src>` | 685 |
| 10 | `<src>发现</src>` | `<src>好几年，你会发现，</src>` | 2203 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维辛运动好平行</src>` | 1840 |
| 12 | `<src>的新榜反而</src>` | `<src>的新棒</src>` | 2049 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1579 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2176 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 1316 |
| 3 | `<src>ギアが</src>` | `<src>ギアです。ギアが</src>` | 1073 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1358 |
| 5 | `<src><\|wait\|></src>` | `<src>逆焼けができなくなってしまう</src>` | 1373 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1568 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 931 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1899 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1180 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いている</src>` | 1860 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 1643 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 2367 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを。</src>` | 1365 |

---

### Test Example 25 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 2070 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel. </src>` | 1638 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1643 |
| 4 | `<src><\|wait\|></src>` | `<src>in </src>` | 705 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>AB Finance </src>` | 989 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a bachelor of psychology. </src>` | 1729 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1265 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the A&E </src>` | 1753 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1907 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2444 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2381 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1361 |

---

### Test Example 26 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1901 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 1510 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 879 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1475 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1260 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を</src>` | 1801 |
| 7 | `<src>ことで、あの</src>` | `<src>調べることで、あの</src>` | 2551 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1641 |
| 9 | `<src>保証する、生息である</src>` | `<src>証明する、生息である</src>` | 1872 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1921 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 2274 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 747 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2296 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1311 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1334 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1060 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1065 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1780 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1512 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. </src>` | 1313 |
| 9 | `<src>is this word </src>` | `<src>Like, oh, is this word </src>` | 1464 |
| 10 | `<src>spelled with a double </src>` | `<src>said with a </src>` | 1725 |
| 11 | `<src><\|wait\|></src>` | `<src>double p, </src>` | 2039 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double lam? I don't </src>` | 2796 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 635 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2319 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1479 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1912 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore </src>` | 1142 |
| 5 | `<src>history as a guide </src>` | `<src>this history as a guide </src>` | 475 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1635 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1175 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1680 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1583 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1970 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1840 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 2616 |
| 13 | `<src>myriad. </src>` | `<src>are Miriam. </src>` | 761 |

---

### Test Example 29 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src><\|wait\|></src>` | 2146 |
| 2 | `<src>一切正常，</src>` | `<src>我当时一切正常，</src>` | 1649 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1735 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1142 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 461 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 1656 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 1399 |
| 8 | `<src>来诊断，</src>` | `<src>一波医生来审断，</src>` | 1630 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下条款：</src>` | 1770 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提款，</src>` | 2319 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1623 |
| 12 | `<src>他们</src>` | `<src><\|wait\|></src>` | 2190 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>他能都很疑惑的离开。</src>` | 974 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2270 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 1169 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 904 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是意味着</src>` | 1108 |
| 5 | `<src>所以呢，</src>` | `<src>罪呢，</src>` | 943 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 788 |
| 7 | `<src>所面临的一些</src>` | `<src>所借你的一些</src>` | 1782 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>外积啊、</src>` | 2497 |
| 9 | `<src>也不可能是</src>` | `<src>跟不幸</src>` | 563 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你</src>` | 2009 |
| 11 | `<src><\|wait\|></src>` | `<src>期间就</src>` | 2015 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来</src>` | 1971 |
| 13 | `<src>因此会建议</src>` | `<src>的因子，会建议</src>` | 1832 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 939 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2055 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1886 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1506 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1391 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1508 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 598 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 2410 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 720 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 1962 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 1943 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2139 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1543 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1195 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1916 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150미가 종업었을 </src>` | 1864 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>연봉 미만 으로 </src>` | 1578 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1393 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 254 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1736 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2538 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 해외 로 </src>` | 757 |
| 9 | `<src>걷게 되는데 </src>` | `<src>익을 꺾게 되는데 </src>` | 2216 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1747 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 2385 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 또한 하지 않은 </src>` | 1353 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들을 보이 게 된 거죠. </src>` | 1796 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new, </src>` | 2088 |
| 2 | `<src>There were </src>` | `<src>there, </src>` | 1391 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 873 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1316 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1297 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC, </src>` | 1534 |
| 7 | `<src>Yeah, so </src>` | `<src><\|wait\|></src>` | 467 |
| 8 | `<src>this is just </src>` | `<src>and so this is </src>` | 2496 |
| 9 | `<src>one another place </src>` | `<src>just one another place </src>` | 1092 |
| 10 | `<src>to look at. </src>` | `<src>to look at, </src>` | 1958 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1627 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2069 |
| 13 | `<src>developers or engineers </src>` | `<src>but developers or engineers would </src>` | 1572 |
| 14 | `<src>working on BugRepo </src>` | `<src>expect the kernel modules should be </src>` | 1055 |
| 15 | `<src>should be aware of that. </src>` | `<src>available of that. </src>` | 1194 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1933 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1712 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 1196 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1185 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 916 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1706 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1405 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 1592 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1811 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 2337 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1931 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1831 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1314 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1094 |

---

### Test Example 35 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1975 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1764 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1516 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1066 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 690 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1663 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 </src>` | 1075 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 흘려 </src>` | 1771 |
| 9 | `<src><\|wait\|></src>` | `<src>갔느니라. </src>` | 1450 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1752 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1944 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 2404 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 746 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1758 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 712 |

---

### Test Example 36 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2124 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう寝かせている。</src>` | 1389 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 784 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1224 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今一日を見てる。</src>` | 1069 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 657 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1644 |
| 8 | `<src><\|wait\|></src>` | `<src>遠くに超えている</src>` | 1040 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>船の軌跡よ。</src>` | 1887 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1537 |
| 11 | `<src>長年</src>` | `<src><\|wait\|></src>` | 1846 |
| 12 | `<src>船大工をやってる</src>` | `<src>長年にわだいこをやってる</src>` | 2119 |
| 13 | `<src>が、</src>` | `<src><\|wait\|></src>` | 2401 |
| 14 | `<src>俺は</src>` | `<src>わよりこんなにすごい</src>` | 405 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊線を</src>` | 1723 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 746 |

---

### Test Example 37 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1972 |
| 2 | `<src>我们可以看到的是</src>` | `<src>这一张的部分呢，</src>` | 1672 |
| 3 | `<src>一个在钓鱼</src>` | `<src>我们可以看到的是一个，但</src>` | 1842 |
| 4 | `<src>的人，但是</src>` | `<src>吊人。但是</src>` | 1348 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1675 |
| 6 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1014 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>所以通常逢到这样的一个状况的</src>` | 2133 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1647 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 2175 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 1543 |
| 11 | `<src>钓到鱼，</src>` | `<src><\|wait\|></src>` | 2407 |
| 12 | `<src>它钓不到鱼</src>` | `<src>调到</src>` | 395 |
| 13 | `<src><\|wait\|></src>` | `<src>与它的意识</src>` | 1768 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 717 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2434 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1301 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1123 |
| 4 | `<src><\|wait\|></src>` | `<src>and </src>` | 968 |
| 5 | `<src>and I have ten of them </src>` | `<src>like ten of them </src>` | 1307 |
| 6 | `<src>that I think are </src>` | `<src>that you really </src>` | 1666 |
| 7 | `<src>really important. </src>` | `<src>important. </src>` | 826 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2004 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into </src>` | 1358 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 1754 |
| 11 | `<src>one minute videos </src>` | `<src>I have about one minute videos </src>` | 1703 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 2455 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one </src>` | 1150 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1828 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 799 |

---

### Test Example 39 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1974 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 1490 |
| 3 | `<src><\|wait\|></src>` | `<src>어 Htmel이라고 하는 </src>` | 1320 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 이해 할 수 </src>` | 1265 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 896 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 </src>` | 1694 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1383 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 1645 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1764 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 2393 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1753 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1973 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 797 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1391 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 929 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2266 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1482 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1597 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src><\|wait\|></src>` | 935 |
| 5 | `<src>也就是</src>` | `<src>比较偏向正财的部分。</src>` | 838 |
| 6 | `<src>在事业方面的</src>` | `<src>也就是在事业方面的</src>` | 1731 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩增长所带来的红利</src>` | 2503 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 563 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1998 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 2129 |
| 11 | `<src>这个月</src>` | `<src>这个月也是</src>` | 2072 |
| 12 | `<src>也是不错，只是</src>` | `<src>不错，只是</src>` | 1587 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说，</src>` | 1098 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了</src>` | 1172 |
| 15 | `<src><\|wait\|></src>` | `<src>那么一点。</src>` | 910 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2325 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1393 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>색인 번호 읽어야 </src>` | 1241 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src><\|wait\|></src>` | 1026 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>연세 서름이듯은 차례 도듯은 </src>` | 1412 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느끼 면 </src>` | 1582 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1132 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1858 |
| 9 | `<src>귀신 이 오면 </src>` | `<src><\|wait\|></src>` | 1605 |
| 10 | `<src>물릴 거고 </src>` | `<src>귀신 이 오면 물릴 거고 </src>` | 2439 |
| 11 | `<src>신이 오면 </src>` | `<src>시녀 이면 </src>` | 1571 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 2379 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주려 하니까 </src>` | 953 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1231 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1005 |

---

### Test Example 42 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2178 |
| 2 | `<src>十一二手とか</src>` | `<src>十一・二日とか</src>` | 1665 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 1478 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 958 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 777 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1650 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 476 |
| 8 | `<src>計算ですか</src>` | `<src>時間が</src>` | 2328 |
| 9 | `<src>ね。</src>` | `<src>ですね。</src>` | 580 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1903 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1921 |
| 12 | `<src><\|wait\|></src>` | `<src>十一・二日</src>` | 1614 |
| 13 | `<src>十一二手で</src>` | `<src><\|wait\|></src>` | 2203 |
| 14 | `<src>あの</src>` | `<src>であの</src>` | 1268 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1269 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 1051 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2253 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1457 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1423 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 865 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? </src>` | 1201 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1953 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 2445 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. </src>` | 1177 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 1938 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, </src>` | 1665 |
| 11 | `<src>That's another level of </src>` | `<src>did you graduate? </src>` | 2499 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 1178 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1855 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 915 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 788 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2279 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1593 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけではなくて、</src>` | 1756 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1386 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1629 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも、</src>` | 482 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルの書いてあと</src>` | 2591 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>これやつは</src>` | 1352 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコードが</src>` | 1835 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成されて、それが</src>` | 2076 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 2428 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 602 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1236 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1138 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 961 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ</src>` | 402 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2120 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1405 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1229 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 1075 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct, </src>` | 1340 |
| 6 | `<src>but the reality </src>` | `<src><\|wait\|></src>` | 1709 |
| 7 | `<src>is is that </src>` | `<src>but the reality is is that </src>` | 1736 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1372 |
| 9 | `<src>block and because the </src>` | `<src>block and because </src>` | 2000 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 2090 |
| 11 | `<src>changed from 20 </src>` | `<src><\|wait\|></src>` | 2037 |
| 12 | `<src>years ago, </src>` | `<src>changed from twenty years ago, </src>` | 1724 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1049 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1157 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point is being </src>` | 1146 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 634 |

---

### Test Example 46 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 2315 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어 어찌 보면 </src>` | 1598 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1881 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1362 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>이 동생 이자 </src>` | 1672 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1035 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 1978 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1253 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1828 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1772 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 2356 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1018 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1211 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것 </src>` | 1112 |
| 15 | `<src>내려놓 고 </src>` | `<src>잘 넣어 놓고 </src>` | 1038 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 622 |

---

### Test Example 47 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 2350 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 1462 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 해맨입니다. </src>` | 1373 |
| 4 | `<src><\|wait\|></src>` | `<src>이 운전 을 할 건 </src>` | 1233 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 897 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>거러 거러 다니 고는 </src>` | 1903 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 으로 가면 </src>` | 2493 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 997 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장렬이에요. </src>` | 2155 |
| 10 | `<src>또 장렬이에요. </src>` | `<src><\|wait\|></src>` | 1674 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 재밌 겠네요. </src>` | 2839 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 731 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1209 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>무렵 하였고요. 그거 는 </src>` | 1290 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>잘한 것 같아요. </src>` | 1101 |
| 16 | `<src><\|wait\|></src>` | `<src>예. </src>` | 664 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계속 뭐 </src>` | 2244 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 </src>` | 1503 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 2111 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1289 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1599 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트예요. </src>` | 536 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트가 </src>` | 2525 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>오고 </src>` | 1547 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2211 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1742 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 2456 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라는 사람 이 </src>` | 349 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1282 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 크리티에서 </src>` | 1243 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 997 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 748 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2236 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手的</src>` | 1682 |
| 3 | `<src>的感情或</src>` | `<src>感情或</src>` | 1316 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1168 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 777 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1701 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 1317 |
| 8 | `<src>会听到人们</src>` | `<src>好经常会听到人们这样说：</src>` | 1734 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1751 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2260 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1446 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 2427 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 883 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1293 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 917 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 741 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 686 |

---

### Test Example 50 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 2989 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 677 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 1956 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1431 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1679 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1315 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1538 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 1565 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 2522 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1568 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 움직이 기 때문 에 </src>` | 2497 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>항상 </src>` | 947 |
| 13 | `<src>요 시총이 </src>` | `<src>뉴스 시총이 </src>` | 1164 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1140 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨봐야 될 것 </src>` | 743 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 492 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1945 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1585 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 내놓 았습니다. </src>` | 1955 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 1264 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>이 로쿠자 의 분석 을 보시면, </src>` | 1700 |
| 6 | `<src>소니가 </src>` | `<src>Sony가 </src>` | 471 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 60 뒤의 </src>` | 2504 |
| 8 | `<src>파이프 를 </src>` | `<src>FPD 파이프를 </src>` | 1709 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2400 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것이 로프 인다. </src>` | 1726 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2224 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>X 박스 시리즈 </src>` | 1261 |
| 13 | `<src><\|wait\|></src>` | `<src>X에서도 없는 </src>` | 1204 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1094 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>SD가 여기 도 없다. </src>` | 559 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 499 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1943 |
| 2 | `<src>首次觉知到</src>` | `<src>佛陀一得</src>` | 1622 |
| 3 | `<src>那个现象：</src>` | `<src>所知觉知到的那个现象，</src>` | 1962 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1296 |
| 5 | `<src><\|wait\|></src>` | `<src>美当我们</src>` | 1354 |
| 6 | `<src>处于爱之中，</src>` | `<src>处于爱之中，</src>` | 552 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱，</src>` | 1931 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 916 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入</src>` | 1707 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2278 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨在场所的时候，</src>` | 1477 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱，</src>` | 2359 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 390 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成</src>` | 1203 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1149 |
| 16 | `<src>那个钟摆</src>` | `<src>恨那个钟摆，</src>` | 1134 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在移动。</src>` | 599 |
| 18 | `<src>继续在移动。</src>` | `<src><\|wait\|></src>` | 277 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2161 |
| 2 | `<src>Also, </src>` | `<src>Also, you will not </src>` | 1674 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to </src>` | 1476 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 946 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 882 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1650 |
| 7 | `<src>So, if </src>` | `<src><\|wait\|></src>` | 1071 |
| 8 | `<src>you get into </src>` | `<src>So, if you get into </src>` | 1927 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1546 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 2247 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1675 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2519 |
| 13 | `<src>you need to let us know, </src>` | `<src>we'll </src>` | 893 |
| 14 | `<src>and we can see about </src>` | `<src>now, and we can see </src>` | 1293 |
| 15 | `<src><\|wait\|></src>` | `<src>about moving those </src>` | 946 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>media files and then making sure </src>` | 887 |
| 17 | `<src>get backed up </src>` | `<src><\|wait\|></src>` | 533 |
| 18 | `<src>properly. </src>` | `<src>it gets backed up properly. </src>` | 514 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 2122 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1315 |
| 3 | `<src>is hungry. </src>` | `<src>is a hungry, </src>` | 1414 |
| 4 | `<src>He knows that </src>` | `<src>he knows that </src>` | 976 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been out there, </src>` | 1138 |
| 6 | `<src><\|wait\|></src>` | `<src>been in the wilderness </src>` | 1743 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>for forty days, that he's hungry, </src>` | 2574 |
| 8 | `<src>And so he says </src>` | `<src>and so he sends </src>` | 950 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus. He said," </src>` | 2017 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>If you are the Son of God, </src>` | 1846 |
| 11 | `<src><\|wait\|></src>` | `<src>prove it." </src>` | 2287 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1381 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1469 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with </src>` | 991 |
| 15 | `<src>temptation? </src>` | `<src>that temptation?" </src>` | 1079 |
| 16 | `<src><\|wait\|></src>` | `<src>Man </src>` | 519 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan </src>` | 275 |
| 18 | `<src>by bread alone. </src>` | `<src>led by bread alone. </src>` | 517 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2359 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1397 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 979 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1224 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR </src>` | 1285 |
| 6 | `<src><\|wait\|></src>` | `<src>field being of critical </src>` | 1531 |
| 7 | `<src>being of critical importance </src>` | `<src>importance </src>` | 398 |
| 8 | `<src>versus variant </src>` | `<src>versus, </src>` | 2376 |
| 9 | `<src><\|wait\|></src>` | `<src>a variant database </src>` | 519 |
| 10 | `<src>databases, </src>` | `<src>system, </src>` | 1563 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2474 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that </src>` | 1630 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree </src>` | 2289 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 926 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these </src>` | 1354 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1013 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 572 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 713 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 455 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2123 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1628 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1411 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 1073 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到</src>` | 860 |
| 6 | `<src>的部分。</src>` | `<src>一个是客厅的部分，</src>` | 1607 |
| 7 | `<src>那客厅一般</src>` | `<src><\|wait\|></src>` | 981 |
| 8 | `<src>都是属于</src>` | `<src>它客厅一般都是</src>` | 1977 |
| 9 | `<src>我们</src>` | `<src>属于我们</src>` | 1566 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 1854 |
| 11 | `<src><\|wait\|></src>` | `<src>在休息的地方，所以呢，</src>` | 2100 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src><\|wait\|></src>` | 2269 |
| 13 | `<src>也会反映的是</src>` | `<src>这身体的部分呢，</src>` | 505 |
| 14 | `<src>你需要给自己</src>` | `<src>反映的是你需要给自己</src>` | 1806 |
| 15 | `<src>一点时间，</src>` | `<src><\|wait\|></src>` | 800 |
| 16 | `<src>可以好好的</src>` | `<src>一点时间可以</src>` | 971 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>好好地坐下来休息，</src>` | 740 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 506 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的吗？</src>` | 335 |
| 20 | `<src>啊，</src>` | `<src>哦，</src>` | 154 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 342 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2385 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1478 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 863 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1254 |
| 5 | `<src>came along </src>` | `<src>came along </src><br><src>along </src>` | 1432 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1717 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 2583 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 746 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 2117 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 1764 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 2113 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1551 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1194 |
| 14 | `<src>the consensus </src>` | `<src><\|wait\|></src>` | 1167 |
| 15 | `<src><\|wait\|></src>` | `<src>the consensus </src>` | 933 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 710 |
| 17 | `<src><\|wait\|></src>` | `<src>So, </src>` | 511 |
| 18 | `<src>So you have some </src>` | `<src><\|wait\|></src>` | 496 |
| 19 | `<src>federal judges </src>` | `<src>you have some federal judges </src>` | 366 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 453 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 279 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 2000 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1481 |
| 3 | `<src>and they often </src>` | `<src><\|wait\|></src>` | 1226 |
| 4 | `<src>show up to </src>` | `<src>and they often show up </src>` | 1053 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1183 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 1712 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1189 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1686 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1535 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 1833 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1977 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 2552 |
| 13 | `<src>they also hate </src>` | `<src><\|wait\|></src>` | 400 |
| 14 | `<src>meaningless conversations </src>` | `<src>they also hate meaningless conversations </src>` | 1865 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 799 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 927 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 676 |
| 18 | `<src>They also love to </src>` | `<src><\|wait\|></src>` | 324 |
| 19 | `<src>play </src>` | `<src>They also love to play </src>` | 259 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, </src>` | 376 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 389 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>and never shy away from a debate. </src>` | 373 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 194 |
| 24 | `<src><\|wait\|></src>` | `<src>ENTP stands for </src>` | 308 |
| 25 | `<src>ENTP stands for </src>` | `<src>Extraverted, Intuitive, Feeling, Thinking, Rational. </src>` | 361 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 3055 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>경무를 거부 한 </src>` | 755 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보를 </src>` | 1710 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1351 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1589 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 482 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2429 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1033 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1930 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1648 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 2107 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1552 |
| 13 | `<src><\|wait\|></src>` | `<src>더루내놓고 </src>` | 1118 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>윤석열 후보 를 </src>` | 1302 |
| 15 | `<src><\|wait\|></src>` | `<src>떨어뜨리 겠다는 뚜끼를 </src>` | 1130 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>품은 공격 성을 </src>` | 510 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 507 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 472 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 362 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴발 </src>` | 420 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 청산 </src>` | 277 |
| 22 | `<src><\|wait\|></src>` | `<src>낫건. </src>` | 266 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당이 </src>` | 234 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 학이 </src>` | 185 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 332 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2102 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 1312 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってるみたいです。なので</src>` | 1306 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>ここのね</src>` | 1128 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>プロフェッショナルホテル</src>` | 1367 |
| 6 | `<src>も</src>` | `<src>も</src>` | 1569 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 996 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1843 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1351 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 1751 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドーストーンホテル</src>` | 1842 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まっていみたいな</src>` | 2551 |
| 13 | `<src>なっていう方はですね</src>` | `<src>っていう方はですね</src>` | 908 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1262 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>まあいいんじゃないか</src>` | 1226 |
| 16 | `<src><\|wait\|></src>` | `<src>なと。はい。</src>` | 1097 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思います。</src>` | 596 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね</src>` | 262 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 439 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 347 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 321 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 202 |
| 23 | `<src>レベルのね</src>` | `<src>そんな辺りのね</src>` | 231 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあ</src>` | 270 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 304 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 303 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 162 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 143 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は。</src>` | 160 |
