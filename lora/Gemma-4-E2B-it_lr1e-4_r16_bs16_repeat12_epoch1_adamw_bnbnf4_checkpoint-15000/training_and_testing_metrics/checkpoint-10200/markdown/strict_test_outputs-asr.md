# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9861
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.8477
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
  - PROCESS_TIME_MS_AVG: 1428.5810
  - PROCESS_TIME_MS_P50: 1346.8950
  - PROCESS_TIME_MS_P95: 2656.0640
  - PROCESS_TIME_MS_MAX: 3010.8410

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
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1676 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1423 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 640 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 981 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1264 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1369 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 646 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1772 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 987 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 1817 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 2644 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2872 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>挖一点松子儿里</src>` | 880 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>边，这个油性也很大。</src>` | 1423 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1208 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 936 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点</src>` | 1249 |
| 7 | `<src>儿核桃</src>` | `<src>儿核桃</src>` | 1932 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 621 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>仁儿，仁儿，</src>` | 1828 |
| 10 | `<src>这种核桃</src>` | `<src>这种核桃</src>` | 1605 |
| 11 | `<src>仁儿。</src>` | `<src>仁儿。</src>` | 1299 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2811 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 946 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1225 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1278 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 378 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1685 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1097 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 1631 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1878 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 2478 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 465 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2688 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1062 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1112 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 1296 |
| 5 | `<src><\|wait\|></src>` | `<src>知道，</src>` | 551 |
| 6 | `<src>知道如何</src>` | `<src>如何趋于</src>` | 1490 |
| 7 | `<src>处于中间，</src>` | `<src>终点，</src>` | 1171 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1533 |
| 9 | `<src>虚阿凡</src>` | `<src>虚要凡，</src>` | 1978 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2418 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 543 |

---

### Test Example 5 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1918 |
| 2 | `<src>옹심이, </src>` | `<src>공심 이 </src>` | 1434 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 698 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 공심이 </src>` | 920 |
| 5 | `<src>옹심이가 </src>` | `<src>어 혹시 공심 이가 </src>` | 1368 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1878 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. 야 </src>` | 1887 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 819 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1916 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해방으로 </src>` | 2576 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 맞는 </src>` | 756 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2940 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성들은 </src>` | 765 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1299 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1300 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 898 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1321 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성들이 </src>` | 2392 |
| 8 | `<src>때문 입니다. </src>` | `<src>었기 때문 입니다. </src>` | 712 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1358 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2578 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교수 들은 </src>` | 1020 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 2539 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 691 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1321 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 692 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 796 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 2097 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 2362 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1019 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1098 |
| 10 | `<src><\|wait\|></src>` | `<src>language are you </src>` | 2574 |
| 11 | `<src>language are you using? </src>` | `<src>using? </src>` | 1110 |

---

### Test Example 8 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2724 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 952 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1313 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1349 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1738 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 845 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 1962 |
| 8 | `<src>能量的运行</src>` | `<src><\|wait\|></src>` | 1796 |
| 9 | `<src>状态，</src>` | `<src>能量的运行状态，</src>` | 553 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2378 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1323 |

---

### Test Example 9 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1982 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1431 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 583 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 960 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 1267 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 656 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1417 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1150 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1555 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1910 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 2721 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1375 |

---

### Test Example 10 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1881 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 1438 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 966 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 567 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 1337 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 1239 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 924 |
| 8 | `<src>来诊断，</src>` | `<src>来诊断，</src>` | 2372 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 256 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 1713 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1334 |
| 12 | `<src>他们</src>` | `<src>他们</src>` | 1539 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 1542 |

---

### Test Example 11 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2993 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 671 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1404 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 1290 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 876 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1305 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 1633 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 953 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 1699 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 485 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 2520 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1611 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2553 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 864 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1328 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1344 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 1683 |
| 6 | `<src>research, </src>` | `<src>research, </src>` | 577 |
| 7 | `<src>looking at the ten percent </src>` | `<src>looking at the ten percent </src>` | 2357 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1808 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 924 |
| 10 | `<src>out there, </src>` | `<src>out there, </src>` | 2066 |
| 11 | `<src>people that we can learn from. </src>` | `<src>people that we can learn from. </src>` | 1956 |

---

### Test Example 13 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2507 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 881 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1400 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1253 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1354 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 639 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1041 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1691 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1776 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1636 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1354 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 2154 |

---

### Test Example 14 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2567 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 881 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1307 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1403 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1933 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 1801 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 925 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1963 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 2000 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 850 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运就属凶。</src>` | 2303 |

