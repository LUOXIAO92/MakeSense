# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9443
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.6755
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
  - PROCESS_TIME_MS_AVG: 1635.8090
  - PROCESS_TIME_MS_P50: 1585.1780
  - PROCESS_TIME_MS_P95: 2830.8650
  - PROCESS_TIME_MS_MAX: 4067.8950

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
| 1 | `<src>最初から</src>` | `<src><\|wait\|></src>` | 1785 |
| 2 | `<src>あの特に</src>` | `<src>最初からあの特に</src>` | 1056 |
| 3 | `<src>これなんかまだ</src>` | `<src>中まだ</src>` | 1353 |
| 4 | `<src>一年生ですからね。</src>` | `<src>1年生からねうんうん</src>` | 1348 |
| 5 | `<src>この時点で</src>` | `<src>その時点で</src>` | 1528 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1363 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1268 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2216 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 1347 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 2767 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1165 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2047 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1318 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1243 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 1157 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1031 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1796 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 923 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2264 |
| 9 | `<src>虚阿凡</src>` | `<src>虚爻凡</src>` | 646 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2522 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 2551 |

---

### Test Example 3 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2148 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1218 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1613 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1121 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1538 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1140 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 1490 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 2028 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1332 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2896 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1106 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2334 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>放在声音的一边，</src>` | 1068 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个音量也很大。</src>` | 1442 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 999 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 638 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点，</src>` | 2471 |
| 7 | `<src>儿核桃</src>` | `<src>和陶</src>` | 1224 |
| 8 | `<src><\|wait\|></src>` | `<src>人，</src>` | 2261 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉吧，</src>` | 1298 |
| 10 | `<src>这种核桃</src>` | `<src><\|wait\|></src>` | 2371 |
| 11 | `<src>仁儿。</src>` | `<src>这种和陶人。</src>` | 1740 |

---

### Test Example 5 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아, </src>` | 2043 |
| 2 | `<src>옹심이, </src>` | `<src>저는 용심히 </src>` | 1037 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1221 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심히 </src>` | 1245 |
| 5 | `<src>옹심이가 </src>` | `<src>쇠술 용심히가 </src>` | 702 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2405 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. </src>` | 1206 |
| 8 | `<src>야, </src>` | `<src>야, </src>` | 2318 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 477 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해킹으로 </src>` | 2497 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 맞는 </src>` | 2503 |

---

### Test Example 6 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1912 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 1267 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 1630 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 909 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1749 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 1190 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>배르나 </src>` | 2170 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1397 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1937 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들은 </src>` | 3202 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>있다. </src>` | 2284 |

---

### Test Example 7 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1701 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1031 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 902 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1006 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 987 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 2655 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 501 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃，</src>` | 2922 |
| 9 | `<src><\|wait\|></src>` | `<src>就这么了。</src>` | 363 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，就吃一碗米粥，</src>` | 2296 |
| 11 | `<src>小小的愿望</src>` | `<src>一个小小的小愿望</src>` | 2857 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 2515 |

---

### Test Example 8 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2206 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1054 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1377 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1334 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1619 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1374 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1530 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 2120 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2691 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2390 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 2526 |

---

### Test Example 9 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1905 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1055 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1589 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1203 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 2730 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 1159 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 2447 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1330 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 3259 |
| 10 | `<src>out there, </src>` | `<src>out there, people with </src>` | 884 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 2336 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1980 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1213 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1283 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就可以解决的反馈主管。</src>` | 1218 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1539 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 1388 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1974 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1687 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 2052 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 3033 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运是属凶。</src>` | 2688 |

---

### Test Example 11 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1806 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 966 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1161 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1241 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 723 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 2479 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1873 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1882 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them </src>` | 2508 |
| 10 | `<src><\|wait\|></src>` | `<src>what language are you </src>` | 2589 |
| 11 | `<src>language are you using? </src>` | `<src>using? </src>` | 2640 |

---

