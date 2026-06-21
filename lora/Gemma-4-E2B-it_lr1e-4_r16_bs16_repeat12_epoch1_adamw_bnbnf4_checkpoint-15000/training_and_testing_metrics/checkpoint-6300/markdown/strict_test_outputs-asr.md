# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9610
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.6490
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
  - PROCESS_TIME_MS_AVG: 1451.6270
  - PROCESS_TIME_MS_P50: 1613.8460
  - PROCESS_TIME_MS_P95: 2135.8830
  - PROCESS_TIME_MS_MAX: 2750.7760

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1962 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气守是容易的，</src>` | 1218 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1402 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师傅</src>` | 1008 |
| 5 | `<src><\|wait\|></src>` | `<src>指导到</src>` | 773 |
| 6 | `<src>知道如何</src>` | `<src>卢波</src>` | 1808 |
| 7 | `<src>处于中间，</src>` | `<src>处于中年，</src>` | 896 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1845 |
| 9 | `<src>虚阿凡</src>` | `<src>需加凡，</src>` | 379 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 1816 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅，</src>` | 2005 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>我的</src>` | 2110 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>松子儿里</src>` | 840 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个油性也很大，</src>` | 1867 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1064 |
| 5 | `<src><\|wait\|></src>` | `<src>呢，</src>` | 1023 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我再放点</src>` | 1882 |
| 7 | `<src>儿核桃</src>` | `<src>葛桃仁，</src>` | 702 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1937 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>可以的吧？</src>` | 1455 |
| 10 | `<src>这种核桃</src>` | `<src>这种葛桃仁</src>` | 1719 |
| 11 | `<src>仁儿。</src>` | `<src>啊。</src>` | 1809 |

---

### Test Example 3 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1912 |
| 2 | `<src>옹심이, </src>` | `<src>용심이 </src>` | 825 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1773 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심이 </src>` | 1104 |
| 5 | `<src>옹심이가 </src>` | `<src>수술 용심이 가 </src>` | 1158 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1661 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. </src>` | 838 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 1858 |
| 9 | `<src>진짜 이거 </src>` | `<src>자 진짜 이거 </src>` | 1123 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해킹으로 조금 </src>` | 1922 |
| 11 | `<src>진짜. </src>` | `<src>주집니다, 제가. </src>` | 2040 |

---

### Test Example 4 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2081 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1228 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1488 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1068 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1929 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1154 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1259 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 1187 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1502 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 1762 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 1771 |

---

### Test Example 5 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1807 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1019 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1647 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1076 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 1520 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 1215 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 846 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1932 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1455 |
| 10 | `<src>out there, </src>` | `<src>out there, people with </src>` | 1729 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 1927 |

---

### Test Example 6 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1800 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptrude. </src>` | 883 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽발시킥이고 </src>` | 1809 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1053 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1020 |
| 6 | `<src><\|wait\|></src>` | `<src>페모르 조직 인 </src>` | 1927 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>해류 나 </src>` | 1046 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1593 |
| 9 | `<src>박한상과 </src>` | `<src>박관 사와 </src>` | 1622 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 1855 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>됩니다. </src>` | 1714 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1964 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1354 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1583 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 968 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 2096 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1017 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 1765 |
| 8 | `<src>能量的运行</src>` | `<src><\|wait\|></src>` | 555 |
| 9 | `<src>状态，</src>` | `<src>能量的运行状态，</src>` | 1699 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1810 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1807 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1844 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1242 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1424 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1133 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1919 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们学校这个状况，</src>` | 1215 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1594 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 829 |
| 9 | `<src>独立承担。</src>` | `<src>不离沉端，</src>` | 1650 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言</src>` | 1774 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该是不受用。</src>` | 1867 |

---

### Test Example 9 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1708 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 914 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 1749 |
| 4 | `<src>一年生ですからね。</src>` | `<src>1年生ですからね。</src>` | 1057 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1527 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1349 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 721 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1943 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 2211 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 1901 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1832 |

---

### Test Example 10 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1708 |
| 2 | `<src>doing? </src>` | `<src><\|wait\|></src>` | 991 |
| 3 | `<src>Drop into </src>` | `<src>doing? Drop into </src>` | 1698 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1020 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1641 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1430 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1472 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1216 |
| 9 | `<src>I ask them what </src>` | `<src>I ask </src>` | 2124 |
| 10 | `<src><\|wait\|></src>` | `<src>the language </src>` | 1974 |
| 11 | `<src>language are you using? </src>` | `<src>you use. </src>` | 1822 |

