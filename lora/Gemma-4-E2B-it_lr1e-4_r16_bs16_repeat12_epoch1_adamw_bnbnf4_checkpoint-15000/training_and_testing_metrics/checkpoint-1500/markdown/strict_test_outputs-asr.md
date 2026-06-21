# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9526
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4636
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
  - PROCESS_TIME_MS_AVG: 1442.2380
  - PROCESS_TIME_MS_P50: 1490.1830
  - PROCESS_TIME_MS_P95: 2575.5440
  - PROCESS_TIME_MS_MAX: 3402.8860

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
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1613 |
| 2 | `<src>あの特に</src>` | `<src>あの</src>` | 1552 |
| 3 | `<src>これなんかまだ</src>` | `<src>特に中学生</src>` | 316 |
| 4 | `<src>一年生ですからね。</src>` | `<src>まだ一年生ですからね。</src>` | 997 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1151 |
| 6 | `<src>こう短く</src>` | `<src>こう身近く</src>` | 1671 |
| 7 | `<src>剪定を</src>` | `<src>選択を</src>` | 518 |
| 8 | `<src><\|wait\|></src>` | `<src>こう</src>` | 1517 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>退ずしていたら</src>` | 946 |
| 10 | `<src>十年経っても</src>` | `<src>一年経っても</src>` | 1644 |
| 11 | `<src>大した。</src>` | `<src>退した。</src>` | 1977 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2119 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>乖的送纸店，</src>` | 1660 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个营收</src>` | 1061 |
| 4 | `<src>然后</src>` | `<src>也很大。</src>` | 1189 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 573 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在帮你</src>` | 1298 |
| 7 | `<src>儿核桃</src>` | `<src>跟陶人</src>` | 1624 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 596 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>交流一下，</src>` | 1949 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 1559 |
| 11 | `<src>仁儿。</src>` | `<src>和陶人。</src>` | 2832 |

---

### Test Example 3 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1737 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src><\|wait\|></src>` | 1590 |
| 3 | `<src>촉발 시키고 </src>` | `<src>애플 슉빠시끼고 </src>` | 1281 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1151 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1218 |
| 6 | `<src><\|wait\|></src>` | `<src>머를 쪼개 고 </src>` | 737 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>헤르나 </src>` | 1797 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1082 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1619 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들인 </src>` | 2519 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>입니다. </src>` | 2020 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1896 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气数是容易的，</src>` | 1695 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 1091 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有</src>` | 1199 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导到</src>` | 1467 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 387 |
| 7 | `<src>处于中间，</src>` | `<src>突破于中年，</src>` | 1937 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1833 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1378 |
| 10 | `<src>要成为</src>` | `<src>要成为一个</src>` | 2704 |
| 11 | `<src>一个师父。</src>` | `<src>师傅，</src>` | 1369 |

---

### Test Example 5 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>面对这个</src>` | 1752 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>情况，我们就是</src>` | 1644 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1115 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管</src>` | 1275 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1314 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们下了这个状况，</src>` | 576 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1859 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1643 |
| 9 | `<src>独立承担。</src>` | `<src>你努力承担。</src>` | 1495 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 2599 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是给做Solution。</src>` | 1582 |

---

### Test Example 6 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなど</src>` | 2073 |
| 2 | `<src>あの</src>` | `<src>が</src>` | 1508 |
| 3 | `<src>いただもらえる</src>` | `<src>あの</src>` | 1084 |
| 4 | `<src>といったようなものも</src>` | `<src>いただくというものも用意しております</src>` | 888 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので</src>` | 512 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1677 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1483 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 641 |
| 9 | `<src>えっと</src>` | `<src>て、えっと</src>` | 1700 |
| 10 | `<src><\|wait\|></src>` | `<src>何でしょうか。</src>` | 1361 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>内側がありますので</src>` | 2597 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>少々お待ちください。</src>` | 1599 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1653 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1523 |
| 3 | `<src>Drop into </src>` | `<src>Drop pin to your body. </src>` | 1223 |
| 4 | `<src>your body. </src>` | `<src>Where does </src>` | 1141 |
| 5 | `<src>Where does the tension </src>` | `<src>the tension start? </src>` | 689 |
| 6 | `<src>start? What is it? </src>` | `<src>What is it? </src>` | 1213 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 1962 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 1742 |
| 9 | `<src>I ask them what </src>` | `<src>Or is it a </src>` | 1512 |
| 10 | `<src><\|wait\|></src>` | `<src>low lung capacity </src>` | 2644 |
| 11 | `<src>language are you using? </src>` | `<src>you using? </src>` | 1412 |

---

### Test Example 8 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大体</src>` | 1940 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1592 |
| 3 | `<src>始めた</src>` | `<src>始まった</src>` | 1072 |
| 4 | `<src>もので、</src>` | `<src>もので</src>` | 253 |
| 5 | `<src>ゴッホ、</src>` | `<src>5号</src>` | 1105 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン</src>` | 1458 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 411 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザームの</src>` | 1939 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1873 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の</src>` | 1655 |
| 11 | `<src>は、田舎の</src>` | `<src><\|wait\|></src>` | 2771 |
| 12 | `<src>中学生でも。</src>` | `<src>絵、</src>` | 1009 |

---

### Test Example 9 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1948 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘撒完以后呢，</src>` | 1661 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力</src>` | 1072 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也</src>` | 1343 |
| 5 | `<src>然后</src>` | `<src>衰弱了，</src>` | 1651 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 1674 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 594 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 1979 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 1535 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2668 |
| 11 | `<src>抑郁状态。</src>` | `<src>低预状态。</src>` | 954 |

