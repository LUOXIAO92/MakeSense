# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9930
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.9338
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.8646
  - TGT_RELEASE_TOTAL: 495
  - TGT_WAIT_ACCURACY: 0.7968
  - TGT_WAIT_TOTAL: 374
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1371.9690
  - PROCESS_TIME_MS_P50: 1400.1060
  - PROCESS_TIME_MS_P95: 2116.7920
  - PROCESS_TIME_MS_MAX: 2698.6930

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 883 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 994 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 1472 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>从一开始，这个孩子还才一年级呢。</tgt>` | 1442 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>この時点で</src><tgt>这时候</tgt>` | 1342 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | 1571 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1391 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1382 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>こうタイズしてってあげると</src><tgt>如果剪短枝条，收紧一点，</tgt>` | 1091 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>十年経っても</src><tgt>十年后</tgt>` | 1676 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>大した。</src><tgt>还是没什么。</tgt>` | 2141 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1474 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | 1554 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>边，这个油性也很大。</src><tgt>Take a few peanuts out, the oil in them is quite high.</tgt>` | 1896 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 961 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1353 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>呢，我再放一点</src><tgt>Then I'll add</tgt>` | 1806 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>核桃仁，</src><tgt>some walnuts,</tgt>` | 858 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1793 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>一个一个的，</src><tgt>one by one,</tgt>` | 1750 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | 1028 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>的。</src><tgt>these walnuts.</tgt>` | 1562 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1047 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is</tgt>` | 1636 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1263 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1103 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水、</src><tgt>water- give our children love,</tgt>` | 1590 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>and fertilize them,</tgt>` | 1666 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1241 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心理营养，</src><tgt>providing them with the psychological nourishment they need,</tgt>` | 2009 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1662 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>并耐心等待孩子</src><tgt>and patiently waiting for them</tgt>` | 1048 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>慢慢长大。</src><tgt>to grow up.</tgt>` | 1742 |

---

### Test Example 4 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1306 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1269 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. </src><tgt>非常に幸せな人々について重要な研究を行いました。</tgt>` | 1293 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>This is tip of the stem </src><tgt>これは</tgt>` | 1363 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>research, looking at </src><tgt>先端の研究で、</tgt>` | 1708 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>the 10% </src><tgt><\|wait\|></tgt>` | 1365 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1696 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>最も幸せな10%の人々を</tgt>` | 706 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People with </src><tgt>対象としています。</tgt>` | 1900 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>whom we can learn from. </src><tgt>私たちが学べる人々です。</tgt>` | 2045 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1262 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>抛洒完以后呢，</src><tgt>撒き終わった後、</tgt>` | 1815 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>内部的压力减轻，</src><tgt>内部の圧力が</tgt>` | 1209 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了，</src><tgt>低下し、エネルギーも衰えます。</tgt>` | 1858 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>然后</src><tgt>そして、</tgt>` | 1031 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | 1254 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1203 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>相对的低能量的运行</src><tgt>比較的低エネルギーの</tgt>` | 1907 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>状态，</src><tgt>稼働状態に留まります。</tgt>` | 1826 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | 1496 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>抑郁状态。</src><tgt>うつ状態です。</tgt>` | 1076 |

---

### Test Example 6 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1236 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气熟是容易的，</src><tgt>「気熟すれば</tgt>` | 1807 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src>但是</src><tgt>易い」ですが、</tgt>` | 1150 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师父</src><tgt>師匠がいれば</tgt>` | 1472 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1484 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>知道如何</src><tgt><\|wait\|></tgt>` | 1180 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>处于中间，</src><tgt>中間の取り方を教えてくれる</tgt>` | 1344 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>人しかいないので、</tgt>` | 1804 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>虚阿凡</src><tgt>虚阿凡は</tgt>` | 1761 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 1019 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师父。</src><tgt>師匠にならなければなりません。</tgt>` | 1653 |

---

### Test Example 7 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>아 저는 </src><tgt>Ah,</tgt>` | 930 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | 1194 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1468 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | 1444 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | 1407 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1612 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데요. </src><tgt>I've got ongsimi, kal ongsimi, and rice noodles mixed in.</tgt>` | 2266 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src>야, </src><tgt>Wow,</tgt>` | 1165 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1794 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>해장으로도 조금 죽입니다, </src><tgt>this is actually</tgt>` | 1752 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>진짜. </src><tgt>good enough for a hangover soup.</tgt>` | 907 |

---

### Test Example 8 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 968 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1547 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1103 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>We also have items like T- shirts available,</tgt>` | 1504 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ぜひご参加ください。</src><tgt>so please do join us.</tgt>` | 1499 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1330 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になりまして、</src><tgt>That's all for the contact information,</tgt>` | 1077 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1500 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1807 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>ランチの案内がありますので</src><tgt>and we have a lunch announcement,</tgt>` | 2020 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>もう少々お待ちください。</src><tgt>so please wait a moment.</tgt>` | 650 |

---

### Test Example 9 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` | 987 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` | 1113 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1284 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>your body. </src><tgt>进入你的身体。</tgt>` | 1240 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>紧张感</tgt>` | 1458 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>从哪里开始？是什么？</tgt>` | 2054 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | 1359 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是胸闷吗？</tgt>` | 1896 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>I ask them what </src><tgt>我问他们</tgt>` | 1772 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1918 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | 654 |

---

