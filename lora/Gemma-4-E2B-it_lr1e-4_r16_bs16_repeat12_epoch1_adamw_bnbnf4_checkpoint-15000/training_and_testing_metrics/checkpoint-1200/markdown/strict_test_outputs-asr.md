# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9610
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3709
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
  - PROCESS_TIME_MS_AVG: 1461.3480
  - PROCESS_TIME_MS_P50: 1468.3510
  - PROCESS_TIME_MS_P95: 2499.3180
  - PROCESS_TIME_MS_MAX: 3080.7740

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
| 1 | `<src><\|wait\|></src>` | `<src>为什么</src>` | 1953 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>在宿舍里，</src>` | 872 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个犹豫</src>` | 729 |
| 4 | `<src>然后</src>` | `<src>很大。然后</src>` | 1634 |
| 5 | `<src><\|wait\|></src>` | `<src>呢，</src>` | 1243 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放假</src>` | 917 |
| 7 | `<src>儿核桃</src>` | `<src>下课后</src>` | 1653 |
| 8 | `<src><\|wait\|></src>` | `<src>人，</src>` | 1215 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉</src>` | 1807 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 1149 |
| 11 | `<src>仁儿。</src>` | `<src>和涛人。</src>` | 1673 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1546 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 860 |
| 3 | `<src>これなんかまだ</src>` | `<src>仲まだ</src>` | 1182 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1973 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1222 |
| 6 | `<src>こう短く</src>` | `<src>こう密告</src>` | 344 |
| 7 | `<src>剪定を</src>` | `<src>選定を</src>` | 1531 |
| 8 | `<src><\|wait\|></src>` | `<src>こう対訴して</src>` | 1951 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>あげると</src>` | 1108 |
| 10 | `<src>十年経っても</src>` | `<src>一年経っても</src>` | 1485 |
| 11 | `<src>大した。</src>` | `<src>対訴。</src>` | 2833 |

---

### Test Example 3 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1783 |
| 2 | `<src>옹심이, </src>` | `<src>봉심이 </src>` | 870 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1276 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼봉심이 </src>` | 1985 |
| 5 | `<src>옹심이가 </src>` | `<src>서울봉심이가 </src>` | 1214 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1615 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>석연하는 건데요. 야 </src>` | 742 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 2323 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 640 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>행으로도 조금 죽입니다. </src>` | 2237 |
| 11 | `<src>진짜. </src>` | `<src>진짜 </src>` | 1855 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1808 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气数是容易的，</src>` | 1045 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 2141 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有</src>` | 1245 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导到</src>` | 935 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1637 |
| 7 | `<src>处于中间，</src>` | `<src>如和处于中间，</src>` | 1409 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1643 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1219 |
| 10 | `<src>要成为</src>` | `<src>要成为一个</src>` | 2329 |
| 11 | `<src>一个师父。</src>` | `<src>师傅，</src>` | 1166 |

---

### Test Example 5 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなど</src>` | 1927 |
| 2 | `<src>あの</src>` | `<src>が</src>` | 818 |
| 3 | `<src>いただもらえる</src>` | `<src>あのいただろうといった</src>` | 985 |
| 4 | `<src>といったようなものも</src>` | `<src>ようなものも用意しております</src>` | 1707 |
| 5 | `<src>用意しておりますので</src>` | `<src>のでぜひ</src>` | 1129 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 814 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1548 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 1143 |
| 9 | `<src>えっと</src>` | `<src>てと</src>` | 1879 |
| 10 | `<src><\|wait\|></src>` | `<src>連絡の</src>` | 1162 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>マッチの案内がありますので</src>` | 2190 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>少々お待ちください。</src>` | 1408 |

---

### Test Example 6 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>面对这个情况，</src>` | 1739 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>我们就是</src>` | 810 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题，</src>` | 1270 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的</src>` | 1859 |
| 5 | `<src>或是通知对方，</src>` | `<src>汇报主管，或是通知对方</src>` | 1366 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我说</src>` | 1598 |
| 7 | `<src>不要想自己</src>` | `<src>这个状况，不要想自己</src>` | 1006 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来。</src>` | 2149 |
| 9 | `<src>独立承担。</src>` | `<src>扛不了，请你承担。</src>` | 1476 |
| 10 | `<src>整体而言，</src>` | `<src>这理论</src>` | 2652 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是一句</src>` | 702 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1589 |
| 2 | `<src>doing? </src>` | `<src>saying? </src>` | 826 |
| 3 | `<src>Drop into </src>` | `<src>Drop pin to your body. </src>` | 1374 |
| 4 | `<src>your body. </src>` | `<src>Where does it </src>` | 1879 |
| 5 | `<src>Where does the tension </src>` | `<src>attention start? </src>` | 1190 |
| 6 | `<src>start? What is it? </src>` | `<src>What is it? Is it a </src>` | 1651 |
| 7 | `<src>Is it a headache? </src>` | `<src>day? </src>` | 923 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it time in your chest? </src>` | 2254 |
| 9 | `<src>I ask them what </src>` | `<src>I have a </src>` | 1360 |
| 10 | `<src><\|wait\|></src>` | `<src>some language that you use </src>` | 2925 |
| 11 | `<src>language are you using? </src>` | `<src>say. </src>` | 567 |

---

### Test Example 8 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying </src>` | 1639 |
| 2 | `<src>Did very important research </src>` | `<src>important research </src>` | 846 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1231 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people? This is </src>` | 2381 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem. </src>` | 1026 |
| 6 | `<src>research, </src>` | `<src>Research looking at </src>` | 1584 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 1481 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1601 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1485 |
| 10 | `<src>out there, </src>` | `<src>out there. People that </src>` | 2869 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 549 |

