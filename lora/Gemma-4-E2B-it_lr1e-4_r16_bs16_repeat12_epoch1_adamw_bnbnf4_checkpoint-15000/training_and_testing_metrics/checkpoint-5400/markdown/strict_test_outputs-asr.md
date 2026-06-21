# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9554
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5298
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
  - PROCESS_TIME_MS_AVG: 1477.3950
  - PROCESS_TIME_MS_P50: 1529.4260
  - PROCESS_TIME_MS_P95: 2282.5880
  - PROCESS_TIME_MS_MAX: 2963.9680

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
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1747 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1648 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 623 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1114 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1013 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 2023 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 638 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1694 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 1775 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 1762 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1961 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2043 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1824 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1226 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师傅</src>` | 1188 |
| 5 | `<src><\|wait\|></src>` | `<src>知道，</src>` | 806 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1616 |
| 7 | `<src>处于中间，</src>` | `<src>如何处于中间，</src>` | 1502 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1991 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 355 |
| 10 | `<src>要成为</src>` | `<src>要成为一个</src>` | 1940 |
| 11 | `<src>一个师父。</src>` | `<src>师傅。</src>` | 1838 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2179 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1779 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 1331 |
| 4 | `<src>用我们深深的</src>` | `<src><\|wait\|></src>` | 1171 |
| 5 | `<src>爱浇水、</src>` | `<src>深深的爱浇水，</src>` | 1388 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 964 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1101 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心灵营养，</src>` | 2421 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 717 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>给耐心等等</src>` | 2052 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 1495 |

---

### Test Example 4 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1881 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1707 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1301 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1267 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is Tip of the Stem </src>` | 1148 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 1179 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 1074 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2321 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 503 |
| 10 | `<src>out there, </src>` | `<src>out there, people who </src>` | 2048 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1888 |

---

### Test Example 5 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1872 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptroller. </src>` | 1732 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽발시끼고 </src>` | 1349 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1181 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 383 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 2087 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>배려 나 </src>` | 1500 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2019 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1099 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 2209 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>있습니다. </src>` | 1290 |

---

### Test Example 6 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2104 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1678 |
| 3 | `<src>始めた</src>` | `<src>始めたもので、</src>` | 993 |
| 4 | `<src>もので、</src>` | `<src><\|wait\|></src>` | 830 |
| 5 | `<src>ゴッホ、</src>` | `<src>工房、</src>` | 882 |
| 6 | `<src>ゴーギャン、</src>` | `<src>合間に</src>` | 1861 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 665 |
| 8 | `<src>セザンヌ、</src>` | `<src>生活の</src>` | 1728 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1670 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどのという人の絵</src>` | 1266 |
| 11 | `<src>は、田舎の</src>` | `<src><\|wait\|></src>` | 2307 |
| 12 | `<src>中学生でも。</src>` | `<src>は田舎の中学生でも。</src>` | 1503 |

---

### Test Example 7 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2298 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>怪得忪子儿</src>` | 1767 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这边，这个要因也很大。</src>` | 1694 |
| 4 | `<src>然后</src>` | `<src><\|wait\|></src>` | 957 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 1969 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在排课啊，</src>` | 943 |
| 7 | `<src>儿核桃</src>` | `<src>和陶儿</src>` | 1969 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1086 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>开始儿对</src>` | 1616 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 2155 |
| 11 | `<src>仁儿。</src>` | `<src>和陶儿。</src>` | 1278 |

---

### Test Example 8 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1811 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1604 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1150 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 872 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 783 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 2251 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1603 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 2092 |
| 9 | `<src>I ask them what </src>` | `<src>I ask </src>` | 1626 |
| 10 | `<src><\|wait\|></src>` | `<src>the language </src>` | 2154 |
| 11 | `<src>language are you using? </src>` | `<src>you use. </src>` | 1315 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아, </src>` | 2031 |
| 2 | `<src>옹심이, </src>` | `<src>저는 용심히 </src>` | 1711 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1357 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심히 </src>` | 1188 |
| 5 | `<src>옹심이가 </src>` | `<src>새우 </src>` | 597 |
| 6 | `<src><\|wait\|></src>` | `<src>용심히가 석연 </src>` | 1924 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>하는 건데요. </src>` | 1666 |
| 8 | `<src>야, </src>` | `<src>야, </src>` | 1834 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1136 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해장으로도 조금 죽입니다, </src>` | 2807 |
| 11 | `<src>진짜. </src>` | `<src>진짜. </src>` | 1457 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1912 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1832 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1290 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1232 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1555 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有的这个状况。</src>` | 903 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1680 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1931 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 1712 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 2085 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业是属实修。</src>` | 1678 |

---

### Test Example 11 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2082 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1822 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1529 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1127 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1994 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 828 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 1925 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 1193 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 2251 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1710 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1631 |

---

### Test Example 12 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 2122 |
| 2 | `<src>あの</src>` | `<src>などがあの</src>` | 1514 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 516 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1379 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1074 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 2058 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 867 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 2218 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 864 |
| 10 | `<src><\|wait\|></src>` | `<src>よろしくお願いします。</src>` | 1691 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 2161 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1740 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2183 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1686 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1327 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1274 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1821 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 893 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1711 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1780 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2057 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1912 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1971 |

---

### Test Example 14 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 2013 |
| 2 | `<src><\|wait\|></src>` | `<src>의인 처여야 </src>` | 1721 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>내실 수 있지만 </src>` | 1506 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1226 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 </src>` | 1947 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 가 보살 인데 꿈일 프로 </src>` | 975 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 이거. </src>` | 2103 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 954 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보살 로 보일 프로 </src>` | 1708 |
| 10 | `<src>지금 나한테 </src>` | `<src>보이 서 우주 가신다. </src>` | 2290 |
| 11 | `<src>보살 이라는데. </src>` | `<src>이 보살이라는데. </src>` | 2238 |

