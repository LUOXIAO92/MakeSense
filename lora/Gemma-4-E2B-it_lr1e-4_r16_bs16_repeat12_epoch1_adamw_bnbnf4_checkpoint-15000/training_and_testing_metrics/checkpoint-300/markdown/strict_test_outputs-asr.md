# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9965
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 1.0000
  - SRC_RELEASE_TOTAL: 716
  - SRC_WAIT_ACCURACY: 0.0000
  - SRC_WAIT_TOTAL: 150
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
  - PROCESS_TIME_MS_AVG: 1424.7010
  - PROCESS_TIME_MS_P50: 1328.7760
  - PROCESS_TIME_MS_P95: 2552.8400
  - PROCESS_TIME_MS_MAX: 15265.0200

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
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1848 |
| 2 | `<src>あの特に</src>` | `<src>あの</src>` | 865 |
| 3 | `<src>これなんかまだ</src>` | `<src>特に</src>` | 1508 |
| 4 | `<src>一年生ですからね。</src>` | `<src>中まだ1年生からね。</src>` | 545 |
| 5 | `<src>この時点で</src>` | `<src>はい、はい。</src>` | 907 |
| 6 | `<src>こう短く</src>` | `<src>その時点で</src>` | 2451 |
| 7 | `<src>剪定を</src>` | `<src>こう</src>` | 380 |
| 8 | `<src><\|wait\|></src>` | `<src>資格を</src>` | 2015 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>とりあえず</src>` | 2086 |
| 10 | `<src>十年経っても</src>` | `<src>資格を</src>` | 762 |
| 11 | `<src>大した。</src>` | `<src>持っても</src>` | 2292 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要</src>` | 2310 |
| 2 | `<src>家长需要做的是，</src>` | `<src>做的是</src>` | 922 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 1455 |
| 4 | `<src>用我们深深的</src>` | `<src>身上的爱胶水</src>` | 1235 |
| 5 | `<src>爱浇水、</src>` | `<src>是</src>` | 531 |
| 6 | `<src>施肥，</src>` | `<src>是</src>` | 2257 |
| 7 | `<src>给足</src>` | `<src>给儿子</src>` | 506 |
| 8 | `<src>孩子心理营养，</src>` | `<src>心里影响</src>` | 1780 |
| 9 | `<src><\|wait\|></src>` | `<src>给内心的</src>` | 2300 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>孩子慢慢</src>` | 627 |
| 11 | `<src>慢慢长大。</src>` | `<src>长大</src>` | 2578 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要</src>` | 2122 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>气数</src>` | 840 |
| 3 | `<src>但是</src>` | `<src>是容易的，</src>` | 1645 |
| 4 | `<src>只有一个师父</src>` | `<src>但是</src>` | 1185 |
| 5 | `<src><\|wait\|></src>` | `<src>只有</src>` | 961 |
| 6 | `<src>知道如何</src>` | `<src>一个</src>` | 1827 |
| 7 | `<src>处于中间，</src>` | `<src>师傅</src>` | 824 |
| 8 | `<src>所以</src>` | `<src>之出于</src>` | 1567 |
| 9 | `<src>虚阿凡</src>` | `<src>中间，</src>` | 2292 |
| 10 | `<src>要成为</src>` | `<src>所以</src>` | 639 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个</src>` | 2748 |

---

### Test Example 4 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1994 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Apple </src>` | 850 |
| 3 | `<src>촉발 시키고 </src>` | `<src>fruit </src>` | 1539 |
| 4 | `<src><\|wait\|></src>` | `<src>pick and </src>` | 1256 |
| 5 | `<src>자신 의 </src>` | `<src>eat </src>` | 651 |
| 6 | `<src><\|wait\|></src>` | `<src>your own </src>` | 2167 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>jogging </src>` | 944 |
| 8 | `<src><\|wait\|></src>` | `<src>heruna </src>` | 1432 |
| 9 | `<src>박한상과 </src>` | `<src>pachang </src>` | 2292 |
| 10 | `<src><\|wait\|></src>` | `<src>and </src>` | 638 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>four generations </src>` | 2745 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>为什么</src>` | 2376 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>的种子纸</src>` | 818 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>里边，这个幼苗</src>` | 1694 |
| 4 | `<src>然后</src>` | `<src>也很大，</src>` | 1284 |
| 5 | `<src><\|wait\|></src>` | `<src>然后</src>` | 1359 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在</src>` | 1325 |
| 7 | `<src>儿核桃</src>` | `<src>放给</src>` | 992 |
| 8 | `<src><\|wait\|></src>` | `<src>他和陶人</src>` | 1442 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>在家里</src>` | 2280 |
| 10 | `<src>这种核桃</src>` | `<src>在家里</src>` | 628 |
| 11 | `<src>仁儿。</src>` | `<src>这种</src>` | 2710 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 2160 |
| 2 | `<src>옹심이, </src>` | `<src>영심이 </src>` | 976 |
| 3 | `<src><\|wait\|></src>` | `<src>칼 </src>` | 1396 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 </src>` | 1235 |
| 5 | `<src>옹심이가 </src>` | `<src>용심이 칼 </src>` | 621 |
| 6 | `<src><\|wait\|></src>` | `<src>용심이가 </src>` | 2243 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>석연 </src>` | 1091 |
| 8 | `<src>야, </src>` | `<src>되는 건데요. </src>` | 1588 |
| 9 | `<src>진짜 이거 </src>` | `<src>야. </src>` | 2048 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>진짜 이거 </src>` | 1093 |
| 11 | `<src>진짜. </src>` | `<src>행으로 </src>` | 2558 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>跑萨玩一</src>` | 2244 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>后呢，内部的</src>` | 1768 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>的液体</src>` | 643 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>剪清，能量也</src>` | 1374 |
| 5 | `<src>然后</src>` | `<src>刷了，然后</src>` | 1359 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在</src>` | 1344 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1127 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的运行状态</src>` | 1996 |
| 9 | `<src>状态，</src>` | `<src>状态。</src>` | 1665 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1127 |
| 11 | `<src>抑郁状态。</src>` | `<src>的低语状态。</src>` | 2641 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>因为这个情况</src>` | 2054 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>我们就是</src>` | 876 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1491 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就是赶紧</src>` | 1244 |
| 5 | `<src>或是通知对方，</src>` | `<src>回复主管</src>` | 966 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>就是通知对方</src>` | 1871 |
| 7 | `<src>不要想自己</src>` | `<src>一下这个状况，</src>` | 1190 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>不要想自己</src>` | 1690 |
| 9 | `<src>独立承担。</src>` | `<src>怎么把它扛下来</src>` | 2077 |
| 10 | `<src>整体而言，</src>` | `<src>工具里承担，</src>` | 1456 |
| 11 | `<src>事业运就属凶。</src>` | `<src>真的而已，</src>` | 2354 |

---

### Test Example 9 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명단에 있는 </src>` | 2396 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>익명들은 </src>` | 935 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1412 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능이 높지 </src>` | 1236 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 742 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 </src>` | 2202 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>뽑힌 </src>` | 1383 |
| 8 | `<src>때문 입니다. </src>` | `<src>사람들이 </src>` | 2074 |
| 9 | `<src><\|wait\|></src>` | `<src>있었습니다. </src>` | 1486 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실을 </src>` | 1740 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐던 </src>` | 2086 |

---

