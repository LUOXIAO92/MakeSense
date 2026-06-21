# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9415
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.6689
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
  - PROCESS_TIME_MS_AVG: 1406.2090
  - PROCESS_TIME_MS_P50: 1408.6660
  - PROCESS_TIME_MS_P95: 2424.6700
  - PROCESS_TIME_MS_MAX: 3558.6100

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
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1653 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 842 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 986 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1185 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1217 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1386 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1746 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 631 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 1823 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 2662 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1172 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要气熟，</src>` | 2001 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>是容易的。</src>` | 897 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 1051 |
| 4 | `<src>只有一个师父</src>` | `<src>但是</src>` | 957 |
| 5 | `<src><\|wait\|></src>` | `<src>只有一个师傅指导</src>` | 1380 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1341 |
| 7 | `<src>处于中间，</src>` | `<src>如除于终前，</src>` | 1786 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1970 |
| 9 | `<src>虚阿凡</src>` | `<src>需加凡，</src>` | 1257 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 2434 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅。</src>` | 590 |

---

### Test Example 3 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1861 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1404 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 844 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1665 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1323 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们学校这个状况。</src>` | 634 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1581 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 2029 |
| 9 | `<src>独立承担。</src>` | `<src>你不利沉担，</src>` | 1311 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言</src>` | 2304 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是给主讯。</src>` | 601 |

---

### Test Example 4 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1950 |
| 2 | `<src>옹심이, </src>` | `<src>용심이 </src>` | 899 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 972 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>아 칼 용심이 </src>` | 1173 |
| 5 | `<src>옹심이가 </src>` | `<src>어우 솔 용심이 가 </src>` | 1690 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1136 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데 요. </src>` | 1705 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1851 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1005 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해방 으로 </src>` | 2463 |
| 11 | `<src>진짜. </src>` | `<src>조금 주깅이다, 제가. </src>` | 968 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2221 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>放在此处一点，</src>` | 1070 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个友星尼亚很大。</src>` | 1364 |
| 4 | `<src>然后</src>` | `<src><\|wait\|></src>` | 1544 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 1478 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我再放大。</src>` | 1495 |
| 7 | `<src>儿核桃</src>` | `<src>喝陶人，</src>` | 591 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1973 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉吧？</src>` | 1708 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 2069 |
| 11 | `<src>仁儿。</src>` | `<src>喝陶人，</src>` | 584 |

---

### Test Example 6 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1957 |
| 2 | `<src><\|wait\|></src>` | `<src>의 좋아요 </src>` | 911 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>눌 수 있지만 </src>` | 1053 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1056 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기가 </src>` | 1414 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요 근데 꾸밀 필요 가 </src>` | 1444 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 있고 </src>` | 1507 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>남한 테 보살 로 보일 필요 가 </src>` | 2102 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>뭐 있어요 우주 가 </src>` | 1378 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 </src>` | 2417 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는데. </src>` | 1300 |

---

### Test Example 7 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2114 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是</src>` | 1197 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1084 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1655 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1219 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 716 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1571 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 2137 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1570 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 2317 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 1140 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2148 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성들은 </src>` | 937 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 933 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1151 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1316 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1549 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성들이 </src>` | 1610 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1946 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1151 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모를 랐던 </src>` | 2819 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 1321 |

---

### Test Example 9 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 2091 |
| 2 | `<src>あの</src>` | `<src>などがあの</src>` | 841 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくもらえる</src>` | 951 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも用意しております</src>` | 1243 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので、ぜひ</src>` | 1303 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 1351 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1631 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1539 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 762 |
| 10 | `<src><\|wait\|></src>` | `<src>この</src>` | 1371 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 2489 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1356 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2021 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1404 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1126 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1482 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1426 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1143 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 910 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 2016 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1911 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2131 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1241 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1805 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1186 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1075 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1665 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 1515 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 957 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at the ten percent </src>` | 1159 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1994 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1259 |
| 10 | `<src>out there, </src>` | `<src>out there, people with </src>` | 2645 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 1351 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1709 |
| 2 | `<src>doing? </src>` | `<src><\|wait\|></src>` | 881 |
| 3 | `<src>Drop into </src>` | `<src>doing? Drop into </src>` | 1231 |
| 4 | `<src>your body. </src>` | `<src>your body. Where does </src>` | 877 |
| 5 | `<src>Where does the tension </src>` | `<src>the tension </src>` | 1160 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1577 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 1663 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tennis in your chest? </src>` | 2088 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 2344 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1728 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 1436 |