### Test Example 12 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2217 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1078 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1564 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1122 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1596 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1296 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 2229 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 1425 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1977 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 3152 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 2696 |

---

### Test Example 13 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1994 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 1028 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1260 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1169 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 578 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 2386 |
| 7 | `<src>大概有十位医生</src>` | `<src>大家又涌入，</src>` | 351 |
| 8 | `<src>来诊断，</src>` | `<src>男生来剪断</src>` | 1358 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿，</src>` | 2084 |
| 10 | `<src>一下提腿，</src>` | `<src>一旦踢腿，</src>` | 1329 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 2604 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 1462 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的离开。</src>` | 2585 |

---

### Test Example 14 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2307 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1026 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1466 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1233 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1600 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1356 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 2441 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1154 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2468 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모르 았 던 </src>` | 2811 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 2571 |

---

### Test Example 15 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2360 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 946 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1253 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 1362 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 748 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 2233 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 1028 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 2496 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 871 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと全部</src>` | 2432 |
| 11 | `<src>傾向が強いので、</src>` | `<src>となんと仕事力が強いので、</src>` | 2228 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 2514 |

---

### Test Example 16 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 2178 |
| 2 | `<src>あの</src>` | `<src>などがあの</src>` | 1039 |
| 3 | `<src>いただもらえる</src>` | `<src>いただく</src>` | 1000 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも用意しております</src>` | 1255 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので、ぜひ</src>` | 619 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ごさなおください。</src>` | 2635 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 451 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 2862 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 473 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1652 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 3640 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 2625 |

---

### Test Example 17 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1987 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel. </src>` | 1062 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 1599 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1088 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a BSc in Finance </src>` | 1561 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a BSc in Psychology. </src>` | 1398 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2008 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the ANU, </src>` | 1684 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2668 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2568 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2096 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 508 |

---

### Test Example 18 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1984 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 </src>` | 1106 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 1786 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주기 일보도르와 수도 다 </src>` | 1286 |
| 5 | `<src>다른 잔찜에 </src>` | `<src><\|wait\|></src>` | 2413 |
| 6 | `<src>죽여 달라 </src>` | `<src>다른 잔찜이 주겨 달라 </src>` | 2320 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았냐? 내가 </src>` | 1498 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 2665 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐? </src>` | 2612 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 2333 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 468 |

---

### Test Example 19 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1874 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 1065 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1645 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1336 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 2535 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1225 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 2372 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1257 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 2745 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1441 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 2450 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 933 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1906 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1221 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1288 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy. And when those </src>` | 1273 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 2579 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 327 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted </src>` | 1686 |
| 8 | `<src>other types of energy, </src>` | `<src>to other types of energy, like </src>` | 1946 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 2346 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2831 |
| 11 | `<src>or gets used to make </src>` | `<src>Or gets used </src>` | 2512 |
| 12 | `<src>different bonds. </src>` | `<src>to make different bonds. </src>` | 1344 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1899 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 959 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 507 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキオーセツビ寺が</src>` | 1970 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたが、</src>` | 600 |
| 6 | `<src>で、</src>` | `<src>ええ。</src>` | 2412 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 313 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義の仕組み</src>` | 2327 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1257 |
| 10 | `<src>は五経、</src>` | `<src>は五本、</src>` | 1674 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3660 |
| 12 | `<src>設備寺、五比</src>` | `<src>セツビ寺五本</src>` | 2656 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1715 |

---

### Test Example 22 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2117 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1047 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 1398 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1129 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 673 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 2396 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1962 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1744 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1949 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の絵</src>` | 3234 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 2768 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1750 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2298 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1057 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1349 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1188 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 695 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 2324 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2809 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 801 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1491 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 3265 |
| 11 | `<src><\|wait\|></src>` | `<src>So this </src>` | 690 |
| 12 | `<src>this game dot scored array. </src>` | `<src>game.court array. </src>` | 2574 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1779 |

---

