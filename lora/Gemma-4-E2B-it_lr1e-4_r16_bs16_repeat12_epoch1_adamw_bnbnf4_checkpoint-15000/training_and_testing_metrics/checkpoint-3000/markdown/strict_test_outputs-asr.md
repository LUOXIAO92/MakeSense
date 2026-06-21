# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9680
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4371
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
  - PROCESS_TIME_MS_AVG: 1440.0340
  - PROCESS_TIME_MS_P50: 1407.3540
  - PROCESS_TIME_MS_P95: 2687.5340
  - PROCESS_TIME_MS_MAX: 3635.6700

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
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1953 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气鼠是容易的，</src>` | 1097 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1012 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师傅</src>` | 1090 |
| 5 | `<src><\|wait\|></src>` | `<src>指导道。</src>` | 1632 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1397 |
| 7 | `<src>处于中间，</src>` | `<src>如喝出由中坚</src>` | 703 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2197 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 568 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2018 |
| 11 | `<src>一个师父。</src>` | `<src>一个师傅，</src>` | 2802 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2057 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1120 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1245 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深沉的爱</src>` | 1734 |
| 5 | `<src>爱浇水、</src>` | `<src>浇水，</src>` | 808 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1377 |
| 7 | `<src>给足</src>` | `<src>培育</src>` | 806 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心灵营养，</src>` | 2176 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1187 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>冷心等等，</src>` | 1567 |
| 11 | `<src>慢慢长大。</src>` | `<src>让孩子慢慢长大。</src>` | 3021 |

---

### Test Example 3 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying important </src>` | 1772 |
| 2 | `<src>Did very important research </src>` | `<src>research </src>` | 1019 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 947 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1301 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1625 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 1428 |
| 7 | `<src>looking at the ten percent </src>` | `<src>a 10% </src>` | 1111 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1832 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1236 |
| 10 | `<src>out there, </src>` | `<src>out there, people that </src>` | 1621 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 3085 |

---

### Test Example 4 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1976 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘沙完以后呢，</src>` | 1107 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的冶炼轻呢</src>` | 1709 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了</src>` | 1646 |
| 5 | `<src>然后</src>` | `<src>啦。然后</src>` | 650 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在</src>` | 1361 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1481 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 1470 |
| 9 | `<src>状态，</src>` | `<src>运行状态，</src>` | 1911 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是</src>` | 2315 |
| 11 | `<src>抑郁状态。</src>` | `<src>所谓的蚁居状态。</src>` | 1724 |

---

### Test Example 5 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명단 에 있는 </src>` | 2146 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1052 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1157 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1055 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1567 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 1462 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1091 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1955 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1437 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2174 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은 </src>` | 2407 |

---

### Test Example 6 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1755 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Abbotol. </src>` | 1142 |
| 3 | `<src>촉발 시키고 </src>` | `<src>축발시키고 </src>` | 1542 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1549 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 725 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 1508 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>녀르나 </src>` | 1368 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1649 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1924 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들은 </src>` | 2898 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>입니다. </src>` | 1140 |

---

### Test Example 7 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1624 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1114 |
| 3 | `<src>これなんかまだ</src>` | `<src>子供がまだ</src>` | 1287 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 962 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1537 |
| 6 | `<src>こう短く</src>` | `<src>こうミミカク</src>` | 1544 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 2802 |
| 8 | `<src><\|wait\|></src>` | `<src>こう退ずして</src>` | 1125 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>あげると</src>` | 1526 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 2835 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 734 |

---

### Test Example 8 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2141 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>怪得忪子儿的地方，</src>` | 1164 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个游行</src>` | 1348 |
| 4 | `<src>然后</src>` | `<src>也很大，</src>` | 1591 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 850 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放假</src>` | 1477 |
| 7 | `<src>儿核桃</src>` | `<src>隔热汤儿，</src>` | 2751 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1092 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>可以的吧？</src>` | 1660 |
| 10 | `<src>这种核桃</src>` | `<src>这种隔热</src>` | 2888 |
| 11 | `<src>仁儿。</src>` | `<src>儿。</src>` | 638 |

---

