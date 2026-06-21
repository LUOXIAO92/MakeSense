# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9513
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4437
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 8
  - TARGET_METRICS_FILTERED_TURN_COUNT: 123
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 52
  - TGT_RELEASE_ACCURACY: 0.9542
  - TGT_RELEASE_TOTAL: 131
  - TGT_WAIT_ACCURACY: 0.9967
  - TGT_WAIT_TOTAL: 615
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1315.2030
  - PROCESS_TIME_MS_P50: 1321.8780
  - PROCESS_TIME_MS_P95: 2189.8820
  - PROCESS_TIME_MS_MAX: 3338.3290

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1224 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>外在声音这一点，</src><tgt><\|wait\|></tgt>` | 935 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个优势</src><tgt><\|wait\|></tgt>` | 1041 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>很大。然后</src><tgt><\|wait\|></tgt>` | 825 |
| 5 | `<src><\|wait\|></src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>呢，</src><tgt>The external sound quality is a big advantage. And then,</tgt>` | 1656 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在面对</src><tgt><\|wait\|></tgt>` | 945 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人</src><tgt><\|wait\|></tgt>` | 1450 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1059 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>这个特点，</src><tgt><\|wait\|></tgt>` | 1499 |
| 10 | `<src>这种核桃</src><tgt>Then, I'll add some walnut kernels— this kind of</tgt>` | `<src>这种</src><tgt>when I face Tao Ren,</tgt>` | 1145 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和陶人。</src><tgt><\|wait\|></tgt>` | 1683 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 835 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1105 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲まだ</src><tgt><\|wait\|></tgt>` | 1012 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 722 |
| 5 | `<src>この時点で</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>あの時点で</src><tgt>一开始，尤其是仲还没一年级，所以</tgt>` | 1469 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう密告</src><tgt><\|wait\|></tgt>` | 1058 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1458 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう退ずして</src><tgt><\|wait\|></tgt>` | 1388 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>あげると</src><tgt><\|wait\|></tgt>` | 1161 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>十年経っても</src><tgt>就算退让选举，十年后</tgt>` | 1181 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>退した。</src><tgt><\|wait\|></tgt>` | 1648 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1130 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做什么？</src><tgt><\|wait\|></tgt>` | 886 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1091 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们身生的爱交</src><tgt><\|wait\|></tgt>` | 864 |
| 5 | `<src>爱浇水、</src><tgt>What parents need to do is this:</tgt>` | `<src>水，</src><tgt>What do parents need to do? Use our love and water</tgt>` | 1830 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>十分</src><tgt><\|wait\|></tgt>` | 731 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>去</src><tgt><\|wait\|></tgt>` | 590 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心里影响。</src><tgt><\|wait\|></tgt>` | 1063 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2249 |
| 10 | `<src>并耐心等待孩子</src><tgt>water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for</tgt>` | `<src>你耐心等</src><tgt>to deeply affect the child's heart. Be patient and</tgt>` | 1434 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 1625 |

---

### Test Example 4 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1241 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>직원 들은 </src><tgt><\|wait\|></tgt>` | 1151 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1168 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 737 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>The staff on the list actually had low intelligence,</tgt>` | 1338 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1012 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>직원 들이 </src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt><\|wait\|></tgt>` | 1901 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1413 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt>and they were randomly selected.</tgt>` | 1683 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>모을 닫던 교사 들은 </src><tgt><\|wait\|></tgt>` | 739 |

---

### Test Example 5 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 1175 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あのいただろうといったような</src><tgt><\|wait\|></tgt>` | 1341 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ものも用意しております</src><tgt><\|wait\|></tgt>` | 1428 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>のでぜひ</src><tgt>We also have T-shirts and similar items available, so please</tgt>` | 1437 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 685 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 948 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1629 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1522 |
| 10 | `<src><\|wait\|></src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src>連絡の</src><tgt>please join us. For contact, that's all for now.</tgt>` | 1599 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>案内がありますので</src><tgt><\|wait\|></tgt>` | 593 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1661 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 846 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>saying? </src><tgt><\|wait\|></tgt>` | 1116 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1299 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 856 |
| 5 | `<src>Where does the tension </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里</tgt>` | `<src>the tension start? </src><tgt>你的身体在说什么？把针尖放在身体上。紧张感从哪里开始？</tgt>` | 1737 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>What is it? Is it a </src><tgt><\|wait\|></tgt>` | 636 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>day? </src><tgt><\|wait\|></tgt>` | 1303 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it tension in your chest? </src><tgt><\|wait\|></tgt>` | 2167 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it a </src><tgt><\|wait\|></tgt>` | 1252 |
| 10 | `<src><\|wait\|></src><tgt>开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>lengthen which are you </src><tgt>是什么？是日期的压力吗？是胸部的紧张吗？还是你</tgt>` | 2342 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>using? </src><tgt><\|wait\|></tgt>` | 1346 |

---

### Test Example 7 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1187 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1181 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1285 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned and to repeat </src><tgt><\|wait\|></tgt>` | 1146 |
| 5 | `<src>Find what you're good at </src><tgt>最后，要重复。学会不断重复。找到你的长处，</tgt>` | `<src>find out you're good at </src><tgt>最后，重复一下。学完后，</tgt>` | 1211 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 673 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good </src><tgt><\|wait\|></tgt>` | 1490 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>yet. </src><tgt><\|wait\|></tgt>` | 1763 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>Get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 1628 |
| 10 | `<src><\|wait\|></src><tgt>多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>多做一些。不过，你还没完全掌握。让身边的人来帮你</tgt>` | 2166 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and tell them next time </src><tgt><\|wait\|></tgt>` | 1689 |

---

### Test Example 8 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 892 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 1087 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 957 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 834 |
| 5 | `<src>This is tip of the stem </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは</tgt>` | `<src>tip of the stem. </src><tgt>非常に幸せな人たちに関する研究をしましたか？これはまさにその入り口です。</tgt>` | 2187 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>Research looking at </src><tgt><\|wait\|></tgt>` | 589 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1365 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2281 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1236 |
| 10 | `<src>out there, </src><tgt>最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there. People that </src><tgt>最も幸せな人々の10%を対象にした研究です。その人たちは</tgt>` | 2638 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1088 |

---

### Test Example 9 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 903 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAがですね</src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1017 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうか</src><tgt><\|wait\|></tgt>` | 811 |
| 5 | `<src>調べるときに、</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area,</tgt>` | `<src>によっては</src><tgt>When it comes to whether it's raw or cooked, depending on the situation,</tgt>` | 2008 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>AAのランクを</src><tgt><\|wait\|></tgt>` | 698 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べたことで</src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうか</src><tgt><\|wait\|></tgt>` | 1646 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>を調べる生食で</src><tgt><\|wait\|></tgt>` | 1608 |
| 10 | `<src>ことを保証する</src><tgt>you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>かどうか保証する</src><tgt>we can guarantee whether it's raw or cooked based on the rank we find for AA.</tgt>` | 1935 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1614 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt><\|wait\|></tgt>` | 856 |

