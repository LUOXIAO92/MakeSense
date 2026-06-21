# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9471
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4106
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
  - PROCESS_TIME_MS_AVG: 1422.4000
  - PROCESS_TIME_MS_P50: 1433.9170
  - PROCESS_TIME_MS_P95: 2118.3880
  - PROCESS_TIME_MS_MAX: 2363.8370

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
| 1 | `<src><\|wait\|></src>` | `<src>快在哪里</src>` | 2188 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>停点，</src>` | 1450 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个收益也很大。</src>` | 1022 |
| 4 | `<src>然后</src>` | `<src><\|wait\|></src>` | 770 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 941 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放假</src>` | 1628 |
| 7 | `<src>儿核桃</src>` | `<src>隔热汤</src>` | 995 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1573 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>人，感觉</src>` | 1437 |
| 10 | `<src>这种核桃</src>` | `<src>这种隔热汤</src>` | 1345 |
| 11 | `<src>仁儿。</src>` | `<src>啊，</src>` | 1698 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要气熟</src>` | 2007 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>是容易的，</src>` | 1473 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1078 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 776 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 929 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1707 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 1326 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2044 |
| 9 | `<src>虚阿凡</src>` | `<src>需要凡</src>` | 641 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 1742 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父，</src>` | 1780 |

---

### Test Example 3 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying important </src>` | 1833 |
| 2 | `<src>Did very important research </src>` | `<src>research </src>` | 1372 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 955 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1212 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 735 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 1677 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 1308 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1894 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 832 |
| 10 | `<src>out there, </src>` | `<src>out there, people with </src>` | 1903 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 1966 |

---

### Test Example 4 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1744 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1416 |
| 3 | `<src>これなんかまだ</src>` | `<src>この中まだ</src>` | 1246 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1276 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 499 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1583 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1374 |
| 8 | `<src><\|wait\|></src>` | `<src>こうタイズして</src>` | 2099 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>おけると</src>` | 678 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 2064 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1908 |

---

### Test Example 5 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要</src>` | 2099 |
| 2 | `<src>家长需要做的是，</src>` | `<src>做的是</src>` | 1430 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1379 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深沉的</src>` | 1280 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1388 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 624 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1331 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 2213 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1077 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心的陪伴</src>` | 1763 |
| 11 | `<src>慢慢长大。</src>` | `<src>长大。</src>` | 2045 |

---

### Test Example 6 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>淘撒完以后的</src>` | 2081 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>呢，</src>` | 1377 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力</src>` | 1365 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也Swan了</src>` | 1275 |
| 5 | `<src>然后</src>` | `<src>了，</src>` | 1209 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 814 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1419 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的运行状态。</src>` | 2214 |
| 9 | `<src>状态，</src>` | `<src><\|wait\|></src>` | 1148 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是</src>` | 1790 |
| 11 | `<src>抑郁状态。</src>` | `<src>所谓的异于状态。</src>` | 1919 |

---

### Test Example 7 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1836 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Abbot, </src>` | 1464 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발시키고 </src>` | 1404 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1264 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1617 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 970 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>며느라 </src>` | 1553 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1462 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1258 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 1869 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>있습니다. </src>` | 1884 |

---

### Test Example 8 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2129 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 1356 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 976 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 892 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 951 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1691 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1219 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります。</src>` | 1615 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1028 |
| 10 | `<src><\|wait\|></src>` | `<src>連絡の</src>` | 1256 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>詳細の案内があります</src>` | 1870 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>のでもう少々お待ちください。</src>` | 1970 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1987 |
| 2 | `<src>옹심이, </src>` | `<src>공심이 </src>` | 1471 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1343 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼공심이 </src>` | 1268 |
| 5 | `<src>옹심이가 </src>` | `<src>어설공심이가 </src>` | 1627 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 547 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. 야 </src>` | 2128 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 1431 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1346 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해행으로 </src>` | 1778 |
| 11 | `<src>진짜. </src>` | `<src>조금씩 움직입니다, 저. </src>` | 2082 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>面对这个情况，</src>` | 1896 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>我们就是</src>` | 1390 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1251 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1390 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1389 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们笑这个状况，</src>` | 702 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1558 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 2116 |
| 9 | `<src>独立承担。</src>` | `<src>不理成单，</src>` | 1686 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1462 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该做的事情。</src>` | 2138 |

---

### Test Example 11 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2181 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성들은 </src>` | 1439 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1209 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1331 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 663 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1485 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성들이 </src>` | 1636 |
| 8 | `<src>때문 입니다. </src>` | `<src>없기 때문 입니다. </src>` | 2054 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1531 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 1563 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은 </src>` | 2251 |

