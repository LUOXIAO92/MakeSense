# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9345
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.6026
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
  - PROCESS_TIME_MS_AVG: 1419.9950
  - PROCESS_TIME_MS_P50: 1419.0890
  - PROCESS_TIME_MS_P95: 2469.7610
  - PROCESS_TIME_MS_MAX: 2888.2170

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
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1630 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 743 |
| 3 | `<src>これなんかまだ</src>` | `<src>中まだ1年</src>` | 1721 |
| 4 | `<src>一年生ですからね。</src>` | `<src>生ですからね</src>` | 1243 |
| 5 | `<src>この時点で</src>` | `<src>この時点でこう</src>` | 1283 |
| 6 | `<src>こう短く</src>` | `<src>短く</src>` | 486 |
| 7 | `<src>剪定を</src>` | `<src>線っていうのを</src>` | 1316 |
| 8 | `<src><\|wait\|></src>` | `<src>こう</src>` | 1627 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>短くしてあげる</src>` | 1101 |
| 10 | `<src>十年経っても</src>` | `<src>と1年経っても</src>` | 2065 |
| 11 | `<src>大した。</src>` | `<src>大丈夫た。</src>` | 2153 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要气守，</src>` | 1931 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>是容易的。</src>` | 1717 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 772 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有一个师傅</src>` | 1365 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1204 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1400 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 785 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1949 |
| 9 | `<src>虚阿凡</src>` | `<src>需要凡</src>` | 688 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2007 |
| 11 | `<src>一个师父。</src>` | `<src>一个师傅。</src>` | 1886 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2075 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>乖的监督者里边，</src>` | 2013 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个有薪也很大，</src>` | 719 |
| 4 | `<src>然后</src>` | `<src><\|wait\|></src>` | 1335 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 1054 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放假</src>` | 1442 |
| 7 | `<src>儿核桃</src>` | `<src>跟涛人，</src>` | 1049 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1727 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉他，</src>` | 1309 |
| 10 | `<src>这种核桃</src>` | `<src>这种涛人</src>` | 2592 |
| 11 | `<src>仁儿。</src>` | `<src>啊。</src>` | 612 |

---

### Test Example 4 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying important </src>` | 1757 |
| 2 | `<src>Did very important research </src>` | `<src>research </src>` | 771 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1671 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1269 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1289 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 1445 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 655 |
| 8 | `<src><\|wait\|></src>` | `<src>of the happiest </src>` | 2176 |
| 9 | `<src>of the happiest people </src>` | `<src>people </src>` | 1250 |
| 10 | `<src>out there, </src>` | `<src>out there, people who </src>` | 2538 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 824 |

---

### Test Example 5 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1869 |
| 2 | `<src>옹심이, </src>` | `<src>명심 이 </src>` | 805 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1670 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 웅심이지. </src>` | 1275 |
| 5 | `<src>옹심이가 </src>` | `<src>그래서 웅심이가 </src>` | 1309 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1460 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. </src>` | 860 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1911 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1205 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해방 적으로 </src>` | 2080 |
| 11 | `<src>진짜. </src>` | `<src>조금씩 입니다, 지금. </src>` | 1370 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2096 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 864 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1534 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1376 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1223 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1565 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1284 |
| 8 | `<src>때문 입니다. </src>` | `<src>없기 때문 입니다. </src>` | 1545 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1628 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2534 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은 </src>` | 565 |

---

### Test Example 7 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2021 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1974 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 618 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1450 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水，</src>` | 1167 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1393 |
| 7 | `<src>给足</src>` | `<src><\|wait\|></src>` | 1284 |
| 8 | `<src>孩子心理营养，</src>` | `<src>培育孩子心智营养，</src>` | 1573 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1738 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>跟耐心等</src>` | 2515 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 1283 |

---

### Test Example 8 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1848 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜을 </src>` | 1868 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주겨 달라 이거 주고 내가 </src>` | 822 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주길 넣고 들어와서다. </src>` | 1932 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜을 </src>` | 646 |
| 6 | `<src>죽여 달라 </src>` | `<src>주겨 달라 </src>` | 1463 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐. 내가 </src>` | 2485 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1313 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐? </src>` | 2681 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아. </src>` | 638 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1221 |

