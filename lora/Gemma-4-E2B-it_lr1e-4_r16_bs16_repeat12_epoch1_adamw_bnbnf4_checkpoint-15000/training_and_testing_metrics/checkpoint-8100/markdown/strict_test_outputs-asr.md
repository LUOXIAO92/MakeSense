# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9791
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.7417
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
  - PROCESS_TIME_MS_AVG: 1411.9760
  - PROCESS_TIME_MS_P50: 1506.2430
  - PROCESS_TIME_MS_P95: 2259.4610
  - PROCESS_TIME_MS_MAX: 2738.7570

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
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1772 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1640 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 349 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 1178 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1695 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1214 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 775 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2238 |
| 9 | `<src>虚阿凡</src>` | `<src>虚阿凡</src>` | 713 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 1447 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 1675 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1544 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1055 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 866 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1213 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 777 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1161 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1540 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 659 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 2561 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 1523 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1671 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1972 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>挖一点松子儿，一般</src>` | 1519 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>就咬很大，</src>` | 593 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1036 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1643 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点</src>` | 1118 |
| 7 | `<src>儿核桃</src>` | `<src>核桃</src>` | 912 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1196 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>仁儿，仁儿儿，</src>` | 1914 |
| 10 | `<src>这种核桃</src>` | `<src>这种核桃</src>` | 1851 |
| 11 | `<src>仁儿。</src>` | `<src>仁儿。</src>` | 1907 |

---

### Test Example 4 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1763 |
| 2 | `<src>옹심이, </src>` | `<src>너무 심이 </src>` | 1060 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 859 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 웅심이 </src>` | 1258 |
| 5 | `<src>옹심이가 </src>` | `<src>그래서 혹 웅심이 가 </src>` | 1929 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1552 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. </src>` | 1007 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1854 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 762 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해방 으로 </src>` | 2061 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 맞는 </src>` | 1784 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1805 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1517 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 621 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1246 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1542 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1563 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 572 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 2447 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1191 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1760 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1786 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1595 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1114 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 760 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1179 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 709 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1448 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1645 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 2610 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1157 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1779 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 1821 |

---

### Test Example 7 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 1970 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1123 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 757 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1234 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1640 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1645 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 632 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 의미 입니다. </src>` | 2527 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1319 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 1696 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은 </src>` | 2194 |

---

### Test Example 8 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 1885 |
| 2 | `<src>あの</src>` | `<src>などが</src>` | 949 |
| 3 | `<src>いただもらえる</src>` | `<src>あのいただもらえる</src>` | 963 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1215 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 701 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1289 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1598 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1142 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1769 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1385 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内があります</src>` | 1804 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>ので、もう少しお待ちください。</src>` | 2010 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1669 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 1418 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 722 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1144 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1776 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1584 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>부모 를 죽인 페르 나 </src>` | 1168 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1866 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1506 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1736 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 2009 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1640 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1429 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 582 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1314 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 1939 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 1516 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at the ten percent </src>` | 1157 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1812 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1598 |
| 10 | `<src>out there, </src>` | `<src>out there, people with </src>` | 1717 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 2040 |

---

### Test Example 11 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1890 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1418 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 601 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1201 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1888 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1698 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1210 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 1786 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1682 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 1672 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 2011 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1823 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 959 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 926 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1028 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 449 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1759 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1608 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1230 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1856 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1732 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 1653 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも</src>` | 2220 |

---

