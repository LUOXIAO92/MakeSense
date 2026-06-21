# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9763
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.8013
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 420
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 140
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 309
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1308.8960
  - PROCESS_TIME_MS_P50: 1293.3950
  - PROCESS_TIME_MS_P95: 2075.5110
  - PROCESS_TIME_MS_MAX: 3045.9700

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 978 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>너무 심이 </src><tgt><\|wait\|></tgt>` | 960 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt>I'm really</tgt>` | 1156 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 웅심이지. </src><tgt><\|wait\|></tgt>` | 1163 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>그래서 웅심이 가 </src><tgt><\|wait\|></tgt>` | 1323 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src><\|wait\|></src><tgt>a killer- minded person. So, the killer- mindedness</tgt>` | 1293 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞이는 건데요. </src><tgt><\|wait\|></tgt>` | 822 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1220 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>gets mixed in. Man, this is</tgt>` | 1945 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해방 으로 </src><tgt><\|wait\|></tgt>` | 1727 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 주기 맞는 </src><tgt><\|wait\|></tgt>` | 687 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 824 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 951 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>これなんかまだ</src><tgt>从一开始，</tgt>` | 1123 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1237 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1120 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>こう短く</src><tgt>毕竟这还才一年级嘛。这时候</tgt>` | 835 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1239 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1352 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>こうタイズしてってあげると</src><tgt>剪短枝条，收紧一点，</tgt>` | 2132 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1852 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 1784 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1321 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | 1266 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>边，这个油性也很大。</src><tgt>Take a few sunflower seeds, the oil content is quite high.</tgt>` | 1303 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 858 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1345 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>呢，我再放一点</src><tgt>Then I'll add</tgt>` | 1477 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | 1451 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1682 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>仁儿，仁儿，</src><tgt>a few walnut kernels, kernels, kernels,</tgt>` | 834 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | 1635 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | 1740 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气熟，</src><tgt><\|wait\|></tgt>` | 1039 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1010 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>事容易的。但是</src><tgt>準備ができていれば、物事は簡単です。でも、</tgt>` | 1411 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个</src><tgt><\|wait\|></tgt>` | 1100 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导的</src><tgt><\|wait\|></tgt>` | 1329 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>師匠の指導が</tgt>` | 1431 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>如除于终前，</src><tgt><\|wait\|></tgt>` | 1510 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1632 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>须要反。</src><tgt>なければ、終わりに達するまでは、反省しなければなりません。</tgt>` | 876 |
| 10 | `<src>要成为</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1657 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师傅。</src><tgt><\|wait\|></tgt>` | 1748 |

---

### Test Example 5 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1354 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 992 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt>Students in the auspicious positions</tgt>` | 983 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1365 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt>were not actually highly intelligent.</tgt>` | 1467 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1462 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>었기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 1734 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>They were students selected at random.</tgt>` | 640 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 모르 았 던 </src><tgt><\|wait\|></tgt>` | 1818 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | 1778 |

---

### Test Example 6 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1237 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1165 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src><\|wait\|></src><tgt>What parents need to do is</tgt>` | 916 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1344 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | 1410 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>water and fertilize our love for them,</tgt>` | 1656 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1307 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | 1765 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src><\|wait\|></src><tgt>give them the psychological nourishment they need,</tgt>` | 1587 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | 756 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1829 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 847 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>Drop into </src><tgt>你的身体在做什么？</tgt>` | 1120 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 1300 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 1313 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>进入你的身体。紧张从哪里开始？是什么？</tgt>` | 1501 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1519 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 1848 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I ask them what </src><tgt>是头痛吗？是胸闷吗？我问他们</tgt>` | 1793 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 705 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | 1924 |

---