---

### Test Example 9 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1672 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 870 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1539 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1245 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1305 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1532 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1298 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1669 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 2063 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2197 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 1407 |

---

### Test Example 10 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1947 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 787 |
| 3 | `<src>始めた</src>` | `<src>始めたもので、</src>` | 1674 |
| 4 | `<src>もので、</src>` | `<src><\|wait\|></src>` | 723 |
| 5 | `<src>ゴッホ、</src>` | `<src>工房、</src>` | 869 |
| 6 | `<src>ゴーギャン、</src>` | `<src>合間、</src>` | 1084 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1443 |
| 8 | `<src>セザンヌ、</src>` | `<src>生産の</src>` | 1061 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1710 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどの</src>` | 1570 |
| 11 | `<src>は、田舎の</src>` | `<src>人の絵、田舎の</src>` | 2822 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1454 |

---

### Test Example 11 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 요걸지 너무 </src>` | 1922 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1704 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>이제 저열 하게 쓸 수 있지만 </src>` | 939 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1340 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>진짜 보살 도요. 아니 </src>` | 1318 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 가 보살 인데 꿈일 프로 </src>` | 1537 |
| 7 | `<src>뭐 있고 </src>` | `<src>하고 있고 </src>` | 2336 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 1132 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보살 로 보일 프로 하고 있어요. </src>` | 2585 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 가 지금 나한테 보살 이라는 </src>` | 977 |
| 11 | `<src>보살 이라는데. </src>` | `<src>얘기 </src>` | 1369 |

---

### Test Example 12 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2026 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 912 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1580 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1307 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1314 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1552 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1377 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1547 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2514 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1733 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1495 |

---

### Test Example 13 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1745 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Abbotule. </src>` | 934 |
| 3 | `<src>촉발 시키고 </src>` | `<src>쪽발 씩기 고 </src>` | 1699 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1430 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1132 |
| 6 | `<src><\|wait\|></src>` | `<src>보모를 죽이 긴. </src>` | 1573 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>Hello, 나. </src>` | 2470 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 382 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 2265 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 1995 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>입니다. </src>` | 1493 |

---

### Test Example 14 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 1990 |
| 2 | `<src>あの</src>` | `<src>などがあの</src>` | 807 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくもらえる</src>` | 1670 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1220 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので、ぜひ</src>` | 1308 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 842 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 920 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります。</src>` | 1305 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1369 |
| 10 | `<src><\|wait\|></src>` | `<src>ご不明な点が</src>` | 1772 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ありましたら、内側が</src>` | 2620 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>ありますのでご参考ください。</src>` | 1655 |

---

### Test Example 15 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1926 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘沙完以后呢，</src>` | 1983 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 666 |
| 4 | `<src>能量也衰弱了，</src>` | `<src><\|wait\|></src>` | 1383 |
| 5 | `<src>然后</src>` | `<src>能量也衰弱了。然后</src>` | 1307 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在</src>` | 1424 |
| 7 | `<src>相对的低</src>` | `<src><\|wait\|></src>` | 2208 |
| 8 | `<src>能量的运行</src>` | `<src>一个相对的低能量的运行</src>` | 600 |
| 9 | `<src>状态，</src>` | `<src>状态。</src>` | 2170 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2005 |
| 11 | `<src>抑郁状态。</src>` | `<src>异于状态。</src>` | 1799 |

---

### Test Example 16 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1803 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 2098 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 490 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1600 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1062 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们的小状况。</src>` | 1466 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1397 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1455 |
| 9 | `<src>独立承担。</src>` | `<src>也不利成本，</src>` | 2238 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1991 |
| 11 | `<src>事业运就属凶。</src>` | `<src>应该就是这样。</src>` | 2218 |

