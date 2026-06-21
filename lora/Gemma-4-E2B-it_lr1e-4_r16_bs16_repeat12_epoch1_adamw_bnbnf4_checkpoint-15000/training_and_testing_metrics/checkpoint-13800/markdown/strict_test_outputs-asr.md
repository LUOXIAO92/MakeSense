# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9903
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.9536
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
  - PROCESS_TIME_MS_AVG: 1335.5250
  - PROCESS_TIME_MS_P50: 1348.4220
  - PROCESS_TIME_MS_P95: 2151.8820
  - PROCESS_TIME_MS_MAX: 2607.9470

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
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1832 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 890 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 961 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 1724 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1167 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1385 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 382 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2244 |
| 9 | `<src>虚阿凡</src>` | `<src>虚阿凡</src>` | 868 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 1525 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 1612 |

---

### Test Example 2 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2020 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 723 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1033 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1713 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1193 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1208 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 352 |
| 8 | `<src>때문 입니다. </src>` | `<src>었기 때문 입니다. </src>` | 2245 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 426 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모를 랐던 </src>` | 2145 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 1672 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src><\|wait\|></src>` | 1653 |
| 2 | `<src>あの特に</src>` | `<src>最初からあの特に</src>` | 744 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 1066 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1801 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1078 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1009 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 531 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2526 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 1264 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 1911 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1607 |

---

### Test Example 4 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 1975 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 714 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1056 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1700 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1206 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 785 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 764 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1419 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1194 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1311 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 2192 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1450 |

---

### Test Example 5 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1961 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 850 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1034 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 2063 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 907 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1341 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1370 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 1300 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1300 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 2207 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 1533 |

---

### Test Example 6 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2030 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>挖一点松子儿里</src>` | 852 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>边，这个油性也很大。</src>` | 1112 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1674 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1101 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点</src>` | 1480 |
| 7 | `<src>儿核桃</src>` | `<src>核桃仁，</src>` | 1671 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 995 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>其实</src>` | 1844 |
| 10 | `<src>这种核桃</src>` | `<src>这这种核桃</src>` | 1790 |
| 11 | `<src>仁儿。</src>` | `<src>呢。</src>` | 1403 |

---

### Test Example 7 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1726 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 840 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1037 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1947 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 995 |
| 6 | `<src>research, </src>` | `<src>research, </src>` | 1440 |
| 7 | `<src>looking at the ten percent </src>` | `<src>looking at the ten percent </src>` | 1745 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 869 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1580 |
| 10 | `<src>out there, </src>` | `<src>out there, </src>` | 1956 |
| 11 | `<src>people that we can learn from. </src>` | `<src>people that we can learn from. </src>` | 1558 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1764 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 859 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 985 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1876 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1021 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 1409 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1269 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1475 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 2030 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1593 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运就属凶。</src>` | 1528 |

---

### Test Example 9 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1648 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 702 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1087 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1687 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1209 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1406 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 582 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 2190 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1649 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1975 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 1525 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1857 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 857 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1088 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 2217 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 676 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1431 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 1870 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 761 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1991 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1635 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1604 |

---

### Test Example 11 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1738 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 854 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 1072 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1922 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 923 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1399 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src><\|wait\|></src>` | 1064 |
| 8 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 페르 나 </src>` | 1687 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1808 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1785 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 1674 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1879 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 760 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 953 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 361 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 2011 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 817 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1397 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 2137 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 537 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1993 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 1616 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1760 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1786 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 872 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 1060 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 2440 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 527 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1312 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐? 내가 </src>` | 1591 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1154 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1520 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>있는 줄 알았느냐? 응? </src>` | 2144 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1776 |

---

### Test Example 14 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1824 |
| 2 | `<src>옹심이, </src>` | `<src>옹심이, </src>` | 784 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1108 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 옹심이, 쌀국수하고 </src>` | 2391 |
| 5 | `<src>옹심이가 </src>` | `<src>옹심이가 </src>` | 610 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1353 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. </src>` | 1577 |
| 8 | `<src>야, </src>` | `<src>야, </src>` | 1069 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1799 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해장으로도 조금 죽입니다, </src>` | 1963 |
| 11 | `<src>진짜. </src>` | `<src>진짜. </src>` | 1778 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1979 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 759 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1083 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1994 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1001 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1434 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2114 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 567 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2253 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1710 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1904 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 2000 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 733 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1065 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 488 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1550 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 932 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1359 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 381 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2283 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 999 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1524 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array. </src>` | 1801 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1834 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1725 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 728 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 686 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 573 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1787 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1009 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1396 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 927 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1728 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 1103 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1751 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 1907 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1524 |

---

### Test Example 18 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1836 |
| 2 | `<src><\|wait\|></src>` | `<src>의지 를 </src>` | 734 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>내일 수 있지만 </src>` | 1097 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1685 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>진짜 보살 도요. 아니 </src>` | 1293 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 의 보살 인데 꾸밀 필요 가 </src>` | 1491 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 있고 </src>` | 2452 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>남한 테 보살 로 보일 필요 가 </src>` | 1137 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>뭐 있어요. 우주 가 </src>` | 1931 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 </src>` | 1640 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는데. </src>` | 1735 |

---

### Test Example 19 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 1968 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 717 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 914 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 462 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1875 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>上げ下げできなくなってしまうので、</src>` | 954 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1304 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 1378 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1272 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうことです</src>` | 1215 |
| 11 | `<src>ね。</src>` | `<src>ね。</src>` | 1969 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1522 |
| 13 | `<src>分解完了。</src>` | `<src>分解完了。</src>` | 1669 |

---

### Test Example 20 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2051 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 704 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1197 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 2117 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 766 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1389 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 1162 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 1498 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 1293 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 2098 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 1519 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1619 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1563 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 734 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 597 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 631 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 1939 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 1025 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1364 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃。真的，</src>` | 2608 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1220 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，只有这么一个</src>` | 2353 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望</src>` | 1504 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1659 |

