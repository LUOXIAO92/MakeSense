# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9443
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4967
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
  - PROCESS_TIME_MS_AVG: 1458.7500
  - PROCESS_TIME_MS_P50: 1488.9590
  - PROCESS_TIME_MS_P95: 2339.6610
  - PROCESS_TIME_MS_MAX: 3046.3430

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2050 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘撒完以后呢，</src>` | 2184 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力</src>` | 442 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也</src>` | 1193 |
| 5 | `<src>然后</src>` | `<src>衰弱了，</src>` | 1536 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 650 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1505 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 2258 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 889 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1485 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 2167 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要</src>` | 2092 |
| 2 | `<src>家长需要做的是，</src>` | `<src>做的是</src>` | 826 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1730 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深沉的爱</src>` | 1204 |
| 5 | `<src>爱浇水、</src>` | `<src>浇水，</src>` | 837 |
| 6 | `<src>施肥，</src>` | `<src>所以</src>` | 1274 |
| 7 | `<src>给足</src>` | `<src><\|wait\|></src>` | 975 |
| 8 | `<src>孩子心理营养，</src>` | `<src>给子孩子心里营养，</src>` | 2648 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1228 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>给耐心等</src>` | 1582 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 2153 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2021 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气鼠是容易的，</src>` | 2289 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 363 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有</src>` | 1159 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导到</src>` | 1389 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 813 |
| 7 | `<src>处于中间，</src>` | `<src>如波处于中，</src>` | 1192 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2219 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1048 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 1487 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅，</src>` | 2436 |

---

### Test Example 4 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying </src>` | 1809 |
| 2 | `<src>Did very important research </src>` | `<src>important research </src>` | 860 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1702 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1301 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1385 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 776 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 1153 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2523 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1027 |
| 10 | `<src>out there, </src>` | `<src>out there, people that </src>` | 1678 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 2159 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2233 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>乖的送子儿队，</src>` | 2318 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个游行</src>` | 354 |
| 4 | `<src>然后</src>` | `<src>也很大，</src>` | 1221 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 1475 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放的</src>` | 647 |
| 7 | `<src>儿核桃</src>` | `<src>和陶人，</src>` | 1320 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2461 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>可以的吧？</src>` | 1072 |
| 10 | `<src>这种核桃</src>` | `<src>这种和陶人，</src>` | 1999 |
| 11 | `<src>仁儿。</src>` | `<src><\|wait\|></src>` | 1683 |

---

### Test Example 6 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1830 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Apple, </src>` | 834 |
| 3 | `<src>촉발 시키고 </src>` | `<src>축복 하시 기고 </src>` | 1761 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1145 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 680 |
| 6 | `<src><\|wait\|></src>` | `<src>보호자에게 </src>` | 1606 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>해루나 </src>` | 1768 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2205 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 997 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 1935 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>있습니다. </src>` | 1724 |

---

### Test Example 7 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1698 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 858 |
| 3 | `<src>これなんかまだ</src>` | `<src>子供がまだ</src>` | 1707 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1134 |
| 5 | `<src>この時点で</src>` | `<src>その時点で</src>` | 673 |
| 6 | `<src>こう短く</src>` | `<src>こう身近く</src>` | 1683 |
| 7 | `<src>剪定を</src>` | `<src>選挙を</src>` | 1848 |
| 8 | `<src><\|wait\|></src>` | `<src>こう退ずして</src>` | 2202 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>あげると</src>` | 891 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 1936 |
| 11 | `<src>大した。</src>` | `<src>退した。</src>` | 1784 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>面对</src>` | 1828 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>这个情况，我们就是</src>` | 847 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题，</src>` | 1733 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1231 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 932 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们笑这个状况，</src>` | 1327 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1549 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 2512 |
| 9 | `<src>独立承担。</src>` | `<src>你無理承担。</src>` | 1006 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1995 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是给主诉。</src>` | 1667 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1982 |
| 2 | `<src>옹심이, </src>` | `<src>용심이 </src>` | 851 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1714 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심이 </src>` | 1219 |
| 5 | `<src>옹심이가 </src>` | `<src>새우 칼 용심이 가 </src>` | 1238 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 981 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. 야 </src>` | 1893 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 2164 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1009 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해행으로도 조금 죽입니다. </src>` | 2141 |
| 11 | `<src>진짜. </src>` | `<src>정말 </src>` | 1598 |

---

### Test Example 10 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명단 에 있는 </src>` | 2215 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성들은 </src>` | 1918 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 651 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고, </src>` | 1344 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1647 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 727 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성들이었기 </src>` | 1940 |
| 8 | `<src>때문 입니다. </src>` | `<src>때문 입니다. </src>` | 2130 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1093 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2176 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐던 교사 들은 </src>` | 1775 |

