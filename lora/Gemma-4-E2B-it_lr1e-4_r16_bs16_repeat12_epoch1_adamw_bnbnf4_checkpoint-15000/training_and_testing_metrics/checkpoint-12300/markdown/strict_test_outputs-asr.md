# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9903
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.9404
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
  - PROCESS_TIME_MS_AVG: 1340.7550
  - PROCESS_TIME_MS_P50: 1344.2970
  - PROCESS_TIME_MS_P95: 2246.3760
  - PROCESS_TIME_MS_MAX: 2907.4660

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
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1988 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>挖一点松子儿里</src>` | 2014 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>边，这个油性也很大。</src>` | 654 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1007 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1245 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点</src>` | 717 |
| 7 | `<src>儿核桃</src>` | `<src>核桃仁，</src>` | 960 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1949 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>而且</src>` | 962 |
| 10 | `<src>这种核桃</src>` | `<src>这这种核桃</src>` | 1992 |
| 11 | `<src>仁儿。</src>` | `<src>呢。</src>` | 1206 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1779 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 2228 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 397 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 1470 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 993 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1316 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 1141 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1051 |
| 9 | `<src>虚阿凡</src>` | `<src>虚阿凡</src>` | 1248 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2431 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 550 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1548 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 916 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 1665 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1220 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1183 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1191 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 424 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2002 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 1348 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 2463 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 437 |

---

### Test Example 4 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1820 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 2120 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 553 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1718 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 671 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1296 |
| 7 | `<src>相对的低</src>` | `<src><\|wait\|></src>` | 861 |
| 8 | `<src>能量的运行</src>` | `<src>相对的低能量的运行</src>` | 1489 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1645 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2279 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 496 |

---

### Test Example 5 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 1946 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 908 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1624 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1118 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1237 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 506 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1105 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1653 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 449 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1313 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 2689 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 636 |

---

### Test Example 6 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1938 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1994 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 613 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1454 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1006 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1271 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 880 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 1392 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1391 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 2608 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 817 |

---

### Test Example 7 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1677 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 1999 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 634 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1435 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 937 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1304 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src><\|wait\|></src>` | 440 |
| 8 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 페르 나 </src>` | 1958 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1942 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2047 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 1213 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 1991 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1724 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 825 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1594 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 877 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1399 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1483 |
| 8 | `<src>때문 입니다. </src>` | `<src>었기 때문 입니다. </src>` | 747 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1775 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모를 랐던 </src>` | 2313 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 1165 |

---

### Test Example 9 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1701 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 2100 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 509 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1644 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 995 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 1351 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1861 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1008 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 1653 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1610 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业师兄。</src>` | 1307 |

---

### Test Example 10 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1762 |
| 2 | `<src>옹심이, </src>` | `<src>옹심이, </src>` | 1677 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 918 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 옹심이, 쌀국수하고 </src>` | 1945 |
| 5 | `<src>옹심이가 </src>` | `<src>옹심이가 </src>` | 644 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1384 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. </src>` | 1884 |
| 8 | `<src>야, </src>` | `<src>야, </src>` | 725 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1803 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해장으로도 조금 죽입니다, </src>` | 1902 |
| 11 | `<src>진짜. </src>` | `<src>진짜. </src>` | 1228 |

---

### Test Example 11 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1733 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 2215 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 451 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 2035 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 563 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1261 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐? 내가 </src>` | 1925 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1070 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2204 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>있는 줄 알았느냐? 응? </src>` | 1141 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1459 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1590 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1713 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 833 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1498 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 985 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1501 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1911 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1174 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 2515 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 642 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 1898 |

---

### Test Example 13 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1771 |
| 2 | `<src><\|wait\|></src>` | `<src>의 좋아요를 </src>` | 1865 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>눌 수 있지만 </src>` | 718 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1582 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기가 </src>` | 919 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요 근데 꾸밀 필요 가 </src>` | 1492 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 있고 </src>` | 1881 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>남한 테 보살 로 보일 필요 가 </src>` | 1178 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>뭐 있어요 우주 가 </src>` | 2521 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 보살 이라는 </src>` | 693 |
| 11 | `<src>보살 이라는데. </src>` | `<src>거예요. </src>` | 2146 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1672 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1859 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 713 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1677 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 990 |
| 6 | `<src>research, </src>` | `<src>research, </src>` | 1276 |
| 7 | `<src>looking at the ten percent </src>` | `<src>looking at the ten percent </src>` | 1840 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 314 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1827 |
| 10 | `<src>out there, </src>` | `<src>out there. People with </src>` | 2205 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 2287 |

---

### Test Example 15 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1846 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1672 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 895 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1023 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 1344 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 461 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1175 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1880 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 376 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 2016 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 1981 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 2248 |