---

### Test Example 12 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1734 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 1435 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1275 |
| 4 | `<src><\|wait\|></src>` | `<src>之间有着某种</src>` | 783 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>联系，</src>` | 711 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1636 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1162 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始</src>` | 1844 |
| 9 | `<src><\|wait\|></src>` | `<src>的？</src>` | 1024 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1741 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1509 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 2110 |

---

### Test Example 13 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1942 |
| 2 | `<src><\|wait\|></src>` | `<src>너무 좋은 </src>` | 1437 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>일 수도 있지만 </src>` | 1037 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요. </src>` | 1205 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 의 </src>` | 637 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 </src>` | 1873 |
| 7 | `<src>뭐 있고 </src>` | `<src>풀어보이 고 나만 </src>` | 1665 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>자기 보살 로 </src>` | 1980 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보이 풀려고 </src>` | 1405 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 가 지금 나한테 보살 이라는 </src>` | 1972 |
| 11 | `<src>보살 이라는데. </src>` | `<src><\|wait\|></src>` | 2202 |

---

### Test Example 14 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1699 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1469 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活的一个轨道，</src>` | 1221 |
| 4 | `<src>的一个轨道哈，</src>` | `<src><\|wait\|></src>` | 879 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 617 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好自在的</src>` | 1661 |
| 7 | `<src>在做热汤</src>` | `<src>时候，在工作、</src>` | 1355 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>谈恋爱，去生活</src>` | 1986 |
| 9 | `<src><\|wait\|></src>` | `<src>的，我当时</src>` | 803 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被动的东西</src>` | 1805 |
| 11 | `<src>小小的愿望</src>` | `<src>一个小小的一个愿望</src>` | 1866 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1784 |

---

### Test Example 15 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1738 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1405 |
| 3 | `<src>Drop into </src>` | `<src>Drop into your body. </src>` | 1464 |
| 4 | `<src>your body. </src>` | `<src>Where does the </src>` | 1207 |
| 5 | `<src>Where does the tension </src>` | `<src>tension </src>` | 1586 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1014 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 1744 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 1536 |
| 9 | `<src>I ask them what </src>` | `<src>Or is the body </src>` | 1789 |
| 10 | `<src><\|wait\|></src>` | `<src>landing page </src>` | 1732 |
| 11 | `<src>language are you using? </src>` | `<src>you use? </src>` | 1959 |

---

### Test Example 16 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2150 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1455 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. Learn to </src>` | 1335 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>reinforce. </src>` | 1226 |
| 5 | `<src>Find what you're good at </src>` | `<src>Repeat five times. By that, you're good at </src>` | 1793 |
| 6 | `<src>and do more of it. </src>` | `<src>and you more of it. </src>` | 1359 |
| 7 | `<src><\|wait\|></src>` | `<src>And when you're not </src>` | 2113 |
| 8 | `<src>And what you're not good at, </src>` | `<src>good at it, </src>` | 703 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with it. </src>` | 2130 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1982 |
| 11 | `<src>And until next time. </src>` | `<src>And and tell next time, </src>` | 2208 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そう</src>` | 1872 |
| 2 | `<src>そこで</src>` | `<src>です。そこで</src>` | 1463 |
| 3 | `<src><\|wait\|></src>` | `<src>天気</src>` | 1109 |
| 4 | `<src>テキという設備寺が</src>` | `<src>の設備が</src>` | 776 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたが、</src>` | 922 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1562 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1195 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井氏の仕組み</src>` | 1912 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 800 |
| 10 | `<src>は五経、</src>` | `<src>五個、</src>` | 1151 |
| 11 | `<src><\|wait\|></src>` | `<src>設備が</src>` | 1845 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 1855 |
| 13 | `<src>です。</src>` | `<src>五つです。</src>` | 1956 |

---

### Test Example 18 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1826 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1438 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1215 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1297 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 587 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1489 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1372 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 2254 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 1238 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1878 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1947 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1887 |

---