### Test Example 9 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1827 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1116 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题，</src>` | 1342 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1845 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 774 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们缺少这个状况，</src>` | 1375 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1457 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1673 |
| 9 | `<src>独立承担。</src>` | `<src>不理成单，</src>` | 2025 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言</src>` | 2510 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该做的事情。</src>` | 1330 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2048 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 1039 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくと言ったような</src>` | 955 |
| 4 | `<src>といったようなものも</src>` | `<src>ものも用意しております</src>` | 1240 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので</src>` | 1628 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 999 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 621 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 2129 |
| 9 | `<src>えっと</src>` | `<src>て、</src>` | 857 |
| 10 | `<src><\|wait\|></src>` | `<src>また</src>` | 1682 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>詳細な案内があります</src>` | 2877 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>ので、申し見てください。</src>` | 1468 |

---

### Test Example 11 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1676 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 987 |
| 3 | `<src>Drop into </src>` | `<src>Drop into your body </src>` | 998 |
| 4 | `<src>your body. </src>` | `<src>where does it </src>` | 1185 |
| 5 | `<src>Where does the tension </src>` | `<src>intend to </src>` | 1657 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1578 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 2762 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 1300 |
| 9 | `<src>I ask them what </src>` | `<src>I ask the body </src>` | 1612 |
| 10 | `<src><\|wait\|></src>` | `<src>language </src>` | 2689 |
| 11 | `<src>language are you using? </src>` | `<src>you use. </src>` | 683 |

---

### Test Example 12 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうですよ。</src>` | 1783 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1053 |
| 3 | `<src><\|wait\|></src>` | `<src>天気</src>` | 783 |
| 4 | `<src>テキという設備寺が</src>` | `<src>とレシピが</src>` | 837 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1446 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 830 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1405 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 1278 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 1646 |
| 10 | `<src>は五経、</src>` | `<src>冒険、</src>` | 1206 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1566 |
| 12 | `<src>設備寺、五比</src>` | `<src>レシピ、</src>` | 2797 |
| 13 | `<src>です。</src>` | `<src>ゴビズ。</src>` | 680 |

---

### Test Example 13 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1893 |
| 2 | `<src>옹심이, </src>` | `<src>용심이 </src>` | 1066 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1001 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심이 </src>` | 1194 |
| 5 | `<src>옹심이가 </src>` | `<src>어설프 용심이가 </src>` | 1829 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1385 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. 야 </src>` | 1698 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 1317 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1642 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해형으로 </src>` | 2722 |
| 11 | `<src>진짜. </src>` | `<src>조금 쥐기 미달 지 않았나요? </src>` | 1698 |

---

### Test Example 14 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2062 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1120 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1263 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1714 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1030 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1469 |
| 7 | `<src><\|wait\|></src>` | `<src>And what you're not good </src>` | 2688 |
| 8 | `<src>And what you're not good at, </src>` | `<src>at, get to people </src>` | 1415 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>around you to help you with </src>` | 1795 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2726 |
| 11 | `<src>And until next time. </src>` | `<src>it. And until next time, </src>` | 706 |

---

### Test Example 15 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1719 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1136 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1697 |
| 4 | `<src><\|wait\|></src>` | `<src>之间有着某种</src>` | 1490 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>联系，</src>` | 614 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1362 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1010 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从天体实验</src>` | 1968 |
| 9 | `<src><\|wait\|></src>` | `<src>开始的？</src>` | 1423 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2000 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思</src>` | 2512 |
| 12 | `<src>连篇。</src>` | `<src>与连篇。</src>` | 926 |

---

### Test Example 16 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1853 |
| 2 | `<src><\|wait\|></src>` | `<src>이거 너무 </src>` | 1059 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>이 저열하지 않을 수 있지만 </src>` | 1454 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1719 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 의 </src>` | 901 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 </src>` | 1485 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 보이 고 </src>` | 2656 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 저 보살 로 </src>` | 1263 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 피라고 보이 색 우주 가 </src>` | 1746 |
| 10 | `<src>지금 나한테 </src>` | `<src>진짜 보살 이라는 </src>` | 3003 |
| 11 | `<src>보살 이라는데. </src>` | `<src>거죠. </src>` | 1316 |

---

### Test Example 17 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 2088 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 884 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 385 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1259 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 784 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1660 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1392 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 978 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1946 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1221 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1552 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game dot sort array. </src>` | 3235 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1348 |

---

### Test Example 18 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1978 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1058 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 969 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1192 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴホ、</src>` | 1695 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1487 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1147 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1862 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1485 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 2395 |
| 11 | `<src>は、田舎の</src>` | `<src>は、</src>` | 1970 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生でも</src>` | 1634 |

---

### Test Example 19 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2055 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 886 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 317 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと、</src>` | 1339 |
| 5 | `<src><\|wait\|></src>` | `<src>信号が消えてできなくなって</src>` | 1932 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 672 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1367 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1275 |
| 9 | `<src>ナットが</src>` | `<src>ヤクネジのナットが</src>` | 1869 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いている</src>` | 2149 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 2794 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 923 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを</src>` | 1427 |