### Test Example 13 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1509 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 878 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活的一个轨道，</src>` | 1077 |
| 4 | `<src>的一个轨道哈，</src>` | `<src><\|wait\|></src>` | 1192 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈在它</src>` | 1680 |
| 6 | `<src>在他下班的时候，</src>` | `<src>下面的时候，</src>` | 1000 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1106 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭阶段的</src>` | 2104 |
| 9 | `<src><\|wait\|></src>` | `<src>时候，</src>` | 777 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，就像是</src>` | 1838 |
| 11 | `<src>小小的愿望</src>` | `<src>一个小小的一个愿望</src>` | 1863 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1974 |

---

### Test Example 14 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1704 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1495 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 484 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1318 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1782 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 1734 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1213 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1845 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 1777 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1747 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运就属凶。</src>` | 2167 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1732 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 1625 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 477 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 1362 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1615 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1607 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐? 내가 </src>` | 1241 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1885 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1794 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>있는 줄 알았느냐? 응? </src>` | 2066 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1907 |

---

### Test Example 16 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1654 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1239 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 682 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1224 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1691 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1214 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 778 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 2359 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 731 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1923 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 2102 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1738 |

---

### Test Example 17 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1929 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1239 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 731 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1351 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1976 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1722 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2327 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 690 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2394 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1765 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1722 |

---

### Test Example 18 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2011 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 990 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 904 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 1282 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1743 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1582 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 531 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 2461 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 1199 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 1837 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 1864 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1599 |

---

### Test Example 19 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1757 |
| 2 | `<src><\|wait\|></src>` | `<src>의 좋아요를 </src>` | 1258 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>눌 수 있지만 </src>` | 712 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1302 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 1833 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요. 근데 꾸밀 필요 가 </src>` | 1943 |
| 7 | `<src>뭐 있고 </src>` | `<src>없고 이거 나만 </src>` | 2381 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>제 보살 로 보일 필요 가 </src>` | 884 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>없어요. 우주 가 </src>` | 2186 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 보살 이라는 </src>` | 2044 |
| 11 | `<src>보살 이라는데. </src>` | `<src>거예요. </src>` | 1815 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1728 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 1166 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 790 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1116 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 508 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 1358 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 1569 |
| 8 | `<src>来诊断，</src>` | `<src>来诊断，</src>` | 585 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 2532 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 1472 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1713 |
| 12 | `<src>他们</src>` | `<src>他们</src>` | 1871 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 2209 |

---

### Test Example 21 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 1920 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 858 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 1024 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1167 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 412 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>上げ下げできなくなってしまうので、</src>` | 1882 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1501 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 1483 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1432 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうことです</src>` | 1514 |
| 11 | `<src>ね。</src>` | `<src>ね。</src>` | 1647 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1907 |
| 13 | `<src>分解完了。</src>` | `<src>分解完了。</src>` | 2204 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1653 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 833 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1074 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1281 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1710 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1214 |
| 7 | `<src><\|wait\|></src>` | `<src>長井</src>` | 758 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>英雄氏の仕組み</src>` | 2166 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 790 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 1704 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1664 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 2352 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 2053 |

---

### Test Example 23 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1627 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 840 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1075 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1329 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1829 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1767 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1515 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1636 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 2125 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1830 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1806 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1914 |

---