---

### Test Example 16 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1941 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1639 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 911 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1407 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1094 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1491 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1968 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1280 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2907 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1088 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1582 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1646 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 892 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1693 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1009 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 964 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 595 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1318 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 1660 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 568 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 1762 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2254 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 1140 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1578 |

---

### Test Example 18 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2011 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 905 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1667 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 1668 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 837 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1429 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 1901 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 907 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 1596 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 1821 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 1157 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1549 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1507 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 940 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 1664 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1218 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 1213 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 1383 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 768 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃。真的，</src>` | 1552 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2053 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，只有这么一个</src>` | 2093 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望</src>` | 1224 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1698 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1637 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 2023 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 583 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1477 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1088 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1382 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1938 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 1017 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 2004 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1244 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1269 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1741 |

---

### Test Example 21 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1604 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1764 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 892 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1330 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1034 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1313 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 688 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1692 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1737 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2242 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1793 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1502 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1720 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 972 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 1646 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1032 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 1194 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 340 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 1423 |
| 8 | `<src>来诊断，</src>` | `<src>来诊断，</src>` | 1968 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿、</src>` | 1112 |
| 10 | `<src>一下提腿，</src>` | `<src>胰腺蒂</src>` | 2401 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题，</src>` | 716 |
| 12 | `<src>他们</src>` | `<src>当然都很</src>` | 1939 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的离开。</src>` | 1397 |

---

### Test Example 23 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1677 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 976 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级市场，哎，</src>` | 1661 |
| 4 | `<src>服务</src>` | `<src>服务</src>` | 1014 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1190 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 462 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，呃，</src>` | 1293 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1815 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信公众号十几年，你会</src>` | 383 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 1970 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信公众号评分</src>` | 2022 |
| 12 | `<src>的新榜反而</src>` | `<src>的新榜反而</src>` | 1977 |
| 13 | `<src>火了。</src>` | `<src>火了。</src>` | 1439 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1741 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Dettig. </src>` | 2201 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 427 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1217 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 1139 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 1391 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 909 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 1391 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1962 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2196 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1854 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1465 |

---

### Test Example 25 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 1993 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 1627 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 935 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1194 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1186 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1364 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 621 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1616 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1204 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 2504 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 543 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array. </src>` | 2197 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1430 |

---

### Test Example 26 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1631 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 987 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1614 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1527 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1026 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1506 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1986 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1520 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 2589 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1365 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1726 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1451 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1940 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1760 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 909 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1421 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1009 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1313 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 992 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1226 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2187 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1907 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1333 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 1787 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1433 |

---

### Test Example 28 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1683 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 2519 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 998 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1057 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 667 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1350 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 1872 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1038 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 1840 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 1446 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1508 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1607 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1553 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1782 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1710 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 828 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1191 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1197 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1353 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 455 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1888 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2122 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2000 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1666 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1670 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1440 |

---

### Test Example 30 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 1931 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 916 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 1655 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1228 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1195 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>上げ下げできなくなってしまうので、</src>` | 1448 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 988 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 1260 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1627 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうことです</src>` | 2395 |
| 11 | `<src>ね。</src>` | `<src>ね。</src>` | 2341 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1517 |
| 13 | `<src>分解完了。</src>` | `<src>分解完了。</src>` | 1160 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1665 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 1712 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 855 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1363 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1130 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1218 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 816 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1505 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1388 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 2562 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 421 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 2152 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1461 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 1161 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1585 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 2008 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 568 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1397 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1094 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1394 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1473 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 780 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1806 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 2203 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1187 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1699 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1312 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1128 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1580 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 2410 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 289 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1710 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 772 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1451 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2038 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1638 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 2377 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1156 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 폐업 도 </src>` | 1709 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>하지 않는 현상 들을 </src>` | 1435 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1261 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1747 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 1638 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 915 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1209 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1187 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1337 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 346 |
| 8 | `<src>this is just </src>` | `<src>this is just </src>` | 1924 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1132 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2579 |
| 11 | `<src>But </src>` | `<src>But </src>` | 491 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1174 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1705 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1518 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1103 |

---

