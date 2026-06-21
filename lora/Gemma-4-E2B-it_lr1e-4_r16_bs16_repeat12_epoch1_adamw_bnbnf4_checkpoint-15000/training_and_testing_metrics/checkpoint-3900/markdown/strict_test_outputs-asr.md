# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9526
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3642
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
  - PROCESS_TIME_MS_AVG: 1436.2390
  - PROCESS_TIME_MS_P50: 1394.0730
  - PROCESS_TIME_MS_P95: 2485.2860
  - PROCESS_TIME_MS_MAX: 3278.3550

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
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1724 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 933 |
| 3 | `<src>これなんかまだ</src>` | `<src>子供がまだ</src>` | 1583 |
| 4 | `<src>一年生ですからね。</src>` | `<src>1年生ですからね。</src>` | 1184 |
| 5 | `<src>この時点で</src>` | `<src>あの時点で</src>` | 1291 |
| 6 | `<src>こう短く</src>` | `<src>こう短い間隔</src>` | 544 |
| 7 | `<src>剪定を</src>` | `<src>線っていうのを</src>` | 1365 |
| 8 | `<src><\|wait\|></src>` | `<src>こう保持して</src>` | 2422 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>いただけると</src>` | 315 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 1840 |
| 11 | `<src>大した。</src>` | `<src>だいした。</src>` | 2396 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>怪得</src>` | 2182 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>嵩子儿这儿，</src>` | 1293 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个游行</src>` | 1569 |
| 4 | `<src>然后</src>` | `<src>也很大。</src>` | 882 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 1299 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放假</src>` | 1403 |
| 7 | `<src>儿核桃</src>` | `<src>隔热汤儿，</src>` | 581 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2352 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>这里</src>` | 979 |
| 10 | `<src>这种核桃</src>` | `<src>这这种</src>` | 2273 |
| 11 | `<src>仁儿。</src>` | `<src>隔热汤儿。</src>` | 1590 |

---

### Test Example 3 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2047 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘撒完以后呢，</src>` | 2192 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的冶炼轻呢</src>` | 1219 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了。</src>` | 404 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1270 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在</src>` | 1532 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 706 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 2149 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 1186 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是</src>` | 2293 |
| 11 | `<src>抑郁状态。</src>` | `<src>所谓的抑郁状态。</src>` | 1394 |

---

### Test Example 4 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1846 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptitude, </src>` | 1239 |
| 3 | `<src>촉발 시키고 </src>` | `<src>욕팔지기 고 </src>` | 1881 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 677 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1350 |
| 6 | `<src><\|wait\|></src>` | `<src>힘을 </src>` | 1511 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>조기 능력을 </src>` | 910 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1932 |
| 9 | `<src>박한상과 </src>` | `<src>박찬과 </src>` | 1280 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들은 </src>` | 2832 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>이다. </src>` | 784 |

---

### Test Example 5 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1983 |
| 2 | `<src>옹심이, </src>` | `<src>용신이 </src>` | 1109 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1734 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용신이에요. </src>` | 944 |
| 5 | `<src>옹심이가 </src>` | `<src>용신이 가 </src>` | 1377 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1707 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. </src>` | 1805 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 858 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1554 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해당 으로 </src>` | 2517 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 맞는 것 같아요. </src>` | 974 |

---

### Test Example 6 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2119 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是</src>` | 2102 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 730 |
| 4 | `<src>用我们深深的</src>` | `<src><\|wait\|></src>` | 910 |
| 5 | `<src>爱浇水、</src>` | `<src>深深的爱交水</src>` | 1456 |
| 6 | `<src>施肥，</src>` | `<src>十个，</src>` | 1447 |
| 7 | `<src>给足</src>` | `<src>给他</src>` | 824 |
| 8 | `<src>孩子心理营养，</src>` | `<src>子心灵营养，</src>` | 2033 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1671 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>给他耐心等等</src>` | 2562 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 832 |

---

### Test Example 7 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2204 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1168 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1474 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1035 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1304 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 1653 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 953 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1903 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1327 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모르 랐던 </src>` | 2987 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은 </src>` | 754 |

---

### Test Example 8 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1998 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 2310 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 907 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有一个</src>` | 545 |
| 5 | `<src><\|wait\|></src>` | `<src>师傅指导到</src>` | 1416 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1676 |
| 7 | `<src>处于中间，</src>` | `<src>如何处于中间，</src>` | 1692 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 959 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 2043 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2327 |
| 11 | `<src>一个师父。</src>` | `<src>一个师傅，</src>` | 781 |

