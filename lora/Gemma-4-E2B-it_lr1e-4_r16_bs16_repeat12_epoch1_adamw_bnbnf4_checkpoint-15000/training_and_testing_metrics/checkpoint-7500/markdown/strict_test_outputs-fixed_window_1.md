# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9638
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.7682
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 683
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 88
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1348.5560
  - PROCESS_TIME_MS_P50: 1326.5660
  - PROCESS_TIME_MS_P95: 2190.2200
  - PROCESS_TIME_MS_MAX: 2812.7100

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是</src><tgt>What parents need to do is</tgt>` | 947 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1571 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt>use</tgt>` | 1234 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水，</src><tgt><\|wait\|></tgt>` | 1256 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>our deep love to water and fertilize</tgt>` | 603 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>培育孩子</src><tgt><\|wait\|></tgt>` | 1411 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>心理营养，</src><tgt>nurture our children's psychological nutrition</tgt>` | 2017 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1818 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>并耐心等待孩子</src><tgt>and patiently wait for</tgt>` | 861 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 2049 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1089 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气熟是容易的，</src><tgt>気象を整えるのは簡単です。</tgt>` | 1358 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 1035 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>只有一个师父</src><tgt>でも、師匠が</tgt>` | 1389 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1255 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>知道如何</src><tgt>どうやって</tgt>` | 1404 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | 881 |
| 8 | `<src>所以</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、</tgt>` | `<src>所以</src><tgt>中間に立つかを知っている人は一人しかいません。ですから、</tgt>` | 1734 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>虚爻凡</src><tgt><\|wait\|></tgt>` | 1961 |
| 10 | `<src>要成为</src><tgt>シュ・アファンは</tgt>` | `<src>要成为</src><tgt>虚爻と凡爻は</tgt>` | 1994 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | 902 |

---

### Test Example 3 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 958 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt>I'm Apple,</tgt>` | 1004 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | 1423 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>triggering the Apple effect,</tgt>` | 1276 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1305 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>and</tgt>` | 1382 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>포모르고깅 헬레나 </src><tgt><\|wait\|></tgt>` | 1059 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>her own FOMO,</tgt>` | 1503 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1912 |
| 10 | `<src><\|wait\|></src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>같은 세대 들은 </src><tgt>the same generation as Park Han- sang,</tgt>` | 2080 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>다. </src><tgt><\|wait\|></tgt>` | 982 |

---

### Test Example 4 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 989 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 750 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1452 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>your body. </src><tgt>进入你的身体。</tgt>` | 1272 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 1326 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>紧张从哪里开始？是什么？</tgt>` | 1415 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 983 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸闷？</tgt>` | 1754 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | 2034 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src><\|wait\|></src><tgt>我问他们</tgt>` | 2178 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | 630 |

---

### Test Example 5 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt>重要な研究を</tgt>` | 818 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1567 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. This is </src><tgt>極度に幸せな人々に対して行いました。</tgt>` | 1550 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1183 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>これは先端の研究です。</tgt>` | 1712 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 1607 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt>最も幸せな</tgt>` | 704 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1835 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, people with </src><tgt>人々の10%を対象に、</tgt>` | 2189 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>whom we can learn from. </src><tgt><\|wait\|></tgt>` | 812 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1252 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt>Students in the auspicious positions</tgt>` | 971 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1422 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1526 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1142 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt>Those randomly selected</tgt>` | 1705 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1032 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 의미 입니다. </src><tgt>students represent what they are.</tgt>` | 1225 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2021 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 모를 last </src><tgt>In fact,</tgt>` | 2105 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>연 교사 들은. </src><tgt><\|wait\|></tgt>` | 820 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1069 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>抛洒完以后呢，</src><tgt>撒き終えたら、</tgt>` | 1101 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | 1390 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了，</src><tgt>内部の圧力が下がり、エネルギーも衰えます。</tgt>` | 1992 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 733 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>就停留在一个</src><tgt>そして、</tgt>` | 1643 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>相对的低</src><tgt><\|wait\|></tgt>` | 1618 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>能量的运行</src><tgt>比較的低いエネルギーレベルで</tgt>` | 766 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态。</src><tgt><\|wait\|></tgt>` | 1847 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>運行する状態に留まります。これがいわゆる</tgt>` | 2512 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | 428 |

---

### Test Example 8 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1112 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>Items like T- shirts</tgt>` | 889 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1194 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt>will be provided,</tgt>` | 1172 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 644 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ぜひご参加ください。</src><tgt>so please do join us.</tgt>` | 1381 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1612 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になりまして、</src><tgt>That's all for the contact information,</tgt>` | 1562 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 720 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>and, um,</tgt>` | 1968 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | 1991 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>もう少々お待ちください。</src><tgt>we have a lunch announcement, so please wait a moment.</tgt>` | 999 |

---

### Test Example 9 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1184 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>挖一点松子儿里</src><tgt>Scoop out a few</tgt>` | 1006 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | 1635 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src>然后</src><tgt>edges of the sunflower seeds— they're quite oily. Then</tgt>` | 1584 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1048 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>呢，我再放一点</src><tgt>I'll add</tgt>` | 1734 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | 1919 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>a few walnut halves</tgt>` | 668 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | 1847 |
| 10 | `<src>这种核桃</src><tgt>some walnut kernels— this kind of</tgt>` | `<src>这种核桃</src><tgt>too. These walnuts</tgt>` | 2310 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | 1726 |

---

### Test Example 10 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 829 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 824 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 1557 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>毕竟这孩子才一年级。</tgt>` | 1336 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1298 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう短く</src><tgt>在这个时候，</tgt>` | 1436 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 932 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>剪短枝条</tgt>` | 1584 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | 2089 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>十年経っても</src><tgt>并收紧，就算过了十年，</tgt>` | 2592 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 1735 |

