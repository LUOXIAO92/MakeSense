# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9262
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5033
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.9683
  - TGT_RELEASE_TOTAL: 63
  - TGT_WAIT_ACCURACY: 0.9963
  - TGT_WAIT_TOTAL: 806
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1577.4810
  - PROCESS_TIME_MS_P50: 1499.5090
  - PROCESS_TIME_MS_P95: 2925.5580
  - PROCESS_TIME_MS_MAX: 4279.3760

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1467 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 969 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1168 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1385 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 734 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 2425 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 826 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>였기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 1910 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1963 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 2229 |
| 11 | `<src>교사 들은. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random. The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교사 들은 </src><tgt>The students in the prime spots were actually not that intelligent. They were just randomly selected. The teachers who didn't know the truth</tgt>` | 2793 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 972 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 996 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1438 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1620 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点でこう</src><tgt><\|wait\|></tgt>` | 1522 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>ミミク枠</src><tgt><\|wait\|></tgt>` | 1799 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1988 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1906 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こう退ずしてね上げると</src><tgt><\|wait\|></tgt>` | 1141 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1924 |
| 11 | `<src>大した。</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，十年后也不会有什么大……</tgt>` | `<src>同じだ。</src><tgt>从一开始，孩子还是小学一年级。那时候就给他们选了“模仿”的职位，十年后还是老样子。</tgt>` | 3072 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1348 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是</src><tgt><\|wait\|></tgt>` | 1135 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1428 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1618 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水，</src><tgt><\|wait\|></tgt>` | 1942 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 1347 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给他子</src><tgt><\|wait\|></tgt>` | 1918 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心灵营养，</src><tgt><\|wait\|></tgt>` | 1913 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>给他</src><tgt><\|wait\|></tgt>` | 718 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢的</src><tgt><\|wait\|></tgt>` | 2392 |
| 11 | `<src>慢慢长大。</src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for them to grow slowly.</tgt>` | `<src>长大。</src><tgt>What parents need to do is water them with our deep love, fertilize them with nourishment for their hearts, and let them grow up slowly.</tgt>` | 3109 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1447 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>得送子儿的事儿，这个</src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>游子也很大？</src><tgt><\|wait\|></tgt>` | 1503 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1566 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢？</src><tgt><\|wait\|></tgt>` | 1527 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在拜干爹，</src><tgt><\|wait\|></tgt>` | 1800 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人，</src><tgt><\|wait\|></tgt>` | 1882 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1225 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>这里说，</src><tgt><\|wait\|></tgt>` | 1236 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 2341 |
| 11 | `<src>仁儿。</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels— this kind of walnut kernels.</tgt>` | `<src>喝陶人。</src><tgt>Why is it that the son must be sent away? And the son is also so great? Then I go to the godfather and the Tao people. Here it says, these Tao people...</tgt>` | 3450 |

---

### Test Example 5 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 1056 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1002 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떨 표할지 고 </src><tgt><\|wait\|></tgt>` | 1479 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1339 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 507 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>포모를 </src><tgt><\|wait\|></tgt>` | 1969 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>죽인 대로나 </src><tgt><\|wait\|></tgt>` | 1223 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1878 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 2168 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt><\|wait\|></tgt>` | 2667 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents. They are the same generation as him.</tgt>` | `<src>다. </src><tgt>I'm not sure how to react. I'm from the generation that killed their FOMO, the generation of Park Han- sang, and so on.</tgt>` | 3368 |

---

### Test Example 6 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1287 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 980 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めたもので、</src><tgt><\|wait\|></tgt>` | 1046 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 677 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1639 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 2281 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 951 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1910 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1928 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ルナールなどという人の絵</src><tgt><\|wait\|></tgt>` | 2390 |
| 11 | `<src>は、田舎の</src><tgt>大致是从这一带开始的，像梵高、高更、塞尚、雷诺阿他们的画，连乡下的</tgt>` | `<src><\|wait\|></src><tgt>大概是从这里开始的，比如高更、高冈、塞尚、伦纳尔这些人的画，</tgt>` | 2381 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>は田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1463 |

---

### Test Example 7 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1375 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1022 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1457 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt><\|wait\|></tgt>` | 1444 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 642 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください</src><tgt><\|wait\|></tgt>` | 1890 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1020 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりまして</src><tgt><\|wait\|></tgt>` | 2041 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1906 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>よろしく</src><tgt><\|wait\|></tgt>` | 2171 |
| 11 | `<src>ランチの案内がありますので</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements, and we have some info about lunch,</tgt>` | `<src>ない内容がありますので</src><tgt>We also have items like T- shirts available, so please feel free to join us. That's all for the contact information. Um, we have some other details, so</tgt>` | 3108 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>もう少しお待ちください</src><tgt><\|wait\|></tgt>` | 1017 |

---

### Test Example 8 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 970 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 963 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1327 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 959 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 962 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 2309 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 975 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 2110 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | 2086 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>language are you </src><tgt><\|wait\|></tgt>` | 2473 |
| 11 | `<src>language are you using? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，你在用什么语言？</tgt>` | `<src>using? </src><tgt>你的身体在做什么？进入你的身体。紧张感从哪里开始？是什么？是头痛吗？是胸闷吗？我问他们，你用的是什么语言？</tgt>` | 3473 |

---

### Test Example 9 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1217 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | 1189 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1372 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有一个师傅</src><tgt><\|wait\|></tgt>` | 1594 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>知道，</src><tgt><\|wait\|></tgt>` | 1793 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如何处于中间，</src><tgt><\|wait\|></tgt>` | 2039 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1816 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 774 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2313 |
| 11 | `<src>一个师父。</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅。</src><tgt>気性が冷めていれば簡単です。でも、師匠は一人しかいません。どうやってその間に立つか。だから、反転が必要なんです。師匠にならなければなりません。</tgt>` | 3596 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1121 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 1108 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1397 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回答主管，</src><tgt><\|wait\|></tgt>` | 1604 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1559 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt><\|wait\|></tgt>` | 1725 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1876 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1791 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>不理成担，</src><tgt><\|wait\|></tgt>` | 706 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言</src><tgt><\|wait\|></tgt>` | 2356 |
| 11 | `<src>事业运就属凶。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall, your career prospects are quite poor.</tgt>` | `<src>是一句就是solution。</src><tgt>When facing this situation, we just need to quickly report it to our supervisor or let them know. We should not try to take everything on ourselves, ignore it, or feel responsible. Overall, it's a simple solution.</tgt>` | 3945 |