---

### Test Example 10 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1105 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1263 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>初めて</src><tgt><\|wait\|></tgt>` | 1244 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src>ゴッホ、</src><tgt>大致是从这一带开始的，</tgt>` | `<src>ご法</src><tgt>大概从这儿开始，</tgt>` | 1034 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ごうぎゃん</src><tgt><\|wait\|></tgt>` | 618 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1480 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>生産の</src><tgt><\|wait\|></tgt>` | 1886 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1392 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の</src><tgt>所以，</tgt>` | 1842 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵</src><tgt><\|wait\|></tgt>` | 1592 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 903 |

---

### Test Example 11 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 943 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 1180 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 1235 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>to set up </src><tgt><\|wait\|></tgt>` | 689 |
| 5 | `<src>ありましたね。</src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>7GBが</src><tgt>그래서 여기서 7GB를</tgt>` | 1108 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>ありましたが、</src><tgt><\|wait\|></tgt>` | 1165 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 463 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>ハセキエヨシの仕組み</src><tgt><\|wait\|></tgt>` | 1358 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1983 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>もうコン</src><tgt>설정하려고 했는데, 하세키에요시의 메커니즘은 이미</tgt>` | 1644 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1518 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>7GB</src><tgt><\|wait\|></tgt>` | 1590 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 853 |

---

### Test Example 12 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 837 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不够的人之间</src><tgt><\|wait\|></tgt>` | 1192 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有着某种</src><tgt><\|wait\|></tgt>` | 593 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>典型性，</src><tgt>If there's a certain type of relationship between a female high school student and someone who is not physically attractive,</tgt>` | 2229 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难他会是</src><tgt><\|wait\|></tgt>` | 577 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1362 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天而夜里开始的</src><tgt><\|wait\|></tgt>` | 2142 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1249 |
| 10 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1767 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1637 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>聊天。</src><tgt>it's hard for him to start a relationship that lasts from day to night. Yang Zisi chats with him.</tgt>` | 2080 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>あとなんか</src><tgt><\|wait\|></tgt>` | 1234 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1160 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1070 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 627 |
| 5 | `<src>多いですね。</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。</tgt>` | `<src>やっぱりですね</src><tgt>还有，大将好像有点想拉开距离，</tgt>` | 1685 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>介護したい方って</src><tgt><\|wait\|></tgt>` | 917 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐに行こう意識が</src><tgt><\|wait\|></tgt>` | 1477 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>高いし</src><tgt><\|wait\|></tgt>` | 2105 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>家で見てと</src><tgt><\|wait\|></tgt>` | 1341 |
| 10 | `<src>全部ちょっと次の投資</src><tgt>想创业的人自我意识都很强，而且</tgt>` | `<src>友達に言おうと</src><tgt>想照顾的人，会立刻产生“快去吧”的意识，而且</tgt>` | 2379 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>しようとしようとしようと</src><tgt><\|wait\|></tgt>` | 1479 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>するので</src><tgt><\|wait\|></tgt>` | 1662 |

---

### Test Example 14 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 908 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 슉빠시끼고 </src><tgt><\|wait\|></tgt>` | 1509 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1295 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt>I'm Apple, and I'm</tgt>` | 1401 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 족인 </src><tgt><\|wait\|></tgt>` | 1488 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 2089 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1326 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 1792 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt>the same generation as my own, like Herona and Park Chan,</tgt>` | 2131 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1610 |

---

### Test Example 15 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1092 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后呢，</src><tgt><\|wait\|></tgt>` | 1316 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力</src><tgt><\|wait\|></tgt>` | 1331 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src>然后</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、</tgt>` | `<src>衰弱了，然后就</src><tgt>淘撒が終わると、内部のエネルギーも衰弱して、</tgt>` | 1525 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1406 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1944 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态。</src><tgt><\|wait\|></tgt>` | 1414 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1853 |
| 10 | `<src>这就是所谓的</src><tgt>比較的低エネルギーの状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>相対的に低エネルギーな運行状態に留まってしまう。これが</tgt>` | 2093 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>逆流状态。</src><tgt><\|wait\|></tgt>` | 1710 |

---

### Test Example 16 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 1150 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1356 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的</src><tgt><\|wait\|></tgt>` | 1397 |
| 5 | `<src>或是通知对方，</src><tgt>In this situation, when we encounter a problem, we should</tgt>` | `<src>汇报主管，或是通知对方</src><tgt>When we face a problem, we should quickly report it to our supervisor or notify the other party</tgt>` | 1587 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们一下这个状况，</src><tgt><\|wait\|></tgt>` | 1488 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1749 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1517 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>工具理性</src><tgt><\|wait\|></tgt>` | 1812 |
| 10 | `<src>整体而言，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall,</tgt>` | `<src>成本，真的而已，</src><tgt>and not try to handle everything ourselves. It's really just a matter of cost- rational tools.</tgt>` | 2202 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是给工具</src><tgt><\|wait\|></tgt>` | 1655 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 층을 </src><tgt><\|wait\|></tgt>` | 1146 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 주고 내가 </src><tgt><\|wait\|></tgt>` | 1441 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수도다. </src><tgt><\|wait\|></tgt>` | 1589 |
| 5 | `<src>다른 잔찜에 </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src><\|wait\|></src><tgt>I might have come here to kill someone on another floor.</tgt>` | 1283 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔팀이 죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1549 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>하잖아. 내가 </src><tgt><\|wait\|></tgt>` | 1880 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1576 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>줄은 아니야. </src><tgt><\|wait\|></tgt>` | 1722 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh?</tgt>` | `<src>아. </src><tgt>Another team is asking for a kill. I'm not the one who's not hearing that. Ah.</tgt>` | 2358 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1483 |

---

### Test Example 18 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1252 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 1343 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1410 |
| 5 | `<src>옹심이가 </src><tgt>I'm having the ongsimi and kal- ongsimi—</tgt>` | `<src>어설 용심이 가 </src><tgt>I have a sword spirit, a sword spirit, and a sword spirit</tgt>` | 1609 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1354 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 2310 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1212 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1708 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover,</tgt>` | `<src>행으로도 조금 죽입니다. </src><tgt>mixed in. Wow, it really kills you even in a row. It's</tgt>` | 2288 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>진짜 </src><tgt><\|wait\|></tgt>` | 1572 |

---

### Test Example 19 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1050 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气数是容易的，</src><tgt><\|wait\|></tgt>` | 1340 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1321 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 1322 |
| 5 | `<src><\|wait\|></src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>一个师傅指导到</src><tgt>気数運は簡単に上がります。でも、師匠の指導が</tgt>` | 1531 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1422 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如初于中坚。</src><tgt><\|wait\|></tgt>` | 2332 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1095 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1767 |
| 10 | `<src>要成为</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src><\|wait\|></src><tgt>中堅に達するまで、師匠の指導がなければなりません。だから、反省が必要です。</tgt>` | 2280 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师傅，</src><tgt><\|wait\|></tgt>` | 1661 |