---

### Test Example 15 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2275 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1642 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1412 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1255 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1738 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 886 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1706 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1774 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1931 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모를 랐던 </src>` | 2038 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 2223 |

---

### Test Example 16 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1912 |
| 2 | `<src><\|wait\|></src>` | `<src>选择啊，一个月</src>` | 1646 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二吉星，哎，</src>` | 795 |
| 4 | `<src>服务</src>` | `<src>服务在</src>` | 767 |
| 5 | `<src>在一级一线</src>` | `<src>一级一线</src>` | 1101 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1293 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说啊，</src>` | 1077 |
| 8 | `<src><\|wait\|></src>` | `<src>在做</src>` | 1241 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>未经授权房屋继承，</src>` | 2348 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1087 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给未经授权</src>` | 2022 |
| 12 | `<src>的新榜反而</src>` | `<src>和平分的信房</src>` | 1320 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 2160 |

---

### Test Example 17 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2439 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 1494 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで、</src>` | 1514 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>放射光管だけは</src>` | 1155 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1221 |
| 6 | `<src>開業したい方って</src>` | `<src>回答して</src>` | 1018 |
| 7 | `<src>すごい</src>` | `<src>いかれたい方ってすごい勢い行き来して</src>` | 1573 |
| 8 | `<src>自己意識高いし、</src>` | `<src>ください。で</src>` | 2069 |
| 9 | `<src>自分で</src>` | `<src>これじゃあちょっと</src>` | 1473 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>その説明を</src>` | 2481 |
| 11 | `<src>傾向が強いので、</src>` | `<src>とっても強ので、</src>` | 1326 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1689 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1880 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1488 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 502 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1641 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 795 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1979 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 684 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 2202 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1180 |
| 10 | `<src>は五経、</src>` | `<src>は五コン、</src>` | 1720 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2083 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、</src>` | 1448 |
| 13 | `<src>です。</src>` | `<src>五ビです。</src>` | 1652 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1736 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1725 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 1489 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1165 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 1659 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在我他下班的时候，</src>` | 937 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1760 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃，</src>` | 1703 |
| 9 | `<src><\|wait\|></src>` | `<src>就这么</src>` | 1618 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我只是备汤的时候</src>` | 2200 |
| 11 | `<src>小小的愿望</src>` | `<src>就这么一个小小的小愿望</src>` | 1560 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1546 |

---

### Test Example 20 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1965 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 1845 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 1415 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 1253 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 2137 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1169 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐. 내가 </src>` | 2461 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1569 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐? </src>` | 2454 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>응. </src>` | 1509 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1546 |