---

### Test Example 11 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2166 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 967 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1634 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1224 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2241 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1048 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1915 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 441 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2193 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2032 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은. </src>` | 2026 |

---

### Test Example 12 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1941 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1010 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>이제 저열한 일일 수 있지만 </src>` | 2129 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 727 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 2099 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요 근데 꿈일 </src>` | 1131 |
| 7 | `<src>뭐 있고 </src>` | `<src>필요 가 보이 고 </src>` | 1999 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 한 보살 로 </src>` | 605 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 필요 가 보이 서 우주 가 </src>` | 2326 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 </src>` | 1951 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는데. </src>` | 1979 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1889 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 1346 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 1484 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 1171 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 2361 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 764 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐. 내가 </src>` | 2032 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1143 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐? </src>` | 1975 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 1967 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1870 |

---

### Test Example 14 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1990 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 878 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 1693 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1073 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 633 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 2237 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 696 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 2002 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1363 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1696 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 2023 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1900 |

---

### Test Example 15 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2088 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 835 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1723 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも用意しております</src>` | 1145 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので</src>` | 939 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1966 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 663 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1989 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1766 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1871 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内があります</src>` | 1796 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>ので、場所をお待ちください。</src>` | 1934 |

---

### Test Example 16 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2105 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 909 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1753 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1192 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 2751 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 961 |
| 7 | `<src><\|wait\|></src>` | `<src>And what you're not good </src>` | 1766 |
| 8 | `<src>And what you're not good at, </src>` | `<src><\|wait\|></src>` | 1473 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>yet, get the people around you to help you with. </src>` | 2257 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1889 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1770 |

---

### Test Example 17 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2193 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 809 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1816 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 1058 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1174 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1702 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 713 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 1995 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 2216 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと全部</src>` | 1950 |
| 11 | `<src>傾向が強いので、</src>` | `<src>運用しちゃうから強いので、</src>` | 1986 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1714 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1738 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1130 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1804 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 873 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1929 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1213 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1700 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 858 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2103 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2016 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子</src>` | 1822 |
| 12 | `<src>连篇。</src>` | `<src>思绪连篇。</src>` | 1890 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1616 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 833 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 1751 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1110 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 760 |
| 6 | `<src>在他下班的时候，</src>` | `<src>哈，在他下班的时候，</src>` | 2362 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1189 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃。真的，</src>` | 1416 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1978 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，就吃一碗，</src>` | 2293 |
| 11 | `<src>小小的愿望</src>` | `<src>一个小小的小愿望</src>` | 2035 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1711 |

---

### Test Example 20 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1801 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 815 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1758 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1102 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 587 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1913 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 914 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 2111 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 694 |
| 10 | `<src>は五経、</src>` | `<src>五経、</src>` | 2008 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2039 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、</src>` | 1781 |
| 13 | `<src>です。</src>` | `<src>五比です。</src>` | 1770 |

---

### Test Example 21 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1781 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 834 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1768 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1187 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1270 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1850 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1432 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1218 |
| 9 | `<src>保証する、生息である</src>` | `<src><\|wait\|></src>` | 2123 |
| 10 | `<src>ことを保証する</src>` | `<src>保証するということは保証するといった意味が</src>` | 2282 |
| 11 | `<src>といったような</src>` | `<src><\|wait\|></src>` | 1687 |
| 12 | `<src>使い方をされます。</src>` | `<src>ある使い方をされます。</src>` | 1841 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2087 |
| 2 | `<src>です。</src>` | `<src>です、</src>` | 811 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 1750 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1143 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 1116 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1579 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 770 |
| 8 | `<src>役ねじの</src>` | `<src>逆ネジの</src>` | 1991 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 718 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いているっていうこと</src>` | 2076 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 1948 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1823 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを。</src>` | 1780 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1779 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1362 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also </src>` | 1386 |
| 4 | `<src>also store energy, </src>` | `<src>store energy. And when those </src>` | 1137 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 2355 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 897 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted </src>` | 1998 |
| 8 | `<src>other types of energy, </src>` | `<src>to other types of energy, like </src>` | 719 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 2077 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2042 |
| 11 | `<src>or gets used to make </src>` | `<src>Or gets used to make </src>` | 1929 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1646 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1893 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel, you. Hi. </src>` | 2316 |
| 3 | `<src>I am currently </src>` | `<src><\|wait\|></src>` | 499 |
| 4 | `<src><\|wait\|></src>` | `<src>I'm currently studying </src>` | 1039 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>a Bacc for Finance </src>` | 2131 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a BSc for </src>` | 1159 |
| 7 | `<src><\|wait\|></src>` | `<src>Psychology. </src>` | 2017 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the ANJ, </src>` | 1170 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 1806 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 2091 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1875 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1721 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2087 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 1034 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment, </src>` | 1644 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1068 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1230 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1518 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 684 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 2012 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1264 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1792 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1819 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 2069 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1718 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1833 |
| 2 | `<src><\|wait\|></src>` | `<src>选择啊，一个月</src>` | 950 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>工资高，</src>` | 1734 |
| 4 | `<src>服务</src>` | `<src>在一个月</src>` | 1009 |
| 5 | `<src>在一级一线</src>` | `<src>一线</src>` | 798 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 2190 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说</src>` | 753 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1870 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做运维工程师几点，</src>` | 1661 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1737 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给运维工程师配置文件</src>` | 1819 |
| 12 | `<src>的新榜反而</src>` | `<src>的新房</src>` | 1906 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1720 |