### Test Example 24 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 2055 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 저 </src>` | 1016 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>할 만할 수 있지만 </src>` | 1846 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1097 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기가 </src>` | 2536 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요 </src>` | 930 |
| 7 | `<src>뭐 있고 </src>` | `<src>인들 꿈일 필요 가 보이 고 </src>` | 2685 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 저 보살 로 </src>` | 1384 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 필요 가 보이 서 우주 가 </src>` | 4068 |
| 10 | `<src>지금 나한테 </src>` | `<src>이제 나한테 </src>` | 2575 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는데. </src>` | 1890 |

---

### Test Example 25 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果在女高中</src>` | 1825 |
| 2 | `<src>如果在女高中生</src>` | `<src><\|wait\|></src>` | 1045 |
| 3 | `<src>与长相古怪的人</src>` | `<src>生与长相古怪的人</src>` | 2109 |
| 4 | `<src><\|wait\|></src>` | `<src>之间，</src>` | 674 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>有着某种联系。</src>` | 1586 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1284 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1647 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1978 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1762 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3484 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子</src>` | 2657 |
| 12 | `<src>连篇。</src>` | `<src>思绪连篇。</src>` | 1835 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src><\|wait\|></src>` | 1979 |
| 2 | `<src><\|wait\|></src>` | `<src>第二个就是能源</src>` | 1037 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>机制场，</src>` | 1210 |
| 4 | `<src>服务</src>` | `<src><\|wait\|></src>` | 1275 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 789 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 2297 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1973 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1639 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做维向攻总号</src>` | 1725 |
| 10 | `<src>发现</src>` | `<src>十几年你会发现，</src>` | 3640 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维向攻平分的</src>` | 2606 |
| 12 | `<src>的新榜反而</src>` | `<src><\|wait\|></src>` | 1758 |
| 13 | `<src>火了。</src>` | `<src>新棒反而活了。</src>` | 1295 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2071 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 990 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1600 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1151 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1735 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1212 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1750 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1867 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2425 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2732 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2675 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1871 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1789 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2240 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1030 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 2118 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 742 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 2635 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1060 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2528 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 503 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2977 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1921 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 2641 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, </src>` | 1874 |
| 13 | `<src>myriad. </src>` | `<src>I'm—Maryed. </src>` | 2223 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1946 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 1376 |
| 3 | `<src>인슐린과 </src>` | `<src>과진 이인출 이런 거 </src>` | 1851 |
| 4 | `<src>이제 거진 </src>` | `<src><\|wait\|></src>` | 624 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>이게 과진 유사 찬 자긍 진을 </src>` | 2767 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>보통 ุก굉장히 </src>` | 1884 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 1671 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연 업 미네랄이다. </src>` | 1558 |
| 9 | `<src>이렇게 </src>` | `<src>이거 굉장히 잘 </src>` | 3846 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>잘 찾죠. </src>` | 2432 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>그렇 죠? </src>` | 1568 |
| 12 | `<src>그거 에다가 </src>` | `<src>이제 구애다가 </src>` | 447 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 2306 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2163 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 950 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 1408 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1211 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 749 |
| 6 | `<src>你现在</src>` | `<src><\|wait\|></src>` | 2217 |
| 7 | `<src>所面临的一些</src>` | `<src>你现在所面临的一些</src>` | 1272 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，</src>` | 2269 |
| 9 | `<src>也不可能是</src>` | `<src>跟不幸</src>` | 1021 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你一时之间就</src>` | 2649 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1742 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 2711 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1777 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 2371 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1802 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1232 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 1159 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1292 |
| 5 | `<src>请你务必就要</src>` | `<src><\|wait\|></src>` | 896 |
| 6 | `<src><\|wait\|></src>` | `<src>请你务必就要先守住</src>` | 2053 |
| 7 | `<src>先守住，</src>` | `<src>走，</src>` | 1484 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 2203 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1737 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 3415 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2639 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1709 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1009 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1561 |

---

### Test Example 32 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2090 |
| 2 | `<src>十一二手とか</src>` | `<src>十一・二日とか</src>` | 1064 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 1207 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1269 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 640 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 2415 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1328 |
| 8 | `<src>計算ですか</src>` | `<src>してたんですかね。</src>` | 2222 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 1185 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2103 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1989 |
| 12 | `<src><\|wait\|></src>` | `<src>十一・二</src>` | 585 |
| 13 | `<src>十一二手で</src>` | `<src>日で</src>` | 2222 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1603 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1123 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 1466 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1910 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 986 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1724 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1016 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1750 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1118 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 2005 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1619 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1565 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 3620 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 2715 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 1859 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1703 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 769 |

---

### Test Example 34 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1834 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 1021 |
| 3 | `<src><\|wait\|></src>` | `<src>어 HTML이라고 하는 </src>` | 1509 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 이해 할 수 </src>` | 1271 |
| 5 | `<src><\|wait\|></src>` | `<src>있고 </src>` | 1554 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 이해 할 수 </src>` | 1342 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1393 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 2116 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1397 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 3576 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 530 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 2456 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1719 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 </src>` | 1231 |
| 15 | `<src>필요 합니다. </src>` | `<src>프로그램 이 필요 합니다. </src>` | 1421 |