### Test Example 10 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1539 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>Those in the auspicious positions</tgt>` | 1308 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1147 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1202 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1888 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1211 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>왔기 때문 입니다. </src><tgt>They were drawn by chance.</tgt>` | 1978 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1735 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 모를 last </src><tgt><\|wait\|></tgt>` | 1061 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>던 교수 들은. </src><tgt>The professors who didn't know the truth...</tgt>` | 1766 |

---

### Test Example 11 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1118 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | 1444 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | 1496 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1374 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 961 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1629 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | 1507 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1782 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 517 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1764 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>같은 세대 들입니다. </src><tgt>They are the same generation that triggered the I Me- Bad People incident and killed their parents.</tgt>` | 2363 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大抵</src><tgt>通常</tgt>` | 1007 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>从这里开始，</tgt>` | 1200 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1378 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>我才做的，</tgt>` | 994 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1241 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 1617 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1348 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1030 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1758 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1760 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 1364 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>中学生でも。</src><tgt>就连乡村初中生也能看懂高更、高更、塞尚、雷诺瓦这些人的画。</tgt>` | 1559 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1268 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 993 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复练习。</tgt>` | 1433 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>学会复习。</tgt>` | 1342 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>Find what you're good at </src><tgt>找到你擅长的事情，</tgt>` | 1972 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>多做一些。</tgt>` | 1542 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1192 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>And what you're not good at, </src><tgt>而你不擅长的事情，</tgt>` | 2043 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>get the people around you to help you with. </src><tgt>就请周围的人帮忙。</tgt>` | 2284 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1861 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>And until next time. </src><tgt>我们下次再见。</tgt>` | 1769 |

---

### Test Example 14 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1063 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If you're a high school girl</tgt>` | 1838 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1148 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1420 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>and there's some kind of connection with someone who looks weird,</tgt>` | 2100 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>could it be</tgt>` | 1431 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 924 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里开始的？</src><tgt>that started that night?</tgt>` | 1535 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1730 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1748 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt>Yangzi's thoughts</tgt>` | 798 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>连篇。</src><tgt>were flowing.</tgt>` | 1693 |

---

### Test Example 15 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | 1576 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 990 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离一点点拉开，</tgt>` | 1865 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>オシャレる方がやっぱ</src><tgt>反而觉得</tgt>` | 1432 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>多いですね。</src><tgt>更时尚。</tgt>` | 1299 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>開業したい方って</src><tgt>想开店的人</tgt>` | 1445 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい</src><tgt><\|wait\|></tgt>` | 1107 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>自己意識高いし、</src><tgt>自我意识很强，</tgt>` | 1972 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>自分で</src><tgt><\|wait\|></tgt>` | 1788 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | 1342 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>傾向が強いので、</src><tgt>也倾向于自己投资，所以</tgt>` | 1382 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なので。</src><tgt>……</tgt>` | 1635 |

---

### Test Example 16 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 808 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>映画出てですね</src><tgt>I'm in a movie,</tgt>` | 1445 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1284 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1302 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>調べるときにまあ</src><tgt>and when we're checking if the movie is alive in various scenes,</tgt>` | 2461 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>映画の卵を調べる</src><tgt><\|wait\|></tgt>` | 1654 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことであの</src><tgt>we look at the movie's eggs,</tgt>` | 1356 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>そのその生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1242 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>保証する</src><tgt><\|wait\|></tgt>` | 1711 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>生息であることが保証する</src><tgt><\|wait\|></tgt>` | 1751 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>と言ったりしますな</src><tgt>and that guarantees it's alive.</tgt>` | 864 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | 1797 |

---

### Test Example 17 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これがギア</src><tgt>이게</tgt>` | 1155 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>です。</src><tgt>기어입니다.</tgt>` | 972 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが</src><tgt>기어가</tgt>` | 1456 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>緩むと芯が</src><tgt>느슨해지면</tgt>` | 1299 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1036 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>上げ下げできなくなってしまうので、</src><tgt>심을 올리고 내릴 수가 없게 됩니다. 그래서</tgt>` | 2201 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | 1432 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | 1442 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | 944 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついているっていうことです</src><tgt>달려 있는 거예요.</tgt>` | 1947 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1987 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src>はい、</src><tgt>네,</tgt>` | 1457 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | 654 |

---

### Test Example 18 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 725 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1141 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1467 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로 돌아가서</tgt>` | 1413 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | 1436 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>在他下班的时候，</src><tgt>퇴근 시간에</tgt>` | 1751 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1358 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국이나 밥을 해 드리고 싶어요. 정말</tgt>` | 2127 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1650 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时悲痛的时候，就直这么一个</src><tgt>그때 슬픔에 빠져 있었는데, 그냥 이렇게</tgt>` | 2349 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>小小的愿望</src><tgt>작은 소망 하나가</tgt>` | 1582 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt>있었어요.</tgt>` | 551 |

---

### Test Example 19 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | 1555 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>해가지고 내가 </src><tgt>Someone told me to make it with another brand of instant noodles,</tgt>` | 1625 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt>so I came in to kill it.</tgt>` | 2026 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | 1503 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 1404 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>해지 않았느냐? 내가 </src><tgt>Didn't I ask for it with another brand?</tgt>` | 1645 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 962 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1875 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I didn't hear that? Huh?</tgt>` | 2342 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 가. </src><tgt>I'm going.</tgt>` | 1770 |