---

### Test Example 27 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2125 |
| 2 | `<src>and then </src>` | `<src>And then </src>` | 941 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1803 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1008 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1222 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1793 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1056 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1455 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1663 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1827 |
| 11 | `<src><\|wait\|></src>` | `<src>So this </src>` | 1729 |
| 12 | `<src>this game dot scored array. </src>` | `<src>game dot sort array. </src>` | 1999 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1761 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1879 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 883 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1795 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1027 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 950 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 1869 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 703 |
| 8 | `<src>来诊断，</src>` | `<src>十二岁医生来诊，</src>` | 2086 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿、</src>` | 1816 |
| 10 | `<src>一下提腿，</src>` | `<src>以下踢腿、</src>` | 1968 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1762 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 1759 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的来开。</src>` | 1780 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1948 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 994 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1637 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1057 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1537 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1580 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1165 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1479 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2076 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2042 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1822 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 2002 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1362 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1820 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 2330 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 인슐린과 </src>` | 830 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 718 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 </src>` | 2246 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1020 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 2004 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1150 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 1732 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 2098 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1959 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1729 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1239 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1795 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 892 |
| 3 | `<src>一个在钓鱼</src>` | `<src><\|wait\|></src>` | 1724 |
| 4 | `<src>的人，但是</src>` | `<src>一个在钓鱼的人，但是</src>` | 1209 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 2137 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 883 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样一个状况的</src>` | 1898 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 548 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 2051 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 1949 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1949 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 1698 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1543 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 1065 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1724 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1218 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 1398 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1078 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1237 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1662 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 785 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 1931 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2064 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 1925 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1824 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1820 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1563 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1142 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1717 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 2431 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 856 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 609 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 2099 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1165 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2154 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1853 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 1896 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1933 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1666 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않을 </src>` | 1717 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들이 보이 게 된 거죠. </src>` | 1359 |

---

### Test Example 34 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1992 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1014 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马</src>` | 1613 |
| 4 | `<src>不是一天造成的，</src>` | `<src>呢，不是一天造成的，</src>` | 1167 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1975 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1102 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1524 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊、</src>` | 910 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 2163 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是一夜之间</src>` | 1952 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1884 |
| 12 | `<src>演变出来的，</src>` | `<src>就演变出来的，</src>` | 1884 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1458 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1285 |

---

### Test Example 35 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who just </src>` | 2093 |
| 2 | `<src>just getting going </src>` | `<src>getting going </src>` | 859 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1758 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1053 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1240 |
| 6 | `<src>that I think are </src>` | `<src>that you really </src>` | 1526 |
| 7 | `<src>really important. </src>` | `<src><\|wait\|></src>` | 697 |
| 8 | `<src><\|wait\|></src>` | `<src>important. </src>` | 1963 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 975 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 1787 |
| 11 | `<src>one minute videos </src>` | `<src>I have about one minute of videos </src>` | 2132 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video. </src>` | 2022 |
| 13 | `<src><\|wait\|></src>` | `<src>They cover each one. </src>` | 1763 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1087 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>You know, a little more detail, </src>` | 1608 |