### Test Example 10 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1808 |
| 2 | `<src><\|wait\|></src>` | `<src>回到我的</src>` | 834 |
| 3 | `<src>回到我生活</src>` | `<src>生活</src>` | 1531 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>有一个轨道，</src>` | 348 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能</src>` | 1108 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好在它下降的时候，</src>` | 1492 |
| 7 | `<src>在做热汤</src>` | `<src>在座日</src>` | 1264 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>唐人</src>` | 1431 |
| 9 | `<src><\|wait\|></src>` | `<src>人，我当时</src>` | 2393 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被一</src>` | 1142 |
| 11 | `<src>小小的愿望</src>` | `<src>个小小的愿望</src>` | 2203 |
| 12 | `<src>哈。</src>` | `<src>好</src>` | 1636 |

---

### Test Example 11 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 이럴지 너무 </src>` | 2191 |
| 2 | `<src><\|wait\|></src>` | `<src>그니 </src>` | 858 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>저희 여야 일 수 있지만 </src>` | 1606 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살도 </src>` | 1288 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기가 </src>` | 1254 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살인데 꿈일 필요 </src>` | 1518 |
| 7 | `<src>뭐 있고 </src>` | `<src>없고 이거 </src>` | 1169 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 보살로 보일 필요 </src>` | 2424 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>없을 필요 있어요. 우주가 </src>` | 1514 |
| 10 | `<src>지금 나한테 </src>` | `<src>다원티 보살이 </src>` | 3037 |
| 11 | `<src>보살 이라는데. </src>` | `<src>란데 </src>` | 803 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1869 |
| 2 | `<src>doing? </src>` | `<src>saying? </src>` | 907 |
| 3 | `<src>Drop into </src>` | `<src>Drop pin to your body. </src>` | 1565 |
| 4 | `<src>your body. </src>` | `<src>Where does </src>` | 1186 |
| 5 | `<src>Where does the tension </src>` | `<src>attention start? </src>` | 1165 |
| 6 | `<src>start? What is it? </src>` | `<src>What is it? Is it a </src>` | 1787 |
| 7 | `<src>Is it a headache? </src>` | `<src>day? Cuz it's a </src>` | 1320 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>time in your chest. </src>` | 2285 |
| 9 | `<src>I ask them what </src>` | `<src>I have a sob. </src>` | 1311 |
| 10 | `<src><\|wait\|></src>` | `<src>Like which are you using? </src>` | 2634 |
| 11 | `<src>language are you using? </src>` | `<src>Saying. </src>` | 1337 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>And </src>` | 2283 |
| 2 | `<src>And lastly, </src>` | `<src>lastly, </src>` | 814 |
| 3 | `<src>is repeat. </src>` | `<src>he's repeat, </src>` | 1694 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>learned to repeat </src>` | 1311 |
| 5 | `<src>Find what you're good at </src>` | `<src>find out you're good at </src>` | 1347 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1472 |
| 7 | `<src><\|wait\|></src>` | `<src>And well, you're not good at </src>` | 2231 |
| 8 | `<src>And what you're not good at, </src>` | `<src>that, get to people </src>` | 2494 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>around you to help you with </src>` | 1561 |
| 10 | `<src><\|wait\|></src>` | `<src>and </src>` | 2212 |
| 11 | `<src>And until next time. </src>` | `<src>and tell </src>` | 463 |

---

### Test Example 14 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>待て</src>` | 2247 |
| 2 | `<src>このあたりから</src>` | `<src>この辺りから</src>` | 974 |
| 3 | `<src>始めた</src>` | `<src>始まったもので</src>` | 1411 |
| 4 | `<src>もので、</src>` | `<src>ご</src>` | 1239 |
| 5 | `<src>ゴッホ、</src>` | `<src>方</src>` | 603 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン</src>` | 2236 |
| 7 | `<src><\|wait\|></src>` | `<src>です。</src>` | 977 |
| 8 | `<src>セザンヌ、</src>` | `<src>その</src>` | 1389 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナール</src>` | 2347 |
| 10 | `<src>という人の絵</src>` | `<src>という人</src>` | 685 |
| 11 | `<src>は、田舎の</src>` | `<src>の絵は</src>` | 2880 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の</src>` | 836 |

---

### Test Example 15 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying </src>` | 1954 |
| 2 | `<src>Did very important research </src>` | `<src>important research </src>` | 946 |
| 3 | `<src><\|wait\|></src>` | `<src>on extremely happy </src>` | 1549 |
| 4 | `<src>on extremely happy people. </src>` | `<src>people. This is </src>` | 1356 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip the stem, </src>` | 1974 |
| 6 | `<src>research, </src>` | `<src>research. Looking </src>` | 819 |
| 7 | `<src>looking at the ten percent </src>` | `<src>at 10% </src>` | 1916 |
| 8 | `<src><\|wait\|></src>` | `<src>of the happiest </src>` | 2325 |
| 9 | `<src>of the happiest people </src>` | `<src>people out </src>` | 686 |
| 10 | `<src>out there, </src>` | `<src>there. People </src>` | 2412 |
| 11 | `<src>people that we can learn from. </src>` | `<src>like we can learn from. </src>` | 1638 |

---

### Test Example 16 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched rubber</src>` | 2017 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>band, chemical</src>` | 897 |
| 3 | `<src>chemical bonds </src>` | `<src>bands also store</src>` | 1498 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those</src>` | 1309 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bands are broken,</src>` | 1183 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy gets</src>` | 1601 |
| 7 | `<src>gets converted to </src>` | `<src>converted to other</src>` | 1120 |
| 8 | `<src>other types of energy, </src>` | `<src>types of energy, like</src>` | 1633 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light.</src>` | 2030 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets you</src>` | 1211 |
| 11 | `<src>or gets used to make </src>` | `<src>to make different bonds</src>` | 2646 |
| 12 | `<src>different bonds. </src>` | `<src>that</src>` | 438 |

---

### Test Example 17 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなど</src>` | 2327 |
| 2 | `<src>あの</src>` | `<src>が</src>` | 890 |
| 3 | `<src>いただもらえる</src>` | `<src>あの、いただ</src>` | 1551 |
| 4 | `<src>といったようなものも</src>` | `<src>くても</src>` | 1312 |
| 5 | `<src>用意しておりますので</src>` | `<src>良いものも用意しておりますので</src>` | 2030 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご</src>` | 763 |
| 7 | `<src>ご連絡としては</src>` | `<src>さください。</src>` | 1109 |
| 8 | `<src>以上になりまして、</src>` | `<src>ご連絡としては</src>` | 1684 |
| 9 | `<src>えっと</src>` | `<src>以上になりました。</src>` | 1983 |
| 10 | `<src><\|wait\|></src>` | `<src>えっと</src>` | 1221 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>皆さん</src>` | 2400 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>の案内がありますので、</src>` | 666 |

---

### Test Example 18 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 2107 |
| 2 | `<src>一切正常，</src>` | `<src>以为</src>` | 823 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>一切正常，</src>` | 1653 |
| 4 | `<src>所以</src>` | `<src>我</src>` | 1190 |
| 5 | `<src>坚持不开刀。</src>` | `<src>可以</src>` | 984 |
| 6 | `<src>期间</src>` | `<src>坚持</src>` | 1811 |
| 7 | `<src>大概有十位医生</src>` | `<src>打开，</src>` | 992 |
| 8 | `<src>来诊断，</src>` | `<src>其实</src>` | 1380 |
| 9 | `<src>一下敲腿，</src>` | `<src>大概</src>` | 2167 |
| 10 | `<src>一下提腿，</src>` | `<src>有</src>` | 568 |
| 11 | `<src>都没有问题。</src>` | `<src>一上</src>` | 2515 |
| 12 | `<src>他们</src>` | `<src>下，</src>` | 1286 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>没有</src>` | 975 |

---

### Test Example 19 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>アドワンさん</src>` | 2399 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が離れてくる</src>` | 949 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>ような感じで</src>` | 1431 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オーサーロカタが</src>` | 1362 |
| 5 | `<src>多いですね。</src>` | `<src>やっぱり多いですね。</src>` | 2378 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 537 |
| 7 | `<src>すごい</src>` | `<src>すぐ</src>` | 1134 |
| 8 | `<src>自己意識高いし、</src>` | `<src>生きがい欲しい方</src>` | 2109 |
| 9 | `<src>自分で</src>` | `<src>が</src>` | 1480 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>ちょっと本音を</src>` | 1394 |
| 11 | `<src>傾向が強いので、</src>` | `<src>打ち合うのが</src>` | 2556 |
| 12 | `<src>なので。</src>` | `<src>強いので</src>` | 993 |