---

### Test Example 9 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大体</src>` | 1841 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 867 |
| 3 | `<src>始めた</src>` | `<src>初めて</src>` | 1186 |
| 4 | `<src>もので、</src>` | `<src>ので</src>` | 1720 |
| 5 | `<src>ゴッホ、</src>` | `<src>ご法</src>` | 1119 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ご言やん</src>` | 693 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1564 |
| 8 | `<src>セザンヌ、</src>` | `<src>生産の</src>` | 2402 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナール</src>` | 724 |
| 10 | `<src>という人の絵</src>` | `<src>などという人の</src>` | 1729 |
| 11 | `<src>は、田舎の</src>` | `<src>絵が</src>` | 2538 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生でも</src>` | 1129 |

---

### Test Example 10 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1943 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>명단 에 있는 닉스들은 </src>` | 1055 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1187 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 2304 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 841 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 1643 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>닉스들이 </src>` | 1391 |
| 8 | `<src>때문 입니다. </src>` | `<src>있었기 때문 입니다. </src>` | 1853 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2125 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2202 |
| 11 | `<src>교사 들은. </src>` | `<src>모을 닫던 교사 들은 </src>` | 1294 |

---

### Test Example 11 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1852 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘撒完以后呢，</src>` | 1021 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的弹性</src>` | 2138 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了。</src>` | 1686 |
| 5 | `<src>然后</src>` | `<src>然后就</src>` | 619 |
| 6 | `<src>就停留在一个</src>` | `<src>停留在</src>` | 1563 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1482 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的运行状态。</src>` | 1746 |
| 9 | `<src>状态，</src>` | `<src><\|wait\|></src>` | 1793 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2416 |
| 11 | `<src>抑郁状态。</src>` | `<src>低于状态。</src>` | 1409 |

---

### Test Example 12 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1924 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要注意是</src>` | 986 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2064 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们生生那爱交</src>` | 1579 |
| 5 | `<src>爱浇水、</src>` | `<src><\|wait\|></src>` | 817 |
| 6 | `<src>施肥，</src>` | `<src>水，所以</src>` | 1564 |
| 7 | `<src>给足</src>` | `<src>可以</src>` | 1304 |
| 8 | `<src>孩子心理营养，</src>` | `<src>说孩子心里勇敢，</src>` | 1823 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1662 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>心耐心，</src>` | 2750 |
| 11 | `<src>慢慢长大。</src>` | `<src>等他慢慢长大。</src>` | 1335 |

---

### Test Example 13 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1578 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 852 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相不够的人之间，</src>` | 1052 |
| 4 | `<src><\|wait\|></src>` | `<src>有着某种</src>` | 1492 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>重要性。</src>` | 1297 |
| 6 | `<src>难道会是</src>` | `<src>难道</src>` | 703 |
| 7 | `<src><\|wait\|></src>` | `<src>会是</src>` | 1628 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从天夜里开始的</src>` | 1242 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1865 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1543 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思</src>` | 2829 |
| 12 | `<src>连篇。</src>` | `<src>学历连篇。</src>` | 1509 |

---

### Test Example 14 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1737 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 층을 </src>` | 939 |
| 3 | `<src>해가지고 내가 </src>` | `<src>죽여달라고 해가지고 내가 </src>` | 2478 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수도다. </src>` | 1893 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 층을 </src>` | 1157 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여달라고 해가지고 </src>` | 714 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>나는 내가 </src>` | 2784 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그런 소리 안 듣고 있는 </src>` | 552 |
| 9 | `<src><\|wait\|></src>` | `<src>줄은 아니야. </src>` | 2321 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>어? </src>` | 1917 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1237 |

---

### Test Example 15 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1648 |
| 2 | `<src>映画でですね、</src>` | `<src>AAがですね</src>` | 889 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1208 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>生食かどうか</src>` | 1931 |
| 5 | `<src>調べるときに、</src>` | `<src>っていう時に入り</src>` | 1322 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあAAの</src>` | 1287 |
| 7 | `<src>ことで、あの</src>` | `<src>Rankを調べたことで</src>` | 572 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>生食かどうか</src>` | 2797 |
| 9 | `<src>保証する、生息である</src>` | `<src>を</src>` | 961 |
| 10 | `<src>ことを保証する</src>` | `<src>生食であることを保証する</src>` | 1924 |
| 11 | `<src>といったような</src>` | `<src>といった使い方を</src>` | 1933 |
| 12 | `<src>使い方をされます。</src>` | `<src>されています。</src>` | 1421 |

---

### Test Example 16 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1671 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 766 |
| 3 | `<src><\|wait\|></src>` | `<src>天気が</src>` | 336 |
| 4 | `<src>テキという設備寺が</src>` | `<src>どうせ</src>` | 1190 |
| 5 | `<src>ありましたね。</src>` | `<src>準備がありましたね。</src>` | 1869 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1146 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 961 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井氏の仕組み</src>` | 954 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 2725 |
| 10 | `<src>は五経、</src>` | `<src>もうコン</src>` | 437 |
| 11 | `<src><\|wait\|></src>` | `<src>せつ準備</src>` | 2089 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 2279 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1701 |

---