---

### Test Example 15 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 2662 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 874 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>저열한 일일 수 있지만 </src>` | 1497 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1202 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>진짜 보살 도요. 아니 </src>` | 1661 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | 929 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 있고 </src>` | 1940 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>남한 테 보살 로 보일 필요 가 </src>` | 2010 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>뭐 있어요. </src>` | 1855 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 가신다. 이제 보살 이라는 </src>` | 1187 |
| 11 | `<src>보살 이라는데. </src>` | `<src>거예요. </src>` | 2255 |

---

### Test Example 16 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2803 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 724 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1164 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 515 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1182 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1727 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 765 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 2118 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1871 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2054 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 940 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 2348 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2659 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 1029 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 1226 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 1432 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1790 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1513 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐? 내가 </src>` | 1297 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1800 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2606 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>있는 줄 알았느냐? 응? </src>` | 683 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 2113 |

---

### Test Example 18 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2571 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 에퍼블리토 </src>` | 1004 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽팔 시키고 </src>` | 1259 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1291 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1842 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 941 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>부모 를 죽인 페르 나 </src>` | 1941 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1798 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 2535 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 500 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 2400 |

---

### Test Example 19 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2541 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 946 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1214 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1215 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 453 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1683 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1609 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 1170 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 1810 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2654 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1064 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1752 |

---

### Test Example 20 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1764 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 1474 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 958 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 853 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1114 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1803 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 897 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1979 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 1921 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 2545 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1224 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1617 |

---

### Test Example 21 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2063 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 1415 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 525 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1123 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1265 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>上げ下げできなくなってしまうので、</src>` | 1626 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 626 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 2301 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1806 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうことです</src>` | 489 |
| 11 | `<src>ね。</src>` | `<src>ね。</src>` | 2455 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1120 |
| 13 | `<src>分解完了。</src>` | `<src>分解完了。</src>` | 1753 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1629 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1473 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 958 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 670 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 1279 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 1953 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1156 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃。真的，</src>` | 1601 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1885 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，只有这么一个</src>` | 2754 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望</src>` | 1539 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1647 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 2879 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 769 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1329 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 803 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 632 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 2103 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1962 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 568 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1799 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 1260 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1725 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array. </src>` | 1940 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1388 |

---

### Test Example 24 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1784 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1453 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 644 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキというセットし具合が</src>` | 1135 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1119 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1665 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 606 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 2369 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1814 |
| 10 | `<src>は五経、</src>` | `<src>は5コン、</src>` | 1489 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1523 |
| 12 | `<src>設備寺、五比</src>` | `<src>セットし具合、</src>` | 2007 |
| 13 | `<src>です。</src>` | `<src>ゴビです。</src>` | 1307 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1834 |
| 2 | `<src><\|wait\|></src>` | `<src>选择啊，一个月</src>` | 1439 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二classList，</src>` | 823 |
| 4 | `<src>服务</src>` | `<src>ให服务</src>` | 698 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1312 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1393 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，啊，</src>` | 787 |
| 8 | `<src><\|wait\|></src>` | `<src>在做运维</src>` | 2407 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>十五现金，你会</src>` | 1889 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 882 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给运维好评分的</src>` | 2179 |
| 12 | `<src>的新榜反而</src>` | `<src>新棒，反而</src>` | 2241 |
| 13 | `<src>火了。</src>` | `<src>活了。</src>` | 1251 |

---

### Test Example 26 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 2641 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Datt리고, </src>` | 1047 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 1152 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1312 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 1373 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 799 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2385 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 1829 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 503 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2660 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2300 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1273 |

---