### Test Example 8 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1249 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 853 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1129 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1161 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>We also have things like T- shirts available,</tgt>` | 1448 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 665 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1118 |
| 8 | `<src>以上になりまして、</src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src>以上になりまして、</src><tgt>so please do join us. That's all for the contact info,</tgt>` | 1743 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>よろしくお願いします。</src><tgt><\|wait\|></tgt>` | 1925 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>ランチの案内があります</src><tgt>and we look forward to seeing you. We have a lunch announcement</tgt>` | 1542 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ので、場所をお楽しみください。</src><tgt><\|wait\|></tgt>` | 880 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 922 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 </src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>에퍼드를 쪽팔 시키고 </src><tgt>I'm going to embarrass Eper,</tgt>` | 1331 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1439 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1375 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | 1526 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1790 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1352 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 963 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt>the same generation as Park Han- sang, who killed his own parents.</tgt>` | 2359 |

---

### Test Example 10 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1045 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 914 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src>始めた</src><tgt>通常从这里开始</tgt>` | 1068 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 471 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1228 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src>ゴーギャン、</src><tgt>画起，</tgt>` | 1480 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1315 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1397 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt>包括高更、高安、塞尚、罗丹</tgt>` | 2020 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1935 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 733 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>中学生でも。</src><tgt>这些人的画，连个乡村初中生也能……</tgt>` | 1926 |

---

### Test Example 11 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1076 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | 1342 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>内部的压力减轻，</src><tgt>散布が終わると、内部の圧力が</tgt>` | 996 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | 1335 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1278 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>就停留在一个</src><tgt>軽減され、エネルギーも衰えます。そして、</tgt>` | 1754 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>相对的低</src><tgt><\|wait\|></tgt>` | 1303 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | 1780 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>状态，</src><tgt>比較的低いエネルギーの運行状態に留まります。</tgt>` | 2046 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1762 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | 880 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 898 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 994 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>非常に重要な研究を行いました。</tgt>` | 1132 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. This is typical </src><tgt><\|wait\|></tgt>` | 1411 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>for the stem research, </src><tgt>極度に幸せな人々に関するものです。これは茎の研究としては典型的なことです。</tgt>` | 2235 |
| 7 | `<src>looking at the ten percent </src><tgt>これは最先端の研究です。</tgt>` | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | 1028 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1661 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt>最も幸せな人々の10パーセントを</tgt>` | 2138 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there. People with </src><tgt><\|wait\|></tgt>` | 1839 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>whom we can learn from. </src><tgt><\|wait\|></tgt>` | 1299 |

---

### Test Example 13 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 937 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 1237 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt>When faced with this situation,</tgt>` | 900 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1480 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | 1456 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>我们现有这个状况，</src><tgt>we should immediately report it to our supervisor or notify the other party about the current situation.</tgt>` | 2501 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 626 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1778 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>独立承担。</src><tgt>Don't think of it as something you have to handle all on your own.</tgt>` | 2143 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | 1815 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | 1415 |

---

### Test Example 14 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1255 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1071 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>is repeat. </src><tgt>最后，重复。重复</tgt>` | 992 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | 1393 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1645 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>就是学学练。找到你擅长的地方，多做一些。</tgt>` | 2436 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 640 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | 1749 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>get the people around you to help you with. </src><tgt>而你不擅长的，就请身边的人帮忙。</tgt>` | 2236 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1793 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | 1705 |

---

### Test Example 15 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 779 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt>제 삶으로</tgt>` | 1130 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | 1166 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | 1208 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>在他下班的时候，</src><tgt>돌아갈 수 있게 해 주세요. 퇴근 후에</tgt>` | 1264 |
| 7 | `<src>在做热汤</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 865 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热饭给他吃。真的</src><tgt><\|wait\|></tgt>` | 1527 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>따뜻한 국물과 밥을 먹여주고 싶어요. 정말</tgt>` | 2076 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | 1861 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | 1913 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt>그때는 정말 이런 작은 소망 하나밖에 없었어요.</tgt>` | 1801 |

---

### Test Example 16 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 972 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | 1244 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>해가지고 내가 </src><tgt>They asked me to be killed by another knife,</tgt>` | 1009 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1488 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | 1373 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>죽여 달라 </src><tgt>so I came in to kill them. They asked me to be killed by another knife,</tgt>` | 2428 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았냐? 내가 </src><tgt><\|wait\|></tgt>` | 801 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1659 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src><\|wait\|></src><tgt>didn't they? I didn't hear that,</tgt>` | 2095 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | 2076 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | 1722 |

---

### Test Example 17 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1012 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>저열한 일일 수 있지만 </src><tgt>これ、ちょっとダサいかもしれないけど、</tgt>` | 1339 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1340 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 가 </src><tgt><\|wait\|></tgt>` | 1402 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꾸밀 필요 가 </src><tgt>本当に菩薩だよ。いや、自分は菩薩だから飾る必要は</tgt>` | 2667 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | 1535 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | 859 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>뭐 있어요 </src><tgt>ないし、菩薩に見える必要もない。でも、</tgt>` | 1957 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>우주 가 질다 하듯 이 보살 이라는 </src><tgt><\|wait\|></tgt>` | 2131 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>듯. </src><tgt><\|wait\|></tgt>` | 1780 |

---

### Test Example 18 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1436 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 800 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离在慢慢拉开，</tgt>` | 1276 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | 1323 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | 1351 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>開業したい方って</src><tgt>果然还是选择装修的人比较多。想开店的人</tgt>` | 1870 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい</src><tgt><\|wait\|></tgt>` | 1117 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | 1842 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>自分で</src><tgt>自我意识很强，</tgt>` | 2008 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | 1059 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | 1298 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので。</src><tgt>而且倾向于自己投资，所以……</tgt>` | 1856 |

---