### Test Example 24 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1625 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1289 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 802 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1172 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1922 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1586 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1153 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1995 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1849 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2065 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子</src>` | 1778 |
| 12 | `<src>连篇。</src>` | `<src>思绪连篇。</src>` | 2027 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1686 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1169 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级市场，哎，</src>` | 922 |
| 4 | `<src>服务</src>` | `<src>服务</src>` | 1080 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1653 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1626 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，呃，</src>` | 630 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2450 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信公众号十几年，你会</src>` | 1403 |
| 10 | `<src>发现</src>` | `<src>发现，给微信</src>` | 1859 |
| 11 | `<src>给微信公众号评分</src>` | `<src>好平凡的</src>` | 1827 |
| 12 | `<src>的新榜反而</src>` | `<src>新棒反而</src>` | 1930 |
| 13 | `<src>火了。</src>` | `<src>火了。</src>` | 1153 |

---

### Test Example 26 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 1987 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1227 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 752 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1196 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1765 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1620 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 595 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2235 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 682 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 2058 |
| 11 | `<src><\|wait\|></src>` | `<src>So this </src>` | 1846 |
| 12 | `<src>this game dot scored array. </src>` | `<src>game.record array. </src>` | 1847 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1845 |

---

### Test Example 27 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1722 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Dilo. </src>` | 1516 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 555 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1144 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 2034 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology. </src>` | 1790 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2359 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the ANU, </src>` | 654 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2097 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2063 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1717 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1784 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 1947 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 1503 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment, </src>` | 483 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1273 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1815 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1705 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1140 |
| 8 | `<src>change can happen </src>` | `<src>happen, </src>` | 1800 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1599 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1676 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1837 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, </src>` | 2517 |
| 13 | `<src>myriad. </src>` | `<src>I'm—</src>` | 405 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1654 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 1212 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 742 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1174 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1712 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1298 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 899 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 2467 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1274 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 1786 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1841 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 1795 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1499 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 980 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1676 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1869 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1229 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 1670 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 </src>` | 1117 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 굉장히 </src>` | 1144 |
| 7 | `<src>굉장히 아주 </src>` | `<src>바로 </src>` | 2364 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src><\|wait\|></src>` | 610 |
| 9 | `<src>이렇게 </src>` | `<src>당뇨 미네랄이다 길이 굉장히 잘 </src>` | 2321 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>잘 </src>` | 1746 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>작동 을 </src>` | 1726 |
| 12 | `<src>그거 에다가 </src>` | `<src>이제 그 후에다가 </src>` | 1917 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1109 |

---

### Test Example 31 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1777 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1215 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 728 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1305 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1755 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1783 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1189 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1914 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2065 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2045 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1819 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1925 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1500 |

---

### Test Example 32 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who just </src>` | 1907 |
| 2 | `<src>just getting going </src>` | `<src>getting going </src>` | 1119 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 768 |
| 4 | `<src><\|wait\|></src>` | `<src>and </src>` | 1130 |
| 5 | `<src>and I have ten of them </src>` | `<src>like ten of them </src>` | 601 |
| 6 | `<src>that I think are </src>` | `<src>that you really </src>` | 1405 |
| 7 | `<src>really important. </src>` | `<src>important </src>` | 1417 |
| 8 | `<src><\|wait\|></src>` | `<src>to to </src>` | 580 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go </src>` | 2451 |
| 10 | `<src>I have about </src>` | `<src>into I have about one </src>` | 1160 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 1721 |
| 12 | `<src>that follow this video </src>` | `<src>at the fall of this video </src>` | 1883 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one. </src>` | 1760 |
| 14 | `<src>that cover each one </src>` | `<src>You know, </src>` | 1669 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1593 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1822 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1414 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢</src>` | 648 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1214 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1748 |
| 6 | `<src>你现在</src>` | `<src><\|wait\|></src>` | 1604 |
| 7 | `<src>所面临的一些</src>` | `<src>你现在所面临的一些</src>` | 1007 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，</src>` | 1961 |
| 9 | `<src>也不可能是</src>` | `<src>跟不幸</src>` | 1397 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你一时</src>` | 1891 |
| 11 | `<src><\|wait\|></src>` | `<src>之间就显现出来。</src>` | 1956 |
| 12 | `<src>演变出来的，</src>` | `<src><\|wait\|></src>` | 2166 |
| 13 | `<src>因此会建议</src>` | `<src>你的经历</src>` | 709 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>会建议属鸡的朋友呢。</src>` | 1610 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1586 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1882 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1277 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1766 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1506 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 640 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2602 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1597 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 1742 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업 들은 </src>` | 1919 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 2616 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 현상 들을 </src>` | 651 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1343 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1556 |
| 2 | `<src>HTML이라고 </src>` | `<src>HTML이라고 </src>` | 822 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1084 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>하는 컴퓨터 도 이해 할 수 </src>` | 1237 |
| 5 | `<src><\|wait\|></src>` | `<src>있고 </src>` | 561 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 이해 할 수 </src>` | 1540 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1595 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 1258 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1741 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1898 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1984 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1920 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 작성 하는 </src>` | 2061 |
| 14 | `<src>프로그램 이 </src>` | `<src>프로그램 이 </src>` | 885 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1227 |

---

### Test Example 36 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1588 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1498 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 472 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1330 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1881 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1605 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 2077 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，</src>` | 1060 |
| 9 | `<src><\|wait\|></src>` | `<src>那我再继续</src>` | 2021 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>操作下去哦。</src>` | 1948 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1784 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1995 |
| 13 | `<src><\|wait\|></src>` | `<src>因为呢，</src>` | 1055 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1117 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1757 |
| 2 | `<src>There were </src>` | `<src>There are </src>` | 1134 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 782 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1258 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1843 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1599 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 913 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 2059 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place </src>` | 1497 |
| 10 | `<src>to look at. </src>` | `<src>where </src>` | 1692 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 2007 |
| 12 | `<src><\|wait\|></src>` | `<src>but the developers, </src>` | 2440 |
| 13 | `<src>developers or engineers </src>` | `<src>engineers </src>` | 508 |
| 14 | `<src>working on BugRepo </src>` | `<src>at XDP on Bugrepos should be </src>` | 1293 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1093 |