---

### Test Example 11 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 1003 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天気</src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>豊作が</src><tgt><\|wait\|></tgt>` | 885 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 1116 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1547 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1700 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | 1984 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2033 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>は五個、</src><tgt><\|wait\|></tgt>` | 2336 |
| 11 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠. 파생 형용사의 구조는</tgt>` | `<src>七日</src><tgt>그렇습니다. 그래서 풍년이 있었죠. 그리고 나가이 케이요 씨의 시스템은 다섯 개,</tgt>` | 2351 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>五日です。</src><tgt><\|wait\|></tgt>` | 886 |

---

### Test Example 12 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 1222 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 1499 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 웅심이 </src><tgt><\|wait\|></tgt>` | 1601 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어 혹시 </src><tgt><\|wait\|></tgt>` | 1583 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>웅심이가 </src><tgt><\|wait\|></tgt>` | 1715 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞이는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1972 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1907 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1641 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해당 으로도 </src><tgt><\|wait\|></tgt>` | 1608 |
| 11 | `<src>진짜. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover, for real.</tgt>` | `<src>조금 죽입니다, 저. </src><tgt>Ah, I'm a ' Bongsim ' type, a ' Kal Ungsim ' type. Uh, maybe it's a mix. Hey, I'm actually a bit of a ' ' guy, you know.</tgt>` | 4279 |

---

### Test Example 13 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1244 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后呢，</src><tgt><\|wait\|></tgt>` | 1161 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻了</src><tgt><\|wait\|></tgt>` | 1505 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也虽然</src><tgt><\|wait\|></tgt>` | 1502 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>弱了，</src><tgt><\|wait\|></tgt>` | 1793 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>然后就停留在</src><tgt><\|wait\|></tgt>` | 1503 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1977 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>一个相对的低能量的运行</src><tgt><\|wait\|></tgt>` | 2123 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态，</src><tgt><\|wait\|></tgt>` | 2501 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1745 |
| 11 | `<src>抑郁状态。</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。これが、いわゆる抑うつ状態です。</tgt>` | `<src>易于状态。</src><tgt>砂漠を掘り終えると、内部の圧力が軽減され、エネルギーも弱まります。そして、比較的低エネルギーの稼働状態に留まります。これがいわゆる「易于状態」です。</tgt>` | 3046 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1436 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 970 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1144 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 816 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1257 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1943 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1342 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 2010 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1951 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 2466 |
| 11 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们要使用这些值。也就是</tgt>` | `<src>So this </src><tgt>好的。那么，在这些例子之后，指令告诉我们，实际上要使用这些值。所以，</tgt>` | 2263 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>game dot sort array </src><tgt><\|wait\|></tgt>` | 1406 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1324 |

---

### Test Example 15 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果在女高中</src><tgt><\|wait\|></tgt>` | 1050 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 972 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>生与长相古怪的人之间，</src><tgt><\|wait\|></tgt>` | 1628 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1522 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>又这毛都没长的人，</src><tgt><\|wait\|></tgt>` | 2289 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1032 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1968 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里</src><tgt><\|wait\|></tgt>` | 1917 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 2039 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1120 |
| 11 | `<src>杨子思绪</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night? Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt>If it were between a girl and a strange- looking person, and that person was even bald, could it have started that night?</tgt>` | 3047 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇，</src><tgt><\|wait\|></tgt>` | 1312 |

---

### Test Example 16 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 913 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1119 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个轨道，</src><tgt><\|wait\|></tgt>` | 1531 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1522 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>好让我能够</src><tgt><\|wait\|></tgt>` | 1940 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>好在他下班的时候，</src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1879 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>的时候，在做热汤</src><tgt><\|wait\|></tgt>` | 2034 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的时候，我当时</src><tgt><\|wait\|></tgt>` | 2223 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被他这样子提醒一个</src><tgt><\|wait\|></tgt>` | 1160 |
| 11 | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가게 해줘. 퇴근하고 뜨거운 국 끓일 때, 그가 그렇게 작은 소망을</tgt>` | 2851 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 1266 |

---

### Test Example 17 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1417 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1001 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1512 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to dance, </src><tgt><\|wait\|></tgt>` | 1589 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>repeat, find what you're good at, </src><tgt><\|wait\|></tgt>` | 2475 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 975 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And when you're not good </src><tgt><\|wait\|></tgt>` | 1945 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>at it, </src><tgt><\|wait\|></tgt>` | 1877 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 2693 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2005 |
| 11 | `<src>And until next time. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。下次再见。</tgt>` | `<src>and and tell next time. </src><tgt>最后一点，就是重复。学会跳舞，重复练习，找到自己擅长的，多做一些。当你跳得不好时，请身边的人帮忙，并告诉他们下次。</tgt>` | 2885 |

---

### Test Example 18 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだん</src><tgt><\|wait\|></tgt>` | 1503 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が</src><tgt><\|wait\|></tgt>` | 1074 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じ</src><tgt><\|wait\|></tgt>` | 1474 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>をシャーラが言う方があって、</src><tgt><\|wait\|></tgt>` | 1707 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>これですね</src><tgt><\|wait\|></tgt>` | 1810 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>回避したい方って</src><tgt><\|wait\|></tgt>` | 1365 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ回避しきいたが</src><tgt><\|wait\|></tgt>` | 1959 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>C</src><tgt><\|wait\|></tgt>` | 1843 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>100点</src><tgt><\|wait\|></tgt>` | 863 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>全振りにおととし</src><tgt><\|wait\|></tgt>` | 2402 |
| 11 | `<src>傾向が強いので、</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且倾向于自己全部投资，</tgt>` | `<src>けどシャーが強いので</src><tgt>嗯，有的时候，像Shara会说距离会慢慢拉开，有些人会想回避，但很快就回避掉了。C100点全振り，但Shara很强，</tgt>` | 3678 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1048 |