### Test Example 19 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1300 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 880 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>好的，这些例子之后，</tgt>` | 1183 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1327 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1342 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | 1348 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1276 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 562 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>实际上</tgt>` | 1671 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt><\|wait\|></tgt>` | 1829 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 726 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot scored array. </src><tgt>要使用这些值。所以这个game.scored数组。</tgt>` | 2210 |
| 13 | `<src><\|wait\|></src><tgt>这个game.scored数组。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1647 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 788 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 962 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt>If you're a high school girl</tgt>` | 1260 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1319 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | 1429 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>and there's some kind of connection with someone who looks weird,</tgt>` | 1804 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1247 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | 1889 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>could it have started that night?</tgt>` | 1956 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 763 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子似乎</src><tgt><\|wait\|></tgt>` | 1573 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇。</src><tgt>Yangzi seems to have been... for a long time.</tgt>` | 2007 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 887 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 828 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src>テキという</src><tgt>그렇습니다. 거기서 ' 테키' 라는</tgt>` | 1318 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>設備寺が</src><tgt><\|wait\|></tgt>` | 1157 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 1096 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>で、</src><tgt>설비가 있었죠. 그리고</tgt>` | 852 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1322 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | 1582 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>나가이 케이요시 씨의 구조는</tgt>` | 1906 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>五経、</src><tgt><\|wait\|></tgt>` | 1852 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>設備寺</src><tgt><\|wait\|></tgt>` | 1773 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>오경, 설비지,</tgt>` | 1030 |
| 13 | `<src>です。</src><tgt>어근, 접미사, 어미로 이루어져 있습니다.</tgt>` | `<src>五比です。</src><tgt><\|wait\|></tgt>` | 1522 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 940 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>活蹦乱跳，</src><tgt>I was perfectly fine back then— bouncing off the walls,</tgt>` | 1337 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1238 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | 1330 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>期间</src><tgt>so I insisted on not having the surgery. During that time,</tgt>` | 1451 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | 1503 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | 1534 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>一下敲腿，</src><tgt>about ten doctors came to diagnose me. They'd give me a good kick,</tgt>` | 1125 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | 1530 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1798 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们</src><tgt>then lift my leg, and it was all fine. They</tgt>` | 1298 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很愉快地离开。</src><tgt><\|wait\|></tgt>` | 1369 |

---

### Test Example 23 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1273 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 1154 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment, </src><tgt>제19조 수정안의 의미는</tgt>` | 981 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1293 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1395 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to how political </src><tgt>그리고</tgt>` | 1336 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1503 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 1446 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침서로서 그 역사를 살펴보는 것입니다.</tgt>` | 2031 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 722 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 1867 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, are </src><tgt>물론</tgt>` | 1424 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 1167 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 858 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>映画出てですね、</src><tgt><\|wait\|></tgt>` | 962 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>いろんな場面で</src><tgt>You know, in movies, in all sorts of situations,</tgt>` | 1255 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生速かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1477 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | 1453 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあ映画のランキングを</src><tgt>when you're checking if a movie is trending,</tgt>` | 1851 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1153 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生速かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1900 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を保証する、生速で</src><tgt>you look up the movie rankings</tgt>` | 2009 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt><\|wait\|></tgt>` | 1863 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1172 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>使い方をされます。</src><tgt>and they guarantee that it's trending.</tgt>` | 1431 |

---

### Test Example 25 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 892 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアが</src><tgt>이게 기어예요. 기어가</tgt>` | 1193 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | 1374 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1318 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라갔다 내려갔다 안 되니까,</tgt>` | 1783 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1368 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | 1749 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | 1979 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | 588 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1688 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>달려 있다는 거죠. 네,</tgt>` | 1406 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 1163 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 886 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 1241 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼, 화학 결합은</tgt>` | 1180 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | 1200 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>and when those bonds </src><tgt><\|wait\|></tgt>` | 1413 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>are broken, that potential energy </src><tgt>에너지도 저장합니다. 그리고 그 결합이 끊어지면,</tgt>` | 2502 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 638 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1683 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt>그 위치 에너지는 열이나 빛 같은 다른 에너지 형태로</tgt>` | 2254 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1888 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | 1765 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>전환되거나 새로운 결합을 만드는 데 사용됩니다.</tgt>` | 1657 |

---