---

### Test Example 21 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1886 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 1646 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 915 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1355 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 569 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 2301 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1690 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1997 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 2102 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1862 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1609 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1777 |

---

### Test Example 22 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2190 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1686 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1356 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1256 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 986 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1383 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1181 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 2322 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 500 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2220 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1563 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 1931 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1658 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1928 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1731 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1463 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1204 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 2126 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 926 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 2192 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, like </src>` | 786 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 2193 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets </src>` | 1724 |
| 11 | `<src>or gets used to make </src>` | `<src>you to make </src>` | 1964 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1698 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1976 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel. </src>` | 1707 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1521 |
| 4 | `<src><\|wait\|></src>` | `<src>in </src>` | 1117 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>AAB Finance </src>` | 1448 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology. </src>` | 1008 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1809 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the university, </src>` | 1819 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 1920 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 2094 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate consultancy </src>` | 2214 |
| 12 | `<src>corporate consultancy. </src>` | `<src>and. </src>` | 1421 |

---

### Test Example 25 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1882 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1661 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1764 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 963 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 2086 |
| 6 | `<src>难道会是</src>` | `<src>难道会使</src>` | 925 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2033 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的</src>` | 1018 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2268 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1694 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 2142 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1481 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2167 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 1514 |
| 3 | `<src>ギアが</src>` | `<src>ギアです。ギアが</src>` | 617 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと、信号が</src>` | 1502 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 910 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 2035 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 931 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 2041 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 965 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いているっていうこと</src>` | 2305 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 1625 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 2376 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを。</src>` | 1413 |

---

### Test Example 27 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1985 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 1702 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1347 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1103 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀，</src>` | 370 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 2088 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 1041 |
| 8 | `<src>来诊断，</src>` | `<src>十二位医生来诊，</src>` | 2584 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 1042 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 2163 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1352 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 2046 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的来开。</src>` | 1500 |

---

### Test Example 28 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2246 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1708 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1480 |
| 4 | `<src><\|wait\|></src>` | `<src>the </src>` | 1048 |
| 5 | `<src>the instruction </src>` | `<src>instruction </src>` | 508 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1968 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1612 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1886 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 992 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 2146 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1292 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array. </src>` | 2274 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1448 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2182 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1507 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1493 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1165 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1655 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 986 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1647 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1811 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1864 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2078 |
| 11 | `<src><\|wait\|></src>` | `<src>p, </src>` | 1592 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double lam? I don't </src>` | 1669 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1543 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 2020 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 1528 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1476 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1117 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1498 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 794 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 1388 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 2251 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1094 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 2320 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1569 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼，</src>` | 1806 |
| 13 | `<src><\|wait\|></src>` | `<src>它也</src>` | 1407 |
| 14 | `<src>的意思哦。</src>` | `<src>以后的事哦。</src>` | 1340 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1887 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 1896 |
| 3 | `<src>인슐린과 </src>` | `<src>과준 이신 </src>` | 1365 |
| 4 | `<src>이제 거진 </src>` | `<src>물질 이고 이것 들은 </src>` | 1229 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 자광인 결합 </src>` | 2331 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>덕은 굉장히 </src>` | 1678 |
| 7 | `<src>굉장히 아주 </src>` | `<src>바로 </src>` | 1734 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연 으로 미네랄이다. </src>` | 1282 |
| 9 | `<src>이렇게 </src>` | `<src>이것 들은 </src>` | 2355 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>기계 가 결정 으로 </src>` | 1451 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1786 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1468 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1233 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>达到了一个</src>` | 1756 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>甜头，那</src>` | 1688 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 1368 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1256 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1400 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 966 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1411 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 2239 |
| 9 | `<src><\|wait\|></src>` | `<src>继续操作，</src>` | 1255 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦，</src>` | 2432 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1381 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1824 |
| 13 | `<src><\|wait\|></src>` | `<src>因为呢，</src>` | 1427 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1271 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2148 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 1599 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 1517 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是意味着</src>` | 1119 |
| 5 | `<src>所以呢，</src>` | `<src>造成了，所以呢，</src>` | 1608 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 800 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1510 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>遗迹啊、</src>` | 2035 |
| 9 | `<src>也不可能是</src>` | `<src>跟风景，</src>` | 1362 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你历史之间</src>` | 2571 |
| 11 | `<src><\|wait\|></src>` | `<src>就演变出来。</src>` | 1374 |
| 12 | `<src>演变出来的，</src>` | `<src><\|wait\|></src>` | 1667 |
| 13 | `<src>因此会建议</src>` | `<src>因此，会建议</src>` | 1515 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1158 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 2004 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 1596 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 662 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1082 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1072 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 2164 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 1039 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 2254 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place </src>` | 603 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 1715 |
| 11 | `<src>But </src>` | `<src>But </src>` | 2016 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1428 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1654 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1454 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1234 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1818 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1918 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1641 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 922 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 2106 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1150 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2507 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1862 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 2110 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업 </src>` | 1543 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>들은 성장 도 </src>` | 1559 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 </src>` | 1696 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1056 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>授業</src>` | 2015 |
| 2 | `<src>十一二手とか</src>` | `<src>一日二日で</src>` | 1510 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>終わった。おそらく</src>` | 583 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1206 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1097 |
| 6 | `<src>一秒に</src>` | `<src>一日一に</src>` | 1565 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>言ってきた今日ぐらいの</src>` | 905 |
| 8 | `<src>計算ですか</src>` | `<src>季節なんですかね。</src>` | 1830 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 1652 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1568 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2211 |
| 12 | `<src><\|wait\|></src>` | `<src>一日二日で</src>` | 1303 |
| 13 | `<src>十一二手で</src>` | `<src><\|wait\|></src>` | 1820 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1373 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1304 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 944 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1796 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 1643 |
| 3 | `<src><\|wait\|></src>` | `<src>HTML이라고 하는 </src>` | 1034 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 이해 할 수 </src>` | 1339 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 484 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 </src>` | 2184 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1398 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 2221 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1190 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 2512 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1383 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1655 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1340 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 </src>` | 1398 |
| 15 | `<src>필요 합니다. </src>` | `<src>프로그램 이 필요 합니다. </src>` | 1070 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1875 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1802 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1430 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1193 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 1952 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하는 우선 에게로 </src>` | 776 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 </src>` | 1697 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 </src>` | 1443 |
| 9 | `<src><\|wait\|></src>` | `<src>걸려 왔느니라. </src>` | 1452 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 </src>` | 2315 |
| 11 | `<src>너희 에게 </src>` | `<src>내가 너희 에게 </src>` | 1380 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1773 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1533 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1235 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1059 |