---

### Test Example 19 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1105 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1403 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people. This is Tip </src><tgt><\|wait\|></tgt>` | 1648 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1596 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>of the stem research. Looking at </src><tgt><\|wait\|></tgt>` | 1685 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 2182 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2087 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 2483 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people like </src><tgt><\|wait\|></tgt>` | 2069 |
| 11 | `<src>people that we can learn from. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>非常に幸せな人たちに関する重要な研究をしました。これがステム研究のヒントです。最も幸せな人たちの10%を見てみると、そこから学ぶことができます。</tgt>` | 2957 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 1072 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 969 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1456 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1467 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1225 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1300 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1060 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt><\|wait\|></tgt>` | 2136 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>heat or light. </src><tgt><\|wait\|></tgt>` | 2084 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 2600 |
| 11 | `<src>or gets used to make </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다. 또는</tgt>` | `<src>to make </src><tgt>늘어난 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 그 잠재 에너지는 열이나 빛 같은 다른 에너지 형태로 변환됩니다. 아니면</tgt>` | 3762 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1195 |

---

### Test Example 21 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1158 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 </src><tgt><\|wait\|></tgt>` | 1025 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>주겨 달라 이거 주고 내가 </src><tgt><\|wait\|></tgt>` | 1523 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>주질 못하 도록 두루 와서도 </src><tgt><\|wait\|></tgt>` | 1751 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다니 지 않게 </src><tgt><\|wait\|></tgt>` | 2403 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>주겨 달라 </src><tgt><\|wait\|></tgt>` | 825 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았냐 내가 </src><tgt><\|wait\|></tgt>` | 2066 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>이런 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 2169 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 줄 알았느냐 </src><tgt><\|wait\|></tgt>` | 2693 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아 </src><tgt><\|wait\|></tgt>` | 1691 |
| 11 | `<src>내가 가. </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh? I'm going.</tgt>` | `<src>내가 </src><tgt>You asked for another type of medicine, and then you came and said you couldn't give it to me, so I wouldn't be able to give it to you. Didn't I say that? Did you think I didn't hear that?</tgt>` | 3232 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1149 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1143 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1456 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1501 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间大概有</src><tgt><\|wait\|></tgt>` | 1753 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>十位医生</src><tgt><\|wait\|></tgt>` | 401 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | 1846 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿、</src><tgt><\|wait\|></tgt>` | 2142 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 2574 |
| 11 | `<src>都没有问题。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>都没有问题，</src><tgt>I was doing great back then, so I insisted on not having surgery. During that time, about ten doctors came to diagnose me. The leg kicks and leg lifts were all fine,</tgt>` | 3473 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1282 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 635 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1139 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Finneghartelu. </src><tgt><\|wait\|></tgt>` | 1184 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1390 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in ITB </src><tgt><\|wait\|></tgt>` | 1555 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance </src><tgt><\|wait\|></tgt>` | 1800 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a brother in psychology. </src><tgt><\|wait\|></tgt>` | 1555 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2012 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at YY, </src><tgt><\|wait\|></tgt>` | 2059 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 2535 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 2027 |
| 11 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src><\|wait\|></src><tgt>제 이름은 Finneghartelu입니다. 저는 현재 ITB에서 비즈니스 재무를 공부하고 있고, 형은 심리학을 공부하고 있습니다. 여기 YY에서 앞으로는</tgt>` | 2914 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | 517 |

---

### Test Example 24 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 일었지 </src><tgt><\|wait\|></tgt>` | 1233 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>너무 이 저 </src><tgt><\|wait\|></tgt>` | 992 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>얘일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1509 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 고사 들도요 </src><tgt><\|wait\|></tgt>` | 1743 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt><\|wait\|></tgt>` | 2172 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>고사 들인데 꿈일 프로 그 </src><tgt><\|wait\|></tgt>` | 1102 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보이 고 </src><tgt><\|wait\|></tgt>` | 1909 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 그 고사 를 </src><tgt><\|wait\|></tgt>` | 2094 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 프로 그 보이 서 </src><tgt><\|wait\|></tgt>` | 2669 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>우주 가신다 한 뒤 고사 리는 </src><tgt><\|wait\|></tgt>` | 2347 |
| 11 | `<src>보살 이라는데. </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に菩薩だと言ってるんだから。</tgt>` | `<src><\|wait\|></src><tgt>これ、そうだったっけ。すごくこれかもしれないけど、本当に高説もあるんだよね。いや、自分の高説で夢かどうかもわからないし、自分だけがその高説を見せるから宇宙が死ぬんだって。で、その高説は</tgt>` | 3106 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1424 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>and, </src><tgt><\|wait\|></tgt>` | 1219 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1080 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 991 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2151 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change can </src><tgt><\|wait\|></tgt>` | 1096 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1896 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>happen in the United States, </src><tgt><\|wait\|></tgt>` | 2103 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2528 |
| 11 | `<src>The meanings </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>the meanings of </src><tgt>제19차 수정헌법의 의미와 역사를 살펴보고, 이것이 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 될 수 있음을</tgt>` | 3517 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>the amendment, of course, </src><tgt><\|wait\|></tgt>` | 1597 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Meirid, </src><tgt><\|wait\|></tgt>` | 1611 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1400 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 984 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアです。ギアが</src><tgt><\|wait\|></tgt>` | 1110 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | 682 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなって</src><tgt><\|wait\|></tgt>` | 1545 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>しまうので、</src><tgt><\|wait\|></tgt>` | 2172 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1071 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1910 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ヤクネ字のナットが</src><tgt><\|wait\|></tgt>` | 2353 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いている</src><tgt><\|wait\|></tgt>` | 2392 |
| 11 | `<src>ね。</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거죠.</tgt>` | `<src>っていうことですね。</src><tgt>이게 기어입니다. 기어가 헐거워지면 핀이 위아래로 움직이지 않게 되니까, 기어 끝에 쇠붙이 나사 같은 게 달려 있는 거죠.</tgt>` | 3818 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1261 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンが完了。</src><tgt><\|wait\|></tgt>` | 1665 |

---

### Test Example 27 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1057 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAアンデスにですね</src><tgt><\|wait\|></tgt>` | 1158 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1418 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>エネルギー節約効果</src><tgt><\|wait\|></tgt>` | 1576 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>みたいな時に</src><tgt><\|wait\|></tgt>` | 1497 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>AAのランキングを</src><tgt><\|wait\|></tgt>` | 1795 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べていることで、あの</src><tgt><\|wait\|></tgt>` | 2193 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>そのエネルギー節約効果っていうの</src><tgt><\|wait\|></tgt>` | 2128 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>を小さくする、節約で</src><tgt><\|wait\|></tgt>` | 2943 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt><\|wait\|></tgt>` | 1747 |
| 11 | `<src>といったような</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>といったような使い方を</src><tgt>So, we've been looking into AA rankings in various scenarios to see the energy saving effects. We're using that to guarantee that the energy saving effect is reduced— that is, that we can save energy.</tgt>` | 3080 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されます。</src><tgt><\|wait\|></tgt>` | 1431 |

