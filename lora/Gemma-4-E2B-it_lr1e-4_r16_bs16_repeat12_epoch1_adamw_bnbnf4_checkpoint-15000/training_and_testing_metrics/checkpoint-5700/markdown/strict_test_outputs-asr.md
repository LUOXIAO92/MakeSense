# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9304
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
  - PROCESS_TIME_MS_AVG: 1486.9450
  - PROCESS_TIME_MS_P50: 1446.7120
  - PROCESS_TIME_MS_P95: 2516.3840
  - PROCESS_TIME_MS_MAX: 3204.2150

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2280 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1817 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 818 |
| 4 | `<src>用我们深深的</src>` | `<src><\|wait\|></src>` | 1108 |
| 5 | `<src>爱浇水、</src>` | `<src>深深的爱浇水，</src>` | 1715 |
| 6 | `<src>施肥，</src>` | `<src>给她</src>` | 420 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1097 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心灵营养，</src>` | 2021 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1194 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>给耐心等等孩子慢慢</src>` | 2107 |
| 11 | `<src>慢慢长大。</src>` | `<src>长大。</src>` | 1758 |

---

### Test Example 2 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 2098 |
| 2 | `<src>옹심이, </src>` | `<src>용심이 </src>` | 1473 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1140 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심이 </src>` | 1098 |
| 5 | `<src>옹심이가 </src>` | `<src>새우 상 용심이 가 </src>` | 717 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1503 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이는 건데요. </src>` | 1384 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1651 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 974 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해행으로도 조금 죽입니다. </src>` | 2164 |
| 11 | `<src>진짜. </src>` | `<src>진짜. </src>` | 2010 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1800 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1468 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 1100 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1114 |
| 5 | `<src>この時点で</src>` | `<src>この時点でこう</src>` | 527 |
| 6 | `<src>こう短く</src>` | `<src>短く</src>` | 1684 |
| 7 | `<src>剪定を</src>` | `<src>剪定をこう</src>` | 1215 |
| 8 | `<src><\|wait\|></src>` | `<src>タイズして</src>` | 1940 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>いただけると</src>` | 1189 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 2319 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1601 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2374 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>怪得忪子儿一般，</src>` | 2098 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个友谊很大。</src>` | 724 |
| 4 | `<src>然后</src>` | `<src><\|wait\|></src>` | 1039 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 1535 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我再拜干家，</src>` | 572 |
| 7 | `<src>儿核桃</src>` | `<src>和陶人</src>` | 2596 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 720 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>很厉害。</src>` | 1815 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 2417 |
| 11 | `<src>仁儿。</src>` | `<src>和陶人。</src>` | 680 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2157 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1924 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 936 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1085 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1511 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个，</src>` | 510 |
| 7 | `<src>相对的低</src>` | `<src><\|wait\|></src>` | 2498 |
| 8 | `<src>能量的运行</src>` | `<src>相对的低能量的运行</src>` | 909 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1902 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2460 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 474 |

---

### Test Example 6 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1983 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1928 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 776 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1187 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1572 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们学校这个状况。</src>` | 521 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 2725 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 927 |
| 9 | `<src>独立承担。</src>` | `<src>不理成担，</src>` | 2001 |
| 10 | `<src>整体而言，</src>` | `<src>责任而已，</src>` | 2376 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是一件就是选项。</src>` | 952 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1863 |
| 2 | `<src>doing? </src>` | `<src><\|wait\|></src>` | 1524 |
| 3 | `<src>Drop into </src>` | `<src>doing? Drop into </src>` | 1126 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1079 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1684 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 569 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 2859 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1064 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them </src>` | 1902 |
| 10 | `<src><\|wait\|></src>` | `<src>for language </src>` | 2178 |
| 11 | `<src>language are you using? </src>` | `<src>you is using. </src>` | 1120 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1947 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptitude, </src>` | 1600 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽팔리 시키고, </src>` | 1279 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1012 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1703 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 욕인, </src>` | 465 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>혈연아, </src>` | 2764 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 840 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1989 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 2427 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>많다. </src>` | 1112 |

---

### Test Example 9 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명단 에 있는 </src>` | 2362 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>식성들은 </src>` | 1508 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1042 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1146 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1541 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 696 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src><\|wait\|></src>` | 2783 |
| 8 | `<src>때문 입니다. </src>` | `<src>식성들이었기 때문 입니다. </src>` | 1004 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1934 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2320 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은. </src>` | 1218 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 2250 |
| 2 | `<src>あの</src>` | `<src>などがあの</src>` | 1472 |
| 3 | `<src>いただもらえる</src>` | `<src>いただける</src>` | 912 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 676 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 847 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 2026 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 2179 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1157 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1647 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2609 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 693 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1263 |

---

### Test Example 11 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2289 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1570 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1021 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1099 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 831 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1451 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2690 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 919 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2285 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2219 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1909 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1941 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1700 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1008 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1192 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem. </src>` | 1935 |
| 6 | `<src>research, </src>` | `<src>Research. </src>` | 933 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 2246 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1184 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1994 |
| 10 | `<src>out there, </src>` | `<src>out there—people that </src>` | 1950 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1933 |