---

### Test Example 35 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2230 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 987 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1614 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1100 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1649 |
| 6 | `<src>that I think are </src>` | `<src>that you really </src>` | 1272 |
| 7 | `<src>really important. </src>` | `<src>important. </src>` | 1428 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2090 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 1452 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 3152 |
| 11 | `<src>one minute videos </src>` | `<src>I have about one minute of videos </src>` | 885 |
| 12 | `<src>that follow this video </src>` | `<src>at the end of this video. </src>` | 2483 |
| 13 | `<src><\|wait\|></src>` | `<src>It'll cover each one, </src>` | 1844 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1619 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>and a little more detail, </src>` | 940 |

---

### Test Example 36 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1847 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1369 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>2명 미만 으로 </src>` | 1603 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 998 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 2586 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1734 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2017 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 3077 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 2122 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 2700 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1761 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 </src>` | 2358 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 522 |

---

### Test Example 37 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2237 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 1045 |
| 3 | `<src>ギアが</src>` | `<src>です。ギアが</src>` | 1756 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1110 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 2714 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 2429 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1271 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 2426 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 2894 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうこと</src>` | 2591 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 1761 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 2405 |
| 13 | `<src>分解完了。</src>` | `<src>はい分解を。</src>` | 595 |

---

### Test Example 38 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2137 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 1094 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1174 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1262 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今非力を見ている。</src>` | 698 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2405 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1109 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2430 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えている船乗る奇跡よ。</src>` | 1365 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2485 |
| 11 | `<src>長年</src>` | `<src><\|wait\|></src>` | 1547 |
| 12 | `<src>船大工をやってる</src>` | `<src>長年にわたり</src>` | 2725 |
| 13 | `<src>が、</src>` | `<src>こうやってるが、</src>` | 1808 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 1468 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい海賊船を見た</src>` | 1059 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 1519 |

---

### Test Example 39 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 2266 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어 멋지 보면 </src>` | 1068 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1923 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 848 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 2744 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1251 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 2352 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1387 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3189 |
| 10 | `<src>책임감 보다는 </src>` | `<src>적인 거라 는 </src>` | 875 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 2364 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 1190 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 781 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 거 </src>` | 1376 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1169 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>응모 했습니다, </src>` | 1544 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1870 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1263 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1514 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1034 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1727 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1166 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 2597 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 </src>` | 985 |
| 9 | `<src><\|wait\|></src>` | `<src>갔느니라. </src>` | 1834 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 3299 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 2712 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1679 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1241 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1448 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1644 |

---

### Test Example 41 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1998 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 1045 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1491 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1226 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1528 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1378 |
| 7 | `<src>Yeah, so </src>` | `<src><\|wait\|></src>` | 1999 |
| 8 | `<src>this is just </src>` | `<src>Yeah, so this is just </src>` | 1728 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 2216 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2885 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 2716 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 1766 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1409 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1158 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1629 |

---

### Test Example 42 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2174 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1041 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて、</src>` | 1681 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1023 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 2727 |
| 6 | `<src>というのもフローリフを</src>` | `<src>そういうのも</src>` | 1001 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルの書いてあと</src>` | 2617 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあとうぜ</src>` | 1345 |
| 9 | `<src>にそこから</src>` | `<src>はPythonコードが</src>` | 2769 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成されて、それが</src>` | 1390 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 2482 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が</src>` | 1661 |
| 13 | `<src>構造になっているからです。</src>` | `<src>可能になっているからです。</src>` | 555 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2045 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 894 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 926 |

