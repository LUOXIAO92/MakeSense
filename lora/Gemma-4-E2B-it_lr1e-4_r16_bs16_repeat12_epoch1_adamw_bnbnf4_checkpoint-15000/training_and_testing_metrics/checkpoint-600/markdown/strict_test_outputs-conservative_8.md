# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9526
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.1987
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.1449
  - TGT_RELEASE_TOTAL: 69
  - TGT_WAIT_ACCURACY: 0.9237
  - TGT_WAIT_TOTAL: 799
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1356.4150
  - PROCESS_TIME_MS_P50: 1267.7240
  - PROCESS_TIME_MS_P95: 2320.2640
  - PROCESS_TIME_MS_MAX: 9926.1010

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1173 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>的总结点，</src><tgt><\|wait\|></tgt>` | 770 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个收益也很大，</src><tgt><\|wait\|></tgt>` | 1192 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1166 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，我在</src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 958 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人</src><tgt><\|wait\|></tgt>` | 1635 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>Why is the summary point for this so good? The returns are also very high. Then, I took a break and</tgt>` | 2381 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels—</tgt>` | `<src>一起去</src><tgt><\|wait\|></tgt>` | 944 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1155 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和陶人。</src><tgt><\|wait\|></tgt>` | 2043 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 844 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 993 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲まだ</src><tgt><\|wait\|></tgt>` | 1141 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>1年生ですからね。</src><tgt><\|wait\|></tgt>` | 1263 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>はいはいはい、その時点で</src><tgt><\|wait\|></tgt>` | 1459 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1430 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>美学、</src><tgt><\|wait\|></tgt>` | 1633 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>対数していって</src><tgt>从一开始，因为我们还是大一新生，所以当时</tgt>` | 2091 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，</tgt>` | `<src>上げる</src><tgt><\|wait\|></tgt>` | 536 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>と10年経っても</src><tgt><\|wait\|></tgt>` | 1969 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>対数だ。</src><tgt><\|wait\|></tgt>` | 1163 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 1018 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1152 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生那爱胶水</src><tgt><\|wait\|></tgt>` | 1320 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>十分，</src><tgt><\|wait\|></tgt>` | 1484 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>可以做孩子</src><tgt><\|wait\|></tgt>` | 1640 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心灵养养。</src><tgt>Parents need to use our love glue to nurture their children's spirits.</tgt>` | 2187 |
| 9 | `<src><\|wait\|></src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 554 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>心内静，</src><tgt><\|wait\|></tgt>` | 1963 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>让孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 1071 |

---

### Test Example 4 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 1018 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>영심이 </src><tgt><\|wait\|></tgt>` | 1122 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 </src><tgt><\|wait\|></tgt>` | 1207 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>영심이 가 </src><tgt><\|wait\|></tgt>` | 1427 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1421 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>석현 하는 건데요. </src><tgt><\|wait\|></tgt>` | 1716 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1521 |
| 9 | `<src>진짜 이거 </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>야 진짜 이거 </src><tgt>I'm a sword-wielding spirit, you know. Seriously,</tgt>` | 1204 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행동 으로도 </src><tgt><\|wait\|></tgt>` | 2081 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽입니다. </src><tgt><\|wait\|></tgt>` | 977 |

---

### Test Example 5 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 750 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>lastly, he repeats </src><tgt><\|wait\|></tgt>` | 1196 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>learning to repeat </src><tgt><\|wait\|></tgt>` | 1163 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>by learning to repeat </src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>by good app </src><tgt><\|wait\|></tgt>` | 1075 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and do more of it, and well, you're not </src><tgt><\|wait\|></tgt>` | 2218 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good at it. </src><tgt><\|wait\|></tgt>` | 1380 |
| 9 | `<src>get the people around you to help you with. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src>People around you </src><tgt>最后，他重复学习，通过好应用多做一些，而且你不会太擅长。你身边的人</tgt>` | 1476 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>need to help you with it, </src><tgt><\|wait\|></tgt>` | 2206 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and in the next time, </src><tgt><\|wait\|></tgt>` | 977 |

---

### Test Example 6 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 953 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1175 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떤 척박 시키고 </src><tgt><\|wait\|></tgt>` | 1498 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 880 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 1312 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로지기인 </src><tgt><\|wait\|></tgt>` | 1986 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1279 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I am making it barren, and I am the one who makes my own people</tgt>` | 2119 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1053 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 같은 </src><tgt><\|wait\|></tgt>` | 2039 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>세대들입니다. </src><tgt><\|wait\|></tgt>` | 1208 |

---

### Test Example 7 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1212 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 981 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただきたいようなものも</src><tgt><\|wait\|></tgt>` | 1250 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1166 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参考ください。</src><tgt><\|wait\|></tgt>` | 1078 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1268 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt>We also have items like T-shirts available, so please refer to them. As for contact, that's all.</tgt>` | 2474 |
| 9 | `<src>えっと</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements,</tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 961 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>例えば</src><tgt><\|wait\|></tgt>` | 1041 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>皆さん</src><tgt><\|wait\|></tgt>` | 2014 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>の案内がありますので、</src><tgt><\|wait\|></tgt>` | 1422 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1292 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들은 </src><tgt><\|wait\|></tgt>` | 1208 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 969 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1318 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1327 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1975 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들이었기 때문 </src><tgt><\|wait\|></tgt>` | 1370 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt>The nicknames on the list were actually not highly intelligent; they were just randomly selected.</tgt>` | 2075 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 2164 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1485 |

---

### Test Example 9 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后，</src><tgt><\|wait\|></tgt>` | 1203 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 1073 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>的液体检清</src><tgt><\|wait\|></tgt>` | 1101 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 1160 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷了，然后就</src><tgt><\|wait\|></tgt>` | 1442 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1514 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1610 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态</src><tgt>淘撒が終わると、内部の液体検清エネルギーも刷って、相対的に低エネルギーな動作状態に留まります。</tgt>` | 2453 |
| 9 | `<src>状态，</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。</tgt>` | `<src>态。</src><tgt><\|wait\|></tgt>` | 1280 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1786 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>的低语状态。</src><tgt><\|wait\|></tgt>` | 1455 |

---