---

### Test Example 13 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2124 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气守是容易的。</src>` | 1922 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 829 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有一个师傅</src>` | 1105 |
| 5 | `<src><\|wait\|></src>` | `<src>知道，</src>` | 1983 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1033 |
| 7 | `<src>处于中间，</src>` | `<src>如何处于中间，</src>` | 2070 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 968 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1827 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 2322 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅，</src>` | 2225 |

---

### Test Example 14 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2186 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1469 |
| 3 | `<src>始めた</src>` | `<src><\|wait\|></src>` | 1097 |
| 4 | `<src>もので、</src>` | `<src>始めたもので、</src>` | 772 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 615 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1965 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1178 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 2063 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1281 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 2510 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 1253 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 2204 |

---

### Test Example 15 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1933 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1553 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1035 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1076 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 600 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1615 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1402 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, like </src>` | 1992 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 1873 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2594 |
| 11 | `<src>or gets used to make </src>` | `<src>Or gets used to make </src>` | 474 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 2358 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2316 |
| 2 | `<src>and then </src>` | `<src>And then </src>` | 1392 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1172 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 903 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 454 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1872 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 496 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2443 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 723 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 2068 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2479 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array </src>` | 991 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1930 |

---

### Test Example 17 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1925 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 1430 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1157 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1151 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 584 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1688 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 2222 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1248 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 2098 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証するといった</src>` | 2507 |
| 11 | `<src>といったような</src>` | `<src>ような使い方をされます。</src>` | 1045 |
| 12 | `<src>使い方をされます。</src>` | `<src><\|wait\|></src>` | 1975 |

---

### Test Example 18 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 2092 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1556 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>저열한 일일 수 있지만 </src>` | 1254 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1066 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>진짜 보살 도요. 아니 </src>` | 2053 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 가 보살 인데 꿈일 프로 </src>` | 2522 |
| 7 | `<src>뭐 있고 </src>` | `<src>보이 고 </src>` | 783 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 1645 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 프로 보이 서 우주 가 </src>` | 3158 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 </src>` | 1124 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는 뜻. </src>` | 2132 |

---

### Test Example 19 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2404 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 1389 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで、</src>` | 1279 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>おしゃれルカデがね、</src>` | 1233 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1856 |
| 6 | `<src>開業したい方って</src>` | `<src>海を楽しみたい方って</src>` | 1072 |
| 7 | `<src>すごい</src>` | `<src>すごい居心地がいい</src>` | 2066 |
| 8 | `<src>自己意識高いし、</src>` | `<src>居心地だから、</src>` | 1049 |
| 9 | `<src>自分で</src>` | `<src>一日中いてもともと</src>` | 2079 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>一人で遊ぶって</src>` | 2039 |
| 11 | `<src>傾向が強いので、</src>` | `<src>結構強いので、</src>` | 1330 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1974 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1828 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到我</src>` | 1544 |
| 3 | `<src>回到我生活</src>` | `<src>生活的一个轨道，</src>` | 1038 |
| 4 | `<src>的一个轨道哈，</src>` | `<src><\|wait\|></src>` | 1060 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 491 |
| 6 | `<src>在他下班的时候，</src>` | `<src>照他下班的时候，</src>` | 1828 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤、</src>` | 2881 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃，</src>` | 914 |
| 9 | `<src><\|wait\|></src>` | `<src>就这么我当时</src>` | 1926 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被他这样子那么</src>` | 2394 |
| 11 | `<src>小小的愿望</src>` | `<src>一个小小的小愿望</src>` | 1492 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1839 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1951 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1400 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1003 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 857 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 660 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1937 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 913 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 2439 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1261 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 2740 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 983 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 1447 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1833 |