---

### Test Example 11 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2139 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 831 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくという</src>` | 1680 |
| 4 | `<src>といったようなものも</src>` | `<src>ようなものも用意しております</src>` | 1109 |
| 5 | `<src>用意しておりますので</src>` | `<src>のでぜひ</src>` | 518 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 1832 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 951 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 2452 |
| 9 | `<src>えっと</src>` | `<src>ので、</src>` | 1112 |
| 10 | `<src><\|wait\|></src>` | `<src>また</src>` | 1314 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>内訳がありますので、</src>` | 2457 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>商品お待ちください。</src>` | 1445 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2065 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1716 |
| 3 | `<src>始めた</src>` | `<src>始まった</src>` | 819 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1107 |
| 5 | `<src>ゴッホ、</src>` | `<src>合法、</src>` | 519 |
| 6 | `<src>ゴーギャン、</src>` | `<src>合業、</src>` | 1826 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1180 |
| 8 | `<src>セザンヌ、</src>` | `<src>生産の</src>` | 2292 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1161 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の絵</src>` | 1622 |
| 11 | `<src>は、田舎の</src>` | `<src><\|wait\|></src>` | 2195 |
| 12 | `<src>中学生でも。</src>` | `<src>は田舎の中学生でも</src>` | 1580 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあ</src>` | 2173 |
| 2 | `<src>距離が</src>` | `<src>なんとなくちょっと距離が</src>` | 866 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1737 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>おしゃれとかって</src>` | 1151 |
| 5 | `<src>多いですね。</src>` | `<src>やっぱりですね</src>` | 902 |
| 6 | `<src>開業したい方って</src>` | `<src>回避したい方って</src>` | 1396 |
| 7 | `<src>すごい</src>` | `<src>すごい息苦しく</src>` | 1657 |
| 8 | `<src>自己意識高いし、</src>` | `<src>たがし、</src>` | 2298 |
| 9 | `<src>自分で</src>` | `<src>実際に</src>` | 800 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>ちょっとほんまに</src>` | 1789 |
| 11 | `<src>傾向が強いので、</src>` | `<src>お互い仕事強いので</src>` | 2061 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1698 |

---

### Test Example 14 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 이렇 지 너무 </src>` | 2013 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1767 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>인절미를 해줄 수 있지만 </src>` | 872 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1258 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 2044 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 피라고 </src>` | 1317 |
| 7 | `<src>뭐 있고 </src>` | `<src>하고 있고 </src>` | 2249 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 1083 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 피라고 보이 색이 </src>` | 1631 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 가진다 한 뒤 보살 이란 </src>` | 2406 |
| 11 | `<src>보살 이라는데. </src>` | `<src><\|wait\|></src>` | 1770 |

---