### Test Example 19 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>다른 </src>` | 1875 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>산지 를 </src>` | 1444 |
| 3 | `<src>해가지고 내가 </src>` | `<src>죽여 달라 해가지고 내가 </src>` | 1453 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 는 것투로 </src>` | 1424 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>와서 나 다른 잔찜의 </src>` | 1828 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1361 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해달라 는 거야. 내가 </src>` | 2325 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그런 소리 안 듣고 있는 </src>` | 1856 |
| 9 | `<src><\|wait\|></src>` | `<src>주변 에서. </src>` | 1527 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 2042 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1407 |

---

### Test Example 20 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2063 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1479 |
| 3 | `<src>始めた</src>` | `<src><\|wait\|></src>` | 1219 |
| 4 | `<src>もので、</src>` | `<src>始めたもので、</src>` | 1281 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 603 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1522 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1413 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 2212 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1142 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の絵</src>` | 1985 |
| 11 | `<src>は、田舎の</src>` | `<src><\|wait\|></src>` | 1878 |
| 12 | `<src>中学生でも。</src>` | `<src>は田舎の中学生でも。</src>` | 1901 |

---

### Test Example 21 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだん</src>` | 2230 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が</src>` | 1436 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ</src>` | 1384 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>をシャーラーが</src>` | 1259 |
| 5 | `<src>多いですね。</src>` | `<src>出たがれっぽいですね。</src>` | 1651 |
| 6 | `<src>開業したい方って</src>` | `<src>回避したい方って</src>` | 1013 |
| 7 | `<src>すごい</src>` | `<src>すごい息追いしきったが</src>` | 2013 |
| 8 | `<src>自己意識高いし、</src>` | `<src>し、</src>` | 1015 |
| 9 | `<src>自分で</src>` | `<src>右にやめて</src>` | 1750 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>ととモンテニアトボトシャー</src>` | 1770 |
| 11 | `<src>傾向が強いので、</src>` | `<src>これが強いので、</src>` | 2137 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1314 |

---

### Test Example 22 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name's </src>` | 1936 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel, </src>` | 1458 |
| 3 | `<src>I am currently </src>` | `<src>and I'm currently studying </src>` | 1466 |
| 4 | `<src><\|wait\|></src>` | `<src>a BA in </src>` | 1221 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>Business Finance </src>` | 1577 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a BSc in Psychology. </src>` | 1109 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1597 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the U of </src>` | 1429 |
| 9 | `<src><\|wait\|></src>` | `<src>Edinburgh, </src>` | 1728 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and the future I want to go into </src>` | 1724 |
| 11 | `<src><\|wait\|></src>` | `<src>is corporate consultancy </src>` | 2094 |
| 12 | `<src>corporate consultancy. </src>` | `<src>and </src>` | 1353 |

---

### Test Example 23 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1877 |
| 2 | `<src><\|wait\|></src>` | `<src>选择二击</src>` | 1474 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>状态，</src>` | 890 |
| 4 | `<src>服务</src>` | `<src>排除了</src>` | 761 |
| 5 | `<src>在一级一线</src>` | `<src>在一击一线</src>` | 1055 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1810 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说</src>` | 1196 |
| 8 | `<src><\|wait\|></src>` | `<src>在做微</src>` | 1996 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>信封高手几点，你可以</src>` | 880 |
| 10 | `<src>发现</src>` | `<src>发觉</src>` | 1758 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信封平分</src>` | 1912 |
| 12 | `<src>的新榜反而</src>` | `<src>的辛膀</src>` | 1977 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1302 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2118 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 1392 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 961 |
| 4 | `<src>緩むと芯が</src>` | `<src>遊ぶと、</src>` | 856 |
| 5 | `<src><\|wait\|></src>` | `<src>シンガーが起き上がれなくなってしまう</src>` | 1278 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1525 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1308 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1989 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 781 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついてるっていうこと</src>` | 1937 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 1748 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 2105 |
| 13 | `<src>分解完了。</src>` | `<src>はい分解を。</src>` | 1348 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2165 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 1633 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment, </src>` | 1015 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 883 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 747 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1680 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1312 |
| 8 | `<src>change can happen </src>` | `<src>happen in the </src>` | 2166 |
| 9 | `<src>in the United States. </src>` | `<src>United States. </src>` | 672 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1954 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1921 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 2190 |
| 13 | `<src>myriad. </src>` | `<src>are Miriam. </src>` | 1529 |

---