---

### Test Example 20 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>面对这个情况，我们就是</src><tgt>In the face of this situation,</tgt>` | 1866 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1099 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>if you run into a problem, report to your supervisor immediately.</tgt>` | 2139 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方，</src><tgt>Or, if you're</tgt>` | 1851 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现有的这个状况，</src><tgt>at the other end, let them know about the current situation.</tgt>` | 1840 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt>Don't just</tgt>` | 1508 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>try to handle everything yourself.</tgt>` | 2043 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>独立承担。</src><tgt>You have to take responsibility.</tgt>` | 2168 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>整体而言，</src><tgt>Overall,</tgt>` | 1657 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>事业运就属凶。</src><tgt>your career luck is in decline.</tgt>` | 773 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1089 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then.</tgt>` | 1299 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>活蹦乱跳，</src><tgt>I was bouncing off the walls,</tgt>` | 1772 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src>所以</src><tgt>so I</tgt>` | 1110 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>坚持不开刀。</src><tgt>insisted on not having the surgery.</tgt>` | 1461 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间</src><tgt><\|wait\|></tgt>` | 1174 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | 1458 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>来诊断，</src><tgt>came to diagnose me,</tgt>` | 1441 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>一下敲腿，</src><tgt>a quick kick,</tgt>` | 938 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一下提腿，</src><tgt>a quick lift,</tgt>` | 1803 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>and they were all fine.</tgt>` | 2167 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们</src><tgt><\|wait\|></tgt>` | 1666 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>都很疑惑的离开。</src><tgt>They left, all full of confusion.</tgt>` | 817 |

---

### Test Example 22 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right, </src><tgt>好的，</tgt>` | 1317 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>这些例子之后，</tgt>` | 1520 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1234 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1449 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | 1717 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1353 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际上</tgt>` | 1358 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 888 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>要使用这些值。所以</tgt>` | 1914 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2145 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | 1777 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1091 |

---

### Test Example 23 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>そうです。</src><tgt>맞아요.</tgt>` | 831 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこで</src><tgt>그럼</tgt>` | 1006 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1521 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>テキという設備寺が</src><tgt>테키라는 시설이</tgt>` | 1420 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | 1452 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt>그리고</tgt>` | 1402 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1433 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt>나가이 케이요 씨의</tgt>` | 1656 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 865 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>は五経、</src><tgt>구조는 오경,</tgt>` | 1889 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2133 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設備寺、五比</src><tgt>시설 사경,</tgt>` | 1760 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>です。</src><tgt>오비입니다.</tgt>` | 1150 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt>제 이름은</tgt>` | 1054 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Kerenath Datt리고, </src><tgt>케레나스 닷트이고요,</tgt>` | 2162 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently </src><tgt>지금</tgt>` | 920 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1411 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | 1533 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Bachelor of Psychology </src><tgt>경영학 학사 과정과</tgt>` | 1893 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 979 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at the ANU, </src><tgt>ANU에서 심리학 학사 과정을</tgt>` | 1666 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1737 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>and in the future, I want to go into </src><tgt>수강하고 있어요. 그리고 앞으로는</tgt>` | 2340 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1716 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 가고 싶어요.</tgt>` | 1425 |

---

### Test Example 25 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1103 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Vanadium and things like that</tgt>` | 2148 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 952 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1332 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1748 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1615 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 843 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1775 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1640 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1547 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt>are so similar to insulin that they're called ' diabetes minerals '.</tgt>` | 1251 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt>And then,</tgt>` | 1696 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아연. </src><tgt>zinc.</tgt>` | 1255 |

---

### Test Example 26 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 너무 </src><tgt>これ、</tgt>` | 1100 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>저열한 일일 수 있지만 </src><tgt>ちょっと下品に聞こえるかもしれないけど、</tgt>` | 1990 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1425 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt>本当に菩薩ですよ。いや、</tgt>` | 2067 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分は菩薩なのに、飾る必要が</tgt>` | 2021 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>뭐 있고 </src><tgt>あるし、</tgt>` | 1713 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>南韓で菩薩に見える必要が</tgt>` | 2093 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>뭐 있어요. 우주 가 </src><tgt>ある。宇宙が</tgt>` | 2304 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | 1745 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>보살 이라는데. </src><tgt>菩薩だと言っているんだよ。</tgt>` | 1460 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1072 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>Like a stretched rubber band, </src><tgt>늘어난 고무줄처럼</tgt>` | 1919 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt>화학 결합은</tgt>` | 1098 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy, </src><tgt>에너지를 저장합니다.</tgt>` | 1523 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | 1982 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 위치 에너지가</tgt>` | 1589 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1418 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>다른 형태의 에너지로</tgt>` | 1010 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt>전환되는데, 예를 들어 열이나 빛 같은 거죠.</tgt>` | 2313 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1794 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>or gets used to make </src><tgt>또는</tgt>` | 1756 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>다른 결합을 만드는 데 사용됩니다.</tgt>` | 1456 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Or, or if you </src><tgt>あるいは、</tgt>` | 1207 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 1178 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何らかの文書を作成しなければならない場合、</tgt>` | 1772 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>文章を書く、</tgt>` | 1476 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1476 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | 1676 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 826 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. Like, oh, </src><tgt>言葉の綴りさえわからないことに気づくかもしれません。「ああ、</tgt>` | 2060 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>is this word </src><tgt>この単語は</tgt>` | 1783 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 2240 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1700 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam? I don't </src><tgt>ダブルP？ダブルL？</tgt>` | 1047 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src>know. </src><tgt>わからないな」</tgt>` | 967 |