### Test Example 17 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1657 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src><\|wait\|></src>` | 880 |
| 3 | `<src>촉발 시키고 </src>` | `<src>애플 슉빠르 시키 고 </src>` | 2764 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1247 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 634 |
| 6 | `<src><\|wait\|></src>` | `<src>모어 조깅 </src>` | 1612 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>헬레나 </src>` | 2158 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 987 |
| 9 | `<src>박한상과 </src>` | `<src>박카상과 </src>` | 2357 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 2162 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>있습니다. </src>` | 1744 |

---

### Test Example 18 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1941 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 932 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 2118 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learned to repeat by </src>` | 1369 |
| 5 | `<src>Find what you're good at </src>` | `<src>doing a good app. </src>` | 1024 |
| 6 | `<src>and do more of it. </src>` | `<src>And do more of it. </src>` | 1667 |
| 7 | `<src><\|wait\|></src>` | `<src>And well, you're not good </src>` | 2840 |
| 8 | `<src>And what you're not good at, </src>` | `<src>enough to get to people </src>` | 1086 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>around you to help you with </src>` | 2016 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1716 |
| 11 | `<src>And until next time. </src>` | `<src>and and tell the next time </src>` | 1875 |

---

### Test Example 19 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 이럴 땐 </src>` | 1824 |
| 2 | `<src><\|wait\|></src>` | `<src>너무 </src>` | 786 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>좋아야 될 수 있지만 </src>` | 2358 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1683 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 의 </src>` | 621 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 </src>` | 1672 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 하고 있고 </src>` | 2802 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 자기 보살 로 </src>` | 805 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 피라고 하고 있어요. </src>` | 2297 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 까지 다한테 보살 이라는 </src>` | 1863 |
| 11 | `<src>보살 이라는데. </src>` | `<src>데. </src>` | 2298 |

---

### Test Example 20 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>あとなんか</src>` | 2019 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が離れてくる</src>` | 1006 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>みたいな感じで</src>` | 1196 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>大将がね</src>` | 1974 |
| 5 | `<src>多いですね。</src>` | `<src>やっぱりですね</src>` | 1103 |
| 6 | `<src>開業したい方って</src>` | `<src>介護したい方って</src>` | 1678 |
| 7 | `<src>すごい</src>` | `<src>すぐに行こう意識が</src>` | 1278 |
| 8 | `<src>自己意識高いし、</src>` | `<src>高いし</src>` | 1797 |
| 9 | `<src>自分で</src>` | `<src>家で見てと多分</src>` | 1290 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>お年寄りを</src>` | 2853 |
| 11 | `<src>傾向が強いので、</src>` | `<src>介護することが強いので</src>` | 728 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 2329 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1747 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 866 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>毫无乱条，</src>` | 1412 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1616 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开道，</src>` | 1388 |
| 6 | `<src>期间</src>` | `<src>期限大概</src>` | 653 |
| 7 | `<src>大概有十位医生</src>` | `<src>有十二生</src>` | 1196 |
| 8 | `<src>来诊断，</src>` | `<src>来设定，</src>` | 2164 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 996 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 1708 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 2549 |
| 12 | `<src>他们</src>` | `<src>当然都很</src>` | 863 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>一会打开。</src>` | 2025 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 1914 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 852 |
| 3 | `<src>ギアが</src>` | `<src>ギアが緩むと</src>` | 1002 |
| 4 | `<src>緩むと芯が</src>` | `<src>信号が</src>` | 1481 |
| 5 | `<src><\|wait\|></src>` | `<src>逆にできなくなって</src>` | 1469 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 714 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1575 |
| 8 | `<src>役ねじの</src>` | `<src>逆ネジの</src>` | 1609 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1465 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついてるっていうこと</src>` | 1818 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 2486 |
| 12 | `<src>はい、</src>` | `<src>はい</src>` | 595 |
| 13 | `<src>分解完了。</src>` | `<src>文型完了を</src>` | 2428 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 1951 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 865 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1184 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1843 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1219 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 508 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1515 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2159 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 985 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 1810 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2516 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game.coord array </src>` | 1244 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1764 |

---

### Test Example 24 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个</src>` | 1678 |
| 2 | `<src><\|wait\|></src>` | `<src>就是传感器二</src>` | 739 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>个小时，</src>` | 351 |
| 4 | `<src>服务</src>` | `<src>还不足</src>` | 1191 |
| 5 | `<src>在一级一线</src>` | `<src>在一季一限</src>` | 1979 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1147 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1643 |
| 8 | `<src><\|wait\|></src>` | `<src>在做微性</src>` | 1273 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>运动好事期间，</src>` | 1851 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1696 |
| 11 | `<src>给微信公众号评分</src>` | `<src>微性运动好平分</src>` | 2782 |
| 12 | `<src>的新榜反而</src>` | `<src>的星膀，反而</src>` | 1445 |
| 13 | `<src>火了。</src>` | `<src>活了。</src>` | 1559 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1553 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到我</src>` | 868 |
| 3 | `<src>回到我生活</src>` | `<src>生活的一个</src>` | 1189 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，让我能够</src>` | 2180 |
| 5 | `<src>让我能够哈，</src>` | `<src>好好的</src>` | 1084 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在它下面的时候，</src>` | 1725 |
| 7 | `<src>在做热汤</src>` | `<src>在工作</src>` | 1403 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>当热浪来的时候，</src>` | 1833 |
| 9 | `<src><\|wait\|></src>` | `<src>我当时</src>` | 1902 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被它热浪</src>` | 2544 |
| 11 | `<src>小小的愿望</src>` | `<src>给我这么一个小小的一个诱惑哈，</src>` | 1530 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 2253 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1674 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 921 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 2120 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1369 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1021 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy gets </src>` | 1578 |
| 7 | `<src>gets converted to </src>` | `<src>converted to other </src>` | 1629 |
| 8 | `<src>other types of energy, </src>` | `<src>types of energy, like </src>` | 1664 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 2075 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets used </src>` | 2303 |
| 11 | `<src>or gets used to make </src>` | `<src>to make different bonds. </src>` | 1705 |
| 12 | `<src>different bonds. </src>` | `<src><\|wait\|></src>` | 2419 |

---

### Test Example 27 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1756 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chunah Teru. </src>` | 994 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 2179 |
| 4 | `<src><\|wait\|></src>` | `<src>in a UX/UI </src>` | 1693 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>background finance </src>` | 613 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a background in psychology. </src>` | 1659 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2618 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at YEN, </src>` | 564 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 1934 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 2492 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate </src>` | 1751 |
| 12 | `<src>corporate consultancy. </src>` | `<src>consultancy. </src>` | 2316 |

