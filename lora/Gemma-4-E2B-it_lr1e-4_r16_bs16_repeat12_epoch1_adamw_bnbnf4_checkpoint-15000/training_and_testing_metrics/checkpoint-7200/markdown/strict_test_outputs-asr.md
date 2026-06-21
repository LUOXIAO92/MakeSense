# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9638
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.7086
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
  - PROCESS_TIME_MS_AVG: 1434.6060
  - PROCESS_TIME_MS_P50: 1480.9710
  - PROCESS_TIME_MS_P95: 2290.6600
  - PROCESS_TIME_MS_MAX: 3105.7840

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
| 1 | `<src><\|wait\|></src>` | `<src>快在哪里</src>` | 2187 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>这边？</src>` | 755 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个友行</src>` | 1078 |
| 4 | `<src>然后</src>` | `<src>也很大，</src>` | 1863 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 596 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我再放大点，</src>` | 1754 |
| 7 | `<src>儿核桃</src>` | `<src>和陶儿</src>` | 1570 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1961 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>这两个儿，</src>` | 301 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 1222 |
| 11 | `<src>仁儿。</src>` | `<src>和陶儿。</src>` | 2565 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1692 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 758 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 1072 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1883 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 638 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1603 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1644 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1657 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 643 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 1454 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 2358 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2127 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是</src>` | 1022 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1684 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1005 |
| 5 | `<src>爱浇水、</src>` | `<src>爱交洗</src>` | 1099 |
| 6 | `<src>施肥，</src>` | `<src>十倍</src>` | 1122 |
| 7 | `<src>给足</src>` | `<src>给</src>` | 1532 |
| 8 | `<src>孩子心理营养，</src>` | `<src>主孩子心灵营养，</src>` | 439 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1856 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待</src>` | 2063 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 2173 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2003 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1617 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1479 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 751 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1663 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 552 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 1549 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2033 |
| 9 | `<src>虚阿凡</src>` | `<src>虚慈凡</src>` | 1022 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2491 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 1091 |

---

### Test Example 5 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2225 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성들은 </src>` | 962 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 888 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1809 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 825 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1550 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성들이 </src>` | 1526 |
| 8 | `<src>때문 입니다. </src>` | `<src>었기 때문 입니다. </src>` | 2046 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1009 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2376 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교수 학들은. </src>` | 1344 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1760 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 835 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 955 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1837 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1190 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1234 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1509 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 2106 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1109 |
| 10 | `<src><\|wait\|></src>` | `<src>language are you </src>` | 2585 |
| 11 | `<src>language are you using? </src>` | `<src>using? </src>` | 975 |

---

### Test Example 7 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1857 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1149 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1629 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1043 |
| 5 | `<src>This is tip of the stem </src>` | `<src><\|wait\|></src>` | 1570 |
| 6 | `<src>research, </src>` | `<src>tip of the stem research, </src>` | 682 |
| 7 | `<src>looking at the ten percent </src>` | `<src>looking at the ten percent </src>` | 1498 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2044 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1023 |
| 10 | `<src>out there, </src>` | `<src>out there, </src>` | 2646 |
| 11 | `<src>people that we can learn from. </src>` | `<src>people that we can learn from. </src>` | 1143 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1854 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 1410 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 1835 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 625 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1760 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 452 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>부모 를 죽인 애려나 </src>` | 1627 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2018 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1569 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2358 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 1310 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아, 저는 </src>` | 1989 |
| 2 | `<src>옹심이, </src>` | `<src>용신이 </src>` | 1202 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1793 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용신이고 </src>` | 797 |
| 5 | `<src>옹심이가 </src>` | `<src>그래서 용신이 </src>` | 1172 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1138 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. </src>` | 1611 |
| 8 | `<src>야, </src>` | `<src>야, </src>` | 2046 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1592 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해방 으로 </src>` | 2335 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 맞는 것 </src>` | 1376 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2075 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1475 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1833 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 695 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1826 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1589 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 427 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 1856 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1898 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2208 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1298 |

---

### Test Example 11 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2040 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 817 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 1002 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1806 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 461 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1862 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1599 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1933 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 404 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1907 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 2248 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1296 |

---

### Test Example 12 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2184 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1154 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1802 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 877 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1966 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 507 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1296 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 2198 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2064 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2119 |
| 11 | `<src>And until next time. </src>` | `<src>And in telling next time. </src>` | 1439 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1925 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 1527 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 1719 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 910 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1752 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1565 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐? 내가 </src>` | 1743 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 623 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1748 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>있는 줄 알았느냐? 응? </src>` | 2466 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1542 |

---

### Test Example 14 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1897 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1500 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1579 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 904 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1877 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 1610 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1513 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 836 |
| 9 | `<src>独立承担。</src>` | `<src>不理成担，</src>` | 2240 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1945 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运是属凶。</src>` | 1898 |