---

### Test Example 20 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name's </src>` | 2130 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran </src>` | 806 |
| 3 | `<src>I am currently </src>` | `<src>Matirigu. Hi, </src>` | 1661 |
| 4 | `<src><\|wait\|></src>` | `<src>I'm currently studying </src>` | 1360 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>in finance and </src>` | 1782 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>a bit of psychology. </src>` | 957 |
| 7 | `<src><\|wait\|></src>` | `<src>Uh here </src>` | 1358 |
| 8 | `<src>here at the ANU, </src>` | `<src>you </src>` | 1934 |
| 9 | `<src><\|wait\|></src>` | `<src>and uh in the </src>` | 1611 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go </src>` | 2289 |
| 11 | `<src><\|wait\|></src>` | `<src>into corporate </src>` | 1562 |
| 12 | `<src>corporate consultancy. </src>` | `<src>consultancy. </src>` | 1170 |

---

### Test Example 21 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2346 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th Amendment </src>` | 964 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>and </src>` | 1404 |
| 4 | `<src>and to explore its </src>` | `<src>to explore </src>` | 877 |
| 5 | `<src>history as a guide </src>` | `<src>its history as a guide </src>` | 636 |
| 6 | `<src>to how political </src>` | `<src>to help political </src>` | 2482 |
| 7 | `<src><\|wait\|></src>` | `<src>change </src>` | 540 |
| 8 | `<src>change can happen </src>` | `<src>can happen </src>` | 1802 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2481 |
| 10 | `<src><\|wait\|></src>` | `<src>The meaning </src>` | 898 |
| 11 | `<src>The meanings </src>` | `<src>of the amendment </src>` | 2754 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, </src>` | 714 |
| 13 | `<src>myriad. </src>` | `<src>of course, I'm </src>` | 2005 |

---

### Test Example 22 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>다른 </src>` | 2056 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>먼지레 죽여 달라고 </src>` | 2214 |
| 3 | `<src>해가지고 내가 </src>` | `<src>달라고 하고 내가 죽이길 </src>` | 506 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>부로 하 수도 다. </src>` | 1270 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔치 </src>` | 2469 |
| 6 | `<src>죽여 달라 </src>` | `<src>때 죽여 달라고 하잖아. </src>` | 1155 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>내가 </src>` | 1486 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>죽은 소리 안 듣고 </src>` | 2463 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았는데 </src>` | 2780 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>나는 야. </src>` | 1210 |
| 11 | `<src>내가 가. </src>` | `<src>아. 내가 </src>` | 2040 |

---

### Test Example 23 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1885 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 932 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相不怪的人之间</src>` | 1641 |
| 4 | `<src><\|wait\|></src>` | `<src>有这种</src>` | 1219 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>毛病</src>` | 2163 |
| 6 | `<src>难道会是</src>` | `<src>而已，</src>` | 712 |
| 7 | `<src><\|wait\|></src>` | `<src>难道</src>` | 1509 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>会是</src>` | 2344 |
| 9 | `<src><\|wait\|></src>` | `<src>从那天</src>` | 1053 |
| 10 | `<src><\|wait\|></src>` | `<src>开始的。</src>` | 2668 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思</src>` | 1338 |
| 12 | `<src>连篇。</src>` | `<src>了</src>` | 2038 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2341 |
| 2 | `<src>です。</src>` | `<src>です</src>` | 793 |
| 3 | `<src>ギアが</src>` | `<src>ギアが緩むと</src>` | 1685 |
| 4 | `<src>緩むと芯が</src>` | `<src>シングア</src>` | 1207 |
| 5 | `<src><\|wait\|></src>` | `<src>が</src>` | 998 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>できなくなってしまうので</src>` | 1889 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1246 |
| 8 | `<src>役ねじの</src>` | `<src>逆ネジの</src>` | 1868 |
| 9 | `<src>ナットが</src>` | `<src>ナットが付いて</src>` | 1766 |
| 10 | `<src>ついているっていうことです</src>` | `<src>いるっていうこと</src>` | 1614 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 2148 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 640 |
| 13 | `<src>分解完了。</src>` | `<src>ハイ分解</src>` | 1747 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 2047 |
| 2 | `<src><\|wait\|></src>` | `<src>进入到</src>` | 952 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二期时，</src>` | 1541 |
| 4 | `<src>服务</src>` | `<src>会服</src>` | 1271 |
| 5 | `<src>在一级一线</src>` | `<src>在二期一线</src>` | 1239 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼大的牛们。</src>` | 1562 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1115 |
| 8 | `<src><\|wait\|></src>` | `<src>在做微信</src>` | 1627 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>沟通好事几年，</src>` | 2145 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1352 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信</src>` | 2402 |
| 12 | `<src>的新榜反而</src>` | `<src>好平分的</src>` | 787 |
| 13 | `<src>火了。</src>` | `<src>心膀反而</src>` | 1640 |

---

### Test Example 26 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2398 |
| 2 | `<src>and then </src>` | `<src>And then after </src>` | 937 |
| 3 | `<src>after these examples, </src>` | `<src>these examples, </src>` | 1500 |
| 4 | `<src><\|wait\|></src>` | `<src>the </src>` | 1238 |
| 5 | `<src>the instruction </src>` | `<src>instruction </src>` | 1044 |
| 6 | `<src>tells us to use </src>` | `<src>tell us to use </src>` | 1840 |
| 7 | `<src><\|wait\|></src>` | `<src>actually </src>` | 2055 |
| 8 | `<src>actually </src>` | `<src>the </src>` | 2109 |
| 9 | `<src><\|wait\|></src>` | `<src>this </src>` | 762 |
| 10 | `<src>these values. So </src>` | `<src>values. So </src>` | 2217 |
| 11 | `<src><\|wait\|></src>` | `<src>game.dot </src>` | 1615 |
| 12 | `<src>this game dot scored array. </src>` | `<src>board array. </src>` | 1099 |
| 13 | `<src><\|wait\|></src>` | `<src>And </src>` | 1187 |

---

### Test Example 27 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>扎到了一个</src>` | 1898 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>电池片，</src>` | 917 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1434 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>找到了电池片之后</src>` | 1215 |
| 5 | `<src>请你务必就要</src>` | `<src>清理</src>` | 457 |
| 6 | `<src><\|wait\|></src>` | `<src>USB接口</src>` | 2374 |
| 7 | `<src>先守住，</src>` | `<src>就要先</src>` | 475 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>手持</src>` | 1796 |
| 9 | `<src><\|wait\|></src>` | `<src>做，</src>` | 2288 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>不要想</src>` | 623 |
| 11 | `<src><\|wait\|></src>` | `<src>着，</src>` | 2596 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>我们会</src>` | 1158 |
| 13 | `<src><\|wait\|></src>` | `<src>这么讲，</src>` | 992 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢，</src>` | 1329 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Well, </src>` | 2091 |
| 2 | `<src>have to produce </src>` | `<src>if you have to produce </src>` | 992 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1500 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1349 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1707 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1112 |
| 7 | `<src>to spell </src>` | `<src>how to spell the word </src>` | 1493 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>is like, </src>` | 2345 |
| 9 | `<src>is this word </src>` | `<src>oh, is this word </src>` | 1090 |
| 10 | `<src>spelled with a double </src>` | `<src>start with a double P? </src>` | 2501 |
| 11 | `<src><\|wait\|></src>` | `<src>Double P? </src>` | 1314 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>I don't know. </src>` | 1151 |
| 13 | `<src>know. </src>` | `<src>Oh, </src>` | 1151 |