### Test Example 27 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 972 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kerenath Dilo. </src><tgt><\|wait\|></tgt>` | 1356 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>I am currently </src><tgt>제 이름은 케레나스 디로입니다. 현재</tgt>` | 986 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1196 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>studying AY Business and Finance </src><tgt><\|wait\|></tgt>` | 1576 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Bachelor of Psychology </src><tgt>AY 비즈니스 및 금융과</tgt>` | 1607 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1295 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | 1836 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>심리학 학부 과정을 ANU에서</tgt>` | 2112 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | 2145 |
| 11 | `<src><\|wait\|></src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1668 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt>수강하고 있습니다. 그리고 졸업 후에는 기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1770 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 938 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>选择啊，</src><tgt><\|wait\|></tgt>` | 952 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>二classList，哎，</src><tgt>次は、2クラスを選択します。ええと、</tgt>` | 1295 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>服务在一基</src><tgt><\|wait\|></tgt>` | 1285 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>一线</src><tgt><\|wait\|></tgt>` | 1411 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>第一ランクのフロントで戦うトッププレイヤーたちですね。</tgt>` | 1911 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | 1269 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1717 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>在做微信公众号十几年，你会</src><tgt>例えば、えー、WeChat公式アカウントを10年以上やってるなら、</tgt>` | 2416 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>发现</src><tgt><\|wait\|></tgt>` | 1760 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | 1468 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的新榜反而</src><tgt>WeChat公式アカウントの評価ランキングが</tgt>` | 1407 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>火了。</src><tgt><\|wait\|></tgt>` | 795 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 919 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1729 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>인슐린과 </src><tgt>Vanadium and these things are almost like insulin</tgt>` | 704 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1089 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1510 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 굉장히 </src><tgt>and they cause very similar action.</tgt>` | 1667 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>바로 </src><tgt><\|wait\|></tgt>` | 1225 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1889 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 이야기 할 정도 로 </src><tgt>They're so similar that you could even call them ' diabetes minerals '.</tgt>` | 2276 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>굉장히 </src><tgt><\|wait\|></tgt>` | 1772 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1363 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt>That's really what it is. Now, on top of that,</tgt>` | 1708 |
| 13 | `<src>아연. </src><tgt>And on top of that, there's zinc.</tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 774 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 1161 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 996 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>あるいは、あるいは何かを文書で作成しなければならない場合、</tgt>` | 1184 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1266 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1395 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know how </src><tgt>テキストを書くとき、</tgt>` | 1698 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1218 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 1909 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt>単語の綴りが全くわからないことに気づくかもしれません。「あ、</tgt>` | 2151 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 1951 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1253 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam? I don't </src><tgt>この単語、ダブルP？ダブルL？</tgt>` | 1767 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 764 |

---

### Test Example 31 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 779 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | 833 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt>嗯，</tgt>` | 1129 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 663 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있고 </src><tgt><\|wait\|></tgt>` | 958 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>사람 도 이해 할 수 </src><tgt>计算机能理解HTML，人也能理解</tgt>` | 1712 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1275 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1361 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>문법 에 </src><tgt>的计算机语言语法，</tgt>` | 1815 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1770 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 688 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>我们得按照它的语法来写代码，</tgt>` | 2033 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | 1848 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | 930 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要一个程序来写这些代码。</tgt>` | 980 |

---

### Test Example 32 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 967 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src>There were </src><tgt>没什么新鲜事。当时</tgt>` | 1147 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | 1201 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1159 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>netfilter, TC. </src><tgt>已经有像netfilter、TC这样的接口了。</tgt>` | 1142 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 939 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>this is just </src><tgt><\|wait\|></tgt>` | 1344 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>one another place </src><tgt>所以这只是</tgt>` | 1802 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 1722 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 645 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt>看的地方之一。但</tgt>` | 1977 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1758 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | 1188 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>开发BugRepo的人应该知道这一点。</tgt>` | 1028 |

---

### Test Example 33 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | 959 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですけど明日</src><tgt>虽然是十一二手，但</tgt>` | 1156 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十目で</src><tgt><\|wait\|></tgt>` | 1190 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 947 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>一秒に</src><tgt>明天十秒，</tgt>` | 872 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1404 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1348 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>生活なんですかね。</src><tgt>大概就是今天左右的生活吧。</tgt>` | 1933 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1710 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 623 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src><\|wait\|></src><tgt>然后</tgt>` | 1742 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | 1283 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1226 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮馬とかが</src><tgt>大概十一二手，</tgt>` | 1145 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>あるから。</src><tgt><\|wait\|></tgt>` | 881 |

---

### Test Example 34 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1057 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>在这个罗马呢</src><tgt>皆さんに注意していただきたいのですが、このローマでは</tgt>` | 1268 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1293 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1392 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>一日にしてできたものではありません。ですから、今</tgt>` | 1660 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1374 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | 1854 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>也不可能是</src><tgt>直面している危機やリスクは、</tgt>` | 2039 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | 1797 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 961 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src>演变出来的，</src><tgt>一晩で突然生み出されたものではないのです。</tgt>` | 1821 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1137 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | 1026 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 909 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | 1669 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>10명 미만 으로 </src><tgt>そのうち150万人が従業員10人未満で</tgt>` | 1351 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 825 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1164 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>非常に小さな企業が多くありました。一般的には</tgt>` | 1637 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1530 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | 1761 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>걷게 되는데 </src><tgt>中小企業は成長するか、あるいは廃業する道に進むことが多いのですが、</tgt>` | 2225 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | 1934 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1792 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>폐업 도 하지 않는 현상 들을 </src><tgt>日本の小企業では成長も廃業もしないという現象を</tgt>` | 1610 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1169 |

---