---

### Test Example 29 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个就是</src><tgt>次は</tgt>` | 813 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1057 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>选择二级市场，哎，</src><tgt>セカンダリーマーケットですね。ああ、</tgt>` | 2232 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>服务</src><tgt><\|wait\|></tgt>` | 935 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一级一线</src><tgt>第一線、</tgt>` | 1315 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>トップトレーダーたちにサービスを</tgt>` | 2156 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说，呃，</src><tgt>提供するんです。例えば、えーと、</tgt>` | 1309 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1621 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>在做微信公众号十几年，你会</src><tgt>WeChat公式アカウントを10年以上やってる人なら、</tgt>` | 2567 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>发现</src><tgt><\|wait\|></tgt>` | 1723 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信公众号评分</src><tgt>WeChat公式アカウントの</tgt>` | 1750 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的新榜，然后</src><tgt>「新榜」の評価を</tgt>` | 1447 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>火了。</src><tgt>受けて、バズったのを見つけるでしょう。</tgt>` | 1075 |

---

### Test Example 30 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 908 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150만 개가 종업원 수 </src><tgt>150万人が</tgt>` | 2026 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>10명 미만 으로 </src><tgt>従業員数10人未満に</tgt>` | 1347 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>あたる非常に小さな企業が</tgt>` | 1611 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>多くありました。</tgt>` | 1243 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | 1348 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt>中小企業は成長するか、</tgt>` | 1310 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>혹은 폐업 할 길을 </src><tgt>あるいは廃業する道筋を</tgt>` | 1657 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>걷게 되는데 </src><tgt>たどりますが、</tgt>` | 2053 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | 2124 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | 1908 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | 1350 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>보이 게 된 거죠. </src><tgt>見せるようになりました。</tgt>` | 1188 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1294 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいんですが、</tgt>` | 1680 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>在这个罗马呢</src><tgt>このローマの</tgt>` | 1249 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>状況は一日にしてできたものではありません。</tgt>` | 1555 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>所以呢，</src><tgt>ですから、</tgt>` | 1411 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt>今</tgt>` | 1044 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>所面临的一些</src><tgt>皆さんが直面している</tgt>` | 1413 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊，跟风险</src><tgt>危機やリスクは、</tgt>` | 1906 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1788 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>一夕之间就</src><tgt>一晩で</tgt>` | 1416 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1171 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的，</src><tgt>生み出されたものではありません。</tgt>` | 1949 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>因此会建议</src><tgt>ですから、</tgt>` | 1273 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには、</tgt>` | 1184 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1019 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到了一个甜头，那</src><tgt>いいところまで来ましたね。</tgt>` | 1836 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt>もし</tgt>` | 859 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了甜头之后，</src><tgt>いいところまで来たら、</tgt>` | 1082 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你务必就要</src><tgt>ぜひ</tgt>` | 1400 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1605 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>先守住，</src><tgt>守り抜いてください。</tgt>` | 1389 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我再</src><tgt>「ああ、</tgt>` | 1908 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 522 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>继续操作下去哦。</src><tgt>まだ続けよう」なんて考えないでください。</tgt>` | 2164 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1854 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのかというと、</tgt>` | 1966 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1322 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>因为呢。</src><tgt>だって……</tgt>` | 1179 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src>这一张的部分呢，</src><tgt>이 부분은</tgt>` | 1319 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 1046 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>的人，但是</src><tgt>낚시를 하는 사람으로 보입니다. 하지만</tgt>` | 1174 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>它是属于逆向的，</src><tgt>이것은 역방향입니다.</tgt>` | 1892 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src>所以</src><tgt>그래서</tgt>` | 1030 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | 1563 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>时候，就要去</src><tgt>맞을 때는</tgt>` | 1831 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意，</src><tgt>특별히 주의해야 합니다.</tgt>` | 1657 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是它能不能够</src><tgt>그 사람이</tgt>` | 905 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지,</tgt>` | 1907 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>它钓不到鱼</src><tgt>잡지 못하는지</tgt>` | 1915 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1495 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>的意思哦。</src><tgt>의미입니다.</tgt>` | 1259 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new. </src><tgt>没什么新鲜事。</tgt>` | 1066 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There were </src><tgt><\|wait\|></tgt>` | 1006 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1467 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such interfaces before, </src><tgt>以前也有这样的接口，</tgt>` | 1330 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1459 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>netfilter, TC. </src><tgt>比如netfilter和TC。</tgt>` | 1917 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>Yeah, so </src><tgt>对，所以</tgt>` | 1263 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src>this is just </src><tgt>这只是</tgt>` | 1582 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>one another place </src><tgt>另一个地方</tgt>` | 626 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>可以看。</tgt>` | 1792 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src>But </src><tgt>但</tgt>` | 2064 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 529 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>developers or engineers </src><tgt>开发者或工程师</tgt>` | 1644 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>working on BugRepo </src><tgt>在做BugRepo的工作，</tgt>` | 1441 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>应该知道这一点。</tgt>` | 1353 |

---