### Test Example 26 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1830 |
| 2 | `<src>映画でですね、</src>` | `<src>Aがでですね、</src>` | 1673 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1154 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>A生息可能かどうかっていうの</src>` | 1642 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1651 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>Aの卵を</src>` | 1418 |
| 7 | `<src>ことで、あの</src>` | `<src>調べそこで</src>` | 1940 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>A生息可能かどうかっていうの</src>` | 721 |
| 9 | `<src>保証する、生息である</src>` | `<src>調査する、生息調査</src>` | 2170 |
| 10 | `<src>ことを保証する</src>` | `<src>ということを保証する</src>` | 2140 |
| 11 | `<src>といったような</src>` | `<src>といったら、その使い方をされます。</src>` | 1901 |
| 12 | `<src>使い方をされます。</src>` | `<src><\|wait\|></src>` | 1616 |

---

### Test Example 27 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2187 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1434 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1358 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1227 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 865 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1271 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1751 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1703 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1021 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1740 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2118 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game dot sort array. </src>` | 2093 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1427 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1925 |
| 2 | `<src>一切正常，</src>` | `<src>也很正常，</src>` | 1452 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>我反复乱跳，</src>` | 1475 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1207 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持不开刀，</src>` | 1624 |
| 6 | `<src>期间</src>` | `<src>切肩大概</src>` | 845 |
| 7 | `<src>大概有十位医生</src>` | `<src>有十万医生来</src>` | 1685 |
| 8 | `<src>来诊断，</src>` | `<src>审断，</src>` | 1556 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 1544 |
| 10 | `<src>一下提腿，</src>` | `<src>以下踢腿，</src>` | 1618 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1983 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 1649 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的离开。</src>` | 1468 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1988 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1426 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1321 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1314 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1590 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 878 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 1548 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1856 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1821 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 1924 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2112 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't know. </src>` | 1949 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1012 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>达到了一个</src>` | 1739 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>天头，</src>` | 1451 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1008 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了天头之后，</src>` | 995 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 862 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1549 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1420 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说哎，那我</src>` | 2217 |
| 9 | `<src><\|wait\|></src>` | `<src>再继续操作</src>` | 638 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦，</src>` | 1997 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1949 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 2121 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1629 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 982 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1839 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们看到的是</src>` | 1416 |
| 3 | `<src>一个在钓鱼</src>` | `<src><\|wait\|></src>` | 1210 |
| 4 | `<src>的人，但是</src>` | `<src>一个在跳舞的人，但是他是</src>` | 1300 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>为了逆向的，</src>` | 721 |
| 6 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1328 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>这通场吗这样的一个状况</src>` | 1441 |
| 8 | `<src>时候，就要去</src>` | `<src>的，需要去特别</src>` | 2199 |
| 9 | `<src>特别注意，</src>` | `<src>注意的是</src>` | 1056 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能够</src>` | 1828 |
| 11 | `<src>钓到鱼，</src>` | `<src>得到</src>` | 1938 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与他跳不到</src>` | 1826 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1548 |
| 14 | `<src>的意思哦。</src>` | `<src>与你的意识。</src>` | 1028 |

---

### Test Example 32 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 1875 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>이것 들은 거진 </src>` | 1751 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1120 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 1381 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 일어날 정도 의 </src>` | 1873 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>굉장히 </src>` | 1464 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 1993 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 910 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 1677 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 2059 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2044 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1615 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1046 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2071 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 1377 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 1395 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1268 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1525 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 505 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1484 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊、</src>` | 2070 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 1044 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你</src>` | 1671 |
| 11 | `<src><\|wait\|></src>` | `<src>期间就眼变出来。</src>` | 2135 |
| 12 | `<src>演变出来的，</src>` | `<src><\|wait\|></src>` | 2020 |
| 13 | `<src>因此会建议</src>` | `<src>因此，</src>` | 1471 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>会建议属鸡的朋友呢，</src>` | 1136 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1756 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>백오십 한계가 </src>` | 1785 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중업에서 열 명 미만 으로 </src>` | 1255 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1275 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1608 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1397 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2342 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 해외 로 </src>` | 1194 |
| 9 | `<src>걷게 되는데 </src>` | `<src>익을 꺾게 되는데 </src>` | 1973 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업 들은 </src>` | 1942 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1838 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>패배 도 하지 않는 </src>` | 1542 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1247 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new, </src>` | 1949 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1453 |
| 3 | `<src><\|wait\|></src>` | `<src>there were </src>` | 1209 |
| 4 | `<src>such interfaces before, </src>` | `<src>such instances before </src>` | 1282 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 545 |
| 6 | `<src>netfilter, TC. </src>` | `<src>that future TC </src>` | 1525 |
| 7 | `<src>Yeah, so </src>` | `<src>I </src>` | 1264 |
| 8 | `<src>this is just </src>` | `<src>said," </src>` | 2001 |
| 9 | `<src>one another place </src>` | `<src>This is just one another place </src>` | 826 |
| 10 | `<src>to look at. </src>` | `<src>where </src>` | 1861 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1822 |
| 12 | `<src><\|wait\|></src>` | `<src>but </src>` | 2021 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers would </src>` | 1429 |
| 14 | `<src>working on BugRepo </src>` | `<src>think of a bug report </src>` | 1052 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that." </src>` | 1261 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1730 |
| 2 | `<src>HTML이라고 </src>` | `<src>HTML이라고 </src>` | 1404 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 975 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>하는 컴퓨터 도 이해 할 수 </src>` | 1108 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 829 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 </src>` | 1802 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1435 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 2294 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1715 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1561 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 2140 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1478 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1393 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1151 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1134 |