---

### Test Example 20 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1743 |
| 2 | `<src>映画でですね、</src>` | `<src>Aがでですね、</src>` | 1089 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1105 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>A制服かどうか</src>` | 1096 |
| 5 | `<src>調べるときに、</src>` | `<src>メディアアプリの時に</src>` | 1678 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>Aの乱攻を</src>` | 1548 |
| 7 | `<src>ことで、あの</src>` | `<src>調べて、あの</src>` | 1484 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>そのA制服かどうか</src>` | 1513 |
| 9 | `<src>保証する、生息である</src>` | `<src>を調書する、制服である</src>` | 1944 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 2752 |
| 11 | `<src>といったような</src>` | `<src>といったような使い方を</src>` | 1288 |
| 12 | `<src>使い方をされます。</src>` | `<src>されています。</src>` | 1537 |

---

### Test Example 21 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1836 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔치 를 </src>` | 1116 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주게 달라 얘가 주고 내가 </src>` | 1637 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔으러서다. </src>` | 2098 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔치 </src>` | 880 |
| 6 | `<src>죽여 달라 </src>` | `<src>메이플 주게 달라 해줘야 </src>` | 964 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>안 되나? 내가 </src>` | 2570 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>큰 소리 안 듣고 있는 </src>` | 1748 |
| 9 | `<src><\|wait\|></src>` | `<src>주자 는다냐? </src>` | 2802 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 1594 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1821 |

---

### Test Example 22 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1753 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1076 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1073 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy. And when those </src>` | 1175 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1607 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1475 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted </src>` | 2083 |
| 8 | `<src>other types of energy, </src>` | `<src>to other types of energy, </src>` | 1113 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 2073 |
| 10 | `<src><\|wait\|></src>` | `<src>or gets used </src>` | 2733 |
| 11 | `<src>or gets used to make </src>` | `<src>to make </src>` | 1003 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 2151 |

---

### Test Example 23 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1663 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到</src>` | 1057 |
| 3 | `<src>回到我生活</src>` | `<src>我生活的一个</src>` | 1179 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，</src>` | 978 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1623 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好好的站上的时候，</src>` | 1436 |
| 7 | `<src>在做热汤</src>` | `<src>在座日</src>` | 1038 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>堂日能量的实现，</src>` | 2065 |
| 9 | `<src><\|wait\|></src>` | `<src>所以说</src>` | 1854 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时被动的作用</src>` | 3027 |
| 11 | `<src>小小的愿望</src>` | `<src>这么一个小小的小小的一个愿望哈，</src>` | 1243 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 2060 |

---

### Test Example 24 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>またまたちょっと</src>` | 2145 |
| 2 | `<src>距離が</src>` | `<src>距離が離れてくる</src>` | 1115 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>みたいな感じで</src>` | 1244 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>大将が</src>` | 957 |
| 5 | `<src>多いですね。</src>` | `<src>あるこうだったから多いですね。</src>` | 1720 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊したい方って</src>` | 1426 |
| 7 | `<src>すごい</src>` | `<src>すぐ行き来しきい다가</src>` | 2114 |
| 8 | `<src>自己意識高いし、</src>` | `<src>シー</src>` | 803 |
| 9 | `<src>自分で</src>` | `<src>ジレで</src>` | 1695 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>またトトンと鳴る</src>` | 2918 |
| 11 | `<src>傾向が強いので、</src>` | `<src>音して行くので</src>` | 1436 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 2142 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src><\|wait\|></src>` | 1907 |
| 2 | `<src>一切正常，</src>` | `<src>我当时已很正常，</src>` | 1110 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1596 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 596 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开档，</src>` | 1579 |
| 6 | `<src>期间</src>` | `<src>起见大概</src>` | 1500 |
| 7 | `<src>大概有十位医生</src>` | `<src>有十万</src>` | 2172 |
| 8 | `<src>来诊断，</src>` | `<src>一生来设定，</src>` | 879 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 1632 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 2720 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1479 |
| 12 | `<src>他们</src>` | `<src>他能</src>` | 980 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 1537 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or or if you have </src>` | 1923 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 981 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1116 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1094 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1637 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1515 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 1197 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. </src>` | 1692 |
| 9 | `<src>is this word </src>` | `<src>Like, oh, is this word </src>` | 1408 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double p </src>` | 2125 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2424 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double l? I don't know </src>` | 1368 |
| 13 | `<src>know. </src>` | `<src>It </src>` | 1307 |