### Test Example 35 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1419 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1171 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment, </src><tgt>제19조 수정안의 의미는</tgt>` | 1827 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore its </src><tgt>그리고</tgt>` | 1350 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이 역사는</tgt>` | 2003 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1427 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 866 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt>정치적 변화가</tgt>` | 1636 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침서입니다.</tgt>` | 2486 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1847 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 1893 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, are </src><tgt>물론 이 수정안의 의미는</tgt>` | 1591 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | 1255 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 782 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | 1012 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1556 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1331 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1462 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1840 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1320 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1630 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 682 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1990 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1984 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 1677 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | 1021 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | 1035 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1143 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1271 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | 1178 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>なですけど、おそらく</src><tgt>像十一二手这种，</tgt>` | 1759 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>十秒で。</src><tgt>大概十秒内。</tgt>` | 1428 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt>嗯，</tgt>` | 1038 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1498 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | 1355 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | 1498 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>ね。</src><tgt>算一秒内一定强度左右吧。</tgt>` | 846 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1577 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1925 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 565 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | 1807 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1293 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | 940 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>あるから。</src><tgt>因为大概有十一二手，还有宫马之类的。</tgt>` | 855 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 1060 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알거니와 너희 가 </src><tgt>知っているだろうが、</tgt>` | 1867 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt>異邦人として</tgt>` | 1150 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>いた時に、</tgt>` | 1426 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src>말 못하 는 </src><tgt>言葉も話せなかった</tgt>` | 1746 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>우상에게로 </src><tgt>偶像に</tgt>` | 1407 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>끄는 그대로 </src><tgt>引きずったのと同じように、</tgt>` | 988 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>引きずり込まれたのだ。</tgt>` | 1848 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1719 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>だから、私は</tgt>` | 1643 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちに</tgt>` | 869 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>告げます。</tgt>` | 1881 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | 1346 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는. </src><tgt>語る者は……</tgt>` | 1153 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 542 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1605 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>始めたばかりの</tgt>` | 1049 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get, </src><tgt>人は、</tgt>` | 1275 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1065 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and I have ten of them </src><tgt>「</tgt>` | 1474 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that I think are </src><tgt>これだけは押さえておけ」</tgt>` | 2122 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>really important. </src><tgt>と思うものを10個挙げるとしたら、</tgt>` | 1326 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1673 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I'm going to go into. </src><tgt>これから</tgt>` | 1791 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1219 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt>1分程度の動画をいくつか見ていきます。</tgt>` | 1426 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>この動画の後に</tgt>` | 1843 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1293 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>that cover each one </src><tgt>それぞれ</tgt>` | 975 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, but. </src><tgt>詳しく解説しているものです。ただ……</tgt>` | 976 |

---

### Test Example 40 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1284 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手</src><tgt>相手の</tgt>` | 1196 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>的感情或</src><tgt>感情や</tgt>` | 1223 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>真实意图的，</src><tgt>真意を察知する、</tgt>` | 1360 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1401 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1633 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>很多时候经常</src><tgt>よく</tgt>` | 1193 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>会听到人们</src><tgt>聞く</tgt>` | 882 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>这样说：“</src><tgt>言葉があります。</tgt>` | 1387 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「皆さん、</tgt>` | 1793 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt>この人は</tgt>` | 982 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了，</src><tgt>また嘘をついている」</tgt>` | 1645 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>と。</tgt>` | 1701 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。”</src><tgt>その目はすべてを物語っている」と。</tgt>` | 1469 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1273 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说。</src><tgt>つまり、</tgt>` | 416 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 813 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt>그렇다면</tgt>` | 1099 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう眠らせてやれ。</src><tgt>그냥 재워버려.</tgt>` | 1822 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt>난</tgt>` | 898 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1184 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있는 거야.</tgt>` | 1760 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1493 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>이제 한계가</tgt>` | 1321 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>遠い超えている。</src><tgt>아득히 멀리해.</tgt>` | 1980 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>ふざける奇跡よ。</src><tgt>장난 아니야, 이 기적은.</tgt>` | 1701 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 885 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1776 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>この大工をやってる</src><tgt>이 목수를</tgt>` | 1824 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>が、</src><tgt>오래 해온 사람이</tgt>` | 1412 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt>이렇게</tgt>` | 956 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>海賊船を</src><tgt>대단한 범선을</tgt>` | 796 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>본 적이 없어.</tgt>` | 802 |

---

### Test Example 42 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어가 면 </src><tgt>进入的话，</tgt>` | 1423 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>会非常迷路。</tgt>` | 1692 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1257 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1421 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>하건 거러 거로 </src><tgt><\|wait\|></tgt>` | 1638 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>다니 고간에 뭐 </src><tgt>开车或走的话，</tgt>` | 1787 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>강북 을 가면 </src><tgt>去江北的话，</tgt>` | 1190 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>不用说了，出国的话</tgt>` | 1456 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>또 장렬이에요. </src><tgt>也是悲惨的。</tgt>` | 1902 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 2084 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>신기 하네요. </src><tgt>挺神奇的。</tgt>` | 709 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>대신 에 이제 </src><tgt>不过现在</tgt>` | 1451 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1331 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>모바일 을 </src><tgt><\|wait\|></tgt>` | 1243 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>꾸나딘 것 같아요. </src><tgt>好像在努力搞移动端。</tgt>` | 607 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>예. </src><tgt>嗯。</tgt>` | 588 |

---