---

### Test Example 10 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1881 |
| 2 | `<src>옹심이, </src>` | `<src>봉심이 </src>` | 1642 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1150 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼봉심이 </src>` | 1254 |
| 5 | `<src>옹심이가 </src>` | `<src>서울봉심이가 </src>` | 1643 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1379 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞였 던 건데요. 야 </src>` | 790 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 1964 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1497 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해행으로 조금 죽입니다. </src>` | 3133 |
| 11 | `<src>진짜. </src>` | `<src>진짜 </src>` | 759 |

---

### Test Example 11 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2037 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是</src>` | 1643 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1105 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们身生的爱</src>` | 1438 |
| 5 | `<src>爱浇水、</src>` | `<src>交水，</src>` | 1594 |
| 6 | `<src>施肥，</src>` | `<src>十分</src>` | 1507 |
| 7 | `<src>给足</src>` | `<src>可以</src>` | 541 |
| 8 | `<src>孩子心理营养，</src>` | `<src>对孩子心里影响。</src>` | 2072 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1612 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>你耐心等</src>` | 2910 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 812 |

---

### Test Example 12 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 이럴지 </src>` | 1920 |
| 2 | `<src><\|wait\|></src>` | `<src>너무 </src>` | 1514 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>이 저희 가 할 수 있지만 </src>` | 1202 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1420 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 </src>` | 1526 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 가 보살 인데 꿈일 </src>` | 1979 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 보이 고 </src>` | 760 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 1733 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보살 로 보이 려고 보이 세 우주 가 </src>` | 2023 |
| 10 | `<src>지금 나한테 </src>` | `<src>진다 한 </src>` | 2401 |
| 11 | `<src>보살 이라는데. </src>` | `<src>이 보살 이라는 게. </src>` | 695 |

---

### Test Example 13 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1720 |
| 2 | `<src>映画でですね、</src>` | `<src>Aが</src>` | 1583 |
| 3 | `<src>いろんな場面で</src>` | `<src>あるんですね。</src>` | 442 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>いいな場面で</src>` | 843 |
| 5 | `<src>調べるときに、</src>` | `<src>急速加速を考えてる</src>` | 1375 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>時にAの</src>` | 1572 |
| 7 | `<src>ことで、あの</src>` | `<src>乱高しながら</src>` | 1936 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>急速加速を</src>` | 1132 |
| 9 | `<src>保証する、生息である</src>` | `<src>減少する、</src>` | 1570 |
| 10 | `<src>ことを保証する</src>` | `<src>急速でること保証する</src>` | 2317 |
| 11 | `<src>といったような</src>` | `<src>といった使い方を</src>` | 2270 |
| 12 | `<src>使い方をされます。</src>` | `<src>されています。</src>` | 344 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1757 |
| 2 | `<src>Did very important research </src>` | `<src>Did varying research </src>` | 1614 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1173 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people? </src>` | 1222 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem. </src>` | 1724 |
| 6 | `<src>research, </src>` | `<src>Research. </src>` | 1497 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 793 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2171 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1799 |
| 10 | `<src>out there, </src>` | `<src>out there. People that </src>` | 2975 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 348 |

---

### Test Example 15 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1743 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1484 |
| 3 | `<src><\|wait\|></src>` | `<src>天気</src>` | 258 |
| 4 | `<src>テキという設備寺が</src>` | `<src>を</src>` | 1040 |
| 5 | `<src>ありましたね。</src>` | `<src>チェックしましたね。</src>` | 1269 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1457 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 400 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井氏の</src>` | 1933 |
| 9 | `<src><\|wait\|></src>` | `<src>仕組みは</src>` | 2009 |
| 10 | `<src>は五経、</src>` | `<src>五個</src>` | 1393 |
| 11 | `<src><\|wait\|></src>` | `<src>チェック</src>` | 2491 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 1411 |
| 13 | `<src>です。</src>` | `<src>五ビス。</src>` | 1014 |

---

### Test Example 16 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2062 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>명단 에 있는 식성들은 </src>` | 1682 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1067 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1452 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1602 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 1971 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>식성들이 </src>` | 1848 |
| 8 | `<src>때문 입니다. </src>` | `<src>있었기 때문 입니다. </src>` | 1578 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2629 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 1255 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교수 들은 </src>` | 1290 |

---