---

### Test Example 9 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1947 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜을 </src>` | 1248 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주게 달라 이거 주고 내가 </src>` | 1950 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주길 넣어 </src>` | 549 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>주도 로 아스다. 다른 잔찜을 </src>` | 1561 |
| 6 | `<src>죽여 달라 </src>` | `<src>주게 달라 </src>` | 1544 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해줘야 되냐 내가 </src>` | 1886 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그런 소리 안 듣고 </src>` | 844 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐 </src>` | 2168 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아 </src>` | 2121 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 774 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying important </src>` | 1845 |
| 2 | `<src>Did very important research </src>` | `<src>research </src>` | 948 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1561 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1217 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1359 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 1788 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 2211 |
| 8 | `<src><\|wait\|></src>` | `<src>of the happiest </src>` | 493 |
| 9 | `<src>of the happiest people </src>` | `<src>people </src>` | 1382 |
| 10 | `<src>out there, </src>` | `<src>out there, people who feel </src>` | 2928 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 886 |

---

### Test Example 11 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1761 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1078 |
| 3 | `<src>Drop into </src>` | `<src>Drop into your body. </src>` | 1981 |
| 4 | `<src>your body. </src>` | `<src>Where does </src>` | 667 |
| 5 | `<src>Where does the tension </src>` | `<src>the tension </src>` | 1271 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1653 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? Is it a </src>` | 1134 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>tension in your chest? </src>` | 1726 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them, well, </src>` | 2166 |
| 10 | `<src><\|wait\|></src>` | `<src>lung capacity. </src>` | 2308 |
| 11 | `<src>language are you using? </src>` | `<src>Are you using </src>` | 1147 |

---

### Test Example 12 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1898 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 2197 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 753 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 859 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1297 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们学校这个状况，</src>` | 1678 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1528 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>怎么都把它扛下来。</src>` | 1265 |
| 9 | `<src>独立承担。</src>` | `<src>不离不伴，</src>` | 2524 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言</src>` | 1929 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该是不属情。</src>` | 1471 |

---

### Test Example 13 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2058 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1117 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 1476 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1080 |
| 5 | `<src>ゴッホ、</src>` | `<src>剛法、</src>` | 1312 |
| 6 | `<src>ゴーギャン、</src>` | `<src>剛厳、</src>` | 547 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1380 |
| 8 | `<src>セザンヌ、</src>` | `<src>精悍、</src>` | 2446 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 516 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 2638 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 1784 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも</src>` | 1502 |

---

### Test Example 14 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうですよ。</src>` | 1866 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 890 |
| 3 | `<src><\|wait\|></src>` | `<src>天気</src>` | 1601 |
| 4 | `<src>テキという設備寺が</src>` | `<src>豊水寺が</src>` | 1188 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたが、</src>` | 848 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 655 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1565 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井家義の仕組み</src>` | 1106 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 1663 |
| 10 | `<src>は五経、</src>` | `<src>五本、</src>` | 1295 |
| 11 | `<src><\|wait\|></src>` | `<src>豊水寺</src>` | 2590 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 1068 |
| 13 | `<src>です。</src>` | `<src>五本です。</src>` | 1628 |

---

### Test Example 15 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1736 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到我</src>` | 1094 |
| 3 | `<src>回到我生活</src>` | `<src>生活的一个轨道，</src>` | 1742 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>哦，</src>` | 889 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1295 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好自在的</src>` | 1475 |
| 7 | `<src>在做热汤</src>` | `<src>那时候，在座日航</src>` | 529 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>日航的</src>` | 2375 |
| 9 | `<src><\|wait\|></src>` | `<src>时候，</src>` | 1116 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时背对座</src>` | 2760 |
| 11 | `<src>小小的愿望</src>` | `<src>座座骑一个小小的小小</src>` | 1274 |
| 12 | `<src>哈。</src>` | `<src>的愿望哈。</src>` | 1643 |

---