---

### Test Example 17 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1734 |
| 2 | `<src>映画でですね、</src>` | `<src>映画出てですね、</src>` | 823 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1669 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうの</src>` | 1274 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに</src>` | 1261 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>映画の欄を</src>` | 1139 |
| 7 | `<src>ことで、あの</src>` | `<src>調べることで、あの</src>` | 662 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうの</src>` | 2206 |
| 9 | `<src>保証する、生息である</src>` | `<src>を示す、生息である</src>` | 516 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1977 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 2248 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 2492 |

---

### Test Example 18 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2097 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1752 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 837 |
| 4 | `<src><\|wait\|></src>` | `<src>the </src>` | 1204 |
| 5 | `<src>the instruction </src>` | `<src><\|wait\|></src>` | 1187 |
| 6 | `<src>tells us to use </src>` | `<src>instruction tells us to use </src>` | 1487 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 677 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 2072 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1042 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1936 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1611 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game.js </src>` | 638 |
| 13 | `<src><\|wait\|></src>` | `<src>array. </src>` | 1934 |

---

### Test Example 19 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2048 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 1879 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment, </src>` | 636 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1379 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1204 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1424 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1009 |
| 8 | `<src>change can happen </src>` | `<src><\|wait\|></src>` | 1767 |
| 9 | `<src>in the United States. </src>` | `<src>happen in the United States. </src>` | 1599 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2641 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 348 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 1104 |
| 13 | `<src>myriad. </src>` | `<src>are Miriam. </src>` | 1595 |

---

### Test Example 20 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1842 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel, and </src>` | 1977 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 613 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1444 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>a BA in business finance </src>` | 1227 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a BSc in psychology. </src>` | 1533 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2464 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at Yaenju, </src>` | 1345 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2450 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, </src>` | 814 |
| 11 | `<src><\|wait\|></src>` | `<src>I want to go into </src>` | 1391 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1947 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1632 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到我</src>` | 1764 |
| 3 | `<src>回到我生活</src>` | `<src>生活的一个轨道，</src>` | 786 |
| 4 | `<src>的一个轨道哈，</src>` | `<src><\|wait\|></src>` | 1261 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 1189 |
| 6 | `<src>在他下班的时候，</src>` | `<src>照他下班的时候</src>` | 1543 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1305 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃，</src>` | 1598 |
| 9 | `<src><\|wait\|></src>` | `<src>就这么</src>` | 1490 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，</src>` | 2771 |
| 11 | `<src>小小的愿望</src>` | `<src>就这么一个小小的愿望</src>` | 1730 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 2068 |

---

### Test Example 22 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだん</src>` | 2134 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が</src>` | 853 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1643 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>おしゃれロカデカが</src>` | 1519 |
| 5 | `<src>多いですね。</src>` | `<src>だいぶ多いですね。</src>` | 1148 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊したい方って</src>` | 1540 |
| 7 | `<src>すごい</src>` | `<src>すごい賑わわしき다가</src>` | 2530 |
| 8 | `<src>自己意識高いし、</src>` | `<src>市</src>` | 1191 |
| 9 | `<src>自分で</src>` | `<src>で見てると</src>` | 2069 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>多分本当に</src>` | 1280 |
| 11 | `<src>傾向が強いので、</src>` | `<src>男勝手が強いので</src>` | 1825 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1936 |

---

### Test Example 23 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1736 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1851 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 773 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1392 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1175 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1435 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1329 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1586 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2023 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2158 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 2272 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1623 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1744 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 2109 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also </src>` | 496 |
| 4 | `<src>also store energy, </src>` | `<src>store energy. And when those </src>` | 1703 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1041 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1422 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 2438 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 454 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 2369 |
| 10 | `<src><\|wait\|></src>` | `<src>Or, </src>` | 1747 |
| 11 | `<src>or gets used to make </src>` | `<src>gets you to make </src>` | 2360 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1594 |

---