### Test Example 17 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1633 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到</src>` | 1583 |
| 3 | `<src>回到我生活</src>` | `<src>我生活的一个</src>` | 1069 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，让我</src>` | 1259 |
| 5 | `<src>让我能够哈，</src>` | `<src>能够好好的</src>` | 617 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在它下面的时候，</src>` | 1351 |
| 7 | `<src>在做热汤</src>` | `<src>在做日航</src>` | 1897 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>日航</src>` | 2012 |
| 9 | `<src><\|wait\|></src>` | `<src>的节奏，</src>` | 1490 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时</src>` | 2662 |
| 11 | `<src>小小的愿望</src>` | `<src>背动着</src>` | 1164 |
| 12 | `<src>哈。</src>` | `<src>一个小小的一个愿望哈。</src>` | 1348 |

---

### Test Example 18 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2050 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1601 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1128 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learned to repeat. </src>` | 1445 |
| 5 | `<src>Find what you're good at </src>` | `<src>Finally, you're good at </src>` | 1665 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1940 |
| 7 | `<src><\|wait\|></src>` | `<src>And when you're not </src>` | 1488 |
| 8 | `<src>And what you're not good at, </src>` | `<src>good at it, </src>` | 1518 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get to people around you to help you with </src>` | 3041 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1276 |
| 11 | `<src>And until next time. </src>` | `<src>it, and in telling next time, </src>` | 1493 |

---

### Test Example 19 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2023 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 1468 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 277 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと、</src>` | 1084 |
| 5 | `<src><\|wait\|></src>` | `<src>信号が消えなくなって</src>` | 1405 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 1572 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1538 |
| 8 | `<src>役ねじの</src>` | `<src>逆ネジの</src>` | 718 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1977 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついてるっていうこと</src>` | 1652 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 2576 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 958 |
| 13 | `<src>分解完了。</src>` | `<src>ハイ分解完了。</src>` | 1457 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1839 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 1582 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>毫无波澜，</src>` | 1164 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1172 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开档，</src>` | 447 |
| 6 | `<src>期间</src>` | `<src>期限大概</src>` | 1429 |
| 7 | `<src>大概有十位医生</src>` | `<src>有十二星</src>` | 1638 |
| 8 | `<src>来诊断，</src>` | `<src>来设定，</src>` | 600 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 2026 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 1800 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 2602 |
| 12 | `<src>他们</src>` | `<src>当然</src>` | 724 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 1575 |

---

### Test Example 21 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1692 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1668 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相不够怪的人之间，</src>` | 1186 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1250 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>有着某种心理。</src>` | 1612 |
| 6 | `<src>难道会是</src>` | `<src>难道</src>` | 1489 |
| 7 | `<src><\|wait\|></src>` | `<src>会是</src>` | 625 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从天际里开始的</src>` | 2207 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1684 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2898 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思</src>` | 651 |
| 12 | `<src>连篇。</src>` | `<src>与年篇</src>` | 1818 |

---

### Test Example 22 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1843 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 산줄에 </src>` | 1645 |
| 3 | `<src>해가지고 내가 </src>` | `<src>죽여달라고 해가지고 내가 </src>` | 1231 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이려고 들어왔 수도 </src>` | 1324 |
| 5 | `<src>다른 잔찜에 </src>` | `<src><\|wait\|></src>` | 1551 |
| 6 | `<src>죽여 달라 </src>` | `<src>다른 산줄에 죽여달라고 </src>` | 1998 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해자 하냐 내가 </src>` | 2231 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그런 소리 </src>` | 1639 |
| 9 | `<src><\|wait\|></src>` | `<src>안 듣고 있는 줄 알아내냐 </src>` | 3403 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아 </src>` | 1088 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1304 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1736 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1671 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1136 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1365 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1679 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1864 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 987 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 1694 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 2327 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets used </src>` | 2305 |
| 11 | `<src>or gets used to make </src>` | `<src>to make different bonds. </src>` | 1075 |
| 12 | `<src>different bonds. </src>` | `<src><\|wait\|></src>` | 1353 |

---

### Test Example 24 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个</src>` | 1756 |
| 2 | `<src><\|wait\|></src>` | `<src>就是进入</src>` | 1579 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二GIS平台，</src>` | 445 |
| 4 | `<src>服务</src>` | `<src>并服务</src>` | 789 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1235 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1689 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1466 |
| 8 | `<src><\|wait\|></src>` | `<src>在做</src>` | 667 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>维生运动好事几年，</src>` | 2381 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 2016 |
| 11 | `<src>给微信公众号评分</src>` | `<src>维生运动好平分的</src>` | 2831 |
| 12 | `<src>的新榜反而</src>` | `<src>星棒</src>` | 1106 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1468 |

---

### Test Example 25 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1821 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chunaharu. </src>` | 1648 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1150 |
| 4 | `<src><\|wait\|></src>` | `<src>in a UX background. </src>` | 1370 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>I have a </src>` | 1638 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>background in psychology. </src>` | 1928 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1662 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at YEN, </src>` | 1593 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 2602 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 1578 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate </src>` | 1199 |
| 12 | `<src>corporate consultancy. </src>` | `<src>consultancy. </src>` | 1406 |

---