---

### Test Example 38 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1752 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1474 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 596 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 1271 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1543 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 1557 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 605 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 2336 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 747 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 2224 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1705 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1760 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1892 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1574 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1012 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1844 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 976 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 944 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1180 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今奇跡を見てる。</src>` | 603 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1391 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1532 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 594 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えてる船の奇跡よ。</src>` | 2712 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1784 |
| 11 | `<src>長年</src>` | `<src></src>` | 1618 |
| 12 | `<src>船大工をやってる</src>` | `<src>流れ舟出川やってる</src>` | 2297 |
| 13 | `<src>が、</src>` | `<src><\|wait\|></src>` | 2008 |
| 14 | `<src>俺は</src>` | `<src>が俺はこんなにすごい</src>` | 934 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1015 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 995 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1643 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1621 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 476 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1183 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1800 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1691 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 </src>` | 1063 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 흘려 </src>` | 1886 |
| 9 | `<src><\|wait\|></src>` | `<src>갔느니라. </src>` | 1534 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1742 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1906 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 2518 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 403 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1618 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1096 |

---

### Test Example 41 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1829 |
| 2 | `<src>十一二手とか</src>` | `<src>十一手とか</src>` | 1231 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>ですね。おそらく</src>` | 716 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1171 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1728 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1438 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一定強ぐらいの</src>` | 728 |
| 8 | `<src>計算ですか</src>` | `<src>成長ですか</src>` | 2466 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 1034 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1794 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1716 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1667 |
| 13 | `<src>十一二手で</src>` | `<src>十一手で</src>` | 1943 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 917 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1180 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 892 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1865 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1237 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 754 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1187 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 2188 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1658 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2380 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>That's one level of attainment. Did you go </src>` | 829 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 2060 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 1924 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1823 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1611 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1084 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 1260 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 873 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 1950 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1060 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>선생 이 뭐라 빌 거야. </src>` | 975 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 소름 이 돋든 </src>` | 1317 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>닭살이 돋든 </src>` | 1930 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오면 </src>` | 1653 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 2456 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 642 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 2082 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1849 |
| 11 | `<src>신이 오면 </src>` | `<src>새니 오면 </src>` | 1782 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1983 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1182 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1216 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 833 |

---