---

### Test Example 22 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1914 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1685 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1153 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1035 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1988 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1470 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1772 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1532 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2715 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 783 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1286 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1975 |

---

### Test Example 23 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2305 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 1385 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 991 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 857 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 726 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1908 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1359 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 1937 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1651 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうことです</src>` | 2831 |
| 11 | `<src>ね。</src>` | `<src>ね。</src>` | 546 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1980 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを。</src>` | 1684 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 2069 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel. </src>` | 1663 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1062 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1122 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>a BA in business finance </src>` | 1968 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a BSc in psychology. </src>` | 1249 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1913 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the end, </src>` | 1271 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 2389 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 1536 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2166 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1834 |

---

### Test Example 25 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2060 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 2080 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 716 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 1271 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1823 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1325 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐. 내가 </src>` | 2061 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1934 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐. </src>` | 2827 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>응. </src>` | 2516 |
| 11 | `<src>내가 가. </src>` | `<src><\|wait\|></src>` | 1806 |

---

### Test Example 26 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src><\|wait\|></src>` | 2078 |
| 2 | `<src>一切正常，</src>` | `<src>我当时一切正常，</src>` | 1822 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 994 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 921 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 1356 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 774 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 1325 |
| 8 | `<src>来诊断，</src>` | `<src>十二名医生来诊，</src>` | 2044 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿，</src>` | 1747 |
| 10 | `<src>一下提腿，</src>` | `<src>一站提腿，</src>` | 2990 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 526 |
| 12 | `<src>他们</src>` | `<src><\|wait\|></src>` | 2268 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>他们都很疑惑的离开。</src>` | 1789 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2342 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1524 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1343 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1019 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1863 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 886 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2128 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 779 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2068 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2385 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 970 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 2203 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1382 |

---

### Test Example 28 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1872 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 2309 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 880 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 753 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1831 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1032 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2349 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1526 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 2818 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업 들은 </src>` | 729 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1721 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 현상 들을 </src>` | 1863 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1556 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2106 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1511 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1087 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1103 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1246 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 994 |
| 7 | `<src>to spell </src>` | `<src><\|wait\|></src>` | 2773 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>to spell the words. Like, oh, </src>` | 1061 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1932 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2370 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2177 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1839 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1267 |

---

### Test Example 30 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1981 |
| 2 | `<src><\|wait\|></src>` | `<src>选择啊，</src>` | 1414 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二classList，哎，</src>` | 1204 |
| 4 | `<src>服务</src>` | `<src>服务在一级，</src>` | 1110 |
| 5 | `<src>在一级一线</src>` | `<src><\|wait\|></src>` | 911 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>一线拼啥的，老牛们，</src>` | 1425 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 2680 |
| 8 | `<src><\|wait\|></src>` | `<src>呃，</src>` | 746 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>再做维向服务考试几点，</src>` | 2285 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 2281 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维向服务评分的</src>` | 2584 |
| 12 | `<src>的新榜反而</src>` | `<src>新棒反而</src>` | 1801 |
| 13 | `<src>火了。</src>` | `<src>活了。</src>` | 1180 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1849 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，</src>` | 1807 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 822 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1141 |
| 5 | `<src>请你务必就要</src>` | `<src>心里务必就要</src>` | 1617 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 538 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 2148 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 1285 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1973 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 2627 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 920 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 2014 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1651 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1143 |

---