---

### Test Example 15 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1946 |
| 2 | `<src><\|wait\|></src>` | `<src>의 좋아요를 </src>` | 1020 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>눌 수 있지만 </src>` | 1698 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1082 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기가 </src>` | 1175 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요 근데 꾸밀 필요 가 </src>` | 1161 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 있고 나만 </src>` | 1570 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>꾸실 보살 로 보일 필요 가 </src>` | 2105 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>뭐 있어요 우주 가 </src>` | 2589 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 보살 이라는 </src>` | 1855 |
| 11 | `<src>보살 이라는데. </src>` | `<src>거예요. </src>` | 1856 |

---

### Test Example 16 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2187 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 733 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1072 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも用意しております</src>` | 1862 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので、ぜひ</src>` | 958 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 1344 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1559 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 2033 |
| 9 | `<src>えっと</src>` | `<src>えっと人数から</src>` | 572 |
| 10 | `<src><\|wait\|></src>` | `<src>いう</src>` | 2291 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>内訳がありますので、</src>` | 1779 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>ご承知お待ちください。</src>` | 1941 |

---

### Test Example 17 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1747 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到我</src>` | 1153 |
| 3 | `<src>回到我生活</src>` | `<src>生活的一个轨道，</src>` | 1922 |
| 4 | `<src>的一个轨道哈，</src>` | `<src><\|wait\|></src>` | 755 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1563 |
| 6 | `<src>在他下班的时候，</src>` | `<src>照他下单的时候，</src>` | 696 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1577 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>的时候，</src>` | 1986 |
| 9 | `<src><\|wait\|></src>` | `<src>就这么运作着。我当时</src>` | 1224 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>背对着</src>` | 2511 |
| 11 | `<src>小小的愿望</src>` | `<src>一个小小的工作</src>` | 1104 |
| 12 | `<src>哈。</src>` | `<src>的运作哈。</src>` | 1941 |

---

### Test Example 18 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1909 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 817 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1921 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 960 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 545 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 1668 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 734 |
| 8 | `<src>来诊断，</src>` | `<src>来侦断，</src>` | 1085 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 2099 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 1463 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 2370 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 980 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的离开。</src>` | 1979 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1777 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1201 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 2046 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 635 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1964 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 490 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1340 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 2150 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1342 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2497 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子</src>` | 1216 |
| 12 | `<src>连篇。</src>` | `<src>思绪连篇。</src>` | 1748 |

---

### Test Example 20 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2139 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 759 |
| 3 | `<src>ギアが</src>` | `<src>です。ギアが</src>` | 1125 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1864 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 795 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1411 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1563 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1154 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1187 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いているっていうこと</src>` | 1632 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 2207 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1233 |
| 13 | `<src>分解完了。</src>` | `<src>はい分解を。</src>` | 1743 |

---

### Test Example 21 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2265 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 824 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 2097 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 832 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1278 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 975 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 1577 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 2108 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 1598 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと全部</src>` | 2479 |
| 11 | `<src>傾向が強いので、</src>` | `<src>取っておる力が強いので、</src>` | 1455 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1377 |

---

### Test Example 22 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1829 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1513 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1566 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 776 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 2022 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1671 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1762 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 524 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 1761 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2254 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1408 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1563 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1940 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Telgu. </src>` | 1396 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 1686 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 697 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 1410 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 866 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1569 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 2093 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1322 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2967 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1424 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1482 |

