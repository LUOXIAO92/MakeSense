# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9331
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5099
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
  - PROCESS_TIME_MS_AVG: 1444.1990
  - PROCESS_TIME_MS_P50: 1543.5840
  - PROCESS_TIME_MS_P95: 2217.1550
  - PROCESS_TIME_MS_MAX: 2613.1480

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
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1899 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要切肤式容易的，</src>` | 2177 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 870 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有</src>` | 753 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导到</src>` | 1746 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 777 |
| 7 | `<src>处于中间，</src>` | `<src>如喝出于终前</src>` | 1378 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1728 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1169 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 1803 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅，</src>` | 1669 |

---

### Test Example 2 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1727 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Abbotrol. </src>` | 980 |
| 3 | `<src>촉발 시키고 </src>` | `<src>욕받이시키고 </src>` | 1840 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 972 |
| 5 | `<src>자신 의 </src>` | `<src>자신의 </src>` | 1224 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 1268 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>헬레나 </src>` | 1305 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1887 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1190 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 1875 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>입니다. </src>` | 1891 |

---

### Test Example 3 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2124 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성들은 </src>` | 869 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1558 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1247 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 881 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 1645 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성들이 </src>` | 1342 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1932 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1438 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 1648 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교수 たちは </src>` | 2085 |

---

### Test Example 4 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1766 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，</src>` | 1776 |
| 3 | `<src>遇到问题</src>` | `<src>我们就遇到问题</src>` | 900 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1121 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1541 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们笑这个状况，</src>` | 967 |
| 7 | `<src>不要想自己</src>` | `<src><\|wait\|></src>` | 1330 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>不要想自己什么</src>` | 1824 |
| 9 | `<src>独立承担。</src>` | `<src>都把他扛下来，</src>` | 1389 |
| 10 | `<src>整体而言，</src>` | `<src>都里承担。整体而言，</src>` | 2005 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该属顺。</src>` | 1879 |

---

### Test Example 5 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src><\|wait\|></src>` | 1672 |
| 2 | `<src>あの特に</src>` | `<src>最初からあの</src>` | 1756 |
| 3 | `<src>これなんかまだ</src>` | `<src>特に今まだ</src>` | 1023 |
| 4 | `<src>一年生ですからね。</src>` | `<src>1年生ですからね。</src>` | 1015 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1895 |
| 6 | `<src>こう短く</src>` | `<src>こう密告</src>` | 749 |
| 7 | `<src>剪定を</src>` | `<src>前提を</src>` | 1367 |
| 8 | `<src><\|wait\|></src>` | `<src>こう暗ず</src>` | 1751 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>してあげると</src>` | 1448 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 2156 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1556 |

---

### Test Example 6 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2149 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>乖的送子儿</src>` | 1916 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这边，这个游行</src>` | 1222 |
| 4 | `<src>然后</src>` | `<src>也很大。然后</src>` | 677 |
| 5 | `<src><\|wait\|></src>` | `<src>呢，</src>` | 1863 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放的</src>` | 753 |
| 7 | `<src>儿核桃</src>` | `<src>格捉豪人，</src>` | 1454 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1686 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>在礼袋，</src>` | 1788 |
| 10 | `<src>这种核桃</src>` | `<src>这种</src>` | 1986 |
| 11 | `<src>仁儿。</src>` | `<src>格捉豪人。</src>` | 1543 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1941 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 966 |
| 3 | `<src>始めた</src>` | `<src><\|wait\|></src>` | 1611 |
| 4 | `<src>もので、</src>` | `<src>始めたもので、</src>` | 1168 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴホ</src>` | 454 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴギョアン</src>` | 1963 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 723 |
| 8 | `<src>セザンヌ、</src>` | `<src>生産の</src>` | 2361 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 445 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどの</src>` | 1690 |
| 11 | `<src>は、田舎の</src>` | `<src>人の絵、</src>` | 2113 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生でも</src>` | 1469 |

---

### Test Example 8 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1691 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 876 |
| 3 | `<src>Drop into </src>` | `<src>Drop into your body </src>` | 1738 |
| 4 | `<src>your body. </src>` | `<src><\|wait\|></src>` | 1051 |
| 5 | `<src>Where does the tension </src>` | `<src>where does the tension </src>` | 890 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1642 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? Is it </src>` | 1621 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>tension in your chest? </src>` | 1741 |
| 9 | `<src>I ask them what </src>` | `<src>Or is the body </src>` | 1828 |
| 10 | `<src><\|wait\|></src>` | `<src>languid? </src>` | 2052 |
| 11 | `<src>language are you using? </src>` | `<src>How do you use it? </src>` | 1656 |

---

### Test Example 9 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2016 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1895 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1040 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深沉的</src>` | 962 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水，</src>` | 2038 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 664 |
| 7 | `<src>给足</src>` | `<src><\|wait\|></src>` | 2404 |
| 8 | `<src>孩子心理营养，</src>` | `<src>培育孩子心里的营养，</src>` | 640 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2010 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待</src>` | 1935 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 1570 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1739 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1894 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1036 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 993 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1787 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 805 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 1780 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1315 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1843 |
| 10 | `<src>out there, </src>` | `<src>out there, people who </src>` | 2160 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1827 |