### Test Example 36 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 1029 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 998 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | 975 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | 1367 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1495 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src>所以</src><tgt>낚시를 하는 사람이 보이는데, 이건 역방향으로 된 거예요. 그래서</tgt>` | 2153 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | 1100 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | 1607 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>特别注意，</src><tgt>이런 상황을 마주했을 때는 특히 주의해야 해요.</tgt>` | 2115 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | 1831 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | 1190 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지, 잡지 못하는지</tgt>` | 1712 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 952 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | 1097 |

---

### Test Example 37 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 822 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | 1236 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>如果你</src><tgt>良い兆しが訪れています。もし</tgt>` | 912 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1378 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1509 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src><\|wait\|></src><tgt>その兆しを得たら、</tgt>` | 1481 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1408 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | 1910 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src><\|wait\|></src><tgt>まずはしっかりと守り抜いてください。そうして「あ、</tgt>` | 2255 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | 1925 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1449 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>じゃあもっと操作を続けよう」なんて考えないでください。なぜそう言うのか？</tgt>` | 2009 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 912 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 814 |

---

### Test Example 38 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1013 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | 947 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>俺は</src><tgt>그럼 그냥 재워버려. 난</tgt>` | 1238 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1070 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | 804 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>지금 기적을 보고 있는 거야.</tgt>` | 1267 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1322 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>遠い超えている</src><tgt><\|wait\|></tgt>` | 1413 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>船の奇跡よ。</src><tgt>이제 한계는 아득히 넘어선 배의 기적이야.</tgt>` | 2138 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1797 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1809 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船大工をやってる</src><tgt>오랫동안 배를 만든</tgt>` | 1246 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>が、</src><tgt><\|wait\|></tgt>` | 1390 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1119 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>こんなにすごい海賊船を</src><tgt>장인인데, 내가 이렇게 대단한 해적선을</tgt>` | 1083 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | 785 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1132 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 963 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>needs to get, </src><tgt>これから始める人には、</tgt>` | 1180 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1336 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1527 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that I think are </src><tgt>これが必要だと思っていて、</tgt>` | 1570 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>really important. </src><tgt><\|wait\|></tgt>` | 1355 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1741 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go into. </src><tgt>本当に大事なものを10個挙げたいと思います。</tgt>` | 2124 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 746 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1598 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>この動画の後に1分程度の動画をいくつか用意しています。</tgt>` | 2170 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | 984 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, </src><tgt>それぞれ詳しく解説しています。</tgt>` | 869 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 어 </src><tgt><\|wait\|></tgt>` | 1186 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | 1161 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>가장 20대를 </src><tgt>嗯，嗯，怎么说呢，</tgt>` | 1119 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1229 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | 1575 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt>他是我最年轻的弟弟，也是</tgt>` | 1621 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | 1386 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1710 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>家人一样的弟弟，所以</tgt>` | 1957 |
| 10 | `<src>책임감 보다는 </src><tgt>所以比起责任感，</tgt>` | `<src>재생 가능 따른 </src><tgt><\|wait\|></tgt>` | 544 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1717 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt>我个人</tgt>` | 1321 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1076 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 것을 </src><tgt><\|wait\|></tgt>` | 1126 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>放了很多东西，</tgt>` | 1110 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 714 |

---

### Test Example 41 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 872 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1452 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>이방인으로 </src><tgt>あなたたちも知っているだろう。あなたたちが異邦人として</tgt>` | 1000 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1174 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1479 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>いたとき、言葉を持たない偶像に</tgt>` | 1687 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1236 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1844 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src><\|wait\|></src><tgt>引きずられて行ったのと同じように、</tgt>` | 2073 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1873 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 1230 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>私があなたたちに告げる。そして、</tgt>` | 1556 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1121 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 1270 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>神の霊によって語る者は……</tgt>` | 483 |

---

### Test Example 42 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1067 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | 978 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>的感情或</src><tgt>相手の感情や</tgt>` | 1131 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真性意图的，</src><tgt><\|wait\|></tgt>` | 1377 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1306 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>很多是</src><tgt>真意を察知する。多くの場合、</tgt>` | 1383 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常</src><tgt><\|wait\|></tgt>` | 1183 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 866 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt>よく</tgt>` | 1585 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你看，</src><tgt><\|wait\|></tgt>` | 1668 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 645 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>又在说谎了，</src><tgt>こんなことを聞く。「ほら、この人また嘘をついているよ」</tgt>` | 2389 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1603 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1088 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>って、その人の目はすべてを物語っているんだ」</tgt>` | 930 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | 1023 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 795 |

---