### Test Example 10 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 1079 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的，</src><tgt><\|wait\|></tgt>` | 1264 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 958 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1219 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师父之道</src><tgt><\|wait\|></tgt>` | 1430 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如初于</src><tgt><\|wait\|></tgt>` | 1640 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>中坚。</src><tgt><\|wait\|></tgt>` | 1473 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以，</src><tgt>気数をつけるのは簡単ですが、師父の道は初めから中堅です。だから、</tgt>` | 2368 |
| 9 | `<src>虚阿凡</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>师者凡</src><tgt><\|wait\|></tgt>` | 1307 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1830 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师父，</src><tgt><\|wait\|></tgt>` | 1509 |

---

### Test Example 11 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 749 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 981 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 997 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>鬼岛，</src><tgt><\|wait\|></tgt>` | 1144 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够保持</src><tgt><\|wait\|></tgt>` | 1338 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>它安全的时候，</src><tgt><\|wait\|></tgt>` | 1207 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在座日</src><tgt><\|wait\|></tgt>` | 1377 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>康乐园，</src><tgt>저를 귀섬으로 데려가서 안전하게 지낼 수 있도록 해 주세요. 그곳에서</tgt>` | 2365 |
| 9 | `<src><\|wait\|></src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>我暂时</src><tgt><\|wait\|></tgt>` | 965 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被痛痛的</src><tgt><\|wait\|></tgt>` | 1192 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的愿望，</src><tgt><\|wait\|></tgt>` | 2072 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt><\|wait\|></tgt>` | 1606 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1080 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1109 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので</src><tgt><\|wait\|></tgt>` | 1117 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1246 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご方法</src><tgt><\|wait\|></tgt>` | 1398 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1407 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ご言やん</src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt>大概是从这里开始的，</tgt>` | 1819 |
| 9 | `<src>ルナールなど</src><tgt>大致是从这一带开始的，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 694 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ルナールなどという人の</src><tgt><\|wait\|></tgt>` | 1394 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1721 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>絵は田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1859 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1178 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 988 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1094 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 1052 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱりですね、</src><tgt><\|wait\|></tgt>` | 1332 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>囲いしたい方って</src><tgt><\|wait\|></tgt>` | 1336 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ囲いこ行きたい</src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>のが</src><tgt>好像是，阿多万好像有点离得远了，大将还是想围住对方，想马上围住对方。</tgt>` | 2147 |
| 9 | `<src>自分で</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且</tgt>` | `<src>いいですね</src><tgt><\|wait\|></tgt>` | 863 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>とともにおととしゃぐ</src><tgt><\|wait\|></tgt>` | 1448 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>囲うのが強いので、</src><tgt><\|wait\|></tgt>` | 1903 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1900 |

---

### Test Example 14 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 920 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>body saying? </src><tgt><\|wait\|></tgt>` | 1066 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1287 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1056 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>attention start? </src><tgt><\|wait\|></tgt>` | 1356 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>What is it? Is it </src><tgt><\|wait\|></tgt>` | 1888 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>a day? </src><tgt><\|wait\|></tgt>` | 1291 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it in your chest? </src><tgt>你的身体在说什么？把针头放在身体上。注意力从哪里开始？是什么？是在一天之内吗？是在胸口吗？</tgt>` | 2621 |
| 9 | `<src>I ask them what </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I have a </src><tgt><\|wait\|></tgt>` | 2072 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>large lymphatic jar, </src><tgt><\|wait\|></tgt>` | 959 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>which are you using? </src><tgt><\|wait\|></tgt>` | 1873 |

---

### Test Example 15 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 945 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 1028 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely happy </src><tgt><\|wait\|></tgt>` | 1130 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>people. This is </src><tgt><\|wait\|></tgt>` | 1272 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1420 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. </src><tgt><\|wait\|></tgt>` | 1887 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at </src><tgt><\|wait\|></tgt>` | 1272 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10% of the happiest </src><tgt>非常に幸せな人々の研究に、様々な重要な研究が行われています。これは研究の入り口です。最も幸せな人々の10%を見ます。</tgt>` | 2712 |
| 9 | `<src>of the happiest people </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people out </src><tgt><\|wait\|></tgt>` | 2108 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. </src><tgt><\|wait\|></tgt>` | 860 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>People that we can learn from. </src><tgt><\|wait\|></tgt>` | 2133 |

---

### Test Example 16 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 너무 </src><tgt><\|wait\|></tgt>` | 1176 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1028 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>좋아요 에일스 있지만 </src><tgt><\|wait\|></tgt>` | 1201 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살도요. </src><tgt><\|wait\|></tgt>` | 1593 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기가 </src><tgt><\|wait\|></tgt>` | 964 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 피로 </src><tgt><\|wait\|></tgt>` | 2497 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보이 고 나만 </src><tgt><\|wait\|></tgt>` | 1054 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 </src><tgt>これはいいですね。でも、本当に菩薩です。いや、菩薩が夢を見ているみたいに見えるんです。私だけが菩薩に見える</tgt>` | 2273 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보일 피로 보이 세 우주 가 </src><tgt><\|wait\|></tgt>` | 2512 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>지단 한데 </src><tgt><\|wait\|></tgt>` | 693 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이란 </src><tgt><\|wait\|></tgt>` | 2238 |

---

### Test Example 17 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1257 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 1041 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 1124 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1368 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1331 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1524 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 957 |
| 9 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们</tgt>` | `<src><\|wait\|></src><tgt>好了，在这些例子之后，指令告诉我们实际上</tgt>` | 1633 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 688 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2356 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>So this game.board array </src><tgt><\|wait\|></tgt>` | 939 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2045 |

---

### Test Example 18 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为这个情况</src><tgt><\|wait\|></tgt>` | 1026 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 989 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1125 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就更改了回报主管</src><tgt><\|wait\|></tgt>` | 1381 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1329 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt><\|wait\|></tgt>` | 2084 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1183 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>怎么都把它扛下来，</src><tgt>Because of this situation, we just changed the reporting manager or notified the other party. We just laugh at the situation. Don't think you have to bear it all.</tgt>` | 2750 |
| 9 | `<src>独立承担。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>工具理性</src><tgt><\|wait\|></tgt>` | 2434 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>承当责任，</src><tgt><\|wait\|></tgt>` | 1188 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>责任是给属人。</src><tgt><\|wait\|></tgt>` | 1901 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 820 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1118 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间，</src><tgt><\|wait\|></tgt>` | 1321 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>又</src><tgt><\|wait\|></tgt>` | 1066 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>有这么重要性。</src><tgt><\|wait\|></tgt>` | 1417 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道</src><tgt><\|wait\|></tgt>` | 1538 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>会是</src><tgt><\|wait\|></tgt>` | 1532 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里</src><tgt>If a female high school student is with someone who doesn't look bad, that's also very important. Could it be that from that night on,</tgt>` | 2539 |
| 9 | `<src><\|wait\|></src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night?</tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1420 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1691 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1441 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>系列篇。</src><tgt><\|wait\|></tgt>` | 1423 |