---

### Test Example 29 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>So this </src>` | 2049 |
| 2 | `<src>そこで</src>` | `<src>so this </src>` | 934 |
| 3 | `<src><\|wait\|></src>` | `<src>is where you have to </src>` | 1565 |
| 4 | `<src>テキという設備寺が</src>` | `<src>do 7.2 GB </src>` | 1384 |
| 5 | `<src>ありましたね。</src>` | `<src>of space, right? </src>` | 2249 |
| 6 | `<src>で、</src>` | `<src>And </src>` | 473 |
| 7 | `<src><\|wait\|></src>` | `<src>then </src>` | 1831 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>the way the </src>` | 2431 |
| 9 | `<src><\|wait\|></src>` | `<src>Hasei-yo's </src>` | 891 |
| 10 | `<src>は五経、</src>` | `<src>shikumi wa </src>` | 2981 |
| 11 | `<src><\|wait\|></src>` | `<src>the same as </src>` | 869 |
| 12 | `<src>設備寺、五比</src>` | `<src>the 7.2 GB </src>` | 1778 |
| 13 | `<src>です。</src>` | `<src>of GB. </src>` | 350 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家</src>` | 2211 |
| 2 | `<src>要提醒大家，</src>` | `<src>在</src>` | 863 |
| 3 | `<src>在这个罗马呢</src>` | `<src>这个罗马呢</src>` | 1589 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是</src>` | 1201 |
| 5 | `<src>所以呢，</src>` | `<src>因为造成的</src>` | 1079 |
| 6 | `<src>你现在</src>` | `<src>所以呢</src>` | 1723 |
| 7 | `<src>所面临的一些</src>` | `<src>现在</src>` | 971 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>除了你的一些</src>` | 1444 |
| 9 | `<src>也不可能是</src>` | `<src>遗迹啊</src>` | 2320 |
| 10 | `<src>一夕之间就</src>` | `<src>跟丰盛</src>` | 1111 |
| 11 | `<src><\|wait\|></src>` | `<src>也包括</src>` | 2535 |
| 12 | `<src>演变出来的，</src>` | `<src>你以前</src>` | 746 |
| 13 | `<src>因此会建议</src>` | `<src>的遗址</src>` | 1280 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>会见证</src>` | 864 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라더니</src>` | 2066 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>일거트는</src>` | 893 |
| 3 | `<src>인슐린과 </src>` | `<src>거진</src>` | 1443 |
| 4 | `<src>이제 거진 </src>` | `<src>유니셜링과</src>` | 1398 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>이거진 유산</src>` | 2009 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>전용기능을</src>` | 850 |
| 7 | `<src>굉장히 아주 </src>` | `<src>완전히</src>` | 1626 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>다른</src>` | 2096 |
| 9 | `<src>이렇게 </src>` | `<src>모네랄이다</src>` | 1167 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이게</src>` | 2537 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>그러니까</src>` | 1311 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거에다가</src>` | 1489 |
| 13 | `<src>아연. </src>` | `<src>아니면</src>` | 857 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중에서 </src>` | 1918 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개 가 </src>` | 1792 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중앙에 </src>` | 666 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>분산되어 </src>` | 1275 |
| 5 | `<src>많았습니다. </src>` | `<src>100명 미만으로 </src>` | 1527 |
| 6 | `<src>일반 적으로는 </src>` | `<src>작은 기업들이 </src>` | 1306 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>성장 하거나 </src>` | 1389 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 </src>` | 2268 |
| 9 | `<src>걷게 되는데 </src>` | `<src>해화법에 </src>` | 1301 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>거의 </src>` | 2411 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성기 없으면 </src>` | 1571 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>성장도 </src>` | 2035 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>폐업 하지는 </src>` | 976 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>帝王的</src>` | 1913 |
| 2 | `<src>我们可以看到的是</src>` | `<src>部分我们</src>` | 886 |
| 3 | `<src>一个在钓鱼</src>` | `<src>看到的是</src>` | 1530 |
| 4 | `<src>的人，但是</src>` | `<src>个帝王，但</src>` | 1369 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>他是</src>` | 1178 |
| 6 | `<src>所以</src>` | `<src>有意义上的</src>` | 1615 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>这一通场</src>` | 1628 |
| 8 | `<src>时候，就要去</src>` | `<src>场一个状况</src>` | 2442 |
| 9 | `<src>特别注意，</src>` | `<src>去特别注意</src>` | 929 |
| 10 | `<src>是它能不能够</src>` | `<src>是</src>` | 2250 |
| 11 | `<src>钓到鱼，</src>` | `<src>他能不能</src>` | 1527 |
| 12 | `<src>它钓不到鱼</src>` | `<src>得到</src>` | 1031 |
| 13 | `<src><\|wait\|></src>` | `<src>与他</src>` | 1277 |
| 14 | `<src>的意思哦。</src>` | `<src>的意事</src>` | 1046 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 2072 |
| 2 | `<src>There were </src>` | `<src>there </src>` | 868 |
| 3 | `<src><\|wait\|></src>` | `<src>was such </src>` | 1536 |
| 4 | `<src>such interfaces before, </src>` | `<src>instances before </src>` | 981 |
| 5 | `<src><\|wait\|></src>` | `<src>net future </src>` | 472 |
| 6 | `<src>netfilter, TC. </src>` | `<src>TC </src>` | 2437 |
| 7 | `<src>Yeah, so </src>` | `<src>there. </src>` | 398 |
| 8 | `<src>this is just </src>` | `<src>And so </src>` | 1900 |
| 9 | `<src>one another place </src>` | `<src>this is just one </src>` | 2553 |
| 10 | `<src>to look at. </src>` | `<src>another place </src>` | 644 |
| 11 | `<src>But </src>` | `<src>where </src>` | 2641 |
| 12 | `<src><\|wait\|></src>` | `<src>devoted </src>` | 976 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1083 |
| 14 | `<src>working on BugRepo </src>` | `<src>would be </src>` | 1225 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1205 |

---

### Test Example 35 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの </src>` | 1988 |
| 2 | `<src>映画でですね、</src>` | `<src>え 、 え 、 </src>` | 994 |
| 3 | `<src>いろんな場面で</src>` | `<src>あんて です ね 。 </src>` | 1536 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src> いる の は 場面 で 、 </src>` | 1465 |
| 5 | `<src>調べるときに、</src>` | `<src> 斉速 稼働 か と いう 時 に 、 </src>` | 2700 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src> 安定 の 乱行 を 調べ 、 </src>` | 2037 |
| 7 | `<src>ことで、あの</src>` | `<src> こと で 、 あの </src>` | 2474 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src> 斉速 稼働 か と いう </src>` | 1026 |
| 9 | `<src>保証する、生息である</src>` | `<src> 斉速 で 、 </src>` | 2908 |
| 10 | `<src>ことを保証する</src>` | `<src> 斉速 で 、 こと を 保証 する と 言っ て い た 。 </src>` | 795 |
| 11 | `<src>といったような</src>` | `<src> あと 使い 方 を さ れ まし た 。 </src>` | 1846 |
| 12 | `<src>使い方をされます。</src>` | `<src> </src>` | 1308 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>that someone who's</src>` | 2334 |
| 2 | `<src>just getting going </src>` | `<src>getting going needs</src>` | 863 |
| 3 | `<src>needs to get, </src>` | `<src>to get</src>` | 1455 |
| 4 | `<src><\|wait\|></src>` | `<src>and</src>` | 978 |
| 5 | `<src>and I have ten of them </src>` | `<src>that ten of them</src>` | 515 |
| 6 | `<src>that I think are </src>` | `<src>that are really important</src>` | 2491 |
| 7 | `<src>really important. </src>` | `<src>to</src>` | 308 |
| 8 | `<src><\|wait\|></src>` | `<src>um</src>` | 1387 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go and do</src>` | 3056 |
| 10 | `<src>I have about </src>` | `<src>I have about one</src>` | 681 |
| 11 | `<src>one minute videos </src>` | `<src>video</src>` | 2723 |
| 12 | `<src>that follow this video </src>` | `<src>that's all this video</src>` | 1078 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one</src>` | 2022 |
| 14 | `<src>that cover each one </src>` | `<src>in a little more detail</src>` | 1080 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>but</src>` | 850 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在产房方面</src>` | 2113 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这是产房</src>` | 897 |
| 3 | `<src>很不错的，但是</src>` | `<src>可以说的</src>` | 1447 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>差不多，但是</src>` | 1199 |
| 5 | `<src>也就是</src>` | `<src>比较</src>` | 433 |
| 6 | `<src>在事业方面的</src>` | `<src>在产房的</src>` | 2441 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>医疗中心</src>` | 1070 |
| 8 | `<src>与收入的</src>` | `<src>所待的</src>` | 1489 |
| 9 | `<src>提升。如果是在</src>` | `<src>红利收入的</src>` | 2321 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>提升，如果</src>` | 1264 |
| 11 | `<src>这个月</src>` | `<src>在投资领域</src>` | 2577 |
| 12 | `<src>也是不错，只是</src>` | `<src>来说，也是不错，只是</src>` | 862 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对来说</src>` | 1581 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微</src>` | 1067 |
| 15 | `<src><\|wait\|></src>` | `<src>入了一个</src>` | 1312 |