---

### Test Example 11 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1830 |
| 2 | `<src><\|wait\|></src>` | `<src>이거 너무 </src>` | 860 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>좋아요 하실 수 있지만 </src>` | 1957 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 고사 </src>` | 1018 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>할 도요. 아니 자기 고사 </src>` | 1864 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>한다는 꿈일 </src>` | 760 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 보이 고 </src>` | 1361 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 고사 할 </src>` | 1804 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>도 보이 고 </src>` | 1894 |
| 10 | `<src>지금 나한테 </src>` | `<src>있어요. 우주 가 이제 고사 리는 </src>` | 2336 |
| 11 | `<src>보살 이라는데. </src>` | `<src>그냥 </src>` | 1985 |

---

### Test Example 12 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2025 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 768 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくという</src>` | 1690 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも用意しております</src>` | 1287 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので</src>` | 841 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1568 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 866 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 2242 |
| 9 | `<src>えっと</src>` | `<src>ので、</src>` | 407 |
| 10 | `<src><\|wait\|></src>` | `<src>ご不明な点</src>` | 2060 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>がございました</src>` | 1894 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>ようでしたら、お申し出ください。</src>` | 2190 |

---

### Test Example 13 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1953 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘沙完以后呢，</src>` | 2050 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力</src>` | 982 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也</src>` | 771 |
| 5 | `<src>然后</src>` | `<src>衰弱了，</src>` | 2272 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 1312 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1921 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 1138 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 1737 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1627 |
| 11 | `<src>抑郁状态。</src>` | `<src>逆流状态。</src>` | 2042 |

---

### Test Example 14 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1883 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔을 </src>` | 1843 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주게 달래 야가지고 내가 </src>` | 1609 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주길 수 있도록 </src>` | 411 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>하도 으도라도 </src>` | 2205 |
| 6 | `<src>죽여 달라 </src>` | `<src>다른 잔 쯤이 주길 달래야 </src>` | 1136 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>하나 인데 내가 </src>` | 2060 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>큰 소리 안 듣고 </src>` | 1146 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 중이라 는 거야. </src>` | 1881 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 1627 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 2103 |

---

### Test Example 15 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そう</src>` | 1757 |
| 2 | `<src>そこで</src>` | `<src>です。そこで</src>` | 858 |
| 3 | `<src><\|wait\|></src>` | `<src>天国という</src>` | 1662 |
| 4 | `<src>テキという設備寺が</src>` | `<src>設定が</src>` | 1065 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたが、</src>` | 357 |
| 6 | `<src>で、</src>` | `<src>で</src>` | 1644 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 775 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井青氏の仕組み</src>` | 1466 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 1655 |
| 10 | `<src>は五経、</src>` | `<src>冒険</src>` | 1397 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1666 |
| 12 | `<src>設備寺、五比</src>` | `<src>設定が</src>` | 1958 |
| 13 | `<src>です。</src>` | `<src>ゴビです。</src>` | 1938 |

---