### Test Example 44 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1928 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어 어찌 보면 </src>` | 1306 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 826 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1146 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 2019 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1523 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 1932 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1044 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1761 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1731 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 2097 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 2146 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 662 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 것을 </src>` | 1244 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1096 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 657 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1859 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1378 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 651 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1152 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 2097 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1722 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 2499 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 1385 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 1809 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1941 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1961 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1134 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1128 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1004 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 760 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 770 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 1947 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 1521 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 552 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1156 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 걸어 걸어다니 </src>` | 2160 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>공간 에 뭐 </src>` | 1514 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 을 가면 </src>` | 1727 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 외국 에 </src>` | 1301 |
| 9 | `<src><\|wait\|></src>` | `<src>나가 면도 장렬 이에요. </src>` | 2135 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 1800 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1833 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1946 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 893 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>몰아 바이오. </src>` | 1227 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 된 것 같아요. </src>` | 901 |
| 16 | `<src><\|wait\|></src>` | `<src>예. </src>` | 804 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1790 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 1129 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 828 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1357 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 1713 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1599 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 991 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 2259 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 1872 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 1872 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1982 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1994 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 965 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1194 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 962 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 889 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1741 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1256 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 892 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1184 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1654 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1739 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1386 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 1644 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1598 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1612 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1930 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 2701 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1020 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1207 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 911 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 857 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1820 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1321 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 685 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1327 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1734 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1494 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常</src>` | 534 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们这样说：</src>` | 2532 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1271 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1725 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1841 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 2084 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1176 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1438 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 994 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 740 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 785 |

---