---

### Test Example 24 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1858 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 810 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级以上</src>` | 1082 |
| 4 | `<src>服务</src>` | `<src><\|wait\|></src>` | 1830 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 991 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1418 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说</src>` | 1490 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1961 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信公众号十几年，你可以</src>` | 417 |
| 10 | `<src>发现</src>` | `<src><\|wait\|></src>` | 2313 |
| 11 | `<src>给微信公众号评分</src>` | `<src>把微信公众号平凡的</src>` | 1939 |
| 12 | `<src>的新榜反而</src>` | `<src>新榜反而</src>` | 1650 |
| 13 | `<src>火了。</src>` | `<src>活了。</src>` | 1691 |

---

### Test Example 25 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1803 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 836 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1066 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1962 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1404 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 895 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1492 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 2202 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 2290 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1956 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1732 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1776 |

---

### Test Example 26 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 2196 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 781 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1121 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1780 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 857 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1536 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1558 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1973 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 579 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 2658 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1364 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot sort array </src>` | 1723 |
| 13 | `<src><\|wait\|></src>` | `<src>is </src>` | 1634 |

---

### Test Example 27 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1830 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 750 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1089 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1914 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1020 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1208 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1640 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 2083 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1026 |
| 10 | `<src>は五経、</src>` | `<src>は五個、</src>` | 2654 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1024 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、</src>` | 1749 |
| 13 | `<src>です。</src>` | `<src>五ビです。</src>` | 1622 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2191 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1161 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 2173 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 622 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1892 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1604 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1282 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1024 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2312 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1898 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1277 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 1655 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1381 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2006 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1129 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1796 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 802 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1171 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1157 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1505 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 2157 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1978 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2246 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1384 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1638 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1340 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1848 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1785 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1884 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 679 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1706 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>놀라 줍니다. 굉장히 </src>` | 1589 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 1949 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다. </src>` | 456 |
| 9 | `<src>이렇게 </src>` | `<src>이도 굉장히 잘 </src>` | 2416 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>잘 존재 왜 </src>` | 1584 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1527 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1465 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1328 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1845 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 1138 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1901 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 695 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1527 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 616 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 1695 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 2046 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1000 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 2651 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1090 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼，</src>` | 2078 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1297 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思喽。</src>` | 1242 |

---

### Test Example 32 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2026 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1035 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1800 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 896 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1151 |
| 6 | `<src>你现在</src>` | `<src><\|wait\|></src>` | 1185 |
| 7 | `<src>所面临的一些</src>` | `<src>你现在所面临的一些</src>` | 1544 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，</src>` | 2147 |
| 9 | `<src>也不可能是</src>` | `<src>跟不幸</src>` | 1503 |
| 10 | `<src>一夕之间就</src>` | `<src>不可能是你一时之间就</src>` | 2610 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1310 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1533 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1399 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1178 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1945 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 878 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1008 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1804 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 976 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1423 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 1493 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 2007 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place </src>` | 554 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2519 |
| 11 | `<src>But </src>` | `<src>But </src>` | 1352 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1566 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1372 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1404 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1293 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1759 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1761 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1917 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1189 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1208 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1567 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2183 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 2566 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 1670 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업 들은 </src>` | 1598 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1412 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않을 </src>` | 1402 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1470 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1773 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1491 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 1455 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 820 |
| 5 | `<src>请你务必就要</src>` | `<src><\|wait\|></src>` | 1220 |
| 6 | `<src><\|wait\|></src>` | `<src>请你务必就要先守</src>` | 1092 |
| 7 | `<src>先守住，</src>` | `<src>走，</src>` | 1556 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 2194 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2299 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦，</src>` | 2058 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1808 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1662 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1158 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1101 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2171 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1113 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 1804 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 730 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 881 |
| 6 | `<src>that I think are </src>` | `<src>that is really </src>` | 1329 |
| 7 | `<src>really important. </src>` | `<src>important. </src>` | 1645 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1867 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 469 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 1735 |
| 11 | `<src>one minute videos </src>` | `<src>I have about one minute of videos </src>` | 2389 |
| 12 | `<src>that follow this video </src>` | `<src>about this video. </src>` | 1771 |
| 13 | `<src><\|wait\|></src>` | `<src>It'll cover each one, </src>` | 1879 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1187 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>and a little more detail, </src>` | 1287 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1975 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1232 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1812 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 933 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1807 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 473 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 1378 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 1985 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1121 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 2856 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1299 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1691 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1468 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1186 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1042 |