---

### Test Example 13 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1804 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptrude, </src>` | 949 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽팔리 시키고 </src>` | 1520 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1545 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1547 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 욕인 </src>` | 1801 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>해르 나와 </src>` | 1115 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1224 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 2535 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들은 </src>` | 1451 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>뭐 </src>` | 1551 |

---

### Test Example 14 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1915 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 </src>` | 1178 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 1575 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주기려고 들어왔 수다. </src>` | 1341 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1482 |
| 6 | `<src>죽여 달라 </src>` | `<src>주겨 달라 해가지고 </src>` | 1815 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>안돼요. 내가 </src>` | 1826 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>큰 소리 안 듣고 </src>` | 546 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐? </src>` | 3092 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 794 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1727 |

---

### Test Example 15 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1783 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 926 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 979 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1965 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 652 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1426 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1535 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 2055 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 1325 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 2425 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 454 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1820 |

---

### Test Example 16 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2039 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 894 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 889 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1168 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 1389 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1417 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1666 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1993 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 627 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 2841 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 847 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1915 |

---

### Test Example 17 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1636 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 900 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 983 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1124 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 1471 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 1411 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1612 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给大家吃，</src>` | 1944 |
| 9 | `<src><\|wait\|></src>` | `<src>就这么</src>` | 995 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时被他作为赞助一个</src>` | 2992 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的小愿望</src>` | 1118 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1909 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1807 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 784 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 997 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1252 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1226 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1331 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1711 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 445 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1915 |
| 10 | `<src>は五経、</src>` | `<src>は五本</src>` | 1707 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2239 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺</src>` | 1254 |
| 13 | `<src>です。</src>` | `<src>五本です。</src>` | 1744 |

---

### Test Example 19 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1802 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1412 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 848 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1654 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1474 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 871 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1218 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 2013 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 1802 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2255 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1353 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1658 |

---

### Test Example 20 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2146 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1062 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1203 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1729 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1577 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1814 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1613 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 836 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 3559 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1118 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 2048 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1896 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 898 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1286 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 857 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持不开档，</src>` | 1456 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 1124 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十二生</src>` | 1732 |
| 8 | `<src>来诊断，</src>` | `<src>来段时间，</src>` | 1505 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下跳退，</src>` | 832 |
| 10 | `<src>一下提腿，</src>` | `<src>一下跌退，</src>` | 2340 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1577 |
| 12 | `<src>他们</src>` | `<src>当然都很</src>` | 1305 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的离开。</src>` | 1689 |

---

### Test Example 22 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2251 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 874 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1468 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 1625 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1453 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1687 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 393 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 2132 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 1999 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 1906 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 1463 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1528 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 2181 |
| 2 | `<src>and then </src>` | `<src>and then after these </src>` | 1091 |
| 3 | `<src>after these examples, </src>` | `<src>examples, </src>` | 1070 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 864 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1190 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1555 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1657 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1585 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 680 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 2533 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1409 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot sort array </src>` | 1598 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1525 |

---

### Test Example 24 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2168 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 907 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1516 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1562 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1400 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 794 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1321 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1897 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1114 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2459 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 671 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, are </src>` | 1626 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1577 |

---

### Test Example 25 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1766 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1176 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相怪的人</src>` | 1357 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1431 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1469 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1261 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 779 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 2073 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2111 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1930 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1648 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1604 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2149 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 899 |
| 3 | `<src>ギアが</src>` | `<src>です。ギアが</src>` | 1104 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1043 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 1451 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1190 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1679 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1260 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1123 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いている</src>` | 2710 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 1222 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 2413 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを。</src>` | 1346 |

---