### Test Example 16 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1935 |
| 2 | `<src><\|wait\|></src>` | `<src>이거 너무 </src>` | 984 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>저열한 데일 수 있지만 </src>` | 2015 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 866 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 1359 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 프로 </src>` | 1706 |
| 7 | `<src>뭐 있고 </src>` | `<src>하고 있고 나만 </src>` | 2392 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>이 보살 로 </src>` | 412 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 프로하고 우주 가 </src>` | 3143 |
| 10 | `<src>지금 나한테 </src>` | `<src>진짜 보살이 라는데 </src>` | 1687 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살이 라는데. </src>` | 1786 |

---

### Test Example 17 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1884 |
| 2 | `<src><\|wait\|></src>` | `<src>涉及到</src>` | 883 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二classList</src>` | 1624 |
| 4 | `<src>服务</src>` | `<src>和服务</src>` | 1158 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 618 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1018 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1539 |
| 8 | `<src><\|wait\|></src>` | `<src>呃，</src>` | 1122 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做维向运动</src>` | 1649 |
| 10 | `<src>发现</src>` | `<src>后世几点，你会发现</src>` | 1793 |
| 11 | `<src>给微信公众号评分</src>` | `<src>维向运动</src>` | 2462 |
| 12 | `<src>的新榜反而</src>` | `<src>形成了新绑</src>` | 760 |
| 13 | `<src>火了。</src>` | `<src>反文化了。</src>` | 2344 |

---

### Test Example 18 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2127 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 1110 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1716 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 934 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1331 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1557 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 908 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1971 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1347 |
| 10 | `<src><\|wait\|></src>` | `<src>連絡の</src>` | 2508 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>内側がありますので</src>` | 1163 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 2440 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1760 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 1250 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 2007 |
| 4 | `<src><\|wait\|></src>` | `<src>之间有着某种</src>` | 553 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>联系，</src>` | 1378 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1704 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1692 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天</src>` | 1016 |
| 9 | `<src><\|wait\|></src>` | `<src>夜里开始的？</src>` | 1958 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2413 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子</src>` | 782 |
| 12 | `<src>连篇。</src>` | `<src>思绪连篇。</src>` | 2443 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1853 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1182 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1769 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 833 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1471 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1606 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 2097 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, like </src>` | 623 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 2299 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets </src>` | 2136 |
| 11 | `<src>or gets used to make </src>` | `<src>used to make </src>` | 1235 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1990 |

---

### Test Example 21 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2151 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1197 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. Learn to </src>` | 1886 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>answer to repeat. Find out </src>` | 740 |
| 5 | `<src>Find what you're good at </src>` | `<src>where you're good at. </src>` | 1494 |
| 6 | `<src>and do more of it. </src>` | `<src>And do more of it. </src>` | 1675 |
| 7 | `<src><\|wait\|></src>` | `<src>And when you're not good </src>` | 2472 |
| 8 | `<src>And what you're not good at, </src>` | `<src>at it, </src>` | 1206 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get to people around you to help you with. </src>` | 3278 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1107 |
| 11 | `<src>And until next time. </src>` | `<src>And and tell next time, </src>` | 2263 |

---

### Test Example 22 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2182 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1107 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1860 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 783 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1272 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1570 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 549 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2215 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 890 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 2537 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1347 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game dot scored array. </src>` | 1541 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1685 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1936 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel, and </src>` | 2091 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 995 |
| 4 | `<src><\|wait\|></src>` | `<src>in a PhD for the </src>` | 701 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>finance </src>` | 1283 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Ph.D. of psychology. </src>` | 1765 |
| 7 | `<src><\|wait\|></src>` | `<src>Here at </src>` | 1354 |
| 8 | `<src>here at the ANU, </src>` | `<src>Yale, </src>` | 1324 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 2501 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 2252 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate consultancy </src>` | 1400 |
| 12 | `<src>corporate consultancy. </src>` | `<src>and. </src>` | 1681 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1836 |
| 2 | `<src>映画でですね、</src>` | `<src>AAアンデスに</src>` | 1142 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1711 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>霊性速度かどうかっていうの</src>` | 1008 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに</src>` | 1322 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>AAの</src>` | 1647 |
| 7 | `<src>ことで、あの</src>` | `<src>ランクを調べて、あの</src>` | 1652 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その霊性速度かどうかっていうの</src>` | 1260 |
| 9 | `<src>保証する、生息である</src>` | `<src>調査する</src>` | 2328 |
| 10 | `<src>ことを保証する</src>` | `<src>速度であること保証する</src>` | 2109 |
| 11 | `<src>といったような</src>` | `<src>といったらその使い方をされています。</src>` | 1545 |
| 12 | `<src>使い方をされます。</src>` | `<src><\|wait\|></src>` | 1680 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1935 |
| 2 | `<src>一切正常，</src>` | `<src><\|wait\|></src>` | 1129 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>一切正常和平烂掉，</src>` | 1985 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 689 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持不开道，</src>` | 1356 |
| 6 | `<src>期间</src>` | `<src>期限大概有</src>` | 1495 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 591 |
| 8 | `<src>来诊断，</src>` | `<src>十二个月以内</src>` | 2235 |
| 9 | `<src>一下敲腿，</src>` | `<src>判断以下敲腿</src>` | 1296 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿</src>` | 2517 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题，</src>` | 1078 |
| 12 | `<src>他们</src>` | `<src>当然</src>` | 1372 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 1732 |