---

### Test Example 28 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 976 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个甜头，</src><tgt><\|wait\|></tgt>` | 1100 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1408 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1654 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 2268 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1032 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1918 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着哎，那我再继续</src><tgt><\|wait\|></tgt>` | 2123 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2447 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>操作下去哦，</src><tgt><\|wait\|></tgt>` | 1809 |
| 11 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src><\|wait\|></src><tgt>好調なところに来たなら、まずは守りましょう。いや、もっと操作を続けよう、</tgt>` | 1833 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1561 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1075 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 784 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt><\|wait\|></tgt>` | 1175 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 인슐린과 </src><tgt><\|wait\|></tgt>` | 1442 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 유사 한 </src><tgt><\|wait\|></tgt>` | 1647 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>작용 이 </src><tgt><\|wait\|></tgt>` | 2151 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1098 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1957 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 2035 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 2534 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 2036 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium, they're so similar to insulin that they're basically called diabetes minerals. So, that's what I mean. Now,</tgt>` | 2726 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 685 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1527 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1290 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>呢，在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1544 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 1500 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>造成了所以呢，</src><tgt><\|wait\|></tgt>` | 2281 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1038 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1975 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt><\|wait\|></tgt>` | 1953 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风险</src><tgt><\|wait\|></tgt>` | 2469 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你事业之间就</src><tgt><\|wait\|></tgt>` | 1517 |
| 11 | `<src><\|wait\|></src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src><\|wait\|></src><tgt>皆さんにお伝えしたいのは、このローマの出来事が、今の皆さんが直面している危機やリスクが、</tgt>` | 2051 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 839 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因此会建议</src><tgt><\|wait\|></tgt>` | 1089 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | 1688 |

---

### Test Example 31 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 1116 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1124 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>涉及到二classList</src><tgt><\|wait\|></tgt>` | 1427 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1578 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>为服务在一级一线</src><tgt><\|wait\|></tgt>` | 2310 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | 1130 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 1892 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1973 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>在做维新攻防后期，你会</src><tgt><\|wait\|></tgt>` | 2618 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1752 |
| 11 | `<src>给微信公众号评分</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>发现给维新攻防平分的</src><tgt>二つ目は、二クラスが第一線で戦っている大牛たちです。例えば、維新攻防の終盤で、</tgt>` | 2343 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1183 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>新绑反而活了。</src><tgt><\|wait\|></tgt>` | 1743 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 980 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 1517 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | 1534 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1489 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1707 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>汤浅朋友们这样的一个状况</src><tgt><\|wait\|></tgt>` | 453 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>的受教要去特别</src><tgt><\|wait\|></tgt>` | 1902 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>注意的是</src><tgt><\|wait\|></tgt>` | 1837 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能够</src><tgt><\|wait\|></tgt>` | 2506 |
| 11 | `<src>钓到鱼，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>钓到鱼，</src><tgt>이 부분은 낚시를 하는 사람을 보여주는데, 이건 역방향적인 상황이에요. 그래서 탕첸 친구분들, 이런 상황에서 배울 때 특히 주의할 점은, 물고기를 잡을 수 있느냐는 거예요.</tgt>` | 3982 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>他钓不到鱼，</src><tgt><\|wait\|></tgt>` | 1338 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的意思是</src><tgt><\|wait\|></tgt>` | 1584 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>老。</src><tgt><\|wait\|></tgt>` | 1293 |

---