---

### Test Example 37 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2061 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう寝かせている</src>` | 1435 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 932 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 794 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>火事を見ている</src>` | 1150 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1664 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1360 |
| 8 | `<src><\|wait\|></src>` | `<src>超えている</src>` | 1972 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈火勢気</src>` | 772 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1858 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1761 |
| 12 | `<src>船大工をやってる</src>` | `<src>船出を行ってる</src>` | 2014 |
| 13 | `<src>が、</src>` | `<src><\|wait\|></src>` | 1276 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1250 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1123 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 1072 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2152 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1404 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1103 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 770 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 974 |
| 6 | `<src>that I think are </src>` | `<src>that I really </src>` | 1727 |
| 7 | `<src>really important. </src>` | `<src>appreciate </src>` | 1275 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2084 |
| 9 | `<src>I'm going to go into. </src>` | `<src>and I'm going to go into </src>` | 745 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 2108 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 1905 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 2045 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one </src>` | 1741 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1051 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1397 |

---

### Test Example 39 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2171 |
| 2 | `<src><\|wait\|></src>` | `<src>숨을 </src>` | 1387 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>아래 빌 거야. </src>` | 1097 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 돋든 </src>` | 1354 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>가시 리 돋든 </src>` | 623 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 너무 야. </src>` | 1712 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1565 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 2074 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 너무 </src>` | 1359 |
| 10 | `<src>물릴 거고 </src>` | `<src>불릴 거고 </src>` | 1786 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 너무 야 </src>` | 1851 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1913 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주니까 </src>` | 1404 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1211 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1104 |

---

### Test Example 40 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2071 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1468 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1380 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1177 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 1428 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 697 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1899 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you </src>` | 1782 |
| 9 | `<src>to college, </src>` | `<src>go to college, </src>` | 1902 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 1978 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level </src>` | 2082 |
| 12 | `<src>attainment. </src>` | `<src>of attainment. </src>` | 1381 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1092 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1227 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1051 |

---

### Test Example 41 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1829 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1863 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1025 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1251 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1670 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1347 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1876 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 938 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1903 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1826 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 2041 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1607 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 987 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1171 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1041 |

---

### Test Example 42 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1955 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1728 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 1067 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较精神正财的部分</src>` | 1403 |
| 5 | `<src>也就是</src>` | `<src><\|wait\|></src>` | 1573 |
| 6 | `<src>在事业方面的</src>` | `<src>又受到市府方面的业绩</src>` | 1476 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>带来的红利，</src>` | 2042 |
| 8 | `<src>与收入的</src>` | `<src>以及收入的提升、</src>` | 772 |
| 9 | `<src>提升。如果是在</src>` | `<src>如果</src>` | 1902 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面</src>` | 1929 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1919 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错的，只是</src>` | 1609 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说，</src>` | 1166 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了一点点</src>` | 1302 |
| 15 | `<src><\|wait\|></src>` | `<src>。</src>` | 858 |

---

### Test Example 43 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>授業</src>` | 1977 |
| 2 | `<src>十一二手とか</src>` | `<src>一日二日とか</src>` | 1481 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>ですと恐らく</src>` | 1246 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1266 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 489 |
| 6 | `<src>一秒に</src>` | `<src>一日一に</src>` | 1593 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一日一今日ぐらいの</src>` | 1375 |
| 8 | `<src>計算ですか</src>` | `<src>せっかんですかね。</src>` | 2210 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 936 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1767 |
| 11 | `<src>おそらく</src>` | `<src>恐ろしく</src>` | 1954 |
| 12 | `<src><\|wait\|></src>` | `<src>一日二日</src>` | 1906 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1405 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1050 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮本とかが</src>` | 1113 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 1053 |

---

### Test Example 44 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2095 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 1454 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1387 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 이제 </src>` | 1233 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1251 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 고 같은 </src>` | 820 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>동생 이잖아. </src>` | 1418 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1977 |
| 9 | `<src><\|wait\|></src>` | `<src>저희 가 </src>` | 626 |
| 10 | `<src>책임감 보다는 </src>` | `<src>뭐다 는 </src>` | 1933 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 1941 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 2001 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1485 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1064 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1052 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1413 |