---

### Test Example 43 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1804 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 1233 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 1751 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 974 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 2595 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1310 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 2278 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1344 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 3658 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 </src>` | 529 |
| 11 | `<src><\|wait\|></src>` | `<src>보인다. </src>` | 2535 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1659 |
| 13 | `<src><\|wait\|></src>` | `<src>인피니트 캐시 </src>` | 1227 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>CS </src>` | 1304 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>가 여기 도 없다. </src>` | 1217 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 576 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 2314 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 1014 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맨다, </src>` | 1969 |
| 4 | `<src><\|wait\|></src>` | `<src>운전 을 할 건 </src>` | 965 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 2529 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>거로 거르 다 이용 안 가네. </src>` | 764 |
| 7 | `<src>강북 을 가면 </src>` | `<src><\|wait\|></src>` | 2543 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>뭐 강북 으로 가면 말할 것도 없고 </src>` | 574 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 </src>` | 1899 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>또 장렬이야. </src>` | 3237 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 객관 적으로 </src>` | 2656 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1707 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1061 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모바일, 그거 는 </src>` | 1507 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>안 좋은 것 같아요. </src>` | 1334 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 471 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2163 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1043 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1714 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1005 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 2819 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 2698 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 1086 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. Did you go </src>` | 2552 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 2638 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2714 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1728 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1503 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1032 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1469 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 250 |

---

### Test Example 46 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2044 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1192 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1612 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src><\|wait\|></src>` | 934 |
| 5 | `<src>也就是</src>` | `<src>比较偏正财的部分。也就是说，</src>` | 2799 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 2974 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的</src>` | 766 |
| 8 | `<src>与收入的</src>` | `<src>红利与收入的</src>` | 2269 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果</src>` | 2844 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面呢，</src>` | 2764 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1588 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 900 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1710 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1374 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 479 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계속 뭐 </src>` | 2162 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 </src>` | 1015 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 1257 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1349 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 771 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨턴트예요. </src>` | 2262 |
| 7 | `<src><\|wait\|></src>` | `<src>여기 컨설턴트가 </src>` | 2531 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>오고 A라는 </src>` | 1189 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1906 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 3292 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 2475 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람 이 </src>` | 1760 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 414 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스킷에서 </src>` | 2224 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 1057 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 818 |

---

### Test Example 48 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 간 것, </src>` | 2358 |
| 2 | `<src><\|wait\|></src>` | `<src>지금 와라 </src>` | 1021 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야, </src>` | 1585 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>이제 서름이 돋든 </src>` | 1321 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>가시 리 돋든 </src>` | 2637 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 </src>` | 1720 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>엄이야. 이걸 흔들 어서 </src>` | 1994 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 2196 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 2949 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 2560 |
| 11 | `<src>신이 오면 </src>` | `<src>새니 오면 </src>` | 1760 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1029 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거 아니 까. </src>` | 1621 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1361 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 간다. </src>` | 493 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2079 |
| 2 | `<src>Activity than </src>` | `<src>Activity. </src>` | 995 |
| 3 | `<src>self-defining what we think </src>` | `<src>Then self-defining, </src>` | 1861 |
| 4 | `<src>the standard is because you're </src>` | `<src>what we think the standard is, </src>` | 1128 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 2635 |
| 6 | `<src>but the reality </src>` | `<src>But </src>` | 2014 |
| 7 | `<src>is is that </src>` | `<src>the reality is that </src>` | 1633 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 3676 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 1463 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 2551 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 335 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1667 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1389 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1112 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything </src>` | 1330 |
| 16 | `<src>held to a higher standard. </src>` | `<src>at this point is being held to </src>` | 488 |

---

### Test Example 50 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 2021 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 998 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 2075 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 869 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 2559 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1172 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2366 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 1212 |
| 9 | `<src>종목 들이 </src>` | `<src>가벼운 종목 들이 </src>` | 2791 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1486 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 2577 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 </src>` | 1874 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 뉴시총이 </src>` | 2087 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 425 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 1637 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 764 |

---

### Test Example 51 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2129 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1093 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1554 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1123 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1599 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1301 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 1436 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们</src>` | 2073 |
| 9 | `<src>这样说：“</src>` | `<src>这样说：“</src>` | 1426 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 3377 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 507 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 2781 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1763 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 2349 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1261 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 561 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 810 |