---

### Test Example 39 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2132 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 1578 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 644 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1071 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1132 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1986 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 743 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1631 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1581 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1533 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 2348 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1591 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1544 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1560 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려 놓고 </src>` | 1019 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠어. </src>` | 1173 |

---

### Test Example 40 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2253 |
| 2 | `<src><\|wait\|></src>` | `<src>背も原が</src>` | 1687 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 1135 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 에 서름이 돋던 </src>` | 1363 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>바치도 </src>` | 326 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>때의 느낌 이 </src>` | 2153 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>어울 리 없어. 그걸 흔들 어서 </src>` | 1568 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 2053 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 1468 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 2455 |
| 11 | `<src>신이 오면 </src>` | `<src>시눈 이 오면 </src>` | 1461 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 찢겨 줄 알고 </src>` | 1663 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 것이라니까 </src>` | 1714 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1006 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1092 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2139 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1639 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1417 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src><\|wait\|></src>` | 1137 |
| 5 | `<src>也就是</src>` | `<src>比较偏向正财的部分，也就是</src>` | 2028 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 822 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩增长所带来的红利</src>` | 2261 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 985 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1881 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 2062 |
| 11 | `<src>这个月</src>` | `<src>这个月也是</src>` | 2014 |
| 12 | `<src>也是不错，只是</src>` | `<src>不错，只是相对于</src>` | 1682 |
| 13 | `<src>相对正财来说就</src>` | `<src>正财来说，就</src>` | 1638 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 922 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 972 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2123 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1698 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1347 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1188 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 697 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1821 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1733 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you go </src>` | 1938 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 1889 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2107 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level </src>` | 1820 |
| 12 | `<src>attainment. </src>` | `<src>of attainment. </src>` | 1786 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1544 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1135 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 937 |