### Test Example 43 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1059 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어떻게 보면 </src><tgt>嗯，从某种意义上讲，</tgt>` | 1773 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1510 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1366 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | 1400 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 1348 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | 1351 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1681 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 516 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | 2003 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1894 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1703 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 713 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | 1346 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | 1190 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 928 |

---

### Test Example 44 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて</tgt>` | 1444 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>선생 이 뭐라 빌 거야. </src><tgt>先生が何か祈る言葉を</tgt>` | 1885 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>니한테 소름 이 돋든 </src><tgt>言ったとしても、</tgt>` | 1765 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>닭살이 돋든 </src><tgt>背中に鳥肌が立ったり、</tgt>` | 1735 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>느낌 이 오면 </src><tgt>何か感覚が</tgt>` | 1588 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 흔들 어서 </src><tgt>よ来たら、これを振って</tgt>` | 1543 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうってことなんだよ。</tgt>` | 988 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>귀신 이 오면 </src><tgt>幽霊が来たら</tgt>` | 2051 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>噛まれるし、</tgt>` | 1935 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | 1781 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>守ってくれる</tgt>` | 1382 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>찔러 줄 거니 까 </src><tgt>かもしれないから、</tgt>` | 984 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>リラックスして</tgt>` | 792 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | 836 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1106 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt>活動、</tgt>` | 884 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1654 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is because you're </src><tgt>つまり自分に基準を定めることですが、</tgt>` | 1588 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>absolutely correct, </src><tgt>その基準が完全に正しいので、</tgt>` | 1523 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src>but the reality </src><tgt>現実には</tgt>` | 1278 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is is that </src><tgt><\|wait\|></tgt>` | 1353 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 1851 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt>私たちが新しい世代だからです。そして、</tgt>` | 702 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>standards have </src><tgt>基準が</tgt>` | 1543 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 2189 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt>20年前に変わってから、</tgt>` | 1571 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt>私たちは</tgt>` | 580 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | 1790 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>everything at this point is being </src><tgt>今の時代、すべてが</tgt>` | 1145 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>held to a higher standard. </src><tgt>より高い基準に照らされているからです。</tgt>` | 913 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt>So, this is</tgt>` | 1554 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1303 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>というだけじゃなくて</src><tgt>not just a visual development environment.</tgt>` | 1419 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1380 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>It's a visual Python development environment.</tgt>` | 1905 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローリフを</src><tgt>That's because</tgt>` | 1588 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt>after you write a flowchart visually,</tgt>` | 1665 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt>it automatically</tgt>` | 948 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>に直さんそこから</src><tgt>converts it to Python code,</tgt>` | 2135 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成される。それが</src><tgt>and then generates it.</tgt>` | 2018 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt>When it runs,</tgt>` | 1701 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt>it performs signal processing.</tgt>` | 1436 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているからです。</src><tgt>That's the structure it's built on.</tgt>` | 1077 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 691 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt>Yes.</tgt>` | 749 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ。</src><tgt>So,</tgt>` | 671 |

---

### Test Example 47 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>金運についてですが、</tgt>` | 1551 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | 1310 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>很不错的，但是</src><tgt>とても良いと言えます。ただ、</tgt>` | 1317 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分，</src><tgt>正の金運に</tgt>` | 1768 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 1122 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>在事业方面的</src><tgt>偏る部分、つまり</tgt>` | 1454 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩成长所带来的红利</src><tgt>仕事の業績向上による恩恵です。</tgt>` | 1425 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>与收入的</src><tgt>収入や</tgt>` | 1497 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>提升。如果是在</src><tgt>収入の増加です。もし</tgt>` | 2059 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>投资理财方面呢，</src><tgt>投資や資産運用に関しては、</tgt>` | 2307 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 1876 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>悪くありませんが、</tgt>` | 1551 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>相对正财来说就</src><tgt>正の金運と比べると</tgt>` | 1337 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>稍微弱了那么一点。</src><tgt>少し弱めです。</tgt>` | 900 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 688 |

---

### Test Example 48 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1330 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1172 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1393 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1074 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>actually go in your education? Did you </src><tgt>실제로 학력이 어느 정도 되나요?</tgt>` | 2116 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>고등학교 졸업하셨나요?</tgt>` | 1808 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 858 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>That's one level of attainment. Did you go </src><tgt>그건 한 단계의 학력 수준입니다.</tgt>` | 2039 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>to college, </src><tgt>대학까지 다녔나요?</tgt>` | 1853 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>and if so, did you graduate? </src><tgt>만약 그렇다면, 졸업하셨나요?</tgt>` | 2340 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of </src><tgt>그건 또 다른</tgt>` | 1887 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt>학력 수준입니다.</tgt>` | 1645 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for </src><tgt>자, 이제</tgt>` | 1191 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>now. I'll see you </src><tgt>여기까지입니다.</tgt>` | 905 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 739 |

---