### Test Example 27 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1887 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Duru. </src>` | 1427 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 966 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1532 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 1519 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 1150 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 929 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 2166 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2630 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 1510 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2440 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1203 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1845 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 955 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级以上</src>` | 1054 |
| 4 | `<src>服务</src>` | `<src><\|wait\|></src>` | 999 |
| 5 | `<src>在一级一线</src>` | `<src>付费在一级一线</src>` | 1473 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1429 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1532 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1820 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做维向攻总好事几点，</src>` | 616 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 2788 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维向攻平分</src>` | 1057 |
| 12 | `<src>的新榜反而</src>` | `<src><\|wait\|></src>` | 1929 |
| 13 | `<src>火了。</src>` | `<src>的兴膀反而活了。</src>` | 1894 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1960 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1034 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1189 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1548 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 634 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1440 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1534 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 2006 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1144 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2670 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 592 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 2820 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1172 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1809 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1756 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1211 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1371 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1550 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>놀라울 정도로 </src>` | 1603 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 1917 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1133 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2243 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 933 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1692 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1877 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1084 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1733 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1250 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 866 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 879 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1432 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1346 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1631 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 2076 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1162 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 2559 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 556 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 2476 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1231 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1077 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1707 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1724 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1238 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1675 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1173 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1647 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2095 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1579 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 2333 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1342 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1746 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 </src>` | 1118 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1709 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2048 |
| 2 | `<src>要提醒大家，</src>` | `<src><\|wait\|></src>` | 1028 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1326 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1590 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1555 |
| 6 | `<src>你现在</src>` | `<src><\|wait\|></src>` | 1673 |
| 7 | `<src>所面临的一些</src>` | `<src>你现在所面临的一些</src>` | 483 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，跟风险</src>` | 1982 |
| 9 | `<src>也不可能是</src>` | `<src>也不可能是</src>` | 2197 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 1763 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1526 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1559 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1306 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1499 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1909 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 919 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1053 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1031 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1304 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC, </src>` | 1543 |
| 7 | `<src>Yeah, so </src>` | `<src>and so </src>` | 1605 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 1925 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place. </src>` | 485 |
| 10 | `<src>to look at. </src>` | `<src><\|wait\|></src>` | 2897 |
| 11 | `<src>But </src>` | `<src>But </src>` | 865 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1516 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1555 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1304 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1776 |

---

### Test Example 35 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1766 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1430 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1011 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1568 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1407 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1002 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1095 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 </src>` | 1920 |
| 9 | `<src><\|wait\|></src>` | `<src>갔느니라. </src>` | 1162 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2522 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 582 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1619 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1812 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1288 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1440 |

---