---

### Test Example 43 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 2138 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>蒸らせてあれ</src>` | 1705 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1133 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 871 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今引き締めと見てる。</src>` | 806 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2097 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 924 |
| 8 | `<src><\|wait\|></src>` | `<src>遠い越えている</src>` | 2277 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>船長貴勢気</src>` | 706 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2188 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1752 |
| 12 | `<src>船大工をやってる</src>` | `<src>船団大工をやってる</src>` | 2421 |
| 13 | `<src>が、</src>` | `<src><\|wait\|></src>` | 1467 |
| 14 | `<src>俺は</src>` | `<src>わおびゃこんなにすごい</src>` | 1523 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1035 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 949 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2293 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맨 니다. </src>` | 1773 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1339 |
| 4 | `<src><\|wait\|></src>` | `<src>하고 있는 걸 </src>` | 1117 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 나가 </src>` | 932 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>이건데 </src>` | 1431 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 으로 가면 </src>` | 1511 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 2076 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 이야긴 또 장렬이에요. </src>` | 1791 |
| 10 | `<src>또 장렬이에요. </src>` | `<src><\|wait\|></src>` | 2178 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 재밌 잖아요. </src>` | 1461 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1640 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1398 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모바일, 그거 는 </src>` | 1172 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>잘 나온 것 같아요. </src>` | 1016 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 935 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2025 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 1628 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1072 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1296 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 476 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 2057 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 960 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 2675 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 723 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 2053 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1548 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 2283 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1558 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because. </src>` | 1450 |
| 15 | `<src>everything at this point is being </src>` | `<src>Everything at this point is being </src>` | 1120 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 1028 |

---

### Test Example 46 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2332 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1518 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 1528 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1201 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 2164 |
| 6 | `<src>that I think are </src>` | `<src>that are really important </src>` | 1152 |
| 7 | `<src>really important. </src>` | `<src><\|wait\|></src>` | 2361 |
| 8 | `<src><\|wait\|></src>` | `<src>to to </src>` | 345 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go </src>` | 2502 |
| 10 | `<src>I have about </src>` | `<src>into, I have about one </src>` | 1547 |
| 11 | `<src>one minute videos </src>` | `<src>minute of videos </src>` | 2286 |
| 12 | `<src>that follow this video </src>` | `<src>at the end of this video </src>` | 1561 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one. </src>` | 1413 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 955 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>You know, in a little more detail, </src>` | 1233 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계서 </src>` | 2131 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1687 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 1450 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 </src>` | 1120 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>사람 과 다른 사람 이 </src>` | 378 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨턴트예요, </src>` | 2168 |
| 7 | `<src><\|wait\|></src>` | `<src>이게 컨설턴트여야 </src>` | 1950 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>되고, </src>` | 1562 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 1103 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2587 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 1334 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람 이 </src>` | 1776 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1424 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스키티에서 </src>` | 1377 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 1138 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 962 |

---

### Test Example 48 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2149 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1664 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 1520 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1137 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 2106 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1033 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 2649 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 853 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 2060 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1398 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1775 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1818 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1389 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1026 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 991 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 536 |

---