### Test Example 50 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>弗洛伊德</src>` | 1637 |
| 2 | `<src>首次觉知到</src>` | `<src>首次觉知到</src>` | 1368 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象：</src>` | 598 |
| 4 | `<src>每当我们</src>` | `<src>每当我们</src>` | 1188 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1765 |
| 6 | `<src>处于爱之中，</src>` | `<src>处于爱之中，</src>` | 1580 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱，</src>` | 548 |
| 8 | `<src>我们也</src>` | `<src>我们也</src>` | 2221 |
| 9 | `<src>同时进入恨。</src>` | `<src>同时进入</src>` | 506 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1660 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨。在早上的时候，</src>` | 1662 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱；</src>` | 2182 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 2263 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成</src>` | 750 |
| 15 | `<src><\|wait\|></src>` | `<src>恨。</src>` | 1105 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆</src>` | 1018 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 569 |
| 18 | `<src>继续在移动。</src>` | `<src>一抖一抖。</src>` | 691 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1559 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 1628 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 509 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1193 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1773 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1704 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 2593 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 613 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2228 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 보인다. </src>` | 1850 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1724 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1930 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1531 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1154 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 763 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 532 |

---

### Test Example 52 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 1834 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 807 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저의 가 </src>` | 1180 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1267 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>비라는 사람 이 </src>` | 1887 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트예요. </src>` | 1952 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트가 </src>` | 2625 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>여기 있고, </src>` | 1488 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 1754 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2001 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 2634 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라는 사람 이 </src>` | 368 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1474 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스큐티에서 </src>` | 1163 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 719 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까, </src>` | 496 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1799 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 1154 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 905 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1158 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1824 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1638 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 986 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1925 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1394 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 1780 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 2042 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2651 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 424 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1603 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1056 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 803 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 368 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 471 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2046 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1113 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 776 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1170 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 1679 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 877 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1244 |
| 8 | `<src>versus variant </src>` | `<src>versus variant </src>` | 1972 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 897 |
| 10 | `<src>databases, </src>` | `<src>databases, </src>` | 1590 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 1780 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1805 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree </src>` | 2739 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 1073 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1138 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 876 |
| 17 | `<src>draw from, </src>` | `<src>draw from. </src>` | 850 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>There's nothing to draw from, right? </src>` | 557 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 382 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1627 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1264 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 687 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1209 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 2102 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1506 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 2678 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1049 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 1956 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 2319 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2188 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 766 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1255 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that </src>` | 1211 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 782 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 694 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead by </src>` | 461 |
| 18 | `<src>by bread alone. </src>` | `<src>rather alone. </src>` | 408 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1755 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1320 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 683 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1329 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1731 |
| 6 | `<src>的部分。</src>` | `<src>的部分，</src>` | 1488 |
| 7 | `<src>那客厅一般</src>` | `<src><\|wait\|></src>` | 536 |
| 8 | `<src>都是属于</src>` | `<src>它客厅一般都是</src>` | 2419 |
| 9 | `<src>我们</src>` | `<src>属于我们要</src>` | 633 |
| 10 | `<src>在休息的地方，</src>` | `<src>休息的地方，</src>` | 2079 |
| 11 | `<src><\|wait\|></src>` | `<src>所以</src>` | 1773 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>呢，是身体的部分</src>` | 1818 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，反映的是</src>` | 1892 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1201 |
| 15 | `<src>一点时间，</src>` | `<src><\|wait\|></src>` | 1096 |
| 16 | `<src>可以好好的</src>` | `<src>一点时间可以</src>` | 751 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>好好地坐下来休息，</src>` | 911 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 478 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 435 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 318 |
| 21 | `<src>所以是说。</src>` | `<src>所以也是说。</src>` | 306 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2011 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1139 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 760 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1241 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1712 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't know </src>` | 1814 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1157 |
| 8 | `<src><\|wait\|></src>` | `<src>the the van </src>` | 1817 |
| 9 | `<src>the the vanguard of social </src>` | `<src><\|wait\|></src>` | 1410 |
| 10 | `<src>change </src>` | `<src>ard of social change. </src>` | 1825 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 1924 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2547 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 413 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1352 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1098 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 697 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 775 |
| 18 | `<src>So you have some </src>` | `<src>So you have something </src>` | 475 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 381 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 333 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 337 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1626 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1302 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 678 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1223 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1828 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1606 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 911 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1986 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 1303 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 1732 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1832 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1689 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1588 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1488 |
| 15 | `<src>and like to </src>` | `<src>and like to </src>` | 1132 |
| 16 | `<src><\|wait\|></src>` | `<src>get straight to the </src>` | 738 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 661 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 450 |
| 19 | `<src>play </src>` | `<src>play </src>` | 380 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, and they </src>` | 379 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 360 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 300 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 277 |
| 24 | `<src><\|wait\|></src>` | `<src>ENTP </src>` | 265 |
| 25 | `<src>ENTP stands for </src>` | `<src>stands for </src>` | 147 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1709 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1464 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 617 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1175 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1952 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1576 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1925 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1051 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1625 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1704 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1952 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 2496 |
| 13 | `<src><\|wait\|></src>` | `<src>드러내 놓고 윤석열 후보 를 </src>` | 1082 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1235 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 884 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 869 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 480 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 400 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 359 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 360 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건 </src>` | 300 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 293 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 304 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 학이 얼마나 </src>` | 283 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 292 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1810 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね今</src>` | 878 |
| 3 | `<src>今作ってる</src>` | `<src>作ってる</src>` | 1032 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいです。なのでここのね</src>` | 1237 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>プロフェッショナルホテル</src>` | 707 |
| 6 | `<src>も</src>` | `<src><\|wait\|></src>` | 1218 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>もう朝食が食べれる場所</src>` | 1757 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1051 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1833 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 1447 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴルドーストーンホテル</src>` | 1887 |
| 12 | `<src>泊まってみたい</src>` | `<src><\|wait\|></src>` | 1905 |
| 13 | `<src>なっていう方はですね</src>` | `<src>泊まってみたいなって方はですね</src>` | 2673 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 829 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 1206 |
| 16 | `<src><\|wait\|></src>` | `<src>なと。はい。</src>` | 1029 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思います。ここに</src>` | 784 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね</src>` | 343 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 397 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 410 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 302 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 361 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 272 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあ</src>` | 225 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 187 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 240 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 287 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 261 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は。</src>` | 142 |