### Test Example 35 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1831 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1877 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢</src>` | 733 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1580 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 916 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1356 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1378 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，跟风险</src>` | 840 |
| 9 | `<src>也不可能是</src>` | `<src>也不可能是</src>` | 1847 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 2204 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1935 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1446 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1445 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 877 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1559 |
| 2 | `<src>HTML이라고 </src>` | `<src>HTML이라고 </src>` | 886 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1698 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>하는 컴퓨터 도 이해 할 수 </src>` | 1033 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1133 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 이해 할 수 </src>` | 574 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1273 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 2090 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1503 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 2535 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1156 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1576 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 작성 하는 </src>` | 1514 |
| 14 | `<src>프로그램 이 </src>` | `<src>프로그램 이 </src>` | 1128 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 973 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1750 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1840 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 746 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 1888 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 565 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 1328 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 1355 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 891 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1566 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 2478 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1144 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1628 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1478 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1169 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 912 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1830 |
| 2 | `<src>十一二手とか</src>` | `<src>十一二手とか</src>` | 1745 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>じゃないですか。おそらく</src>` | 866 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1337 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1014 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1320 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一定強ぐらいの</src>` | 451 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですか</src>` | 1810 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 985 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2179 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1016 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1608 |
| 13 | `<src>十一二手で</src>` | `<src>十一二手で</src>` | 1575 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1402 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 943 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 863 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 1933 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1720 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 852 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1470 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1079 |
| 6 | `<src>that I think are </src>` | `<src>that I think are </src>` | 1398 |
| 7 | `<src>really important. </src>` | `<src>really important. </src>` | 1869 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 839 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 2344 |
| 10 | `<src>I have about </src>` | `<src>I have about </src>` | 1174 |
| 11 | `<src>one minute videos </src>` | `<src>one minute videos </src>` | 1139 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 1719 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1303 |
| 14 | `<src>that cover each one </src>` | `<src>that cover each one </src>` | 1170 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1021 |

---

### Test Example 40 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 1976 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1658 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>선생 이 뭐라 빌 거야. </src>` | 1002 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 소름 이 돋든 </src>` | 1747 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>닭살이 돋든 </src>` | 861 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오면 </src>` | 1363 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1951 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1193 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 2618 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 457 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 </src>` | 1106 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1804 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1581 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 957 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 850 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1856 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 995 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1595 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1027 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今奇跡を見てる。</src>` | 1347 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 365 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1279 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1903 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えてる船の奇跡よ。</src>` | 1199 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2401 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 691 |
| 12 | `<src>船大工をやってる</src>` | `<src>船大工をやってる</src>` | 1399 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 1683 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1608 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 972 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 892 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1871 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1752 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 860 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1242 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 1221 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1326 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 924 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>That's one level of attainment. Did you go </src>` | 1426 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 2036 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2061 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1686 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1440 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1635 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 953 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 751 |

---

### Test Example 43 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1635 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 2309 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 354 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1524 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 981 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1417 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1955 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 1234 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2503 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 544 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 2017 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1531 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1342 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1059 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 893 |

---

### Test Example 44 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1885 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 930 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1705 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1193 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 1228 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1318 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 814 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1454 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1232 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 2662 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 357 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 2173 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1425 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것을 </src>` | 1233 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 944 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1062 |

---

### Test Example 45 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 1972 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 2116 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 529 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1208 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 걸어 걸어다니 </src>` | 1198 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>공간 에 뭐 </src>` | 1343 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 을 가면 </src>` | 1248 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 외국 에 나가 면 </src>` | 1073 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1800 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>또 장렬이에요. </src>` | 2215 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 창피 하네요. </src>` | 1341 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 </src>` | 1780 |
| 13 | `<src>이제 </src>` | `<src>이제 </src>` | 1392 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>열심히 물어봐요. </src>` | 1079 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다인 것 같아요. </src>` | 990 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 448 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1871 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1980 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 643 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1319 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1096 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1472 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 2058 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 1515 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 2523 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 957 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1579 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1524 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1237 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1074 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 715 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 763 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1736 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1838 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 786 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1720 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 769 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1431 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1691 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 437 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1945 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2037 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 2094 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 1655 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1266 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1156 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 861 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 810 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1849 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 2015 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 618 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1544 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 877 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1307 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 879 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们</src>` | 1415 |
| 9 | `<src>这样说：“</src>` | `<src>这样说：“</src>` | 1368 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2560 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 425 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 2276 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1369 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 1292 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1071 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 721 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 813 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1768 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 942 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1659 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1588 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 909 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1436 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 2000 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1273 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 2590 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 423 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 2228 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1574 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1200 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1092 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 851 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 822 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1577 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 2108 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 559 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1514 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 968 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1369 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 2068 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1324 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2725 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 보인다. </src>` | 991 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1627 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1523 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1176 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1073 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 778 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 785 |

---