---

### Test Example 20 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 949 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt><\|wait\|></tgt>` | 1110 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1318 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 길리 고 들어왔어. </src><tgt><\|wait\|></tgt>` | 1793 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 쯤에 </src><tgt><\|wait\|></tgt>` | 848 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 해자나 </src><tgt><\|wait\|></tgt>` | 2292 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>안 되냐? 내가 </src><tgt><\|wait\|></tgt>` | 1024 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt>They asked me to kill someone in the advanced sector, so I came in to do it. They were asking for someone to be killed at a party or something. I didn't want to hear that kind of talk.</tgt>` | 3070 |
| 9 | `<src><\|wait\|></src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room?</tgt>` | `<src>중요한 거야. </src><tgt><\|wait\|></tgt>` | 2134 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 1637 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1338 |

---

### Test Example 21 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 1104 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunah Teru, </src><tgt><\|wait\|></tgt>` | 1364 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 901 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in AI, </src><tgt><\|wait\|></tgt>` | 1190 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>back-end finance, </src><tgt><\|wait\|></tgt>` | 1356 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bit of psychology. </src><tgt><\|wait\|></tgt>` | 2050 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 1080 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>you're in </src><tgt>제 이름은 치나 테루입니다. 현재 AI, 백엔드 금융, 그리고 심리학을 공부하고 있어요. 들으신 분들은</tgt>` | 2619 |
| 9 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1970 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>the future, I want to go into </src><tgt><\|wait\|></tgt>` | 1091 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1562 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1397 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>so here, </src><tgt><\|wait\|></tgt>` | 1035 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>you have to </src><tgt><\|wait\|></tgt>` | 1140 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>do 7.2 GB </src><tgt><\|wait\|></tgt>` | 1364 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>already, right? </src><tgt><\|wait\|></tgt>` | 1350 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1623 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1486 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>the heavy use of </src><tgt><\|wait\|></tgt>` | 1734 |
| 9 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>the system </src><tgt>자, 여기 7.2GB는 이미 사용하고 계시죠? 그리고 시스템의</tgt>` | 1167 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>hooking </src><tgt><\|wait\|></tgt>` | 2353 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to 7.2 GB </src><tgt><\|wait\|></tgt>` | 792 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>GB </src><tgt><\|wait\|></tgt>` | 2079 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>is </src><tgt><\|wait\|></tgt>` | 1094 |

---

### Test Example 23 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1235 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1455 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 771 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore </src><tgt><\|wait\|></tgt>` | 1176 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>its history as a guide </src><tgt><\|wait\|></tgt>` | 1467 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help </src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt><\|wait\|></tgt>` | 1536 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>19세기 수정헌법의 의미를 살펴보고, 그것이 정치적 변화에 어떻게 도움이 될 수 있는지</tgt>` | 2283 |
| 9 | `<src>in the United States. </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 676 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 2298 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 697 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendment, </src><tgt><\|wait\|></tgt>` | 2196 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>of course, I'm </src><tgt><\|wait\|></tgt>` | 1365 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1132 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 743 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1201 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 1169 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>逆にできなくなって</src><tgt><\|wait\|></tgt>` | 1366 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>しまうので、</src><tgt><\|wait\|></tgt>` | 965 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1619 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1187 |
| 9 | `<src>ナットが</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt>이것이 기어입니다. 기어가 헐거워지면 신호가 오히려 안 되게 되니까, 기어 끝에 역나사 너트가</tgt>` | 2759 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 2423 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 984 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1926 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文部会完了を</src><tgt><\|wait\|></tgt>` | 1419 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1100 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1116 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy, </src><tgt><\|wait\|></tgt>` | 1152 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1453 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy gets </src><tgt><\|wait\|></tgt>` | 1635 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to other </src><tgt><\|wait\|></tgt>` | 1523 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>types of energy, </src><tgt>고무줄처럼 늘어난 화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면 그 잠재 에너지는 다른 종류의 에너지로 변환됩니다.</tgt>` | 2961 |
| 9 | `<src>like heat or light, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 2482 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>or gets used </src><tgt><\|wait\|></tgt>` | 1398 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds </src><tgt><\|wait\|></tgt>` | 1654 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1413 |

---