### Test Example 16 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあ</src>` | 2052 |
| 2 | `<src>距離が</src>` | `<src>だんだんちょっと距離が</src>` | 981 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1845 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>大将が</src>` | 957 |
| 5 | `<src>多いですね。</src>` | `<src>タタタタポイですね。</src>` | 1252 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊したい方って</src>` | 1266 |
| 7 | `<src>すごい</src>` | `<src>すぐポイポイ行き来行き</src>` | 1430 |
| 8 | `<src>自己意識高いし、</src>` | `<src>ただい</src>` | 1781 |
| 9 | `<src>自分で</src>` | `<src>ジュレゼミと</src>` | 1408 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>トモンツムニを</src>` | 1970 |
| 11 | `<src>傾向が強いので、</src>` | `<src>取取取シャグが強いので</src>` | 1978 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1692 |

---

### Test Example 17 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아, 저는 </src>` | 1954 |
| 2 | `<src>옹심이, </src>` | `<src>용신이 </src>` | 1725 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1136 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>아 칼 용신이 </src>` | 934 |
| 5 | `<src>옹심이가 </src>` | `<src>어설프 용신이 가 </src>` | 2274 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 954 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. 야, </src>` | 2382 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 1257 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1764 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해행으로도 </src>` | 1962 |
| 11 | `<src>진짜. </src>` | `<src>조금 주극입니다, 정말. </src>` | 2111 |

---

### Test Example 18 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2075 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1736 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1127 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to read and repeat. </src>` | 933 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 2446 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1408 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1774 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1527 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2383 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1464 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time, </src>` | 1778 |

---

### Test Example 19 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1746 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1923 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 975 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy. And when those </src>` | 951 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1849 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 752 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted </src>` | 1411 |
| 8 | `<src>other types of energy, </src>` | `<src>to other types of energy, like </src>` | 1749 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 1672 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2100 |
| 11 | `<src>or gets used to make </src>` | `<src>Or gets used to make </src>` | 1518 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1777 |

---

### Test Example 20 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1719 |
| 2 | `<src>映画でですね、</src>` | `<src>AAアンデスに</src>` | 993 |
| 3 | `<src>いろんな場面で</src>` | `<src>世論の場面で</src>` | 1844 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>AA制服かどうか</src>` | 1026 |
| 5 | `<src>調べるときに、</src>` | `<src>メディアでいるときに</src>` | 1785 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>AAの乱高下を</src>` | 920 |
| 7 | `<src>ことで、あの</src>` | `<src>調べて、あの</src>` | 1389 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その制服かどうか</src>` | 1698 |
| 9 | `<src>保証する、生息である</src>` | `<src>を調書する、</src>` | 1634 |
| 10 | `<src>ことを保証する</src>` | `<src>制服であること保証する</src>` | 2255 |
| 11 | `<src>といったような</src>` | `<src>といったような使い方を</src>` | 1540 |
| 12 | `<src>使い方をされます。</src>` | `<src>されます。</src>` | 1658 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1643 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到</src>` | 944 |
| 3 | `<src>回到我生活</src>` | `<src>我生活的一个</src>` | 1603 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，</src>` | 1175 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 897 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好好的站上的时候，</src>` | 1636 |
| 7 | `<src>在做热汤</src>` | `<src><\|wait\|></src>` | 1296 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>在座日航日航的</src>` | 2024 |
| 9 | `<src><\|wait\|></src>` | `<src>这个里面，我当时</src>` | 1493 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被他作为催促一个</src>` | 2283 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望哈，</src>` | 1566 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 1781 |

---

### Test Example 22 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1734 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高心中</src>` | 1910 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人之间</src>` | 1426 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 469 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>有着某种用意，</src>` | 2087 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 668 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2278 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那里开始</src>` | 732 |
| 9 | `<src><\|wait\|></src>` | `<src>的？</src>` | 1695 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2165 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1457 |
| 12 | `<src>连篇。</src>` | `<src>片片。</src>` | 1774 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1855 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel. </src>` | 1863 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1156 |
| 4 | `<src><\|wait\|></src>` | `<src>in a business </src>` | 773 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>background finance </src>` | 1832 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a bachelor of psychology </src>` | 854 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1398 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at IU. </src>` | 1679 |
| 9 | `<src><\|wait\|></src>` | `<src>And in the </src>` | 2088 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 2137 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2026 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1533 |

---

### Test Example 24 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2016 |
| 2 | `<src>The meaning of </src>` | `<src><\|wait\|></src>` | 802 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment </src>` | 2024 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1016 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1744 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 770 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1262 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1850 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1197 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1769 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1573 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 2283 |
| 13 | `<src>myriad. </src>` | `<src>are myriad. </src>` | 1579 |

---

### Test Example 25 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2028 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 873 |
| 3 | `<src>ギアが</src>` | `<src>ギアです。ギアが</src>` | 1841 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと信号が</src>` | 1086 |
| 5 | `<src><\|wait\|></src>` | `<src>出せができなくなって</src>` | 1735 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 820 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1380 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1842 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1460 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いている</src>` | 1753 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 1902 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1773 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを</src>` | 1611 |

---