---

### Test Example 20 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 942 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是说</src><tgt><\|wait\|></tgt>` | 1053 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二classList，</src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>它服务</src><tgt><\|wait\|></tgt>` | 778 |
| 5 | `<src>在一级一线</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で</tgt>` | `<src>在一级一线</src><tgt>2つ目は、二つのクラスです。これらは</tgt>` | 1773 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼大的男女们。</src><tgt><\|wait\|></tgt>` | 917 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1402 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1670 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>维信运动好事期间，</src><tgt><\|wait\|></tgt>` | 1619 |
| 10 | `<src>发现</src><tgt>戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>一級一線で活動する男女です。例えば、維信運動の好事期間中、</tgt>` | 1931 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维信运动</src><tgt><\|wait\|></tgt>` | 1607 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>平分的星棒，</src><tgt><\|wait\|></tgt>` | 963 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1432 |

---

### Test Example 21 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴 찌 너무 </src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1127 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>이 저열하려 했지만 </src><tgt><\|wait\|></tgt>` | 1533 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1409 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 자기 의 </src><tgt>これ、あまりにも低く抑えようとしていたんですが、本当に菩薩です。いや、自分の</tgt>` | 1549 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 피로 고 </src><tgt><\|wait\|></tgt>` | 1507 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보이 고 </src><tgt><\|wait\|></tgt>` | 2196 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 이 보살 로 </src><tgt><\|wait\|></tgt>` | 1175 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 피로 고 보이 세 우주 까지 </src><tgt><\|wait\|></tgt>` | 1948 |
| 10 | `<src>지금 나한테 </src><tgt>自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に</tgt>` | `<src>다왔는데 이 보살 이란 </src><tgt>菩薩なのに夢のように見えて、私だけがこの菩薩に見えて、宇宙まで来てしまったんです。この菩薩とは</tgt>` | 2872 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>그냥 </src><tgt><\|wait\|></tgt>` | 831 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1099 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 764 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 700 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 1251 |
| 5 | `<src><\|wait\|></src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이</tgt>` | `<src>出せなくなって</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가</tgt>` | 2225 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>しまうので、</src><tgt><\|wait\|></tgt>` | 646 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1488 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 2194 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1220 |
| 10 | `<src>ついているっていうことです</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>付いているっていうこと</src><tgt>나오지 못하게 되니까 기어 끝에 역나사 너트가 붙어 있는</tgt>` | 2681 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1047 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい</src><tgt><\|wait\|></tgt>` | 1475 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文型完了を</src><tgt><\|wait\|></tgt>` | 733 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1218 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 1259 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1459 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1359 |
| 5 | `<src>the instruction </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>the instruction </src><tgt>好的。然后，在这些例子之后，</tgt>` | 1386 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1483 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1687 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1425 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 664 |
| 10 | `<src>these values. So </src><tgt>说明告诉我们要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>它告诉我们，实际上要使用这些值。所以</tgt>` | 2038 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1342 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game.board array </src><tgt><\|wait\|></tgt>` | 1815 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 635 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 964 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunhatteru. </src><tgt><\|wait\|></tgt>` | 1350 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1381 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a BA in </src><tgt><\|wait\|></tgt>` | 1348 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>Finance and a </src><tgt>제 이름은 Chunhatteru입니다. 현재 금융학 학사 학위와</tgt>` | 1569 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>BSc in Psychology. </src><tgt><\|wait\|></tgt>` | 1461 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2186 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 1232 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1695 |
| 10 | `<src>and in the future, I want to go into </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>심리학 학사 학위를 전공하고 있습니다. Yale에서</tgt>` | 2224 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1554 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 926 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 786 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1195 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个</src><tgt><\|wait\|></tgt>` | 1423 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>轨道，让我</src><tgt><\|wait\|></tgt>` | 1369 |
| 5 | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가고 싶어요.</tgt>` | `<src>能够好自在</src><tgt>제 삶의 궤도로 돌아가서</tgt>` | 1475 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>它下半段的时候，</src><tgt><\|wait\|></tgt>` | 1584 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在工作</src><tgt><\|wait\|></tgt>` | 1871 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>和生活之间</src><tgt><\|wait\|></tgt>` | 1364 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的过渡</src><tgt><\|wait\|></tgt>` | 1850 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>的时候，我当时被他</src><tgt>하반기를 편안하게 보낼 수 있도록, 일과 삶 사이의 전환기에</tgt>` | 2309 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>说一个小小</src><tgt><\|wait\|></tgt>` | 1634 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>的愿望哈。</src><tgt><\|wait\|></tgt>` | 1281 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1247 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1409 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1409 |
| 5 | `<src>and when those bonds are broken, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면</tgt>` | `<src>bonds are broken, </src><tgt>고무줄처럼 늘어난 화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면</tgt>` | 1650 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy gets </src><tgt><\|wait\|></tgt>` | 1370 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to </src><tgt><\|wait\|></tgt>` | 2189 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt><\|wait\|></tgt>` | 1277 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>heat or light. </src><tgt><\|wait\|></tgt>` | 1777 |
| 10 | `<src><\|wait\|></src><tgt>잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>Or gets used </src><tgt>그 잠재 에너지는 열이나 빛 같은 다른 형태의 에너지로 변환됩니다.</tgt>` | 2147 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds. </src><tgt><\|wait\|></tgt>` | 1657 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1076 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 634 |
| 5 | `<src>you realize that </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>you realize that </src><tgt>あるいは、何かを書きたい、テキストを書こうとしている場合、</tgt>` | 1915 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 717 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1498 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>and it's like oh, </src><tgt><\|wait\|></tgt>` | 2055 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1290 |
| 10 | `<src>spelled with a double </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>start with a double p? </src><tgt>スペルが全くわからないことに気づいて、「あ、この単語は『double p』で始まるの？」ってなる。</tgt>` | 3338 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 777 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double l, I don't know. </src><tgt><\|wait\|></tgt>` | 1764 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1456 |

---