---

### Test Example 28 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 1869 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 789 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，不是</src>` | 849 |
| 4 | `<src>不是一天造成的，</src>` | `<src>以前造成的，</src>` | 1621 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1347 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 732 |
| 7 | `<src>所面临的一些</src>` | `<src>什么你的一些</src>` | 1606 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>遗迹啊，</src>` | 1104 |
| 9 | `<src>也不可能是</src>` | `<src>跟风景</src>` | 1940 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是</src>` | 1265 |
| 11 | `<src><\|wait\|></src>` | `<src>一致之间就演变出来。</src>` | 2800 |
| 12 | `<src>演变出来的，</src>` | `<src><\|wait\|></src>` | 824 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 2235 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>各位的朋友呢，</src>` | 1730 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 1944 |
| 2 | `<src>The meaning of </src>` | `<src><\|wait\|></src>` | 944 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 2461 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1461 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 683 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1523 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1731 |
| 8 | `<src>change can happen </src>` | `<src>happen in the </src>` | 1502 |
| 9 | `<src>in the United States. </src>` | `<src>United States. </src>` | 1993 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2302 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of the amendment </src>` | 1287 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of course I'm </src>` | 1737 |
| 13 | `<src>myriad. </src>` | `<src>Maryed. </src>` | 1411 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1628 |
| 2 | `<src>我们可以看到的是</src>` | `<src>这章的部分我们看到的是</src>` | 1011 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个</src>` | 1110 |
| 4 | `<src>的人，但是</src>` | `<src>带调的人，但是他是</src>` | 2223 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>属于逆向的。</src>` | 1036 |
| 6 | `<src>所以</src>` | `<src>这通常</src>` | 1614 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>好吗？这样</src>` | 1233 |
| 8 | `<src>时候，就要去</src>` | `<src>一个状况，需要去特别</src>` | 1920 |
| 9 | `<src>特别注意，</src>` | `<src>的注意是</src>` | 1785 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能</src>` | 2535 |
| 11 | `<src>钓到鱼，</src>` | `<src>得到</src>` | 1016 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与他</src>` | 1928 |
| 13 | `<src><\|wait\|></src>` | `<src>得到与意识</src>` | 1572 |
| 14 | `<src>的意思哦。</src>` | `<src>的。</src>` | 904 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 1712 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>이것 들은 </src>` | 900 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 유실 이 일어났 습니다. </src>` | 2870 |
| 4 | `<src>이제 거진 </src>` | `<src>이거는 거진 </src>` | 1449 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유산 한 징그러운 </src>` | 742 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>아름 징그러운 </src>` | 1185 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 2769 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연히 미네랄 이다. </src>` | 562 |
| 9 | `<src>이렇게 </src>` | `<src>이거는 </src>` | 2186 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>기강이 잘 좀 오해. </src>` | 2189 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2218 |
| 12 | `<src>그거 에다가 </src>` | `<src>그 후에다가 </src>` | 1754 |
| 13 | `<src>아연. </src>` | `<src>아니 죠. </src>` | 1112 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1577 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个天头，</src>` | 1006 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1255 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了天头之后，</src>` | 2084 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必</src>` | 1038 |
| 6 | `<src><\|wait\|></src>` | `<src>就要先</src>` | 1570 |
| 7 | `<src>先守住，</src>` | `<src>守住，</src>` | 864 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想着，哎，那我</src>` | 2289 |
| 9 | `<src><\|wait\|></src>` | `<src>再去操作</src>` | 1254 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦。</src>` | 2535 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 993 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么呢？</src>` | 1930 |
| 13 | `<src><\|wait\|></src>` | `<src>这么讲，因为呢，</src>` | 2157 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1003 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or or if you have </src>` | 1809 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 805 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1386 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1991 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1115 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1692 |
| 7 | `<src>to spell </src>` | `<src>how to spell the word </src>` | 1909 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>and it's like oh, </src>` | 1409 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2168 |
| 10 | `<src>spelled with a double </src>` | `<src>start with a double p? </src>` | 2249 |
| 11 | `<src><\|wait\|></src>` | `<src>Double p, </src>` | 1547 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double l, I don't know. </src>` | 2663 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1288 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1603 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개 가 </src>` | 988 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중화 벌써 1000만으로 </src>` | 2813 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1509 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1409 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 453 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 기업 들은 성장 하거나 </src>` | 2927 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 해외 에서 </src>` | 1383 |
| 9 | `<src>걷게 되는데 </src>` | `<src>이렇게 되는데 </src>` | 2731 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>해외 에서 </src>` | 717 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 2352 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않은 </src>` | 1716 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들도 보이 게 된 거죠. </src>` | 1563 |

---

### Test Example 35 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1776 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个财运可以说是</src>` | 954 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不好的，但是</src>` | 2184 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较赚钱的部分</src>` | 1359 |
| 5 | `<src>也就是</src>` | `<src>也就</src>` | 796 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的业绩</src>` | 1617 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>相对所大的</src>` | 924 |
| 8 | `<src>与收入的</src>` | `<src>红利，</src>` | 2141 |
| 9 | `<src>提升。如果是在</src>` | `<src>收入的提升。如果</src>` | 1262 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面</src>` | 2460 |
| 11 | `<src>这个月</src>` | `<src>这个月也是</src>` | 1061 |
| 12 | `<src>也是不错，只是</src>` | `<src>不错，只是</src>` | 1559 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对而言来说，</src>` | 2486 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就算</src>` | 972 |
| 15 | `<src><\|wait\|></src>` | `<src>入了那么一点。</src>` | 998 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1621 |
| 2 | `<src>HTML이라고 </src>` | `<src>어 </src>` | 841 |
| 3 | `<src><\|wait\|></src>` | `<src>HJL이라고 하는 </src>` | 1399 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴피터도 </src>` | 1969 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1147 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1574 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 586 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 어노 에 </src>` | 2568 |
| 9 | `<src>문법 에 </src>` | `<src>문법 의 </src>` | 1265 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>말 이렇게 우리 가 이제 </src>` | 2977 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>조도들을 작성 해야 </src>` | 611 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 2368 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그것 들을 </src>` | 1624 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1048 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1045 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 1733 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 889 |
| 3 | `<src><\|wait\|></src>` | `<src>there was such </src>` | 1374 |
| 4 | `<src>such interfaces before, </src>` | `<src>interest before. </src>` | 1870 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1200 |
| 6 | `<src>netfilter, TC. </src>` | `<src>Next future TC </src>` | 1649 |
| 7 | `<src>Yeah, so </src>` | `<src>here. </src>` | 992 |
| 8 | `<src>this is just </src>` | `<src>So this is just </src>` | 2130 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1255 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2636 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 951 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 2227 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1713 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on Bug Repos should be </src>` | 1199 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1036 |

---

### Test Example 38 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 1850 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 748 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 971 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1675 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1528 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨턴트예요. </src>` | 743 |
| 7 | `<src><\|wait\|></src>` | `<src>B가 컨설턴트 이 </src>` | 1539 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>어가지고 </src>` | 2738 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 432 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2286 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 2112 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1461 |
| 13 | `<src>실제 </src>` | `<src>실제 크로 사이트 </src>` | 1722 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>스크립트 에서 </src>` | 1150 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>XSP까지 </src>` | 1033 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까 </src>` | 1035 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 1885 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>濡らせてやる。</src>` | 952 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1191 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1856 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>引き知ってみる。</src>` | 1328 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1286 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 525 |
| 8 | `<src><\|wait\|></src>` | `<src>超えてる</src>` | 2283 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不れる奇跡。</src>` | 889 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1865 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 2420 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなデイクーを</src>` | 965 |
| 13 | `<src>が、</src>` | `<src>やってる。</src>` | 1908 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなに</src>` | 1548 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>すごい階族線を見た</src>` | 1121 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 1179 |