---

### Test Example 45 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어 가면 </src>` | 2152 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 해맨입니다. </src>` | 1809 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1012 |
| 4 | `<src><\|wait\|></src>` | `<src>하고 온 </src>` | 1192 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>거로 거로 다녀 </src>` | 755 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>이건데 </src>` | 1277 |
| 7 | `<src>강북 을 가면 </src>` | `<src>막굴 가면 </src>` | 1291 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 2133 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장렬이에요. </src>` | 780 |
| 10 | `<src>또 장렬이에요. </src>` | `<src><\|wait\|></src>` | 2089 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 챙겨 야 </src>` | 2181 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1884 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1551 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>무뤄요. 그거 는 </src>` | 1122 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>나인 것 같아요. </src>` | 1317 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 747 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2075 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1616 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうだけじゃなくて、</src>` | 1258 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルパイソン開発</src>` | 1355 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>環境なんですね。</src>` | 1571 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも、</src>` | 1257 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルの書いてあと</src>` | 2076 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それは</src>` | 817 |
| 9 | `<src>にそこから</src>` | `<src>パイソンコードがそっから生成される</src>` | 2046 |
| 10 | `<src>生成されて、それが</src>` | `<src>っていうそれが</src>` | 1838 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 2009 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われる</src>` | 1600 |
| 13 | `<src>構造になっているからです。</src>` | `<src>っていう構造になっているからですね。</src>` | 1055 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1046 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 988 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ、</src>` | 574 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 2052 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1394 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들이 있습니다. 저희 가 </src>` | 1324 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 999 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 616 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트 예요. </src>` | 1896 |
| 7 | `<src><\|wait\|></src>` | `<src>이게 컨설턴트 예요. </src>` | 2364 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>그리고 A라는 </src>` | 1265 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1749 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1620 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>들여 쓸 때 </src>` | 2220 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라는 사람 이 </src>` | 1423 |
| 13 | `<src>실제 </src>` | `<src>실제 크로스사이트 </src>` | 1407 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크리티에서 </src>` | 1159 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 1153 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 649 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1727 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1486 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놨습니다. </src>` | 1509 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 1066 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>로쿠자 의 분석 을 보시면 </src>` | 1635 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 624 |
| 7 | `<src>26비트 FP </src>` | `<src>유력 히트할 </src>` | 1947 |
| 8 | `<src>파이프 를 </src>` | `<src>FPD 파이프 를 </src>` | 1716 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 1909 |
| 10 | `<src>것으로 보인다. </src>` | `<src>나충가서 </src>` | 1843 |
| 11 | `<src><\|wait\|></src>` | `<src>보인다. </src>` | 2068 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈, X에서도 없는 </src>` | 1662 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 968 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시, </src>` | 1259 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>LSi가 여기 도 없다. </src>` | 1326 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 263 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>锤磨</src>` | 2029 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>或砍之对手的</src>` | 1671 |
| 3 | `<src>的感情或</src>` | `<src>感觉</src>` | 918 |
| 4 | `<src>真实意图的，</src>` | `<src>或真实意图的，</src>` | 1244 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 488 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1623 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常会</src>` | 1371 |
| 8 | `<src>会听到人们</src>` | `<src>听到人们这样说：“</src>` | 2333 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1083 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1794 |
| 11 | `<src>这个人</src>` | `<src>这个人又在</src>` | 2001 |
| 12 | `<src>又在说谎了，</src>` | `<src>作荒了，</src>` | 1834 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛已经</src>` | 1610 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>说明了一切。”</src>` | 1021 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1108 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 961 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 609 |

---