### Test Example 27 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2833 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 842 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1326 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1390 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 2088 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 2439 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1851 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1520 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 1636 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2285 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1434 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2785 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 744 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1303 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1360 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1595 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 711 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 2243 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1914 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1361 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 1677 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2141 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1463 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1323 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2818 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 883 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1494 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1225 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1908 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1019 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1672 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1969 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2572 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1001 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1783 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 1544 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1094 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2547 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1173 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1104 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1289 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1893 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1130 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 1609 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1910 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2671 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 978 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1822 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1666 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1136 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 2642 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 745 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1331 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1287 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1278 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 675 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 1178 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1615 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1851 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 2756 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1212 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 1875 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1515 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 1152 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 2479 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1122 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1240 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1271 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1886 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1495 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 1291 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1911 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 2627 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1223 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 폐업 도 </src>` | 1811 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>하지 않는 현상 들을 </src>` | 1656 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1242 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2448 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 738 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 898 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 745 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1263 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1737 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 912 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 2006 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1803 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 2793 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1498 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1858 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1592 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1008 |

---

### Test Example 34 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2716 |
| 2 | `<src>十一二手とか</src>` | `<src>十一二手とか</src>` | 789 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 1340 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 944 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 448 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1132 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一定強ぐらいの</src>` | 969 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですか</src>` | 2096 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 482 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1894 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2311 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 606 |
| 13 | `<src>十一二手で</src>` | `<src>十一二手で</src>` | 2336 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1166 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1443 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 1031 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 2489 |
| 2 | `<src>HTML이라고 </src>` | `<src>而HTML</src>` | 768 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1163 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>이라고 하는 컴퓨터 도 이해 할 수 </src>` | 614 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1040 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 이해 할 수 </src>` | 2113 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2038 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 585 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1693 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1658 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1357 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 2336 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 작성 하는 </src>` | 1320 |
| 14 | `<src>프로그램 이 </src>` | `<src>프로그램 이 </src>` | 1300 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1183 |

---

### Test Example 36 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2733 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 873 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢</src>` | 1313 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1347 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1853 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 888 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1924 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，跟风险</src>` | 1851 |
| 9 | `<src>也不可能是</src>` | `<src>也不可能是</src>` | 2679 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 1009 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1761 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1299 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1251 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1254 |

---

### Test Example 37 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2765 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 784 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1366 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1137 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 410 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1814 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1152 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you go </src>` | 1608 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 1762 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2699 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level </src>` | 1069 |
| 12 | `<src>attainment. </src>` | `<src>of attainment. </src>` | 1723 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1562 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 1348 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1042 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2912 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 743 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 1329 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1264 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 647 |
| 6 | `<src>that I think are </src>` | `<src>that I think are </src>` | 1488 |
| 7 | `<src>really important. </src>` | `<src>really important. </src>` | 1804 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 835 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 1976 |
| 10 | `<src>I have about </src>` | `<src>I have about </src>` | 2606 |
| 11 | `<src>one minute videos </src>` | `<src>one minute videos </src>` | 1137 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 1837 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1439 |
| 14 | `<src>that cover each one </src>` | `<src>that cover each one </src>` | 1191 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, but. </src>` | 1298 |

---

### Test Example 39 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 2656 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 784 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1355 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1187 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 301 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1753 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 961 |
| 8 | `<src>this is just </src>` | `<src>this is just </src>` | 1849 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1872 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2768 |
| 11 | `<src>But </src>` | `<src>But </src>` | 1131 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1595 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1667 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1365 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1349 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1989 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 1487 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 969 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 657 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 1357 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1562 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 717 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 2171 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1816 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 535 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 2444 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1360 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1859 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것을 </src>` | 1471 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1194 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1409 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1980 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 1498 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 939 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 643 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今奇跡を見てる。</src>` | 1339 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1762 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 831 |
| 8 | `<src><\|wait\|></src>` | `<src>遠い超えている</src>` | 2012 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>ふうの奇跡よ。</src>` | 1860 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2325 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 601 |
| 12 | `<src>船大工をやってる</src>` | `<src>この大工を</src>` | 2017 |
| 13 | `<src>が、</src>` | `<src>やってるが、</src>` | 1400 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 1428 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい階族線を</src>` | 1300 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 1052 |