### Test Example 15 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1854 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 832 |
| 3 | `<src><\|wait\|></src>` | `<src>天国という</src>` | 1741 |
| 4 | `<src>テキという設備寺が</src>` | `<src>設定値が</src>` | 1130 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 650 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1499 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 917 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井教授の仕組み</src>` | 2425 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 936 |
| 10 | `<src>は五経、</src>` | `<src>五孔、</src>` | 933 |
| 11 | `<src><\|wait\|></src>` | `<src>設定値</src>` | 1890 |
| 12 | `<src>設備寺、五比</src>` | `<src>五ビジ</src>` | 1760 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1768 |

---

### Test Example 16 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1708 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到</src>` | 1814 |
| 3 | `<src>回到我生活</src>` | `<src>我生活的一个</src>` | 798 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，</src>` | 1213 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1061 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好自在的状态的时候，</src>` | 1099 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 927 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭的</src>` | 2633 |
| 9 | `<src><\|wait\|></src>` | `<src>时候，我当时</src>` | 1157 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被他做作业</src>` | 1669 |
| 11 | `<src>小小的愿望</src>` | `<src>的这个小小的愿望哈，</src>` | 2311 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 1851 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1937 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 산지 를 </src>` | 2071 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주게 달라 해가지고 내가 </src>` | 631 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주길 넣고 들어왔어도 </src>` | 1237 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔치 </src>` | 1821 |
| 6 | `<src>죽여 달라 </src>` | `<src>메이플을 하려 하잖아 </src>` | 1132 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>했냐? 내가 </src>` | 2546 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>이런 소리 안 듣고 있는 </src>` | 1413 |
| 9 | `<src><\|wait\|></src>` | `<src>주판은요. </src>` | 2053 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아 </src>` | 1764 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1859 |

---

### Test Example 18 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1735 |
| 2 | `<src>doing? </src>` | `<src><\|wait\|></src>` | 1782 |
| 3 | `<src>Drop into </src>` | `<src>saying? Drop pin to your body. </src>` | 895 |
| 4 | `<src>your body. </src>` | `<src><\|wait\|></src>` | 1189 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 2009 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1097 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 2788 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 1286 |
| 9 | `<src>I ask them what </src>` | `<src>Or is the body </src>` | 2069 |
| 10 | `<src><\|wait\|></src>` | `<src>language </src>` | 1559 |
| 11 | `<src>language are you using? </src>` | `<src>you're using? </src>` | 1993 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1783 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 2078 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人之间</src>` | 630 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1174 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>有着某种荣幸，</src>` | 1719 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 689 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1734 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从天黎尔</src>` | 2199 |
| 9 | `<src><\|wait\|></src>` | `<src>开始的？</src>` | 955 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2059 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思</src>` | 1907 |
| 12 | `<src>连篇。</src>` | `<src>与年篇。</src>` | 1764 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1849 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1928 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 662 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1217 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1660 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 527 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1893 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 2472 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 1463 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets used </src>` | 2389 |
| 11 | `<src>or gets used to make </src>` | `<src>to make </src>` | 1273 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1535 |

---

### Test Example 21 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2151 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1814 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 748 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learned to repeat. </src>` | 1357 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find out what you're good at. </src>` | 2143 |
| 6 | `<src>and do more of it. </src>` | `<src>And do more of it. </src>` | 1760 |
| 7 | `<src><\|wait\|></src>` | `<src>And what you're not good </src>` | 2568 |
| 8 | `<src>And what you're not good at, </src>` | `<src>at, get to people </src>` | 1241 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>around you to help you with </src>` | 2556 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1347 |
| 11 | `<src>And until next time. </src>` | `<src>it. And until next time, </src>` | 1880 |

---

### Test Example 22 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1831 |
| 2 | `<src>映画でですね、</src>` | `<src>Aがですね、</src>` | 1846 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 802 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>円制速度かどうかっていう</src>` | 1322 |
| 5 | `<src>調べるときに、</src>` | `<src>場合において、</src>` | 1789 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>Aの乱交調べ</src>` | 967 |
| 7 | `<src>ことで、あの</src>` | `<src>ということで、あの</src>` | 1945 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>そのその制速度かどうかっていう</src>` | 1993 |
| 9 | `<src>保証する、生息である</src>` | `<src>調べる制速度</src>` | 1524 |
| 10 | `<src>ことを保証する</src>` | `<src>であることを保証するといった</src>` | 2252 |
| 11 | `<src>といったような</src>` | `<src>使い方を</src>` | 1347 |
| 12 | `<src>使い方をされます。</src>` | `<src>定めました。</src>` | 1862 |

---

### Test Example 23 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2149 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 824 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 1730 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと信号が</src>` | 1129 |
| 5 | `<src><\|wait\|></src>` | `<src>消えてできなくなって</src>` | 565 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 1740 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 972 |
| 8 | `<src>役ねじの</src>` | `<src>逆ネジの</src>` | 2532 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1176 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうこと</src>` | 1593 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 2024 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1457 |
| 13 | `<src>分解完了。</src>` | `<src>ハイ分解完了。</src>` | 1909 |

---

### Test Example 24 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个</src>` | 1862 |
| 2 | `<src><\|wait\|></src>` | `<src>就是进入了</src>` | 1720 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二classList，</src>` | 863 |
| 4 | `<src>服务</src>` | `<src>并服务于</src>` | 1210 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 987 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1286 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1269 |
| 8 | `<src><\|wait\|></src>` | `<src>在做</src>` | 2255 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>维信运动好事几点，</src>` | 1272 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1742 |
| 11 | `<src>给微信公众号评分</src>` | `<src>维信运动</src>` | 1870 |
| 12 | `<src>的新榜反而</src>` | `<src>平分的星棒</src>` | 1736 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1682 |

---

### Test Example 25 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2214 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1938 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 698 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1180 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 983 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1200 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1144 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2292 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1232 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1585 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2151 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game.board array. </src>` | 1769 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1685 |