---

### Test Example 38 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2098 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 781 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1978 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 992 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 772 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1457 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아 </src>` | 1656 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1753 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 488 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1762 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 2094 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1155 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1750 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것 </src>` | 1300 |
| 15 | `<src>내려놓 고 </src>` | `<src>잘 넣어놓고. </src>` | 1363 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠어. </src>` | 1117 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2066 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 1072 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 882 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1779 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今基地を見ている。</src>` | 657 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1580 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1566 |
| 8 | `<src><\|wait\|></src>` | `<src>遠い超えている</src>` | 1536 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>船の基地を</src>` | 794 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1749 |
| 11 | `<src>長年</src>` | `<src><\|wait\|></src>` | 2274 |
| 12 | `<src>船大工をやってる</src>` | `<src>長年にわたる会宮を</src>` | 1432 |
| 13 | `<src>が、</src>` | `<src>やってる。</src>` | 1501 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 1401 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい海賊船を</src>` | 1395 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 1002 |

---

### Test Example 40 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1774 |
| 2 | `<src>HTML이라고 </src>` | `<src>而Hjemel</src>` | 1295 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1685 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>이라고 하는 컴퓨터 도 </src>` | 807 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1738 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 540 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1525 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>이해 할 수 있는 컴퓨터 언어 의 </src>` | 2165 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 2323 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1981 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1573 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1385 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1349 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1289 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1138 |

---

### Test Example 41 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>図</src>` | 1966 |
| 2 | `<src>十一二手とか</src>` | `<src>1、2、とか</src>` | 939 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 1009 |
| 4 | `<src>十秒で。</src>` | `<src>10秒で。</src>` | 1795 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 911 |
| 6 | `<src>一秒に</src>` | `<src>1秒に</src>` | 1413 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>1秒ぐらいの</src>` | 1643 |
| 8 | `<src>計算ですか</src>` | `<src>インターンスか</src>` | 2053 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 1032 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2429 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1047 |
| 12 | `<src><\|wait\|></src>` | `<src>1、2、</src>` | 1745 |
| 13 | `<src>十一二手で</src>` | `<src>2で</src>` | 1632 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1085 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮本とかが</src>` | 1274 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 934 |

---

### Test Example 42 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1996 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 992 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 2094 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 773 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 2004 |
| 6 | `<src>but the reality </src>` | `<src>But the </src>` | 454 |
| 7 | `<src>is is that </src>` | `<src>reality is that </src>` | 1346 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 2104 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 1555 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 2310 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1202 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1754 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1455 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1092 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything </src>` | 990 |
| 16 | `<src>held to a higher standard. </src>` | `<src>at this point is being held to </src>` | 1047 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2060 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1211 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1902 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 691 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 1634 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 628 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1608 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>That's one level of attainment. Did you go </src>` | 2247 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 1950 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2350 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1848 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1628 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1281 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 1291 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1040 |

---

### Test Example 44 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1842 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1592 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1719 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 628 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1898 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1740 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 2024 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src><\|wait\|></src>` | 797 |
| 9 | `<src><\|wait\|></src>` | `<src>끌려 갔느니라. </src>` | 2968 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1153 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1945 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1344 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1311 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1076 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1064 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2103 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1368 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 1789 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 672 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1998 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1244 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 588 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 2143 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 1782 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 2313 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1308 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1671 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1322 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1155 |
| 15 | `<src>はい。</src>` | `<src>はい、</src>` | 1042 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 963 |

---