### Test Example 33 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1066 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HCL이라고 하는 </src><tgt><\|wait\|></tgt>` | 1492 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1558 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>컴피터도 이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1693 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1659 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1969 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1976 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2435 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 말할게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1706 |
| 11 | `<src>코드 를 작성 해야 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>조건 을 작성 해야 </src><tgt>嗯，HCL这种计算机语言，人也能理解，</tgt>` | 1537 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 821 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 조건 을 </src><tgt><\|wait\|></tgt>` | 1359 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1674 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1342 |

---

### Test Example 34 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you have </src><tgt><\|wait\|></tgt>` | 1231 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 966 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1494 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1648 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1762 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1537 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1966 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>how to spell the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 2355 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 2503 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1927 |
| 11 | `<src><\|wait\|></src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>spelled with a double p, </src><tgt>あるいは、何かを書きたいとき、文章を書こうとしたとき、スペルが全くわからないことに気づく。例えば、「この単語はpを二つ重ねてるのか、</tgt>` | 3120 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double lam? I don't know </src><tgt><\|wait\|></tgt>` | 1790 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>it. </src><tgt><\|wait\|></tgt>` | 1188 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1100 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there were such </src><tgt><\|wait\|></tgt>` | 1431 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>interposes before, </src><tgt><\|wait\|></tgt>` | 1606 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1646 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>netfilter, TC, </src><tgt><\|wait\|></tgt>` | 1654 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>etc. </src><tgt><\|wait\|></tgt>` | 1870 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>Yes, </src><tgt><\|wait\|></tgt>` | 1502 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>so this is just one </src><tgt><\|wait\|></tgt>` | 949 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>another place to look at. </src><tgt><\|wait\|></tgt>` | 2706 |
| 11 | `<src>But </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt>没什么新意，之前也有过这样的东西，比如netfilter、TC等等。是的，所以这只是看的地方而已。</tgt>` | 3019 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 725 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1097 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on Bug Repo </src><tgt><\|wait\|></tgt>` | 1618 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 1443 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>授業</src><tgt><\|wait\|></tgt>` | 1222 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一日二日とか</src><tgt><\|wait\|></tgt>` | 1168 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>でした。おそらく</src><tgt><\|wait\|></tgt>` | 1422 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 1557 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1494 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一日一に</src><tgt><\|wait\|></tgt>` | 1797 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1918 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>してたんですが、</src><tgt><\|wait\|></tgt>` | 1929 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ね、</src><tgt><\|wait\|></tgt>` | 732 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 2300 |
| 11 | `<src>おそらく</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。然后</tgt>` | `<src>おそらく</src><tgt>大概是一天一两天，大概十秒，嗯，一天一到一天一天的频率吧。然后，</tgt>` | 2821 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一日二日</src><tgt><\|wait\|></tgt>` | 887 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1239 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1593 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮内馬とかが</src><tgt><\|wait\|></tgt>` | 908 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 654 |

---

### Test Example 37 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150명계가 종업원 수를 </src><tgt><\|wait\|></tgt>` | 1164 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | 1453 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1636 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 2151 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1103 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 2113 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 에 </src><tgt><\|wait\|></tgt>` | 2095 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>익을 꺾여도 건데 </src><tgt><\|wait\|></tgt>` | 2926 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>일본 에 상업 이 없던은 </src><tgt><\|wait\|></tgt>` | 1941 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は成長も廃業も</tgt>` | `<src>성장 도 </src><tgt>その中で、150人規模の企業は従業員数が10人未満の非常に小さな企業が多くありました。一般的に、中小企業は成長したり、あるいは海外で成功を収めたりするんですが、日本で商売がなかったものは成長も</tgt>` | 3060 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>표 없다고 하지 않을 </src><tgt><\|wait\|></tgt>` | 1421 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들만 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1347 |

---

### Test Example 38 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1377 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어 어찌 보면 </src><tgt><\|wait\|></tgt>` | 990 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 또래 </src><tgt><\|wait\|></tgt>` | 1209 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>생명이자 그래도 </src><tgt><\|wait\|></tgt>` | 718 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>가족 같은 </src><tgt><\|wait\|></tgt>` | 1987 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아 </src><tgt><\|wait\|></tgt>` | 1204 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1851 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1890 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>챙긴 거라 는 </src><tgt><\|wait\|></tgt>` | 781 |
| 11 | `<src>조금 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>조건 </src><tgt>嗯，怎么说呢，也是和二十代一起长大的同龄人，也是像家人一样的弟弟，所以，嗯，因为是照顾他，</tgt>` | 4174 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1375 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1298 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 것을 </src><tgt><\|wait\|></tgt>` | 686 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | 1555 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 1450 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1155 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 1395 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1589 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1929 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1366 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1965 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 2117 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2494 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1757 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。ですから、あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちも知っているだろう。あなたたちが異邦人であった時、言葉を持たない偶像へと引きずられていった。だから、私があなたたちに</tgt>` | 2239 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1282 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1626 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 1334 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1053 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1333 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう蒸らせてあれ。</src><tgt><\|wait\|></tgt>` | 1058 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1451 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今ひきてる</src><tgt><\|wait\|></tgt>` | 1598 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>見てる。</src><tgt><\|wait\|></tgt>` | 1345 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1750 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 416 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>とうに超えてる</src><tgt><\|wait\|></tgt>` | 1928 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>ふ重きせ球。</src><tgt><\|wait\|></tgt>` | 2060 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2499 |
| 11 | `<src>長年</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>長年</src><tgt>그럼 그냥 쪄버려. 난 지금 찌는 거 보고 있어. 더 이상 한계는 이미 넘었어. 무거운 찌개야.</tgt>` | 3102 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなでいくを</src><tgt><\|wait\|></tgt>` | 1036 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってるんだ。</src><tgt><\|wait\|></tgt>` | 1132 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt><\|wait\|></tgt>` | 1750 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>海賊船を見た</src><tgt><\|wait\|></tgt>` | 1301 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 944 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1180 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1089 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不多的，但是</src><tgt><\|wait\|></tgt>` | 1436 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1532 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>比较精神正财的部分</src><tgt><\|wait\|></tgt>` | 1672 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>尤其是在事业方面</src><tgt><\|wait\|></tgt>` | 1651 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长的动力</src><tgt><\|wait\|></tgt>` | 1990 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>以及收入的提升</src><tgt><\|wait\|></tgt>` | 2001 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 2003 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果设投资理财方面</src><tgt><\|wait\|></tgt>` | 1281 |
| 11 | `<src>这个月</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>这个月</src><tgt>金運については、今月はそれほど多くないと言えます。ただ、精神的な正財の部分、特に仕事の業績向上や収入アップの動機については、投資や資産運用に関しては今月</tgt>` | 3513 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错的，</src><tgt><\|wait\|></tgt>` | 1145 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对正财来说，</src><tgt><\|wait\|></tgt>` | 1739 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了一点</src><tgt><\|wait\|></tgt>` | 1419 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>。</src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 42 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1324 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1136 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get. </src><tgt><\|wait\|></tgt>` | 1444 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1566 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>And I have ten of them </src><tgt><\|wait\|></tgt>` | 2473 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that I think are </src><tgt><\|wait\|></tgt>` | 962 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>really important. </src><tgt><\|wait\|></tgt>` | 1850 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1991 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | 2681 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1991 |
| 11 | `<src>one minute videos </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I have about one minute videos </src><tgt>これから始める人には、これが必要だと思っています。10個くらいあるんですが、特に大事だと思うものがあります。1分程度の動画を</tgt>` | 2550 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | 760 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1659 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1288 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>You know, in a little more detail. </src><tgt><\|wait\|></tgt>` | 1052 |