### Test Example 25 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1759 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 738 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1653 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキオーセツビ寺が</src>` | 820 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 864 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1063 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1414 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 1331 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1562 |
| 10 | `<src>は五経、</src>` | `<src>は五個、</src>` | 1718 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2579 |
| 12 | `<src>設備寺、五比</src>` | `<src>テストビ寺、</src>` | 2694 |
| 13 | `<src>です。</src>` | `<src>五ビ寺。</src>` | 1392 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2013 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 766 |
| 3 | `<src>ギアが</src>` | `<src>ギアです。ギアが</src>` | 1776 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと、信号が</src>` | 1408 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 1261 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1362 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1091 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1710 |
| 9 | `<src>ナットが</src>` | `<src>ヤクネジのナットが</src>` | 1657 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いているっていうこと</src>` | 2694 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 402 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 2319 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンハイ完了。</src>` | 1563 |

---

### Test Example 27 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src><\|wait\|></src>` | 1887 |
| 2 | `<src>一切正常，</src>` | `<src>我当时一切正常，</src>` | 1957 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 666 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1404 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持不开刀。</src>` | 1112 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 1441 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 1318 |
| 8 | `<src>来诊断，</src>` | `<src>十二名医生来诊，</src>` | 1541 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿，</src>` | 2011 |
| 10 | `<src>一下提腿，</src>` | `<src>一打提腿</src>` | 2283 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1521 |
| 12 | `<src>他们</src>` | `<src><\|wait\|></src>` | 1425 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>他们都很疑惑的来。</src>` | 1680 |

---

### Test Example 28 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1685 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 2318 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 477 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1621 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 847 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1483 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2102 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 722 |
| 9 | `<src>걷게 되는데 </src>` | `<src>몇 개 되는데 </src>` | 2118 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 2125 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1184 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 현상 들을 </src>` | 1731 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1812 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1782 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 2319 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 422 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1295 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1304 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1426 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 2199 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 605 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2002 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 2197 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2220 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1664 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1166 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1668 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1983 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 537 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1368 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1223 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1409 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1020 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 1887 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1503 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 2751 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 450 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 2329 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1408 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 998 |

---