### Test Example 36 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1803 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 1021 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个</src>` | 916 |
| 4 | `<src>的人，但是</src>` | `<src>在钓鱼的人，</src>` | 1040 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>但是它是属于逆向的，</src>` | 1679 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 885 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 1865 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 2142 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1841 |
| 10 | `<src>是它能不能够</src>` | `<src>是他们能够</src>` | 2168 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够钓到鱼，</src>` | 1623 |
| 12 | `<src>它钓不到鱼</src>` | `<src>他钓不到</src>` | 1627 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1304 |
| 14 | `<src>的意思哦。</src>` | `<src>鱼的意识哦。</src>` | 1696 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>十，</src>` | 1966 |
| 2 | `<src>十一二手とか</src>` | `<src>二日で</src>` | 839 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>解けた。おそらく</src>` | 1037 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1106 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1215 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1361 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1806 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですか</src>` | 525 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 1700 |
| 10 | `<src>でなんか</src>` | `<src>二なんか</src>` | 1870 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2023 |
| 12 | `<src><\|wait\|></src>` | `<src>十一二日で</src>` | 1328 |
| 13 | `<src>十一二手で</src>` | `<src><\|wait\|></src>` | 1768 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1083 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮本とかが</src>` | 1286 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 953 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2134 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1016 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1209 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 769 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them that </src>` | 1657 |
| 6 | `<src>that I think are </src>` | `<src>I really </src>` | 965 |
| 7 | `<src>really important. </src>` | `<src>appreciate. </src>` | 1727 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1950 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into </src>` | 501 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 2931 |
| 11 | `<src>one minute videos </src>` | `<src>I have about one minute videos </src>` | 938 |
| 12 | `<src>that follow this video </src>` | `<src>at the fall this video </src>` | 2489 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one, </src>` | 1307 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1177 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>and a little more detail, </src>` | 1217 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2049 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 869 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 949 |
| 4 | `<src><\|wait\|></src>` | `<src>今激烈</src>` | 1169 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>を見ている。</src>` | 1272 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1397 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1693 |
| 8 | `<src><\|wait\|></src>` | `<src>遠い超えている</src>` | 1605 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>船の奇跡よ。</src>` | 824 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2723 |
| 11 | `<src>長年</src>` | `<src></src>` | 1149 |
| 12 | `<src>船大工をやってる</src>` | `<src>流れの深い川で構えている</src>` | 1614 |
| 13 | `<src>が、</src>` | `<src>わ。</src>` | 1501 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 1218 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい海賊船を見た</src>` | 1687 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 302 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1923 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1250 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1139 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 1599 |
| 5 | `<src>也就是</src>` | `<src><\|wait\|></src>` | 1416 |
| 6 | `<src>在事业方面的</src>` | `<src>也就是在事业方面的</src>` | 1715 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 412 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 1965 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果</src>` | 1204 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面呢，</src>` | 2802 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1231 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1795 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1261 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1413 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 675 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 간 코 </src>` | 2220 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1060 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>생활 벌 길 거야 </src>` | 1212 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src><\|wait\|></src>` | 758 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>연세 서름이 돋은 자차 이 </src>` | 2111 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느끼 면 </src>` | 714 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1653 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1983 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 오면 </src>` | 1249 |
| 10 | `<src>물릴 거고 </src>` | `<src>풀릴 거고 </src>` | 2499 |
| 11 | `<src>신이 오면 </src>` | `<src>시니오미안 너 </src>` | 583 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src><\|wait\|></src>` | 2597 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>지켜 주라고 찌르 줘라. 그러니까 </src>` | 1390 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 함 마음 에 </src>` | 1244 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 간 코 </src>` | 865 |

---

### Test Example 42 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1676 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 801 |
| 3 | `<src><\|wait\|></src>` | `<src>HTML이라고 하는 </src>` | 998 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 이해 할 수 </src>` | 1288 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1280 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 이해 할 수 </src>` | 1574 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1592 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 2059 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1775 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 2274 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1397 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1579 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1270 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 </src>` | 1197 |
| 15 | `<src>필요 합니다. </src>` | `<src>프로그램 이 필요 합니다. </src>` | 901 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2044 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. How far </src>` | 1201 |
| 3 | `<src>How far did you </src>` | `<src>did you </src>` | 960 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 830 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 1650 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1240 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 1693 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. Did you go </src>` | 2006 |
| 9 | `<src>to college, </src>` | `<src>to college and </src>` | 1496 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>so, did you graduate? </src>` | 2532 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1617 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1529 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1406 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1729 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 669 |

---

### Test Example 44 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2089 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 813 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1089 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1110 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1504 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1329 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아 </src>` | 1683 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1917 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 905 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 2805 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 600 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1918 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1691 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1022 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1518 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다 </src>` | 864 |

---

### Test Example 45 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계속 뭐 </src>` | 2113 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 </src>` | 1047 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 1567 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1379 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1439 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨턴트예요. </src>` | 1378 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트 가 </src>` | 741 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>여기 있고, A라는 </src>` | 1958 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1150 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2731 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>줄어 들었을 때 </src>` | 1306 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람 이 </src>` | 1863 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1163 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스킷에서 </src>` | 1501 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 674 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 918 |

---

### Test Example 46 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1713 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 1253 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 1260 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1471 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1440 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1129 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 942 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1960 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2504 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 </src>` | 1618 |
| 11 | `<src><\|wait\|></src>` | `<src>보인다. </src>` | 1419 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1627 |
| 13 | `<src><\|wait\|></src>` | `<src>인피니트 캐시 </src>` | 1367 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>SI에 </src>` | 1592 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>슬라이드 가 여기 도 없다. </src>` | 321 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 894 |

---

### Test Example 47 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 2191 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 1415 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 967 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1542 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 걸어 걸어다니 </src>` | 1404 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>공간 에 뭐 </src>` | 640 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 을 가면 </src>` | 1521 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 1927 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 </src>` | 1189 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>또 장렬이에요. </src>` | 2697 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 창피 하네요. 어 </src>` | 1203 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 2026 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1009 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>물어볼. </src>` | 1364 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다인 것 같아요. </src>` | 1014 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 984 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1908 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1026 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 1690 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1259 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1441 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1589 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 449 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 2002 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 1948 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2084 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1336 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 1845 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1350 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1754 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 774 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 417 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2031 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1291 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1109 |
| 4 | `<src>真实意图的，</src>` | `<src>真性意图的，</src>` | 1619 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1445 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1603 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 495 |
| 8 | `<src>会听到人们</src>` | `<src>靠经常会听到</src>` | 2043 |
| 9 | `<src>这样说：“</src>` | `<src>人们这样说：“</src>` | 2080 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1906 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1397 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1733 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1161 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 1633 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 408 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 907 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 392 |