---

### Test Example 38 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>Oh, </src>` | 1894 |
| 2 | `<src>HTML이라고 </src>` | `<src>eighty-</src>` | 1000 |
| 3 | `<src><\|wait\|></src>` | `<src>eighty-one, </src>` | 1508 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>which is </src>` | 1293 |
| 5 | `<src><\|wait\|></src>` | `<src>also </src>` | 2133 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>a person </src>` | 720 |
| 7 | `<src><\|wait\|></src>` | `<src>who can also </src>` | 1794 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>do </src>` | 2046 |
| 9 | `<src>문법 에 </src>` | `<src>do </src>` | 947 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>the wrong thing. </src>` | 1712 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>We need to write </src>` | 2220 |
| 12 | `<src>되는데 </src>` | `<src>the articles, </src>` | 1086 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>but </src>` | 1211 |
| 14 | `<src>프로그램 이 </src>` | `<src>we need to write </src>` | 1098 |
| 15 | `<src>필요 합니다. </src>` | `<src>the articles, </src>` | 1301 |

---

### Test Example 39 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>10</src>` | 2166 |
| 2 | `<src>十一二手とか</src>` | `<src>12手とか</src>` | 1838 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>あった。恐らく</src>` | 677 |
| 4 | `<src>十秒で。</src>` | `<src>10秒で</src>` | 1277 |
| 5 | `<src>まあ</src>` | `<src>まあ1秒</src>` | 1162 |
| 6 | `<src>一秒に</src>` | `<src>に</src>` | 1506 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>行って</src>` | 857 |
| 8 | `<src>計算ですか</src>` | `<src>今日ぐらいの</src>` | 1531 |
| 9 | `<src>ね。</src>` | `<src>せつあんすかね。</src>` | 2424 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1167 |
| 11 | `<src>おそらく</src>` | `<src>恐らく</src>` | 2425 |
| 12 | `<src><\|wait\|></src>` | `<src>11手</src>` | 719 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1965 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 726 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮山とかが</src>` | 1128 |
| 16 | `<src>あるから。</src>` | `<src>だから</src>` | 679 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 2285 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>村せてやる</src>` | 961 |
| 3 | `<src>俺は</src>` | `<src>あれ</src>` | 1410 |
| 4 | `<src><\|wait\|></src>` | `<src>俺は</src>` | 1235 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>ひきつ</src>` | 621 |
| 6 | `<src><\|wait\|></src>` | `<src>よ見てる</src>` | 2236 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1098 |
| 8 | `<src><\|wait\|></src>` | `<src>超えてる</src>` | 1597 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不自由</src>` | 2100 |
| 10 | `<src><\|wait\|></src>` | `<src>の奇跡よ。</src>` | 1276 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 2434 |
| 12 | `<src>船大工をやってる</src>` | `<src>の代行を</src>` | 599 |
| 13 | `<src>が、</src>` | `<src>やってる</src>` | 1960 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなに</src>` | 858 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>すごい</src>` | 1021 |
| 16 | `<src>見たことがない。</src>` | `<src>速線を見たことがない。</src>` | 707 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Educational</src>` | 2203 |
| 2 | `<src>Educational attainment. </src>` | `<src>entainment. How far</src>` | 895 |
| 3 | `<src>How far did you </src>` | `<src>did you actually</src>` | 1604 |
| 4 | `<src><\|wait\|></src>` | `<src>go in your</src>` | 1305 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>education? Did you</src>` | 2244 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school?</src>` | 643 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of</src>` | 1813 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>entertainment. Did you</src>` | 2529 |
| 9 | `<src>to college, </src>` | `<src>go to college, and</src>` | 753 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>so did you graduate?</src>` | 2870 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of</src>` | 942 |
| 12 | `<src>attainment. </src>` | `<src>entertainment.</src>` | 1973 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now.</src>` | 1008 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you</src>` | 1115 |
| 15 | `<src>online. </src>` | `<src>online.</src>` | 450 |

---

### Test Example 42 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>또 이 또 </src>` | 1978 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알고 있나요? </src>` | 1802 |
| 3 | `<src>이방인으로 </src>` | `<src>여기 가 이방인으로 </src>` | 715 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때 에 </src>` | 1306 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못 하는 </src>` | 1358 |
| 6 | `<src>우상에게로 </src>` | `<src>무상에게로 </src>` | 1435 |
| 7 | `<src>끄는 그대로 </src>` | `<src>가는 그대로 </src>` | 1649 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느라 </src>` | 2720 |
| 9 | `<src><\|wait\|></src>` | `<src>그러니까 </src>` | 697 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그럼 으로 내가 </src>` | 2920 |
| 11 | `<src>너희 에게 </src>` | `<src>너희에게 </src>` | 961 |
| 12 | `<src>알리 노니 </src>` | `<src>알리노니 </src>` | 2018 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님의 영어로 </src>` | 1069 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1022 |
| 15 | `<src><\|wait\|></src>` | `<src>는 </src>` | 452 |

---