---

### Test Example 52 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2393 |
| 2 | `<src>in turmoil </src>` | `<src>in Europa mile </src>` | 976 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1230 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1281 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR field </src>` | 648 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2393 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1203 |
| 8 | `<src>versus variant </src>` | `<src>versus the. </src>` | 2331 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 522 |
| 10 | `<src>databases, </src>` | `<src>Variant databases, </src>` | 2595 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2408 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that </src>` | 2085 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree </src>` | 550 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1627 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these data </src>` | 1300 |
| 16 | `<src>data sources that we can </src>` | `<src>sources that we can </src>` | 1312 |
| 17 | `<src>draw from, </src>` | `<src>draw from. </src>` | 1641 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>There's nothing to draw from. </src>` | 868 |
| 19 | `<src><\|wait\|></src>` | `<src>Right. </src>` | 570 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1819 |
| 2 | `<src>首次觉知到</src>` | `<src>Fuloo一档的手机</src>` | 1245 |
| 3 | `<src>那个现象：</src>` | `<src>觉知到了那个现象。</src>` | 1629 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 916 |
| 5 | `<src><\|wait\|></src>` | `<src>美登我们</src>` | 1584 |
| 6 | `<src>处于爱之中，</src>` | `<src>处于爱室内，</src>` | 1306 |
| 7 | `<src>所谓的爱，</src>` | `<src>属位的爱，</src>` | 2891 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 745 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入</src>` | 2360 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2837 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨在早上的时候，</src>` | 2742 |
| 12 | `<src>它是爱；</src>` | `<src>它在爱。</src>` | 1732 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1257 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成</src>` | 1231 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1306 |
| 16 | `<src>那个钟摆</src>` | `<src>恨，那个钟摆。</src>` | 510 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在运动。</src>` | 738 |
| 18 | `<src>继续在移动。</src>` | `<src><\|wait\|></src>` | 586 |

---

### Test Example 54 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2324 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1028 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1169 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1342 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 678 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 2405 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1645 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1944 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of social </src>` | 1464 |
| 10 | `<src>change </src>` | `<src>change </src>` | 2948 |
| 11 | `<src>these days, </src>` | `<src>these days. </src>` | 824 |
| 12 | `<src><\|wait\|></src>` | `<src>But they're </src>` | 2278 |
| 13 | `<src>but they rather reflect </src>` | `<src>rather reflect </src>` | 469 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1645 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 991 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 1570 |
| 17 | `<src><\|wait\|></src>` | `<src>So, </src>` | 758 |
| 18 | `<src>So you have some </src>` | `<src>you have some </src>` | 1055 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 753 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 288 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 434 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1865 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 976 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1609 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1131 |
| 5 | `<src>he's been without food, </src>` | `<src>he knows that </src>` | 1622 |
| 6 | `<src><\|wait\|></src>` | `<src>food in the wilderness </src>` | 1306 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>sporty day is that he's hungry. </src>` | 2454 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1169 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 2902 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 2451 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2462 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1820 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1162 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that </src>` | 1423 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 1590 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 692 |
| 17 | `<src>Man shall not live </src>` | `<src>Man generally </src>` | 333 |
| 18 | `<src>by bread alone. </src>` | `<src>led by brute alone. </src>` | 547 |