---

### Test Example 26 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1934 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chirun Hattori, </src>` | 2172 |
| 3 | `<src>I am currently </src>` | `<src>and I am currently studying </src>` | 477 |
| 4 | `<src><\|wait\|></src>` | `<src>a BA in </src>` | 1249 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>Business Finance </src>` | 1812 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a B.A. in Psychology. </src>` | 1101 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2449 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at Yale, </src>` | 1229 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1519 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2599 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1679 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1572 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2180 |
| 2 | `<src>The meaning of </src>` | `<src><\|wait\|></src>` | 1814 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 836 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1213 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1489 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 629 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1529 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 2278 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1174 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1935 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1780 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 1998 |
| 13 | `<src>myriad. </src>` | `<src>I'mirred. </src>` | 1578 |

---

### Test Example 28 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒</src>` | 2019 |
| 2 | `<src>要提醒大家，</src>` | `<src>大家，</src>` | 853 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1726 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1212 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 880 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1318 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 870 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊、</src>` | 2441 |
| 9 | `<src>也不可能是</src>` | `<src>风险</src>` | 1128 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是</src>` | 1090 |
| 11 | `<src><\|wait\|></src>` | `<src>一夜之间就</src>` | 2373 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1574 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1567 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1567 |

---

### Test Example 29 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src><\|wait\|></src>` | 1975 |
| 2 | `<src>一切正常，</src>` | `<src>我当时一切正常，</src>` | 2073 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>毫无反应，</src>` | 560 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1227 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持打开，</src>` | 2094 |
| 6 | `<src>期间</src>` | `<src>奇迹大大盖</src>` | 941 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 2462 |
| 8 | `<src>来诊断，</src>` | `<src>由神位医生来审断。</src>` | 1353 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿，</src>` | 1746 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 1980 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1419 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 1833 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>愉快地开。</src>` | 1121 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Well, or if you have </src>` | 1995 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 1640 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 863 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1167 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 721 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1613 |
| 7 | `<src>to spell </src>` | `<src>how to spell the word(s), </src>` | 2069 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>like," Oh, is </src>` | 2277 |
| 9 | `<src>is this word </src>` | `<src>this word </src>` | 1281 |
| 10 | `<src>spelled with a double </src>` | `<src>starts with a double P?" </src>` | 2574 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1403 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>Double P." I don't know </src>` | 2069 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1260 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 1887 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>이것 들은 </src>` | 2036 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 1000이라는 </src>` | 634 |
| 4 | `<src>이제 거진 </src>` | `<src>거진 </src>` | 1115 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 중량 을 </src>` | 1288 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>가지 고 굉장히 </src>` | 894 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 1827 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연히 미네랄 이다. </src>` | 2674 |
| 9 | `<src>이렇게 </src>` | `<src>이것 들은 </src>` | 1485 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>기여 할 정도 의 </src>` | 2441 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>제 그런 거죠. 이제 </src>` | 1599 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1789 |
| 13 | `<src>아연. </src>` | `<src>아니면. </src>` | 1236 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1795 |
| 2 | `<src>我们可以看到的是</src>` | `<src>这一张的部分，</src>` | 2077 |
| 3 | `<src>一个在钓鱼</src>` | `<src>我们看到的是一个</src>` | 585 |
| 4 | `<src>的人，但是</src>` | `<src>戴雪的人，但是</src>` | 1261 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的。</src>` | 1738 |
| 6 | `<src>所以</src>` | `<src>这通场</src>` | 944 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>有没有这样的一个状况呢？</src>` | 2102 |
| 8 | `<src>时候，就要去</src>` | `<src>受到</src>` | 1328 |
| 9 | `<src>特别注意，</src>` | `<src>去特别注意的是，</src>` | 1011 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能</src>` | 1866 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够得到</src>` | 1704 |
| 12 | `<src>它钓不到鱼</src>` | `<src>于他吊不到</src>` | 1782 |
| 13 | `<src><\|wait\|></src>` | `<src>于他的益处？</src>` | 1683 |
| 14 | `<src>的意思哦。</src>` | `<src><\|wait\|></src>` | 1286 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1778 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개가 </src>` | 2063 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중화 본 것으로 유명 미만 으로 </src>` | 639 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1213 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1875 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 986 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 </src>` | 2482 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>성장 하거나 혹은 </src>` | 1396 |
| 9 | `<src>걷게 되는데 </src>` | `<src>회업의 길을 걷게 되는데 </src>` | 1979 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>회업을 </src>` | 1876 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>소기업 들은 성장 도 </src>` | 1911 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>패업도 하지 않은 현상 들을 </src>` | 1760 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1392 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 1909 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 862 |
| 3 | `<src><\|wait\|></src>` | `<src>there was </src>` | 1679 |
| 4 | `<src>such interfaces before, </src>` | `<src>such instances before, </src>` | 242 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1139 |
| 6 | `<src>netfilter, TC. </src>` | `<src>next future TC, </src>` | 1746 |
| 7 | `<src>Yeah, so </src>` | `<src><\|wait\|></src>` | 849 |
| 8 | `<src>this is just </src>` | `<src>and so this is just </src>` | 2007 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1745 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 947 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 2037 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1776 |
| 13 | `<src>developers or engineers </src>` | `<src>But developers or engineers </src>` | 1839 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on Bug Repositories </src>` | 1687 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1351 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>达到了</src>` | 1696 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>一个天顶，</src>` | 1991 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 658 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了天顶之后，</src>` | 1300 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1816 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 958 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1947 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想着哎，</src>` | 1746 |
| 9 | `<src><\|wait\|></src>` | `<src>那我再去做</src>` | 1425 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>操作下去哦。</src>` | 2438 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1298 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1838 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1418 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1195 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2154 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1771 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 790 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1147 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I got ten of them </src>` | 1050 |
| 6 | `<src>that I think are </src>` | `<src>that are really important </src>` | 1182 |
| 7 | `<src>really important. </src>` | `<src><\|wait\|></src>` | 1634 |
| 8 | `<src><\|wait\|></src>` | `<src>to </src>` | 2062 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go and do </src>` | 1177 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 1908 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 1680 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video. </src>` | 1681 |
| 13 | `<src><\|wait\|></src>` | `<src>It'll cover each one, </src>` | 1791 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1380 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>and a little more detail, </src>` | 1262 |