---

### Test Example 36 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1892 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 848 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1715 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1088 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 922 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 2082 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 836 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 1767 |
| 9 | `<src>one another place </src>` | `<src>this is just one </src>` | 1337 |
| 10 | `<src>to look at. </src>` | `<src>another place you look at. </src>` | 1847 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1920 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 1827 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1706 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1256 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1469 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在餐饮方面，</src>` | 1915 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月餐饮可以说是</src>` | 993 |
| 3 | `<src>很不错的，但是</src>` | `<src>上半年但是</src>` | 1621 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 1143 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1588 |
| 6 | `<src>在事业方面的</src>` | `<src>在市外方面的业绩</src>` | 1364 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>相对稳但是</src>` | 1105 |
| 8 | `<src>与收入的</src>` | `<src>容易收入的</src>` | 1433 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1454 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 1849 |
| 11 | `<src>这个月</src>` | `<src>这个月也是</src>` | 1770 |
| 12 | `<src>也是不错，只是</src>` | `<src>不错，只是</src>` | 1916 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对整体来说</src>` | 1831 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微若了一点，</src>` | 1273 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1240 |

---

### Test Example 38 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1683 |
| 2 | `<src>HTML이라고 </src>` | `<src>HTML이라고 </src>` | 832 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1769 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>하는 컴퓨터 도 이해 할 수 </src>` | 1168 |
| 5 | `<src><\|wait\|></src>` | `<src>있고 </src>` | 1167 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 이해 할 수 </src>` | 1777 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1126 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 1559 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1906 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1948 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1957 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1746 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1467 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 </src>` | 1067 |
| 15 | `<src>필요 합니다. </src>` | `<src>프로그램 이 필요 합니다. </src>` | 1478 |

---

### Test Example 39 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2012 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1033 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1693 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1011 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 1871 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1205 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1473 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you </src>` | 1060 |
| 9 | `<src>to college, </src>` | `<src>go to college? </src>` | 1588 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, did you graduate? </src>` | 2119 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level </src>` | 2008 |
| 12 | `<src>attainment. </src>` | `<src>of attainment. </src>` | 1839 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1590 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1362 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1102 |

---

### Test Example 40 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>十、</src>` | 1933 |
| 2 | `<src>十一二手とか</src>` | `<src>二日で</src>` | 823 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>解けた。おそらく</src>` | 1778 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1066 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 699 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 2023 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 806 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですか</src>` | 1921 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 435 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2161 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1919 |
| 12 | `<src><\|wait\|></src>` | `<src>十一に</src>` | 1858 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1720 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1472 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮本とかが</src>` | 1259 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 1077 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 간 코 </src>` | 2168 |
| 2 | `<src><\|wait\|></src>` | `<src>새머라 </src>` | 1014 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야 </src>` | 1610 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니 했지 </src>` | 1031 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>소름 이 돋는까치리 </src>` | 1239 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>돋는 느낌 이 </src>` | 1692 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>엄이야 이걸 </src>` | 676 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>한들 어서 같이 놀자는 거야 </src>` | 2045 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>니 시니 이으면 </src>` | 1932 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1923 |
| 11 | `<src>신이 오면 </src>` | `<src>씨니 이으면 </src>` | 1955 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1801 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1630 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1357 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 간다. </src>` | 1103 |

---

### Test Example 42 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1776 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1350 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1487 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 977 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1954 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1251 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1760 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 726 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2096 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1920 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1812 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1791 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1565 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1294 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1075 |

---

### Test Example 43 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2044 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 898 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1887 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1020 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1414 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1443 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 883 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1760 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1291 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1726 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 1890 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1896 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1480 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1267 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1378 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 979 |

---