---

### Test Example 11 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>너무 심이 </src><tgt>I'm</tgt>` | 882 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1192 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 옹심이, 쌀 옹심이, 쌀 옹심이하고 </src><tgt>really into raw noodles— raw noodles, rice noodles, and rice noodles.</tgt>` | 2240 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | 986 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I</tgt>` | 1606 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>야, </src><tgt>it's a mix of rice noodles and ongsimi. Man,</tgt>` | `<src>야 </src><tgt>mix them together.</tgt>` | 714 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1968 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>this is seriously killer for a hangover,</tgt>` | `<src>해장으로도 조금 죽입니다, </src><tgt>Wow, this is actually enough to make a hangover soup,</tgt>` | 2690 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>진짜. </src><tgt><\|wait\|></tgt>` | 1847 |

---

### Test Example 12 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1378 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>距離が</src><tgt>嗯，</tgt>` | 723 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | 1598 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>オシャレる方がやっぱ</src><tgt>感觉距离在慢慢拉开，时尚穿搭</tgt>` | 1562 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | 1075 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>開業してたり方って</src><tgt>的人确实比较多。开业的人</tgt>` | 1767 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい</src><tgt><\|wait\|></tgt>` | 1503 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>自己意識高いし、</src><tgt>自我意识很强，</tgt>` | 813 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>自分で</src><tgt><\|wait\|></tgt>` | 1789 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>全部ちょっと次の投資</src><tgt>自己会</tgt>` | 1580 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | 1247 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので。</src><tgt>倾向于自己投资，所以……</tgt>` | 1932 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1273 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src><\|wait\|></src><tgt>好的。</tgt>` | 806 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>And then after these examples, </src><tgt><\|wait\|></tgt>` | 1599 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | 1264 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1311 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 858 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1115 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际上</tgt>` | 1644 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 536 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>要使用这些值。所以</tgt>` | 2134 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2297 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>this game dot scored </src><tgt>这个game.scored</tgt>` | 869 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>array. </src><tgt><\|wait\|></tgt>` | 1315 |

---

### Test Example 14 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>通常从这里开始，</tgt>` | 933 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1368 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>我才开始的，</tgt>` | 1087 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 829 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt>高富、高安、</tgt>` | 1114 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1718 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt>塞尚、</tgt>` | 1937 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1811 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt>路纳尔等人的画作</tgt>` | 935 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 2094 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>中学生でも。</src><tgt>，连乡村初中生也能……</tgt>` | 2032 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1230 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 823 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1512 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>就是重复。学会重复。重复</tgt>` | 1451 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>你擅长的，多做一些。</tgt>` | 1924 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1775 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>And what you're not good at, </src><tgt>而你不擅长的，</tgt>` | 2063 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | 2061 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>就请身边的人帮忙。</tgt>` | 928 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | 1962 |

---

### Test Example 16 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 949 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>面对这个情况，</src><tgt>In this situation,</tgt>` | 844 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>我们就是遇到问题</src><tgt><\|wait\|></tgt>` | 1592 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>when we run into a problem, we should quickly report it to our supervisor.</tgt>` | 2190 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | 596 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现有的这个状况，</src><tgt>Or we can just let them know the current situation.</tgt>` | 2170 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1544 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't try to handle everything on your own.</tgt>` | 2233 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>苦力偿贪，</src><tgt><\|wait\|></tgt>` | 2405 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>这太多了也</src><tgt>Don't be a hard worker, and don't be greedy.</tgt>` | 734 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是你这是属行。</src><tgt><\|wait\|></tgt>` | 1626 |

---

### Test Example 17 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1203 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>です。</src><tgt>이게 기어입니다.</tgt>` | 860 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1383 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | 1336 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1007 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>上げ下げできなくなってしまうので、</src><tgt>위아래로 움직이지 못하게 됩니다. 그래서</tgt>` | 955 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1455 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>役ねじの</src><tgt>기어 앞쪽에</tgt>` | 1951 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1781 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>ついているっていうことです。</src><tgt>역나사 너트가 달려 있는 겁니다.</tgt>` | 1046 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1897 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>네,</tgt>` | 1715 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 599 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果在女</src><tgt><\|wait\|></tgt>` | 832 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>高中生与长相</src><tgt>If a female high school student</tgt>` | 1019 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1434 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>不怪的人之间，</src><tgt>and is with someone she doesn't find unattractive,</tgt>` | 1574 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>有着某种荣幸，</src><tgt><\|wait\|></tgt>` | 1225 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>难道会是</src><tgt>there's a certain honor to it. Could it be</tgt>` | 2168 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1537 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里开始的？</src><tgt>what started that night?</tgt>` | 1899 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 917 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>Was it</tgt>` | 1932 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 1868 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>连篇。</src><tgt>Yangzi's thoughts that night?</tgt>` | 1565 |

---