### Test Example 26 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2095 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1580 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment </src>` | 1230 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1307 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1593 |
| 6 | `<src>to how political </src>` | `<src>to how </src>` | 1497 |
| 7 | `<src><\|wait\|></src>` | `<src>political change </src>` | 605 |
| 8 | `<src>change can happen </src>` | `<src>can happen </src>` | 2031 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1638 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2690 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 974 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 1386 |
| 13 | `<src>myriad. </src>` | `<src>I'mared. </src>` | 1692 |

---

### Test Example 27 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2097 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1641 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1155 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1296 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1591 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1559 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 656 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1970 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1600 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 2730 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 975 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game dot sort array </src>` | 1761 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1509 |

---

### Test Example 28 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>あとなんか</src>` | 2149 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が</src>` | 1563 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1177 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オーシャラーとか</src>` | 1368 |
| 5 | `<src>多いですね。</src>` | `<src>タタガレーボールですね</src>` | 1707 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊したい方って</src>` | 1943 |
| 7 | `<src>すごい</src>` | `<src>すぐに行こう意識が</src>` | 2110 |
| 8 | `<src>自己意識高いし、</src>` | `<src>高いし</src>` | 1612 |
| 9 | `<src>自分で</src>` | `<src>自分でも</src>` | 2589 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>とこ見てとこ見て</src>` | 1125 |
| 11 | `<src>傾向が強いので、</src>` | `<src>こうやってシャグが強いので</src>` | 1850 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1433 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or or if you have </src>` | 1902 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 1561 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1169 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1374 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1599 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1933 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 461 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. It's like oh, </src>` | 2134 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2104 |
| 10 | `<src>spelled with a double </src>` | `<src>start with a double </src>` | 2637 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 418 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>P, double L, I don't know </src>` | 2159 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1369 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1741 |
| 2 | `<src>我们可以看到的是</src>` | `<src>这一张的部分</src>` | 1599 |
| 3 | `<src>一个在钓鱼</src>` | `<src>我们看到的是一个</src>` | 1174 |
| 4 | `<src>的人，但是</src>` | `<src>戴旧的人，但是</src>` | 1399 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于</src>` | 1570 |
| 6 | `<src>所以</src>` | `<src>逆向的。</src>` | 1876 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>这同样形成了</src>` | 501 |
| 8 | `<src>时候，就要去</src>` | `<src>这样一个状况，</src>` | 2041 |
| 9 | `<src>特别注意，</src>` | `<src>就要特别的注意</src>` | 1717 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能</src>` | 2718 |
| 11 | `<src>钓到鱼，</src>` | `<src>得到</src>` | 579 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与它</src>` | 1521 |
| 13 | `<src><\|wait\|></src>` | `<src>得到意识</src>` | 1494 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 1027 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1788 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 </src>` | 1645 |
| 3 | `<src>인슐린과 </src>` | `<src>이거 들은 거의 </src>` | 1146 |
| 4 | `<src>이제 거진 </src>` | `<src>유리 수리인가 </src>` | 1336 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>이거 컷인 유산 쟁이들 </src>` | 1800 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>그러니까 </src>` | 1768 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 2045 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>강염 미네랄이다 </src>` | 1631 |
| 9 | `<src>이렇게 </src>` | `<src>이거 </src>` | 2549 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>굉장히 잘 좀 </src>` | 1195 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>그래 그런 거죠 </src>` | 1321 |
| 12 | `<src>그거 에다가 </src>` | `<src>이제 그 후에다가 </src>` | 1564 |
| 13 | `<src>아연. </src>` | `<src>아현. </src>` | 1227 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1692 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>백오십만 개가 </src>` | 1654 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중화 벌써 1천만 개로 </src>` | 1312 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1340 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1471 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1892 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 </src>` | 1142 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>성장 하거나 </src>` | 1607 |
| 9 | `<src>걷게 되는데 </src>` | `<src>혹은 해외 법인 을 거쳐도 되는데 </src>` | 3142 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 에 </src>` | 1452 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성기 없던 것은 </src>` | 1076 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>성장 도 </src>` | 1449 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>폐업도 하지 않은 현상 들 보이 게 된 거죠. </src>` | 1813 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 1984 |
| 2 | `<src>要提醒大家，</src>` | `<src>啊，</src>` | 1559 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1204 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1360 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1595 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1529 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 729 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，</src>` | 2202 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 1676 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是</src>` | 2521 |
| 11 | `<src><\|wait\|></src>` | `<src>一夜之间就</src>` | 768 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的。</src>` | 1541 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1636 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属于的朋友呢，</src>` | 1261 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1679 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>扎到了一个尖头，</src>` | 1635 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1076 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>找到了尖头之后，</src>` | 1431 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必</src>` | 1633 |
| 6 | `<src><\|wait\|></src>` | `<src>主要先</src>` | 1721 |
| 7 | `<src>先守住，</src>` | `<src>守住，</src>` | 500 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说</src>` | 2194 |
| 9 | `<src><\|wait\|></src>` | `<src>哎，</src>` | 1990 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>那我再去做</src>` | 2666 |
| 11 | `<src><\|wait\|></src>` | `<src>下去哦。</src>` | 390 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 2032 |
| 13 | `<src><\|wait\|></src>` | `<src>因为呢，</src>` | 1367 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1206 |

---

### Test Example 35 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>또 </src>` | 1675 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니 뭐여. </src>` | 1654 |
| 3 | `<src>이방인으로 </src>` | `<src>여기 가 </src>` | 1053 |
| 4 | `<src>있을 때에 </src>` | `<src>이방인으로 </src>` | 1261 |
| 5 | `<src>말 못하 는 </src>` | `<src>있기 때문 에 </src>` | 493 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하는 우상에게로 </src>` | 1543 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 그대로 </src>` | 1810 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느라 </src>` | 1295 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1539 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그럼 으로 내가 </src>` | 2518 |
| 11 | `<src>너희 에게 </src>` | `<src>너희에게 </src>` | 1928 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1057 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 </src>` | 1351 |
| 14 | `<src>말하는 자는. </src>` | `<src>영으로 말하는 자는 </src>` | 1521 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1132 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who </src>` | 2039 |
| 2 | `<src>just getting going </src>` | `<src>is just getting going </src>` | 1600 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1162 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1203 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I got ten of them </src>` | 1664 |
| 6 | `<src>that I think are </src>` | `<src>that are really important </src>` | 1518 |
| 7 | `<src>really important. </src>` | `<src><\|wait\|></src>` | 657 |
| 8 | `<src><\|wait\|></src>` | `<src>um. </src>` | 1548 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go and do </src>` | 1660 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 2907 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 1137 |
| 12 | `<src>that follow this video </src>` | `<src>at fall this video. </src>` | 1307 |
| 13 | `<src><\|wait\|></src>` | `<src>The coverage </src>` | 1510 |
| 14 | `<src>that cover each one </src>` | `<src>each one </src>` | 1264 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1079 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 1815 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1647 |
| 3 | `<src><\|wait\|></src>` | `<src>there was </src>` | 1108 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interests before. </src>` | 1272 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1207 |
| 6 | `<src>netfilter, TC. </src>` | `<src>Net future TC </src>` | 625 |
| 7 | `<src>Yeah, so </src>` | `<src><\|wait\|></src>` | 1914 |
| 8 | `<src>this is just </src>` | `<src>is just </src>` | 1785 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1457 |
| 10 | `<src>to look at. </src>` | `<src>to look at </src>` | 2694 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1395 |
| 12 | `<src><\|wait\|></src>` | `<src>about </src>` | 1181 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1431 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on Bug Repos. </src>` | 1547 |
| 15 | `<src>should be aware of that. </src>` | `<src>Should be wherever. </src>` | 1116 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1942 |
| 2 | `<src>十一二手とか</src>` | `<src>十一二手とか</src>` | 1630 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>なですけど、</src>` | 1165 |
| 4 | `<src>十秒で。</src>` | `<src>おそらく</src>` | 1168 |
| 5 | `<src>まあ</src>` | `<src>十秒でまあ</src>` | 1219 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 640 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1931 |
| 8 | `<src>計算ですか</src>` | `<src>速度なんですかね。</src>` | 1624 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 1454 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2254 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1764 |
| 12 | `<src><\|wait\|></src>` | `<src>十一二手</src>` | 413 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1742 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1471 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1250 |
| 16 | `<src>あるから。</src>` | `<src>だから</src>` | 706 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1867 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1618 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 1156 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分</src>` | 1336 |
| 5 | `<src>也就是</src>` | `<src>。</src>` | 1545 |
| 6 | `<src>在事业方面的</src>` | `<src>也就是在事业方面的</src>` | 1585 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩增长所带来的</src>` | 740 |
| 8 | `<src>与收入的</src>` | `<src>红利，</src>` | 1995 |
| 9 | `<src>提升。如果是在</src>` | `<src>收入的提升。</src>` | 1606 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>如果</src>` | 2575 |
| 11 | `<src>这个月</src>` | `<src>在投资理财方面，这个月</src>` | 1107 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 2017 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对增财来说，</src>` | 1509 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就算</src>` | 1147 |
| 15 | `<src><\|wait\|></src>` | `<src>为了那么一点。</src>` | 936 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 1987 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>ムラせてやる。</src>` | 1642 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1057 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1245 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>火勢を見ても</src>` | 516 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1355 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1860 |
| 8 | `<src><\|wait\|></src>` | `<src>超に</src>` | 399 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>超えてる不烈火勢気よ。</src>` | 2162 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1700 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 2717 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなでいくを</src>` | 697 |
| 13 | `<src>が、</src>` | `<src>やってる</src>` | 1994 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 1364 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい解足線を</src>` | 1337 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 926 |