---

### Test Example 27 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1845 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chirunha Trujillo. </src>` | 1144 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1489 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1556 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>a BA in Finance </src>` | 857 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a BSc in Psychology. </src>` | 1425 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2680 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the university, </src>` | 1052 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1647 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 3421 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1406 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1374 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1796 |
| 2 | `<src><\|wait\|></src>` | `<src>进入了二GIS</src>` | 1066 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>场，</src>` | 990 |
| 4 | `<src>服务</src>` | `<src>还服务</src>` | 1161 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1680 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1424 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 906 |
| 8 | `<src><\|wait\|></src>` | `<src>在做维静</src>` | 2056 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>运动好事几点，你会</src>` | 1320 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 1629 |
| 11 | `<src>给微信公众号评分</src>` | `<src>维静运动好拼分的</src>` | 3078 |
| 12 | `<src>的新榜反而</src>` | `<src>新棒，</src>` | 1504 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1313 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2079 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 1148 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment </src>` | 1122 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1013 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1638 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1437 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1038 |
| 8 | `<src>change can happen </src>` | `<src>happen in the </src>` | 1896 |
| 9 | `<src>in the United States. </src>` | `<src>United States. </src>` | 1479 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2059 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 2418 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 1534 |
| 13 | `<src>myriad. </src>` | `<src>I'm buried. </src>` | 1404 |

---

### Test Example 30 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1679 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>백오십만 개가 종업원 수 </src>` | 1174 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>1천 미만 으로 </src>` | 1573 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1741 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 659 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1362 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 </src>` | 1232 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>성장 하거나 혹은 </src>` | 1694 |
| 9 | `<src>걷게 되는데 </src>` | `<src>폐업 해 길게 되는데 </src>` | 1701 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>이거 는 </src>` | 2683 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>소기업 들은 </src>` | 1584 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>성장 도 폐업 도 하지 않는 </src>` | 1705 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들을 보이 게 된 거죠. </src>` | 1555 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2006 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 985 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 1008 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1194 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1666 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1507 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1293 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊</src>` | 1596 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 1309 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是</src>` | 1654 |
| 11 | `<src><\|wait\|></src>` | `<src>一夜之间就</src>` | 2898 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 385 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 2135 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1441 |

---