### Test Example 26 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 </src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이것들은 </src><tgt><\|wait\|></tgt>` | 1018 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유니트 링과 </src><tgt><\|wait\|></tgt>` | 1503 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거는 거진 </src><tgt><\|wait\|></tgt>` | 1058 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산 한 링이 </src><tgt><\|wait\|></tgt>` | 1276 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>나란치로 굉장히 </src><tgt><\|wait\|></tgt>` | 2076 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt>These are either vanadium or something similar. These are almost unit rings, and this is almost a unit ring, and it's very, very</tgt>` | 2621 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 다물리라 </src><tgt><\|wait\|></tgt>` | 842 |
| 9 | `<src>이렇게 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where</tgt>` | `<src>이것이 다기다 </src><tgt><\|wait\|></tgt>` | 1766 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>그런데 </src><tgt><\|wait\|></tgt>` | 1247 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1449 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그것에다가 </src><tgt><\|wait\|></tgt>` | 1560 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아니면 </src><tgt><\|wait\|></tgt>` | 1489 |

---

### Test Example 27 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 1041 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二期市场，</src><tgt><\|wait\|></tgt>` | 1181 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会服务</src><tgt><\|wait\|></tgt>` | 1194 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一期一线</src><tgt><\|wait\|></tgt>` | 1425 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们。</src><tgt><\|wait\|></tgt>` | 1994 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1193 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt>2期市場は、1期の一線大牛たちをサポートします。例えば、微信で</tgt>` | 2277 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>沟通好几十年，</src><tgt><\|wait\|></tgt>` | 1352 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1856 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>微信沟通好</src><tgt><\|wait\|></tgt>` | 1666 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>平衡的性膀</src><tgt><\|wait\|></tgt>` | 1505 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1377 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切都正常，</src><tgt><\|wait\|></tgt>` | 1160 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无反应，</src><tgt><\|wait\|></tgt>` | 1070 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1175 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1444 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>切片大概</src><tgt><\|wait\|></tgt>` | 1486 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1592 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来判断，</src><tgt>Everything was normal at the time, no reaction at all. So, I insisted on not cutting in, and I used the twelve- life method to judge.</tgt>` | 2604 |
| 9 | `<src>一下敲腿，</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 1427 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 1701 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1615 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>当然都很</src><tgt><\|wait\|></tgt>` | 1410 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1386 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1050 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 1013 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1210 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是以前造成的</src><tgt><\|wait\|></tgt>` | 1240 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1401 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1456 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1593 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt>皆さんにお伝えしたいのですが、このローマは以前の危機とは違うので、</tgt>` | 1845 |
| 9 | `<src>也不可能是</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、</tgt>` | `<src>跟丰收也不</src><tgt><\|wait\|></tgt>` | 751 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>可能是</src><tgt><\|wait\|></tgt>` | 1276 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一起逐渐</src><tgt><\|wait\|></tgt>` | 1808 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 1539 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的经济会</src><tgt><\|wait\|></tgt>` | 1498 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>见义修德的朋友呢，</src><tgt><\|wait\|></tgt>` | 1517 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1161 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1035 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>to produce something written, </src><tgt><\|wait\|></tgt>` | 1202 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1232 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 2176 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1067 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the word. It's like, oh, </src><tgt>あるいは、何か書く必要がある場合、文章を書く必要がある場合、単語のスペルが全く分からないことに気づく。まるで「ああ、</tgt>` | 2725 |
| 9 | `<src>is this word </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 2305 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 702 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>start with a double p, </src><tgt><\|wait\|></tgt>` | 2296 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double l, </src><tgt><\|wait\|></tgt>` | 1322 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>I don't know. </src><tgt><\|wait\|></tgt>` | 985 |

---

### Test Example 31 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new </src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1038 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there was such </src><tgt><\|wait\|></tgt>` | 1116 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>interest before. </src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Net future </src><tgt><\|wait\|></tgt>` | 1389 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>TC </src><tgt><\|wait\|></tgt>` | 1301 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>there. </src><tgt><\|wait\|></tgt>` | 1529 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>So this is just </src><tgt>之前就有这样的兴趣。NetFutureTC。所以这只是</tgt>` | 1698 |
| 9 | `<src>one another place </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个</tgt>` | `<src>one another </src><tgt><\|wait\|></tgt>` | 957 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>place to look at </src><tgt><\|wait\|></tgt>` | 1085 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2121 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>what </src><tgt><\|wait\|></tgt>` | 1387 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1574 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>would like to </src><tgt><\|wait\|></tgt>` | 1324 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>have a pair of that. </src><tgt><\|wait\|></tgt>` | 745 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 933 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개 가 </src><tgt><\|wait\|></tgt>` | 1314 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중호보서 100만으로 </src><tgt><\|wait\|></tgt>` | 1612 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업들이 </src><tgt><\|wait\|></tgt>` | 1381 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 964 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1856 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1383 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 </src><tgt>そのうち150社は、中小型企業で、それぞれ100万の売上でした。一般的に、中小企業は成長するか、あるいは</tgt>` | 2174 |
| 9 | `<src>걷게 되는데 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>해외 획득에 </src><tgt><\|wait\|></tgt>` | 2363 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>관련 되는데, 이번에 </src><tgt><\|wait\|></tgt>` | 830 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업 들은 성장 도 </src><tgt><\|wait\|></tgt>` | 2301 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>폐업도 하지 않는 </src><tgt><\|wait\|></tgt>` | 1410 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 890 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 911 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>前头，</src><tgt><\|wait\|></tgt>` | 1092 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1024 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了前头之后</src><tgt><\|wait\|></tgt>` | 1257 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>亲密UPB</src><tgt><\|wait\|></tgt>` | 1410 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就要先</src><tgt><\|wait\|></tgt>` | 1665 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>手足，</src><tgt><\|wait\|></tgt>` | 1525 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我在</src><tgt>彼は前方にいる。もし前方にいるなら、親密なUPBを先に手足で</tgt>` | 2489 |
| 9 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。</tgt>` | `<src>继续操作</src><tgt><\|wait\|></tgt>` | 1319 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 1679 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1717 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1462 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1389 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1077 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>帝僵的部分</src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1119 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1002 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>戴吊的人，但是</src><tgt><\|wait\|></tgt>` | 1339 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于逆向的</src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这通场</src><tgt><\|wait\|></tgt>` | 1850 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>像那么这样一个</src><tgt><\|wait\|></tgt>` | 1382 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>状况，就叫去</src><tgt>제강 부분에서 우리가 본 것은 갓을 쓴 사람인데, 그 사람은 역방향의 이 상황과 같은 상황이라고 불립니다. 그래서</tgt>` | 2616 |
| 9 | `<src>特别注意，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>特别注意是</src><tgt><\|wait\|></tgt>` | 2291 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 677 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到于他</src><tgt><\|wait\|></tgt>` | 1998 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>得到不到</src><tgt><\|wait\|></tgt>` | 1069 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>于他的意思</src><tgt><\|wait\|></tgt>` | 1351 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>了。</src><tgt><\|wait\|></tgt>` | 1126 |

---

### Test Example 35 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1220 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1113 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1060 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1197 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and like ten of them </src><tgt><\|wait\|></tgt>` | 1438 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really </src><tgt><\|wait\|></tgt>` | 1521 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>「今まさに動き出している人」って、本当に重要なこと、つまり10個くらいあるんです。</tgt>` | 2298 |
| 9 | `<src>I'm going to go into. </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 984 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 2275 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1273 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>at the end of this video. </src><tgt><\|wait\|></tgt>` | 1759 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It'll cover each one. </src><tgt><\|wait\|></tgt>` | 1550 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>And a little more </src><tgt><\|wait\|></tgt>` | 953 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>detail, but </src><tgt><\|wait\|></tgt>` | 583 |