### Test Example 46 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 간 것 </src>` | 2242 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1165 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>새모가 빌 거야, </src>` | 2057 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니의 때 서름이 </src>` | 802 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋은 자리 돋은 자식. </src>` | 2077 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오 며 </src>` | 1576 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 2025 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야, </src>` | 1279 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 오면 </src>` | 2676 |
| 10 | `<src>물릴 거고 </src>` | `<src>풀릴 거고 </src>` | 1307 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면요 </src>` | 1777 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1489 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주다 보니까 </src>` | 1392 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1148 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 간다. </src>` | 711 |

---

### Test Example 47 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 2193 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 1519 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1685 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 650 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 걸어 걸어다니 </src>` | 1979 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>공간 에 뭐 </src>` | 474 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 1400 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 2056 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 </src>` | 2156 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장렬이에요. </src>` | 2117 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 재밌 잖아요. </src>` | 1632 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1575 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1185 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>물올 바요. 그거 는 </src>` | 1355 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>다인 것 같아요. </src>` | 1141 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 585 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1745 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 1396 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 1827 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 760 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면, </src>` | 1893 |
| 6 | `<src>소니가 </src>` | `<src>Sony가 </src>` | 1552 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 433 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1907 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2376 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것을 봅 보인 다. </src>` | 2091 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1789 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1675 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1232 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1201 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 1266 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 240 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2075 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1399 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1697 |
| 4 | `<src>真实意图的，</src>` | `<src>真性意图的，</src>` | 899 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1873 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1622 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 1582 |
| 8 | `<src>会听到人们</src>` | `<src>靠经常会听到</src>` | 725 |
| 9 | `<src>这样说：“</src>` | `<src>人们这样说：“</src>` | 2273 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1929 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1277 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1629 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1387 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 1271 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1150 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 733 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 638 |

---