---

### Test Example 43 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1324 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 1076 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1605 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1546 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 2093 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨텐츠예요. </src><tgt><\|wait\|></tgt>` | 1243 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 컨텐츠예요 </src><tgt><\|wait\|></tgt>` | 1913 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 있고, A라는 </src><tgt><\|wait\|></tgt>` | 1945 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 1899 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1393 |
| 11 | `<src>뿌렸 을 때 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、</tgt>` | `<src>줬을 때 </src><tgt>ですから、もちろんこういうケースもあります。AさんとBさんがコンテンツを共有しているとします。Aさんが悪意のあるコードを</tgt>` | 2858 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1319 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스사이트 </src><tgt><\|wait\|></tgt>` | 738 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크리 에러 에서 </src><tgt><\|wait\|></tgt>` | 1522 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>계시 파일까지 </src><tgt><\|wait\|></tgt>` | 1266 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 999 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1453 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해맵니다. </src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전을 </src><tgt><\|wait\|></tgt>` | 1219 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하려고 은 </src><tgt><\|wait\|></tgt>` | 811 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1265 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있건 뭐 </src><tgt><\|wait\|></tgt>` | 1968 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1214 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1912 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 </src><tgt><\|wait\|></tgt>` | 2378 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장려 리예요. </src><tgt><\|wait\|></tgt>` | 2560 |
| 11 | `<src>좀 창피 하네요. </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国就更惨了。真有点丢人。</tgt>` | `<src>좀 책임 이 아니 에요. </src><tgt>进去的时候非常危险。想开车的话，只能走走停停，去江北区的话更是难说，出国的话又是一场挑战。责任也不小。</tgt>` | 3501 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1395 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1621 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모바일 을 그거 는 </src><tgt><\|wait\|></tgt>` | 1336 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>다인 것 같아요. </src><tgt><\|wait\|></tgt>` | 840 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 425 |

---

### Test Example 45 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 1150 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt><\|wait\|></tgt>` | 1064 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1548 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1616 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1992 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1233 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 </src><tgt><\|wait\|></tgt>` | 1825 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 가벼운 </src><tgt><\|wait\|></tgt>` | 1976 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1630 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1604 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>주도 하면서 </src><tgt>If the stock market index is rising, these large- cap stocks will likely see a sharp rise. But first, the lighter stocks will lead the market,</tgt>` | 3101 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1578 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1659 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1350 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1033 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | 889 |

---

### Test Example 46 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1271 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉对手的</src><tgt><\|wait\|></tgt>` | 1168 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>感情或</src><tgt><\|wait\|></tgt>` | 1391 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | 1601 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1573 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1693 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>好经常会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 699 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1940 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 2404 |
| 11 | `<src>这个人</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが「ほら、</tgt>` | `<src>这个人又在</src><tgt>相手の感情や本当の意図を察したり感じ取ったりすること。よく聞く言葉の一つに「見て、この人は</tgt>` | 3062 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>说谎了，</src><tgt><\|wait\|></tgt>` | 1017 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1101 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1617 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1334 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 1036 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 1003 |

---

### Test Example 47 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1295 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment: </src><tgt><\|wait\|></tgt>` | 1030 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1516 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1600 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? Did you </src><tgt><\|wait\|></tgt>` | 2462 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 982 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt><\|wait\|></tgt>` | 2087 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>of attainment. Did you </src><tgt><\|wait\|></tgt>` | 2115 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>go to college? </src><tgt><\|wait\|></tgt>` | 2612 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, did you graduate? </src><tgt><\|wait\|></tgt>` | 2136 |
| 11 | `<src>That's another level of </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>That's another level </src><tgt>학력 수준: 교육은 어느 정도까지 마치셨나요? 고등학교 졸업하셨나요? 그건 한 단계의 학력 수준입니다. 대학에 가셨나요? 그렇다면 졸업하셨나요? 그건 또 다른 단계의</tgt>` | 3068 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>of attainment. </src><tgt><\|wait\|></tgt>` | 1458 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1275 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt><\|wait\|></tgt>` | 1058 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 966 |

---

### Test Example 48 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 간고 </src><tgt><\|wait\|></tgt>` | 1498 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새 못 알아 </src><tgt><\|wait\|></tgt>` | 1086 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1436 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 </src><tgt><\|wait\|></tgt>` | 1590 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋든 차리 돋든 </src><tgt><\|wait\|></tgt>` | 2148 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>내 기명응이야. </src><tgt><\|wait\|></tgt>` | 1240 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 2139 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 2126 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 2440 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>너무 밀릴 거고 </src><tgt><\|wait\|></tgt>` | 2001 |
| 11 | `<src>신이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら</tgt>` | `<src>신이 너무 밀리 면 </src><tgt>目隠しして、新しいものを植えるんだ。昔の根が伸びるんだ、根が伸びるんだ。俺の気性なんだ。これを揺らして一緒に遊ぼうってことだよ。気性が押しつぶされて、気性が押しつぶされるなら、</tgt>` | 3588 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1307 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주라고 그러니까 </src><tgt><\|wait\|></tgt>` | 1343 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 987 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 간다. </src><tgt><\|wait\|></tgt>` | 933 |

---

### Test Example 49 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1255 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, </src><tgt><\|wait\|></tgt>` | 1019 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to move </src><tgt><\|wait\|></tgt>` | 1543 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>me directly. </src><tgt><\|wait\|></tgt>` | 1542 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I'm an </src><tgt><\|wait\|></tgt>` | 1676 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>resources, </src><tgt><\|wait\|></tgt>` | 1611 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>so if </src><tgt><\|wait\|></tgt>` | 1764 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into a </src><tgt><\|wait\|></tgt>` | 510 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation where you </src><tgt><\|wait\|></tgt>` | 1882 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 2536 |
| 11 | `<src>you've added the wrong media </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src><\|wait\|></src><tgt>另外，你无法直接移动我。我是资源，所以如果你遇到这种情况，意识到自己添加了</tgt>` | 2598 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>the wrong media files </src><tgt><\|wait\|></tgt>` | 1053 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>to a particular resource, </src><tgt><\|wait\|></tgt>` | 1498 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1675 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1295 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure </src><tgt><\|wait\|></tgt>` | 1029 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 872 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>they get backed up properly. </src><tgt><\|wait\|></tgt>` | 588 |