### Test Example 19 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 851 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>映画でですね、</src><tgt>In the movie,</tgt>` | 912 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1593 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>映画生息かどうかっていうのを</src><tgt>it asks whether the movie is alive in various situations.</tgt>` | 2031 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときにまあ</src><tgt><\|wait\|></tgt>` | 780 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>映画の卵を調べる</src><tgt>When checking for movie eggs,</tgt>` | 1789 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことであの</src><tgt><\|wait\|></tgt>` | 1852 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt>it</tgt>` | 1832 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | 935 |
| 10 | `<src>ことを保証する</src><tgt>This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>ことを保証する</src><tgt>guarantees that it is alive,</tgt>` | 2149 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1843 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt>or rather, guarantees its presence.</tgt>` | 1584 |

---

### Test Example 20 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 939 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src><\|wait\|></src><tgt>次は</tgt>` | 816 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | 1368 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>服务</src><tgt>第2の選択肢、二次市場です。ああ、</tgt>` | 1310 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 897 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>トップクラスのトレーダーをサポートするんです。</tgt>` | 1006 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | 1645 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src><\|wait\|></src><tgt>例えば、えー、</tgt>` | 1914 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | 1890 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>发现</src><tgt>WeChat公式アカウントを10年以上やってると、</tgt>` | 1048 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | 1890 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的新榜反而</src><tgt>WeChat公式アカウントの評価ランキングが</tgt>` | 2165 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>火了。</src><tgt><\|wait\|></tgt>` | 1367 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 757 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>그가</tgt>` | 849 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个轨道，</src><tgt><\|wait\|></tgt>` | 1553 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src><\|wait\|></src><tgt>제 삶의 궤도로 돌아가게 해줬어요.</tgt>` | 1530 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够哈在它</src><tgt><\|wait\|></tgt>` | 1235 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>下降的时候，</src><tgt>그가 하강할 때</tgt>` | 1713 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤、热饭</src><tgt><\|wait\|></tgt>` | 1677 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>之类的</src><tgt>뜨거운 국이나 밥을</tgt>` | 694 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>吃的，</src><tgt><\|wait\|></tgt>` | 1870 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我但是悲痛说，</src><tgt>먹을 수 있게 해줬어요. 하지만 슬프게도,</tgt>` | 2813 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>做一个小小的小愿望哈。</src><tgt><\|wait\|></tgt>` | 1894 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src><\|wait\|></src><tgt>작은 소원을 빌었어요.</tgt>` | 1512 |

---

### Test Example 22 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1049 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src><\|wait\|></src><tgt>これ、</tgt>` | 829 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1702 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src><\|wait\|></src><tgt>ちょっと低すぎるかもしれないけど、</tgt>` | 1295 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | 1367 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当に菩薩だよ。いや、自分が菩薩なのに、飾る必要が</tgt>` | 2735 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | 990 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>あるし、南韓で菩薩に見える必要が</tgt>` | 2427 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | 2375 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>지금 도안 때 보살 이라면. </src><tgt>ある。宇宙が今、ドアンで菩薩なら。</tgt>` | 2444 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1131 |

---

### Test Example 23 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 869 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>그렇습니다. 거기서</tgt>` | 895 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1232 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>テキという設備寺が</src><tgt>테키라는 설비가</tgt>` | 1296 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 701 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>で、</src><tgt>있었죠. 그래서</tgt>` | 1184 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt>나가이 요시노 겐이 씨의</tgt>` | 2110 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1904 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>は五経、</src><tgt>구조는 오경,</tgt>` | 2039 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 970 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設備寺、五経。</src><tgt>설비지, 오경입니다.</tgt>` | 1987 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1381 |

---

### Test Example 24 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1017 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt>I want to be killed by the other one.</tgt>` | 1554 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | 976 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt>I came in trying to kill him.</tgt>` | 1805 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | 857 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt>I want to be killed by the other one.</tgt>` | 2006 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | 1834 |
| 8 | `<src>그 소리 안 듣고 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>그 소리 안 듣고 </src><tgt>Didn't I say to be killed by the other one?</tgt>` | 2323 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 줄 알았느냐? </src><tgt><\|wait\|></tgt>` | 2369 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt>Did you think I didn't hear that?</tgt>` | 2193 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | 1377 |

---

### Test Example 25 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 936 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Vanadium and these things are</tgt>` | 1657 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 888 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt>basically like insulin,</tgt>` | 1222 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1338 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 </src><tgt>they cause almost the same action.</tgt>` | 1799 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1597 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt>They are very, very, very important minerals for diabetes.</tgt>` | 1042 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1516 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt>They are so important that you have to talk about them.</tgt>` | 2616 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1798 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt>And then,</tgt>` | 1200 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 628 |

---

### Test Example 26 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1019 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Kerenath Duru. </src><tgt>제 이름은 케레나스 두루입니다.</tgt>` | 1545 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently </src><tgt><\|wait\|></tgt>` | 874 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src><\|wait\|></src><tgt>현재</tgt>` | 1212 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Bachelor of Psychology </src><tgt>재무학 학사 과정과 심리학 학사 과정을</tgt>` | 1832 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at the ANU, </src><tgt>ANU에서</tgt>` | 691 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1968 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>and in the future, I want to go into </src><tgt>수강하고 있습니다. 앞으로는</tgt>` | 2720 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1807 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1633 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 911 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>Like a stretched rubber band, </src><tgt>늘어난 고무줄처럼,</tgt>` | 1159 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 1232 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | 1535 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1263 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 결합이 끊어지면,</tgt>` | 1811 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1875 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>그 위치 에너지는 다른 형태의 에너지로</tgt>` | 1993 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 956 |
| 10 | `<src><\|wait\|></src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src><\|wait\|></src><tgt>전환됩니다. 예를 들어 열이나 빛,</tgt>` | 2065 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | 1829 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1608 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 931 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then.</tgt>` | 918 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1595 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src>所以</src><tgt>I was bouncing off the walls,</tgt>` | 1355 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | 1288 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>期间</src><tgt>so I insisted on not having the surgery. During that time,</tgt>` | 1807 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>大概有十位医生来</src><tgt><\|wait\|></tgt>` | 1960 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>诊断，</src><tgt>about ten doctors came to diagnose me,</tgt>` | 1515 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | 943 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一下提腿，</src><tgt>a quick kick, a quick lift,</tgt>` | 2461 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1785 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们</src><tgt>and everything was fine. They</tgt>` | 1416 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | 662 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1190 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt>제19조</tgt>` | 886 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1596 |
| 4 | `<src>and to explore its </src><tgt>수정헌법 제19조의 의미를 살펴보고,</tgt>` | `<src>and to explore its </src><tgt>의 의미와</tgt>` | 1327 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1289 |
| 6 | `<src>to how political </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to how political </src><tgt>역사를 탐구해 보겠습니다. 이 조항은</tgt>` | 1768 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1561 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt>정치적 변화가</tgt>` | 779 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 2041 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침서입니다.</tgt>` | 2671 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1811 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>물론</tgt>` | 1497 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Marylied. </src><tgt><\|wait\|></tgt>` | 1185 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 1207 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>have to produce </src><tgt>あるいは、</tgt>` | 650 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1555 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何かを書き起こさなければならない場合、</tgt>` | 1601 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1115 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt>テキストを書く必要がある場合、</tgt>` | 1838 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1882 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からなくて、「ああ、</tgt>` | 1929 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 798 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>spelled with a double </src><tgt>この単語は</tgt>` | 2187 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1836 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam? I don't </src><tgt>ダブルp？ダブルl？</tgt>` | 1689 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 1124 |