---

### Test Example 40 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who is </src>` | 1920 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 832 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1255 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1864 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I got ten of them </src>` | 1363 |
| 6 | `<src>that I think are </src>` | `<src>that are really important </src>` | 1670 |
| 7 | `<src>really important. </src>` | `<src><\|wait\|></src>` | 1266 |
| 8 | `<src><\|wait\|></src>` | `<src>um. </src>` | 1787 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go and do </src>` | 1555 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 2857 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 999 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video. </src>` | 2067 |
| 13 | `<src><\|wait\|></src>` | `<src>The coverage of each one </src>` | 1479 |
| 14 | `<src>that cover each one </src>` | `<src>and a little more </src>` | 1341 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>detail, but </src>` | 1116 |

---

### Test Example 41 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1841 |
| 2 | `<src>十一二手とか</src>` | `<src>十二手とか</src>` | 969 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>なやつが</src>` | 2072 |
| 4 | `<src>十秒で。</src>` | `<src>おそらく十秒で</src>` | 1274 |
| 5 | `<src>まあ</src>` | `<src><\|wait\|></src>` | 995 |
| 6 | `<src>一秒に</src>` | `<src>まあ一秒に</src>` | 1684 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1265 |
| 8 | `<src>計算ですか</src>` | `<src>時間ですかね。</src>` | 1830 |
| 9 | `<src>ね。</src>` | `<src>そうですね。</src>` | 1510 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2721 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 579 |
| 12 | `<src><\|wait\|></src>` | `<src>十二手</src>` | 2235 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1684 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 454 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1513 |
| 16 | `<src>あるから。</src>` | `<src>だから</src>` | 956 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1872 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. How far </src>` | 998 |
| 3 | `<src>How far did you </src>` | `<src>did you actually </src>` | 2049 |
| 4 | `<src><\|wait\|></src>` | `<src>go in your </src>` | 1155 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>education? Did you </src>` | 1119 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1688 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 1505 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. Did you </src>` | 1736 |
| 9 | `<src>to college, </src>` | `<src>go to college, and </src>` | 1911 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>so did you graduate? </src>` | 2523 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1487 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1472 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now. </src>` | 1449 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you </src>` | 1697 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1016 |

---