### Test Example 31 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1788 |
| 2 | `<src><\|wait\|></src>` | `<src>选择啊，</src>` | 791 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二classList，哎，</src>` | 1761 |
| 4 | `<src>服务</src>` | `<src>服务在一基</src>` | 1201 |
| 5 | `<src>在一级一线</src>` | `<src><\|wait\|></src>` | 1265 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>一线拼杀的大牛们。</src>` | 1562 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 989 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1766 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做维向攻总好事几点，</src>` | 1809 |
| 10 | `<src>发现</src>` | `<src>你可以发现</src>` | 2616 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维向攻平分</src>` | 2563 |
| 12 | `<src>的新榜反而</src>` | `<src><\|wait\|></src>` | 1472 |
| 13 | `<src>火了。</src>` | `<src>的新棒反而活了。</src>` | 1179 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1773 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 1714 |
| 3 | `<src>一个在钓鱼</src>` | `<src><\|wait\|></src>` | 767 |
| 4 | `<src>的人，但是</src>` | `<src>一个在跳舞的人，但是</src>` | 1665 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>他是属于逆向的，</src>` | 1151 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1304 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常我们这样一个状况</src>` | 1328 |
| 8 | `<src>时候，就要去</src>` | `<src>就要去</src>` | 1430 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1518 |
| 10 | `<src>是它能不能够</src>` | `<src>是他们能够</src>` | 2656 |
| 11 | `<src>钓到鱼，</src>` | `<src>勾到与他</src>` | 547 |
| 12 | `<src>它钓不到鱼</src>` | `<src><\|wait\|></src>` | 2257 |
| 13 | `<src><\|wait\|></src>` | `<src>跳不过去的意识</src>` | 1568 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 1202 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1904 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1703 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 766 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1281 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1200 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1547 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 1273 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1638 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1847 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2452 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2257 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1972 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1308 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1858 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 894 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1581 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1315 |
| 5 | `<src><\|wait\|></src>` | `<src>but </src>` | 1188 |
| 6 | `<src>netfilter, TC. </src>` | `<src>future TC </src>` | 1455 |
| 7 | `<src>Yeah, so </src>` | `<src>will </src>` | 449 |
| 8 | `<src>this is just </src>` | `<src>just </src>` | 2327 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 529 |
| 10 | `<src>to look at. </src>` | `<src>to work at. </src>` | 2283 |
| 11 | `<src>But </src>` | `<src>But </src>` | 1733 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1217 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1543 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on Bug Repo </src>` | 1528 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1424 |

---

### Test Example 35 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 간 보 </src>` | 2092 |
| 2 | `<src><\|wait\|></src>` | `<src>새말아 </src>` | 771 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 1674 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 </src>` | 1055 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋던 자태도 </src>` | 923 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>된 느낌 이 </src>` | 848 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>오며 이걸 흔들 어서 </src>` | 1624 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 2414 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 1410 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 2502 |
| 11 | `<src>신이 오면 </src>` | `<src>시눈 이 오면 너 </src>` | 695 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>찢겨 죽으라고 </src>` | 1077 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주려 하니까 </src>` | 1606 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1747 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 간다. </src>` | 1224 |

---

### Test Example 36 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家</src>` | 1951 |
| 2 | `<src>要提醒大家，</src>` | `<src><\|wait\|></src>` | 1750 |
| 3 | `<src>在这个罗马呢</src>` | `<src>呢，在这个罗马呢，不是以</src>` | 932 |
| 4 | `<src>不是一天造成的，</src>` | `<src><\|wait\|></src>` | 1355 |
| 5 | `<src>所以呢，</src>` | `<src>奠造成的，所以呢，</src>` | 1286 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1410 |
| 7 | `<src>所面临的一些</src>` | `<src>熟悉你的一些</src>` | 1638 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>价值观</src>` | 1006 |
| 9 | `<src>也不可能是</src>` | `<src>跟风格，也不可能是</src>` | 1657 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 2647 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1718 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 2154 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1047 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1162 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who just </src>` | 2028 |
| 2 | `<src>just getting going </src>` | `<src>getting going </src>` | 862 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1599 |
| 4 | `<src><\|wait\|></src>` | `<src>and </src>` | 1178 |
| 5 | `<src>and I have ten of them </src>` | `<src>like ten of them </src>` | 1298 |
| 6 | `<src>that I think are </src>` | `<src>that you really </src>` | 912 |
| 7 | `<src>really important. </src>` | `<src>important </src>` | 763 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1451 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go </src>` | 1403 |
| 10 | `<src>I have about </src>` | `<src>into I have about one </src>` | 2118 |
| 11 | `<src>one minute videos </src>` | `<src>minute of videos </src>` | 2152 |
| 12 | `<src>that follow this video </src>` | `<src>about this video </src>` | 2503 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one. </src>` | 1573 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1164 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>In a little more detail, </src>` | 1165 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1732 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 2116 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 548 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1451 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 1110 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하 는 우선 에게로 </src>` | 1562 |
| 7 | `<src>끄는 그대로 </src>` | `<src><\|wait\|></src>` | 1487 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 돌려 </src>` | 1200 |
| 9 | `<src><\|wait\|></src>` | `<src>갔느니라. </src>` | 1886 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2354 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1248 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1539 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1495 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1297 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1017 |

---

### Test Example 39 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1905 |
| 2 | `<src>十一二手とか</src>` | `<src>十一、二、三、とか</src>` | 2115 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>なです。おそらく</src>` | 550 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1401 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1038 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1420 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1030 |
| 8 | `<src>計算ですか</src>` | `<src>時間ですかね。</src>` | 1754 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 1493 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2530 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 517 |
| 12 | `<src><\|wait\|></src>` | `<src>十一、二、</src>` | 1591 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 2069 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1037 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮本とかが</src>` | 1214 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 839 |

---

### Test Example 40 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1956 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment: </src>` | 900 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1622 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1194 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? </src>` | 1277 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1498 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 619 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. </src>` | 2185 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 1508 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, did you </src>` | 2802 |
| 11 | `<src>That's another level of </src>` | `<src>graduate? </src>` | 473 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 2432 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1562 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1573 |
| 15 | `<src>online. </src>` | `<src><\|wait\|></src>` | 964 |