### Test Example 28 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这章的部分</src><tgt><\|wait\|></tgt>` | 878 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1242 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1228 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>带调的人，但是他是</src><tgt><\|wait\|></tgt>` | 1271 |
| 5 | `<src>它是属于逆向的，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요.</tgt>` | `<src>属于逆向的。</src><tgt>이 장의 일부는 ' 조절하는 사람 '을 보여줍니다. 하지만 그는 역방향적인 사람입니다.</tgt>` | 1702 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这同样</src><tgt><\|wait\|></tgt>` | 1406 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>好像是一个状况</src><tgt><\|wait\|></tgt>` | 1368 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>需要去特别</src><tgt><\|wait\|></tgt>` | 1273 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>注意是</src><tgt><\|wait\|></tgt>` | 1001 |
| 10 | `<src>是它能不能够</src><tgt>그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>他能不能</src><tgt>이 상황은 특별히 주의해야 할 것 같습니다. 그가</tgt>` | 1984 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 1485 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他调不到</src><tgt><\|wait\|></tgt>` | 1177 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与他的意识</src><tgt><\|wait\|></tgt>` | 1053 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>了。</src><tgt><\|wait\|></tgt>` | 1474 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 948 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이런 것들은 </src><tgt><\|wait\|></tgt>` | 1239 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유실 이 일어났 습니다. </src><tgt><\|wait\|></tgt>` | 1511 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1225 |
| 5 | `<src>유사 한 작용 이 </src><tgt>Things like vanadium</tgt>` | `<src>거진 유산 한 적인 </src><tgt>There was a significant loss of vanadium. This is</tgt>` | 1506 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>물질 로는 굉장히 </src><tgt><\|wait\|></tgt>` | 1475 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1878 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다. </src><tgt><\|wait\|></tgt>` | 1638 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이거 굉장히 </src><tgt><\|wait\|></tgt>` | 1696 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>아주 </src><tgt>definitely a mineral. This is</tgt>` | 1804 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1352 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그 후에다가 </src><tgt><\|wait\|></tgt>` | 875 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아니 죠. </src><tgt><\|wait\|></tgt>` | 1444 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它到了一个</src><tgt><\|wait\|></tgt>` | 864 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>尖头，</src><tgt><\|wait\|></tgt>` | 1141 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1319 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了尖头之后，</src><tgt><\|wait\|></tgt>` | 1306 |
| 5 | `<src>请你务必就要</src><tgt>うまくいったなと思ったらね。その時は必ず利益を</tgt>` | `<src>请你务必</src><tgt>先端ができた場合、必ず</tgt>` | 1118 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 563 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>主要手阻，</src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着，哎，那我</src><tgt><\|wait\|></tgt>` | 2070 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>再去操作</src><tgt><\|wait\|></tgt>` | 1245 |
| 10 | `<src>继续操作下去哦。</src><tgt>確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>主要な手で操作してください。ああ、それから操作しようと思って。</tgt>` | 2127 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1598 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1568 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 728 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1540 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1109 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个</src><tgt><\|wait\|></tgt>` | 1093 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，不是</src><tgt><\|wait\|></tgt>` | 1191 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>一定要成的。</src><tgt><\|wait\|></tgt>` | 554 |
| 5 | `<src>所以呢，</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、</tgt>` | `<src>所以呢，</src><tgt>皆さんにお伝えしたいのは、このローマは必ずしも成功するわけではないということです。ですから、</tgt>` | 2196 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 587 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>有什么</src><tgt><\|wait\|></tgt>` | 1301 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>一些遗迹啊，</src><tgt><\|wait\|></tgt>` | 2214 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景</src><tgt><\|wait\|></tgt>` | 1205 |
| 10 | `<src>一夕之间就</src><tgt>今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是一致之间</src><tgt>今、遺跡や風景が一致しているわけではないので、</tgt>` | 2072 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就演变出来。</src><tgt><\|wait\|></tgt>` | 1661 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>它的</src><tgt><\|wait\|></tgt>` | 1603 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>引起会建议</src><tgt><\|wait\|></tgt>` | 605 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>你的一些朋友呢，</src><tgt><\|wait\|></tgt>` | 1583 |

---

### Test Example 32 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1022 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1170 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>符合广播条，</src><tgt><\|wait\|></tgt>` | 1427 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1331 |
| 5 | `<src>坚持不开刀。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery.</tgt>` | `<src>坚持不开道，</src><tgt>Everything was normal at the time, in line with the broadcast rules. So, I insisted on not opening the gate,</tgt>` | 1692 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1335 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 2202 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来整段，</src><tgt><\|wait\|></tgt>` | 1319 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 1701 |
| 10 | `<src>一下提腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>以下踢腿，</src><tgt>with a deadline of about twelve days. I kept kicking the gate,</tgt>` | 2083 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1701 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 733 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一会打开。</src><tgt><\|wait\|></tgt>` | 1186 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 868 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개 가 </src><tgt><\|wait\|></tgt>` | 1219 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중화 벌써 1000만으로 </src><tgt><\|wait\|></tgt>` | 1522 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1358 |
| 5 | `<src>많았습니다. </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。</tgt>` | `<src>많았습니다. </src><tgt>そのうち150社は、中国で1000万の売上を達成した、非常に小さな企業でした。</tgt>` | 1594 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1454 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 기업 들은 성장 하기나 </src><tgt><\|wait\|></tgt>` | 2782 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 에서 </src><tgt><\|wait\|></tgt>` | 614 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 되는데 </src><tgt><\|wait\|></tgt>` | 1690 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は</tgt>` | `<src>이번 에 </src><tgt>一般的に小さな企業は成長したり、海外でそうなることもありますが、今回は</tgt>` | 2040 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1618 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>폐업 도 하지 않은 </src><tgt><\|wait\|></tgt>` | 838 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1404 |

---

### Test Example 34 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1173 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1211 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1482 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1334 |
| 5 | `<src>history as a guide </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>19세 개정안의 의미와 그 역사를 탐구하며, 그것을</tgt>` | 1634 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1373 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change can </src><tgt><\|wait\|></tgt>` | 2022 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1347 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>happen in the United States. </src><tgt><\|wait\|></tgt>` | 1835 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침으로 삼고 있습니다.</tgt>` | 2351 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of the amendment </src><tgt><\|wait\|></tgt>` | 1583 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of course I'm </src><tgt><\|wait\|></tgt>` | 1565 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Maryed. </src><tgt><\|wait\|></tgt>` | 874 |

---

### Test Example 35 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1179 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 1124 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1308 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1249 |
| 5 | `<src>and I have ten of them </src><tgt>それは始めたばかりの人が手に入れるべきもので、</tgt>` | `<src>and I have ten of them </src><tgt>何かを始める必要がある人、そしてその10人</tgt>` | 1366 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 580 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1365 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1990 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 1483 |
| 10 | `<src>I have about </src><tgt>私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I have about one </src><tgt>が本当に重要な1人</tgt>` | 1825 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minutes </src><tgt><\|wait\|></tgt>` | 1535 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>at all this video. </src><tgt><\|wait\|></tgt>` | 905 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage of each one </src><tgt><\|wait\|></tgt>` | 1403 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1530 |
| 15 | `<src>in a little more detail, but. </src><tgt>この動画の後に、それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, </src><tgt>の動画に1分ほど使います。それぞれもう少し詳しく解説します。</tgt>` | 1108 |

---