---

### Test Example 42 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2754 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 817 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1262 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 1370 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1779 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 799 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 2037 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 1871 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 2319 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 675 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 2283 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1219 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1421 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1297 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 946 |

---

### Test Example 43 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2670 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 728 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1400 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1085 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 396 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1539 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 565 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 2517 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 1951 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 2299 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 598 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 2300 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1417 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1268 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 1317 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 906 |

---

### Test Example 44 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 뭐 </src>` | 2003 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 이런 경우 들도 </src>` | 1480 |
| 3 | `<src>있습니다. </src>` | `<src>있습니다. </src>` | 1083 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 가 A라는 사람 과 </src>` | 688 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 서로 </src>` | 1147 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>컨설턴트예요, </src>` | 1687 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 615 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>모이 킹 컨설턴트여가지고 </src>` | 2350 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 1772 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1831 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>뿌렸 을 때 </src>` | 1139 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 2175 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1244 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스쿠티에서 </src>` | 1579 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일 까지 </src>` | 1266 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 1002 |

---

### Test Example 45 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 2527 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1058 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1215 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1315 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1858 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1079 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1673 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 2015 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2650 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1286 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1925 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1475 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1227 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1368 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 351 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2836 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 850 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 1254 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1322 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 2011 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1871 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 894 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 1897 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 2395 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 506 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 2258 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1392 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1215 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1094 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 1104 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 730 |

---

### Test Example 47 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2892 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 857 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>선생 이 뭐라 빌 거야. </src>` | 1529 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 소름 이 돋든 </src>` | 1305 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>닭살이 돋든 </src>` | 1886 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오면 </src>` | 1928 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 783 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1896 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 2656 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1292 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 </src>` | 1927 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1604 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1155 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1330 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 742 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 2767 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 688 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 1546 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1236 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1541 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 655 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2227 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 600 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1505 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2662 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1375 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 2018 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1592 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1091 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 1304 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 716 |

---