---

### Test Example 50 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1285 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 1500 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1598 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 2301 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローグラフは</src><tgt><\|wait\|></tgt>` | 1108 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 2058 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それ自体はPythonコード</src><tgt><\|wait\|></tgt>` | 2169 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>なんそこから</src><tgt><\|wait\|></tgt>` | 2443 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | 1941 |
| 11 | `<src>実行されることで</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>実行されることで</src><tgt>So this is not just a visual development environment, but a Visual Python development environment. The reason is that after you write a flow graph visually, it generates Python code from that, and that code is then executed,</tgt>` | 3102 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるっていう</src><tgt><\|wait\|></tgt>` | 1671 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 1322 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はいじゃあ</src><tgt><\|wait\|></tgt>` | 728 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1002 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>Furor一的首知觉</src><tgt><\|wait\|></tgt>` | 1119 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>觉知到了那个现象，</src><tgt><\|wait\|></tgt>` | 1512 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1513 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>美当我们处于</src><tgt><\|wait\|></tgt>` | 1762 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>爱之中所位的爱，</src><tgt><\|wait\|></tgt>` | 1971 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1901 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>我们也同时进入</src><tgt><\|wait\|></tgt>` | 1737 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1438 |
| 11 | `<src>在早上的时候，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는</tgt>` | `<src>恨在长上的时候，</src><tgt>Furor의 첫 번째 지각이 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때, 동시에 증오가 길을 걷기 시작합니다.</tgt>` | 3364 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>他是在</src><tgt><\|wait\|></tgt>` | 1373 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1632 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>他就变成了</src><tgt><\|wait\|></tgt>` | 896 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 739 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>恨那个中百，</src><tgt><\|wait\|></tgt>` | 956 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 922 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | 717 |

---

### Test Example 52 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1237 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 990 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1565 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1572 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 2122 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>but the reality is is that </src><tgt><\|wait\|></tgt>` | 1939 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 2356 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt><\|wait\|></tgt>` | 2541 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1926 |
| 11 | `<src>changed from 20 </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>standards have changed from </src><tgt>活動、そして自分たちで基準を定義すること。なぜなら、あなたが完全に正しいからです。でも、現実は、私たちが新しい世代だからです。そして基準が</tgt>` | 3008 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt><\|wait\|></tgt>` | 1680 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1354 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard </src><tgt><\|wait\|></tgt>` | 1062 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point is </src><tgt><\|wait\|></tgt>` | 1043 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>being held to a higher standard </src><tgt><\|wait\|></tgt>` | 736 |

---