---

### Test Example 37 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2219 |
| 2 | `<src><\|wait\|></src>` | `<src>새워라 빌고 </src>` | 2093 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>내가 </src>` | 469 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>이제 서름이 </src>` | 1159 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋은 자태 리 </src>` | 982 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>돋은 느낌 이 온이야. </src>` | 1364 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 944 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 2780 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 1035 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1740 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 너 </src>` | 1983 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>지켜 주라고 </src>` | 1751 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주라고 하니까 </src>` | 1784 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1414 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1183 |

---

### Test Example 38 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1949 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 2155 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 471 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏正财的部分</src>` | 1254 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1295 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面</src>` | 803 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>的业绩增长</src>` | 1803 |
| 8 | `<src>与收入的</src>` | `<src>所带来的红利，</src>` | 2257 |
| 9 | `<src>提升。如果是在</src>` | `<src>也就是提升。如果</src>` | 1013 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面</src>` | 2132 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1776 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错的，只是</src>` | 1829 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对整体来说，</src>` | 1570 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了</src>` | 1236 |
| 15 | `<src><\|wait\|></src>` | `<src>那么一点。</src>` | 1037 |

---

### Test Example 39 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1773 |
| 2 | `<src>HTML이라고 </src>` | `<src>呃，</src>` | 1692 |
| 3 | `<src><\|wait\|></src>` | `<src>HCL이라고 하는 </src>` | 867 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴피터도 </src>` | 1198 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1179 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1106 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1530 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 2519 |
| 9 | `<src>문법 에 </src>` | `<src>문법 의 </src>` | 950 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>말 이렇게 우리 가 이제 </src>` | 2115 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>초드들을 </src>` | 1630 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 2023 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드들을 </src>` | 1521 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1305 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1096 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1841 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 </src>` | 2056 |
| 3 | `<src>이방인으로 </src>` | `<src>너희 가 이방인으로 </src>` | 629 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1187 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1695 |
| 6 | `<src>우상에게로 </src>` | `<src>우상 에게로 </src>` | 552 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그대로 </src>` | 1826 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 2509 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1425 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2340 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1379 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1910 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1390 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1290 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 947 |

---

### Test Example 41 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2116 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 844 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1819 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1211 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>이 동생 이자 </src>` | 1397 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 도 가족 </src>` | 818 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 1879 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 2103 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 734 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 한 거다는 </src>` | 1803 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 1964 |
| 12 | `<src>자기 스스로 </src>` | `<src>좀 </src>` | 1642 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1653 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1232 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려 놓고 </src>` | 1153 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>생각 했습니다. </src>` | 1093 |