### Test Example 32 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1979 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 2299 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 인슐린과 </src>` | 889 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 731 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 느냐 를 정밀 </src>` | 2040 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>하게 굉장히 </src>` | 2684 |
| 7 | `<src>굉장히 아주 </src>` | `<src>바로 </src>` | 616 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다. </src>` | 2210 |
| 9 | `<src>이렇게 </src>` | `<src>이게 굉장히 </src>` | 2475 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>잘 기억 이 저장 을 </src>` | 490 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2339 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1768 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1147 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2180 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1701 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1042 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1127 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1950 |
| 6 | `<src>你现在</src>` | `<src><\|wait\|></src>` | 1134 |
| 7 | `<src>所面临的一些</src>` | `<src>你现在所面临的一些</src>` | 2153 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，</src>` | 1211 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 2339 |
| 10 | `<src>一夕之间就</src>` | `<src>不可能是一夕之间就</src>` | 1493 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1795 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1610 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1664 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1195 |

---

### Test Example 34 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2221 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1551 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1061 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1058 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 998 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1253 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 2396 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you go </src>` | 958 |
| 9 | `<src>to college, </src>` | `<src>to college? </src>` | 1698 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And did you graduate? </src>` | 2864 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level </src>` | 376 |
| 12 | `<src>attainment. </src>` | `<src>of attainment. </src>` | 1844 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1642 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1712 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1101 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 2087 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 1413 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1136 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1084 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 526 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC, </src>` | 1739 |
| 7 | `<src>Yeah, so </src>` | `<src>and so on. </src>` | 1837 |
| 8 | `<src>this is just </src>` | `<src>This is just </src>` | 1354 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1542 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2841 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 693 |
| 12 | `<src><\|wait\|></src>` | `<src>But the level </src>` | 1872 |
| 13 | `<src>developers or engineers </src>` | `<src>operators or engineers </src>` | 1490 |
| 14 | `<src>working on BugRepo </src>` | `<src>work on for should be </src>` | 1722 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1250 |

---

### Test Example 36 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1929 |
| 2 | `<src>我们可以看到的是</src>` | `<src>砖墙的部分，我们看到的是</src>` | 2063 |
| 3 | `<src>一个在钓鱼</src>` | `<src><\|wait\|></src>` | 668 |
| 4 | `<src>的人，但是</src>` | `<src>一个戴雪的人，但是</src>` | 1170 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>他是属于逆向的，</src>` | 1994 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1592 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>汤浅朋友这样</src>` | 1646 |
| 8 | `<src>时候，就要去</src>` | `<src>一个状况的教学去</src>` | 1328 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意的是，</src>` | 2768 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能够</src>` | 911 |
| 11 | `<src>钓到鱼，</src>` | `<src><\|wait\|></src>` | 2210 |
| 12 | `<src>它钓不到鱼</src>` | `<src>调到于他调不到</src>` | 1860 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1265 |
| 14 | `<src>的意思哦。</src>` | `<src>一定的意识哦。</src>` | 1142 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone </src>` | 2218 |
| 2 | `<src>just getting going </src>` | `<src>who's just getting going </src>` | 1842 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 893 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1072 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1785 |
| 6 | `<src>that I think are </src>` | `<src>that I really </src>` | 393 |
| 7 | `<src>really important. </src>` | `<src>appreciate </src>` | 2221 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 978 |
| 9 | `<src>I'm going to go into. </src>` | `<src>um. I'm going to go </src>` | 1822 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 2756 |
| 11 | `<src>one minute videos </src>` | `<src>and have about one minute videos </src>` | 498 |
| 12 | `<src>that follow this video </src>` | `<src>about this video. </src>` | 1623 |
| 13 | `<src><\|wait\|></src>` | `<src>They'll cover each one. </src>` | 1830 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1564 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>You know, a little more detail, </src>` | 1395 |

---

### Test Example 38 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1825 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 1428 |
| 3 | `<src><\|wait\|></src>` | `<src>HTML이라고 하는 </src>` | 1157 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src><\|wait\|></src>` | 680 |
| 5 | `<src><\|wait\|></src>` | `<src>컴퓨터 도 이해 할 수 있고 </src>` | 874 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src><\|wait\|></src>` | 1813 |
| 7 | `<src><\|wait\|></src>` | `<src>사람 도 이해 할 수 있는 </src>` | 1623 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 1760 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1948 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 2785 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 980 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1891 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1683 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1282 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1152 |

---

### Test Example 39 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2169 |
| 2 | `<src>十一二手とか</src>` | `<src>十一・二日とか</src>` | 1799 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 882 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1041 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 944 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1199 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1317 |
| 8 | `<src>計算ですか</src>` | `<src>設定なんですか</src>` | 1942 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 1350 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2533 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1086 |
| 12 | `<src><\|wait\|></src>` | `<src>十・一・二</src>` | 1704 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1624 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1545 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1313 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 869 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2215 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれに。</src>` | 1758 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 930 |
| 4 | `<src><\|wait\|></src>` | `<src>今、</src>` | 1059 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>翡翠を見ている。</src>` | 948 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1253 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1200 |
| 8 | `<src><\|wait\|></src>` | `<src>遠くに超えている</src>` | 2055 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>船旅奇跡。</src>` | 1430 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2684 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 870 |
| 12 | `<src>船大工をやってる</src>` | `<src>船旅をやってる</src>` | 2150 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 1665 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1448 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1150 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 1077 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2380 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1535 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>선생 이 뭐라 빌 거야. </src>` | 1303 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 소름 이 돋든 </src>` | 1227 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>가짜 리 돋든 </src>` | 1843 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오면 </src>` | 1714 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1636 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1949 |
| 9 | `<src>귀신 이 오면 </src>` | `<src><\|wait\|></src>` | 2526 |
| 10 | `<src>물릴 거고 </src>` | `<src>귀신 이 오면 물릴 거고 </src>` | 499 |
| 11 | `<src>신이 오면 </src>` | `<src>선생 이 오면 </src>` | 2033 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1665 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주려 하니까 </src>` | 1480 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1218 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1001 |

---

### Test Example 42 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1938 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 </src>` | 1685 |
| 3 | `<src>이방인으로 </src>` | `<src>너희 가 이방인으로 </src>` | 1197 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1024 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 1902 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하는 우상에게로 </src>` | 1139 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 </src>` | 1925 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 돌려갖는이라. </src>` | 1101 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1880 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2194 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 2240 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1802 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님의 영으로 </src>` | 1331 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1326 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 885 |