---

### Test Example 31 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 820 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>HTML이라고 </src><tgt>HTML</tgt>` | 827 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1178 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>这种计算机也能理解，</tgt>` | 1331 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 825 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>있고 사람 도 </src><tgt>人也能</tgt>` | 1099 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1787 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt>理解的计算机语言，</tgt>` | 2014 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1850 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 말개우리 가 이제 </src><tgt>语法规则，我们现在</tgt>` | 1225 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1630 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>需要编写代码，</tgt>` | 1806 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1558 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>编写这些代码的程序</tgt>` | 956 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 483 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | 715 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1445 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>在跳舞的人，但是他</src><tgt>춤을 추는 사람이 보이는데요,</tgt>` | 1331 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src>所以</src><tgt>그런데 역방향으로 되어 있어요.</tgt>` | 1592 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>汤浅芙摩这样的一个</src><tgt><\|wait\|></tgt>` | 931 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>状况会受到</src><tgt>탕첸푸모 같은 상황은</tgt>` | 1458 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>去特别注意的是，</src><tgt><\|wait\|></tgt>` | 1892 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能够</src><tgt>특히 주목할 점은 그 사람이</tgt>` | 2056 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 958 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>与他吊不到</src><tgt>매달리지 않고</tgt>` | 1831 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1452 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>哦。</src><tgt>당신의 의식에서 벗어날 수 있느냐는 거예요.</tgt>` | 1301 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1078 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1018 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | 1445 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>このローマは一日にしてできたものではなく、</tgt>` | 1695 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1055 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src><\|wait\|></src><tgt>時間をかけて築き上げられたものです。ですから、</tgt>` | 1927 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>你现在所面临的一些</src><tgt><\|wait\|></tgt>` | 1834 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>危机啊，</src><tgt>今皆さんが直面している危機や</tgt>` | 1943 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风险</src><tgt><\|wait\|></tgt>` | 868 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是你</src><tgt>リスクは、</tgt>` | 1940 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一夜之间就显现出来。</src><tgt><\|wait\|></tgt>` | 1811 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src><\|wait\|></src><tgt>一瞬で現れるものではありません。</tgt>` | 1453 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>你可能会借鉴</src><tgt><\|wait\|></tgt>` | 571 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの方々は、</tgt>` | 1024 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 838 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到了一个甜头，那</src><tgt>良い兆しが訪れました。</tgt>` | 1163 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt><\|wait\|></tgt>` | 1249 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了甜头之后，</src><tgt>もし良い兆しを得た後、</tgt>` | 1523 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1242 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src><\|wait\|></src><tgt>必ず</tgt>` | 1634 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1576 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想说，哎，那我再</src><tgt>守り抜いてください。そうして「ああ、</tgt>` | 1233 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1591 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>继续操作下去哦。</src><tgt>もっと操作しよう」なんて考えないでください。</tgt>` | 2543 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1871 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのか？</tgt>` | 1605 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1150 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt>それはですね、</tgt>` | 1067 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1023 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src>There are </src><tgt>没什么新鲜事。</tgt>` | 821 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1562 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such interfaces before, </src><tgt>以前就有这样的接口，</tgt>` | 1323 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1298 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>netfilter, TC. </src><tgt>netfilter，TC。</tgt>` | 1576 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, </src><tgt><\|wait\|></tgt>` | 853 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>so this is just </src><tgt>对，所以这只是</tgt>` | 1593 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1938 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>看的地方而已。</tgt>` | 1995 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 920 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt>但</tgt>` | 1734 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1491 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>working on BugRepo </src><tgt>在BugRepo上工作的开发者或工程师</tgt>` | 1247 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 1100 |

---

### Test Example 36 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어떻게 보면 </src><tgt>嗯，怎么说呢，</tgt>` | 940 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1532 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>20岁左右</tgt>` | 1149 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | 1323 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt>一起走过最久的朋友，也是</tgt>` | 631 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아 </src><tgt><\|wait\|></tgt>` | 1566 |
| 8 | `<src>그러니까 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>그러니까 </src><tgt>家人，所以</tgt>` | 1856 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1648 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | 835 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 2215 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt>更倾向于</tgt>` | 802 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1394 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt>靠自己</tgt>` | 1405 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>많은 것을 내놓 고. </src><tgt><\|wait\|></tgt>` | 1189 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>응모 했습니다, 느꼈 다. </src><tgt>去付出更多。嗯，我感受到了。</tgt>` | 1159 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1280 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | 831 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1471 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt>やるべきことは</tgt>` | 1245 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that I really </src><tgt>10個あります。これらは</tgt>` | 1494 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>appreciate. </src><tgt><\|wait\|></tgt>` | 944 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt>本当に感謝しています。</tgt>` | 1498 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1934 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src><\|wait\|></src><tgt>さて、</tgt>` | 854 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>I have about one minute of </src><tgt><\|wait\|></tgt>` | 2046 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>slides for this video. </src><tgt>この動画のスライドは1分程度です。</tgt>` | 2170 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I'll cover each one. </src><tgt><\|wait\|></tgt>` | 1370 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src><\|wait\|></src><tgt>一つずつ説明していきます。</tgt>` | 1187 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>In a little more detail, </src><tgt><\|wait\|></tgt>` | 1093 |