### Test Example 49 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 </src>` | 2104 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1515 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>인상 하는 흐름 을 보인 다면 </src>` | 1552 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1223 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 2061 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만, </src>` | 1086 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2084 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 782 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 1723 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2031 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1654 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이기 때문 에 </src>` | 1617 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 시총이 </src>` | 1822 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 948 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨봐야 </src>` | 1072 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 672 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2100 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1796 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1391 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1181 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1745 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 674 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常</src>` | 1665 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们这样说：</src>` | 1856 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1199 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2361 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1268 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1955 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1374 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1338 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1020 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 959 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 382 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1774 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1695 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 내놓 았습니다. </src>` | 1991 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 </src>` | 786 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>의 분석 을 보시면, </src>` | 2229 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1562 |
| 7 | `<src>26비트 FP </src>` | `<src>이 역할 도 FPD </src>` | 2023 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1579 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2429 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 보입니다. </src>` | 1729 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1872 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈 X에서도 없는, </src>` | 1770 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 890 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1113 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L2가 여기 도 없다. </src>` | 493 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 370 |

---

### Test Example 52 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1974 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1521 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1303 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1085 |
| 5 | `<src>he's been without food, </src>` | `<src>he knows that </src>` | 403 |
| 6 | `<src><\|wait\|></src>` | `<src>for even the wilderness </src>` | 2111 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>sporty day, is that he's hungry. </src>` | 1381 |
| 8 | `<src>And so he says </src>` | `<src>And so he sends </src>` | 2229 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus. </src>` | 1026 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>Hey, if you're the Son of God, prove it. </src>` | 2964 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn </src>` | 1457 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>these stones to bread. </src>` | 1677 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1687 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with that? </src>` | 969 |
| 15 | `<src>temptation? </src>` | `<src>The temptation. </src>` | 1043 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 923 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead by bread. </src>` | 499 |
| 18 | `<src>by bread alone. </src>` | `<src>Alone. </src>` | 489 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1826 |
| 2 | `<src>首次觉知到</src>` | `<src>佛罗伊的首次觉知</src>` | 1818 |
| 3 | `<src>那个现象：</src>` | `<src>到那个现象，</src>` | 1399 |
| 4 | `<src>每当我们</src>` | `<src>每当我们</src>` | 1073 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 968 |
| 6 | `<src>处于爱之中，</src>` | `<src>处于爱之中，</src>` | 1439 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱，</src>` | 1613 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1925 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入</src>` | 1788 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2172 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨在掌上的时候，</src>` | 1587 |
| 12 | `<src>它是爱；</src>` | `<src>它是</src>` | 1548 |
| 13 | `<src>到了晚上，</src>` | `<src>爱到了晚上，</src>` | 1745 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成了</src>` | 902 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1064 |
| 16 | `<src>那个钟摆</src>` | `<src>恨那个钟摆。</src>` | 948 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 504 |
| 18 | `<src>继续在移动。</src>` | `<src>一路上。</src>` | 497 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2046 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 1692 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1682 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1074 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1975 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 814 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1865 |
| 8 | `<src>you get into </src>` | `<src>you get into the </src>` | 1380 |
| 9 | `<src>a situation </src>` | `<src>situation where you </src>` | 1936 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2016 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 1899 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1789 |
| 13 | `<src>you need to let us know, </src>` | `<src>you can do </src>` | 1461 |
| 14 | `<src>and we can see about </src>` | `<src>let us know, and we can see about </src>` | 1158 |
| 15 | `<src><\|wait\|></src>` | `<src>uploading those media </src>` | 1094 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>files and then making sure they </src>` | 449 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 270 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 486 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2361 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1611 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 1143 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 876 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR field, </src>` | 799 |
| 6 | `<src><\|wait\|></src>` | `<src>being an </src>` | 1997 |
| 7 | `<src>being of critical importance </src>` | `<src>of critical importance </src>` | 826 |
| 8 | `<src>versus variant </src>` | `<src>versus, you know, </src>` | 2181 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 973 |
| 10 | `<src>databases, </src>` | `<src>variant databases, which is obviously </src>` | 1729 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>one of my loves. </src>` | 2204 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that </src>` | 1620 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree </src>` | 1544 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 1723 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 794 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1239 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 782 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 467 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 511 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2300 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1655 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 986 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 925 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 868 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 2154 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1291 |
| 8 | `<src><\|wait\|></src>` | `<src>the the van </src>` | 2270 |
| 9 | `<src>the the vanguard of social </src>` | `<src>ard of social </src>` | 587 |
| 10 | `<src>change </src>` | `<src>change. </src>` | 2109 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 1598 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1706 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect </src>` | 1762 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1410 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 845 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 1059 |
| 17 | `<src><\|wait\|></src>` | `<src>So, </src>` | 756 |
| 18 | `<src>So you have some </src>` | `<src>you have some </src>` | 472 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 506 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 284 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 163 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2020 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1721 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1460 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的不分分呢，</src>` | 1285 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到</src>` | 1940 |
| 6 | `<src>的部分。</src>` | `<src>一个是课体的部分，</src>` | 766 |
| 7 | `<src>那客厅一般</src>` | `<src>课体一般都</src>` | 1844 |
| 8 | `<src>都是属于</src>` | `<src><\|wait\|></src>` | 1409 |
| 9 | `<src>我们</src>` | `<src>是属于我们在</src>` | 1778 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 2094 |
| 11 | `<src><\|wait\|></src>` | `<src>休息的地方，</src>` | 1511 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，是身体的部分</src>` | 1696 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，反映的是</src>` | 1677 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 805 |
| 15 | `<src>一点时间，</src>` | `<src><\|wait\|></src>` | 1038 |
| 16 | `<src>可以好好的</src>` | `<src>一点时间可以好好的做</src>` | 956 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>一下啦休息，</src>` | 475 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 335 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>小朋友的人的吗？</src>` | 345 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 230 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 339 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1842 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1698 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1490 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1115 |
| 5 | `<src><\|wait\|></src>` | `<src>completely </src>` | 928 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>revolutionize the world. </src>` | 1529 |
| 7 | `<src><\|wait\|></src>` | `<src>The personality </src>` | 1621 |
| 8 | `<src>Their personality is </src>` | `<src>is something that </src>` | 1888 |
| 9 | `<src>something of a </src>` | `<src>has a contradiction, </src>` | 1294 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2526 |
| 11 | `<src>While they're </src>` | `<src>while they're </src>` | 1372 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1749 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1509 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1173 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1140 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 983 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 477 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 525 |
| 19 | `<src>play </src>` | `<src>play the devil's advocate </src>` | 324 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and they </src>` | 159 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy away </src>` | 269 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 278 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 250 |
| 24 | `<src><\|wait\|></src>` | `<src>E.P. Stanslaw </src>` | 323 |
| 25 | `<src>ENTP stands for </src>` | `<src>for. </src>` | 247 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 2229 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>강물 을 거부 한 </src>` | 1478 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후부 를 </src>` | 1662 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 972 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후부의 당슬을 </src>` | 2180 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1175 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2399 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 812 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2321 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1142 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 2000 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1620 |
| 13 | `<src><\|wait\|></src>` | `<src>더루내놓고 </src>` | 1561 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>윤석열 후보 를 </src>` | 1003 |
| 15 | `<src><\|wait\|></src>` | `<src>떨어뜨리 겠다는 뚜끼를 </src>` | 1205 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>품은 공격 성을 </src>` | 392 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 290 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 506 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 317 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 342 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건. </src>` | 354 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 233 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 276 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 290 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 296 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2077 |
| 2 | `<src>食堂ね</src>` | `<src>食後ね今</src>` | 1575 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいな</src>` | 526 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>です。なので</src>` | 1200 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ここの毛織サロンホテル</src>` | 1239 |
| 6 | `<src>も</src>` | `<src>も</src>` | 2006 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1000 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1993 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になっているので</src>` | 962 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 1753 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドーストーンホテル</src>` | 2203 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいなって</src>` | 1731 |
| 13 | `<src>なっていう方はですね</src>` | `<src>いう方はですね</src>` | 1815 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1492 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 943 |
| 16 | `<src><\|wait\|></src>` | `<src>なと。はい。</src>` | 1181 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思います。</src>` | 424 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね</src>` | 561 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 522 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 301 |
| 21 | `<src>歩いて一分</src>` | `<src>一分</src>` | 370 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 317 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 260 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあホテル</src>` | 288 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 278 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 254 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 167 |
| 28 | `<src>ください</src>` | `<src>ください。それなら</src>` | 159 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ですね今回は。</src>` | 157 |