### Test Example 49 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 2869 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 991 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1181 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1272 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 거로 거로 </src>` | 616 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>다니 고간에 뭐 </src>` | 1619 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 을 가면 </src>` | 2374 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 외국 에 나가 면 </src>` | 1978 |
| 9 | `<src><\|wait\|></src>` | `<src>또 장렬이에요. </src>` | 2694 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 994 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1807 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1484 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1085 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모바일, 그거 는 </src>` | 1369 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>다인 것 같아요. </src>` | 796 |
| 16 | `<src><\|wait\|></src>` | `<src>예. </src>` | 721 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2739 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 952 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1236 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1369 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1809 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 914 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 1888 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们</src>` | 1797 |
| 9 | `<src>这样说：“</src>` | `<src>这样说：“</src>` | 634 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2313 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1408 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1904 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1607 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 1103 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1254 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 713 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 191 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>弗洛伊德</src>` | 2589 |
| 2 | `<src>首次觉知到</src>` | `<src><\|wait\|></src>` | 761 |
| 3 | `<src>那个现象：</src>` | `<src>首次觉知到的那个现象，</src>` | 1427 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1258 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 1227 |
| 6 | `<src>处于爱之中，</src>` | `<src>爱之中</src>` | 730 |
| 7 | `<src>所谓的爱，</src>` | `<src>所位的爱，</src>` | 1074 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1604 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入恨。</src>` | 1944 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2625 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 984 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱；</src>` | 1787 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1376 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1222 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1356 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆</src>` | 764 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 745 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 482 |

---

### Test Example 52 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 2457 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 1003 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 1265 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1328 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1932 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1202 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 1538 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1783 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2949 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 </src>` | 1782 |
| 11 | `<src><\|wait\|></src>` | `<src>보인다. </src>` | 1432 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1616 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1024 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1335 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 797 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 491 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2716 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 749 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1374 |
| 4 | `<src>move media objects </src>` | `<src><\|wait\|></src>` | 1167 |
| 5 | `<src><\|wait\|></src>` | `<src>move media objects </src>` | 328 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1902 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1246 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1450 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1890 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 2483 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 567 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2357 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1405 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1220 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1318 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 842 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 712 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 506 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 3011 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 686 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 1347 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1065 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 419 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1553 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 619 |
| 8 | `<src>versus variant </src>` | `<src>versus variant </src>` | 2280 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1728 |
| 10 | `<src>databases, </src>` | `<src>databases, </src>` | 362 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2575 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 635 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree </src>` | 2178 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 1530 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1073 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1424 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 652 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 828 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 514 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 2605 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 724 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1314 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1352 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 1494 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 605 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 2597 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1966 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 2540 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 866 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1928 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1411 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1149 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>say to deal with that </src>` | 1387 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 793 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 748 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 496 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone. </src>` | 282 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2894 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 766 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1116 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 532 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1136 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1590 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 863 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2155 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1823 |
| 10 | `<src>change </src>` | `<src>social change </src>` | 1093 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 1891 |
| 12 | `<src><\|wait\|></src>` | `<src>but they rather </src>` | 1950 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect </src>` | 1267 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1503 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1154 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged </src>` | 1306 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 674 |
| 18 | `<src>So you have some </src>` | `<src>so. You have some </src>` | 237 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 489 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 380 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 341 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2658 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 737 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1201 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 577 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1070 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 1655 |
| 7 | `<src>那客厅一般</src>` | `<src><\|wait\|></src>` | 688 |
| 8 | `<src>都是属于</src>` | `<src>它客厅一般都是</src>` | 2251 |
| 9 | `<src>我们</src>` | `<src>属于我们</src>` | 1788 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 495 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2441 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，这身体的部分</src>` | 1564 |
| 13 | `<src>也会反映的是</src>` | `<src>它反映的是</src>` | 1709 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1391 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间，</src>` | 1134 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的做</src>` | 1258 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>一下洗去，</src>` | 364 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 735 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空污衣人的嘛。</src>` | 545 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 346 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 378 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 2541 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 838 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1320 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1312 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 918 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1281 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2038 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 563 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 1755 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 1823 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1170 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, they also </src>` | 2362 |
| 13 | `<src>they also hate </src>` | `<src><\|wait\|></src>` | 1363 |
| 14 | `<src>meaningless conversations </src>` | `<src>hate meaningless conversations </src>` | 1241 |
| 15 | `<src>and like to </src>` | `<src>and like to </src>` | 1158 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1061 |
| 17 | `<src>get straight to the point. </src>` | `<src>get straight to the point. </src>` | 788 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 506 |
| 19 | `<src>play </src>` | `<src>play </src>` | 364 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, and they </src>` | 252 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 199 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 258 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 271 |
| 24 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 282 |
| 25 | `<src>ENTP stands for </src>` | `<src>ENTP stands for </src>` | 271 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 2725 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 838 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1265 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1296 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1867 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1006 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1803 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1833 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2686 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1184 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1608 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1639 |
| 13 | `<src><\|wait\|></src>` | `<src>드러내 놓고 윤석열 </src>` | 1272 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>후보 를 떨어뜨리겠다는 </src>` | 1479 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 350 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 736 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 535 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 374 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 377 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 237 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건 </src>` | 335 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 261 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 269 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 </src>` | 263 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 291 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1947 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 1456 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってる</src>` | 597 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいですなのでここのね</src>` | 1125 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴールドストーンホテル</src>` | 1248 |
| 6 | `<src>も</src>` | `<src>も</src>` | 1790 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1119 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1681 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1934 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 2699 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴールドストーンホテルを</src>` | 1320 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1896 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なっていう方はですね</src>` | 1485 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1143 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 1258 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 330 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>なとはい思いますここ</src>` | 765 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね釜山</src>` | 549 |
| 19 | `<src>駅ももう</src>` | `<src>駅ももう</src>` | 360 |
| 20 | `<src><\|wait\|></src>` | `<src>歩いて</src>` | 356 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかるか</src>` | 271 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんなikan</src>` | 308 |
| 23 | `<src>レベルのね</src>` | `<src>かそんなレベルのね</src>` | 298 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあ</src>` | 259 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 271 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 239 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 161 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 132 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではですね今回は。</src>` | 145 |