### Test Example 26 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2118 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1860 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1161 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 768 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1846 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 857 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1921 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1098 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1433 |
| 10 | `<src>these values. So </src>` | `<src>these values. So, </src>` | 2073 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1683 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot sword array </src>` | 1828 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1509 |

---

### Test Example 27 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src><\|wait\|></src>` | 1855 |
| 2 | `<src>一切正常，</src>` | `<src>我当时已很正常，</src>` | 1933 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>毫不乱跳，</src>` | 1124 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 759 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持不开刀。</src>` | 1775 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 743 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 1287 |
| 8 | `<src>来诊断，</src>` | `<src>一名医生来审断，</src>` | 1973 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿，</src>` | 1467 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 2182 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1499 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 1802 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的理一开。</src>` | 1588 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个</src>` | 1754 |
| 2 | `<src><\|wait\|></src>` | `<src>就是进入了二</src>` | 1829 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>级市场，</src>` | 1122 |
| 4 | `<src>服务</src>` | `<src>被俘</src>` | 895 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 2269 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1243 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1965 |
| 8 | `<src><\|wait\|></src>` | `<src>在做维新</src>` | 798 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>运动好事几年前，</src>` | 1928 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1766 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维新运动和平分的</src>` | 2217 |
| 12 | `<src>的新榜反而</src>` | `<src>新绑</src>` | 1492 |
| 13 | `<src>火了。</src>` | `<src>反之活了。</src>` | 1478 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or or if you have </src>` | 1908 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 874 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1614 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1173 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1044 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1488 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 1435 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, is </src>` | 1932 |
| 9 | `<src>is this word </src>` | `<src>this word </src>` | 1944 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2159 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1948 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam. I don't know. </src>` | 1890 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1473 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1753 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 2438 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 인슐린과 </src>` | 1295 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 1043 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 </src>` | 1332 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 굉장히 </src>` | 1308 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 1865 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1130 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 1694 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 1833 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2179 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1645 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1521 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1702 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，</src>` | 1904 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 984 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 929 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1815 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 756 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1361 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说哎，那我</src>` | 1831 |
| 9 | `<src><\|wait\|></src>` | `<src>再继续操作</src>` | 1513 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦，</src>` | 2221 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1485 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1852 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1443 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1353 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1707 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개 가 종업원 수가 </src>` | 2408 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>100명 미만 으로 </src>` | 1300 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1487 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 907 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1286 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 기업 들은 </src>` | 2018 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>성장 하거나 혹은 </src>` | 1273 |
| 9 | `<src>걷게 되는데 </src>` | `<src>회화 획일 될 것 기대 되는데 </src>` | 2223 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>왜 그러면 </src>` | 1745 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>소기업 들은 </src>` | 1827 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>성장 도 회화 획일 되는 현상 들을 </src>` | 1925 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1477 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1956 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1873 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1275 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 682 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 2259 |
| 6 | `<src>你现在</src>` | `<src><\|wait\|></src>` | 770 |
| 7 | `<src>所面临的一些</src>` | `<src>你现在所面临的一些</src>` | 2462 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊</src>` | 972 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险，</src>` | 1554 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你</src>` | 1893 |
| 11 | `<src><\|wait\|></src>` | `<src>一夜之间就</src>` | 2024 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1588 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1405 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1151 |

---

### Test Example 34 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1640 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 781 |
| 3 | `<src><\|wait\|></src>` | `<src>HTML이라고 하는 </src>` | 1722 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 </src>` | 1268 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 640 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1565 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 734 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 2613 |
| 9 | `<src>문법 에 </src>` | `<src><\|wait\|></src>` | 488 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>문법 이 맞게 우리 가 이제 </src>` | 2302 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 </src>` | 1708 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 2108 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1582 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1488 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1056 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1729 |
| 2 | `<src>我们可以看到的是</src>` | `<src>最长的部分，</src>` | 1877 |
| 3 | `<src>一个在钓鱼</src>` | `<src>我们看到的是一个</src>` | 1151 |
| 4 | `<src>的人，但是</src>` | `<src>戴雪的人，但是</src>` | 809 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 2295 |
| 6 | `<src>所以</src>` | `<src><\|wait\|></src>` | 820 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>所以通场佛嘛，</src>` | 2449 |
| 8 | `<src>时候，就要去</src>` | `<src>这样的一个状况</src>` | 1168 |
| 9 | `<src>特别注意，</src>` | `<src>需要去特别注意的是。</src>` | 1809 |
| 10 | `<src>是它能不能够</src>` | `<src>它能不能</src>` | 1564 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够达到</src>` | 2138 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与它吊不到</src>` | 1580 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1451 |
| 14 | `<src>的意思哦。</src>` | `<src>与你的意识。</src>` | 1126 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who just </src>` | 2051 |
| 2 | `<src>just getting going </src>` | `<src>getting going </src>` | 879 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1614 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1165 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 636 |
| 6 | `<src>that I think are </src>` | `<src>that you really </src>` | 1774 |
| 7 | `<src>really important. </src>` | `<src>might want to </src>` | 1049 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2109 |
| 9 | `<src>I'm going to go into. </src>` | `<src>um I'm going to go </src>` | 1036 |
| 10 | `<src>I have about </src>` | `<src>into I have about one </src>` | 1885 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 1729 |
| 12 | `<src>that follow this video </src>` | `<src>at the fall of this video </src>` | 2277 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one </src>` | 1582 |
| 14 | `<src>that cover each one </src>` | `<src>in a little more </src>` | 1544 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>detail, </src>` | 941 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new, </src>` | 1843 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1764 |
| 3 | `<src><\|wait\|></src>` | `<src>there are such </src>` | 1017 |
| 4 | `<src>such interfaces before, </src>` | `<src>instances before </src>` | 960 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1234 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilterTC, </src>` | 1179 |
| 7 | `<src>Yeah, so </src>` | `<src>and so </src>` | 1220 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 1952 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place </src>` | 1259 |
| 10 | `<src>to look at. </src>` | `<src>where it </src>` | 1747 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1587 |
| 12 | `<src><\|wait\|></src>` | `<src>developed, </src>` | 1966 |
| 13 | `<src>developers or engineers </src>` | `<src><\|wait\|></src>` | 1585 |
| 14 | `<src>working on BugRepo </src>` | `<src>so an engineer's work in the bug reporter </src>` | 1802 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1077 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>10</src>` | 1889 |
| 2 | `<src>十一二手とか</src>` | `<src>見てとか</src>` | 793 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>な形だ</src>` | 1725 |
| 4 | `<src>十秒で。</src>` | `<src>と恐らく10秒</src>` | 1265 |
| 5 | `<src>まあ</src>` | `<src>でまあ</src>` | 1358 |
| 6 | `<src>一秒に</src>` | `<src>1秒に</src>` | 1035 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>行って今日ぐらいの</src>` | 1111 |
| 8 | `<src>計算ですか</src>` | `<src>時間が</src>` | 2007 |
| 9 | `<src>ね。</src>` | `<src>あるんですかね。</src>` | 720 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1737 |
| 11 | `<src>おそらく</src>` | `<src>恐らく</src>` | 1901 |
| 12 | `<src><\|wait\|></src>` | `<src>11</src>` | 1859 |
| 13 | `<src>十一二手で</src>` | `<src>見てで</src>` | 1516 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1256 |
| 15 | `<src>宮馬とかが</src>` | `<src>見合うまとかが</src>` | 1379 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 958 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1756 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니화. </src>` | 1907 |
| 3 | `<src>이방인으로 </src>` | `<src>너희 가 </src>` | 987 |
| 4 | `<src>있을 때에 </src>` | `<src>이방인 으로 있을 때에 </src>` | 994 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 1740 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하 는 우선 에게로 </src>` | 926 |
| 7 | `<src>끄는 그대로 </src>` | `<src><\|wait\|></src>` | 2204 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 흘려 </src>` | 838 |
| 9 | `<src><\|wait\|></src>` | `<src>갔느니라. </src>` | 2051 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 </src>` | 1894 |
| 11 | `<src>너희 에게 </src>` | `<src>내가 너희 에게 </src>` | 1583 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1806 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1435 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1226 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1028 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1966 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう寝かせている。</src>` | 806 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1707 |
| 4 | `<src><\|wait\|></src>` | `<src>今</src>` | 1043 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>血気を見ている。</src>` | 417 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2011 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 655 |
| 8 | `<src><\|wait\|></src>` | `<src>超に超えている</src>` | 2511 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈気勢。</src>` | 544 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2070 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1863 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなでいくを</src>` | 1836 |
| 13 | `<src>が、</src>` | `<src>やってるんだ。</src>` | 1544 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1478 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>解足線を</src>` | 1332 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 976 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1874 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1877 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 1115 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏正</src>` | 765 |
| 5 | `<src>也就是</src>` | `<src>财的部分。也就是说，</src>` | 2106 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 640 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩增长</src>` | 1871 |
| 8 | `<src>与收入的</src>` | `<src>所带来的红利</src>` | 1141 |
| 9 | `<src>提升。如果是在</src>` | `<src>与收入的提升，</src>` | 2075 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>如果涉及到投资理财方面</src>` | 2120 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 2008 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错的，</src>` | 1534 |
| 13 | `<src>相对正财来说就</src>` | `<src>只是相对整体来说，</src>` | 1540 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了那么一点</src>` | 1252 |
| 15 | `<src><\|wait\|></src>` | `<src>的。</src>` | 816 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1977 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1766 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1139 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 876 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? </src>` | 2323 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1115 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 2187 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. </src>` | 1124 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 1882 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And did you </src>` | 1656 |
| 11 | `<src>That's another level of </src>` | `<src>graduate? </src>` | 2134 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 1730 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1455 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1025 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 867 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2120 |
| 2 | `<src><\|wait\|></src>` | `<src>새 영화 를 </src>` | 1770 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 1001 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 </src>` | 1019 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋든 내 차리 돋든 </src>` | 2351 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 너무야. </src>` | 1350 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 </src>` | 1828 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>흔들 어서 같이 놀자는 거야. </src>` | 1272 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 </src>` | 1819 |
| 10 | `<src>물릴 거고 </src>` | `<src>너무 많이 불릴 거고 </src>` | 1760 |
| 11 | `<src>신이 오면 </src>` | `<src>시니 이 너무 </src>` | 2067 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>지켜 주라고 </src>` | 1691 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주잖아. 그러니까 </src>` | 1465 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1027 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 888 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1991 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1894 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうだけじゃなくて、</src>` | 1214 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルパイソン</src>` | 680 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね。</src>` | 1983 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも、</src>` | 638 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフのビジュアルの書いて</src>` | 1482 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>後、それは</src>` | 1647 |
| 9 | `<src>にそこから</src>` | `<src>パイソンコードが</src>` | 1656 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成される、それが</src>` | 2383 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで信号処理</src>` | 1937 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われる</src>` | 1549 |
| 13 | `<src>構造になっているからです。</src>` | `<src>っていう工程になっているからである。</src>` | 1475 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1297 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 1033 |
| 16 | `<src>じゃあ。</src>` | `<src>はい。じゃあ、</src>` | 464 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1927 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then self </src>` | 1731 |
| 3 | `<src>self-defining what we think </src>` | `<src>defining what we think </src>` | 1016 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, because you're </src>` | 1076 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct. </src>` | 1742 |
| 6 | `<src>but the reality </src>` | `<src><\|wait\|></src>` | 730 |
| 7 | `<src>is is that </src>` | `<src>But the reality is that </src>` | 1357 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on </src>` | 1938 |
| 9 | `<src>block and because the </src>` | `<src>the block, and because </src>` | 1928 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 1926 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from </src>` | 1539 |
| 12 | `<src>years ago, </src>` | `<src>twenty years ago, </src>` | 1756 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1463 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1279 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 971 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to a higher standard. </src>` | 921 |

---

### Test Example 46 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1992 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 809 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 2036 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 999 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>통생 의자, 그리고 </src>` | 2366 |
| 6 | `<src>그래도 가족 </src>` | `<src>가족 같은 </src>` | 1345 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>통생 의자나 </src>` | 1951 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1272 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 1689 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 감 보다는 </src>` | 1661 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 2128 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1561 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1374 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1044 |
| 15 | `<src>내려놓 고 </src>` | `<src>잘 넣어 놓고 </src>` | 960 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 278 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 </src>` | 1852 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 1715 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인다면 </src>` | 1390 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이러 다행 주도 </src>` | 739 |
| 5 | `<src>큰 폭의 </src>` | `<src>어 큰 폭의 </src>` | 2227 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 879 |
| 7 | `<src>먼저 </src>` | `<src>어 먼저 </src>` | 2242 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 412 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 2179 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1866 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1964 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이기 때문 에 </src>` | 1687 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 뉴시 총이 </src>` | 1587 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1234 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 </src>` | 1022 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 416 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2132 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 896 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맵니다. </src>` | 1969 |
| 4 | `<src><\|wait\|></src>` | `<src>이 운전 을 하고 </src>` | 924 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 2082 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>걸어 걸어 다니 고 아니면 </src>` | 783 |
| 7 | `<src>강북 을 가면 </src>` | `<src>막굴 가면 </src>` | 2508 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 444 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 는 것도 </src>` | 2072 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장렬 이요. </src>` | 2102 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 챙기 해야 네. </src>` | 2293 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1589 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1434 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>무료 바이오 그거 는 </src>` | 1117 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>다인 것 같아요. </src>` | 1042 |
| 16 | `<src><\|wait\|></src>` | `<src>예. </src>` | 679 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1958 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩和感觉</src>` | 1894 |
| 3 | `<src>的感情或</src>` | `<src>对手的感情</src>` | 1032 |
| 4 | `<src>真实意图的，</src>` | `<src>或真挚意图的。</src>` | 979 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2019 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 637 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 2055 |
| 8 | `<src>会听到人们</src>` | `<src>好经常会听到人们这样说：“</src>` | 1043 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1781 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2052 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1521 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在作谎了。”</src>` | 1873 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1246 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1347 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 949 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 871 |
| 17 | `<src><\|wait\|></src>` | `<src>说：“</src>` | 700 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 1958 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 792 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들이 있습니다. 저희 가 </src>` | 2186 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 917 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 2264 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 커플 텐트 예요. </src>` | 1265 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 커플 텐트 예요. </src>` | 2263 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>그리고 </src>` | 1813 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2030 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1584 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>줄어들 었을 때 </src>` | 1899 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비라는 사람 이 </src>` | 1300 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1310 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스 사이트 크 </src>` | 1098 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>에서 예 </src>` | 660 |
| 16 | `<src>감염 이 될까. </src>` | `<src>X 파일까지 감염 이 될까 </src>` | 863 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1668 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1870 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 내놓 았습니다. </src>` | 1485 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 436 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>로쿠자 내부 색을 보시면 </src>` | 2455 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1434 |
| 7 | `<src>26비트 FP </src>` | `<src>UHD 60 </src>` | 1882 |
| 8 | `<src>파이프 를 </src>` | `<src>FTP 파이 를 </src>` | 1978 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128 비트 로 </src>` | 2172 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 보입니다. </src>` | 2111 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1585 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈 엑스에서도 없는 </src>` | 1724 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 984 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1080 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>LSi가 여기 도 없다. </src>` | 736 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 339 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Um, </src>` | 1872 |
| 2 | `<src>Also, </src>` | `<src>also, </src>` | 787 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1923 |
| 4 | `<src>move media objects </src>` | `<src>move me media objects </src>` | 1070 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1039 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources </src>` | 1274 |
| 7 | `<src>So, if </src>` | `<src>though, </src>` | 685 |
| 8 | `<src>you get into </src>` | `<src>if you get into </src>` | 2528 |
| 9 | `<src>a situation </src>` | `<src>the situation where you </src>` | 857 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 1975 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 1718 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource </src>` | 2171 |
| 13 | `<src>you need to let us know, </src>` | `<src>in the URL. Now, </src>` | 1675 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1493 |
| 15 | `<src><\|wait\|></src>` | `<src>moving those media </src>` | 1036 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>files and then making sure </src>` | 1074 |
| 17 | `<src>get backed up </src>` | `<src>they get backed up </src>` | 706 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 431 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1704 |
| 2 | `<src>首次觉知到</src>` | `<src>佛老一的首支</src>` | 1918 |
| 3 | `<src>那个现象：</src>` | `<src>觉知到了那个现象，</src>` | 1322 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 563 |
| 5 | `<src><\|wait\|></src>` | `<src>美当我们处于</src>` | 2111 |
| 6 | `<src>处于爱之中，</src>` | `<src>爱之中，</src>` | 655 |
| 7 | `<src>所谓的爱，</src>` | `<src>所有的爱</src>` | 2282 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 723 |
| 9 | `<src>同时进入恨。</src>` | `<src>要么也同时进入</src>` | 1973 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2022 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨，</src>` | 1687 |
| 12 | `<src>它是爱；</src>` | `<src>在早上的时候它是爱，</src>` | 1839 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上。</src>` | 1424 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成</src>` | 1266 |
| 15 | `<src><\|wait\|></src>` | `<src>恨。</src>` | 879 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆</src>` | 671 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 717 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 427 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2193 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 771 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1723 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1169 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the air field </src>` | 566 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1798 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 767 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 2257 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 525 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 1666 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2424 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 1932 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree upon </src>` | 1560 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 1376 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1319 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1034 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 470 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 739 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 363 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point </src>` | 1735 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1704 |
| 3 | `<src>is hungry. </src>` | `<src>is a hungry. </src>` | 1137 |
| 4 | `<src>He knows that </src>` | `<src>He knows that he's </src>` | 963 |
| 5 | `<src>he's been without food, </src>` | `<src>knows that for a </src>` | 2266 |
| 6 | `<src><\|wait\|></src>` | `<src>human in sport </src>` | 1412 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>day, he's hungry, </src>` | 2065 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 2021 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, hey, if you're </src>` | 2192 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>the Son of God, prove it </src>` | 2253 |
| 11 | `<src><\|wait\|></src>` | `<src>to me. </src>` | 1482 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread. </src>` | 1568 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1002 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with that </src>` | 961 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 303 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 683 |
| 17 | `<src>Man shall not live </src>` | `<src>Man, John Actley had to </src>` | 433 |
| 18 | `<src>by bread alone. </src>` | `<src>break it alone. </src>` | 325 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1868 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片</src>` | 1787 |
| 3 | `<src><\|wait\|></src>` | `<src>呢，</src>` | 999 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片呢，</src>` | 972 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1354 |
| 6 | `<src>的部分。</src>` | `<src>客梯的部分。</src>` | 1034 |
| 7 | `<src>那客厅一般</src>` | `<src>那客梯一般</src>` | 1280 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1917 |
| 9 | `<src>我们</src>` | `<src>我们在</src>` | 983 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 1802 |
| 11 | `<src><\|wait\|></src>` | `<src>休息的地方，所以呢，</src>` | 1824 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这身体的部分</src>` | 2162 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，反映的是</src>` | 1569 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给</src>` | 1426 |
| 15 | `<src>一点时间，</src>` | `<src>自己一点时间</src>` | 996 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好地</src>` | 830 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 445 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们看到</src>` | 691 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>这边是空无一人的嘛。</src>` | 499 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 331 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 347 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2126 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful, </src>` | 944 |
| 3 | `<src>right, </src>` | `<src>individual right, </src>` | 1610 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1176 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 508 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't know </src>` | 2107 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1360 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1825 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1420 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 1566 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 1923 |
| 12 | `<src><\|wait\|></src>` | `<src>but they rather </src>` | 1965 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 1624 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1337 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 943 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged </src>` | 991 |
| 17 | `<src><\|wait\|></src>` | `<src>soam. </src>` | 685 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 376 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 252 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 315 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 374 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1725 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1774 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1125 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 886 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1653 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 873 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1310 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1836 |
| 9 | `<src>something of a </src>` | `<src>something that'll have a contradiction. </src>` | 1548 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2023 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1787 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1782 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1455 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations, </src>` | 1436 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 917 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 906 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 731 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 409 |
| 19 | `<src>play </src>` | `<src><\|wait\|></src>` | 261 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>play the devil's advocate, </src>` | 230 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 387 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 281 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 271 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. stands for </src>` | 325 |
| 25 | `<src>ENTP stands for </src>` | `<src>for. </src>` | 333 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 </src>` | 1763 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>이준석은 정부 를 </src>` | 2056 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>거부 한 명분 이 후보 를 </src>` | 1478 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 373 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 2195 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1188 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2114 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1125 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1866 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1836 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 2109 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들은 해놓고 </src>` | 1685 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 를 </src>` | 1451 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 989 |
| 15 | `<src><\|wait\|></src>` | `<src>독기 를 품은 </src>` | 886 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 740 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 441 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 351 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 299 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 172 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납건 </src>` | 279 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 234 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 259 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 </src>` | 162 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 335 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1939 |
| 2 | `<src>食堂ね</src>` | `<src>食後ね今</src>` | 981 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいです。なので</src>` | 1968 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>ここで</src>` | 854 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>このホテル</src>` | 1346 |
| 6 | `<src>も</src>` | `<src>の朝食が</src>` | 1055 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 1256 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1907 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になっているので</src>` | 1196 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 1680 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドストンホテル</src>` | 1742 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 2140 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なという方はですね</src>` | 1577 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさ</src>` | 1374 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>てもってみまあいいんじゃない</src>` | 1174 |
| 16 | `<src><\|wait\|></src>` | `<src>かなと。はい。</src>` | 1055 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 656 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここホテルからですね</src>` | 367 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 271 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 362 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかる</src>` | 399 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんないか</src>` | 298 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 285 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>リッチのねまあホテル</src>` | 280 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 342 |
| 26 | `<src>よかったらですね</src>` | `<src>翌日だったらですね</src>` | 171 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 153 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 139 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は</src>` | 135 |