---

### Test Example 26 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだん</src>` | 2223 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が</src>` | 1056 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1872 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>おしゃれロカデカで</src>` | 841 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1307 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1782 |
| 7 | `<src>すごい</src>` | `<src>すごい理想移り越し</src>` | 2519 |
| 8 | `<src>自己意識高いし、</src>` | `<src>だから、ぜひ</src>` | 1219 |
| 9 | `<src>自分で</src>` | `<src>ぜひぜひ</src>` | 2359 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>ちょっとご相談の方ぜひ</src>` | 1453 |
| 11 | `<src>傾向が強いので、</src>` | `<src>結構強いので</src>` | 1600 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1498 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2154 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th Amendment </src>` | 2106 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>and, </src>` | 708 |
| 4 | `<src>and to explore its </src>` | `<src>to explore its </src>` | 909 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1295 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1438 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 551 |
| 8 | `<src>change can happen </src>` | `<src>happen, </src>` | 2399 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1350 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2608 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1008 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, I'm </src>` | 1944 |
| 13 | `<src>myriad. </src>` | `<src>buried. </src>` | 1364 |

---

### Test Example 28 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2124 |
| 2 | `<src>です。</src>` | `<src>ギア</src>` | 830 |
| 3 | `<src>ギアが</src>` | `<src>です。ギアが</src>` | 1680 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1215 |
| 5 | `<src><\|wait\|></src>` | `<src>逆が逆ができなくなってしまう</src>` | 1430 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので</src>` | 1478 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 635 |
| 8 | `<src>役ねじの</src>` | `<src>ヤクネ字の</src>` | 2282 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1449 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いているっていうこと</src>` | 2778 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 810 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1992 |
| 13 | `<src>分解完了。</src>` | `<src>はい分解完了。</src>` | 1288 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要</src>` | 1993 |
| 2 | `<src>要提醒大家，</src>` | `<src>提醒大家，</src>` | 849 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1685 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1184 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1301 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 532 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1359 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊</src>` | 1692 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 984 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是一夜之间</src>` | 1919 |
| 11 | `<src><\|wait\|></src>` | `<src>就演变出来。</src>` | 2485 |
| 12 | `<src>演变出来的，</src>` | `<src><\|wait\|></src>` | 1187 |
| 13 | `<src>因此会建议</src>` | `<src>因此，</src>` | 2040 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>会建议属鸡的朋友呢，</src>` | 1120 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 1885 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>이것 들은 </src>` | 1243 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 인슐린과 </src>` | 1949 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 588 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 </src>` | 1370 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1707 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 2312 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 512 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2325 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 2084 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1400 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1837 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1428 |

---

### Test Example 31 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or or if you have </src>` | 1988 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 1048 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1478 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1115 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1309 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1069 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 840 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, is </src>` | 2602 |
| 9 | `<src>is this word </src>` | `<src>this word </src>` | 1947 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2575 |
| 11 | `<src><\|wait\|></src>` | `<src>p, </src>` | 1311 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double lam? I don't know. </src>` | 2125 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1492 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>达到了一个</src>` | 1737 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>天头，</src>` | 979 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1532 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了天头之后，</src>` | 1194 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1408 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1500 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 526 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说：“哎，</src>` | 2392 |
| 9 | `<src><\|wait\|></src>` | `<src>那我再继续操作</src>` | 1352 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦。”</src>` | 2608 |
| 11 | `<src><\|wait\|></src>` | `<src>所以</src>` | 813 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>我们要</src>` | 1403 |
| 13 | `<src><\|wait\|></src>` | `<src>怎么会这么讲？因为呢，</src>` | 1872 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1416 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1834 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们看到的是</src>` | 1191 |
| 3 | `<src>一个在钓鱼</src>` | `<src><\|wait\|></src>` | 1602 |
| 4 | `<src>的人，但是</src>` | `<src>一个在跳舞的人，但是</src>` | 991 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>他是属于逆向的，</src>` | 1494 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1428 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>汤浅朋友像</src>` | 1095 |
| 8 | `<src>时候，就要去</src>` | `<src>这样的一个状况</src>` | 1736 |
| 9 | `<src>特别注意，</src>` | `<src>需要去特别注意的是</src>` | 2236 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能</src>` | 2147 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够调到</src>` | 801 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与他跳不到</src>` | 2414 |
| 13 | `<src><\|wait\|></src>` | `<src>与你的意识</src>` | 938 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 1193 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new, </src>` | 1946 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1194 |
| 3 | `<src><\|wait\|></src>` | `<src>there are such </src>` | 1614 |
| 4 | `<src>such interfaces before, </src>` | `<src>interposes before, </src>` | 964 |
| 5 | `<src><\|wait\|></src>` | `<src>and future </src>` | 1379 |
| 6 | `<src>netfilter, TC. </src>` | `<src>TC </src>` | 1430 |
| 7 | `<src>Yeah, so </src>` | `<src>and so </src>` | 429 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 2385 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place </src>` | 1271 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2699 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 992 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 1440 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1658 |
| 14 | `<src>working on BugRepo </src>` | `<src>who work on Babel should be </src>` | 1602 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 755 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1795 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개 가 </src>` | 2078 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중오버에서 100미만 으로 </src>` | 1543 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 619 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 918 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1699 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>자그럽 기업 들은 성장 하거나 </src>` | 2609 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 해외 로 </src>` | 2630 |
| 9 | `<src>걷게 되는데 </src>` | `<src>익을 꺾게 되는데 </src>` | 2234 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 에 소기업 들은 </src>` | 1662 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1542 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>패 업도 하지 않은 </src>` | 1536 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 881 |