---

### Test Example 38 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 871 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万人が従業員数</tgt>` | 1810 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | 806 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな企業が</tgt>` | 1715 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 842 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くありました。一般的には</tgt>` | 1865 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1991 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>혹은 폐업 할 길을 </src><tgt>中小企業は成長するか、あるいは廃業する道</tgt>` | 2316 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | 2305 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>일본 의 소기업들은 </src><tgt>を歩むことになりますが、日本の小企業は</tgt>` | 2074 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1452 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>폐업 도 하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | 1336 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1090 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니와 너희 가 </src><tgt>あなたたちも知っているでしょう。あなたたちは</tgt>` | 1470 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 974 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>異邦人としていた時に、</tgt>` | 1384 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1140 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>言葉を持たない偶像に</tgt>` | 1735 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1271 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>引きずられて行ったのと同じように、</tgt>` | 1039 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1940 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>私は</tgt>` | 2040 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 872 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>あなたたちに告げます。</tgt>` | 1956 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1408 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는. </src><tgt>神の霊で語る者は……</tgt>` | 1270 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1066 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう眠らせてやれ。</src><tgt>그럼 그냥 재워버려.</tgt>` | 1122 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1374 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>今</src><tgt>난 지금</tgt>` | 1256 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>奇跡を見てる。</src><tgt><\|wait\|></tgt>` | 1336 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>기적을 보고 있어.</tgt>` | 1393 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 823 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>遠い超えている</src><tgt>한계는</tgt>` | 1732 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不二光奇跡。</src><tgt><\|wait\|></tgt>` | 1866 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>아득히 초월한 후리가케의 기적.</tgt>` | 1147 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1707 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船大工をやってる</src><tgt>오랫동안 배를</tgt>` | 2070 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>が、</src><tgt><\|wait\|></tgt>` | 1449 |
| 14 | `<src>俺は</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>俺は</src><tgt>만들던 내가,</tgt>` | 1142 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | 785 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선을 본 적이 없어.</tgt>` | 828 |

---

### Test Example 41 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10. </src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>1・2・3とか</src><tgt>10，</tgt>` | 953 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>でした。おそらく</src><tgt><\|wait\|></tgt>` | 1498 |
| 4 | `<src>十秒で。</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>10秒で。</src><tgt>是1、2、3之类的。大概是10秒。</tgt>` | 1949 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 829 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>1秒に</src><tgt>嗯，</tgt>` | 1626 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1544 |
| 8 | `<src>計算ですか</src><tgt>一秒一手多一点</tgt>` | `<src>インターンスみたいな</src><tgt>像实习生那样，一秒左右的</tgt>` | 896 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ことな。</src><tgt><\|wait\|></tgt>` | 1827 |
| 10 | `<src>でなんか</src><tgt>这样算。然后</tgt>` | `<src>でなんか</src><tgt>间隔。然后</tgt>` | 2016 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 841 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>1・2・3</src><tgt>大概是</tgt>` | 1819 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1424 |
| 14 | `<src>あの</src><tgt>十一二手的时候，</tgt>` | `<src>あの</src><tgt>1、2、3，那个，</tgt>` | 1223 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1092 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>あるから。</src><tgt>有Mi-auma之类的。</tgt>` | 830 |

---

### Test Example 42 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>一旦进去，就会完全迷路。</tgt>` | 1113 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1371 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>开车</tgt>` | 1187 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1217 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>할 것, 걸어 걸어 다니 고 안에 뭐 </src><tgt>还是走，还是走，走着走着，</tgt>` | 1406 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | 805 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>去江北就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt>不用说去江北，</tgt>` | 1972 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 </src><tgt><\|wait\|></tgt>` | 2049 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>장렬이에요. </src><tgt>去国外也是惨。</tgt>` | 2094 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | 811 |
| 12 | `<src>대신 에 </src><tgt>真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>有点丢人。</tgt>` | 1791 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1433 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>몰라 바이요. </src><tgt>不如现在努力学习吧。</tgt>` | 1218 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | 1136 |
| 16 | `<src><\|wait\|></src><tgt>这一点倒是做得还行。</tgt>` | `<src><\|wait\|></src><tgt>我觉得这应该就是这样。</tgt>` | 848 |

---

### Test Example 43 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>金運についてですが、今月は</tgt>` | 1172 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很普通的，但是</src><tgt><\|wait\|></tgt>` | 1172 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分，</src><tgt>普通と言えるでしょう。ただ、正の収入に偏っている部分が</tgt>` | 2367 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 415 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>在事业方面的</src><tgt>、つまり</tgt>` | 1582 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | 1624 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>与收入的</src><tgt>仕事の業績向上や収入の</tgt>` | 843 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | 1961 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>投资理财方面呢，</src><tgt>増加といった恩恵が大きいです。投資や資産運用に関しては、</tgt>` | 2696 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1764 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>今月も悪くはありません。ただ、</tgt>` | 1609 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | 1152 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>稍微弱了那么一点。</src><tgt>正の収入に比べると少し弱めです。</tgt>` | 1193 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 879 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1103 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | 865 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1605 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>어디까지</tgt>` | 1235 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | 1402 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>공부하셨나요? 고등학교 졸업하셨나요?</tgt>` | 1980 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1843 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계의 교육 수준입니다.</tgt>` | 2331 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>to college, </src><tgt><\|wait\|></tgt>` | 2232 |
| 10 | `<src>and if so, did you graduate? </src><tgt>대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>and if so, did you graduate? </src><tgt>대학까지 가셨나요? 그렇다면 졸업하셨나요?</tgt>` | 660 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | 1806 |
| 12 | `<src>attainment. </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>attainment. </src><tgt>그것도 또 다른 단계의 교육 수준입니다.</tgt>` | 1537 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | 1086 |
| 14 | `<src>now. I'll see you </src><tgt>그럼 오늘은 여기까지 하겠습니다.</tgt>` | `<src>now. I'll see you </src><tgt>자, 이제 여기까지입니다.</tgt>` | 1211 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 853 |