### Test Example 53 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 973 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1070 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놨습니다. </src><tgt><\|wait\|></tgt>` | 1542 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠 자의 </src><tgt><\|wait\|></tgt>` | 1625 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 2305 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>손이 </src><tgt><\|wait\|></tgt>` | 924 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 칩에 </src><tgt><\|wait\|></tgt>` | 2134 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FP 파이프 를 </src><tgt><\|wait\|></tgt>` | 2085 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 2566 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나중 하게 로 파인다. </src><tgt><\|wait\|></tgt>` | 2135 |
| 11 | `<src><\|wait\|></src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>엑스 박스 </src><tgt>そして、これについて多くの人が分析しています。このロクジャの分析を見ると、ソニーのイオレットチップはFPパイプを128ビットで最終的に採用しています。Xboxは</tgt>` | 2950 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>시리즈 x에서도 없는 </src><tgt><\|wait\|></tgt>` | 1684 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1404 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>CS. </src><tgt><\|wait\|></tgt>` | 987 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>S2가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 973 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 672 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1570 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 911 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>on the first section </src><tgt><\|wait\|></tgt>` | 1263 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 937 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the HR field </src><tgt><\|wait\|></tgt>` | 1110 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1991 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1211 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1835 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1910 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 754 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously the one of my loves. </src><tgt>HR分野の最初のセクションで、変異データベースが非常に重要であることと、私の大好きなもの、明らかに</tgt>` | 4162 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if you </src><tgt><\|wait\|></tgt>` | 1438 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>don't agree upon </src><tgt><\|wait\|></tgt>` | 1327 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields </src><tgt><\|wait\|></tgt>` | 622 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1596 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 1239 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 1078 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 967 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 703 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1505 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 963 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1194 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1006 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1009 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | 1916 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1803 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1918 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1158 |
| 11 | `<src>these days, </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>有意义的个人权利，最高法院是最后才出现的，而不是引领者。我不认为法院想成为社会变革的前沿。如今，</tgt>` | 3703 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1161 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | 969 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1065 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1565 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | 1353 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 1009 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>you have some </src><tgt><\|wait\|></tgt>` | 888 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges </src><tgt><\|wait\|></tgt>` | 353 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 589 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 453 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1024 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1477 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that he's </src><tgt><\|wait\|></tgt>` | 1631 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>about the food </src><tgt><\|wait\|></tgt>` | 1551 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in the wilderness, </src><tgt><\|wait\|></tgt>` | 1725 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>so thirsty, and is hungry. </src><tgt><\|wait\|></tgt>` | 1957 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>And so he says to </src><tgt><\|wait\|></tgt>` | 2033 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus," Hey, if you have </src><tgt><\|wait\|></tgt>` | 2501 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>the Son of God, prove it." </src><tgt><\|wait\|></tgt>` | 1845 |
| 11 | `<src><\|wait\|></src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src><\|wait\|></src><tgt>ある時、彼はイエスが飢えていることを知っていました。彼は、荒野の食べ物について知っていました。喉が渇いていて、お腹も空いていることを知っていました。だからイエスに言いました。「おい、もし神の御子なら、証明してみろよ」</tgt>` | 3589 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | 1719 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1299 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>say this </src><tgt><\|wait\|></tgt>` | 973 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>deal with that temptation? </src><tgt><\|wait\|></tgt>` | 1025 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 706 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan led by </src><tgt><\|wait\|></tgt>` | 511 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>great alone. </src><tgt><\|wait\|></tgt>` | 446 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1209 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片</src><tgt><\|wait\|></tgt>` | 1026 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>哦，图片</src><tgt><\|wait\|></tgt>` | 1434 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>的右边呢，</src><tgt><\|wait\|></tgt>` | 1643 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1499 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>一个是客厅的部分，</src><tgt><\|wait\|></tgt>` | 1780 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1691 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 590 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1804 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | 2514 |
| 11 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>所以呢，</src><tgt>그럼 사진을 한번 볼까요? 사진 오른쪽에는 거실 부분이 보이네요. 거실은 보통 우리가 쉬는 공간이라서,</tgt>` | 2699 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分</src><tgt><\|wait\|></tgt>` | 1013 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>会反映的是</src><tgt><\|wait\|></tgt>` | 1468 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 832 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 1056 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 1392 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt><\|wait\|></tgt>` | 1026 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们可以看到这边是</src><tgt><\|wait\|></tgt>` | 940 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的嘛。</src><tgt><\|wait\|></tgt>` | 706 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 438 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以意思是说。</src><tgt>이곳은 몸의 부분이에요. 그러니까 자신에게 시간을 주고 편안하게 앉아 쉬어야 한다는 뜻이죠. 여기는 아무도 없는 걸 볼 수 있어요. 아, 그러니까 말하는 건...</tgt>` | 868 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 964 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1225 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>and they often show up </src><tgt><\|wait\|></tgt>` | 1194 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 767 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>to completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | 2243 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1045 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>The personality is </src><tgt><\|wait\|></tgt>` | 2029 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 2056 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2580 |
| 11 | `<src>While they're </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>While they're </src><tgt>彼らは非常に稀で、世界を完全に変革することがよくあります。その性格は矛盾をはらんでいます。彼らは</tgt>` | 3031 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | 1051 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1135 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations, </src><tgt><\|wait\|></tgt>` | 1593 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1281 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to the </src><tgt><\|wait\|></tgt>` | 1063 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 1013 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love to </src><tgt><\|wait\|></tgt>` | 735 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 487 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 536 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and they never shy away </src><tgt><\|wait\|></tgt>` | 371 |
| 22 | `<src>never shy away from a debate. </src><tgt>外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>外向的ですが、無意味な会話は嫌い、要点を突くのが好きです。彼らは悪魔の代弁を好みますし、議論を避けることはありません。</tgt>` | 740 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 289 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T. P. </src><tgt><\|wait\|></tgt>` | 421 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for </src><tgt><\|wait\|></tgt>` | 374 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>강물 을 거부 한 </src><tgt><\|wait\|></tgt>` | 1073 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보를 </src><tgt><\|wait\|></tgt>` | 1511 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1541 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당슬을 </src><tgt><\|wait\|></tgt>` | 2250 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1077 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 2128 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 2118 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2521 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 2015 |
| 11 | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok had the excuse of rejecting the main candidate and was even quite boastful about the main candidate. But now, the moment Yoon Suk- yeol removed Kim Jong- in</tgt>` | 3071 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해 놓고 </src><tgt><\|wait\|></tgt>` | 1723 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1370 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 1000 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 909 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 734 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 471 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 462 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 367 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 327 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 청상답군 </src><tgt>has been determined to attack Yoon Suk- yeol and knock him down. He was determined to attack Yoon Suk- yeol, harboring the venom to knock him down. Lee Jun- seok's arrogant and arrogant demeanor</tgt>` | 916 |
| 22 | `<src><\|wait\|></src><tgt>Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 268 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 361 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 </src><tgt><\|wait\|></tgt>` | 306 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 403 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1294 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | 985 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってるみたいです。なるほど。</src><tgt><\|wait\|></tgt>` | 1231 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>でここのね</src><tgt><\|wait\|></tgt>` | 990 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>プロフェッショナルホテル</src><tgt><\|wait\|></tgt>` | 1129 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も朝食が</src><tgt><\|wait\|></tgt>` | 2285 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 932 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1956 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっているので</src><tgt><\|wait\|></tgt>` | 1927 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | 2186 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>ゴルドストンホテル</src><tgt>Well, it looks like they're making it up now at the diner. I see. And it's supposed to be a place where you can have breakfast at the Professional Hotel too. So, in the future,</tgt>` | 3530 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 932 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | 1278 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1731 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 1405 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt><\|wait\|></tgt>` | 914 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。ここ</src><tgt><\|wait\|></tgt>` | 969 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>のホテルからですね</src><tgt><\|wait\|></tgt>` | 727 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 485 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 469 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt>if you're thinking about staying at the Goldston Hotel, I think it might be a good option. Yes. From this hotel, you can walk to Busan Station</tgt>` | 700 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel, it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかからないか</src><tgt><\|wait\|></tgt>` | 400 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルでのね律の</src><tgt><\|wait\|></tgt>` | 333 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>いいねまあホテル</src><tgt><\|wait\|></tgt>` | 405 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt><\|wait\|></tgt>` | 391 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>良かっ たらですね</src><tgt><\|wait\|></tgt>` | 326 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 382 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 218 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね今回は。</src><tgt><\|wait\|></tgt>` | 223 |