---

### Test Example 36 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1957 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 2164 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 1021 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较正财的部分</src>` | 589 |
| 5 | `<src>也就是</src>` | `<src>又都在</src>` | 1351 |
| 6 | `<src>在事业方面的</src>` | `<src>事业方面</src>` | 1562 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>的业绩增长所带来的红利</src>` | 1282 |
| 8 | `<src>与收入的</src>` | `<src>与收入的提升</src>` | 1572 |
| 9 | `<src>提升。如果是在</src>` | `<src>呢，</src>` | 1660 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>如果它的投资理财方面</src>` | 2784 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1240 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错的，</src>` | 1915 |
| 13 | `<src>相对正财来说就</src>` | `<src>只是相对正财来说，</src>` | 1189 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了一点</src>` | 1255 |
| 15 | `<src><\|wait\|></src>` | `<src>。</src>` | 847 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>授業</src>` | 1979 |
| 2 | `<src>十一二手とか</src>` | `<src>一日とか</src>` | 897 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 1630 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1171 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1293 |
| 6 | `<src>一秒に</src>` | `<src>一日に</src>` | 403 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1543 |
| 8 | `<src>計算ですか</src>` | `<src>時間ですかね。</src>` | 2441 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 1046 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2398 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1271 |
| 12 | `<src><\|wait\|></src>` | `<src>十一日</src>` | 1363 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1746 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 979 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1392 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 942 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2139 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1228 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1561 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 891 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1413 |
| 6 | `<src>that I think are </src>` | `<src>that you really </src>` | 1592 |
| 7 | `<src>really important. </src>` | `<src>important </src>` | 1029 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1767 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 1960 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 2534 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 1123 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 2041 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one. </src>` | 1198 |
| 14 | `<src>that cover each one </src>` | `<src>You know, </src>` | 1142 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1057 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 2095 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>蒸らせてやれ。</src>` | 1291 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1412 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 996 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>火通してみる。</src>` | 1355 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1514 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 475 |
| 8 | `<src><\|wait\|></src>` | `<src>遠を超えている</src>` | 2374 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈火勢気よ。</src>` | 1248 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2437 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1115 |
| 12 | `<src>船大工をやってる</src>` | `<src>船出を行ってる</src>` | 1377 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 1734 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1477 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 882 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 1040 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1820 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 2207 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1021 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 574 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1332 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1679 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1207 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 1593 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2198 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2235 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1297 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1974 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1501 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 890 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1092 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2167 |
| 2 | `<src><\|wait\|></src>` | `<src>선무라 낄 </src>` | 1231 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>거야. </src>` | 1611 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 </src>` | 922 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋든 자들이 </src>` | 1367 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>돋든 내기 멈이야. </src>` | 1910 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 </src>` | 2331 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>한들어서 같이 놀자는 거야. </src>` | 545 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 3097 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1300 |
| 11 | `<src>신이 오면 </src>` | `<src>선이 오면 너 </src>` | 1443 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>지켜 주라고 </src>` | 1728 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주려니까 </src>` | 1512 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 846 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1126 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2092 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1186 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1760 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 777 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 1413 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1571 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1101 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you </src>` | 1747 |
| 9 | `<src>to college, </src>` | `<src>go to college? </src>` | 1811 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, did you graduate? </src>` | 2743 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level </src>` | 1440 |
| 12 | `<src>attainment. </src>` | `<src>of attainment. </src>` | 1750 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now. </src>` | 1654 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you </src>` | 857 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1159 |