### Test Example 36 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 862 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니 뭐니 </src><tgt><\|wait\|></tgt>` | 1292 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1440 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>말 못하 는 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない</tgt>` | `<src>말 못하는 </src><tgt>また、ここで異邦人として</tgt>` | 1370 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1430 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그때 로 </src><tgt><\|wait\|></tgt>` | 1552 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 1605 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 686 |
| 10 | `<src>그러므로 내가 </src><tgt>偶像に引かれるままに連れて行かれました。ですから、</tgt>` | `<src>그럼 으로 내가 </src><tgt>言葉を失い、偶像へと引きずられていきました。そうして</tgt>` | 2350 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1184 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1809 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 </src><tgt><\|wait\|></tgt>` | 1180 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>영으로 말하는 자는 </src><tgt><\|wait\|></tgt>` | 972 |
| 15 | `<src><\|wait\|></src><tgt>あなたがたに教えます。神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>あなたたちに伝えます。神の霊によって語る者は、</tgt>` | 837 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1003 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个财运可以说是</src><tgt><\|wait\|></tgt>` | 1242 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不好的，但是</src><tgt><\|wait\|></tgt>` | 1393 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较赚钱的部分</src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src>也就是</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり</tgt>` | `<src>也就是</src><tgt>財運に関しては、とても悪いと言えるでしょう。ただ、稼げる部分としては、</tgt>` | 1518 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的业绩</src><tgt><\|wait\|></tgt>` | 1414 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>和所带的红利</src><tgt><\|wait\|></tgt>` | 1929 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>以及收入的提升</src><tgt><\|wait\|></tgt>` | 1410 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1804 |
| 10 | `<src>投资理财方面呢，</src><tgt>仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>如果是在投资理财方面</src><tgt>事業の業績や得られる利益、収入の増加です。投資や資産運用に関しては、</tgt>` | 2153 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月也是</src><tgt><\|wait\|></tgt>` | 1678 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>不错，只是</src><tgt><\|wait\|></tgt>` | 467 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说</src><tgt><\|wait\|></tgt>` | 1435 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就算</src><tgt><\|wait\|></tgt>` | 797 |
| 15 | `<src><\|wait\|></src><tgt>悪くはないんですが、本業の収入に比べると少し弱めですね。</tgt>` | `<src>入了那么一点。</src><tgt>今月も悪くないですが、それほどではないかもしれません。</tgt>` | 1028 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十二手とか</src><tgt><\|wait\|></tgt>` | 1266 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>言った。おそらく</src><tgt><\|wait\|></tgt>` | 1399 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 1336 |
| 5 | `<src>まあ</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>まあ</src><tgt>他说十二手之类的。大概十秒钟，</tgt>` | 1454 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1491 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 2215 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt><\|wait\|></tgt>` | 1253 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1770 |
| 10 | `<src>でなんか</src><tgt>一秒一手多一点这样算。然后</tgt>` | `<src>でなんか</src><tgt>一秒左右的时间吧。然后</tgt>` | 1790 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 955 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十二手</src><tgt><\|wait\|></tgt>` | 1228 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1179 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 828 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮馬とかが</src><tgt>大概十二手，</tgt>` | 646 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 837 |

---

### Test Example 39 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1222 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세인보라 </src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 990 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 서름이 </src><tgt><\|wait\|></tgt>` | 799 |
| 5 | `<src>닭살이 돋든 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり</tgt>` | `<src>돋은 차리 돋은 </src><tgt>目を閉じて、戦場へ向かう。もう、</tgt>` | 2102 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 무야. </src><tgt><\|wait\|></tgt>` | 608 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1443 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1930 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1348 |
| 10 | `<src>물릴 거고 </src><tgt>何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、</tgt>` | `<src>무울 일 거고 </src><tgt>こうだ。こう揺らして一緒に遊ぼうってこと。きっと気性が荒いだろうし、</tgt>` | 2195 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 무울 일 거고 </src><tgt><\|wait\|></tgt>` | 1846 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1819 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>인찔러 주다니까 </src><tgt><\|wait\|></tgt>` | 1355 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에. </src><tgt><\|wait\|></tgt>` | 1079 |
| 15 | `<src>눈 감아. </src><tgt>神様が来たら守ってくれるように突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>きっと気性が荒いだろうし、きっと守ってくれるだろう。だから安心して。目を閉じて。</tgt>` | 1145 |

---

### Test Example 40 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 977 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1281 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>There was such </src><tgt><\|wait\|></tgt>` | 1330 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>interest before, </src><tgt><\|wait\|></tgt>` | 1370 |
| 5 | `<src><\|wait\|></src><tgt>没什么新鲜的。以前就有过这样的接口，</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事。以前确实很有兴趣，</tgt>` | 1483 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>net future TC. </src><tgt><\|wait\|></tgt>` | 1486 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1973 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>And so this is just </src><tgt><\|wait\|></tgt>` | 1432 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1826 |
| 10 | `<src>to look at. </src><tgt>比如netfilter和 TC。所以这只是另一个需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>netfutureTC。所以这只是另一个地方可以看看。</tgt>` | 2095 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1721 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1133 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 809 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on Bug Repos should be </src><tgt><\|wait\|></tgt>` | 879 |
| 15 | `<src>should be aware of that. </src><tgt>但开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 41 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 898 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>呃，</src><tgt><\|wait\|></tgt>` | 1121 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HTM이라고 하는 </src><tgt><\|wait\|></tgt>` | 1446 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1380 |
| 5 | `<src><\|wait\|></src><tgt>HTML是一种</tgt>` | `<src>이해 할 수 있고 </src><tgt>呃，计算机也应该能理解HTM，</tgt>` | 1486 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1507 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1777 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>있는 컴퓨터 어노에 </src><tgt><\|wait\|></tgt>` | 1517 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1835 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>맞게 우리 가 이제 </src><tgt>而且</tgt>` | 1651 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 895 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 1532 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1423 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 969 |
| 15 | `<src>필요 합니다. </src><tgt>我们需要按照它的语法来编写代码，而编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>我们现在需要编写代码，需要一个程序来编写这些代码。</tgt>` | 1108 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1106 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 1170 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1229 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 814 |
| 5 | `<src>actually go in your education? Did you </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>go in your education? </src><tgt>학력 수준. 실제로 교육을 얼마나 받았나요?</tgt>` | 1525 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 735 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1528 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 2153 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1395 |
| 10 | `<src>and if so, did you graduate? </src><tgt>고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>And then so did you graduate </src><tgt>고등학교를 졸업했나요? 그건 한 단계의 학력입니다. 대학에 갔나요? 그리고</tgt>` | 3162 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>that's another level of </src><tgt><\|wait\|></tgt>` | 1002 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1441 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 1739 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 784 |
| 15 | `<src>online. </src><tgt>그게 또 다른 단계입니다. 그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>그럼 또 한 단계의 학력입니다. 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 1176 |

---

### Test Example 43 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らせてやる。</src><tgt><\|wait\|></tgt>` | 1279 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1230 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1222 |
| 5 | `<src>今奇跡を見てる。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어.</tgt>` | `<src>ひどい女見てる。</src><tgt>그럼 젖게 해줄게. 난 끔찍한 여자를 보고 있어.</tgt>` | 1653 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1466 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1151 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1391 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>ふれを禁止する。</src><tgt><\|wait\|></tgt>` | 1172 |
| 10 | `<src><\|wait\|></src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>더 이상 한계는 넘어서는 건 금지야.</tgt>` | 1991 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1507 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなデイコを</src><tgt><\|wait\|></tgt>` | 1610 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 559 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1570 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>すごい解毒線を</src><tgt><\|wait\|></tgt>` | 816 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt>오랫동안 부나 데이코를 해왔어. 난 이렇게 엄청난 해독선을 본 적이 없어.</tgt>` | 1305 |