### Test Example 32 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1787 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 1149 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 1000일인가 </src>` | 2027 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1644 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>6000줄한 긍정 을 </src>` | 1433 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>보긴 하지, </src>` | 829 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 2139 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연 업 미네랄이다. </src>` | 1343 |
| 9 | `<src>이렇게 </src>` | `<src>이거 이제 </src>` | 1529 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 3114 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 676 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1897 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1360 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new, </src>` | 1875 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1072 |
| 3 | `<src><\|wait\|></src>` | `<src>there were </src>` | 1053 |
| 4 | `<src>such interfaces before, </src>` | `<src>such instances before </src>` | 1090 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1660 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netFilterTC, </src>` | 1387 |
| 7 | `<src>Yeah, so </src>` | `<src>and so </src>` | 733 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 2226 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place </src>` | 1236 |
| 10 | `<src>to look at. </src>` | `<src>where it </src>` | 1539 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 2914 |
| 12 | `<src><\|wait\|></src>` | `<src>developed </src>` | 526 |
| 13 | `<src>developers or engineers </src>` | `<src>or engineered </src>` | 1407 |
| 14 | `<src>working on BugRepo </src>` | `<src>something. OpenBGP should be </src>` | 1414 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1266 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1739 |
| 2 | `<src>我们可以看到的是</src>` | `<src>最长的部分，</src>` | 1091 |
| 3 | `<src>一个在钓鱼</src>` | `<src>我们看到的是一个</src>` | 1390 |
| 4 | `<src>的人，但是</src>` | `<src>戴雪的人，但是他是</src>` | 1931 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>属于逆向的，</src>` | 692 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1277 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>同样的方法</src>` | 1205 |
| 8 | `<src>时候，就要去</src>` | `<src>这样的一个状况，</src>` | 1807 |
| 9 | `<src>特别注意，</src>` | `<src>需要去特别注意的是</src>` | 2188 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能</src>` | 2555 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够得到</src>` | 1252 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与他吊不到</src>` | 1814 |
| 13 | `<src><\|wait\|></src>` | `<src>与你的意识</src>` | 1444 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 1022 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1671 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个天顶，</src>` | 1132 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1241 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了天顶之后，</src>` | 1707 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必</src>` | 979 |
| 6 | `<src><\|wait\|></src>` | `<src>坐下</src>` | 1367 |
| 7 | `<src>先守住，</src>` | `<src>守时，</src>` | 1382 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说“哎呀，</src>` | 1804 |
| 9 | `<src><\|wait\|></src>` | `<src>我再继续操作</src>` | 2114 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦”。</src>` | 2682 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1017 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1667 |
| 13 | `<src><\|wait\|></src>` | `<src>因为呢，</src>` | 1475 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1113 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>二十</src>` | 1897 |
| 2 | `<src>十一二手とか</src>` | `<src>二日とか</src>` | 895 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 317 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1320 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 762 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1644 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1535 |
| 8 | `<src>計算ですか</src>` | `<src>時間ですかね。</src>` | 2397 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 592 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1450 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2012 |
| 12 | `<src><\|wait\|></src>` | `<src>十日</src>` | 2350 |
| 13 | `<src>十一二手で</src>` | `<src>二日で</src>` | 1341 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1246 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1447 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 823 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2082 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1059 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1392 |
| 4 | `<src><\|wait\|></src>` | `<src>and, </src>` | 809 |
| 5 | `<src>and I have ten of them </src>` | `<src>like ten of them that </src>` | 1625 |
| 6 | `<src>that I think are </src>` | `<src>are really </src>` | 1432 |
| 7 | `<src>really important. </src>` | `<src>important, </src>` | 1068 |
| 8 | `<src><\|wait\|></src>` | `<src>so </src>` | 1805 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into </src>` | 1755 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 2613 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 1662 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 1284 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one </src>` | 1363 |
| 14 | `<src>that cover each one </src>` | `<src>in a little more </src>` | 1478 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>detail, </src>` | 902 |

---

### Test Example 38 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1998 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう鳴らせてやるよ。</src>` | 1189 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1226 |
| 4 | `<src><\|wait\|></src>` | `<src>今</src>` | 867 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>引き地を見ている。</src>` | 1676 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1441 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1096 |
| 8 | `<src><\|wait\|></src>` | `<src>超に超えている</src>` | 1840 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈気勢。</src>` | 1408 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1883 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 2573 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなでいくを</src>` | 383 |
| 13 | `<src>が、</src>` | `<src>やってるな。</src>` | 1358 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1480 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1177 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 1010 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1783 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와, </src>` | 1105 |
| 3 | `<src>이방인으로 </src>` | `<src>너희 가 </src>` | 1357 |
| 4 | `<src>있을 때에 </src>` | `<src>이방인으로 있을 때에 </src>` | 1930 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 667 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못 하는 우선에게로 </src>` | 1485 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 </src>` | 2594 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 걸려 </src>` | 691 |
| 9 | `<src><\|wait\|></src>` | `<src>갔느니라. </src>` | 2041 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 </src>` | 2785 |
| 11 | `<src>너희 에게 </src>` | `<src>내가 너희 에게 </src>` | 817 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1466 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 </src>` | 1451 |
| 14 | `<src>말하는 자는. </src>` | `<src>영으로 말하는 자는 </src>` | 1249 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 970 |

---

### Test Example 40 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 1995 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 873 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 496 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1317 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1689 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트 예요. </src>` | 922 |
| 7 | `<src><\|wait\|></src>` | `<src>이게 컨설턴트 예요. </src>` | 1453 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>그리고 </src>` | 2461 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 968 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1791 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>들여 쓸 때 </src>` | 3004 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라는 사람 이 </src>` | 566 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1608 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스 사이트 크리티에서 </src>` | 1547 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 1037 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까 </src>` | 1053 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2001 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1083 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1280 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 905 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? </src>` | 1640 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1544 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 2263 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. </src>` | 726 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 2153 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, </src>` | 2671 |
| 11 | `<src>That's another level of </src>` | `<src>did you graduate? </src>` | 1161 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 1779 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1455 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1202 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 879 |

---

### Test Example 42 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1711 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 1107 |
| 3 | `<src><\|wait\|></src>` | `<src>어 HTM이라고 하는 </src>` | 1528 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 </src>` | 1699 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 771 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1365 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1387 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 1737 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 2005 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 2798 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 </src>` | 1045 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 1950 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1254 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1226 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 991 |

---