### Test Example 50 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>Fourth of the </src>` | 1789 |
| 2 | `<src>首次觉知到</src>` | `<src>month, </src>` | 1409 |
| 3 | `<src>那个现象：</src>` | `<src>which is the sign of </src>` | 1254 |
| 4 | `<src>每当我们</src>` | `<src>me. </src>` | 978 |
| 5 | `<src><\|wait\|></src>` | `<src>Mei Danwu </src>` | 623 |
| 6 | `<src>处于爱之中，</src>` | `<src>chúy爱之</src>` | 1681 |
| 7 | `<src>所谓的爱，</src>` | `<src>中属位的爱，</src>` | 1430 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 2043 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时</src>` | 667 |
| 10 | `<src><\|wait\|></src>` | `<src>进入恨，</src>` | 1905 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上</src>` | 1790 |
| 12 | `<src>它是爱；</src>` | `<src>的时候它撒爱。</src>` | 2071 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1490 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成</src>` | 909 |
| 15 | `<src><\|wait\|></src>` | `<src>恨，</src>` | 1107 |
| 16 | `<src>那个钟摆</src>` | `<src>那个中百，</src>` | 1067 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 672 |
| 18 | `<src>继续在移动。</src>` | `<src>移动。</src>` | 577 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1932 |
| 2 | `<src><\|wait\|></src>` | `<src>상승 하는 </src>` | 1389 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 1550 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형 주도 </src>` | 1308 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1619 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 </src>` | 1383 |
| 7 | `<src>먼저 </src>` | `<src>하겠지만 먼저 </src>` | 2039 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 690 |
| 9 | `<src>종목 들이 </src>` | `<src>가벼운 종목 들이 </src>` | 2043 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2008 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 움직이 기 때문 에 </src>` | 2268 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src><\|wait\|></src>` | 1653 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 시총이 가벼운 </src>` | 1248 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>종목 을 </src>` | 1104 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨봐야 </src>` | 736 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 613 |

---