---

### Test Example 43 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2085 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 2066 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうだけじゃなくて、</src>` | 1124 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 601 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1447 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも</src>` | 1528 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルの書いてあと</src>` | 1397 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それは</src>` | 1347 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコードがそっから</src>` | 1541 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されるって、それが</src>` | 2797 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 838 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が</src>` | 2397 |
| 13 | `<src>構造になっているからです。</src>` | `<src>行われるっていうところに</src>` | 979 |
| 14 | `<src><\|wait\|></src>` | `<src>なっているから</src>` | 1192 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 751 |
| 16 | `<src>じゃあ。</src>` | `<src>はいじゃあ</src>` | 1102 |

---

### Test Example 44 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1743 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 999 |
| 3 | `<src><\|wait\|></src>` | `<src>HTML이라고 하는 </src>` | 1561 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 이해 할 수 </src>` | 1223 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1426 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 이해 할 수 </src>` | 1841 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2350 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 1025 |
| 9 | `<src>문법 에 </src>` | `<src><\|wait\|></src>` | 2463 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>문법 의 뭐랄게 우리 가 이제 </src>` | 1710 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 2231 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1153 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1360 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1045 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 869 |

---

### Test Example 45 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2108 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 996 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1873 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 904 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1362 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1708 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 1518 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1229 |
| 9 | `<src><\|wait\|></src>` | `<src>저희 가 </src>` | 1753 |
| 10 | `<src>책임감 보다는 </src>` | `<src>정말 뭐다 는 </src>` | 2641 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 830 |
| 12 | `<src>자기 스스로 </src>` | `<src>좀 </src>` | 2314 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1001 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1315 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 964 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 </src>` | 905 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수가 </src>` | 1926 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 1169 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 2130 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이러 면 개형 주도 </src>` | 597 |
| 5 | `<src>큰 폭의 </src>` | `<src>또 </src>` | 1193 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만 </src>` | 1688 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1076 |
| 8 | `<src>이 가벼운 </src>` | `<src>가벼운 </src>` | 1671 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1395 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2768 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 움직 이기 </src>` | 890 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>때문 에 </src>` | 2363 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 리 초기 </src>` | 1111 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목을 </src>` | 1356 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 </src>` | 1007 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 1013 |

---

### Test Example 47 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2211 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 1177 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맨이다. </src>` | 2002 |
| 4 | `<src><\|wait\|></src>` | `<src>운전을 하고 </src>` | 555 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 1416 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>걸어 걸어 다니 고는 </src>` | 1684 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 으로 가면 </src>` | 2220 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 503 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장렬이에요. </src>` | 2707 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 1731 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>시간 이 </src>` | 1195 |
| 12 | `<src>대신 에 </src>` | `<src>또 대신 에 이제 </src>` | 2039 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1229 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>무료 를 그거 는 </src>` | 1151 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>다인 것 같아요. </src>` | 1141 |
| 16 | `<src><\|wait\|></src>` | `<src>예. </src>` | 705 |

---