---

### Test Example 41 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 2049 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어, 어째 보면 </src>` | 1637 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 이십대를 </src>` | 1145 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1198 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>이 동생 이자 </src>` | 1141 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 도 가족 같은 </src>` | 774 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>동생 이잖아. </src>` | 1916 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1246 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 1547 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생감보다는 </src>` | 2371 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 2086 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 1184 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1366 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1371 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓고 </src>` | 1186 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 </src>` | 1000 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1979 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. How far </src>` | 1649 |
| 3 | `<src>How far did you </src>` | `<src>did you actually </src>` | 1113 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1257 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>go in your education? </src>` | 1681 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1939 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 544 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. </src>` | 2000 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 2141 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, did you graduate? </src>` | 2771 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1145 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1514 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now. </src>` | 1603 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you </src>` | 1064 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 864 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2139 |
| 2 | `<src><\|wait\|></src>` | `<src>생워라 </src>` | 1598 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 1145 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 </src>` | 1411 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋은 잣자리 돋은 </src>` | 1706 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 </src>` | 1863 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>오며 이걸 </src>` | 1859 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>흔들 어서 같이 놀자는 거야. </src>` | 1689 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 </src>` | 2662 |
| 10 | `<src>물릴 거고 </src>` | `<src>오며 올릴 거고 </src>` | 1222 |
| 11 | `<src>신이 오면 </src>` | `<src>기신이 오면 너 </src>` | 1305 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>지켜 주라고 </src>` | 1562 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>인찔러 주잖아. </src>` | 1394 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>그러니까 편안 마음 에. </src>` | 1006 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 962 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね</src>` | 1972 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1642 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうだけじゃなくて</src>` | 1082 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルPython</src>` | 1230 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね</src>` | 1679 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも</src>` | 358 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフのビジュアルの</src>` | 1800 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>書いてあとそれは</src>` | 2049 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコードがそっから</src>` | 1652 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されてそれは</src>` | 2824 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで信号処理</src>` | 891 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われるっていう</src>` | 1676 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ことをしているから</src>` | 1526 |
| 14 | `<src><\|wait\|></src>` | `<src>です。</src>` | 1091 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 1007 |
| 16 | `<src>じゃあ。</src>` | `<src>はいじゃあ</src>` | 930 |