---

### Test Example 41 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1723 |
| 2 | `<src>HTML이라고 </src>` | `<src>어 Htielmei, </src>` | 2092 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 491 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>이라고 하는 컴피또도 </src>` | 1706 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1037 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1411 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 2226 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴피또 어 너의 </src>` | 588 |
| 9 | `<src>문법 에 </src>` | `<src><\|wait\|></src>` | 2140 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>문법 의 말기, 우리 가 이제 </src>` | 2187 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>초드들을 작성 해야 </src>` | 1259 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1421 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 고거들을 </src>` | 1655 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 </src>` | 1258 |
| 15 | `<src>필요 합니다. </src>` | `<src>프로그램 이 필요 합니다. </src>` | 1115 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1986 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 822 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1768 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1272 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1232 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1455 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 1085 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1712 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 1330 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 감 보다는 </src>` | 2814 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 428 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스승으로서 </src>` | 1290 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1419 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1426 |
| 15 | `<src>내려놓 고 </src>` | `<src>다 내려놓 고 </src>` | 1397 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1212 |

---

### Test Example 43 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1954 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 956 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1532 |
| 4 | `<src><\|wait\|></src>` | `<src>今、</src>` | 398 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>奇跡を見ている。</src>` | 1374 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1010 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1429 |
| 8 | `<src><\|wait\|></src>` | `<src>遠くに超えている</src>` | 1398 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不現実的な奇跡よ。</src>` | 1442 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1944 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 2301 |
| 12 | `<src>船大工をやってる</src>` | `<src>船大工をやってる</src>` | 2281 |
| 13 | `<src>が、</src>` | `<src><\|wait\|></src>` | 1635 |
| 14 | `<src>俺は</src>` | `<src>が俺はこんなにすごい</src>` | 1114 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1186 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 975 |

---