### Test Example 43 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>또 </src>` | 1606 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니 뭐여? </src>` | 1037 |
| 3 | `<src>이방인으로 </src>` | `<src>여기 가 이방인으로 </src>` | 2353 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1415 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하는 </src>` | 709 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1652 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 그대로 </src>` | 1915 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느라 </src>` | 1256 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1974 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그럼 으로 내가 </src>` | 2439 |
| 11 | `<src>너희 에게 </src>` | `<src>너희에게 </src>` | 1885 |
| 12 | `<src>알리 노니 </src>` | `<src>알리노니 </src>` | 2258 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1045 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 969 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 992 |

---

### Test Example 44 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 1985 |
| 2 | `<src><\|wait\|></src>` | `<src>세인바라 </src>` | 946 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 1304 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>이제 서름이 </src>` | 1976 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋은 차리 돋은 </src>` | 1249 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>이렇게 무야. </src>` | 1571 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1637 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1639 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 </src>` | 1987 |
| 10 | `<src>물릴 거고 </src>` | `<src>무미울 </src>` | 2409 |
| 11 | `<src>신이 오면 </src>` | `<src>거고 신이 </src>` | 1604 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>어떻게 쳐줄라고 </src>` | 2499 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>진짜 줘서 </src>` | 377 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>그러니까 편안 마음 에. </src>` | 1697 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 975 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね</src>` | 1865 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 969 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうやつで、</src>` | 2193 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルPython</src>` | 1466 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね。</src>` | 820 |
| 6 | `<src>というのもフローリフを</src>` | `<src>こういうのも</src>` | 1559 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフのビジュアルの書いてあと</src>` | 1654 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>とりあえずはPython</src>` | 1456 |
| 9 | `<src>にそこから</src>` | `<src>コードなんそっから生成される</src>` | 1768 |
| 10 | `<src>生成されて、それが</src>` | `<src>やつでそれが</src>` | 2645 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで信号処理</src>` | 1423 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われるっていう</src>` | 1625 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ことになるから</src>` | 1390 |
| 14 | `<src><\|wait\|></src>` | `<src>です。</src>` | 1097 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 927 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ</src>` | 980 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>드러가면 </src>` | 2001 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 해명 입니다. </src>` | 1004 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 2024 |
| 4 | `<src><\|wait\|></src>` | `<src>하고 온 거로 </src>` | 1270 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 다니 고 </src>` | 1027 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>그런데 뭐 </src>` | 1616 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북으로 가면 </src>` | 1175 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 1930 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가면 또 장려 리요. </src>` | 1979 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 2442 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1464 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1636 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1340 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>노발 요. 그거 는 </src>` | 1121 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>다인 것 같아요. </src>` | 967 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 967 |

---

### Test Example 47 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1936 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어차피 보면 </src>` | 998 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 2351 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1293 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>이 동생 이자 </src>` | 853 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 도 </src>` | 1588 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>가족 같은 동생 이잖아. </src>` | 2309 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 760 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 1344 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 한 못하 는 </src>` | 3081 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 1255 |
| 12 | `<src>자기 스스로 </src>` | `<src>조금 </src>` | 1657 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1464 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1008 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓고 </src>` | 1058 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1028 |

---

### Test Example 48 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1794 |
| 2 | `<src>Activity than </src>` | `<src>Activity. </src>` | 860 |
| 3 | `<src>self-defining what we think </src>` | `<src>Then self-defining what we think </src>` | 2485 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 1415 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct </src>` | 795 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1555 |
| 7 | `<src>is is that </src>` | `<src>is that </src>` | 2164 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new cat and </src>` | 1067 |
| 9 | `<src>block and because the </src>` | `<src>block, and because </src>` | 2359 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 2047 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from </src>` | 1455 |
| 12 | `<src>years ago, </src>` | `<src>20 years ago, </src>` | 1834 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1043 |
| 14 | `<src>a higher standard because </src>` | `<src>our standard </src>` | 1022 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 1360 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to our standard. </src>` | 628 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1563 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 952 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놓았습니다. </src>` | 2462 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 </src>` | 1453 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>의 분석 을 보시면 </src>` | 643 |
| 6 | `<src>소니가 </src>` | `<src>소니 가 </src>` | 1570 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 60에 </src>` | 1966 |
| 8 | `<src>파이프 를 </src>` | `<src>FP 파이프 를 </src>` | 1268 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2124 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 로포인 다. </src>` | 2356 |
| 11 | `<src><\|wait\|></src>` | `<src>엑스박스 시리즈 </src>` | 2066 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스에서도 없는 </src>` | 2016 |
| 13 | `<src><\|wait\|></src>` | `<src>인피니트 캐시 </src>` | 1111 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>CS가 </src>` | 943 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>여기도 없다. </src>` | 1066 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 616 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1847 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>锤模管</src>` | 948 |
| 3 | `<src>的感情或</src>` | `<src>只对所的感情</src>` | 2241 |
| 4 | `<src>真实意图的，</src>` | `<src>或真实意图的。</src>` | 1690 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 615 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1565 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常会</src>` | 1575 |
| 8 | `<src>会听到人们</src>` | `<src>听到人们这样说：</src>` | 1685 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 2213 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2212 |
| 11 | `<src>这个人</src>` | `<src>这个人又在</src>` | 1461 |
| 12 | `<src>又在说谎了，</src>` | `<src>躲黄了。</src>` | 1599 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛已经</src>` | 1256 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>说明了一切。</src>` | 1397 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1181 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 392 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 591 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>for all </src>` | 1584 |
| 2 | `<src>首次觉知到</src>` | `<src>the source </src>` | 847 |
| 3 | `<src>那个现象：</src>` | `<src>that can be </src>` | 1176 |
| 4 | `<src>每当我们</src>` | `<src>identified, </src>` | 1745 |
| 5 | `<src><\|wait\|></src>` | `<src>but we are </src>` | 1243 |
| 6 | `<src>处于爱之中，</src>` | `<src>in the middle of </src>` | 558 |
| 7 | `<src>所谓的爱，</src>` | `<src>love. </src>` | 1497 |
| 8 | `<src>我们也</src>` | `<src>We also </src>` | 1542 |
| 9 | `<src>同时进入恨。</src>` | `<src>enter the </src>` | 1525 |
| 10 | `<src><\|wait\|></src>` | `<src>heat </src>` | 1703 |
| 11 | `<src>在早上的时候，</src>` | `<src>in the middle of the </src>` | 2771 |
| 12 | `<src>它是爱；</src>` | `<src>love. </src>` | 1244 |
| 13 | `<src>到了晚上，</src>` | `<src>It's over. </src>` | 1781 |
| 14 | `<src>它就变成恨。</src>` | `<src>It becomes </src>` | 1339 |
| 15 | `<src><\|wait\|></src>` | `<src>heat. </src>` | 1121 |
| 16 | `<src>那个钟摆</src>` | `<src>That's the point. </src>` | 1050 |
| 17 | `<src><\|wait\|></src>` | `<src>It continues </src>` | 873 |
| 18 | `<src>继续在移动。</src>` | `<src>in a loop. </src>` | 629 |