### Test Example 43 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1131 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1188 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>很不错的，但是</src><tgt>金運については、今月はかなり良いと言えます。ただ、</tgt>` | 1201 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 978 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正财的部分，也就是</src><tgt><\|wait\|></tgt>` | 1649 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>在事业方面的</src><tgt>正財、つまり</tgt>` | 1334 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | 1430 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>与收入的</src><tgt><\|wait\|></tgt>` | 1743 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>提升。如果是在</src><tgt>仕事の業績向上や収入アップといった面が強くなっています。もし</tgt>` | 2302 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | 2001 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1291 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>投資や資産運用に関しては、今月も悪くありません。ただ、</tgt>` | 1902 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | 709 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | 1278 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src><\|wait\|></src><tgt>正財と比べると少し弱めです。</tgt>` | 944 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1289 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1081 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 해맨입니다. 운전 을 </src><tgt>进去的话非常危险。</tgt>` | 1079 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>할 건 거로 </src><tgt><\|wait\|></tgt>` | 1302 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1419 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>거로 다니 고간에 뭐 </src><tgt>我打算开车去，</tgt>` | 1694 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1359 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | 1852 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>또 장렬이에요. </src><tgt>去江北也一样，去国外也是一样惨。</tgt>` | 2126 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1749 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>찍혀 내요. </src><tgt><\|wait\|></tgt>` | 1249 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>会被拍到。所以现在</tgt>` | 1422 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1058 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모르 바요. 그거 는 </src><tgt><\|wait\|></tgt>` | 1040 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>내일 인 것 같아요. </src><tgt>我正努力学习英语。那个好像是明天的事。</tgt>` | 960 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 700 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1179 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 926 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>How far did you </src><tgt>학력. 당신은</tgt>` | 1143 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1279 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? Did you </src><tgt><\|wait\|></tgt>` | 1328 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>실제로 학력이 얼마나 되나요? 고등학교 졸업했나요?</tgt>` | 1560 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1447 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | 1886 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>to college, </src><tgt>그건 한 단계의 학력입니다. 대학교에 다녔나요?</tgt>` | 2019 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | 641 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | 1871 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>attainment. </src><tgt>만약 그렇다면, 졸업했나요? 그건 또 다른 단계의 학력입니다.</tgt>` | 2382 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | 1152 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | 1443 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>자, 이제 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 1019 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1152 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index is rising,</tgt>` | 1120 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1342 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1412 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt>even these large- cap stocks will rise sharply,</tgt>` | 1887 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1084 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1793 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt>but first, these lighter stocks</tgt>` | 2152 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1739 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 1097 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 항상 </src><tgt>move the market first. So they</tgt>` | 1777 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 1021 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1163 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt>always keep an eye on the light- cap stocks</tgt>` | 787 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | 637 |

---