### Test Example 43 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>で、これはですね、</src>` | 2275 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1890 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていう開発環境</src>` | 539 |
| 4 | `<src><\|wait\|></src>` | `<src>で、</src>` | 1305 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>Python開発環境なんです。</src>` | 2220 |
| 6 | `<src>というのもフローリフを</src>` | `<src>そういうのも</src>` | 570 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアル</src>` | 1366 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>の書いてあとは</src>` | 1952 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコード</src>` | 1514 |
| 10 | `<src>生成されて、それが</src>` | `<src>を生成して、それが実行</src>` | 1636 |
| 11 | `<src>実行されることで</src>` | `<src>されることで信号処理</src>` | 2261 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が起こらされるっていう。</src>` | 1037 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ところでになっているから</src>` | 1293 |
| 14 | `<src><\|wait\|></src>` | `<src>です。</src>` | 1028 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 1026 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ</src>` | 449 |

---

### Test Example 44 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>穿摩</src>` | 2211 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>和</src>` | 820 |
| 3 | `<src>的感情或</src>` | `<src>敢直</src>` | 1589 |
| 4 | `<src>真实意图的，</src>` | `<src>对手的敢</src>` | 1233 |
| 5 | `<src><\|wait\|></src>` | `<src>情火</src>` | 1008 |
| 6 | `<src><\|wait\|></src>` | `<src>真</src>` | 1809 |
| 7 | `<src>很多时候经常</src>` | `<src>实</src>` | 1077 |
| 8 | `<src>会听到人们</src>` | `<src>好经常会</src>` | 1491 |
| 9 | `<src>这样说：“</src>` | `<src>听人们</src>` | 2181 |
| 10 | `<src>你们看，</src>` | `<src>这样说</src>` | 1094 |
| 11 | `<src>这个人</src>` | `<src>吧，你们看，</src>` | 2894 |
| 12 | `<src>又在说谎了，</src>` | `<src>这个人又</src>` | 480 |
| 13 | `<src>他的眼睛</src>` | `<src>在躲黄了，</src>` | 1918 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>他的眼睛已经</src>` | 1006 |
| 15 | `<src><\|wait\|></src>` | `<src>说明了一切。</src>` | 1076 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 446 |
| 17 | `<src><\|wait\|></src>` | `<src>说</src>` | 649 |

---

### Test Example 45 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1875 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>다른 사람들이 </src>` | 898 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석을 해 놓았습니다. </src>` | 1606 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 </src>` | 1289 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>의 분석을 보시면 </src>` | 1985 |
| 6 | `<src>소니가 </src>` | `<src>소니 가 </src>` | 807 |
| 7 | `<src>26비트 FP </src>` | `<src>유리 룩트 에 </src>` | 1351 |
| 8 | `<src>파이프 를 </src>` | `<src>FPB 파이프 를 </src>` | 2281 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128 비트 로 </src>` | 1372 |
| 10 | `<src>것으로 보인다. </src>` | `<src>나추 가 로 포인트 </src>` | 2995 |
| 11 | `<src><\|wait\|></src>` | `<src>한다. </src>` | 903 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈 에서도 </src>` | 1970 |
| 13 | `<src><\|wait\|></src>` | `<src>없는 인피니트 캐시 </src>` | 406 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>에 </src>` | 1345 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>S2 가 여기 도 없다. </src>` | 898 |
| 16 | `<src><\|wait\|></src>` | `<src>` | 681 |

---

### Test Example 46 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Ah, activity </src>` | 2167 |
| 2 | `<src>Activity than </src>` | `<src>then self </src>` | 930 |
| 3 | `<src>self-defining what we think </src>` | `<src>defining what we think </src>` | 1535 |
| 4 | `<src>the standard is because you're </src>` | `<src>standard is, because </src>` | 1316 |
| 5 | `<src>absolutely correct, </src>` | `<src>you're absolutely correct. </src>` | 1320 |
| 6 | `<src>but the reality </src>` | `<src>But the reality </src>` | 1421 |
| 7 | `<src>is is that </src>` | `<src>is that </src>` | 1119 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new </src>` | 1684 |
| 9 | `<src>block and because the </src>` | `<src>kid block, and because </src>` | 2176 |
| 10 | `<src>standards have </src>` | `<src>the standards have changed. </src>` | 2279 |
| 11 | `<src>changed from 20 </src>` | `<src>Since from </src>` | 1546 |
| 12 | `<src>years ago, </src>` | `<src>twenty years ago, </src>` | 1309 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held </src>` | 1074 |
| 14 | `<src>a higher standard because </src>` | `<src>to our standard, </src>` | 1164 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 1196 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is also to our standard. </src>` | 728 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수가 </src>` | 2082 |
| 2 | `<src><\|wait\|></src>` | `<src>상승 하는 </src>` | 901 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>그름 을 보인 다음에 </src>` | 1571 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 </src>` | 1272 |
| 5 | `<src>큰 폭의 </src>` | `<src>대형 주도 </src>` | 1505 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>어 큰 폭 상승 을 하겠지만 </src>` | 1373 |
| 7 | `<src>먼저 </src>` | `<src>어 먼저 </src>` | 1809 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 종목 </src>` | 2696 |
| 9 | `<src>종목 들이 </src>` | `<src>들이 </src>` | 748 |
| 10 | `<src>먼저 </src>` | `<src>이 먼저 시장 을 </src>` | 3035 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 움직이기 때문에 </src>` | 663 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>항상 </src>` | 1910 |
| 13 | `<src>요 시총이 </src>` | `<src>유동 시 총 이 가벼운 종목 </src>` | 953 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>을 </src>` | 900 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>어 눈으로 봐야 될 것 같습니다. </src>` | 764 |
| 16 | `<src>같습니다. </src>` | `<src>아. </src>` | 757 |

---