---

### Test Example 56 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2103 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 1012 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1986 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 858 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1670 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1178 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 2850 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 785 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 2112 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 3033 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 2612 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1728 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1227 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1442 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1639 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 960 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 517 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 373 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2069 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1061 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1442 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 1213 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1530 |
| 6 | `<src>的部分。</src>` | `<src>客厅的部分。</src>` | 1367 |
| 7 | `<src>那客厅一般</src>` | `<src><\|wait\|></src>` | 1795 |
| 8 | `<src>都是属于</src>` | `<src>那客厅一般都是</src>` | 1791 |
| 9 | `<src>我们</src>` | `<src>属于我们</src>` | 1502 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 3453 |
| 11 | `<src><\|wait\|></src>` | `<src>所以</src>` | 520 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>呢，是身体的部分</src>` | 2561 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，会反映的是</src>` | 1718 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 2028 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 515 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的做</src>` | 1611 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>一下啦休息。</src>` | 652 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可不，我们可以看到这边是</src>` | 394 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 540 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 283 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 359 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1899 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1023 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1474 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 1083 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 833 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 2169 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1913 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1684 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1534 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 3434 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 522 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 2306 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1745 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 433 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 2180 |
| 16 | `<src><\|wait\|></src>` | `<src>and like it </src>` | 533 |
| 17 | `<src>get straight to the point. </src>` | `<src>gets straight to the point. </src>` | 1309 |
| 18 | `<src>They also love to </src>` | `<src><\|wait\|></src>` | 791 |
| 19 | `<src>play </src>` | `<src>They also love to play </src>` | 610 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, </src>` | 413 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 341 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 306 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 290 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. </src>` | 322 |
| 25 | `<src>ENTP stands for </src>` | `<src>Stands for </src>` | 261 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1971 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1182 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1757 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 875 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 2725 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1499 |
| 7 | `<src>제법 생색까지 </src>` | `<src><\|wait\|></src>` | 2078 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>제법 생색까지 냈지만 이제 는 </src>` | 1571 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 3811 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2549 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1700 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1017 |
| 13 | `<src><\|wait\|></src>` | `<src>드러내 놓고 윤석열 후보 </src>` | 1657 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>를 떨어뜨리 겠다는 </src>` | 1646 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 686 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 361 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 510 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 327 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 294 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 153 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건 </src>` | 238 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 278 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 289 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 </src>` | 279 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 292 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2105 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね今</src>` | 1030 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいな</src>` | 901 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>です。なので</src>` | 898 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ここのね</src>` | 1006 |
| 6 | `<src>も</src>` | `<src>プロフェッショナルホテルも</src>` | 2751 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>超食が食べれる場所</src>` | 1225 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 2353 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になっているので</src>` | 1266 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2341 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドーストーンホテル</src>` | 1942 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいなって</src>` | 2499 |
| 13 | `<src>なっていう方はですね</src>` | `<src>いう方はですね</src>` | 1648 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 602 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 2004 |
| 16 | `<src><\|wait\|></src>` | `<src>なと。はい。</src>` | 1078 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思います。</src>` | 705 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね</src>` | 823 |
| 19 | `<src>駅ももう</src>` | `<src>プサン駅も</src>` | 560 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 275 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかるか</src>` | 189 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かからないか</src>` | 323 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 298 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>リッチのねまあホテル</src>` | 333 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってます</src>` | 261 |
| 26 | `<src>よかったらですね</src>` | `<src>ので行ったらですね</src>` | 288 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 265 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 192 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は。</src>` | 159 |