---

### Test Example 22 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1697 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 837 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1091 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2008 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 922 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1344 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2176 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 563 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1920 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1652 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1682 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1600 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1786 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Dettig. </src>` | 883 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 1021 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1933 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 1023 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 1391 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2058 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 643 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1711 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 1980 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1847 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1441 |

---

### Test Example 24 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1788 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 762 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1147 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1664 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 1164 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 883 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 717 |
| 8 | `<src>来诊断，</src>` | `<src>来诊断，</src>` | 2471 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 1011 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 1607 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1760 |
| 12 | `<src>他们</src>` | `<src>他们</src>` | 1714 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 1583 |

---

### Test Example 25 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1702 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 783 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1112 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 2306 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 742 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1391 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 2429 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1073 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 1700 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1774 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1683 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1519 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1700 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 882 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 998 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1978 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1039 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1349 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 2540 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 1099 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 1635 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1837 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1726 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1394 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1990 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 759 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1169 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 2006 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 885 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1344 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1243 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1396 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1231 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1794 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1638 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 1833 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1273 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1748 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 765 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级市场，哎，</src>` | 1118 |
| 4 | `<src>服务</src>` | `<src>服务</src>` | 1878 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1013 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1464 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，呃，</src>` | 1308 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1352 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信公众号十几年，你会</src>` | 1410 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 1982 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信公众号评分</src>` | 1475 |
| 12 | `<src>的新榜反而</src>` | `<src>的新榜反而</src>` | 1691 |
| 13 | `<src>火了。</src>` | `<src>火了。</src>` | 1162 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1763 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 930 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 956 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1813 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1124 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1439 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 2020 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 642 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2034 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 1648 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2069 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1304 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1276 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1852 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 708 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1075 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 2127 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 888 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1440 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 2427 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 878 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1550 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 1639 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1936 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1533 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1256 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1724 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 713 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1144 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1735 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1135 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1345 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 527 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 2184 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1229 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 2121 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1486 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 1737 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1174 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 1131 |

---

### Test Example 32 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1873 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 850 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢</src>` | 1046 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1944 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 999 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1390 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1796 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，跟风险</src>` | 912 |
| 9 | `<src>也不可能是</src>` | `<src>也不可能是</src>` | 1638 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 1951 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1446 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1785 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1340 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1034 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1657 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 852 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 964 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1729 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1187 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1395 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1025 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 1746 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2070 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 1559 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1663 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1711 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1249 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1017 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1645 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 958 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1000 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 2309 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 615 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1397 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2578 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1406 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 2137 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1518 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 폐업 도 </src>` | 1845 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>하지 않는 현상 들을 </src>` | 1372 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1165 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1826 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 715 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1109 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1788 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1094 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1414 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 937 |
| 8 | `<src>this is just </src>` | `<src>this is just </src>` | 1705 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1002 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 1581 |
| 11 | `<src>But </src>` | `<src>But </src>` | 1563 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1878 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1427 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1349 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1111 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1622 |
| 2 | `<src>HTML이라고 </src>` | `<src>HTML이라고 </src>` | 731 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 933 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>하는 컴퓨터 도 이해 할 수 </src>` | 539 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1802 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 이해 할 수 </src>` | 1044 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1240 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 2576 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1141 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1996 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1620 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1703 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 작성 하는 </src>` | 1296 |
| 14 | `<src>프로그램 이 </src>` | `<src>프로그램 이 </src>` | 1268 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1065 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1861 |
| 2 | `<src>十一二手とか</src>` | `<src>十一二手とか</src>` | 766 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>じゃないですか。おそらく</src>` | 1117 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1750 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1066 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 785 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一定強ぐらいの</src>` | 798 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですか</src>` | 1613 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 948 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1330 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2076 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1445 |
| 13 | `<src>十一二手で</src>` | `<src>十一二手で</src>` | 1731 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1195 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1330 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 1001 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1709 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 876 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1034 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 2048 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 906 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1394 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 2443 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 433 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1932 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1535 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1795 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1527 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1348 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1047 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 794 |

---

### Test Example 39 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2024 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 753 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>선생 이 뭐라 빌 거야. </src>` | 1161 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 소름 이 돋든 </src>` | 2339 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>닭살이 돋든 </src>` | 749 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오면 </src>` | 1299 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1716 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 894 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 1373 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 2124 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 </src>` | 1508 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1809 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1373 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1094 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 925 |