---

### Test Example 45 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1240 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>The stock index</tgt>` | 619 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | 1649 |
| 4 | `<src>이런 대형주 도 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src>이런 대형주 도 </src><tgt>is showing an upward trend, so these large- cap stocks</tgt>` | 2078 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | 569 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>상승 을 하겠지만 </src><tgt>will likely rise sharply,</tgt>` | 1718 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1907 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt>but first,</tgt>` | 855 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1568 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt>these lighter stocks</tgt>` | 2104 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 625 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 항상 </src><tgt>move the market first,</tgt>` | 1936 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 1393 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt>so the market cap of these lighter stocks</tgt>` | 1292 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1115 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt>is always something to keep an eye on.</tgt>` | 1048 |

---

### Test Example 46 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1063 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt>活動、</tgt>` | 812 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1576 |
| 4 | `<src>the standard is because you're </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is because you're </src><tgt>つまり自分自身で基準を定義するよりも、</tgt>` | 1631 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | 1094 |
| 6 | `<src>but the reality </src><tgt>完全に正しいのです。しかし現実には、</tgt>` | `<src>but the reality </src><tgt>あなたが完全に正しいからこそ、</tgt>` | 1700 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is is that </src><tgt><\|wait\|></tgt>` | 1539 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt>現実として、私たちは</tgt>` | 890 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt><\|wait\|></tgt>` | 1966 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>standards have </src><tgt>新しい世代だからです。そして基準は</tgt>` | 2464 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1795 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt>20年前に変わったのです。</tgt>` | 1456 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 685 |
| 14 | `<src>a higher standard because </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard because </src><tgt>だからこそ、私たちはより高い基準を求められています。</tgt>` | 1079 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | 1135 |
| 16 | `<src>held to a higher standard. </src><tgt>今はすべてがより高い基準を求められているからです。</tgt>` | `<src>held to a higher standard. </src><tgt>今の時代、すべてがより高い基準で評価されているからです。</tgt>` | 1107 |

---

### Test Example 47 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>So, this is</tgt>` | 963 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | 1457 |
| 4 | `<src><\|wait\|></src><tgt>This isn't just a visual development environment;</tgt>` | `<src><\|wait\|></src><tgt>not just a visual development environment,</tgt>` | 1326 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1414 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのもフローリフを</src><tgt>but a visual Python development environment. That's because</tgt>` | 2081 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1784 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt>after you write the flow graph visually,</tgt>` | 2297 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>にそこから</src><tgt><\|wait\|></tgt>` | 2283 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>it generates Python code from it,</tgt>` | 1829 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 991 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt>and that code is executed to perform signal processing.</tgt>` | 1170 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 902 |
| 14 | `<src><\|wait\|></src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src><\|wait\|></src><tgt>That's the structure it uses.</tgt>` | 1077 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 784 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ。</src><tgt>Yes. So.</tgt>` | 587 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 827 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 분석 을 </src><tgt>そして、これについて多くの人が</tgt>` | 1095 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | 1342 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 로쿠자 의 </src><tgt>分析を挙げています。ここで</tgt>` | 1492 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1182 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | 1934 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | 1873 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>파이프 를 </src><tgt>26ビットFPパイプラインを</tgt>` | 1943 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | 1109 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>것으로 보인다. </src><tgt>128ビットに低減したようです。</tgt>` | 1906 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1807 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>Xbox Series X에서도 없는 </src><tgt>XboxSeriesXにはない</tgt>` | 1584 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュ</tgt>` | 1112 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 845 |
| 16 | `<src><\|wait\|></src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src><\|wait\|></src><tgt>L3もありません。</tgt>` | 611 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1086 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手</src><tgt>相手の</tgt>` | 877 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>的感情或</src><tgt><\|wait\|></tgt>` | 1564 |
| 4 | `<src>真实意图的，</src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src>真实意图的。</src><tgt>感情や真意を推し量ったり感じ取ったりすること。</tgt>` | 2046 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 751 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>多くは</tgt>` | 1622 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>很多时候，</src><tgt><\|wait\|></tgt>` | 1535 |
| 8 | `<src>会听到人们</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>经常会听到</src><tgt>よく</tgt>` | 710 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>人们这样说：“</src><tgt><\|wait\|></tgt>` | 1978 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「見てよ、</tgt>` | 1964 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 942 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了。”</src><tgt>この人また嘘ついてる」って聞く。</tgt>` | 2198 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1140 |
| 14 | `<src>已经说明了一切。”</src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>その人の目は全部話してるんだよ」って。その人の目は全部話してるんだよ」って。</tgt>` | 1502 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 918 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说。</src><tgt>つまり、</tgt>` | 744 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 556 |

---

### Test Example 50 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1231 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src><\|wait\|></src><tgt>目を閉じて、</tgt>` | 891 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>선물을 </src><tgt><\|wait\|></tgt>` | 1503 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>빌 거야. 얘네 서름이 돋든 </src><tgt>プレゼントを待ってるんだ。彼らが</tgt>` | 1678 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>가시 리 돋든 </src><tgt><\|wait\|></tgt>` | 1177 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 </src><tgt>寒さに震えたり、</tgt>` | 1755 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>엄이야. 이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 2008 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>そうやって遊ぼうって。だから、これを振って一緒に遊ぶんだ。</tgt>` | 2397 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | 2334 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>幽霊が来たら噛まれるし、</tgt>` | 2053 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>시눈 이 오면 </src><tgt><\|wait\|></tgt>` | 1525 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>鬼が来たら守ってくれって</tgt>` | 1362 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주려 하니까 </src><tgt><\|wait\|></tgt>` | 1197 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>刺そうとしてるから、リラックスして</tgt>` | 1006 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 343 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | 962 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src><\|wait\|></src><tgt>프로이트는</tgt>` | 797 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>首次觉知到了那个现象：</src><tgt><\|wait\|></tgt>` | 1639 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src><\|wait\|></src><tgt>그 현상을 처음으로 자각했습니다.</tgt>` | 1395 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>每当我们处于</src><tgt><\|wait\|></tgt>` | 1135 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>爱之中，</src><tgt>우리가 사랑 속에 있을 때,</tgt>` | 1730 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | 1382 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt>소위 사랑은</tgt>` | 836 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>我们也同时进入恨。</src><tgt><\|wait\|></tgt>` | 2023 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>동시에 증오가 됩니다.</tgt>` | 2026 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | 887 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>它是爱；</src><tgt>아침에는 사랑이고,</tgt>` | 1949 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1383 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>它就变成恨。</src><tgt>밤이 되면 증오가 됩니다.</tgt>` | 1238 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1023 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆</src><tgt>그 진자의</tgt>` | 806 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在运动。</src><tgt><\|wait\|></tgt>` | 603 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src><\|wait\|></src><tgt>운동은 계속됩니다.</tgt>` | 613 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 797 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | 1554 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src><\|wait\|></src><tgt>您将无法</tgt>` | 1282 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1256 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | 554 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 1515 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into </src><tgt>所以，如果您</tgt>` | 1906 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt><\|wait\|></tgt>` | 1707 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize </src><tgt>发现</tgt>` | 707 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | 2418 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>某个资源里放错了媒体文件，</tgt>` | 2201 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | 1425 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt>请告诉我们，我们</tgt>` | 1129 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1063 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files and then making sure they </src><tgt>可以帮忙移动这些文件，并确保它们</tgt>` | 1097 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 420 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>能正确备份。</tgt>` | 548 |

---

### Test Example 53 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계서 뭐 </src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>물론 이제 </src><tgt>旧約聖書については、もちろん</tgt>` | 999 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1528 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースはあります。Aという人と</tgt>` | 1442 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1182 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 컨설턴트 예요. </src><tgt>Bという人がそれぞれコンサルタントで、お互いに</tgt>` | 2295 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 컨설턴트 예요. </src><tgt><\|wait\|></tgt>` | 1594 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src><\|wait\|></src><tgt>コンサルタントなんです。そう、コンサルタントなんです。</tgt>` | 2287 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>그리고 A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 2329 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>そして、Aという人が</tgt>` | 1904 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1531 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비란 사람이 </src><tgt>悪性コードを与えたとき、Bという人が</tgt>` | 1279 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스사이트 </src><tgt><\|wait\|></tgt>` | 1085 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크리 에서 </src><tgt>実際にクロスサイトクリレーションして、</tgt>` | 830 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>예시 파일 까지 </src><tgt><\|wait\|></tgt>` | 637 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>例のファイルまで感染してしまうかどうか……</tgt>` | 640 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1490 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt>私は</tgt>` | 638 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1426 |
| 4 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src><\|wait\|></src><tgt>最初のセクションで少し混乱していました。</tgt>` | 1117 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | 989 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src><\|wait\|></src><tgt>EHRの項目について</tgt>` | 868 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1605 |
| 8 | `<src>versus variant </src><tgt>決定的な重要性と、</tgt>` | `<src>versus variants </src><tgt>、それがバリアントと比べてどれほど重要かについて。</tgt>` | 2019 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1610 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>database, </src><tgt>データベースは</tgt>` | 755 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | 2477 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src><\|wait\|></src><tgt>もちろん私の大好きな分野です。</tgt>` | 1827 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | 1645 |
| 14 | `<src>upon the fields that need </src><tgt>つまり、</tgt>` | `<src>upon the fields that need </src><tgt>もし、</tgt>` | 1166 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these </src><tgt><\|wait\|></tgt>` | 835 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>これらのデータソースに含めるべき項目について合意できなければ、</tgt>` | 984 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 516 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right? </src><tgt>引き出すものが何もないということですよね？</tgt>` | 727 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 277 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1025 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼はイエスを</tgt>` | 877 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1363 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>He knows that </src><tgt>飢えていると知りました。</tgt>` | 1299 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | 1395 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src><\|wait\|></src><tgt>彼は、</tgt>` | 1648 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | 1625 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>And so he says </src><tgt>40日間荒野で食べ物もなかったことを知っていました。だから彼はこう言いました。</tgt>` | 1434 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | 1462 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it. </src><tgt>「おい、もしお前が神の御子なら、証明してみろ。</tgt>` | 2698 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1786 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えろ。」</tgt>` | 1688 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1053 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | 1096 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 918 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src><\|wait\|></src><tgt>その誘惑にどう対処したのでしょうか。</tgt>` | 564 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | 499 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>by bread alone. </src><tgt>人はパンだけで生きることはできない。</tgt>` | 524 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1241 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | 872 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1378 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>个人权利，最高法院</tgt>` | 1113 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 708 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt>最后才介入，而不是主导。</tgt>` | 1219 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 2113 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt>我不认为法院想</tgt>` | 1593 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1870 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change </src><tgt>成为</tgt>` | 737 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 2104 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>But they </src><tgt>当今社会变革的最前沿。但他们</tgt>` | 2085 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>rather reflect </src><tgt><\|wait\|></tgt>` | 1451 |
| 14 | `<src>the consensus </src><tgt>它们更倾向于</tgt>` | `<src>the consensus </src><tgt>更多反映的是</tgt>` | 1143 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 908 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>已经形成的共识。</tgt>` | 503 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 861 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have some </src><tgt>所以。</tgt>` | 415 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges </src><tgt><\|wait\|></tgt>` | 541 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>你有一些联邦法官，</tgt>` | 468 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 342 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1068 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1408 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분에서는</tgt>` | 1337 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是</src><tgt><\|wait\|></tgt>` | 1264 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>客厅的部分，</src><tgt>거실 부분,</tgt>` | 1466 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 944 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>那客厅一般都是</src><tgt>거실은 보통</tgt>` | 1588 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>属于我们要</src><tgt><\|wait\|></tgt>` | 1936 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src><\|wait\|></src><tgt>우리가</tgt>` | 1820 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>休息的地方，所以</src><tgt><\|wait\|></tgt>` | 981 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>呢，是身体的部分</src><tgt>쉴 공간이라서 신체 부분은</tgt>` | 2166 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，反映的是</src><tgt><\|wait\|></tgt>` | 1386 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt>필요한 부분을</tgt>` | 1128 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1050 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>一点时间可以</src><tgt>스스로</tgt>` | 815 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>好好地坐下来休息，</src><tgt><\|wait\|></tgt>` | 669 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们可以看到这边是</src><tgt>충분히 앉아서 쉬는 시간을 가져야 한다는 걸 보여줘요. 여기는</tgt>` | 839 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的吗？</src><tgt><\|wait\|></tgt>` | 395 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>啊，</src><tgt>아무도 없는 모습이네요. 아,</tgt>` | 351 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 340 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 905 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>この人々は極めて稀で、</tgt>` | 1084 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1329 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up to </src><tgt>よく</tgt>` | 1232 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1329 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>completely revolutionize the world </src><tgt>世界を完全に変革するような形で現れます。</tgt>` | 1664 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 818 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>their personality is </src><tgt>彼らの性格は</tgt>` | 1495 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a </src><tgt><\|wait\|></tgt>` | 1914 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src>contradiction. </src><tgt>矛盾をはらんでいます。</tgt>` | 1413 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1458 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的で、</tgt>` | 1982 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1557 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations </src><tgt>無意味な会話を嫌い、</tgt>` | 1214 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1109 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>and like to get straight to </src><tgt>直接</tgt>` | 874 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 540 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love to </src><tgt>本題に入ります。また、</tgt>` | 600 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>play </src><tgt><\|wait\|></tgt>` | 352 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, and they </src><tgt>悪魔の肩を借りて議論を振るうのが好きで、</tgt>` | 598 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 348 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 426 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 253 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>彼らは</tgt>` | 365 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | 343 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1298 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>당무 를 거부 한 </src><tgt>Lee Jun- seok</tgt>` | 726 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1346 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt>said he refused the party's nomination on the grounds of candidate selection,</tgt>` | 2090 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 696 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>and that he refused the nomination to secure the candidate's victory,</tgt>` | 2156 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1636 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>even putting on quite a show. But now</tgt>` | 2316 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2358 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt>with Yoon Suk- yeol as the candidate</tgt>` | 2052 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1485 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석은 </src><tgt>removing Kim Jong- in,</tgt>` | 1187 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>드러내 놓고 윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 1175 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt>Lee Jun- seok has openly declared his intention to knock Yoon Suk- yeol out</tgt>` | 1348 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 605 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt>and has shown</tgt>` | 396 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 401 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>a determined, aggressive stance</tgt>` | 292 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 274 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt>to defeat him.</tgt>` | 347 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상납건 </src><tgt><\|wait\|></tgt>` | 332 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt>Lee Jun- seok's sexual gratification scandal</tgt>` | 519 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 274 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt>is a point the Democratic Party</tgt>` | 365 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 332 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1047 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt>Well,</tgt>` | 802 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | 1089 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>みたいです。なのでここのね</src><tgt>it looks like they're making it right now in the cafeteria. So,</tgt>` | 1588 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスコンホテル</src><tgt><\|wait\|></tgt>` | 981 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src><\|wait\|></src><tgt>at the Golfson Hotel,</tgt>` | 881 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>も朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1829 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt>it's a place where you can have breakfast,</tgt>` | 1996 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1922 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ねここ</src><tgt>so I'm planning to go there later.</tgt>` | 2061 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスコンホテル</src><tgt><\|wait\|></tgt>` | 928 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I'll be staying at the Golfson Hotel</tgt>` | 2045 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>泊まりたいなという方はですね</src><tgt><\|wait\|></tgt>` | 1334 |
| 14 | `<src>検討なさってみて</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>検討なさってみて</src><tgt>if you're thinking of staying there,</tgt>` | 1265 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 1150 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なとはい。</src><tgt>you might want to consider it. Yeah.</tgt>` | 1044 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 329 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>ここのホテルからですね</src><tgt>I think it's a good idea.</tgt>` | 528 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅ももう</src><tgt><\|wait\|></tgt>` | 362 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt>From this hotel, you can walk to Busan Station</tgt>` | 450 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかるかと</src><tgt><\|wait\|></tgt>` | 316 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんなしか</src><tgt>in about a minute,</tgt>` | 261 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 263 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>リッチのいいねまあ</src><tgt>so it's not really that far,</tgt>` | 327 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | 371 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>and it's a nice hotel. So if you'd like,</tgt>` | 403 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 332 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください</src><tgt>please give it some thought.</tgt>` | 298 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね今回は。</src><tgt><\|wait\|></tgt>` | 196 |