---

### Test Example 42 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 2102 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>蒸らせてやる。</src>` | 1833 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 739 |
| 4 | `<src><\|wait\|></src>` | `<src>今</src>` | 1097 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>引き締めている。</src>` | 521 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1772 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 898 |
| 8 | `<src><\|wait\|></src>` | `<src>超に超えている</src>` | 2624 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈火勢気よ。</src>` | 1264 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1630 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1970 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなデイクーを</src>` | 1545 |
| 13 | `<src>が、</src>` | `<src>やってるら。</src>` | 1829 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1366 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>解毒線を</src>` | 1178 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 1244 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2083 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. How far </src>` | 2194 |
| 3 | `<src>How far did you </src>` | `<src>did you </src>` | 432 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go in your </src>` | 1284 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>education? Did you </src>` | 1816 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1004 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 2425 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. Did you </src>` | 1329 |
| 9 | `<src>to college, </src>` | `<src>go to college, </src>` | 1421 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2549 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1850 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1602 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now. </src>` | 1461 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you </src>` | 1186 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1067 |

---

### Test Example 44 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2017 |
| 2 | `<src>十一二手とか</src>` | `<src>十一日とか</src>` | 1829 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>言ってた。恐らく</src>` | 829 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1258 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1730 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 684 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1946 |
| 8 | `<src>計算ですか</src>` | `<src>時間ですかね。</src>` | 1969 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 1018 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2140 |
| 11 | `<src>おそらく</src>` | `<src>恐らく</src>` | 1822 |
| 12 | `<src><\|wait\|></src>` | `<src>十一日</src>` | 1688 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1496 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1207 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1071 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 992 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2096 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 2046 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうのが出てきて、</src>` | 597 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルPython</src>` | 1205 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね。</src>` | 1936 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも</src>` | 905 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルン</src>` | 2103 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>と書いてあとそれは</src>` | 1550 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコードが</src>` | 1114 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成されて、それが</src>` | 2689 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで信号処理</src>` | 1378 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われるっていう</src>` | 1678 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ことをしているから</src>` | 1430 |
| 14 | `<src><\|wait\|></src>` | `<src>です。</src>` | 1112 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 1028 |
| 16 | `<src>じゃあ。</src>` | `<src>はいじゃあ</src>` | 908 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2228 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 해맨이다. </src>` | 2162 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 448 |
| 4 | `<src><\|wait\|></src>` | `<src>하고 온 거로 </src>` | 1254 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 다니 고 </src>` | 1766 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>간에 뭐 </src>` | 926 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 1909 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 1872 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 는 것도 작열이에요. </src>` | 1333 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 2288 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1517 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1533 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1538 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모여 봐요. 그거 는 </src>` | 1405 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>된 거 같아요. </src>` | 986 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 754 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 2079 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1728 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들이 있습니다. 저희 가 </src>` | 986 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1248 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1711 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트 예요. </src>` | 978 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이 컨설턴트 에게 </src>` | 2223 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>해주고 A라는 </src>` | 1532 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 884 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2528 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 1622 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1600 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1514 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스 사이트 스큐티에서 </src>` | 1366 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>X 파일까지 </src>` | 1083 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 798 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2074 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感觉</src>` | 1934 |
| 3 | `<src>的感情或</src>` | `<src>对手的感情</src>` | 686 |
| 4 | `<src>真实意图的，</src>` | `<src>或真实意图的。</src>` | 1282 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1691 |
| 6 | `<src><\|wait\|></src>` | `<src>很多</src>` | 535 |
| 7 | `<src>很多时候经常</src>` | `<src>时候，</src>` | 1782 |
| 8 | `<src>会听到人们</src>` | `<src>经常会听到</src>` | 2177 |
| 9 | `<src>这样说：“</src>` | `<src>人们这样说：“</src>` | 1082 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2000 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1603 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在作谎了。”</src>` | 2024 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1463 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1335 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1081 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 1000 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 648 |

---