### Test Example 44 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2000 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 970 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1660 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1063 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今非力を見ている。</src>` | 819 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1911 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 767 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2029 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えているふねを気勢気、</src>` | 1672 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1783 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1751 |
| 12 | `<src>船大工をやってる</src>` | `<src>船大工をやってる</src>` | 2123 |
| 13 | `<src>が、</src>` | `<src><\|wait\|></src>` | 1766 |
| 14 | `<src>俺は</src>` | `<src>が俺はこんなにすごい</src>` | 1224 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1351 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 332 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2039 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1072 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて、</src>` | 1805 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 881 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 2177 |
| 6 | `<src>というのもフローリフを</src>` | `<src>そういうのも</src>` | 955 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルに書いた後、</src>` | 2211 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあずはPythonコード</src>` | 1054 |
| 9 | `<src>にそこから</src>` | `<src>にそんから</src>` | 1850 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 2076 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1792 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1769 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1215 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1241 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 864 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ</src>` | 708 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 2136 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 920 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맨다, </src>` | 1902 |
| 4 | `<src><\|wait\|></src>` | `<src>이 운전 하고 </src>` | 975 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 1924 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>걸어 걸어 다니 고 안에 뭐 </src>` | 1418 |
| 7 | `<src>강북 을 가면 </src>` | `<src><\|wait\|></src>` | 2022 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>강북 으로 가면 말할 것도 없고 </src>` | 1663 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 </src>` | 1843 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>또 장렬이에요. </src>` | 1870 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 신경 이 </src>` | 1935 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1767 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1085 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>못 가요. 그거 는 </src>` | 1335 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>안 된 것 같아요. </src>` | 469 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 632 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1910 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 855 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 2130 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형 주도 </src>` | 850 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1949 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만 </src>` | 1303 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1977 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 529 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 2355 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1918 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1845 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 </src>` | 1902 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 시총이 </src>` | 1295 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1467 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 717 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 645 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2006 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1115 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1614 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1144 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2245 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 907 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 1736 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们这样说：</src>` | 586 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 2121 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1959 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1779 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1809 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1499 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1144 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1233 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 351 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 578 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1678 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1125 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 했었 습니다. </src>` | 2165 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 599 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 2349 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 899 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 2116 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1373 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 1906 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 보인다. </src>` | 1826 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2049 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1847 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1125 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1400 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 395 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 666 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1936 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 855 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1879 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1163 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 2329 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 911 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 2036 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1419 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 1763 |
| 10 | `<src>standards have </src>` | `<src><\|wait\|></src>` | 1903 |
| 11 | `<src>changed from 20 </src>` | `<src>standards have changed from 20 </src>` | 2014 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1775 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1276 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1192 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything </src>` | 536 |
| 16 | `<src>held to a higher standard. </src>` | `<src>at this point is being held to </src>` | 784 |

---