---

### Test Example 43 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2249 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 1408 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1237 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 일정 </src>` | 1119 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>이 동생 이자 </src>` | 1278 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 같은 </src>` | 916 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>동생 이잖아. </src>` | 1480 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1619 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1205 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 2571 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 1323 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 2186 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1804 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것을 </src>` | 1287 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓고 </src>` | 1143 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1177 |

---

### Test Example 44 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2080 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1766 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 936 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 1203 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1807 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 907 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 2326 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 1281 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 2506 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面</src>` | 1378 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 2323 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1912 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1291 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1298 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 891 |

---

### Test Example 45 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 </src>` | 2046 |
| 2 | `<src><\|wait\|></src>` | `<src>인상 하는 </src>` | 1515 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인다면 </src>` | 1198 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1177 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1918 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만 </src>` | 2217 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 929 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 1161 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 2357 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 1610 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 움직이 기 때문 에 </src>` | 1591 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src><\|wait\|></src>` | 1714 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 시총이 </src>` | 1697 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1291 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨봐야 될 것 </src>` | 1134 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 570 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계소 </src>` | 2227 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1475 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 1369 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1088 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1862 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨턴트예요. </src>` | 1057 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트 가 </src>` | 2311 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>여기 있고 </src>` | 1449 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2917 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 712 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>줄어들 었을 때 </src>` | 1311 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람 이 </src>` | 1907 |
| 13 | `<src>실제 </src>` | `<src>실제 크로스사이트 </src>` | 1671 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크리티에서 </src>` | 1224 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 901 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 920 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2213 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1801 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 874 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1194 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1948 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1143 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 1962 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们这样说：</src>` | 1246 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 2005 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1906 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1055 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 2123 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1380 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1399 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 980 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 840 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 316 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1854 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1679 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 했었 습니다. </src>` | 1234 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1004 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1891 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1036 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 2146 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1140 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2246 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 보인다. </src>` | 1716 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2282 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1962 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1143 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1260 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 1148 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 277 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2111 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 1438 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1267 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1207 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 1936 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1028 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 2014 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1314 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 2207 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 1696 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1194 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 2106 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1604 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1290 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 930 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 959 |