### Test Example 49 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 </src>` | 1920 |
| 2 | `<src><\|wait\|></src>` | `<src>인상 되는 </src>` | 1781 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다음 에 </src>` | 859 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1252 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1893 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1078 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2379 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 1218 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1589 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2335 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 1472 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 1961 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1347 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1347 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 1138 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 642 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1729 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1929 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놨습니다. </src>` | 771 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자예요. </src>` | 1222 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 2027 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1270 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 칩에 </src>` | 2672 |
| 8 | `<src>파이프 를 </src>` | `<src>FPD 파이 를 </src>` | 1130 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2144 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것이 로커인이다. </src>` | 1929 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1720 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈, </src>` | 1588 |
| 13 | `<src><\|wait\|></src>` | `<src>엑스에서도 없는 </src>` | 1303 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시, </src>` | 1237 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>LSi가 여기 도 없다. </src>` | 822 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 629 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1998 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1814 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 840 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 1236 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 2153 |
| 6 | `<src>but the reality </src>` | `<src><\|wait\|></src>` | 1868 |
| 7 | `<src>is is that </src>` | `<src>But the reality is that </src>` | 2323 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on </src>` | 1212 |
| 9 | `<src>block and because the </src>` | `<src>the block, and because </src>` | 2318 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 1582 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from </src>` | 1598 |
| 12 | `<src>years ago, </src>` | `<src>twenty years ago, </src>` | 1567 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1351 |
| 14 | `<src>a higher standard because </src>` | `<src>higher standards </src>` | 967 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 916 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to higher standards. </src>` | 741 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1778 |
| 2 | `<src>首次觉知到</src>` | `<src>FourthE的首支</src>` | 1935 |
| 3 | `<src>那个现象：</src>` | `<src>觉知到了那个现象，</src>` | 730 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1240 |
| 5 | `<src><\|wait\|></src>` | `<src>美当我们处于</src>` | 1741 |
| 6 | `<src>处于爱之中，</src>` | `<src>爱之中，</src>` | 855 |
| 7 | `<src>所谓的爱，</src>` | `<src>所有的爱</src>` | 1602 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 2112 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时</src>` | 961 |
| 10 | `<src><\|wait\|></src>` | `<src>进入恨，</src>` | 2045 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 2001 |
| 12 | `<src>它是爱；</src>` | `<src>他是在</src>` | 1676 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1510 |
| 14 | `<src>它就变成恨。</src>` | `<src>他就变成</src>` | 1303 |
| 15 | `<src><\|wait\|></src>` | `<src>恨，</src>` | 992 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆。</src>` | 990 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 647 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 454 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2290 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1656 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 867 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1111 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the AHR field, </src>` | 805 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1561 |
| 7 | `<src>being of critical importance </src>` | `<src>and of critical importance </src>` | 891 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 2350 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1129 |
| 10 | `<src>databases, </src>` | `<src>variant databases, which is obviously </src>` | 1194 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>one of my loves. </src>` | 2509 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 1395 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree upon </src>` | 1869 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 1347 |
| 15 | `<src>to be in these </src>` | `<src><\|wait\|></src>` | 1335 |
| 16 | `<src>data sources that we can </src>` | `<src>to be in these data sources that we can </src>` | 1431 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 326 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 684 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 404 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2032 |
| 2 | `<src>Also, </src>` | `<src>Also, you will not </src>` | 2073 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 587 |
| 4 | `<src>move media objects </src>` | `<src>meadia objects </src>` | 1237 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1755 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1020 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1804 |
| 8 | `<src>you get into </src>` | `<src>you get into a </src>` | 1897 |
| 9 | `<src>a situation </src>` | `<src>situation where you </src>` | 1135 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2580 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 1330 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1613 |
| 13 | `<src>you need to let us know, </src>` | `<src>we can do </src>` | 1628 |
| 14 | `<src>and we can see about </src>` | `<src>us. Now, and we can see about </src>` | 1573 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1096 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files </src>` | 406 |
| 17 | `<src>get backed up </src>` | `<src>and then making sure they get back up </src>` | 752 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 427 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1785 |
| 2 | `<src>he knows Jesus </src>` | `<src>and Noah's Jesus </src>` | 2154 |
| 3 | `<src>is hungry. </src>` | `<src>was hungry, </src>` | 451 |
| 4 | `<src>He knows that </src>` | `<src>and he knows that he's </src>` | 1306 |
| 5 | `<src>he's been without food, </src>` | `<src>going to </src>` | 1818 |
| 6 | `<src><\|wait\|></src>` | `<src>be in the wilderness </src>` | 960 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>for a short time, that he's hungry, </src>` | 3046 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 1052 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 1822 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 2182 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1979 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread. </src>` | 1460 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1324 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that? </src>` | 1128 |
| 15 | `<src>temptation? </src>` | `<src>That temptation. </src>` | 989 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 656 |
| 17 | `<src>Man shall not live </src>` | `<src>Man, Jonathan lead by bread. </src>` | 501 |
| 18 | `<src>by bread alone. </src>` | `<src>Alone. </src>` | 338 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2251 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful, </src>` | 1817 |
| 3 | `<src>right, </src>` | `<src>individual right, </src>` | 786 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1218 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 977 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't know </src>` | 1416 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 2040 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1960 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the vanguard of </src>` | 953 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2011 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 1741 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1874 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 1462 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1228 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1169 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 1021 |
| 17 | `<src><\|wait\|></src>` | `<src>So. </src>` | 649 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 315 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 282 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 379 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 402 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1997 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片呢，</src>` | 1931 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 678 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 1275 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1829 |
| 6 | `<src>的部分。</src>` | `<src>客亭的部分，</src>` | 978 |
| 7 | `<src>那客厅一般</src>` | `<src>而客亭一般</src>` | 2004 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1387 |
| 9 | `<src>我们</src>` | `<src><\|wait\|></src>` | 1010 |
| 10 | `<src>在休息的地方，</src>` | `<src>我们在休息的地方，</src>` | 2120 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 2008 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的部分，</src>` | 1769 |
| 13 | `<src>也会反映的是</src>` | `<src>会反映的是</src>` | 1563 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1292 |
| 15 | `<src>一点时间，</src>` | `<src><\|wait\|></src>` | 950 |
| 16 | `<src>可以好好的</src>` | `<src>一点时间可以好的</src>` | 919 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>做一下休息，</src>` | 643 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们看到这边是</src>` | 472 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛。</src>` | 322 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 159 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 407 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1794 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1822 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 747 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1103 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 658 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1693 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1314 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 2461 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1072 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 1905 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1862 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, they also </src>` | 1907 |
| 13 | `<src>they also hate </src>` | `<src><\|wait\|></src>` | 1601 |
| 14 | `<src>meaningless conversations </src>` | `<src>hate meaningless conversations. </src>` | 1359 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1045 |
| 16 | `<src><\|wait\|></src>` | `<src>And like it </src>` | 1039 |
| 17 | `<src>get straight to the point. </src>` | `<src>gets straight to the point. </src>` | 237 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 610 |
| 19 | `<src>play </src>` | `<src>to play the devil's advocate </src>` | 510 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and then </src>` | 346 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 286 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 200 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 234 |
| 24 | `<src><\|wait\|></src>` | `<src>E.g., </src>` | 300 |
| 25 | `<src>ENTP stands for </src>` | `<src>N.P. Stanfor. </src>` | 294 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 의 이준석은 </src>` | 1892 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>강무를 거부 한 </src>` | 2145 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 493 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1198 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선을 </src>` | 1932 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 986 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2575 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1228 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1543 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2273 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1425 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들은 해놓고 </src>` | 2004 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 를 </src>` | 1349 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리겠다는 </src>` | 1244 |
| 15 | `<src><\|wait\|></src>` | `<src>독기 를 품은 </src>` | 1091 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 251 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로. </src>` | 677 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 것이 </src>` | 467 |
| 19 | `<src>것입니다. </src>` | `<src>입니다. </src>` | 367 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 435 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납건. </src>` | 313 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 253 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 285 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 에 얼마나 </src>` | 251 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 296 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2059 |
| 2 | `<src>食堂ね</src>` | `<src>食後のね</src>` | 1729 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってみたいです。なので</src>` | 952 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>ここで</src>` | 1108 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>このホテルズンホテル</src>` | 1138 |
| 6 | `<src>も</src>` | `<src>も朝食が</src>` | 1156 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 1719 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 2021 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になっているので</src>` | 1035 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 1646 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドストンホテル</src>` | 2067 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたりな</src>` | 1764 |
| 13 | `<src>なっていう方はですね</src>` | `<src>っていう方はですね</src>` | 1715 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさって</src>` | 1342 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てみるとまあいいんじゃない</src>` | 1191 |
| 16 | `<src><\|wait\|></src>` | `<src>なと</src>` | 1122 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。ここ</src>` | 492 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ホテルからですね</src>` | 259 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 460 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 409 |
| 21 | `<src>歩いて一分</src>` | `<src>一本かかる</src>` | 434 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かからないか</src>` | 263 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね立地の</src>` | 292 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>いいねまあホテル</src>` | 277 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 255 |
| 26 | `<src>よかったらですね</src>` | `<src>翌ったらですね</src>` | 284 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさって</src>` | 167 |
| 28 | `<src>ください</src>` | `<src>みてください。それで</src>` | 150 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ですね今回は</src>` | 142 |