### Test Example 48 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>Fourth一的</src>` | 1782 |
| 2 | `<src>首次觉知到</src>` | `<src>手指</src>` | 954 |
| 3 | `<src>那个现象：</src>` | `<src>觉得到了那个现象，</src>` | 1728 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 995 |
| 5 | `<src><\|wait\|></src>` | `<src>美登我们</src>` | 1314 |
| 6 | `<src>处于爱之中，</src>` | `<src>处于爱之中</src>` | 856 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱。</src>` | 945 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1097 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时</src>` | 1638 |
| 10 | `<src><\|wait\|></src>` | `<src>进入恨</src>` | 1773 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上</src>` | 2424 |
| 12 | `<src>它是爱；</src>` | `<src>的时候他撒爱，</src>` | 870 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 2385 |
| 14 | `<src>它就变成恨。</src>` | `<src>他就变成</src>` | 977 |
| 15 | `<src><\|wait\|></src>` | `<src>恨，</src>` | 1304 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆。</src>` | 703 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 1035 |
| 18 | `<src>继续在移动。</src>` | `<src>移动。</src>` | 533 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1746 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1268 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 했었 습니다. </src>` | 2159 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자예요. </src>` | 445 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1322 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1535 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 60, FPD </src>` | 1303 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1542 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2728 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 보입니다. </src>` | 2052 |
| 11 | `<src><\|wait\|></src>` | `<src>엑스 박스 </src>` | 1452 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>시리즈 X에서도 없는 </src>` | 1811 |
| 13 | `<src><\|wait\|></src>` | `<src>인피니트 캐시 </src>` | 1649 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>CS, </src>` | 688 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>CS가 여기 도 없다. </src>` | 1245 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 377 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2001 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1199 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining, what we think </src>` | 2113 |
| 4 | `<src>the standard is because you're </src>` | `<src>that standard is, because you're </src>` | 630 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 1230 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1624 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 1151 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on </src>` | 1733 |
| 9 | `<src>block and because the </src>` | `<src>the block, and because </src>` | 2785 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 1640 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from </src>` | 1311 |
| 12 | `<src>years ago, </src>` | `<src>twenty years ago, </src>` | 1889 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1270 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1038 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point is </src>` | 1164 |
| 16 | `<src>held to a higher standard. </src>` | `<src>being held to a higher standard. </src>` | 793 |

---

### Test Example 51 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2080 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 2185 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 889 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的。</src>` | 714 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1295 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1492 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 527 |
| 8 | `<src>会听到人们</src>` | `<src>好经常会听到人们这样说。</src>` | 2431 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1927 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2472 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 840 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了。</src>` | 2468 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1117 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1144 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 950 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 978 |
| 17 | `<src><\|wait\|></src>` | `<src>就是说。</src>` | 386 |

---

### Test Example 52 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 2065 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 904 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 2229 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 703 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1369 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트 예요. </src>` | 1853 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이 컨설턴트 예요 </src>` | 2535 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>이렇게 컨설턴트 예요. </src>` | 2573 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2014 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1519 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>들여 쓸 때 </src>` | 1705 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라라는 사람 이 </src>` | 1591 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 707 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트에서 </src>` | 1142 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 716 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까 </src>` | 499 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2017 |
| 2 | `<src>Also, </src>` | `<src>Also, you will not </src>` | 2098 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 996 |
| 4 | `<src>move media objects </src>` | `<src>media objects </src>` | 655 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1384 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources </src>` | 1581 |
| 7 | `<src>So, if </src>` | `<src><\|wait\|></src>` | 1102 |
| 8 | `<src>you get into </src>` | `<src>if you get into </src>` | 1737 |
| 9 | `<src>a situation </src>` | `<src>a situation where you </src>` | 1610 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2767 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 773 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource. </src>` | 2473 |
| 13 | `<src>you need to let us know, </src>` | `<src>We'll deal with that. </src>` | 1104 |
| 14 | `<src>and we can see about </src>` | `<src>Now, we can see about </src>` | 1250 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1002 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure </src>` | 994 |
| 17 | `<src>get backed up </src>` | `<src>you get back up </src>` | 480 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 460 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point </src>` | 1794 |
| 2 | `<src>he knows Jesus </src>` | `<src>in those Jesus </src>` | 1180 |
| 3 | `<src>is hungry. </src>` | `<src>as a hungry, </src>` | 1756 |
| 4 | `<src>He knows that </src>` | `<src>in those that he's been </src>` | 912 |
| 5 | `<src>he's been without food, </src>` | `<src>through that food </src>` | 1308 |
| 6 | `<src><\|wait\|></src>` | `<src>in the wilderness, </src>` | 1680 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>spurted away, that he's hungry, </src>` | 2494 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 1160 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, say, </src>` | 2556 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 1515 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn these </src>` | 2189 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>stones to bread. </src>` | 1059 |
| 13 | `<src><\|wait\|></src>` | `<src>How did Jesus </src>` | 1418 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>deal with that </src>` | 670 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 1082 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 518 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead by bread. </src>` | 470 |
| 18 | `<src>by bread alone. </src>` | `<src>I'm alone. </src>` | 480 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2273 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1060 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1727 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 859 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the AHR field </src>` | 1339 |
| 6 | `<src><\|wait\|></src>` | `<src>being of critical impact </src>` | 1471 |
| 7 | `<src>being of critical importance </src>` | `<src><\|wait\|></src>` | 529 |
| 8 | `<src>versus variant </src>` | `<src>importance versus </src>` | 2317 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 509 |
| 10 | `<src>databases, </src>` | `<src>variant databases, which is obviously </src>` | 3121 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>one of my loves. </src>` | 1402 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if you </src>` | 1513 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>don't agree upon </src>` | 1792 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 1518 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 731 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1110 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 563 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 459 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 502 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2210 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1104 |
| 3 | `<src>right, </src>` | `<src>right, and that </src>` | 1728 |
| 4 | `<src>and the Supreme Court </src>` | `<src>the Supreme Court </src>` | 867 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1296 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't know </src>` | 1562 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 547 |
| 8 | `<src><\|wait\|></src>` | `<src>the the Van </src>` | 2366 |
| 9 | `<src>the the vanguard of social </src>` | `<src>Guard of Social </src>` | 1184 |
| 10 | `<src>change </src>` | `<src>Change, </src>` | 2331 |
| 11 | `<src>these days, </src>` | `<src>these days. </src>` | 1299 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1287 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect the </src>` | 1694 |
| 14 | `<src>the consensus </src>` | `<src><\|wait\|></src>` | 1233 |
| 15 | `<src><\|wait\|></src>` | `<src>consensus that's already </src>` | 1163 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged </src>` | 1114 |
| 17 | `<src><\|wait\|></src>` | `<src>soam. </src>` | 709 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 478 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 309 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 295 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 393 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1968 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片</src>` | 1210 |
| 3 | `<src><\|wait\|></src>` | `<src>呢，图片</src>` | 1612 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>的部分呢，</src>` | 922 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到</src>` | 1394 |
| 6 | `<src>的部分。</src>` | `<src>一个是客厅的部分，</src>` | 1585 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅</src>` | 956 |
| 8 | `<src>都是属于</src>` | `<src>一般都是</src>` | 1811 |
| 9 | `<src>我们</src>` | `<src>属于我们</src>` | 1560 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息</src>` | 2421 |
| 11 | `<src><\|wait\|></src>` | `<src>的地方，</src>` | 900 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，这身体的部分</src>` | 1692 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，反映的是</src>` | 1641 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1441 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 678 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 1168 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息</src>` | 554 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可。我们可以看到</src>` | 480 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>这边是放五一人的嘛，</src>` | 562 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 368 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 339 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1823 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1207 |
| 3 | `<src>and they often </src>` | `<src><\|wait\|></src>` | 1617 |
| 4 | `<src>show up to </src>` | `<src>and they often show up </src>` | 914 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1345 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 1625 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1032 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1755 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1455 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2635 |
| 11 | `<src>While they're </src>` | `<src>While they're extroverted </src>` | 962 |
| 12 | `<src>extroverted, </src>` | `<src><\|wait\|></src>` | 1897 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1352 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations, </src>` | 1496 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 836 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to the </src>` | 1153 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 272 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 476 |
| 19 | `<src>play </src>` | `<src><\|wait\|></src>` | 474 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>play the devil's advocate, </src>` | 474 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 321 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 212 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 215 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. stands for </src>` | 313 |
| 25 | `<src>ENTP stands for </src>` | `<src>for. </src>` | 265 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1894 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>정무를 거부 한 </src>` | 2167 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1119 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 493 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1446 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1623 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2456 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제는 </src>` | 1037 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2698 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1276 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1440 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들은 냄새 고 </src>` | 2000 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 를 </src>` | 1584 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1055 |
| 15 | `<src><\|wait\|></src>` | `<src>독기 를 품은 </src>` | 1030 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 500 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 476 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 189 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 327 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴발 </src>` | 299 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납건. </src>` | 292 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 211 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 264 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 296 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 275 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2052 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね今</src>` | 1145 |
| 3 | `<src>今作ってる</src>` | `<src>作ってる</src>` | 1577 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいです。なのでここのね</src>` | 1066 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>フロントのホテル</src>` | 1425 |
| 6 | `<src>も</src>` | `<src>で朝食が</src>` | 1511 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 974 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1836 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1580 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 2641 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴルドーストーンホテル</src>` | 846 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいな</src>` | 2228 |
| 13 | `<src>なっていう方はですね</src>` | `<src>っていう方はですね</src>` | 1152 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1448 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>まあいいんじゃないか</src>` | 988 |
| 16 | `<src><\|wait\|></src>` | `<src>なとはい。</src>` | 962 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思います。ここ</src>` | 240 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね</src>` | 467 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 455 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 344 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 170 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかからないか</src>` | 342 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 244 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあホテル</src>` | 204 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 233 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 299 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 264 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 132 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではね</src>` | 140 |