### Test Example 48 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2409 |
| 2 | `<src><\|wait\|></src>` | `<src>세모라 </src>` | 856 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 뻔 했어요. </src>` | 1640 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>안 그랬대. </src>` | 1302 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>소름이 돋은 </src>` | 2559 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>차례 돋은 느낌 </src>` | 542 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이 겹을 흔들어서 </src>` | 1965 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 2455 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 </src>` | 1221 |
| 10 | `<src>물릴 거고 </src>` | `<src>오물리 럴 거고 </src>` | 2773 |
| 11 | `<src>신이 오면 </src>` | `<src>기신이 오물리 럴 거고 </src>` | 1205 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>기신이 오물리 럴 거고 </src>` | 1238 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>지 려 주 니까 </src>` | 1625 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 마음 에. </src>` | 729 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 777 |

---

### Test Example 49 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>드러가면 </src>` | 2407 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맨니다. </src>` | 1919 |
| 3 | `<src>운전 을 </src>` | `<src>이 운전은 </src>` | 550 |
| 4 | `<src><\|wait\|></src>` | `<src>거로 </src>` | 1281 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>거로 다니고 </src>` | 2585 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>가는 에 뭐 </src>` | 537 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북으로 가면 </src>` | 1912 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 </src>` | 2356 |
| 9 | `<src><\|wait\|></src>` | `<src>거야. </src>` | 806 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장려리요. </src>` | 3087 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 </src>` | 530 |
| 12 | `<src>대신 에 </src>` | `<src>괜히 에 대신에 이제 </src>` | 1989 |
| 13 | `<src>이제 </src>` | `<src>이제 열심히 </src>` | 995 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>열심히 </src>` | 840 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>노배를 그건 안 한 거 같아요. </src>` | 856 |
| 16 | `<src><\|wait\|></src>` | `<src>예. </src>` | 671 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계소 </src>` | 2259 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 이런 </src>` | 893 |
| 3 | `<src>있습니다. </src>` | `<src>경우 들 습니다. </src>` | 1645 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 A 라는 사람 </src>` | 1327 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>과 B 라는 사람이 </src>` | 1484 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 </src>` | 1243 |
| 7 | `<src><\|wait\|></src>` | `<src>컨설턴트 에 </src>` | 1390 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>B 컨설턴트 에 </src>` | 2407 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>B 라는 사람이 </src>` | 1159 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2972 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>설 었을 때 </src>` | 1088 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라는 사람이 </src>` | 1976 |
| 13 | `<src>실제 </src>` | `<src>실 었을 때 </src>` | 976 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로 사이트 스크 에 서 </src>` | 1306 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>GXP 까지 </src>` | 344 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까 </src>` | 809 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Um, </src>` | 2166 |
| 2 | `<src>Also, </src>` | `<src>also, you will not </src>` | 1823 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 672 |
| 4 | `<src>move media objects </src>` | `<src>media objects </src>` | 1311 |
| 5 | `<src><\|wait\|></src>` | `<src>between the </src>` | 1862 |
| 6 | `<src>between the resources. </src>` | `<src>resources </src>` | 811 |
| 7 | `<src>So, if </src>` | `<src>so if </src>` | 1055 |
| 8 | `<src>you get into </src>` | `<src>you get into the situation </src>` | 1544 |
| 9 | `<src>a situation </src>` | `<src>where you </src>` | 2131 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 1255 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media file </src>` | 2730 |
| 12 | `<src>files to a particular resource, </src>` | `<src>to a particular resource </src>` | 750 |
| 13 | `<src>you need to let us know, </src>` | `<src>to put in the list. </src>` | 1787 |
| 14 | `<src>and we can see about </src>` | `<src>Now, we can see </src>` | 1518 |
| 15 | `<src><\|wait\|></src>` | `<src>about giving those media files </src>` | 851 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>and then making sure </src>` | 739 |
| 17 | `<src>get backed up </src>` | `<src>you get backed up </src>` | 423 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 418 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>For all the </src>` | 1931 |
| 2 | `<src>首次觉知到</src>` | `<src>the </src>` | 798 |
| 3 | `<src>那个现象：</src>` | `<src>the ability to </src>` | 1645 |
| 4 | `<src>每当我们</src>` | `<src>do that, but </src>` | 1356 |
| 5 | `<src><\|wait\|></src>` | `<src>we are </src>` | 1460 |
| 6 | `<src>处于爱之中，</src>` | `<src>in the midst of </src>` | 1307 |
| 7 | `<src>所谓的爱，</src>` | `<src>love, </src>` | 2042 |
| 8 | `<src>我们也</src>` | `<src>we can also </src>` | 2368 |
| 9 | `<src>同时进入恨。</src>` | `<src>enter the </src>` | 753 |
| 10 | `<src><\|wait\|></src>` | `<src>heavenly realm </src>` | 2857 |
| 11 | `<src>在早上的时候，</src>` | `<src>when we are in the heavenly realm, </src>` | 1003 |
| 12 | `<src>它是爱；</src>` | `<src>we can also </src>` | 1955 |
| 13 | `<src>到了晚上，</src>` | `<src>reach the end of the </src>` | 976 |
| 14 | `<src>它就变成恨。</src>` | `<src>love, and it becomes </src>` | 1106 |
| 15 | `<src><\|wait\|></src>` | `<src>that love. </src>` | 450 |
| 16 | `<src>那个钟摆</src>` | `<src>That love. </src>` | 732 |
| 17 | `<src><\|wait\|></src>` | `<src>It continues to </src>` | 445 |
| 18 | `<src>继续在移动。</src>` | `<src>do it. </src>` | 401 |

---

### Test Example 53 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>meaningful </src>` | 2408 |
| 2 | `<src>Meaningful individual </src>` | `<src>individual </src>` | 785 |
| 3 | `<src>right, </src>` | `<src>right, and </src>` | 1567 |
| 4 | `<src>and the Supreme Court </src>` | `<src>Supreme Court </src>` | 341 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 1161 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And </src>` | 1400 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>I thought the courts </src>` | 1377 |
| 8 | `<src><\|wait\|></src>` | `<src>wanted to be </src>` | 1139 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the vanguard of social change. </src>` | 2265 |
| 10 | `<src>change </src>` | `<src>Uh, </src>` | 1403 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 1458 |
| 12 | `<src><\|wait\|></src>` | `<src>but they rather </src>` | 2434 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect the </src>` | 930 |
| 14 | `<src>the consensus </src>` | `<src>consensus </src>` | 1360 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1067 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 1015 |
| 17 | `<src><\|wait\|></src>` | `<src>So, </src>` | 455 |
| 18 | `<src>So you have some </src>` | `<src>you have </src>` | 735 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 414 |
| 20 | `<src><\|wait\|></src>` | `<src>who </src>` | 387 |
| 21 | `<src>who. </src>` | `<src>who </src>` | 315 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point </src>` | 1929 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 930 |
| 3 | `<src>is hungry. </src>` | `<src>is a hungry </src>` | 1475 |
| 4 | `<src>He knows that </src>` | `<src>man. He knows </src>` | 1351 |
| 5 | `<src>he's been without food, </src>` | `<src>that he's </src>` | 1399 |
| 6 | `<src><\|wait\|></src>` | `<src>not willing to sport </src>` | 1406 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>a wild in sport </src>` | 1930 |
| 8 | `<src>And so he says </src>` | `<src>day, that he's hungry. And so he says </src>` | 2963 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 1549 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the son of God, </src>` | 2522 |
| 11 | `<src><\|wait\|></src>` | `<src>prove it. Turn </src>` | 2031 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>these stones to bread. </src>` | 1248 |
| 13 | `<src><\|wait\|></src>` | `<src>How did Jesus </src>` | 1200 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>deal with that </src>` | 555 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 383 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 347 |
| 17 | `<src>Man shall not live </src>` | `<src>genuinely </src>` | 384 |
| 18 | `<src>by bread alone. </src>` | `<src>led by </src>` | 314 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2456 |
| 2 | `<src>in turmoil </src>` | `<src>in the first mile </src>` | 910 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1547 |
| 4 | `<src><\|wait\|></src>` | `<src>about the </src>` | 1180 |
| 5 | `<src>about the EHR fields </src>` | `<src>HR field </src>` | 1085 |
| 6 | `<src><\|wait\|></src>` | `<src>being of critical importance </src>` | 1831 |
| 7 | `<src>being of critical importance </src>` | `<src>versus </src>` | 1009 |
| 8 | `<src>versus variant </src>` | `<src>important versus </src>` | 1563 |
| 9 | `<src><\|wait\|></src>` | `<src>variant database </src>` | 2106 |
| 10 | `<src>databases, </src>` | `<src>which is obviously </src>` | 1173 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>one of my loves. </src>` | 2771 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 666 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree </src>` | 1828 |
| 14 | `<src>upon the fields that need </src>` | `<src>on the fields </src>` | 1125 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these data </src>` | 1300 |
| 16 | `<src>data sources that we can </src>` | `<src>sources that we can </src>` | 774 |
| 17 | `<src>draw from, </src>` | `<src>draw from. There's nothing </src>` | 542 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 390 |
| 19 | `<src><\|wait\|></src>` | `<src>Right? </src>` | 253 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2152 |
| 2 | `<src>它的图片哦，</src>` | `<src>一下</src>` | 920 |
| 3 | `<src><\|wait\|></src>` | `<src>它的图片</src>` | 1445 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>呢，</src>` | 1108 |
| 5 | `<src>的一个是客厅</src>` | `<src>呢我们可以看到</src>` | 387 |
| 6 | `<src>的部分。</src>` | `<src>一个</src>` | 1404 |
| 7 | `<src>那客厅一般</src>` | `<src>是克汀的部分。</src>` | 1326 |
| 8 | `<src>都是属于</src>` | `<src>克汀一般是属于</src>` | 2098 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 2165 |
| 10 | `<src>在休息的地方，</src>` | `<src>在修饰的地方，</src>` | 835 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 2820 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的部分。</src>` | 1004 |
| 13 | `<src>也会反映的是</src>` | `<src>它会反映的是</src>` | 2082 |
| 14 | `<src>你需要给自己</src>` | `<src>需要给</src>` | 1077 |
| 15 | `<src>一点时间，</src>` | `<src>自己一点时间</src>` | 1163 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好地做。</src>` | 409 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>下洗去，</src>` | 724 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们看到</src>` | 384 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>这边是</src>` | 400 |
| 20 | `<src>啊，</src>` | `<src>非常五一人的嘛。</src>` | 312 |
| 21 | `<src>所以是说。</src>` | `<src>好，所以</src>` | 274 |