---

### Test Example 50 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2224 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1769 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて、</src>` | 1000 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1089 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1990 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1741 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 1655 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それ自体はPythonを</src>` | 2057 |
| 9 | `<src>にそこから</src>` | `<src>書かずに、そっから</src>` | 2745 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1176 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 2007 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1622 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているから</src>` | 1249 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1026 |
| 15 | `<src>はい。</src>` | `<src>ですね、</src>` | 885 |
| 16 | `<src>じゃあ。</src>` | `<src>はい。じゃあ</src>` | 671 |

---

### Test Example 51 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2385 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 1524 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맨니다. </src>` | 1244 |
| 4 | `<src><\|wait\|></src>` | `<src>운전 을 할 건 </src>` | 1094 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 1919 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>거러 거러 다니 고는 뭐 </src>` | 1371 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 1914 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없이 </src>` | 1778 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장렬이에요. </src>` | 3204 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 1855 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1594 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1691 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1179 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모바일 을 그거 는 </src>` | 962 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>안 된 것 같아요. </src>` | 771 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 583 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2164 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 1418 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1259 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1041 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1128 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1005 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1191 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1939 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1193 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 2208 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1781 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2177 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know. </src>` | 1880 |
| 14 | `<src>and we can see about </src>` | `<src>Now we can see about </src>` | 1332 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1195 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 1218 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 655 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 343 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1894 |
| 2 | `<src>首次觉知到</src>` | `<src>佛罗伊的寿子觉知道</src>` | 2294 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象，</src>` | 620 |
| 4 | `<src>每当我们</src>` | `<src>每当我们</src>` | 930 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1914 |
| 6 | `<src>处于爱之中，</src>` | `<src>处于爱之中，</src>` | 981 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱，</src>` | 2084 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 787 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入恨。</src>` | 2098 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2305 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上</src>` | 1122 |
| 12 | `<src>它是爱；</src>` | `<src>的时候，它是爱，</src>` | 2139 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1565 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1200 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1097 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆，</src>` | 905 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在运动。</src>` | 647 |
| 18 | `<src>继续在移动。</src>` | `<src><\|wait\|></src>` | 567 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1905 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1518 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1068 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1073 |
| 5 | `<src>he's been without food, </src>` | `<src>he's going to </src>` | 1270 |
| 6 | `<src><\|wait\|></src>` | `<src>be in the wilderness for a short time. </src>` | 1046 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>He's going to be hungry. </src>` | 3112 |
| 8 | `<src>And so he says </src>` | `<src>And so he sends to </src>` | 1444 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus. He says, </src>` | 2920 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>If you're the Son of God, prove it </src>` | 754 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2220 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>by turning these stones to bread. </src>` | 1981 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1222 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with </src>` | 1164 |
| 15 | `<src>temptation? </src>` | `<src>that temptation? </src>` | 918 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 356 |
| 17 | `<src>Man shall not live </src>` | `<src>Man, Jonathan lead by </src>` | 642 |
| 18 | `<src>by bread alone. </src>` | `<src>a rope alone. </src>` | 558 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was </src>` | 2368 |
| 2 | `<src>in turmoil </src>` | `<src>a bit under a mile </src>` | 1730 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1061 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1129 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR </src>` | 1567 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 512 |
| 7 | `<src>being of critical importance </src>` | `<src>fields and their critical importance </src>` | 2730 |
| 8 | `<src>versus variant </src>` | `<src>versus the </src>` | 728 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1930 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 2613 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 752 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that </src>` | 1937 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree </src>` | 1914 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1244 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these data </src>` | 1224 |
| 16 | `<src>data sources that we can </src>` | `<src>sources that we can </src>` | 962 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 635 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 621 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 370 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2395 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1560 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1006 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1069 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 498 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1782 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 2529 |
| 8 | `<src><\|wait\|></src>` | `<src>the the van </src>` | 777 |
| 9 | `<src>the the vanguard of social </src>` | `<src>ard of social </src>` | 1676 |
| 10 | `<src>change </src>` | `<src>change. </src>` | 2587 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 657 |
| 12 | `<src><\|wait\|></src>` | `<src>but they rather </src>` | 1118 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 2025 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1551 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1205 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 1178 |
| 17 | `<src><\|wait\|></src>` | `<src>So. </src>` | 861 |
| 18 | `<src>So you have some </src>` | `<src>You have some </src>` | 629 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 555 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 417 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 311 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2095 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1694 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1017 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1199 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1944 |
| 6 | `<src>的部分。</src>` | `<src>的部分，</src>` | 972 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 2063 |
| 8 | `<src>都是属于</src>` | `<src><\|wait\|></src>` | 931 |
| 9 | `<src>我们</src>` | `<src>都是属于我们要</src>` | 1881 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 2322 |
| 11 | `<src><\|wait\|></src>` | `<src>休息的地方，所以呢，</src>` | 1127 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>是身体的部分</src>` | 2043 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，会反映的是</src>` | 1456 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1264 |
| 15 | `<src>一点时间，</src>` | `<src><\|wait\|></src>` | 1079 |
| 16 | `<src>可以好好的</src>` | `<src>一点时间可以好好的做</src>` | 1007 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>一下啦休息，</src>` | 685 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 583 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛。</src>` | 439 |
| 20 | `<src>啊，</src>` | `<src><\|wait\|></src>` | 347 |
| 21 | `<src>所以是说。</src>` | `<src>哦，所以是说。</src>` | 309 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1930 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1538 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1075 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1078 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 973 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1248 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2153 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1039 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1663 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2723 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 693 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1613 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1665 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1628 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1311 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 927 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 783 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 603 |
| 19 | `<src>play </src>` | `<src><\|wait\|></src>` | 584 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>play the devil's advocate, </src>` | 436 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 352 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 279 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 295 |
| 24 | `<src><\|wait\|></src>` | `<src>E.E.P. stands for </src>` | 306 |
| 25 | `<src>ENTP stands for </src>` | `<src>stand for. </src>` | 254 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 2007 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1869 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 934 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1016 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1998 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1190 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2044 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1216 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2709 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1117 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 2022 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1705 |
| 13 | `<src><\|wait\|></src>` | `<src>들러내 놓고 윤석열 후보 를 </src>` | 1624 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1264 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 880 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 494 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 598 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 566 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 427 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 362 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건. </src>` | 327 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 271 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 253 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 307 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 290 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2169 |
| 2 | `<src>食堂ね</src>` | `<src>食後ね今</src>` | 1433 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいです。なるほど。</src>` | 1339 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>でここのね</src>` | 1164 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>もうロボットホテル</src>` | 1881 |
| 6 | `<src>も</src>` | `<src><\|wait\|></src>` | 302 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>で朝食が食べれる場所</src>` | 2933 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1000 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1885 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 2198 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ロボットホテルの</src>` | 1199 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいなって</src>` | 2131 |
| 13 | `<src>なっていう方はですね</src>` | `<src>いう方はですね</src>` | 1482 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討させて</src>` | 1157 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てみるとまあいいんじゃない</src>` | 1004 |
| 16 | `<src><\|wait\|></src>` | `<src>かなと。はい。</src>` | 936 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思います。</src>` | 336 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね。</src>` | 435 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 554 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 408 |
| 21 | `<src>歩いて一分</src>` | `<src>一本かかるか</src>` | 361 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かからないかなんだって</src>` | 310 |
| 23 | `<src>レベルのね</src>` | `<src>あるでしょうね。</src>` | 270 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>のね立地のいいねまあ</src>` | 305 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 293 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 254 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 161 |
| 28 | `<src>ください</src>` | `<src>ください。それなら</src>` | 155 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は。</src>` | 168 |