### Test Example 47 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1302 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 928 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて、先生が何か祈っているんだ。</tgt>` | 1386 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | 1345 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 오면 </src><tgt>君に鳥肌が立ったり、ゾクゾクするような感覚が来たら、</tgt>` | 2563 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1576 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 682 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>귀신 이 오면 </src><tgt>それを振り回して一緒に遊ぼうってことだよ。幽霊が来たら</tgt>` | 2222 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | 1821 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | 1562 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>噛まれるかもしれないし、神様が来たら守ってくれと</tgt>` | 1837 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | 932 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 870 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>刺してくれるかもしれないから、リラックスして目を閉じて。</tgt>` | 956 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | 1033 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | 999 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>있습니다. </src><tgt>ですから、もちろんこういうケースもあります。</tgt>` | 1179 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1359 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>컨설턴트예요. 뭐 </src><tgt>AさんとBさんがお互いにコンサルタントです。例えば、</tgt>` | 1720 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1348 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>이게 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | 1959 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aさんがコンサルタントだから、Aさんが</tgt>` | 2051 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1835 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | 1051 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>B라는 사람 이 </src><tgt>悪性コードを仕掛けた時に、Bさんが</tgt>` | 1814 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스사이트 스퀘어 스큐티에서 </src><tgt><\|wait\|></tgt>` | 1414 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src><\|wait\|></src><tgt>実際にクロスサイトスクリプティング（XSS）で</tgt>` | 552 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>EX 파일 까지 감염 이 될까. </src><tgt><\|wait\|></tgt>` | 714 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1275 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>というだけじゃなくて</src><tgt>So, this isn't just about the visual development environment.</tgt>` | 1070 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1119 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1570 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのもフローリフを</src><tgt>It's a Visual Python development environment.</tgt>` | 1828 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1322 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | 1750 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>にそこから</src><tgt>You write the flow chart visually, and then it generates Python code from that.</tgt>` | 2133 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | 1893 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1438 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 1241 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているからです。</src><tgt>That code is then executed, and that's how signal processing works.</tgt>` | 1389 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1058 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 819 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ。</src><tgt>Yes. So,</tgt>` | 385 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 895 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | 1359 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>내놓 았습니다. </src><tgt>そしてこれについて、多くの人が分析を投稿しました。</tgt>` | 942 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | 1242 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1457 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ここでロクジャの分析を見てみると、ソニーが</tgt>` | 1842 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | 1247 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | 1675 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트로 낮춘 </src><tgt>26ビットFPファインダーを128ビットに</tgt>` | 2267 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | 1924 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1639 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>Xbox Series X에서도 없는 </src><tgt>落としたようです。XboxSeriesXにはない</tgt>` | 1623 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 543 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1316 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3もありません。</tgt>` | 949 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 578 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1025 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt><\|wait\|></tgt>` | 938 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt>活動、そして自分を定義する</tgt>` | 1225 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | 1388 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>but the reality </src><tgt>基準とは何か。なぜなら、あなたが完全に正しいからです。しかし、</tgt>` | 1876 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is is that </src><tgt><\|wait\|></tgt>` | 1302 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 1907 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt>現実として、私たちは</tgt>` | 1866 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>standards have </src><tgt><\|wait\|></tgt>` | 1805 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1038 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt>新しい世代だからです。そして基準は20年前に変わりました。</tgt>` | 1938 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1130 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | 1332 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>everything at this point is being </src><tgt>だからこそ、私たちはより高い基準を求められています。なぜなら、今の時代にはすべてが</tgt>` | 998 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められています。なぜなら、今はすべてがより高い基準を求められているからです。</tgt>` | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | 622 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, </src><tgt><\|wait\|></tgt>` | 945 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src>you will not be able to </src><tgt>另外，</tgt>` | 1133 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1340 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1314 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>您将无法在资源之间移动媒体对象。</tgt>` | 1403 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 1183 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 750 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>a situation </src><tgt>所以，如果您遇到</tgt>` | 1726 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>where you realize </src><tgt><\|wait\|></tgt>` | 2011 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | 1783 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>把媒体文件加到了错误的位置，</tgt>` | 1104 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | 1697 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1183 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src><\|wait\|></src><tgt>请务必通知我们，我们会</tgt>` | 1202 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure </src><tgt><\|wait\|></tgt>` | 691 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 700 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt>帮您移动这些文件，并确保它们能正确备份。</tgt>` | 736 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | 921 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | 1157 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>那个现象：</src><tgt>프로이트는 그 현상을 처음 깨달았습니다.</tgt>` | 1009 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>每当我们</src><tgt><\|wait\|></tgt>` | 1256 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1417 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>处于爱之中，</src><tgt>우리가 사랑에 빠져 있을 때,</tgt>` | 1642 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | 1396 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1834 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>我们也同时进入恨。</src><tgt>소위 사랑이 있을 때, 동시에 증오도 느끼게 된다는 것입니다.</tgt>` | 2324 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1890 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | 1773 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>它是爱；</src><tgt>아침에는 사랑이고,</tgt>` | 1284 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 699 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | 1333 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src><\|wait\|></src><tgt>밤이 되면 증오로 변합니다.</tgt>` | 846 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | 424 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 398 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | 569 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1424 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 843 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>最初のセクションで少し混乱していました。</tgt>` | 1152 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1307 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src><\|wait\|></src><tgt>EHRの項目について</tgt>` | 1316 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1204 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus variant </src><tgt><\|wait\|></tgt>` | 672 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src><\|wait\|></src><tgt>「重要性」と</tgt>` | 1814 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>databases, </src><tgt><\|wait\|></tgt>` | 1686 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously it's my love. </src><tgt><\|wait\|></tgt>` | 745 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src><\|wait\|></src><tgt>バリアントデータベースのどちらがより重要か、という話で。もちろん、それは私の愛好分野です。</tgt>` | 2492 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | 1662 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | 1119 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>to be in these </src><tgt>つまり、</tgt>` | 992 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 795 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 821 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right? </src><tgt>これらのデータソースに含めるべき項目について合意できなければ、引き出すものがないということですよね？</tgt>` | 1001 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 399 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>is hungry. </src><tgt>ある時、彼はイエスが飢えていることを知ります。</tgt>` | 1175 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1192 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | 1575 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src><\|wait\|></src><tgt>彼は、</tgt>` | 1295 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | 1685 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>And so he says </src><tgt><\|wait\|></tgt>` | 1757 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>to Jesus," Hey, </src><tgt>40日間荒野で食べ物も水もなくて、飢えていることを知っています。だからイエスにこう言います。「おい、</tgt>` | 2577 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | 1994 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1628 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread." </src><tgt>もし神の御子なら証明してみせろ。この石をパンに変えろ」。</tgt>` | 1620 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1092 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | 650 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>イエスはこの誘惑にどう対処したのでしょうか？</tgt>` | 857 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 503 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | 425 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>by bread alone. </src><tgt>人はパンだけで生きることはできないのです。</tgt>` | 401 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1335 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 921 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | 1129 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1336 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1322 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt>最高法院是最后介入的，而不是引领。</tgt>` | 1503 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 1577 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1750 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>the the vanguard of </src><tgt>我不认为法院想成为</tgt>` | 1275 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1052 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days, </src><tgt><\|wait\|></tgt>` | 1752 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>but they're </src><tgt>社会变革的最前沿。虽然现在这样，但</tgt>` | 1410 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>rather reflect </src><tgt><\|wait\|></tgt>` | 1277 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1062 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>that's already </src><tgt>它们更多反映的是</tgt>` | 942 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 810 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 884 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src>You have some </src><tgt>已经形成的共识。所以，</tgt>` | 605 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges </src><tgt><\|wait\|></tgt>` | 421 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 407 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who. </src><tgt>你还有一些联邦法官，他们……</tgt>` | 404 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1022 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1160 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1385 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>的部分。</src><tgt>사진 부분에는 거실이 있어요.</tgt>` | 1500 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1397 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般都是</src><tgt><\|wait\|></tgt>` | 1795 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src>属于我们要</src><tgt>거실은 보통</tgt>` | 695 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | 1650 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1924 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src>所以呢，这身体的部分</src><tgt>쉴 때 쓰는 공간이라서, 이 신체 부분은</tgt>` | 1914 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | 1045 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 843 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>一点时间，可以</src><tgt>잠시 시간을 갖고</tgt>` | 1202 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 488 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>好好地坐下来休息。可是</src><tgt><\|wait\|></tgt>` | 845 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>我们可以看到，这边是</src><tgt>편안하게 앉아 쉬어야 한다는 걸 보여줘요. 그런데 여기는</tgt>` | 800 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的嘛。</src><tgt><\|wait\|></tgt>` | 373 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 358 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>사람이 없는 모습이에요. 아, 그래서 말이죠.</tgt>` | 379 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 950 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>and they often </src><tgt>彼らは非常に珍しく、</tgt>` | 1174 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1331 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1350 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>completely revolutionize the world. </src><tgt>世界を完全に変革するような出来事をしばしば引き起こします。</tgt>` | 1835 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1296 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | 1734 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>something of a </src><tgt>彼らの性格は、</tgt>` | 1855 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | 702 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1868 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>ある種の矛盾をはらんでいます。外向的である一方で、</tgt>` | 2236 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1117 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | 921 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src>and like to </src><tgt>無意味な会話を嫌い、</tgt>` | 892 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 845 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | 621 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love to </src><tgt>要点を簡潔に話すことを好みます。また、</tgt>` | 630 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>play </src><tgt><\|wait\|></tgt>` | 344 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | 358 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src><\|wait\|></src><tgt>悪魔の肩を貸すような議論を好みます。そして、</tgt>` | 478 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | 256 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 292 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src><\|wait\|></src><tgt>議論を避けることは決してありません。</tgt>` | 396 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | 357 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1212 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1134 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | 801 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1280 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1567 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1363 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1393 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt>put forward his reasons for rejecting his official duties— claiming it was for the sake of the candidate and their victory— and even seemed to be trying to look impressive. But now</tgt>` | 3046 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1077 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1903 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol eliminated Kim Jong- in,</tgt>` | 1864 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | 1038 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>드러내 놓고 윤석열 </src><tgt><\|wait\|></tgt>` | 1119 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>후보 를 떨어뜨리겠다는 </src><tgt>Lee Jun- seok</tgt>` | 1312 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 917 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 587 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 458 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 370 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt>was determined to show his hostility and aggression, vowing to attack and derail the Yoon Suk- yeol campaign.</tgt>` | 511 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 이준석의 </src><tgt><\|wait\|></tgt>` | 321 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>성상 납건. </src><tgt><\|wait\|></tgt>` | 351 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>The image of Lee Jun- seok's chest.</tgt>` | 437 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 326 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 351 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt>How much of a boon is this for the Democratic Party?</tgt>` | 424 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 996 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | 864 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってる</src><tgt>Well,</tgt>` | 1069 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | 581 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | 1226 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt>it looks like they're making it right now in the cafeteria. So the Goldstone Hotel</tgt>` | 2285 |
| 7 | `<src>朝食が食べれる場所</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 822 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1216 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt>is planned to be a place where you can have breakfast,</tgt>` | 2038 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1842 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | 1844 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>so I'd like to stay there in the future.</tgt>` | 1286 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | 1444 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1150 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>もまあいいんじゃないか</src><tgt>If you're thinking about it,</tgt>` | 1133 |
| 16 | `<src><\|wait\|></src><tgt>thinking about staying here in the future,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 641 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | 847 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>のホテルからですね釜山</src><tgt>I think it's a good idea. From this hotel,</tgt>` | 797 |
| 19 | `<src>駅ももう</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>釜山駅も</src><tgt><\|wait\|></tgt>` | 388 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 379 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt>you can walk to Busan Station in just a minute.</tgt>` | 376 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんないかそんな</src><tgt><\|wait\|></tgt>` | 313 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | 298 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあ</src><tgt>The location is really great—</tgt>` | 405 |
| 25 | `<src>ホテルになってますので</src><tgt>so the location is really good.</tgt>` | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | 355 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 334 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt>it's a hotel,</tgt>` | 343 |
| 28 | `<src>ください</src><tgt>If you'd like, please consider it.</tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 204 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | 186 |