---

### Test Example 57 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1950 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare. </src>` | 964 |
| 3 | `<src>and they often </src>` | `<src>And they often </src>` | 1478 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1244 |
| 5 | `<src><\|wait\|></src>` | `<src>completely revolutionize </src>` | 1127 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>the world. </src>` | 1745 |
| 7 | `<src><\|wait\|></src>` | `<src>The personality </src>` | 1764 |
| 8 | `<src>Their personality is </src>` | `<src>is something </src>` | 2295 |
| 9 | `<src>something of a </src>` | `<src>of a contradiction. </src>` | 951 |
| 10 | `<src>contradiction. </src>` | `<src>Well, </src>` | 2237 |
| 11 | `<src>While they're </src>` | `<src>they're extroverted, </src>` | 1765 |
| 12 | `<src>extroverted, </src>` | `<src>they also </src>` | 1913 |
| 13 | `<src>they also hate </src>` | `<src>hate meaningless </src>` | 655 |
| 14 | `<src>meaningless conversations </src>` | `<src>conversations. </src>` | 1267 |
| 15 | `<src>and like to </src>` | `<src>And like </src>` | 662 |
| 16 | `<src><\|wait\|></src>` | `<src>they get straight to the </src>` | 720 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 276 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 302 |
| 19 | `<src>play </src>` | `<src>to play the devil's advocate, </src>` | 500 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and </src>` | 213 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy away </src>` | 255 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 291 |
| 23 | `<src><\|wait\|></src>` | `<src>E and </src>` | 275 |
| 24 | `<src><\|wait\|></src>` | `<src>CP stands </src>` | 265 |
| 25 | `<src>ENTP stands for </src>` | `<src>for </src>` | 218 |

---

### Test Example 58 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전의 이준석은</src>` | 2060 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>정무를 거부한</src>` | 1884 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분이</src>` | 546 |
| 4 | `<src>위해서 라면서 </src>` | `<src>후보를 위해서</src>` | 1260 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>하면서 후보의 당선을</src>` | 1439 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서</src>` | 1366 |
| 7 | `<src>제법 생색까지 </src>` | `<src>세 배까지 냈지만</src>` | 1869 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>이제는</src>` | 2193 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보가</src>` | 1002 |
| 10 | `<src>김종인 을 </src>` | `<src>김정은을</src>` | 2776 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제관 순간</src>` | 1131 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들으내 놓고</src>` | 1841 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보를</src>` | 362 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리겠다는</src>` | 1540 |
| 15 | `<src><\|wait\|></src>` | `<src>도끼를 품은</src>` | 819 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격성을</src>` | 853 |
| 17 | `<src><\|wait\|></src>` | `<src>보이기로</src>` | 401 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한</src>` | 391 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다.</src>` | 303 |
| 20 | `<src><\|wait\|></src>` | `<src>가 선발 이준석은</src>` | 298 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>성상 납권</src>` | 300 |
| 22 | `<src><\|wait\|></src>` | `<src>이</src>` | 266 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당이</src>` | 305 |
| 24 | `<src><\|wait\|></src>` | `<src>공격에 얼마나</src>` | 227 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까?</src>` | 262 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ </src>` | 2219 |
| 2 | `<src>食堂ね</src>` | `<src>食 の 今 作っ て </src>` | 965 |
| 3 | `<src>今作ってる</src>` | `<src>みたい です 。 </src>` | 1532 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>な の で 、 ここ の </src>` | 1423 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src> の ホテル </src>` | 1402 |
| 6 | `<src>も</src>` | `<src> の 、 朝食 が </src>` | 1341 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src> 食べれる 場所 </src>` | 1221 |
| 8 | `<src>になってる</src>` | `<src> に なっ てる </src>` | 1915 |
| 9 | `<src>予定になってるので</src>` | `<src> 予定 に なっ てる の で 、 </src>` | 1865 |
| 10 | `<src>今後ねここ</src>` | `<src> 今後 ね 、 ここ </src>` | 2868 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src> ゴー ドストン ホテル </src>` | 1057 |
| 12 | `<src>泊まってみたい</src>` | `<src> 泊まっ て み たい な と </src>` | 1930 |
| 13 | `<src>なっていう方はですね</src>` | `<src> 思っ た 方 は です ね 、 </src>` | 575 |
| 14 | `<src>検討なさってみて</src>` | `<src> 転落 さ て </src>` | 1350 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src> 見 て 、 まあ 、 いい ん じゃ ない </src>` | 802 |
| 16 | `<src><\|wait\|></src>` | `<src> な と 、 はい 。 </src>` | 764 |
| 17 | `<src>なとはい思いますここ</src>` | `<src> 思い ます 。 </src>` | 389 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src> ここ の ホテル から です ね 、 </src>` | 470 |
| 19 | `<src>駅ももう</src>` | `<src> アップ サン 駅 も </src>` | 274 |
| 20 | `<src><\|wait\|></src>` | `<src> ある い て </src>` | 249 |
| 21 | `<src>歩いて一分</src>` | `<src> 1 分 かかる か </src>` | 310 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src> かん ない か 、 そんな </src>` | 296 |
| 23 | `<src>レベルのね</src>` | `<src> で の ね 、 立地 の </src>` | 321 |
| 24 | `<src>立地のいいねまあ</src>` | `<src> いい ね 、 まあ 、 ホテル </src>` | 245 |
| 25 | `<src>ホテルになってますので</src>` | `<src> なっ て ます の で 、 </src>` | 258 |
| 26 | `<src>よかったらですね</src>` | `<src> 欲かっ たら です ね 、 </src>` | 298 |
| 27 | `<src>ご検討なさってみて</src>` | `<src> ここ に 転落 さっ て み てく </src>` | 274 |
| 28 | `<src>ください</src>` | `<src> なさい 。 それ が </src>` | 244 |
| 29 | `<src>それではですね今回は。</src>` | `<src> ね 、 今回 は </src>` | 223 |

---

### Test Example 60 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어</src>` | 2302 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어` | 15265 |
| 3 | `<src>가장 20대를 </src>` | `<src>어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어, 어` | 7458 |
| 4 | `<src><\|wait\|></src>` | `<src>20대를 함께 한</src>` | 249 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자</src>` | 284 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇다고</src>` | 202 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아.</src>` | 247 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까</src>` | 140 |
| 9 | `<src><\|wait\|></src>` | `<src>어, 제인 건</src>` | 249 |
| 10 | `<src>책임감 보다는 </src>` | `<src>뭐라는 </src>` | 186 |
| 11 | `<src>조금 </src>` | `<src>저 그런 자기 스스로</src>` | 146 |
| 12 | `<src>자기 스스로 </src>` | `<src>수술을</src>` | 196 |
| 13 | `<src><\|wait\|></src>` | `<src>좀</src>` | 198 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 건</src>` | 146 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려 놓고</src>` | 122 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다고</src>` | 152 |