---

### Test Example 36 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 848 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알고 있나요? </src><tgt><\|wait\|></tgt>` | 1059 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1247 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1268 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1352 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1650 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>가는 그대로 </src><tgt><\|wait\|></tgt>` | 1480 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>걸려 갔느라 </src><tgt>またご存知ですか？ここで異邦人として言葉を話せないウサンにそのまま連れて行かれ、</tgt>` | 2397 |
| 9 | `<src><\|wait\|></src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。</tgt>` | `<src>그럼 </src><tgt><\|wait\|></tgt>` | 1344 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼으로 내가 </src><tgt><\|wait\|></tgt>` | 1815 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1525 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리노니 </src><tgt><\|wait\|></tgt>` | 1506 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영어로 </src><tgt><\|wait\|></tgt>` | 1486 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 1051 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 556 |

---

### Test Example 37 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1130 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어차피 보면 </src><tgt><\|wait\|></tgt>` | 892 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1294 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1248 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이런 인생 이자 </src><tgt><\|wait\|></tgt>` | 1420 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1559 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1339 |
| 9 | `<src><\|wait\|></src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>어 </src><tgt>反正看，</tgt>` | 802 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인감모다는 </src><tgt><\|wait\|></tgt>` | 667 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금은 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1550 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>해봐. </src><tgt><\|wait\|></tgt>` | 1611 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2143 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 1181 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 1155 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 </src><tgt>你就是那个和二十代一起走过的人，像这样的人。所以，嗯，</tgt>` | 1951 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手</src><tgt><\|wait\|></tgt>` | 784 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>とかだと</src><tgt><\|wait\|></tgt>` | 1123 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1166 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>10秒で</src><tgt><\|wait\|></tgt>` | 1385 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ1秒に</src><tgt><\|wait\|></tgt>` | 1082 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1619 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>設定なんすよね。</src><tgt>因为是二手车之类的，大概10秒，也就是每秒1秒左右的设置。</tgt>` | 2215 |
| 9 | `<src>ね。</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。</tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 933 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 801 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 2306 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11</src><tgt><\|wait\|></tgt>` | 985 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>二つで</src><tgt><\|wait\|></tgt>` | 1961 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1287 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 827 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから</src><tgt>所以，大概是11个，那个“见合うま”之类的，</tgt>` | 1837 |

---

### Test Example 39 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1150 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Hiemel이라고 하는 </src><tgt><\|wait\|></tgt>` | 1210 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터도 </src><tgt><\|wait\|></tgt>` | 1231 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있고 </src><tgt><\|wait\|></tgt>` | 1316 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람도 </src><tgt><\|wait\|></tgt>` | 1474 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있는 </src><tgt><\|wait\|></tgt>` | 1620 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터의 언어에 </src><tgt>哦，计算机也能够理解Hiemel，而且人们也能理解计算机的语言。</tgt>` | 2318 |
| 9 | `<src>문법 에 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1309 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법이 맞게 </src><tgt><\|wait\|></tgt>` | 1909 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>우리가 이제 그것들을 </src><tgt><\|wait\|></tgt>` | 1640 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 1490 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1391 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>그것들을 작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1202 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1002 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 1051 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个餐饮可以说是</src><tgt><\|wait\|></tgt>` | 1210 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1049 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正餐的部分</src><tgt><\|wait\|></tgt>` | 1411 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1170 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>以及在西域方面的</src><tgt><\|wait\|></tgt>` | 1753 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>夜间餐馆所代表的</src><tgt><\|wait\|></tgt>` | 1559 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>红利</src><tgt>食事に関しては、かなり良いと言えますが、正餐寄りです。また、西域の夜間レストランが象徴する夜間飲食のメリットも</tgt>` | 2532 |
| 9 | `<src>提升。如果是在</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>收入的提升，</src><tgt><\|wait\|></tgt>` | 2310 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果是在投资领域</src><tgt><\|wait\|></tgt>` | 686 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月也是</src><tgt><\|wait\|></tgt>` | 1762 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>不错，只是</src><tgt><\|wait\|></tgt>` | 1285 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说就</src><tgt><\|wait\|></tgt>` | 1333 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了那么一点</src><tgt><\|wait\|></tgt>` | 1178 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1011 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1121 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らせてやれ</src><tgt><\|wait\|></tgt>` | 1102 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1115 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1195 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>火事を見ている</src><tgt><\|wait\|></tgt>` | 1426 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1383 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えてる</src><tgt>그렇다면 그냥 젖게 해라. 나는 불이 난 걸 보고 있어. 이제 한계는</tgt>` | 2329 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>ふれふれ</src><tgt><\|wait\|></tgt>` | 574 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>火勢よ。</src><tgt><\|wait\|></tgt>` | 1536 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1595 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長年ぶなデイコール</src><tgt><\|wait\|></tgt>` | 2044 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってるんだ。</src><tgt><\|wait\|></tgt>` | 1176 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1267 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい快族線を見た</src><tgt><\|wait\|></tgt>` | 1192 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 975 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational </src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>containment. How far </src><tgt><\|wait\|></tgt>` | 983 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1197 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt><\|wait\|></tgt>` | 1265 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1407 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1441 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1780 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>containment. Did you </src><tgt>교육적 격리. 실제로 얼마나 교육을 받았나요? 고등학교를 졸업했나요? 그건 한 단계의 격리입니다. </tgt>` | 2558 |
| 9 | `<src>to college, </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>go to college, </src><tgt><\|wait\|></tgt>` | 1519 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and so did you graduate </src><tgt><\|wait\|></tgt>` | 1606 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>that's another level of </src><tgt><\|wait\|></tgt>` | 1890 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>containment. </src><tgt><\|wait\|></tgt>` | 1265 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 1383 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 1172 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 953 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1211 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세인바라 </src><tgt><\|wait\|></tgt>` | 1010 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌고야 </src><tgt><\|wait\|></tgt>` | 1209 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 서름이 </src><tgt><\|wait\|></tgt>` | 1252 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 차리도 </src><tgt><\|wait\|></tgt>` | 1427 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>돋은 느낌 이오며 </src><tgt><\|wait\|></tgt>` | 1805 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들어서 </src><tgt><\|wait\|></tgt>` | 1482 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt>目を閉じて、セインバラを祈り、今、ソラムが芽生えたような気がして、それを揺らして一緒に遊ぼうというんだ。</tgt>` | 2664 |
| 9 | `<src>귀신 이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 2306 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>오며 물릴 거고 </src><tgt><\|wait\|></tgt>` | 763 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오며 </src><tgt><\|wait\|></tgt>` | 2143 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜주고 </src><tgt><\|wait\|></tgt>` | 1216 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>달려주니까 </src><tgt><\|wait\|></tgt>` | 988 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에. </src><tgt><\|wait\|></tgt>` | 1239 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 933 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 1124 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1265 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうだけじゃなくて</src><tgt><\|wait\|></tgt>` | 1095 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1186 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1352 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1620 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアル</src><tgt><\|wait\|></tgt>` | 1495 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>の書いてあとそれは</src><tgt>This isn't just a visual development environment, it's a visual Python development environment. And this is also a flow graph visual. And that's</tgt>` | 2640 |
| 9 | `<src>にそこから</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>Pythonコードなんそっから生成</src><tgt><\|wait\|></tgt>` | 2183 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>されてそれが</src><tgt><\|wait\|></tgt>` | 867 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1693 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1372 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことをしているから</src><tgt><\|wait\|></tgt>` | 1336 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 1059 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 425 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 876 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 996 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>then </src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self defining </src><tgt><\|wait\|></tgt>` | 1155 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>what we think the standard is, </src><tgt><\|wait\|></tgt>` | 1302 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1502 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1850 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1269 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>活動、そして自分自身を定義する基準は、あなたが完全に正しいと思うからこそ、その基準は正しい。しかし、現実は、</tgt>` | 2564 |
| 9 | `<src>block and because the </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>in the box, </src><tgt><\|wait\|></tgt>` | 1814 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed </src><tgt><\|wait\|></tgt>` | 1306 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>from </src><tgt><\|wait\|></tgt>` | 1628 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt><\|wait\|></tgt>` | 1438 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1356 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard because </src><tgt><\|wait\|></tgt>` | 1149 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>everything at this point </src><tgt><\|wait\|></tgt>` | 1036 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to our standard. </src><tgt><\|wait\|></tgt>` | 705 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인증 상승 하는 </src><tgt><\|wait\|></tgt>` | 1169 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인다면 </src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주도 </src><tgt><\|wait\|></tgt>` | 1377 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1072 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 2059 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1159 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt>If the stock index is rising, these large-cap stocks will also see a significant increase, but first,</tgt>` | 2253 |
| 9 | `<src>종목 들이 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1343 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1830 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1730 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1402 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시총이 </src><tgt><\|wait\|></tgt>` | 1420 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 온 종목 을 </src><tgt><\|wait\|></tgt>` | 1185 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 1064 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 721 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 이런 경우 들을 </src><tgt><\|wait\|></tgt>` | 1075 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>수도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1230 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1289 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨컨트예요. </src><tgt><\|wait\|></tgt>` | 2320 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>B가 컨설턴트 </src><tgt><\|wait\|></tgt>` | 1129 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>여 가지고 A라는 </src><tgt>ですから、もちろんこのようなケースもあります。Aという人とBという人が相互にコンコンテです。Bがコンサルタントで、Aという</tgt>` | 2419 |
| 9 | `<src>A라는 사람 이 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 2304 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 825 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 2142 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비라는 사람이 </src><tgt><\|wait\|></tgt>` | 1213 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로사이트스 </src><tgt><\|wait\|></tgt>` | 1160 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>T에서 </src><tgt><\|wait\|></tgt>` | 1140 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>X까지 </src><tgt><\|wait\|></tgt>` | 855 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까? </src><tgt><\|wait\|></tgt>` | 872 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1177 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매 니다. </src><tgt><\|wait\|></tgt>` | 1221 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>이 운전 을 </src><tgt><\|wait\|></tgt>` | 1121 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 걸 </src><tgt><\|wait\|></tgt>` | 1232 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1380 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있으면은 뭐 </src><tgt><\|wait\|></tgt>` | 1624 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북으로 가면 </src><tgt><\|wait\|></tgt>` | 1519 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt>进去的时候，我真是太迷茫了。我走过那段路，如果我走过那段路，</tgt>` | 2423 |
| 9 | `<src><\|wait\|></src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가면 또 장려 리요. </src><tgt><\|wait\|></tgt>` | 2066 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1160 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 챙기 냐요. </src><tgt><\|wait\|></tgt>` | 2155 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1132 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>열심히 해보아요. </src><tgt><\|wait\|></tgt>` | 1168 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 안인 것 같아요. </src><tgt><\|wait\|></tgt>` | 1121 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 814 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람들이 </src><tgt><\|wait\|></tgt>` | 987 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1307 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 1078 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자이의 분석을 보시면 </src><tgt><\|wait\|></tgt>` | 1570 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니 가 </src><tgt><\|wait\|></tgt>` | 1847 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이오렉트의 </src><tgt><\|wait\|></tgt>` | 1295 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPP 파이프를 </src><tgt>そして、多くの人がこれについて分析しています。このロクジャイの分析を見ると、ソニーがイオレクのFPPパイプを</tgt>` | 2647 |
| 9 | `<src>128비트로 낮춘 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 2418 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮추어서 로포인다. </src><tgt><\|wait\|></tgt>` | 734 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 2179 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1238 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1107 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>S2가 </src><tgt><\|wait\|></tgt>` | 1109 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>여기도 없다. </src><tgt><\|wait\|></tgt>` | 932 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 742 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 1065 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和关于</src><tgt><\|wait\|></tgt>` | 1015 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>针对对手的感情</src><tgt><\|wait\|></tgt>` | 1209 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>和真实意图的。</src><tgt><\|wait\|></tgt>` | 1271 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1417 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1532 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1622 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说，</src><tgt>伝聞や、相手の感情や真意に関するものも多いです。よく</tgt>` | 2301 |
| 9 | `<src>这样说：“</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが</tgt>` | `<src>啊。</src><tgt><\|wait\|></tgt>` | 1131 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看。</src><tgt><\|wait\|></tgt>` | 2043 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1374 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>躲黄了。</src><tgt><\|wait\|></tgt>` | 1583 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1439 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 665 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1028 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 886 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是说。</src><tgt>よく聞くのですが、この人はまた逃げているようです。もう目は全てを物語っています。つまり、</tgt>` | 1179 |