### Test Example 43 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1880 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1103 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 1493 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏正财</src>` | 1682 |
| 5 | `<src>也就是</src>` | `<src>的部分。也就是说，</src>` | 806 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面</src>` | 1331 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>的业绩增长</src>` | 1468 |
| 8 | `<src>与收入的</src>` | `<src>所带来的红利</src>` | 1484 |
| 9 | `<src>提升。如果是在</src>` | `<src>与收入的提升，</src>` | 2075 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>如果设投资理财方面</src>` | 3039 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 933 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错的，</src>` | 2058 |
| 13 | `<src>相对正财来说就</src>` | `<src>只是相对正财来说，</src>` | 1379 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微落了那么一点点。</src>` | 1157 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1088 |

---

### Test Example 44 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2136 |
| 2 | `<src><\|wait\|></src>` | `<src>새 문을 </src>` | 1089 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>밝을 거야. </src>` | 1274 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 </src>` | 965 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋든 차리 돋든 </src>` | 1787 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 너무 야. </src>` | 1465 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 2683 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀 자는 거야. </src>` | 1430 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 </src>` | 1677 |
| 10 | `<src>물릴 거고 </src>` | `<src>너무 많이 굴릴 거고 </src>` | 2898 |
| 11 | `<src>신이 오면 </src>` | `<src>시리 굴리 요. </src>` | 1344 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1412 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주잖아. 그러니까 </src>` | 1534 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 마음 에 </src>` | 932 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 716 |

---

### Test Example 45 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어 가면 </src>` | 2088 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 1160 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1366 |
| 4 | `<src><\|wait\|></src>` | `<src>하려고 은 </src>` | 822 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 걸어 다니 고 </src>` | 1740 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>있으면은 </src>` | 1389 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 을 가면 </src>` | 1694 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 1288 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 </src>` | 2180 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장렬이에요. </src>` | 2793 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 챙기 안 해요. </src>` | 1114 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1613 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1432 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>무뤄봐요. 그거 는 </src>` | 1254 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>잘한 것 같아요. </src>` | 1016 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 370 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 </src>` | 1860 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 1039 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인다면 </src>` | 1557 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이러 면 대형 주도 </src>` | 1956 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 505 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1393 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1642 |
| 8 | `<src>이 가벼운 </src>` | `<src>가벼운 </src>` | 1294 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1652 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2583 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 1617 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 </src>` | 1577 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 리 </src>` | 1549 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>초기 가벼운 종목 을 </src>` | 1406 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 </src>` | 1005 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 392 |

---

### Test Example 47 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2031 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어디 를 보면 </src>` | 1134 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1569 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 이런 </src>` | 1688 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 그래도 </src>` | 758 |
| 6 | `<src>그래도 가족 </src>` | `<src>가족 </src>` | 1373 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 2116 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 848 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 1497 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 감보다는 </src>` | 2428 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 2060 |
| 12 | `<src>자기 스스로 </src>` | `<src>쓰는 </src>` | 1623 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1390 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 것을 </src>` | 1127 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 993 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 706 |

---

### Test Example 48 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1892 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1092 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1556 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, because you're </src>` | 2103 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 394 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1359 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 1369 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on </src>` | 1765 |
| 9 | `<src>block and because the </src>` | `<src>the block, and because </src>` | 2222 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 2699 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from </src>` | 916 |
| 12 | `<src>years ago, </src>` | `<src>twenty years ago, </src>` | 1644 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1541 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1168 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 1010 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to a higher standard </src>` | 437 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2016 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1082 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうやつでやって、</src>` | 1505 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルパイソン</src>` | 1567 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね。</src>` | 848 |
| 6 | `<src>というのもフローリフを</src>` | `<src>こういうのも</src>` | 1338 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフとビジュアルの書いて</src>` | 1345 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>あとそれは</src>` | 1568 |
| 9 | `<src>にそこから</src>` | `<src>パイソンコードなんそっから生成される</src>` | 1699 |
| 10 | `<src>生成されて、それが</src>` | `<src>やつで、それが</src>` | 2485 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで信号処理</src>` | 1925 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われるっていう</src>` | 2193 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ことをしている</src>` | 1195 |
| 14 | `<src><\|wait\|></src>` | `<src>からですね。</src>` | 1095 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 1208 |
| 16 | `<src>じゃあ。</src>` | `<src>はいじゃあ</src>` | 579 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1655 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1103 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놨습니다. </src>` | 1730 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 1247 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>이 로쿠 자의 분석 을 보시면 </src>` | 1041 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1369 |
| 7 | `<src>26비트 FP </src>` | `<src>UHD, </src>` | 1317 |
| 8 | `<src>파이프 를 </src>` | `<src>FHD, 4K, </src>` | 1795 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2241 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 보입니다. </src>` | 3190 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 466 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈, </src>` | 1895 |
| 13 | `<src><\|wait\|></src>` | `<src>엑스에서도 없는 </src>` | 1271 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시, </src>` | 1225 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>LSI가 여기 도 없다. </src>` | 1216 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 630 |