---

### Test Example 45 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 1953 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1498 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 401 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 971 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1279 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트예요. </src>` | 1757 |
| 7 | `<src><\|wait\|></src>` | `<src>B가 컨설턴트 </src>` | 1964 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>여가지고 A라는 </src>` | 1594 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1389 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2796 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>줬을 때 </src>` | 1473 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1330 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1558 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로 사이트 스크립트 에서 </src>` | 1567 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>XRP까지 </src>` | 926 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까 </src>` | 1057 |

---

### Test Example 46 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1701 |
| 2 | `<src>HTML이라고 </src>` | `<src>어 </src>` | 1550 |
| 3 | `<src><\|wait\|></src>` | `<src>H1이라고 하는 </src>` | 1171 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴피트도 </src>` | 1434 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1689 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1879 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1843 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴피트의 언어 의 </src>` | 1548 |
| 9 | `<src>문법 에 </src>` | `<src>문법 의 </src>` | 2707 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>말 이렇게 우리 가 이제 </src>` | 1306 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>초도들을 </src>` | 1488 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 1730 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그것 들을 </src>` | 1245 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1050 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1000 |

---

### Test Example 47 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어 가면 </src>` | 2055 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 </src>` | 1572 |
| 3 | `<src>운전 을 </src>` | `<src>해매입니다. </src>` | 1128 |
| 4 | `<src><\|wait\|></src>` | `<src>운전 을 하고 </src>` | 1264 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 다니 고 </src>` | 924 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>있거나 </src>` | 928 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 으로 가면 </src>` | 1918 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 988 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에게 나가 는 것도 </src>` | 1712 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장려 료예요. </src>` | 2433 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 챙기 는 거. </src>` | 2275 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1695 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1556 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>뭐해 봐요. 그거 는 </src>` | 1511 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>잘하는 것 같아요. </src>` | 1073 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 823 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1621 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1649 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놓았습니다. </src>` | 1194 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 1142 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>이 로쿠자 분석 을 보시면 </src>` | 1473 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 393 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 60, </src>` | 1971 |
| 8 | `<src>파이프 를 </src>` | `<src>FP 파이프 를 </src>` | 1861 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 </src>` | 1613 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것이 로포인이다. </src>` | 3341 |
| 11 | `<src><\|wait\|></src>` | `<src>엑스박스 </src>` | 645 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>시리즈, </src>` | 1841 |
| 13 | `<src><\|wait\|></src>` | `<src>엑스에서도 없는 </src>` | 1557 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시, </src>` | 1430 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>S가 여기 도 없다. </src>` | 1061 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 723 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1971 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感觉</src>` | 1631 |
| 3 | `<src>的感情或</src>` | `<src>对手的感情</src>` | 1106 |
| 4 | `<src>真实意图的，</src>` | `<src>或真实意图的。</src>` | 1410 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1648 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1836 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常会</src>` | 506 |
| 8 | `<src>会听到人们</src>` | `<src>听到人们这样说：“</src>` | 2076 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1731 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2774 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 461 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在躲黄了。”</src>` | 1708 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1536 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1317 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 906 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 877 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 361 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1887 |
| 2 | `<src>Activity than </src>` | `<src>Activity, </src>` | 1602 |
| 3 | `<src>self-defining what we think </src>` | `<src>then self-defining </src>` | 1125 |
| 4 | `<src>the standard is because you're </src>` | `<src>what we think the standard is, </src>` | 1474 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 1639 |
| 6 | `<src>but the reality </src>` | `<src>But the reality </src>` | 1890 |
| 7 | `<src>is is that </src>` | `<src>is that </src>` | 968 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on </src>` | 1753 |
| 9 | `<src>block and because the </src>` | `<src>the block, </src>` | 2385 |
| 10 | `<src>standards have </src>` | `<src>and because the standards have </src>` | 2248 |
| 11 | `<src>changed from 20 </src>` | `<src><\|wait\|></src>` | 1043 |
| 12 | `<src>years ago, </src>` | `<src>changed from twenty years ago, </src>` | 1648 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1478 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1064 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 1088 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to a higher standard. </src>` | 547 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 절수가 </src>` | 1833 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 1591 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다음에 </src>` | 1203 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형 주도 </src>` | 1374 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1554 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>어 큰 폭의 상승 을 </src>` | 2002 |
| 7 | `<src>먼저 </src>` | `<src>하겠지만 먼저 </src>` | 2035 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 1525 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가변 종목 들이 </src>` | 3291 |
| 10 | `<src>먼저 </src>` | `<src>이 먼저 시장 을 </src>` | 663 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 움직이기 </src>` | 2043 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>때문 에 </src>` | 1467 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요식초기 </src>` | 1305 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가변 종목 을 </src>` | 1011 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈으로 봐야 </src>` | 769 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 445 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1672 |
| 2 | `<src>首次觉知到</src>` | `<src>フローイの所得主義</src>` | 1670 |
| 3 | `<src>那个现象：</src>` | `<src>決直到的那個現象，</src>` | 1181 |
| 4 | `<src>每当我们</src>` | `<src>美当中</src>` | 1184 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1639 |
| 6 | `<src>处于爱之中，</src>` | `<src>属于愛之中</src>` | 1481 |
| 7 | `<src>所谓的爱，</src>` | `<src>所位的愛，</src>` | 676 |
| 8 | `<src>我们也</src>` | `<src>我们</src>` | 1791 |
| 9 | `<src>同时进入恨。</src>` | `<src>也同时進入</src>` | 1467 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2741 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨，</src>` | 1273 |
| 12 | `<src>它是爱；</src>` | `<src>在早上的时候他才爱。</src>` | 1289 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1490 |
| 14 | `<src>它就变成恨。</src>` | `<src>他就变成恨。</src>` | 1304 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1075 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆。</src>` | 990 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 643 |
| 18 | `<src>继续在移动。</src>` | `<src>一动。</src>` | 526 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1900 |
| 2 | `<src>Also, </src>` | `<src>Also, you will not </src>` | 1636 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 1112 |
| 4 | `<src>move media objects </src>` | `<src>media objects </src>` | 1195 |
| 5 | `<src><\|wait\|></src>` | `<src>between </src>` | 907 |
| 6 | `<src>between the resources. </src>` | `<src>the resources </src>` | 960 |
| 7 | `<src>So, if </src>` | `<src>though, </src>` | 1616 |
| 8 | `<src>you get into </src>` | `<src>if you get into </src>` | 621 |
| 9 | `<src>a situation </src>` | `<src>a situation where you </src>` | 1998 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 1831 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 2752 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular </src>` | 663 |
| 13 | `<src>you need to let us know, </src>` | `<src>resource, we'll need to let us know. </src>` | 2138 |
| 14 | `<src>and we can see about </src>` | `<src>And we can see about </src>` | 1429 |
| 15 | `<src><\|wait\|></src>` | `<src>moving those media </src>` | 1176 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>files and then making sure </src>` | 1060 |
| 17 | `<src>get backed up </src>` | `<src>they get back up </src>` | 801 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 546 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1706 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1569 |
| 3 | `<src>is hungry. </src>` | `<src>is a son of Henry. </src>` | 1207 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1170 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been through </src>` | 1329 |
| 6 | `<src><\|wait\|></src>` | `<src>the wilderness </src>` | 470 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>a sporty day. </src>` | 1929 |
| 8 | `<src>And so he says </src>` | `<src>He's hungry, and so he says to </src>` | 2498 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 2040 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're a son of God, prove it. </src>` | 2941 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1294 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread. </src>` | 1763 |
| 13 | `<src><\|wait\|></src>` | `<src>How did </src>` | 1221 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>Jesus deal with that </src>` | 960 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 969 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 496 |
| 17 | `<src>Man shall not live </src>` | `<src>Man, Jonathan lead by bread. </src>` | 607 |
| 18 | `<src>by bread alone. </src>` | `<src>Alone. </src>` | 402 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2164 |
| 2 | `<src>in turmoil </src>` | `<src>in the wrong mile </src>` | 1611 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1101 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1189 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR </src>` | 655 |
| 6 | `<src><\|wait\|></src>` | `<src>field being of </src>` | 1281 |
| 7 | `<src>being of critical importance </src>` | `<src>critical importance </src>` | 1847 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 628 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1877 |
| 10 | `<src>databases, </src>` | `<src>variant databases, which is obviously </src>` | 2087 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>not of my loves. </src>` | 2752 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that </src>` | 956 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree upon </src>` | 1459 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields </src>` | 1429 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in </src>` | 1227 |
| 16 | `<src>data sources that we can </src>` | `<src>these data sources </src>` | 962 |
| 17 | `<src>draw from, </src>` | `<src>that we can draw from. </src>` | 837 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>There's nothing to draw from, right? </src>` | 645 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 397 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2148 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful </src>` | 1546 |
| 3 | `<src>right, </src>` | `<src>individual right, </src>` | 1090 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1276 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 974 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And I don't I don't </src>` | 1069 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>I don't think the courts want to be </src>` | 2044 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1960 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1640 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2823 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 801 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1781 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 1494 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1344 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 861 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 982 |
| 17 | `<src><\|wait\|></src>` | `<src>So. </src>` | 230 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 524 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 454 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 193 |
| 21 | `<src>who. </src>` | `<src>who </src>` | 311 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1915 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1603 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1118 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片呢，我们可以看到</src>` | 1426 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个</src>` | 1585 |
| 6 | `<src>的部分。</src>` | `<src>是克汀的部分，</src>` | 1938 |
| 7 | `<src>那客厅一般</src>` | `<src>而克汀一般</src>` | 1062 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1521 |
| 9 | `<src>我们</src>` | `<src>我们在</src>` | 1967 |
| 10 | `<src>在休息的地方，</src>` | `<src>收集的地方</src>` | 2484 |
| 11 | `<src><\|wait\|></src>` | `<src>啊，所以呢，</src>` | 564 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>它是身体的部分</src>` | 1947 |
| 13 | `<src>也会反映的是</src>` | `<src>才会反映的是</src>` | 1431 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给</src>` | 1185 |
| 15 | `<src>一点时间，</src>` | `<src>自己一点时间</src>` | 833 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好</src>` | 947 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>的做下来，</src>` | 293 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>收集，</src>` | 576 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>可我们看到这边是十五五一人</src>` | 548 |
| 20 | `<src>啊，</src>` | `<src>的嘛，好，</src>` | 391 |
| 21 | `<src>所以是说。</src>` | `<src>所以也是说。</src>` | 309 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1736 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare. </src>` | 1632 |
| 3 | `<src>and they often </src>` | `<src>And they often </src>` | 1110 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 1271 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1658 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 1728 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 587 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1951 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1668 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2811 |
| 11 | `<src>While they're </src>` | `<src>Well, they're extroverted </src>` | 875 |
| 12 | `<src>extroverted, </src>` | `<src><\|wait\|></src>` | 2102 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1396 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations. </src>` | 1221 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 913 |
| 16 | `<src><\|wait\|></src>` | `<src>And like it </src>` | 815 |
| 17 | `<src>get straight to the point. </src>` | `<src>gets straight to the point. </src>` | 216 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 551 |
| 19 | `<src>play </src>` | `<src>to play the devil's advocate </src>` | 536 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>but they </src>` | 368 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy away </src>` | 291 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 209 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 205 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. stands for </src>` | 333 |
| 25 | `<src>ENTP stands for </src>` | `<src>strong. </src>` | 289 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src><\|wait\|></src>` | 1761 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>이전 의 이준석은 </src>` | 1666 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>경무를 거부 한 명분이 후보 를 </src>` | 1428 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 하면서 </src>` | 1097 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선을 </src>` | 1608 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 하면서 </src>` | 1908 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1549 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1524 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2573 |
| 10 | `<src>김종인 을 </src>` | `<src>김정은을 </src>` | 1706 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제간 순간 </src>` | 1024 |
| 12 | `<src>이준석은 </src>` | `<src>이준석을 들은 해놓고 </src>` | 1591 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 </src>` | 1446 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>를 떨어뜨리겠다는 </src>` | 1116 |
| 15 | `<src><\|wait\|></src>` | `<src>뜻끼를 품은 </src>` | 1050 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 631 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 525 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 305 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 282 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 393 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석 청상납건 </src>` | 427 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 279 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당이 </src>` | 305 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 에 얼마나 </src>` | 321 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 273 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1931 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今</src>` | 1594 |
| 3 | `<src>今作ってる</src>` | `<src>作ってみたいです。</src>` | 1112 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>なので</src>` | 889 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ここのね</src>` | 656 |
| 6 | `<src>も</src>` | `<src>ホテルも</src>` | 1561 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1943 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 2172 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1601 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2633 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドストンホテル</src>` | 1050 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1442 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なという方はですね</src>` | 1626 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさって</src>` | 1249 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>みてもまあいいんじゃない</src>` | 1054 |
| 16 | `<src><\|wait\|></src>` | `<src>なと</src>` | 886 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 482 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここホテルからですね</src>` | 513 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 189 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 431 |
| 21 | `<src>歩いて一分</src>` | `<src>1分かかる</src>` | 280 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんないか</src>` | 199 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 334 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>リッチのいいねまあホテル</src>` | 317 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 277 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 304 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさって</src>` | 272 |
| 28 | `<src>ください</src>` | `<src>みてください</src>` | 160 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではね</src>` | 152 |