---

### Test Example 52 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 절수가 </src>` | 1741 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 906 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 2410 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형 주도 </src>` | 1645 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 508 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>어 큰 폭의 상승 을 하겠지만 </src>` | 1655 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2618 |
| 8 | `<src>이 가벼운 </src>` | `<src>가변 온 정보 </src>` | 528 |
| 9 | `<src>종목 들이 </src>` | `<src>들이 </src>` | 1759 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2533 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 1025 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직 이 기 때문 에 </src>` | 1973 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 </src>` | 1426 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>요소 2초기 가변 온 정보 를 </src>` | 1871 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈으로 봐야 될 것 같습니다. </src>` | 1155 |
| 16 | `<src>같습니다. </src>` | `<src><\|wait\|></src>` | 683 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1832 |
| 2 | `<src>Also, </src>` | `<src>Also, you will not </src>` | 985 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 2174 |
| 4 | `<src>move media objects </src>` | `<src>media objects </src>` | 1044 |
| 5 | `<src><\|wait\|></src>` | `<src>between the </src>` | 1081 |
| 6 | `<src>between the resources. </src>` | `<src>resources. </src>` | 1037 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 777 |
| 8 | `<src>you get into </src>` | `<src>you get into the situation </src>` | 2777 |
| 9 | `<src>a situation </src>` | `<src>where you </src>` | 453 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2422 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 1965 |
| 12 | `<src>files to a particular resource, </src>` | `<src>file to a particular resource, </src>` | 1459 |
| 13 | `<src>you need to let us know, </src>` | `<src>we'll let us know. </src>` | 1601 |
| 14 | `<src>and we can see about </src>` | `<src>Now, and we can see about </src>` | 1294 |
| 15 | `<src><\|wait\|></src>` | `<src>giving those media files </src>` | 1636 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>and then making sure </src>` | 1089 |
| 17 | `<src>get backed up </src>` | `<src>they get backed up </src>` | 334 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 584 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2043 |
| 2 | `<src>in turmoil </src>` | `<src>in the wrong mile </src>` | 902 |
| 3 | `<src>in the first section </src>` | `<src>in the first section about </src>` | 2256 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1161 |
| 5 | `<src>about the EHR fields </src>` | `<src>the AHR field </src>` | 1019 |
| 6 | `<src><\|wait\|></src>` | `<src>being of critical importance </src>` | 1587 |
| 7 | `<src>being of critical importance </src>` | `<src>versus </src>` | 861 |
| 8 | `<src>versus variant </src>` | `<src><\|wait\|></src>` | 2209 |
| 9 | `<src><\|wait\|></src>` | `<src>variant data </src>` | 1174 |
| 10 | `<src>databases, </src>` | `<src>bases, which is obviously </src>` | 2417 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>not my loves. </src>` | 1180 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 1459 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree upon </src>` | 2293 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 519 |
| 15 | `<src>to be in these </src>` | `<src>to be in these data </src>` | 1031 |
| 16 | `<src>data sources that we can </src>` | `<src>sources that we can </src>` | 1185 |
| 17 | `<src>draw from, </src>` | `<src>draw from. There's nothing </src>` | 802 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 653 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 388 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2001 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful </src>` | 855 |
| 3 | `<src>right, </src>` | `<src>individual right, and </src>` | 1177 |
| 4 | `<src>and the Supreme Court </src>` | `<src>the Supreme Court </src>` | 1837 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 1396 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And I I don't know </src>` | 1334 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 576 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2783 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the vanguard of </src>` | 553 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2290 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 1958 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1439 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 1575 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1273 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1066 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged </src>` | 1134 |
| 17 | `<src><\|wait\|></src>` | `<src>so </src>` | 701 |
| 18 | `<src>So you have some </src>` | `<src>you have something </src>` | 191 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 584 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 395 |
| 21 | `<src>who. </src>` | `<src>who </src>` | 356 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1633 |
| 2 | `<src>he knows Jesus </src>` | `<src>and it warns Jesus </src>` | 954 |
| 3 | `<src>is hungry. </src>` | `<src>of a hungry </src>` | 2071 |
| 4 | `<src>He knows that </src>` | `<src>and warns that he's </src>` | 1468 |
| 5 | `<src>he's been without food, </src>` | `<src>not that for him </src>` | 919 |
| 6 | `<src><\|wait\|></src>` | `<src>to be in the wilderness </src>` | 1624 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>for forty days that he's hungry. </src>` | 2440 |
| 8 | `<src>And so he says </src>` | `<src>And so he says to </src>` | 774 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, say, if </src>` | 2229 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>you're the son of God, prove it. </src>` | 2384 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn these </src>` | 2234 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>stones to bread. </src>` | 1820 |
| 13 | `<src><\|wait\|></src>` | `<src>How did Jesus </src>` | 1496 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>deal with that? </src>` | 1340 |
| 15 | `<src>temptation? </src>` | `<src>That temptation. </src>` | 326 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 590 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead by bread. </src>` | 408 |
| 18 | `<src>by bread alone. </src>` | `<src>Alone. </src>` | 379 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1778 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 948 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1311 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片呢，我们可以看到</src>` | 2096 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是克汀，</src>` | 1119 |
| 6 | `<src>的部分。</src>` | `<src>的部分，</src>` | 1569 |
| 7 | `<src>那客厅一般</src>` | `<src>克汀一般</src>` | 1598 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1484 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 1338 |
| 10 | `<src>在休息的地方，</src>` | `<src>在修饰的地方。</src>` | 2877 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 598 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的</src>` | 2365 |
| 13 | `<src>也会反映的是</src>` | `<src>部分，它会反映的是</src>` | 1739 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给</src>` | 1530 |
| 15 | `<src>一点时间，</src>` | `<src>自己一点时间</src>` | 1194 |
| 16 | `<src>可以好好的</src>` | `<src>可以好的</src>` | 293 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>做一下</src>` | 593 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>休息，可以看到</src>` | 407 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>这边是双五一人的嘛。</src>` | 451 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 291 |
| 21 | `<src>所以是说。</src>` | `<src>所以说是说。</src>` | 349 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1649 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 918 |
| 3 | `<src>and they often </src>` | `<src>and they often show </src>` | 2251 |
| 4 | `<src>show up to </src>` | `<src>up to </src>` | 1161 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 996 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1612 |
| 7 | `<src><\|wait\|></src>` | `<src>The person </src>` | 864 |
| 8 | `<src>Their personality is </src>` | `<src>alive is something </src>` | 2182 |
| 9 | `<src>something of a </src>` | `<src>that have a contradiction. </src>` | 772 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2056 |
| 11 | `<src>While they're </src>` | `<src>Well, they're extroverted, </src>` | 2092 |
| 12 | `<src>extroverted, </src>` | `<src>they also </src>` | 2084 |
| 13 | `<src>they also hate </src>` | `<src>hate meaningless </src>` | 1835 |
| 14 | `<src>meaningless conversations </src>` | `<src>conversations. </src>` | 523 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1453 |
| 16 | `<src><\|wait\|></src>` | `<src>And like it straight to the </src>` | 1068 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 251 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 600 |
| 19 | `<src>play </src>` | `<src>to play the devil's advocate, </src>` | 424 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and they're </src>` | 363 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy about </src>` | 298 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>a debate. </src>` | 338 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 257 |
| 24 | `<src><\|wait\|></src>` | `<src>E.P. Stansfield </src>` | 326 |
| 25 | `<src>ENTP stands for </src>` | `<src>or. </src>` | 304 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 의 이준석은 </src>` | 1714 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>정무 를 거부 한 </src>` | 1001 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 2242 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 하면서 </src>` | 1354 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선을 </src>` | 861 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1624 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2269 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 887 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2024 |
| 10 | `<src>김종인 을 </src>` | `<src>김정은을 재건 </src>` | 2443 |
| 11 | `<src>제거 한 순간 </src>` | `<src>순간 이준석은 </src>` | 1899 |
| 12 | `<src>이준석은 </src>` | `<src>두려 내놓고 </src>` | 2225 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 가 </src>` | 1097 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1053 |
| 15 | `<src><\|wait\|></src>` | `<src>독기 를 품은 </src>` | 1011 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 616 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 443 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 386 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 315 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 321 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석 성상 납권 </src>` | 315 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 270 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당이 </src>` | 329 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 에 얼마나 </src>` | 275 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재 입니까? </src>` | 255 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1831 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今作って</src>` | 902 |
| 3 | `<src>今作ってる</src>` | `<src>みたいです。</src>` | 1196 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>なので</src>` | 1755 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ここのねゴルフスローンホテル</src>` | 1515 |
| 6 | `<src>も</src>` | `<src>も朝食が</src>` | 1620 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 864 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 2164 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1201 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 1646 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルフスローンホテル</src>` | 1972 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1453 |
| 13 | `<src>なっていう方はですね</src>` | `<src>な方ですね。</src>` | 2237 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさって</src>` | 566 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てみるとまあいいんじゃない</src>` | 1395 |
| 16 | `<src><\|wait\|></src>` | `<src>なと</src>` | 1039 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 517 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここホテルからですね</src>` | 598 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 404 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 190 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかるか</src>` | 333 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんないかそんなレベル</src>` | 313 |
| 23 | `<src>レベルのね</src>` | `<src>でのね立地の</src>` | 337 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>いいねまあホテル</src>` | 265 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 280 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 300 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>検討なさってみて</src>` | 271 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 238 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は</src>` | 148 |