### Test Example 44 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1873 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1930 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不好的，但是</src>` | 616 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较平静的</src>` | 1292 |
| 5 | `<src>也就是</src>` | `<src>部分。也就是说，</src>` | 1214 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 1459 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>预计生财的</src>` | 1125 |
| 8 | `<src>与收入的</src>` | `<src>红利以及收入的</src>` | 1715 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升，</src>` | 1718 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>如果涉及到投资理财方面，</src>` | 2673 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 2341 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1644 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对整体来说，</src>` | 1164 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了一点</src>` | 1054 |
| 15 | `<src><\|wait\|></src>` | `<src>的。</src>` | 1050 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1986 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1942 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて、</src>` | 664 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1388 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1233 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも</src>` | 1363 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルの書いてあと</src>` | 1463 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それは</src>` | 1307 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコードが</src>` | 1493 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成されて、それが</src>` | 2804 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1826 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 2125 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているから</src>` | 1175 |
| 14 | `<src><\|wait\|></src>` | `<src>です。</src>` | 1085 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 919 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ</src>` | 277 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2114 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 1723 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맨다 이 운전 을 </src>` | 942 |
| 4 | `<src><\|wait\|></src>` | `<src>해운 거로 </src>` | 1399 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 1116 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>거르 다 네이건에 뭐 </src>` | 1582 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 2460 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 1309 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 인의 낙업도 </src>` | 2866 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장렬이에요. 좀 </src>` | 468 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1367 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1939 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1217 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모르 바요. 그거 는 </src>` | 1388 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>다른 것 같아요. </src>` | 985 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 326 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계소 </src>` | 1975 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 786 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 1886 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1463 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1149 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨펌을 </src>` | 1481 |
| 7 | `<src><\|wait\|></src>` | `<src>한 듯한 </src>` | 2480 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>테이 커컨설턴트가 와 가지고 </src>` | 1055 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 1937 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1665 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>줬을 때 </src>` | 1288 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람 이 </src>` | 1496 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1585 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스키 에서 </src>` | 1494 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 875 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 518 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1859 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1696 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보이 는 다음 에 </src>` | 975 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1578 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 919 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만 </src>` | 1576 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2419 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 1175 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 2543 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 895 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 움직이 기 때문 에 </src>` | 1445 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src><\|wait\|></src>` | 1424 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 리 초기 </src>` | 1660 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목을 </src>` | 1381 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨봐야 </src>` | 909 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 509 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1898 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1744 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 897 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, because you're </src>` | 1885 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 721 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1459 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 1386 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1482 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 2257 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 1954 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1490 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 2137 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1211 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1137 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything </src>` | 880 |
| 16 | `<src>held to a higher standard. </src>` | `<src>at this point is being held to </src>` | 510 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1939 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1775 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 765 |
| 4 | `<src>真实意图的，</src>` | `<src>真性的图片的。</src>` | 1265 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1207 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1487 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候，经常会</src>` | 1401 |
| 8 | `<src>会听到人们</src>` | `<src>听到人们这样说：</src>` | 1536 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1635 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2620 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 470 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了。</src>` | 2337 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1370 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1158 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 970 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 1044 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 385 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1659 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1871 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 했었 습니다. </src>` | 832 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1493 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1067 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1495 |
| 7 | `<src>26비트 FP </src>` | `<src>26MP, FPD </src>` | 2531 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1502 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 2888 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 로프 인다. </src>` | 1481 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1416 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>X 박스 시리즈 X에서도 없는 </src>` | 1656 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1249 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1108 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L시가 여기 도 없다. </src>` | 567 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 507 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1926 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 875 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1705 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1453 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1123 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1462 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1340 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1442 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1556 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 2606 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 556 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2347 |
| 13 | `<src>you need to let us know, </src>` | `<src>we can </src>` | 1368 |
| 14 | `<src>and we can see about </src>` | `<src>then we can see about </src>` | 1363 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1004 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 936 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 508 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 413 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2163 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 728 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 1727 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1218 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR field </src>` | 1283 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1451 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 544 |
| 8 | `<src>versus variant </src>` | `<src>versus the </src>` | 2279 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1268 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 2007 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 1378 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1043 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree </src>` | 1625 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1582 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these </src>` | 1396 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1024 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 502 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 723 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 271 |

---

### Test Example 54 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1679 |
| 2 | `<src>首次觉知到</src>` | `<src>佛法的首只</src>` | 909 |
| 3 | `<src>那个现象：</src>` | `<src>觉知到了那个现象，</src>` | 1696 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1290 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们</src>` | 1150 |
| 6 | `<src>处于爱之中，</src>` | `<src>处于爱之中，</src>` | 1505 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱，</src>` | 1292 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1588 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入</src>` | 1765 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2518 |
| 11 | `<src>在早上的时候，</src>` | `<src>恨，在早上的时候，</src>` | 2746 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱，</src>` | 1396 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1135 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1027 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1059 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆。</src>` | 532 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在移动。</src>` | 389 |
| 18 | `<src>继续在移动。</src>` | `<src><\|wait\|></src>` | 306 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point </src>` | 1722 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1719 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry, </src>` | 763 |
| 4 | `<src>He knows that </src>` | `<src>he knows that </src>` | 1366 |
| 5 | `<src>he's been without food, </src>` | `<src>he's good at his job </src>` | 1364 |
| 6 | `<src><\|wait\|></src>` | `<src>in the wilderness </src>` | 1497 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>sporty days that he's hungry. </src>` | 2463 |
| 8 | `<src>And so he says </src>` | `<src>And so he sends </src>` | 458 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus. Hey, if you feel </src>` | 2750 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>the Son of God </src>` | 1420 |
| 11 | `<src><\|wait\|></src>` | `<src>proved it, turn </src>` | 2448 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>these stones to bread. </src>` | 1659 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1096 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with that </src>` | 1132 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 901 |
| 16 | `<src><\|wait\|></src>` | `<src>Man, </src>` | 564 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan lead by </src>` | 362 |
| 18 | `<src>by bread alone. </src>` | `<src>right alone. </src>` | 392 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2111 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 906 |
| 3 | `<src>right, </src>` | `<src>right, and that </src>` | 1619 |
| 4 | `<src>and the Supreme Court </src>` | `<src>the Supreme Court </src>` | 1200 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1255 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't know </src>` | 1581 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1176 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1585 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1397 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2614 |
| 11 | `<src>these days, </src>` | `<src>These days </src>` | 522 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 935 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1705 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1461 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1267 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 1087 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 778 |
| 18 | `<src>So you have some </src>` | `<src>So you have some </src>` | 573 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 373 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 380 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 335 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1897 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片呢，</src>` | 1858 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 649 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的不分分呢，</src>` | 1581 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到一个是</src>` | 1107 |
| 6 | `<src>的部分。</src>` | `<src>客厅的部分，</src>` | 1427 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 1387 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1358 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 1337 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 2600 |
| 11 | `<src><\|wait\|></src>` | `<src>在休息的地方。所以呢，</src>` | 589 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>是身体的部分</src>` | 1281 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，反映的是</src>` | 1498 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1694 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 1242 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 971 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 512 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 596 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>公主一人的吗？</src>` | 422 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 285 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 374 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1754 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1738 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 776 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1266 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1228 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world </src>` | 1508 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1194 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1580 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1535 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2581 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 462 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 2163 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1614 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1082 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1071 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 1202 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 555 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 409 |
| 19 | `<src>play </src>` | `<src><\|wait\|></src>` | 380 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>play the devil's advocate, </src>` | 227 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 221 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 271 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 285 |
| 24 | `<src><\|wait\|></src>` | `<src>E.P. Stanslaw </src>` | 298 |
| 25 | `<src>ENTP stands for </src>` | `<src>for. </src>` | 271 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1819 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>경무를 거부 한 </src>` | 2043 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 594 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1406 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1237 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1390 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2121 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 614 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2007 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2316 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 2481 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1493 |
| 13 | `<src><\|wait\|></src>` | `<src>들어내 놓고 윤석열 후보 를 </src>` | 1291 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1249 |
| 15 | `<src><\|wait\|></src>` | `<src>뜻끼를 </src>` | 766 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>품은 공격 성을 </src>` | 585 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 425 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 347 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 378 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 이준석의 </src>` | 299 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>성상납권 </src>` | 305 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 248 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 302 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 </src>` | 231 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 292 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1928 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今</src>` | 765 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいです。なるほど。</src>` | 1823 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>でここのね</src>` | 1500 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴルフスコンホテル</src>` | 1139 |
| 6 | `<src>も</src>` | `<src>も</src>` | 1334 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>少々が食べれる場所</src>` | 860 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1917 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1285 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 2374 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴルドストンホテル</src>` | 926 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいな</src>` | 1893 |
| 13 | `<src>なっていう方はですね</src>` | `<src>っていう方はですね</src>` | 1888 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1073 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>まあいいんじゃないか</src>` | 1199 |
| 16 | `<src><\|wait\|></src>` | `<src>なと。はい。</src>` | 1098 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 525 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね</src>` | 321 |
| 19 | `<src>駅ももう</src>` | `<src>新三駅も</src>` | 254 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 309 |
| 21 | `<src>歩いて一分</src>` | `<src>一分</src>` | 361 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 289 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね立地の</src>` | 317 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>いいねまあホテル</src>` | 265 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 271 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 235 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 275 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 157 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今度は</src>` | 150 |