### Test Example 49 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 뭐 </src><tgt>だから、</tgt>` | 1035 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こういうケースも</tgt>` | 1757 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>있습니다. </src><tgt>あります。</tgt>` | 1022 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | 1221 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람 이 서로 </src><tgt>Bさんがお互いに</tgt>` | 1719 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>컨설턴트예요, </src><tgt>コンサルタントなんです。</tgt>` | 1851 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1114 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>모이 킹 컨설턴트여가지고 </src><tgt>モーキング・コンサルタントで、</tgt>` | 2098 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | 1786 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪性コードを</tgt>` | 2131 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>뿌렸 을 때 </src><tgt>ばらしたら、</tgt>` | 458 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>B라는 사람 이 </src><tgt>Bさんが</tgt>` | 1696 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1449 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングで</tgt>` | 1425 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | 853 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>感染しちゃうのか、という話です。</tgt>` | 807 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そして、これについて</tgt>` | 1117 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人が</tgt>` | 1311 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>내놓 았습니다. </src><tgt>分析を挙げています。</tgt>` | 1521 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 로쿠자 의 </src><tgt>ロクジャの</tgt>` | 1545 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>분석 을 보시면 </src><tgt>分析を見ると、</tgt>` | 1615 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니가 </src><tgt>ソニーが</tgt>` | 1234 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | 1091 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>파이프 를 </src><tgt>26ビットFPファームウェアを</tgt>` | 1974 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트로 낮춘 </src><tgt>128ビットに</tgt>` | 2146 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>것으로 보인다. </src><tgt>落としたようです。</tgt>` | 1960 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1700 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>Xbox Series X에서도 없는 </src><tgt>XboxSeriesXにはない</tgt>` | 916 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1138 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュ</tgt>` | 1189 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L3가 여기 도 없다. </src><tgt>L3もありません。</tgt>` | 917 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 690 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1406 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1043 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index is rising,</tgt>` | 1690 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1494 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | 1515 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will also rise sharply,</tgt>` | 1845 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 913 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1516 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1803 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1282 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 1293 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 항상 </src><tgt>but since the lighter stocks lead the market,</tgt>` | 2053 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 1575 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1183 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 882 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt>we should always keep an eye on those lighter- cap stocks.</tgt>` | 881 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1253 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 886 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>you will not be able to </src><tgt>你将无法</tgt>` | 1583 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1178 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1486 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | 1929 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>So, if </src><tgt>所以，如果</tgt>` | 1255 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 1687 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt>你遇到这种情况，</tgt>` | 608 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize </src><tgt>发现</tgt>` | 1567 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt>添加了错误的媒体</tgt>` | 2117 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>文件到某个资源，</tgt>` | 545 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>you need to let us know, </src><tgt>你需要告诉我们，</tgt>` | 1801 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt>我们就能</tgt>` | 1573 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1152 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files and then making sure they </src><tgt>移动这些媒体文件，并确保它们</tgt>` | 983 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 704 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>得到妥善备份。</tgt>` | 502 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | 1162 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1054 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>首次觉知到了那个现象：</src><tgt>프로이트는 그 현상을 처음으로 자각했습니다.</tgt>` | 1873 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1357 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>每当我们处于</src><tgt>우리가</tgt>` | 1298 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1349 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>爱之中，舒服位的爱，</src><tgt>사랑 속에 있을 때, 편안한 상태의 사랑을 경험할 때,</tgt>` | 2323 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 909 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>我们也同时进入恨。</src><tgt>우리는 동시에 증오 상태로 접어들게 됩니다.</tgt>` | 2412 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1860 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | 1708 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>它是爱；</src><tgt>사랑이고,</tgt>` | 1178 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>到了晚上，</src><tgt>밤에는</tgt>` | 753 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>它就变成恨。</src><tgt>증오로 변합니다.</tgt>` | 1181 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 784 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆</src><tgt>그 진자의 움직임이</tgt>` | 650 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 288 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>继续在移动。</src><tgt>계속해서 움직이고 있습니다.</tgt>` | 531 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point, </src><tgt>ある時、</tgt>` | 1280 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | 1174 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is hungry. </src><tgt>飢えていることを知りました。</tgt>` | 1496 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1065 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he's been without food, </src><tgt>彼は、</tgt>` | 1399 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>40日間プリミティブな荒野にいたせいで、飢えていることを知りました。</tgt>` | 2699 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>And so he says </src><tgt>だから彼は、</tgt>` | 938 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>to Jesus," Hey, </src><tgt>イエスに言いました。「おい、</tgt>` | 2230 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it. </src><tgt>もしお前が神の御子なら、証明してみろ。</tgt>` | 2168 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1640 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えろ。」</tgt>` | 1695 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1130 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | 896 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>その誘惑にどう対処したのでしょうか？</tgt>` | 811 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 511 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Man shall not live </src><tgt>人は</tgt>` | 405 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>by bread alone. </src><tgt>パンだけで生きることはできないのです。</tgt>` | 442 |

---

### Test Example 55 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>그럼</tgt>` | 967 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그 사진을 한번 볼까요?</tgt>` | 1572 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1269 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분에서는</tgt>` | 1101 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>的部分。</src><tgt>거실 부분이 보이네요.</tgt>` | 1564 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | 1432 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1433 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 862 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>在休息的地方，</src><tgt>쉴 때 쓰는 공간이에요.</tgt>` | 1829 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2161 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>所以呢，这身体的部分</src><tgt>그래서 이 신체 부분은</tgt>` | 1073 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | 1082 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 1504 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>一点时间，</src><tgt>잠시 시간을 내서</tgt>` | 1267 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 780 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>坐下来休息。可是</src><tgt>편안하게 앉아 쉬어야 한다는 걸 보여줘요. 하지만</tgt>` | 824 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>我们可以看到这边是</src><tgt>여기</tgt>` | 430 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>空无一人的嘛，</src><tgt>아무도 없는 걸 보면,</tgt>` | 502 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 341 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>그러니까...</tgt>` | 338 |