### Test Example 51 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 뭐 </src>` | 1873 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 이런 경우 들도 </src>` | 2145 |
| 3 | `<src>있습니다. </src>` | `<src>있습니다. </src>` | 521 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 가 A라는 사람 과 </src>` | 1867 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 서로 </src>` | 757 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>컨설턴트예요, </src>` | 1350 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1953 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>모이 킹 컨설턴트여가지고 </src>` | 1463 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2597 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 679 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>뿌렸 을 때 </src>` | 1863 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1488 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1159 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스쿠티에서 </src>` | 1182 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일 까지 </src>` | 748 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 852 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1812 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 1642 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 976 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1240 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1102 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1307 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 331 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1858 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 860 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 1708 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1795 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2194 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1642 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1294 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1046 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 816 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 780 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 391 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1622 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1721 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 823 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1389 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 1136 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1309 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 2073 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1036 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 2449 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 906 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2068 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1518 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1241 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that </src>` | 1058 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 919 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 236 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 693 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone. </src>` | 423 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2037 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 905 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 1625 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1112 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 1283 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1086 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 528 |
| 8 | `<src>versus variant </src>` | `<src>versus variant </src>` | 1511 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 549 |
| 10 | `<src>databases, </src>` | `<src>databases, </src>` | 1404 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2681 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1195 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree </src>` | 1844 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 1487 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1011 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 874 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 634 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 1012 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 271 |

---

### Test Example 55 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>弗洛伊德</src>` | 1636 |
| 2 | `<src>首次觉知到</src>` | `<src>首次觉知到</src>` | 1839 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象：</src>` | 721 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1482 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 1009 |
| 6 | `<src>处于爱之中，</src>` | `<src><\|wait\|></src>` | 1445 |
| 7 | `<src>所谓的爱，</src>` | `<src>爱之中，所谓的爱，</src>` | 2112 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1544 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入恨。</src>` | 2480 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1271 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 1702 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱；</src>` | 1520 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1069 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 904 |
| 15 | `<src><\|wait\|></src>` | `<src>那个</src>` | 608 |
| 16 | `<src>那个钟摆</src>` | `<src>钟摆，</src>` | 792 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在移动。</src>` | 451 |
| 18 | `<src>继续在移动。</src>` | `<src><\|wait\|></src>` | 356 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1967 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 974 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1599 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1080 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1081 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 540 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1510 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1833 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of social </src>` | 1326 |
| 10 | `<src>change </src>` | `<src>change </src>` | 2252 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 629 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2242 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1513 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1152 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1020 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 957 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 515 |
| 18 | `<src>So you have some </src>` | `<src>So you have some </src>` | 414 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 399 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 350 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 303 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1755 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1768 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 845 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1790 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 767 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 1302 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 1294 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 896 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 1495 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 2494 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 947 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，这身体的部分</src>` | 1715 |
| 13 | `<src>也会反映的是</src>` | `<src>也会反映的是</src>` | 1399 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1237 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间，</src>` | 1053 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 725 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息。可是</src>` | 822 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>我们可以看到这边是</src>` | 437 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 348 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 287 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 161 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1624 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1764 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 842 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1376 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1025 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1404 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 932 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1295 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 1354 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 2496 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 353 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 2246 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1535 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1169 |
| 15 | `<src>and like to </src>` | `<src>and like to </src>` | 1077 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 830 |
| 17 | `<src>get straight to the point. </src>` | `<src>get straight to the point. </src>` | 752 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 303 |
| 19 | `<src>play </src>` | `<src>play </src>` | 277 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, and they </src>` | 395 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 315 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 298 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 243 |
| 24 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 240 |
| 25 | `<src>ENTP stands for </src>` | `<src>ENTP stands for </src>` | 264 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1702 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1963 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 635 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1545 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1066 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1325 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2022 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1314 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2670 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 304 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1950 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1509 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1266 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | 1234 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 838 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 638 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 291 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 395 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 375 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 334 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>가슴 발 이준석의 성상납 건 </src>` | 342 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 245 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 239 |
| 24 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 248 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | 305 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1825 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 870 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってる</src>` | 1579 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいですなのでここのね</src>` | 289 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴールドストーンホテル</src>` | 1504 |
| 6 | `<src>も</src>` | `<src>も</src>` | 892 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1473 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1898 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1057 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 1993 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴールドストーンホテルを</src>` | 1301 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1517 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なっていう方はですね</src>` | 1581 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1548 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 984 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 948 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>なとはい思いますここ</src>` | 425 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね釜山</src>` | 819 |
| 19 | `<src>駅ももう</src>` | `<src>駅ももう</src>` | 397 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 347 |
| 21 | `<src>歩いて一分</src>` | `<src>歩いて一分</src>` | 362 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないかそんな</src>` | 322 |
| 23 | `<src>レベルのね</src>` | `<src>レベルのね</src>` | 248 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあ</src>` | 239 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 274 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 247 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 147 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 123 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではですね今回は。</src>` | 155 |