---

### Test Example 44 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 절수가 </src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt><\|wait\|></tgt>` | 1217 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 </src><tgt><\|wait\|></tgt>` | 1356 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>보인 다음에 이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1516 |
| 5 | `<src>큰 폭의 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src><\|wait\|></src><tgt>After seeing the stock price trend rising, this large- cap lead</tgt>` | 1387 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1510 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1744 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 1450 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1735 |
| 10 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>이 먼저 시장 을 </src><tgt>will see a large increase, but first, these volatile stocks</tgt>` | 1424 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 899 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1718 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요소 1초기 가변 온 </src><tgt><\|wait\|></tgt>` | 1212 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>종목 을 </src><tgt><\|wait\|></tgt>` | 808 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>눈으로 봐야 될 것 같습니다. </src><tgt>will be moving the market first. So, I think you'll need to watch these volatile stocks closely.</tgt>` | 1403 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 563 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1063 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1129 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1283 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1080 |
| 5 | `<src>absolutely correct, </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>because you're absolutely correct </src><tgt>活動、そして自分自身で基準を定義することです。なぜなら、</tgt>` | 1531 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 589 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1331 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat and </src><tgt><\|wait\|></tgt>` | 2528 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, and because </src><tgt><\|wait\|></tgt>` | 1047 |
| 10 | `<src>standards have </src><tgt>しかし現実には、</tgt>` | `<src>the standards have changed, </src><tgt>あなたは完全に正しいのですが、現実は、私たちが新しい猫であり、ブロックであり、基準が変わったからです。</tgt>` | 3132 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>from 2017 </src><tgt><\|wait\|></tgt>` | 959 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt><\|wait\|></tgt>` | 1436 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1300 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard </src><tgt><\|wait\|></tgt>` | 1015 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>2017年以来、私たちは基準に拘束されています。なぜなら、今のところ、</tgt>` | 1038 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 668 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1110 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 874 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1194 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 778 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに</tgt>` | `<src>B라는 사람이 </src><tgt>ですから、もちろんこういうケースもあります。AさんとBさんが</tgt>` | 1830 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨턴트예요. </src><tgt><\|wait\|></tgt>` | 826 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>B가 컨설턴트 이 </src><tgt><\|wait\|></tgt>` | 1704 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>어가지고 </src><tgt><\|wait\|></tgt>` | 2221 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람이 </src><tgt><\|wait\|></tgt>` | 1124 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>お互いにコンテナです。Bさんがコンサルタントで、Aさんが悪性コードを</tgt>` | 3161 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 816 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비라는 사람이 </src><tgt><\|wait\|></tgt>` | 1580 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로 사이트 </src><tgt><\|wait\|></tgt>` | 1315 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>스크립트에서 </src><tgt><\|wait\|></tgt>` | 1043 |
| 15 | `<src>EX 파일 까지 </src><tgt>配布したとします。その場合、Bさんは実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>XSP까지 </src><tgt>渡したとき、Bさんが実際にクロスサイトスクリプトでXSPまで</tgt>` | 1056 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>가능히 될까? </src><tgt><\|wait\|></tgt>` | 833 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>锤模和感知的</src><tgt><\|wait\|></tgt>` | 1191 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>目标感火真实</src><tgt><\|wait\|></tgt>` | 1422 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>图片的</src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src><\|wait\|></src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt>錘模と感度によるターゲット感火のリアルな画像。</tgt>` | 1530 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1424 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1714 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1540 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1065 |
| 10 | `<src>你们看，</src><tgt>するとき、よく耳にするのが「ほら、</tgt>` | `<src>你们看，</src><tgt>よく聞く言葉があります。見てください。</tgt>` | 1239 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1571 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>说黄了。</src><tgt><\|wait\|></tgt>` | 1416 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 745 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1355 |
| 15 | `<src><\|wait\|></src><tgt>また嘘をついている。目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>この人は「もうダメだ」と言っています。彼の目はすべてを物語っています。</tgt>` | 1231 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 834 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 700 |

---

### Test Example 48 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1328 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>と違ってですね</src><tgt><\|wait\|></tgt>` | 1382 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1296 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt>This is a visual Python development environment, unlike the visual development environment.</tgt>` | 1499 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1402 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルの書いてあと</src><tgt><\|wait\|></tgt>` | 1996 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>これやつは</src><tgt><\|wait\|></tgt>` | 1370 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードなんそっから生成される</src><tgt><\|wait\|></tgt>` | 1926 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつそれが</src><tgt>This one is a flow graph visual. And this one is Python code that gets generated from it.</tgt>` | 2228 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1655 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1300 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことに</src><tgt><\|wait\|></tgt>` | 902 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているからですね。</src><tgt><\|wait\|></tgt>` | 504 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt>It's for signal processing to be executed, so that's it. Yes.</tgt>` | 1056 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 596 |

---