---

### Test Example 50 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2067 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1246 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 1151 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1553 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1547 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1802 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 2004 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 491 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 2797 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1040 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1587 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1638 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1335 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1627 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 992 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 371 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1957 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 930 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1467 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 1607 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 1664 |
| 6 | `<src>but the reality </src>` | `<src>But the reality </src>` | 1677 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 1263 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1231 |
| 9 | `<src>block and because the </src>` | `<src>block, and because the </src>` | 3025 |
| 10 | `<src>standards have </src>` | `<src><\|wait\|></src>` | 801 |
| 11 | `<src>changed from 20 </src>` | `<src>standards have changed from 20 </src>` | 1725 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1988 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1320 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1192 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point is being </src>` | 1242 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 434 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1725 |
| 2 | `<src>首次觉知到</src>` | `<src>佛罗伊的首次觉知</src>` | 1557 |
| 3 | `<src>那个现象：</src>` | `<src>到了那个现象，</src>` | 989 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1434 |
| 5 | `<src><\|wait\|></src>` | `<src>美登我们处于</src>` | 1487 |
| 6 | `<src>处于爱之中，</src>` | `<src><\|wait\|></src>` | 1480 |
| 7 | `<src>所谓的爱，</src>` | `<src>爱之中熟悉的爱，</src>` | 589 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1994 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入</src>` | 1596 |
| 10 | `<src><\|wait\|></src>` | `<src>恨，</src>` | 2180 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上</src>` | 570 |
| 12 | `<src>它是爱；</src>` | `<src>的时候他才爱。</src>` | 2631 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1003 |
| 14 | `<src>它就变成恨。</src>` | `<src>他就变成</src>` | 1179 |
| 15 | `<src><\|wait\|></src>` | `<src>恨，那个</src>` | 1172 |
| 16 | `<src>那个钟摆</src>` | `<src>钟摆。</src>` | 842 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在移动</src>` | 437 |
| 18 | `<src>继续在移动。</src>` | `<src>中。</src>` | 542 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2010 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 911 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1508 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1544 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1488 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1726 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 376 |
| 8 | `<src>you get into </src>` | `<src>you get into this </src>` | 1975 |
| 9 | `<src>a situation </src>` | `<src><\|wait\|></src>` | 1597 |
| 10 | `<src>where you realize </src>` | `<src>situation where you realize </src>` | 2405 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1420 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1676 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1362 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1766 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 473 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 897 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 536 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 263 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2279 |
| 2 | `<src>in turmoil </src>` | `<src>in there a mile </src>` | 1027 |
| 3 | `<src>in the first section </src>` | `<src>on the first section about </src>` | 1326 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1547 |
| 5 | `<src>about the EHR fields </src>` | `<src>the EHR field </src>` | 1363 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 595 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1534 |
| 8 | `<src>versus variant </src>` | `<src>versus the. </src>` | 1911 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 494 |
| 10 | `<src>databases, </src>` | `<src>Variant databases, </src>` | 2738 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 1231 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if. </src>` | 2417 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>We don't agree upon </src>` | 1326 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 1257 |
| 15 | `<src>to be in these </src>` | `<src>to be in these data </src>` | 1101 |
| 16 | `<src>data sources that we can </src>` | `<src>sources that we can. </src>` | 845 |
| 17 | `<src>draw from, </src>` | `<src>Draw from. </src>` | 452 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>There's nothing to draw from, right? </src>` | 731 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 443 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1758 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1019 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1083 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 853 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 1695 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1130 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 1857 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1973 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, if you're Jesus, </src>` | 3206 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it." </src>` | 968 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn these </src>` | 2437 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>stones to bread." </src>` | 1277 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1220 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>say deal with that </src>` | 1099 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 988 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 381 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 645 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone." </src>` | 494 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2234 |
| 2 | `<src>Meaningful individual </src>` | `<src><\|wait\|></src>` | 915 |
| 3 | `<src>right, </src>` | `<src>Meaningful individual right, and then </src>` | 1523 |
| 4 | `<src>and the Supreme Court </src>` | `<src>the Supreme Court </src>` | 1532 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1323 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 683 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1706 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1908 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of social </src>` | 1570 |
| 10 | `<src>change </src>` | `<src>change </src>` | 2126 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 534 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2542 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1273 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1271 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 968 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 979 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 391 |
| 18 | `<src>So you have some </src>` | `<src>So you have some </src>` | 635 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 451 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 349 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 317 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1932 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1088 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1206 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1718 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1463 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 1491 |
| 7 | `<src>那客厅一般</src>` | `<src><\|wait\|></src>` | 548 |
| 8 | `<src>都是属于</src>` | `<src>它客厅一般都是</src>` | 2067 |
| 9 | `<src>我们</src>` | `<src>属于我们</src>` | 1395 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 2333 |
| 11 | `<src><\|wait\|></src>` | `<src>在休息的地方，所以</src>` | 1074 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>呢，这身体的部分</src>` | 2182 |
| 13 | `<src>也会反映的是</src>` | `<src>会反映的是</src>` | 1269 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1208 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 864 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 1016 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 341 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 641 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 499 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 304 |
| 21 | `<src>所以是说。</src>` | `<src>所以也是说。</src>` | 381 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1763 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1079 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1194 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 776 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1268 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1552 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1590 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 2091 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 2138 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 1923 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1449 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, they also </src>` | 1681 |
| 13 | `<src>they also hate </src>` | `<src><\|wait\|></src>` | 1339 |
| 14 | `<src>meaningless conversations </src>` | `<src>hate meaningless conversations </src>` | 1706 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 332 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to the </src>` | 1021 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 584 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 237 |
| 19 | `<src>play </src>` | `<src>play the devil's advocate, </src>` | 449 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and they're </src>` | 298 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy </src>` | 364 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>of a debate. </src>` | 270 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 301 |
| 24 | `<src><\|wait\|></src>` | `<src>INTP stands for </src>` | 281 |
| 25 | `<src>ENTP stands for </src>` | `<src>introvert, </src>` | 287 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1868 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1363 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1128 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1459 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1650 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1727 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1737 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 557 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2762 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1209 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1564 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1559 |
| 13 | `<src><\|wait\|></src>` | `<src>드러내 놓고 윤석열 후보 </src>` | 1465 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src><\|wait\|></src>` | 1617 |
| 15 | `<src><\|wait\|></src>` | `<src>을 떨어뜨리 겠다는 뚝길을 </src>` | 969 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>푸는 공격 성을 </src>` | 413 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 640 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 463 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 320 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 이준석의 </src>` | 320 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src><\|wait\|></src>` | 179 |
| 22 | `<src><\|wait\|></src>` | `<src>성상 랍건 </src>` | 216 |
| 23 | `<src>민주당 이 </src>` | `<src><\|wait\|></src>` | 286 |
| 24 | `<src><\|wait\|></src>` | `<src>민주당 이 공격 하기에 </src>` | 336 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 312 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2021 |
| 2 | `<src>食堂ね</src>` | `<src>食後ね</src>` | 866 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってるみたいな</src>` | 1035 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>です。なのでここのね</src>` | 1178 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>コラボスンのホテル</src>` | 1432 |
| 6 | `<src>も</src>` | `<src>でも</src>` | 1143 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1793 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1611 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 666 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 2535 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>コラボスンのホテル</src>` | 1468 |
| 12 | `<src>泊まってみたい</src>` | `<src><\|wait\|></src>` | 1625 |
| 13 | `<src>なっていう方はですね</src>` | `<src>泊まりたいなという方はですねけ</src>` | 2003 |
| 14 | `<src>検討なさってみて</src>` | `<src>動画の最後に</src>` | 1254 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てまあいいんじゃない</src>` | 1328 |
| 16 | `<src><\|wait\|></src>` | `<src>なとはい。</src>` | 867 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思いますここの</src>` | 425 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ホテルからです</src>` | 605 |
| 19 | `<src>駅ももう</src>` | `<src>ね부산駅も</src>` | 197 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 384 |
| 21 | `<src>歩いて一分</src>` | `<src>一分</src>` | 325 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 411 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 257 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>リッチのねまあホテル</src>` | 324 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 283 |
| 26 | `<src>よかったらですね</src>` | `<src>行ったらですね</src>` | 293 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 167 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 135 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではね回は。</src>` | 167 |