---

### Test Example 51 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2008 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩和感觉</src>` | 1093 |
| 3 | `<src>的感情或</src>` | `<src>对手的感情</src>` | 1382 |
| 4 | `<src>真实意图的，</src>` | `<src>或真挚意图的。</src>` | 1922 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 697 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1334 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 1244 |
| 8 | `<src>会听到人们</src>` | `<src>后经场会提到</src>` | 1723 |
| 9 | `<src>这样说：“</src>` | `<src>人们这样说：“</src>` | 1571 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2362 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1865 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在挖墙了。”</src>` | 789 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1682 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1402 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 984 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 1071 |
| 17 | `<src><\|wait\|></src>` | `<src>说：“</src>` | 625 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1681 |
| 2 | `<src>首次觉知到</src>` | `<src>フォローIDの数字</src>` | 1137 |
| 3 | `<src>那个现象：</src>` | `<src>解凍した形像、</src>` | 1722 |
| 4 | `<src>每当我们</src>` | `<src>みたいな</src>` | 1250 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 840 |
| 6 | `<src>处于爱之中，</src>` | `<src>目当を外している</src>` | 1512 |
| 7 | `<src>所谓的爱，</src>` | `<src>小位の愛、</src>` | 1789 |
| 8 | `<src>我们也</src>` | `<src>能めて</src>` | 1169 |
| 9 | `<src>同时进入恨。</src>` | `<src>同時</src>` | 1871 |
| 10 | `<src><\|wait\|></src>` | `<src>進入恨，</src>` | 2728 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候</src>` | 1414 |
| 12 | `<src>它是爱；</src>` | `<src>他撒爱，</src>` | 1460 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1259 |
| 14 | `<src>它就变成恨。</src>` | `<src>他就变成</src>` | 1160 |
| 15 | `<src><\|wait\|></src>` | `<src>恨，</src>` | 978 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆。</src>` | 881 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 663 |
| 18 | `<src>继续在移动。</src>` | `<src>移动。</src>` | 340 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1959 |
| 2 | `<src>Also, </src>` | `<src>Also, you will not </src>` | 1121 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 1493 |
| 4 | `<src>move media objects </src>` | `<src>media objects </src>` | 1454 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 851 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources </src>` | 1402 |
| 7 | `<src>So, if </src>` | `<src>though, if </src>` | 1157 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1768 |
| 9 | `<src>a situation </src>` | `<src>a situation where you </src>` | 1509 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2374 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 2117 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1601 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know. </src>` | 1616 |
| 14 | `<src>and we can see about </src>` | `<src>And we can see about </src>` | 1209 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 966 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure </src>` | 606 |
| 17 | `<src>get backed up </src>` | `<src>they get backed up </src>` | 620 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 353 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2211 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 984 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 963 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1225 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the AHR field </src>` | 1713 |
| 6 | `<src><\|wait\|></src>` | `<src>being of critical </src>` | 1351 |
| 7 | `<src>being of critical importance </src>` | `<src>importance </src>` | 733 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 2143 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 465 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 2021 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 3395 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 448 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree </src>` | 1500 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1459 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these </src>` | 1205 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources </src>` | 902 |
| 17 | `<src>draw from, </src>` | `<src>that we can draw from, </src>` | 713 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 785 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 255 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1736 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1049 |
| 3 | `<src>is hungry. </src>` | `<src>is a son of Henry, </src>` | 1730 |
| 4 | `<src>He knows that </src>` | `<src>he knows that </src>` | 1489 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been told </src>` | 776 |
| 6 | `<src><\|wait\|></src>` | `<src>about the wilderness </src>` | 1388 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>story, that he's hungry, </src>` | 2523 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 612 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 1979 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're a son of God, prove it. </src>` | 3636 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1321 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread, </src>` | 1364 |
| 13 | `<src><\|wait\|></src>` | `<src>and how did he </src>` | 1362 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with that </src>` | 989 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 904 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 644 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead by bread. </src>` | 468 |
| 18 | `<src>by bread alone. </src>` | `<src>Alone. </src>` | 287 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2145 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful, </src>` | 1058 |
| 3 | `<src>right, </src>` | `<src>individual right, </src>` | 1107 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1090 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 1676 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And I don't know </src>` | 1523 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1368 |
| 8 | `<src><\|wait\|></src>` | `<src>the the van </src>` | 1589 |
| 9 | `<src>the the vanguard of social </src>` | `<src>argument of </src>` | 1426 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2050 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 2378 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 567 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect the </src>` | 1846 |
| 14 | `<src>the consensus </src>` | `<src><\|wait\|></src>` | 1244 |
| 15 | `<src><\|wait\|></src>` | `<src>consensus that's already </src>` | 1141 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 1056 |
| 17 | `<src><\|wait\|></src>` | `<src>So, </src>` | 615 |
| 18 | `<src>So you have some </src>` | `<src>you have </src>` | 280 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 311 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 285 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 365 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1911 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1101 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1255 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 946 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1583 |
| 6 | `<src>的部分。</src>` | `<src>客订的部分，</src>` | 1514 |
| 7 | `<src>那客厅一般</src>` | `<src>那客订一般</src>` | 2752 |
| 8 | `<src>都是属于</src>` | `<src>都是</src>` | 556 |
| 9 | `<src>我们</src>` | `<src>属于我们</src>` | 2023 |
| 10 | `<src>在休息的地方，</src>` | `<src>休息的地方，</src>` | 2792 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 897 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的部分</src>` | 1449 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，会反映的是</src>` | 1537 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1122 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 914 |
| 16 | `<src>可以好好的</src>` | `<src>可以好的</src>` | 729 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 707 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可由我们可以看到</src>` | 408 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>这边是放五椅人的嘛，</src>` | 329 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 322 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 297 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1726 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1052 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1107 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 1061 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1671 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 1536 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1283 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1600 |
| 9 | `<src>something of a </src>` | `<src>something that'll have a contradiction. </src>` | 1515 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2186 |
| 11 | `<src>While they're </src>` | `<src>Well, they're </src>` | 2387 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted. </src>` | 1469 |
| 13 | `<src>they also hate </src>` | `<src>They also hate </src>` | 1380 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations, </src>` | 1190 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 944 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 842 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 618 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 390 |
| 19 | `<src>play </src>` | `<src>to play the devil's advocate </src>` | 336 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>a lot, </src>` | 389 |
| 21 | `<src><\|wait\|></src>` | `<src>and they never </src>` | 317 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>shy away from a debate. </src>` | 281 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 268 |
| 24 | `<src><\|wait\|></src>` | `<src>E. and C.P. </src>` | 312 |
| 25 | `<src>ENTP stands for </src>` | `<src>stands for. </src>` | 305 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 </src>` | 1769 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>이준석은 정부 를 </src>` | 1153 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>거부 한 멤버 이 </src>` | 1587 |
| 4 | `<src>위해서 라면서 </src>` | `<src>후보 를 위해서 하며서 </src>` | 1868 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 534 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1343 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제보 생색까지 </src>` | 2676 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 613 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2079 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2953 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 685 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들은 해놓고 </src>` | 2176 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 를 </src>` | 1430 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 955 |
| 15 | `<src><\|wait\|></src>` | `<src>독기 를 품은 </src>` | 1070 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 649 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 403 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 344 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 408 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 285 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납건 </src>` | 325 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 269 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 335 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 학이 얼마나 </src>` | 317 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재 입니까? </src>` | 277 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>で、まあ</src>` | 2032 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今</src>` | 1068 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいです。なので、</src>` | 1757 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>でここのね</src>` | 1586 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ホテルです</src>` | 697 |
| 6 | `<src>も</src>` | `<src>とホテルも</src>` | 1360 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>象徴が食べれる場所</src>` | 2673 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 986 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので、</src>` | 1762 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2784 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドストンホテル</src>` | 799 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1953 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なという方はですね、</src>` | 1375 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさって</src>` | 1067 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てみると、まあいいんじゃない</src>` | 1234 |
| 16 | `<src><\|wait\|></src>` | `<src>かなと。はい。</src>` | 644 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。ここ</src>` | 398 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね。</src>` | 355 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 325 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 158 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 246 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 288 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 290 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいね、まあホテル</src>` | 358 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので、</src>` | 289 |
| 26 | `<src>よかったらですね</src>` | `<src>翌ったらですね、</src>` | 256 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 174 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 159 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね、今回は</src>` | 161 |