---

### Test Example 51 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A Aが</src><tgt><\|wait\|></tgt>` | 1121 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>あるんですね。</src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>色々な場面で</src><tgt><\|wait\|></tgt>` | 1264 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>清掃活動とかをしている時に</src><tgt><\|wait\|></tgt>` | 1426 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>Aへの</src><tgt><\|wait\|></tgt>` | 1779 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>連絡を調べたことで、</src><tgt><\|wait\|></tgt>` | 1504 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あの清掃活動とか</src><tgt><\|wait\|></tgt>` | 1855 |
| 9 | `<src>保証する、生息である</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence—</tgt>` | `<src>をすること</src><tgt>There's an A A, you see. When you're doing cleaning activities or something, and you look up contact information for A, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you know, you` | 9926 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>を保証する</src><tgt><\|wait\|></tgt>` | 583 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方をされました。</src><tgt><\|wait\|></tgt>` | 794 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 329 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 1027 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 1324 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1056 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1191 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1333 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1800 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>either, if </src><tgt><\|wait\|></tgt>` | 1377 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the situation </src><tgt><\|wait\|></tgt>` | 1717 |
| 9 | `<src>a situation </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果</tgt>` | `<src>where you </src><tgt>另外，你将无法在资源之间移动媒体对象，</tgt>` | 922 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 2424 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 747 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>to a particular resource </src><tgt><\|wait\|></tgt>` | 2153 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>instead of </src><tgt><\|wait\|></tgt>` | 1033 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>let us know, and we can see </src><tgt><\|wait\|></tgt>` | 1325 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about giving those media files </src><tgt><\|wait\|></tgt>` | 1229 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>to us </src><tgt><\|wait\|></tgt>` | 874 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure to get backed up </src><tgt><\|wait\|></tgt>` | 990 |
| 18 | `<src>properly. </src><tgt>你发现自己给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 300 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the sort of </src><tgt><\|wait\|></tgt>` | 1114 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>the concept </src><tgt><\|wait\|></tgt>` | 1060 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>that we </src><tgt><\|wait\|></tgt>` | 1185 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>are all about </src><tgt><\|wait\|></tgt>` | 1379 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>the relationship </src><tgt><\|wait\|></tgt>` | 1461 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>between the two sides </src><tgt><\|wait\|></tgt>` | 1739 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>of love. </src><tgt>모든 관계에서 사랑의 개념이 중요합니다. 양측의 사랑 관계가</tgt>` | 2245 |
| 9 | `<src>同时进入恨。</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>Now, let's </src><tgt><\|wait\|></tgt>` | 1067 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>enter into </src><tgt><\|wait\|></tgt>` | 2036 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the stage </src><tgt><\|wait\|></tgt>` | 1133 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>of the stage of love. </src><tgt><\|wait\|></tgt>` | 1949 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It's over. </src><tgt><\|wait\|></tgt>` | 1499 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>It becomes </src><tgt><\|wait\|></tgt>` | 565 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that sort of </src><tgt><\|wait\|></tgt>` | 1085 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>the concept. </src><tgt><\|wait\|></tgt>` | 882 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt>사랑의 무대에서 이제 막을 내립니다. 그것은 그 개념이 됩니다. 그것은 계속</tgt>` | 1117 |
| 18 | `<src>继续在移动。</src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다. 그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>to evolve. </src><tgt><\|wait\|></tgt>` | 443 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1392 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1168 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1052 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt><\|wait\|></tgt>` | 1125 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1365 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1460 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance versus </src><tgt><\|wait\|></tgt>` | 1583 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt>最初のセクションで少し間違った道を進んでいました。AHRフィールドの重要性が、</tgt>` | 1898 |
| 9 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、</tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 633 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt><\|wait\|></tgt>` | 1385 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1891 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1586 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1448 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1390 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1194 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 991 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 751 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt>バリアントデータベースが、明らかに私の好きなものの一つです。つまり、これらのデータソースに含めるべきフィールドについて合意できていない場合、それから引き出すものはありませんよね？</tgt>` | 1087 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 359 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 1031 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a hungry </src><tgt><\|wait\|></tgt>` | 1071 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>and knows that he's </src><tgt><\|wait\|></tgt>` | 1492 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>not about </src><tgt><\|wait\|></tgt>` | 1163 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being in the wilderness </src><tgt><\|wait\|></tgt>` | 1965 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>all day. He's that he's hungry </src><tgt><\|wait\|></tgt>` | 1849 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt>ある時、彼はイエスが飢えていることを知っていた。そして、一日中荒野にいるわけではないことを知っていた。彼は飢えていると、</tgt>` | 2110 |
| 9 | `<src>to Jesus," Hey, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus, say, "If </src><tgt><\|wait\|></tgt>` | 2395 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>the Son of God </src><tgt><\|wait\|></tgt>` | 669 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>proved it, turn </src><tgt><\|wait\|></tgt>` | 2138 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>these stones to bread, </src><tgt><\|wait\|></tgt>` | 1251 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>how did Jesus </src><tgt><\|wait\|></tgt>` | 935 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>deal with that </src><tgt><\|wait\|></tgt>` | 1172 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation?" </src><tgt><\|wait\|></tgt>` | 973 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 704 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>genuinely </src><tgt><\|wait\|></tgt>` | 580 |
| 18 | `<src>by bread alone. </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？人はパンだけで生きるものではない。</tgt>` | `<src>led by prayer alone. </src><tgt>イエスよ、神の子がその試練を乗り越えたなら、石をパンに変えられたなら、どうやってその試練を乗り越えたのか？本当に祈りだけで導かれていたんだ。</tgt>` | 1002 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1210 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 936 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1042 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1149 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1339 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I I I don't I don't </src><tgt><\|wait\|></tgt>` | 1720 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>have the courts want to be </src><tgt><\|wait\|></tgt>` | 1608 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>有意义的个人权利，而最高法院最后才加入，而不是领导者。我我我并不希望法院</tgt>` | 2290 |
| 9 | `<src>the the vanguard of social </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为</tgt>` | `<src>the vanguard of social change </src><tgt><\|wait\|></tgt>` | 643 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2197 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 849 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 2014 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1225 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1219 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged </src><tgt><\|wait\|></tgt>` | 953 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>so. </src><tgt>是社会变革的先锋队。但它们反映的是已经形成的共识。</tgt>` | 861 |
| 18 | `<src>So you have some </src><tgt>法院现在想成为社会变革的先锋，它们更倾向于反映已经形成的共识。所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 424 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 435 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 403 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 362 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>一下</src><tgt><\|wait\|></tgt>` | 988 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 1178 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分</src><tgt><\|wait\|></tgt>` | 1235 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个</src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>是客听的部分，</src><tgt><\|wait\|></tgt>` | 1587 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>而客听一般</src><tgt><\|wait\|></tgt>` | 1624 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1576 |
| 9 | `<src>我们</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가</tgt>` | `<src>是属于我们</src><tgt>그럼 이미지 부분을 한번 보겠습니다. 이미지 부분에는 '객청'이라는 부분이 보이는데, 객청은 보통</tgt>` | 1411 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在修习的地方，</src><tgt><\|wait\|></tgt>` | 2489 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1286 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分</src><tgt><\|wait\|></tgt>` | 1569 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1528 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>我们需要</src><tgt><\|wait\|></tgt>` | 514 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>给自己一点时间</src><tgt><\|wait\|></tgt>` | 1140 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>好好地</src><tgt><\|wait\|></tgt>` | 841 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做下来，休息</src><tgt><\|wait\|></tgt>` | 729 |
| 18 | `<src>我们可以看到这边是</src><tgt>쉬는 곳이잖아요. 그래서 이 신체 부위도 여러분이 자신에게 시간을 내서 편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们看到</src><tgt><\|wait\|></tgt>` | 532 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是包含五一人的嘛。</src><tgt>그래서 이건 몸의 부분인데, 우리가 잠시 시간을 내서 제대로 쉬어야 한다는 뜻이에요. 쉬어야 하니까요. 여기는 51인분 포함된 거죠.</tgt>` | 912 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 318 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以也是说</src><tgt><\|wait\|></tgt>` | 441 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1107 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1168 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1354 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1493 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 1514 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>personality is </src><tgt>この人たちは全く珍しく、世界を完全に変革することがよくあります。その個性は</tgt>` | 1945 |
| 9 | `<src>something of a </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は</tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 796 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1637 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1495 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, they also </src><tgt><\|wait\|></tgt>` | 2335 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1053 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 1157 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like to </src><tgt><\|wait\|></tgt>` | 1224 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt><\|wait\|></tgt>` | 933 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt>矛盾したものです。外向的でありながら、無意味な会話も嫌います。そしてすぐに本題に入ります。</tgt>` | 1213 |
| 18 | `<src>They also love to </src><tgt>矛盾しています。外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 441 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 443 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 370 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 390 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate </src><tgt><\|wait\|></tgt>` | 270 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 329 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in an IEP </src><tgt><\|wait\|></tgt>` | 353 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>standoff or </src><tgt><\|wait\|></tgt>` | 296 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이전 </src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>성공 을 경험 을 </src><tgt><\|wait\|></tgt>` | 1275 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>경험 을 </src><tgt><\|wait\|></tgt>` | 944 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1231 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후후의 당수를 </src><tgt><\|wait\|></tgt>` | 1364 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1725 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색 까지 </src><tgt><\|wait\|></tgt>` | 1481 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제는 </src><tgt>I've been sharing my experiences to help others succeed, and I've even been bragging about it, but now</tgt>` | 2399 |
| 9 | `<src>윤석열 후보 가 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>윤성률 후보 가 </src><tgt><\|wait\|></tgt>` | 1450 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정일 을 </src><tgt><\|wait\|></tgt>` | 1714 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제관 순간 </src><tgt><\|wait\|></tgt>` | 1816 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석 은 들으 내놓고 </src><tgt><\|wait\|></tgt>` | 1522 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤성률 후보 </src><tgt><\|wait\|></tgt>` | 1201 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 1293 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼 를 품은 </src><tgt><\|wait\|></tgt>` | 947 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 792 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt>Yoon Sung-yul, the candidate who was in the running for the presidency during the Kim Jong-il era, has put his foot down and is ready to attack Yoon Sung-yul, brandishing an axe.</tgt>` | 1015 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 272 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 320 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가 세발 </src><tgt><\|wait\|></tgt>` | 427 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 성상 납권 </src><tgt><\|wait\|></tgt>` | 269 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가. </src><tgt><\|wait\|></tgt>` | 295 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 369 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 이 얼마나 </src><tgt><\|wait\|></tgt>` | 278 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재 됩니까? </src><tgt><\|wait\|></tgt>` | 317 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 751 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt><\|wait\|></tgt>` | 1195 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1147 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1366 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスローンホテルも</src><tgt><\|wait\|></tgt>` | 1082 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる</src><tgt><\|wait\|></tgt>` | 1728 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>場所になってる</src><tgt>I'd like to try making something after dinner. So, this Golf Sloan Hotel is a place where you can have breakfast.</tgt>` | 2272 |
| 9 | `<src>予定になってるので</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>よって</src><tgt><\|wait\|></tgt>` | 857 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1177 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルフスローンホテル</src><tgt><\|wait\|></tgt>` | 2051 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1430 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なという方はですね</src><tgt><\|wait\|></tgt>` | 1559 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1403 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみてまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 691 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 964 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt>If you're considering staying at the Golf Sloan Hotel in the future, I think it's a good idea to check it out.</tgt>` | 1427 |
| 18 | `<src>のホテルからですね釜山</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel,</tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 592 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 442 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 394 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 389 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんな </src><tgt><\|wait\|></tgt>` | 349 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>かそんなレベルのね</src><tgt><\|wait\|></tgt>` | 340 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 358 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt>It's a great location— you can walk to Busan Station in just a minute or so. So, it's a nice hotel.</tgt>` | 646 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 269 |
| 27 | `<src>ご検討なさってみて</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good. If you'd like,</tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 198 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 188 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt><\|wait\|></tgt>` | 179 |