---

### Test Example 56 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1606 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 989 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>最初のセクションで少し混乱していました。</tgt>` | 1827 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1255 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the EHR fields </src><tgt>EHRの項目について</tgt>` | 1326 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1374 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>being of critical importance </src><tgt>重要性について</tgt>` | 1281 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus variant </src><tgt>議論する部分です。</tgt>` | 1494 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 850 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>databases, </src><tgt>バリアントデータベースと比較して、</tgt>` | 2082 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously one of my loves. </src><tgt>これは私にとって大好きな分野の一つです。</tgt>` | 2136 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1815 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>Is that if we don't agree </src><tgt>もし私たちが</tgt>` | 1635 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | 1206 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these </src><tgt><\|wait\|></tgt>` | 900 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>データソースに含めるべき項目について合意できなければ、</tgt>` | 935 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from, </src><tgt>利用できるデータソースは</tgt>` | 455 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right? </src><tgt>存在しないことになりますよね。</tgt>` | 558 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 372 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1477 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 1110 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | 1585 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>最高法院</tgt>` | 975 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt>不是主导的，而是后来跟进的。</tgt>` | 2326 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>And I don't think the courts want to be </src><tgt>而且我不认为法院想</tgt>` | 1529 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1300 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of social change </src><tgt><\|wait\|></tgt>` | 1903 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>anymore. </src><tgt>再当社会变革的最前沿了。</tgt>` | 2138 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>如今，</tgt>` | 481 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1739 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src>but they rather reflect </src><tgt>它们更多地反映了</tgt>` | 1325 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1087 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 602 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>that's already emerged. </src><tgt>已经形成的共识。</tgt>` | 917 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 605 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>So you have some </src><tgt>所以，</tgt>` | 516 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>federal judges </src><tgt>你有一些联邦法官</tgt>` | 440 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 381 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>……</tgt>` | 340 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>彼らは</tgt>` | 940 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>非常に珍しく、</tgt>` | 1245 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>and they often </src><tgt>よく</tgt>` | 1236 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1267 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1457 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>completely revolutionize the world. </src><tgt>世界を完全に変革するような出来事を引き起こします。</tgt>` | 2170 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1102 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>Their personality is </src><tgt>彼らの</tgt>` | 1546 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a </src><tgt><\|wait\|></tgt>` | 673 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src>contradiction. </src><tgt>性格は矛盾をはらんでいます。</tgt>` | 2104 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 1881 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ですが、</tgt>` | 1819 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1409 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations </src><tgt>無意味な会話や</tgt>` | 1094 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src>and like to </src><tgt><\|wait\|></tgt>` | 666 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 847 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>get straight to the point. </src><tgt>回りくどいやり取りを嫌い、要点をズバリ言うタイプです。</tgt>` | 1023 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love to </src><tgt>また、</tgt>` | 427 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>play </src><tgt><\|wait\|></tgt>` | 293 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, and they </src><tgt>悪魔の肩を貸すのも好きで、</tgt>` | 503 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 227 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 353 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 294 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 348 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>ENTP stands for </src><tgt>ENTPは</tgt>` | 366 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1604 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1351 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1151 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1426 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1747 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1519 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 832 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1733 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1826 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1502 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1062 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | 1747 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>드러내 놓고 윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 1455 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 1196 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뜻끼를 </src><tgt><\|wait\|></tgt>` | 515 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt><\|wait\|></tgt>` | 831 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 691 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 482 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>것입니다. </src><tgt>Previously, Lee Jun-seok even went to the candidate's camp, claiming he was doing it for the candidate's victory. But now, the moment Yoon Suk- yeol removed Kim Jong- in, Lee Jun-seok revealed his intent to attack and bring down the Yoon candidate.</tgt>` | 1227 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>과세 말 이준석의 </src><tgt><\|wait\|></tgt>` | 374 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>성상 납건. </src><tgt>The case of Lee Jun-seok's past misconduct.</tgt>` | 406 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 306 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 356 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 313 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt>How much of a boost is this for the opposition party?</tgt>` | 412 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1075 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | 1012 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | 1551 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>みたいですなのでここのね</src><tgt>It looks like they're making it in the cafeteria right now, so</tgt>` | 1896 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | 1067 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1318 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1563 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1415 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので</src><tgt>the Goldstone Hotel will also be a place where you can have breakfast.</tgt>` | 1138 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | 1767 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | 2045 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1717 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なっていう方はですね</src><tgt>If you're thinking of staying at the Goldstone Hotel in the future,</tgt>` | 1560 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 978 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>もまあいいんじゃないか</src><tgt>it might be worth considering.</tgt>` | 766 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 844 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>なとはい思いますここ</src><tgt>I think it's a good idea.</tgt>` | 851 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | 468 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | 362 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 374 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | 381 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | 373 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | 333 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいねまあ</src><tgt>The location is great— you can walk to Busan Station in about a minute or two.</tgt>` | 473 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>ホテルになってますので</src><tgt>Since it's a hotel,</tgt>` | 290 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>if you're interested,</tgt>` | 288 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 298 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください</src><tgt>please give it some thought.</tgt>` | 203 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>それではですね今回は。</src><tgt>Alright, that's it for this time.</tgt>` | 243 |