### Test Example 50 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1746 |
| 2 | `<src>首次觉知到</src>` | `<src>佛罗伊的所指</src>` | 1533 |
| 3 | `<src>那个现象：</src>` | `<src>解读到的那个现象，</src>` | 1831 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 522 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 1768 |
| 6 | `<src>处于爱之中，</src>` | `<src><\|wait\|></src>` | 408 |
| 7 | `<src>所谓的爱，</src>` | `<src>爱之中所谓的爱，</src>` | 1559 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 2003 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入</src>` | 682 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2546 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨，</src>` | 1235 |
| 12 | `<src>它是爱；</src>` | `<src>在早上的时候，他是一，</src>` | 1697 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1676 |
| 14 | `<src>它就变成恨。</src>` | `<src>他就变成恨，</src>` | 1226 |
| 15 | `<src><\|wait\|></src>` | `<src>那个</src>` | 1120 |
| 16 | `<src>那个钟摆</src>` | `<src><\|wait\|></src>` | 1014 |
| 17 | `<src><\|wait\|></src>` | `<src>钟摆</src>` | 680 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 648 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1947 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1123 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 2259 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 602 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1839 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1774 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2039 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 1098 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 2722 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1038 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 2056 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 1536 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1239 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 업을 </src>` | 1201 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 901 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 645 |

---

### Test Example 52 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계속 뭐 </src>` | 2146 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 </src>` | 1157 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 2265 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 553 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>비라는 사람 이 </src>` | 1894 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트예요. </src>` | 1773 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트가 </src>` | 2088 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>해가지고 </src>` | 1993 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2256 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1765 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 1781 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라는 사람 이 </src>` | 1129 |
| 13 | `<src>실제 </src>` | `<src>실제 크로스사이트로 </src>` | 1336 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>제어 사이트에서 </src>` | 989 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>예기스 파일 까지 </src>` | 570 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 645 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2270 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 861 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 1817 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 994 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 756 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1483 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1632 |
| 8 | `<src>versus variant </src>` | `<src>versus, </src>` | 1756 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 481 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 1251 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2899 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that, </src>` | 1322 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree </src>` | 1656 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 1331 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1275 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1050 |
| 17 | `<src>draw from, </src>` | `<src>draw from. </src>` | 851 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>There's nothing to draw from, right? </src>` | 677 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 461 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1991 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 792 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 2043 |
| 4 | `<src>move media objects </src>` | `<src><\|wait\|></src>` | 894 |
| 5 | `<src><\|wait\|></src>` | `<src>move media objects </src>` | 1198 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1148 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1582 |
| 8 | `<src>you get into </src>` | `<src>you get into the </src>` | 2005 |
| 9 | `<src>a situation </src>` | `<src>situation where you </src>` | 1026 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2739 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 988 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2098 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1449 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1308 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1081 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure </src>` | 1145 |
| 17 | `<src>get backed up </src>` | `<src>they get backed up </src>` | 657 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 489 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1808 |
| 2 | `<src>he knows Jesus </src>` | `<src><\|wait\|></src>` | 955 |
| 3 | `<src>is hungry. </src>` | `<src>he knows Jesus is hungry. </src>` | 2076 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 701 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 1523 |
| 6 | `<src><\|wait\|></src>` | `<src>in the wilderness, </src>` | 747 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>shortly decayed, </src>` | 1553 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 2104 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus," Hey, </src>` | 1213 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it." </src>` | 3106 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn these </src>` | 1740 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>stones to bread." </src>` | 1806 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1077 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>say to deal with </src>` | 1278 |
| 15 | `<src>temptation? </src>` | `<src>that temptation? </src>` | 989 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 579 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 652 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone." </src>` | 528 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1967 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1196 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1622 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 988 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1409 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 715 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 1571 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1364 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 874 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 1259 |
| 11 | `<src><\|wait\|></src>` | `<src>所以</src>` | 2317 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>呢，这身体的部分</src>` | 1073 |
| 13 | `<src>也会反映的是</src>` | `<src>都会反映的是，</src>` | 1908 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1492 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 1171 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 1174 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 913 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 523 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 655 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 407 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 293 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2246 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 877 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 955 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1848 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 719 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't know, </src>` | 1846 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>I don't think the courts want to be </src>` | 1459 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1932 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of social </src>` | 1120 |
| 10 | `<src>change </src>` | `<src>change </src>` | 2396 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 1087 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1798 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1675 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1220 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1201 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 1068 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 305 |
| 18 | `<src>So you have some </src>` | `<src>So you have </src>` | 647 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 475 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 335 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 144 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1805 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1003 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1684 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 992 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1085 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1275 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1575 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 2145 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1819 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2274 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1311 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1588 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1400 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations, </src>` | 1240 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1030 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to the </src>` | 1034 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 632 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 312 |
| 19 | `<src>play </src>` | `<src>play the devil's advocate, </src>` | 308 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and they, </src>` | 285 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy away </src>` | 333 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 236 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 285 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. </src>` | 295 |
| 25 | `<src>ENTP stands for </src>` | `<src>Standfor. </src>` | 274 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1899 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1451 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1832 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 621 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1910 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1571 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 445 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1892 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2061 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2151 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1655 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1759 |
| 13 | `<src><\|wait\|></src>` | `<src>드러내 놓고 윤석열 후보 </src>` | 1343 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>를 떨어뜨리 겠다는 </src>` | 1264 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 992 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 519 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 638 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 508 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 312 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 304 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건 </src>` | 301 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 272 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 285 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 298 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까. </src>` | 286 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>で、まあ</src>` | 2077 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 786 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってる</src>` | 1082 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいです。なので、ここのね</src>` | 1950 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴールドストーンホテル</src>` | 1617 |
| 6 | `<src>も</src>` | `<src>でも</src>` | 512 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1726 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 2067 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1278 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね、ここ</src>` | 2620 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴールドストーンホテルを</src>` | 1211 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1777 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なっていう方はですね、</src>` | 1481 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1165 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>も、まあいいんじゃないか</src>` | 1180 |
| 16 | `<src><\|wait\|></src>` | `<src>なと、はい、</src>` | 1032 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 621 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね、</src>` | 490 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 179 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 249 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかるか</src>` | 389 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんでかかんでかからないか、そんな</src>` | 248 |
| 23 | `<src>レベルのね</src>` | `<src>ですよね。</src>` | 217 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>リッチのね、まあホテル</src>` | 304 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので、</src>` | 277 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね、</src>` | 272 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 174 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 153 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね、今回は。</src>` | 158 |