### Test Example 51 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계속 뭐 </src>` | 2078 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 </src>` | 996 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 2138 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 707 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 2257 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트 예요. </src>` | 1206 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트 가 </src>` | 1978 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>오고 A라는 </src>` | 1515 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1623 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1933 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 2020 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람 이 </src>` | 1718 |
| 13 | `<src>실제 </src>` | `<src>실제 크로스사이트 </src>` | 1312 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크리 에 써서 </src>` | 1385 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>예스 파이까지 </src>` | 332 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까? </src>` | 722 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>フロア1の</src>` | 1785 |
| 2 | `<src>首次觉知到</src>` | `<src>少女が</src>` | 792 |
| 3 | `<src>那个现象：</src>` | `<src>記述した</src>` | 1719 |
| 4 | `<src>每当我们</src>` | `<src>面積。まあ</src>` | 1086 |
| 5 | `<src><\|wait\|></src>` | `<src>私たちより</src>` | 802 |
| 6 | `<src>处于爱之中，</src>` | `<src>室内</src>` | 1781 |
| 7 | `<src>所谓的爱，</src>` | `<src>側屋の愛</src>` | 915 |
| 8 | `<src>我们也</src>` | `<src>も</src>` | 1929 |
| 9 | `<src>同时进入恨。</src>` | `<src>やはり長時間</src>` | 522 |
| 10 | `<src><\|wait\|></src>` | `<src>入る。在</src>` | 2194 |
| 11 | `<src>在早上的时候，</src>` | `<src>早上的时候，</src>` | 2035 |
| 12 | `<src>它是爱；</src>` | `<src>它是一</src>` | 1689 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1807 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成</src>` | 1470 |
| 15 | `<src><\|wait\|></src>` | `<src>很</src>` | 1185 |
| 16 | `<src>那个钟摆</src>` | `<src>那个重白，</src>` | 1064 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 692 |
| 18 | `<src>继续在移动。</src>` | `<src>移动。</src>` | 521 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1973 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 895 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1911 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 918 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1426 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1490 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1016 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1619 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1641 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 1841 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1963 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1925 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1823 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1176 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1243 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 844 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 620 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 390 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2168 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 805 |
| 3 | `<src>in the first section </src>` | `<src>in the first section about </src>` | 1867 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1005 |
| 5 | `<src>about the EHR fields </src>` | `<src>the EHR field </src>` | 957 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1859 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 711 |
| 8 | `<src>versus variant </src>` | `<src>versus the. </src>` | 1973 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1020 |
| 10 | `<src>databases, </src>` | `<src>Variant databases, </src>` | 1731 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2221 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 1925 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree </src>` | 1760 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1082 |
| 15 | `<src>to be in these </src>` | `<src>that need to be </src>` | 1305 |
| 16 | `<src>data sources that we can </src>` | `<src>in these data sources that we can </src>` | 933 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 643 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 668 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 388 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1743 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 888 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1738 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1085 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food. </src>` | 1984 |
| 6 | `<src><\|wait\|></src>` | `<src>He's been in the wilderness </src>` | 1421 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>forty days, and he's hungry. </src>` | 2125 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1900 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, if you're </src>` | 2147 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>the Son of God, prove it." </src>` | 2001 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn </src>` | 1620 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>these stones to bread." </src>` | 1614 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1188 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>say deal with that </src>` | 1239 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 761 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 532 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead </src>` | 183 |
| 18 | `<src>by bread alone. </src>` | `<src>by his own. </src>` | 409 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2200 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 895 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1721 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1077 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1017 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1916 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1205 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1440 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1447 |
| 10 | `<src>change </src>` | `<src>social change </src>` | 1646 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 1852 |
| 12 | `<src><\|wait\|></src>` | `<src>but they rather </src>` | 1916 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 1727 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1266 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1254 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 747 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 635 |
| 18 | `<src>So you have some </src>` | `<src>So you have </src>` | 588 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 422 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 318 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 162 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1926 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片呢，</src>` | 1029 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1637 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 1085 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到</src>` | 1250 |
| 6 | `<src>的部分。</src>` | `<src>一个是客厅的部分，</src>` | 1665 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 937 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1679 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 2202 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 1956 |
| 11 | `<src><\|wait\|></src>` | `<src>所以</src>` | 1842 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>呢，是身体的部分</src>` | 1770 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，反映的是</src>` | 1594 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1122 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 1191 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 745 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 267 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 457 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>荒芜一人的嘛，</src>` | 454 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 335 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 306 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1827 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 863 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1727 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 1008 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 864 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 2241 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1195 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1383 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 1905 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 1926 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1891 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1833 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1573 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1029 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1326 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 400 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 608 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 569 |
| 19 | `<src>play </src>` | `<src><\|wait\|></src>` | 433 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>play the devil's advocate, </src>` | 423 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 285 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 241 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 270 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. </src>` | 333 |
| 25 | `<src>ENTP stands for </src>` | `<src>Standfor. </src>` | 306 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1874 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>경무를 거부 한 </src>` | 1184 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1679 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 948 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 2729 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 881 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1821 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 2168 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2037 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1913 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1781 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1491 |
| 13 | `<src><\|wait\|></src>` | `<src>들러내 놓고 윤석열 후보 를 </src>` | 1518 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 949 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 679 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 553 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 433 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 382 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 284 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 269 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건. </src>` | 329 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 287 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 295 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 </src>` | 302 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재 입니까? </src>` | 317 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1972 |
| 2 | `<src>食堂ね</src>` | `<src>食後ね今</src>` | 911 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいなものだ</src>` | 1819 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>のでここのね</src>` | 1137 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>プロフェッショナルホテル</src>` | 1982 |
| 6 | `<src>も</src>` | `<src>も</src>` | 1059 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1669 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 776 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1740 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 1872 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴルドーストーンホテル</src>` | 1827 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいな</src>` | 1856 |
| 13 | `<src>なっていう方はですね</src>` | `<src>っていう方はですね</src>` | 1779 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさせて</src>` | 1067 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てみるとまあいいんじゃないか</src>` | 1474 |
| 16 | `<src><\|wait\|></src>` | `<src>なとはい。</src>` | 787 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思いますここの</src>` | 533 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ホテルからですね</src>` | 235 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 393 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 375 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 283 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 285 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 276 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のねまあホテル</src>` | 314 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 306 |
| 26 | `<src>よかったらですね</src>` | `<src>行ったらですね</src>` | 285 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 273 |
| 28 | `<src>ください</src>` | `<src>くださいそれならです</src>` | 185 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は。</src>` | 141 |