---

### Test Example 40 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 1961 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 723 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 1111 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1772 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1132 |
| 6 | `<src>that I think are </src>` | `<src>that I think are </src>` | 1383 |
| 7 | `<src>really important. </src>` | `<src>really important. </src>` | 1218 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1439 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 1280 |
| 10 | `<src>I have about </src>` | `<src>I have about </src>` | 2111 |
| 11 | `<src>one minute videos </src>` | `<src>one minute videos </src>` | 1461 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 1771 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1229 |
| 14 | `<src>that cover each one </src>` | `<src>that cover each one </src>` | 1292 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, but. </src>` | 1184 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1910 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 757 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1123 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2061 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 1058 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1298 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1904 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>That's one level of attainment. Did you go </src>` | 761 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 1844 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 1816 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 2078 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1291 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1394 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 1175 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 869 |

---

### Test Example 42 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1822 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 814 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1065 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 2336 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 582 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 1434 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 2328 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 356 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 2129 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 1695 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1919 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1405 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1465 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1100 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 846 |

---

### Test Example 43 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1896 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 803 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1088 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1701 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今奇跡を見てる。</src>` | 1199 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1419 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1259 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1437 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えてる船の奇跡よ。</src>` | 1604 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1950 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1402 |
| 12 | `<src>船大工をやってる</src>` | `<src>船大工をやってる</src>` | 1858 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 1180 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 1086 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい海賊船を</src>` | 1097 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 893 |

---

### Test Example 44 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1920 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 758 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1081 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1696 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 1271 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1395 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 1348 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1318 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1080 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1750 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 1701 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1618 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1491 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것을 </src>` | 1234 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1208 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1040 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1929 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 825 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 1047 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1927 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1036 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1438 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 2398 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 623 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 1791 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1612 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1889 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1384 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1459 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1018 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 700 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 917 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1812 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 701 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 1187 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 2209 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 698 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1449 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2109 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 555 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1939 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1641 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1757 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 1647 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1351 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1104 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 930 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 793 |

---

### Test Example 47 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1623 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 863 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 1082 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 2204 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 734 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1346 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 2165 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 531 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2152 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 보인다. </src>` | 1669 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1947 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1317 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1313 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1173 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 1018 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 627 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 2003 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 861 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1020 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2080 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 걸어 걸어다니 </src>` | 1045 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>공간 에 뭐 </src>` | 1282 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 을 가면 </src>` | 2420 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 외국 에 나가 면 </src>` | 585 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1785 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>또 장렬이에요. </src>` | 1671 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 창피 하네요. </src>` | 2045 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 </src>` | 1420 |
| 13 | `<src>이제 </src>` | `<src>이제 </src>` | 1254 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>열심히 물어봐요. </src>` | 1125 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다인 것 같아요. </src>` | 1054 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 520 |

---