### Test Example 49 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>드러가면 </src><tgt><\|wait\|></tgt>` | 1231 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해명 입니다. </src><tgt><\|wait\|></tgt>` | 1242 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1281 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1433 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>一进去就会晕头转向。不管是开车还是走路，</tgt>` | `<src>걸어 다니 고 </src><tgt>如果被揭穿，那可就不是小事了。因为我只是去开车，</tgt>` | 1654 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그런데 뭐 </src><tgt><\|wait\|></tgt>` | 1357 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 2071 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1372 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 는 것도 작렬 이요. </src><tgt><\|wait\|></tgt>` | 2020 |
| 10 | `<src>또 장렬이에요. </src><tgt>去江北就不用说了，去外国就更惨了。</tgt>` | `<src>좀 </src><tgt>但如果去往江北，那更是无话可说，去国外更是雪上加霜。我</tgt>` | 2204 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>진짜 아니 요. </src><tgt><\|wait\|></tgt>` | 1535 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1272 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 987 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>뭐 바요. 그거 는 </src><tgt><\|wait\|></tgt>` | 640 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>真有点丢人。不过，我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>아닌 것 같아요. </src><tgt>真的不是那样。不如现在努力工作吧。我觉得</tgt>` | 770 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 593 |

---

### Test Example 50 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1193 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어차피 보면 </src><tgt><\|wait\|></tgt>` | 1254 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1454 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1292 |
| 5 | `<src>함께 한 동생 이자 </src><tgt>怎么说呢，</tgt>` | `<src>이 동생 이자 </src><tgt>反正，</tgt>` | 1360 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 1555 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 2116 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1295 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1775 |
| 10 | `<src>책임감 보다는 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>재인감모다는 </src><tgt>他也是我们一起经历过二十岁的弟弟，所以也像家人一样。所以，</tgt>` | 2190 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1700 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1198 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 853 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 638 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓고 </src><tgt>把很多事情放下，</tgt>` | 953 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 849 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 857 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1137 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1414 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 </src><tgt><\|wait\|></tgt>` | 1375 |
| 5 | `<src>분석 을 보시면 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、</tgt>` | `<src>의 분석 을 보시면 </src><tgt>これについて多くの人が分析をしています。ここでロクジャの分析を見ると、</tgt>` | 1549 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 1438 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 60에 </src><tgt><\|wait\|></tgt>` | 2069 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FP 파이프를 </src><tgt><\|wait\|></tgt>` | 1395 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1841 |
| 10 | `<src>것으로 보인다. </src><tgt>ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>낮춘 것을 로포인 다. </src><tgt>ソニーがイエロク60のFPパイプを128ビットに下げていることがわかります。</tgt>` | 2539 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 1388 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1300 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1045 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>LSI가 </src><tgt><\|wait\|></tgt>` | 935 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>여기도 없다. </src><tgt>XboxシリーズにはないインフィニティキャッシュLSIもありません。</tgt>` | 962 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 420 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>for all e </src><tgt><\|wait\|></tgt>` | 883 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the source </src><tgt><\|wait\|></tgt>` | 1136 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>to be resolved, </src><tgt><\|wait\|></tgt>` | 1367 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but then we </src><tgt><\|wait\|></tgt>` | 1423 |
| 5 | `<src><\|wait\|></src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>should </src><tgt>모든 e의 소스 코드를 해결한 후,</tgt>` | 1417 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>continue </src><tgt><\|wait\|></tgt>` | 1447 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>to the next </src><tgt><\|wait\|></tgt>` | 981 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>pair, and then </src><tgt><\|wait\|></tgt>` | 1693 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>we can enter </src><tgt><\|wait\|></tgt>` | 1020 |
| 10 | `<src><\|wait\|></src><tgt>사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>다음 쌍으로 넘어가고,</tgt>` | 1815 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the next time it's on the stack, </src><tgt><\|wait\|></tgt>` | 1944 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>that's the one. </src><tgt><\|wait\|></tgt>` | 1786 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It's done. </src><tgt><\|wait\|></tgt>` | 1352 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>It becomes </src><tgt><\|wait\|></tgt>` | 1030 |
| 15 | `<src><\|wait\|></src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다.</tgt>` | `<src>the next one. </src><tgt>스택에 올라올 때 그게 바로 그겁니다. 끝났습니다. 다음으로 넘어갑니다.</tgt>` | 1230 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>That's the end. </src><tgt><\|wait\|></tgt>` | 856 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt><\|wait\|></tgt>` | 574 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>in a loop. </src><tgt><\|wait\|></tgt>` | 566 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1318 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1072 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1192 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 554 |
| 5 | `<src>about the EHR fields </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの</tgt>` | `<src>about the AHR field </src><tgt>AHRの最初のセクションで、少し間違った場所に入ってしまいました。</tgt>` | 2055 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 571 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance versus </src><tgt><\|wait\|></tgt>` | 1371 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1685 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant data </src><tgt><\|wait\|></tgt>` | 1506 |
| 10 | `<src>databases, </src><tgt>決定的な重要性と、</tgt>` | `<src>bases, which is obviously </src><tgt>重要なデータベースであることと、バリアントデータベースであることの対比についてです。これは明らかに</tgt>` | 2022 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1656 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 922 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1508 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1285 |
| 15 | `<src>to be in these </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、</tgt>` | `<src>to be in these data </src><tgt>私の好きなテーマの一つです。つまり、これらのデータに含めるべきフィールドについて合意できなければ、</tgt>` | 1401 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>sources that we can </src><tgt><\|wait\|></tgt>` | 836 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 865 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 607 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 537 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 1258 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1333 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>be able to move media objects </src><tgt><\|wait\|></tgt>` | 1470 |
| 5 | `<src><\|wait\|></src><tgt>另外，你没法</tgt>` | `<src><\|wait\|></src><tgt>另外，你将无法</tgt>` | 1366 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources </src><tgt><\|wait\|></tgt>` | 1509 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though if </src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the situation </src><tgt><\|wait\|></tgt>` | 1548 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 708 |
| 10 | `<src>where you realize </src><tgt>在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>where you realize you've added </src><tgt>在资源之间移动媒体对象，但如果你发现</tgt>` | 2059 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1312 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>the wrong media files to a particular resource, </src><tgt><\|wait\|></tgt>` | 1930 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>we'll let us know. </src><tgt><\|wait\|></tgt>` | 1563 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>Now, and we can see about </src><tgt><\|wait\|></tgt>` | 932 |
| 15 | `<src><\|wait\|></src><tgt>给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法</tgt>` | `<src><\|wait\|></src><tgt>将错误的文件添加到特定资源中，我们会通知你。现在，我们可以</tgt>` | 1056 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure </src><tgt><\|wait\|></tgt>` | 818 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 577 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>they get back up properly. </src><tgt><\|wait\|></tgt>` | 604 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 883 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>and it warns Jesus </src><tgt><\|wait\|></tgt>` | 1194 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>of hunger. </src><tgt><\|wait\|></tgt>` | 1292 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1404 |
| 5 | `<src>he's been without food, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに</tgt>` | `<src>he's going to </src><tgt>ある時、イエスは飢えについて警告します。彼は、</tgt>` | 1523 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1488 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry, </src><tgt><\|wait\|></tgt>` | 2778 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 830 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 1710 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the son of God, prove it </src><tgt>40日間、荒野で飢えていることを知っています。だからイエスに言います。「もしあなたが神の子なら、</tgt>` | 2871 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>turn these stones to bread. </src><tgt><\|wait\|></tgt>` | 1393 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 955 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>deal with that? </src><tgt><\|wait\|></tgt>` | 953 |
| 15 | `<src>temptation? </src><tgt>この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>The temptation. </src><tgt>この石をパンに変えなさい。イエスはそれをどう乗り越えたのでしょうか？誘惑にどう対処したのでしょうか。</tgt>` | 1108 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 551 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 647 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>Alone. </src><tgt><\|wait\|></tgt>` | 346 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1241 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 968 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, and </src><tgt><\|wait\|></tgt>` | 1032 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>the Supreme Court </src><tgt><\|wait\|></tgt>` | 800 |
| 5 | `<src>came along </src><tgt>有意义的个人权利，而最高法院</tgt>` | `<src>came along last, </src><tgt>有意义的个人权利，而最高法院最后才介入，</tgt>` | 1999 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I I don't know </src><tgt><\|wait\|></tgt>` | 843 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1555 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2212 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1124 |
| 10 | `<src>change </src><tgt>是最后才介入的，不是引领者。我不认为</tgt>` | `<src>social change. </src><tgt>而不是引领社会变革。我不知道法院是否想成为社会变革的先锋。</tgt>` | 2424 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days, </src><tgt><\|wait\|></tgt>` | 1296 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but they rather </src><tgt><\|wait\|></tgt>` | 1759 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1245 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 838 |
| 15 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，它们更倾向于</tgt>` | `<src>that's already </src><tgt>但现在，他们更多地反映的是已经达成共识的</tgt>` | 967 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 607 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 749 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 428 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 595 |
| 20 | `<src><\|wait\|></src><tgt>反映已经形成的共识。所以，有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 399 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 354 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 1222 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1347 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1454 |
| 5 | `<src>的一个是客厅</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면</tgt>` | `<src>了一个是克汀，</src><tgt>그럼 사진을 한번 볼게요. 사진 부분에는 크틴이</tgt>` | 1539 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>的部分，</src><tgt><\|wait\|></tgt>` | 1357 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>克汀一般</src><tgt><\|wait\|></tgt>` | 1953 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是属于</src><tgt><\|wait\|></tgt>` | 1352 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1856 |
| 10 | `<src>在休息的地方，</src><tgt>거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>在修饰的地方。</src><tgt>있는데, 크틴은 보통 우리가 수식하는 부분에 속해요.</tgt>` | 2149 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1687 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分。</src><tgt><\|wait\|></tgt>` | 751 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它反映的是</src><tgt><\|wait\|></tgt>` | 1179 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>我们需要给</src><tgt><\|wait\|></tgt>` | 736 |
| 15 | `<src>一点时间，</src><tgt>그래서 이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>自己一点时间</src><tgt>그러니까 이건 신체 부분이에요. 우리가</tgt>` | 1016 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好</src><tgt><\|wait\|></tgt>` | 718 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>的做一下</src><tgt><\|wait\|></tgt>` | 460 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>休息，可以看到</src><tgt><\|wait\|></tgt>` | 547 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是双耳人的嘛。</src><tgt><\|wait\|></tgt>` | 422 |
| 20 | `<src>啊，</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는 아무도 없네요.</tgt>` | `<src>好，</src><tgt>잠시 쉬면서 잘 쉬어야 해요. 여기는 양쪽 귀 부분이에요. 자,</tgt>` | 588 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以说是说。</src><tgt><\|wait\|></tgt>` | 326 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 882 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1177 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1321 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1248 |
| 5 | `<src><\|wait\|></src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>completely </src><tgt>彼らは全く珍しく、</tgt>` | 1028 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>revolutionize the world. </src><tgt><\|wait\|></tgt>` | 719 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1414 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>is something </src><tgt><\|wait\|></tgt>` | 1654 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>of a contradiction. </src><tgt><\|wait\|></tgt>` | 1545 |
| 10 | `<src>contradiction. </src><tgt>世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>世界を完全に革命する存在です。その性格は矛盾をはらんでいます。</tgt>` | 1644 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>Well, they're extroverted, </src><tgt><\|wait\|></tgt>` | 743 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>they also </src><tgt><\|wait\|></tgt>` | 1561 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1290 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 856 |
| 15 | `<src>and like to </src><tgt>外交的である一方、無意味な会話は嫌います。そして、</tgt>` | `<src>And like to </src><tgt>外向的で、無意味な会話を嫌います。そして</tgt>` | 1723 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt><\|wait\|></tgt>` | 804 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 792 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 782 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 543 |
| 20 | `<src>the devil's advocate, and they </src><tgt>要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and then </src><tgt>本題に入ります。また、悪魔の代弁者になるのも好きです。</tgt>` | 794 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 389 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 376 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 300 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.P. Stansfield </src><tgt><\|wait\|></tgt>` | 358 |
| 25 | `<src>ENTP stands for </src><tgt>議論を避けることはありません。ENTPとは</tgt>` | `<src>or. </src><tgt>議論を避けることは決してありません。E.P.サンズフィールドや。</tgt>` | 479 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今作って</src><tgt><\|wait\|></tgt>` | 1220 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>みたいです。</src><tgt><\|wait\|></tgt>` | 1252 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 653 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ここのねゴルフスローンホテル</src><tgt>Well, it looks like they're making something right after the meal. So</tgt>` | 1973 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も朝食が</src><tgt><\|wait\|></tgt>` | 598 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1354 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1601 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1485 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt>the Golf Swan Hotel is also a place where you can have breakfast. So, going forward,</tgt>` | 1802 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 585 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1595 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>な方はですね</src><tgt><\|wait\|></tgt>` | 1534 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討させて</src><tgt><\|wait\|></tgt>` | 610 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>見てまあいいんじゃない</src><tgt>if you're thinking about staying at the Golf Swan Hotel, let's consider it. I think it's a good idea</tgt>` | 2256 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 953 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 619 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 465 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 576 |
| 20 | `<src><\|wait\|></src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 573 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかるか</src><tgt><\|wait\|></tgt>` | 388 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんないか</src><tgt><\|wait\|></tgt>` | 398 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね立地の</src><tgt><\|wait\|></tgt>` | 341 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>いいねまあホテル</src><tgt><\|wait\|></tgt>` | 310 |
| 25 | `<src>ホテルになってますので</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 289 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 301 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさって</src><tgt><\|wait\|></tgt>` | 261 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>みてください</src><tgt><\|wait\|></tgt>` | 256 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね今回は</src><tgt><\|wait\|></tgt>` | 251 |

---

### Test Example 60 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 968 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>정무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1273 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1377 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1292 |
| 5 | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>후보 의 당선을 </src><tgt>Lee Jun- seok, who previously refused to take on political duties, was running for the nomination</tgt>` | 1656 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1442 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 2530 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 936 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1783 |
| 10 | `<src>김종인 을 </src><tgt>for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>김정은을 </src><tgt>while claiming to be for the candidate's victory, he even made a bit of a show of it. But now, Yoon Suk- yeol's campaign</tgt>` | 2895 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제간 순간 </src><tgt><\|wait\|></tgt>` | 928 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석을 들으 내놓고 </src><tgt><\|wait\|></tgt>` | 1628 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 870 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 898 |
| 15 | `<src><\|wait\|></src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>독기 를 품은 </src><tgt>is filled with the resolve to defeat Lee Jun- seok the moment he was brought up, and Yoon Suk- yeol's campaign</tgt>` | 1302 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 548 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 성을 보이 기로 </src><tgt><\|wait\|></tgt>` | 431 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 381 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt><\|wait\|></tgt>` | 353 |
| 20 | `<src><\|wait\|></src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's</tgt>` | `<src>가슴 발 </src><tgt>is preparing to attack.</tgt>` | 277 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 청상 납권 </src><tgt><\|wait\|></tgt>` | 379 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 286 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 274 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 얼마나 </src><tgt><\|wait\|></tgt>` | 275 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute— what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 입니까? </src><tgt>How big of a boon is this for the Democratic Party's attack on Lee Jun- seok's nomination?</tgt>` | 435 |