### Test Example 52 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1979 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1464 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1393 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 1316 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 1692 |
| 6 | `<src>but the reality </src>` | `<src><\|wait\|></src>` | 1310 |
| 7 | `<src>is is that </src>` | `<src>But the reality is is that </src>` | 1982 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on </src>` | 882 |
| 9 | `<src>block and because the </src>` | `<src>the block, and because </src>` | 1971 |
| 10 | `<src>standards have </src>` | `<src>the standards have changed, </src>` | 1978 |
| 11 | `<src>changed from 20 </src>` | `<src><\|wait\|></src>` | 1921 |
| 12 | `<src>years ago, </src>` | `<src>from twenty years ago, </src>` | 1806 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1098 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1238 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point is </src>` | 999 |
| 16 | `<src>held to a higher standard. </src>` | `<src>being held to a higher standard </src>` | 680 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point </src>` | 1806 |
| 2 | `<src>he knows Jesus </src>` | `<src>in those Jesus </src>` | 1400 |
| 3 | `<src>is hungry. </src>` | `<src>was hungry, </src>` | 1224 |
| 4 | `<src>He knows that </src>` | `<src>he knows that </src>` | 1297 |
| 5 | `<src>he's been without food, </src>` | `<src>he knows that </src>` | 595 |
| 6 | `<src><\|wait\|></src>` | `<src>for even in the wilderness, </src>` | 1597 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>sporty day, he's hungry, </src>` | 2198 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 1513 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 1771 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it </src>` | 2081 |
| 11 | `<src><\|wait\|></src>` | `<src>by </src>` | 1762 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>turning these stones to bread. </src>` | 1564 |
| 13 | `<src><\|wait\|></src>` | `<src>How did Jesus </src>` | 1139 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>deal with that </src>` | 1050 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 1129 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 750 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lived by </src>` | 607 |
| 18 | `<src>by bread alone. </src>` | `<src>rain alone. </src>` | 464 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2008 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 1418 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to move </src>` | 1585 |
| 4 | `<src>move media objects </src>` | `<src>me directly. </src>` | 1179 |
| 5 | `<src><\|wait\|></src>` | `<src>Abducts between </src>` | 1608 |
| 6 | `<src>between the resources. </src>` | `<src>the resources. </src>` | 1128 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1625 |
| 8 | `<src>you get into </src>` | `<src>you get into a </src>` | 1296 |
| 9 | `<src>a situation </src>` | `<src>situation where you </src>` | 1382 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 1770 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 2047 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1763 |
| 13 | `<src>you need to let us know, </src>` | `<src>meant to let us know. </src>` | 1434 |
| 14 | `<src>and we can see about </src>` | `<src>And we can see about </src>` | 1159 |
| 15 | `<src><\|wait\|></src>` | `<src>moving those media </src>` | 1016 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>files and then making sure </src>` | 737 |
| 17 | `<src>get backed up </src>` | `<src>they get back up </src>` | 633 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 432 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2264 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1352 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 963 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 810 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the HR field </src>` | 1104 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1602 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1407 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 1772 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 792 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 1308 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 1843 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that </src>` | 2046 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree upon </src>` | 1785 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields </src>` | 1261 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these </src>` | 1166 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources, </src>` | 1114 |
| 17 | `<src>draw from, </src>` | `<src>that we can draw from, </src>` | 774 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 710 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 413 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2233 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful, </src>` | 1423 |
| 3 | `<src>right, </src>` | `<src>individual right, </src>` | 912 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court came </src>` | 987 |
| 5 | `<src>came along </src>` | `<src>along last, </src>` | 927 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading, and I don't want to </src>` | 1909 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>have the courts want to be </src>` | 1665 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1892 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1257 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 1849 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 1891 |
| 12 | `<src><\|wait\|></src>` | `<src>but they rather </src>` | 1860 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect </src>` | 1411 |
| 14 | `<src>the consensus </src>` | `<src><\|wait\|></src>` | 993 |
| 15 | `<src><\|wait\|></src>` | `<src>the consensus </src>` | 1073 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged </src>` | 988 |
| 17 | `<src><\|wait\|></src>` | `<src>soam. </src>` | 619 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 179 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 401 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 318 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 219 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1975 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1484 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1297 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 1215 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到</src>` | 609 |
| 6 | `<src>的部分。</src>` | `<src>一个是客厅的部分，</src>` | 1468 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 1422 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 2005 |
| 9 | `<src>我们</src>` | `<src><\|wait\|></src>` | 671 |
| 10 | `<src>在休息的地方，</src>` | `<src>我们在休息</src>` | 2026 |
| 11 | `<src><\|wait\|></src>` | `<src>的地方，所以呢，</src>` | 2067 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的部分</src>` | 1922 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，反映的是</src>` | 1636 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 971 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 1177 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 1038 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 500 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 281 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 475 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 237 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 287 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1815 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1446 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1211 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 872 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 718 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 1901 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1543 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1950 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1193 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 1731 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1932 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 2017 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1483 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations, </src>` | 1120 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1093 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 881 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 606 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 468 |
| 19 | `<src>play </src>` | `<src><\|wait\|></src>` | 311 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>play the devil's advocate, </src>` | 362 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 281 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 269 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 309 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. stands for </src>` | 320 |
| 25 | `<src>ENTP stands for </src>` | `<src>for </src>` | 241 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 의 이준석은 </src>` | 1891 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>정무 를 거부 한 </src>` | 1724 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1121 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1268 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1700 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1402 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2115 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 721 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1959 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2004 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 2050 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들은 해 놓고 </src>` | 1743 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 를 </src>` | 1104 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1174 |
| 15 | `<src><\|wait\|></src>` | `<src>독기 를 품은 </src>` | 936 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 626 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 444 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 304 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 292 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 169 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납건. </src>` | 261 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 234 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 310 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 293 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 289 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>がまあ</src>` | 2072 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 1429 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってるみたいなの</src>` | 1437 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>でここのね</src>` | 1260 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>プロフェッショナルホテル</src>` | 1631 |
| 6 | `<src>も</src>` | `<src>で朝食が</src>` | 967 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 1651 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1373 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1244 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 1845 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴルドストンホテルを</src>` | 1894 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいなって</src>` | 1861 |
| 13 | `<src>なっていう方はですね</src>` | `<src>いう方はですね</src>` | 1442 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1117 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>まあいいんじゃないか</src>` | 1242 |
| 16 | `<src><\|wait\|></src>` | `<src>なとはい。</src>` | 752 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います</src>` | 590 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね</src>` | 465 |
| 19 | `<src>駅ももう</src>` | `<src>都心駅も</src>` | 376 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 279 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかるか</src>` | 265 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんないかそんな</src>` | 313 |
| 23 | `<src>レベルのね</src>` | `<src>辺りのね</src>` | 271 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあホテル</src>` | 295 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 289 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 145 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 176 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 140 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではね今回は</src>` | 144 |