### Test Example 49 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 뭐 </src>` | 1911 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 이런 경우 들도 </src>` | 893 |
| 3 | `<src>있습니다. </src>` | `<src>있습니다. </src>` | 1018 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 가 A라는 사람 과 </src>` | 2372 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 서로 </src>` | 643 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>컨설턴트예요, </src>` | 1406 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2437 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>모이 킹 컨설턴트여가지고 </src>` | 1161 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 1746 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1904 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>뿌렸 을 때 </src>` | 1669 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1360 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1126 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스쿠티에서 </src>` | 1185 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일 까지 </src>` | 749 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 541 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1911 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 833 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1048 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 2052 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 903 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1406 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 2147 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们</src>` | 527 |
| 9 | `<src>这样说：“</src>` | `<src>这样说：“</src>` | 2075 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1533 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1485 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1788 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1273 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 1040 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 913 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 945 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 248 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1846 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 732 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1149 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 2166 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 791 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1365 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 2561 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1276 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 2069 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 1455 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1828 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1191 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1323 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1035 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 990 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 310 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>弗洛伊德</src>` | 1706 |
| 2 | `<src>首次觉知到</src>` | `<src>首次觉知到</src>` | 809 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象：</src>` | 1038 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1944 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 926 |
| 6 | `<src>处于爱之中，</src>` | `<src><\|wait\|></src>` | 1397 |
| 7 | `<src>所谓的爱，</src>` | `<src>爱之中，所谓的爱，</src>` | 1264 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1437 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入恨。</src>` | 1399 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2141 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 1408 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱；</src>` | 1772 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1261 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1179 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1009 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆</src>` | 899 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 261 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 448 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1680 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 712 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1076 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1665 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 1261 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1392 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 1651 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1096 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 1373 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 2374 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1846 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1520 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1294 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that </src>` | 1094 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 825 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 904 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 440 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone. </src>` | 278 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1868 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 731 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1211 |
| 4 | `<src>move media objects </src>` | `<src><\|wait\|></src>` | 1886 |
| 5 | `<src><\|wait\|></src>` | `<src>move media objects </src>` | 999 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1457 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1585 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1016 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1659 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 1948 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1544 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1867 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1385 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1100 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 718 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 1058 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 464 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 417 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2099 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 685 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 1096 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1674 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 1231 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1382 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 448 |
| 8 | `<src>versus variant </src>` | `<src>versus variant </src>` | 2202 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 906 |
| 10 | `<src>databases, </src>` | `<src>databases, </src>` | 1504 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 1899 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1730 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree </src>` | 1572 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 1318 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1001 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 974 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 489 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 557 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 353 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2011 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 757 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 914 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 431 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1773 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1013 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1461 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1565 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of social </src>` | 1037 |
| 10 | `<src>change </src>` | `<src>change </src>` | 1260 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 2172 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1465 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1836 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1193 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1096 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 1081 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 866 |
| 18 | `<src>So you have some </src>` | `<src>So you have some </src>` | 294 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 434 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 376 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 273 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1844 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 754 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1071 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1998 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 989 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 1398 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 1352 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1270 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 1080 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 1907 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1553 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，这身体的部分</src>` | 1814 |
| 13 | `<src>也会反映的是</src>` | `<src>也会反映的是</src>` | 1279 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1202 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间，</src>` | 989 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 870 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息。可是</src>` | 626 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>我们可以看到这边是</src>` | 476 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 479 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 207 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 259 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1715 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 751 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1098 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1694 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1169 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1481 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2532 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 865 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 1569 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 1694 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1924 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1380 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1300 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1021 |
| 15 | `<src>and like to </src>` | `<src>and like to </src>` | 944 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 698 |
| 17 | `<src>get straight to the point. </src>` | `<src>get straight to the point. </src>` | 441 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 261 |
| 19 | `<src>play </src>` | `<src>play </src>` | 203 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, and they </src>` | 329 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 223 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 279 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 247 |
| 24 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 251 |
| 25 | `<src>ENTP stands for </src>` | `<src>ENTP stands for </src>` | 218 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1778 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 826 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1057 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 2016 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 941 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1342 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2538 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 962 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1641 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1700 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1875 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1504 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1251 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | 1430 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 975 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 356 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 231 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 375 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 291 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 245 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>가슴 발 이준석의 성상납 건 </src>` | 312 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 218 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 277 |
| 24 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 224 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | 274 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1870 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 753 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってる</src>` | 933 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいですなのでここのね</src>` | 520 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴールドストーンホテル</src>` | 1890 |
| 6 | `<src>も</src>` | `<src>も</src>` | 811 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1389 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1764 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 880 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 2163 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴールドストーンホテルを</src>` | 1587 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1908 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なっていう方はですね</src>` | 1381 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1335 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 1026 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 829 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>なとはい思いますここ</src>` | 1029 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね釜山</src>` | 476 |
| 19 | `<src>駅ももう</src>` | `<src>駅ももう</src>` | 394 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 286 |
| 21 | `<src>歩いて一分</src>` | `<src>歩いて一分</src>` | 261 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないかそんな</src>` | 224 |
| 23 | `<src>レベルのね</src>` | `<src>レベルのね</src>` | 243 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあ</src>` | 161 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 230 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 228 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 223 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 138 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではですね今回は。</src>` | 135 |
