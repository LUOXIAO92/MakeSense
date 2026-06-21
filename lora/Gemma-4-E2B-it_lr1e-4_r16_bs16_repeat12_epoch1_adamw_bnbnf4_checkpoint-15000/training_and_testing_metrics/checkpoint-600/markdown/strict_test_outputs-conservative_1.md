# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9735
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.1987
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
  - PROCESS_TIME_MS_AVG: 1304.7840
  - PROCESS_TIME_MS_P50: 1291.5160
  - PROCESS_TIME_MS_P95: 1950.3110
  - PROCESS_TIME_MS_MAX: 2724.9530

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1056 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>做的是</src><tgt>Parents need to</tgt>` | 806 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1032 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>深沉的爱交</src><tgt><\|wait\|></tgt>` | 1086 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt>use our deep love to water</tgt>` | 1499 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十分</src><tgt><\|wait\|></tgt>` | 796 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给孩子</src><tgt>the child</tgt>` | 1234 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>心灵营养。</src><tgt><\|wait\|></tgt>` | 1625 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>心耐心</src><tgt>heart nourishment.</tgt>` | 1518 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>等他</src><tgt><\|wait\|></tgt>` | 838 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt>Be patient and kind as he grows up.</tgt>` | 1641 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 973 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>是容易的，</src><tgt>気数をつけるのは簡単です。</tgt>` | 1537 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 925 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>一个师傅</src><tgt>でも、師匠が</tgt>` | 983 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>值得录。</src><tgt><\|wait\|></tgt>` | 1520 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如和除于</src><tgt>録る価値があるなら、</tgt>` | 1604 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>中间。</src><tgt><\|wait\|></tgt>` | 1513 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以，</src><tgt>中継してほしいです。</tgt>` | 1596 |
| 9 | `<src>虚阿凡</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1285 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt>だから、反省が必要で、</tgt>` | 1126 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>师傅。</src><tgt><\|wait\|></tgt>` | 1730 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 735 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 994 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲まだ</src><tgt><\|wait\|></tgt>` | 1095 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>1年生ですからね。</src><tgt>因为我们还是大一新生。</tgt>` | 1306 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう</src><tgt>在那个时候，</tgt>` | 1390 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>資格を</src><tgt><\|wait\|></tgt>` | 1236 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数していって</src><tgt>我们把这个资格</tgt>` | 1950 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>上げる</src><tgt><\|wait\|></tgt>` | 822 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>と10年経っても</src><tgt>算进去，就算过了十年，</tgt>` | 1762 |
| 11 | `<src>大した。</src><tgt>十年后也不会有什么大……</tgt>` | `<src>大丈夫。</src><tgt><\|wait\|></tgt>` | 1751 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>的总结点，</src><tgt>Why the summary point?</tgt>` | 993 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个收益也很大，</src><tgt><\|wait\|></tgt>` | 1281 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src><\|wait\|></src><tgt>The returns are also very high,</tgt>` | 1206 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，我在</src><tgt><\|wait\|></tgt>` | 1618 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>放假</src><tgt>and then I</tgt>` | 1302 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>的活动</src><tgt><\|wait\|></tgt>` | 1410 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>took a break</tgt>` | 1718 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>和陶人，</src><tgt><\|wait\|></tgt>` | 895 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这些</src><tgt>and went to the pottery class with Tao Ren,</tgt>` | 1649 |
| 11 | `<src>仁儿。</src><tgt>this kind of walnut kernels.</tgt>` | `<src>和陶人。</src><tgt><\|wait\|></tgt>` | 1828 |

---

### Test Example 5 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1049 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>lastly, </src><tgt>最后，</tgt>` | 800 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>he repeats </src><tgt><\|wait\|></tgt>` | 1018 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>learning to repeat </src><tgt>他重复学习</tgt>` | 1114 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>by finding a good app </src><tgt><\|wait\|></tgt>` | 1518 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it </src><tgt>找一个好的App，多做一些。</tgt>` | 1622 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and when you're not </src><tgt><\|wait\|></tgt>` | 1320 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>good at it, </src><tgt>当你不擅长的时候，</tgt>` | 1807 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 1175 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src>and </src><tgt>让周围的人来帮你，</tgt>` | 1662 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>in tell next time. </src><tgt><\|wait\|></tgt>` | 1904 |

---

### Test Example 6 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1109 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 970 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>T-shirts and such</tgt>` | 1109 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただろうというものも</src><tgt><\|wait\|></tgt>` | 1281 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>are also available.</tgt>` | 1467 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参考ください。</src><tgt><\|wait\|></tgt>` | 1209 |
| 7 | `<src>ご連絡としては</src><tgt>so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 963 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt>Please refer to this for your reference.</tgt>` | 2015 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>で、えっと</src><tgt><\|wait\|></tgt>` | 1019 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>この</src><tgt><\|wait\|></tgt>` | 1588 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>内訳がありますので、</src><tgt>The breakdown is as follows:</tgt>` | 1164 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1239 |

---

### Test Example 7 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 965 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>영심이 </src><tgt>I'm</tgt>` | 1001 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1145 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 웅심이 </src><tgt><\|wait\|></tgt>` | 1251 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>소소 웅심이 가 </src><tgt>a small spirit of the sword, a small spirit of the sword,</tgt>` | 2613 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 894 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞이는 건데요. </src><tgt><\|wait\|></tgt>` | 2012 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt>is mixing. Hey,</tgt>` | 1010 |
| 9 | `<src>진짜 이거 </src><tgt>Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1607 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행동 으로도 </src><tgt>this really</tgt>` | 700 |
| 11 | `<src>진짜. </src><tgt>seriously killer for a hangover, for real.</tgt>` | `<src>조금 죽입니다. </src><tgt><\|wait\|></tgt>` | 1814 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 824 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 쳐박히고 </src><tgt>I'm</tgt>` | 1722 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1306 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 984 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로지기인 </src><tgt>a person who's been buried in their own</tgt>` | 1796 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1750 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1271 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt>Hernan Park</tgt>` | 1763 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1518 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt>and generations like that.</tgt>` | 844 |

---

### Test Example 9 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1185 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들은 </src><tgt>The NickS on the list</tgt>` | 1385 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 906 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt>actually don't have high intelligence,</tgt>` | 1164 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않고 </src><tgt><\|wait\|></tgt>` | 1509 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt>they were just picked at random</tgt>` | 1608 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들이었기 때문 </src><tgt><\|wait\|></tgt>` | 2142 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>입니다. </src><tgt>because they were NickS.</tgt>` | 1209 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1602 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 642 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교사 들은 </src><tgt>The teachers who didn't know the Sasi</tgt>` | 1905 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后，</src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>那内部的</src><tgt>淘撒が終わったら、</tgt>` | 1065 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>的液体检清</src><tgt><\|wait\|></tgt>` | 1336 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也</src><tgt>内部の液体検査エネルギーも</tgt>` | 998 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷了落了，然后就</src><tgt><\|wait\|></tgt>` | 1860 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>停留在</src><tgt>消えて、停滞して、</tgt>` | 1305 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1839 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>低能量的运行状态</src><tgt>比較的低エネルギーの動作状態に留まる</tgt>` | 1662 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>态。</src><tgt><\|wait\|></tgt>` | 1647 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>状態です。これは</tgt>` | 1871 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>的低于状态。</src><tgt><\|wait\|></tgt>` | 509 |

---

### Test Example 11 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1031 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>从这里开始，</tgt>` | 1042 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので</src><tgt><\|wait\|></tgt>` | 1110 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt>事情就这么开始了。</tgt>` | 1235 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご方法</src><tgt><\|wait\|></tgt>` | 1461 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ご言やん</src><tgt><\|wait\|></tgt>` | 1209 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>您说</tgt>` | 961 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt><\|wait\|></tgt>` | 1773 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt>Cezanne、Lunard，</tgt>` | 1322 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>などという人の</src><tgt><\|wait\|></tgt>` | 1721 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵は</src><tgt>这些人的画作</tgt>` | 1869 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 770 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 829 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt>重要な研究を</tgt>` | 1074 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely </src><tgt><\|wait\|></tgt>` | 1159 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>happy people? This is </src><tgt>極めて幸せな人々の間で、様々な研究が行われたのでしょうか？</tgt>` | 1741 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem, </src><tgt><\|wait\|></tgt>` | 1198 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. </src><tgt>これは研究の入り口です。</tgt>` | 1441 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at </src><tgt><\|wait\|></tgt>` | 1698 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10% of the happiest </src><tgt>最も幸せな人々の10%を見ます。</tgt>` | 1791 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people out </src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, </src><tgt>その中で、</tgt>` | 1893 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | 1893 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>ちょっと距離が離れてくる</src><tgt>Advantage，</tgt>` | 1079 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1153 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>大賞とかで</src><tgt>好像距离有点远了，</tgt>` | 1193 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱりですね、</src><tgt><\|wait\|></tgt>` | 1542 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>解消したい方って</src><tgt>大家想解决这个问题，</tgt>` | 1482 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐにご意識いただけたら</src><tgt><\|wait\|></tgt>` | 1872 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>いい</src><tgt>就</tgt>` | 1240 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ですね、でも</src><tgt><\|wait\|></tgt>` | 1100 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>本当に本当に</src><tgt>真的真的</tgt>` | 1223 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>強くなっている</src><tgt><\|wait\|></tgt>` | 1837 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>ので、なので</src><tgt>变强了，所以</tgt>` | 1875 |

---

### Test Example 14 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 818 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>A Aが</src><tgt>That A A</tgt>` | 992 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>あるんですね。</src><tgt><\|wait\|></tgt>` | 1046 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>その辺で</src><tgt>exists. In that regard,</tgt>` | 1260 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>清掃活動とかっていう時</src><tgt><\|wait\|></tgt>` | 1481 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>にAの欄を</src><tgt>when we do cleanup activities,</tgt>` | 1362 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、</src><tgt><\|wait\|></tgt>` | 900 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あの清掃活動とか</src><tgt>we look at the A column</tgt>` | 2185 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を</src><tgt><\|wait\|></tgt>` | 912 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>清掃でこと保証する</src><tgt>and guarantee that the cleanup activities are</tgt>` | 1910 |
| 11 | `<src>といったような</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>といった使い方をされます。</src><tgt><\|wait\|></tgt>` | 1869 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>used for that purpose.</tgt>` | 1789 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 877 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt>On the other hand,</tgt>` | 1279 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여 달라고 주고 내가 죽일 려 </src><tgt><\|wait\|></tgt>` | 1630 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>그것으로 하소서. </src><tgt>let them kill the advanced ones, and I'll kill them with that.</tgt>` | 2094 |
| 5 | `<src>다른 잔찜에 </src><tgt>came in here to do it.</tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>전진 쪽에 달아 </src><tgt>On the other side,</tgt>` | 1453 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>자란다. 내가 </src><tgt><\|wait\|></tgt>` | 1769 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt>the front lines are growing. I'm not hearing that kind of talk,</tgt>` | 2070 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>중요한 게. </src><tgt><\|wait\|></tgt>` | 819 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아. </src><tgt>that's important.</tgt>` | 1542 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1695 |

---

### Test Example 16 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为这个情况</src><tgt><\|wait\|></tgt>` | 883 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>我们就是</src><tgt>Because of this situation,</tgt>` | 1099 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1223 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就更改了</src><tgt><\|wait\|></tgt>` | 1041 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>回复主管，或是通知对方</src><tgt>we had to change our reply to the supervisor,</tgt>` | 2289 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>消息，</src><tgt><\|wait\|></tgt>` | 904 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>这个状况，不要想自己</src><tgt>or notify the other party about this situation.</tgt>` | 2557 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>怎么都把它</src><tgt><\|wait\|></tgt>` | 978 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>扛下来，</src><tgt>Don't think you can handle it,</tgt>` | 1876 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>工具理性</src><tgt><\|wait\|></tgt>` | 1852 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是客观的</src><tgt>instrumental rationality is objective,</tgt>` | 1878 |

---

### Test Example 17 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 너무 </src><tgt><\|wait\|></tgt>` | 1030 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>이 저희 에 </src><tgt>これは</tgt>` | 906 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>열여야 할 수 있지만 </src><tgt><\|wait\|></tgt>` | 1469 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>진짜 보살 도요 </src><tgt>あまりにも</tgt>` | 980 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기가 </src><tgt><\|wait\|></tgt>` | 1623 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 피로고 </src><tgt>必要かもしれません。でも、本当に菩薩なのに、夢を見ている</tgt>` | 2485 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보이 고 나만 </src><tgt><\|wait\|></tgt>` | 1950 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>이 보살 로 </src><tgt>のは私だけ</tgt>` | 948 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 피로고 </src><tgt><\|wait\|></tgt>` | 1552 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>우주 가신다. 이 보살 이란 </src><tgt>ように見えます。宇宙が</tgt>` | 2111 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>그런데. </src><tgt><\|wait\|></tgt>` | 1693 |

---

### Test Example 18 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 735 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>body saying? </src><tgt>你的身体在说什么？</tgt>` | 1238 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1540 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does </src><tgt>把针头插到你的身体上。</tgt>` | 1724 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt><\|wait\|></tgt>` | 1156 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>What is it? Is it </src><tgt>紧张感从哪里开始？是什么？</tgt>` | 1445 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>a day? </src><tgt><\|wait\|></tgt>` | 1525 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it tightening in your chest? </src><tgt>是一天的问题吗？是在胸口收紧吗？</tgt>` | 1752 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it </src><tgt><\|wait\|></tgt>` | 1577 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>a low level of charge you use </src><tgt>还是你用的是低电量？</tgt>` | 2097 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>saying. </src><tgt><\|wait\|></tgt>` | 1744 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 708 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt>저를</tgt>` | 998 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>鬼道号，</src><tgt>귀도호로 돌아가게 해 주세요.</tgt>` | 1367 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够好好的</src><tgt><\|wait\|></tgt>` | 1621 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在它下面的时候，</src><tgt>그 아래에서</tgt>` | 1493 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日航</src><tgt><\|wait\|></tgt>` | 1764 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>日航的日航</src><tgt>일본 항공의 일본 항공을</tgt>` | 1694 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的时候，</src><tgt><\|wait\|></tgt>` | 1647 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时</src><tgt>제가 그때</tgt>` | 984 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>背着一个</src><tgt><\|wait\|></tgt>` | 1335 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>小小的愿望，</src><tgt>작은 소망을 안고 있었는데,</tgt>` | 1951 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 760 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt>If you're a female high school student</tgt>` | 1743 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间</src><tgt><\|wait\|></tgt>` | 1172 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有这种</src><tgt>have this kind of relationship</tgt>` | 1381 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>重要性，</src><tgt><\|wait\|></tgt>` | 1048 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>because of the importance of being with someone who doesn't look like a bad boy,</tgt>` | 2236 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1696 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里</src><tgt>does it mean that it starts that night</tgt>` | 1191 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1514 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>from that night?</tgt>` | 1802 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1820 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>系列篇。</src><tgt>The Yang Zisi series.</tgt>` | 751 |

---

### Test Example 21 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Chunah Teru, </src><tgt>제 이름은 츠나 테루입니다.</tgt>` | 1667 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1168 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src>in AI, </src><tgt>현재 AI를 공부하고 있습니다.</tgt>` | 1629 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>back-end finance, </src><tgt><\|wait\|></tgt>` | 1260 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bit of psychology. </src><tgt>그리고 약간의 심리학도 공부하고 있고요.</tgt>` | 1443 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1423 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yaein, </src><tgt>여기 예인에서</tgt>` | 1449 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1721 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>미래에는</tgt>` | 1997 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consulting, </src><tgt><\|wait\|></tgt>` | 1787 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src><\|wait\|></src><tgt>기업 컨설팅 쪽으로</tgt>` | 895 |

---

### Test Example 22 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1133 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>and then after </src><tgt>好的，然后</tgt>` | 1090 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 1171 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1131 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt>这些例子之后，</tgt>` | 1539 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1410 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1258 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>它告诉我们</tgt>` | 1679 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 944 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>实际上使用这些值。</tgt>` | 1679 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1838 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>So this game.board array </src><tgt><\|wait\|></tgt>` | 1883 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>所以这个game.board数组</tgt>` | 1097 |

---

### Test Example 23 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1096 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이것이 기어입니다.</tgt>` | 998 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1173 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>信号が</src><tgt>기어가 헐거워지면</tgt>` | 1301 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>逆にできなくなってしまう</src><tgt><\|wait\|></tgt>` | 1584 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>場合があるので、</src><tgt>신호가 오히려 안 될 수 있으니,</tgt>` | 1592 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1729 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src><\|wait\|></src><tgt>기어 앞에는</tgt>` | 1513 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>逆ネジのナットが</src><tgt><\|wait\|></tgt>` | 1734 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>付いているっていうこと</src><tgt>역나사 너트가 붙어 있다는 뜻입니다.</tgt>` | 1206 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1177 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>네,</tgt>` | 1658 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文部材完了を</src><tgt><\|wait\|></tgt>` | 1226 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber </src><tgt><\|wait\|></tgt>` | 875 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>band, </src><tgt>고무줄처럼 늘어난 밴드처럼,</tgt>` | 1657 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1161 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | 1861 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>And when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1367 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy gets </src><tgt>그 결합이 끊어지면,</tgt>` | 1462 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to </src><tgt><\|wait\|></tgt>` | 1687 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>그 잠재 에너지는 다른 종류의 에너지로 변환됩니다.</tgt>` | 1947 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 840 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>or gets used </src><tgt>열이나 빛 같은,</tgt>` | 1915 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make different bonds </src><tgt><\|wait\|></tgt>` | 1762 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>다른 결합을 만드는 데 사용됩니다.</tgt>` | 1554 |

---

### Test Example 25 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 873 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>so here, </src><tgt>자, 여기서는</tgt>` | 1119 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>they think </src><tgt><\|wait\|></tgt>` | 1223 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>to do 7.2 GB </src><tgt>7.2GB를</tgt>` | 1169 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>already, right? </src><tgt><\|wait\|></tgt>` | 1578 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>And </src><tgt>이미 처리한다고 생각하는 거죠?</tgt>` | 1476 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1649 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>the heavy use of </src><tgt><\|wait\|></tgt>` | 1508 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the CPU </src><tgt>CPU 사용량이</tgt>` | 1473 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>will go on </src><tgt><\|wait\|></tgt>` | 803 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7.2 GB </src><tgt><\|wait\|></tgt>` | 1839 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>GB. </src><tgt>7.2GB까지 계속될 겁니다.</tgt>` | 1955 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1531 |

---

### Test Example 26 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 </src><tgt><\|wait\|></tgt>` | 999 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이것들은 </src><tgt><\|wait\|></tgt>` | 961 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유니트 링과 </src><tgt>These are essentially unit rings</tgt>` | 1756 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거는 거진 </src><tgt><\|wait\|></tgt>` | 1514 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사한 링이 </src><tgt><\|wait\|></tgt>` | 1391 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>그런 걸 굉장히 </src><tgt>and they are very similar to those rings.</tgt>` | 989 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1687 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 다모니레라 </src><tgt><\|wait\|></tgt>` | 1646 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>다기다 </src><tgt>They are all naturally</tgt>` | 1718 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>기다기다 </src><tgt><\|wait\|></tgt>` | 1875 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt>there, you know. Now,</tgt>` | 1090 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거에다가 </src><tgt><\|wait\|></tgt>` | 1075 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt>add to that,</tgt>` | 1545 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1128 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt>19차 수정헌법의 의미는</tgt>` | 1727 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1083 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore </src><tgt>그리고</tgt>` | 1049 |
| 5 | `<src>history as a guide </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>its history as a guide </src><tgt><\|wait\|></tgt>` | 1292 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help political </src><tgt>정치적</tgt>` | 1367 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change </src><tgt><\|wait\|></tgt>` | 1482 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>변화에 어떻게 도움이 되는지</tgt>` | 1668 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1527 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt>미국에서</tgt>` | 751 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1805 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, I'm </src><tgt>수정헌법의 의미를</tgt>` | 2100 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>married. </src><tgt><\|wait\|></tgt>` | 1737 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 853 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>就是是</src><tgt>二つ目は</tgt>` | 995 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二期实操，</src><tgt><\|wait\|></tgt>` | 1161 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>配副在</src><tgt>第二期の実践です。副の</tgt>` | 1308 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>一期一线</src><tgt><\|wait\|></tgt>` | 1588 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>一期一线のベテランたちとの</tgt>` | 1752 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1677 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做微信</src><tgt>戦い方、例えば</tgt>` | 1463 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好是几点，</src><tgt><\|wait\|></tgt>` | 1763 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>微信でのコミュニケーションのコツが</tgt>` | 1306 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信沟通好</src><tgt><\|wait\|></tgt>` | 1074 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>平分的兴棒</src><tgt>うまく分かれます。</tgt>` | 1889 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1668 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1016 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>啊，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1247 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1328 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是以前造成的</src><tgt>このローマでは、以前の</tgt>` | 881 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1512 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>ものではありません。</tgt>` | 1379 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1272 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>危机啊</src><tgt>今直面している</tgt>` | 1781 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟丰收</src><tgt><\|wait\|></tgt>` | 835 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是</src><tgt>危機や豊作も、</tgt>` | 1729 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间就</src><tgt><\|wait\|></tgt>` | 1863 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来</src><tgt>全く同じものではないはずです。</tgt>` | 1870 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因此会建议</src><tgt><\|wait\|></tgt>` | 1328 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>各位的朋友呢，</src><tgt>ですから、皆さんには</tgt>` | 738 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 921 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切都正常，</src><tgt>Everything was normal back then,</tgt>` | 1357 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无反应，</src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src>所以</src><tgt>no reaction at all. So</tgt>` | 987 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1645 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>切片大概</src><tgt>we stuck to the plan, didn't cut it,</tgt>` | 1694 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二位医生</src><tgt><\|wait\|></tgt>` | 1861 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>来审断，</src><tgt>and about twelve doctors came to examine it.</tgt>` | 1476 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 1752 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>The following are the ones who were dragged out,</tgt>` | 2086 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1741 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>and they were all fine,</tgt>` | 1337 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一会打开。</src><tgt><\|wait\|></tgt>` | 734 |

---

### Test Example 31 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 774 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150개 가 </src><tgt>そのうち150個は</tgt>` | 1524 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중요 범주 로 </src><tgt><\|wait\|></tgt>` | 1260 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업들이 </src><tgt>非常に小さな企業</tgt>` | 1360 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1029 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>が多いです。一般的には</tgt>` | 1503 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 2450 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>혹은 </src><tgt>成長したり、</tgt>` | 952 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>해외 뱅크에 </src><tgt><\|wait\|></tgt>` | 1788 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>거의 다는데 </src><tgt>海外銀行にほとんど入っている</tgt>` | 1946 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>이보내 성장이 </src><tgt><\|wait\|></tgt>` | 1838 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>폐업도 하지 않는 </src><tgt>この成長は</tgt>` | 1281 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 826 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 771 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>前头，</src><tgt>彼は前方に進み出た。</tgt>` | 1516 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 922 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>得到了前头之后，</src><tgt>前方に進んだら、</tgt>` | 1072 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你</src><tgt><\|wait\|></tgt>` | 1489 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>务必</src><tgt>必ず</tgt>` | 1334 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>走，不要</src><tgt><\|wait\|></tgt>` | 1424 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>想做，因为那我在</src><tgt>走ってくれ。そうしないと、</tgt>` | 2029 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续操作</src><tgt><\|wait\|></tgt>` | 1674 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>私は操作を続けられないからね。</tgt>` | 744 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1742 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt>なぜなら、</tgt>` | 1707 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？因为呢，</src><tgt><\|wait\|></tgt>` | 1424 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt>なぜそんな言い方をするのか？だって、</tgt>` | 856 |

---

### Test Example 33 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 965 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手</src><tgt>由于</tgt>` | 996 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>とかだと</src><tgt><\|wait\|></tgt>` | 1080 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt>一二手车，</tgt>` | 1048 |
| 5 | `<src>まあ</src><tgt>差不多十秒。</tgt>` | `<src>10秒で</src><tgt><\|wait\|></tgt>` | 1289 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ1秒に</src><tgt>大概10秒，</tgt>` | 1404 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 828 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>セタンすかね</src><tgt>大概一秒钟</tgt>` | 1879 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1270 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt>左右吧。</tgt>` | 1299 |
| 11 | `<src>おそらく</src><tgt>然后</tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 915 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11二手</src><tgt>而且大概</tgt>` | 1900 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1753 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>11二手车，</tgt>` | 1223 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合う馬とかが</src><tgt><\|wait\|></tgt>` | 831 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから</src><tgt>所以，</tgt>` | 984 |

---

### Test Example 34 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1058 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어차피 보면 </src><tgt>反正</tgt>` | 811 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1225 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt>看，</tgt>` | 914 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이런 인생 이자 </src><tgt><\|wait\|></tgt>` | 1489 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt>人生就是和20代一起走过的，</tgt>` | 1644 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1199 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt>所以，</tgt>` | 1221 |
| 9 | `<src><\|wait\|></src><tgt>所以</tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1269 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인감모다는 </src><tgt>在再因感模道</tgt>` | 1755 |
| 11 | `<src>조금 </src><tgt>比起责任感，</tgt>` | `<src>조금은 자기 스스로 </src><tgt><\|wait\|></tgt>` | 677 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt>稍微有点</tgt>` | 1673 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1793 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>정 많은 거 </src><tgt><\|wait\|></tgt>` | 1106 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>自己做点事，</tgt>` | 968 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 </src><tgt><\|wait\|></tgt>` | 1056 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new </src><tgt><\|wait\|></tgt>` | 904 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src>there </src><tgt><\|wait\|></tgt>` | 996 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>was such </src><tgt>没什么新奇的，</tgt>` | 1362 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>interest before. </src><tgt><\|wait\|></tgt>` | 1031 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Net future </src><tgt>之前就有这样的兴趣。</tgt>` | 1597 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>TC </src><tgt><\|wait\|></tgt>` | 1379 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>there. </src><tgt>NetfutureTC。</tgt>` | 1648 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>So this is just </src><tgt><\|wait\|></tgt>` | 1623 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt>所以这只是</tgt>` | 1112 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>to look at </src><tgt><\|wait\|></tgt>` | 1216 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src>what </src><tgt><\|wait\|></tgt>` | 1762 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>dev </src><tgt>一个地方</tgt>` | 1748 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>ops or engineers </src><tgt><\|wait\|></tgt>` | 501 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>would like to be </src><tgt><\|wait\|></tgt>` | 1691 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt>让DevOps或工程师了解一下。</tgt>` | 1130 |

---

### Test Example 36 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 976 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt>あるいは、何か書いたものを</tgt>` | 1562 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 852 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt>書いたり、テキストを作成したりする場合、</tgt>` | 1746 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1436 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1854 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the word. It's like, oh, </src><tgt>単語のスペルが全くわからないことに気づく。なんていうか、「あ、</tgt>` | 2725 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 796 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>starts with a </src><tgt><\|wait\|></tgt>` | 1880 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>double p, </src><tgt>この単語は「double p」で始まる</tgt>` | 1999 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double l, </src><tgt><\|wait\|></tgt>` | 1713 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>I don't know. </src><tgt>double l、なんていうか、</tgt>` | 1203 |

---

### Test Example 37 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>帝僵的部分</src><tgt><\|wait\|></tgt>` | 810 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>我们看到的是</src><tgt>우리가 본 것은</tgt>` | 1225 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 987 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>戴旧的人，但是</src><tgt>낡은 사람입니다. 하지만</tgt>` | 1221 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于</src><tgt><\|wait\|></tgt>` | 1509 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src>逆向的，</src><tgt>그는 역방향적입니다.</tgt>` | 1647 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这种像一个</src><tgt><\|wait\|></tgt>` | 1719 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>庄观的修者</src><tgt>이런 종류의</tgt>` | 1653 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>去特别注意</src><tgt><\|wait\|></tgt>` | 1698 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是它能不能</src><tgt>장관의 수행자들은 특별히 주의해야 합니다. 그들이</tgt>` | 2148 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到与</src><tgt><\|wait\|></tgt>` | 1782 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>他掉不到</src><tgt>그것을</tgt>` | 885 |
| 13 | `<src><\|wait\|></src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>与他的意识</src><tgt><\|wait\|></tgt>` | 1177 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>了。</src><tgt>그의 의식에 닿을 수 있는지</tgt>` | 1140 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1082 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>まさに今、</tgt>` | 1011 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1211 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1137 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and that ten of them </src><tgt>やるべき人がいる</tgt>` | 1712 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 1426 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>その10個が本当に重要だという</tgt>` | 2258 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>um </src><tgt><\|wait\|></tgt>` | 1041 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt>ことをやります。</tgt>` | 1710 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 690 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1676 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at that. </src><tgt>1分程度の動画を撮ります。</tgt>` | 1909 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It'll cover each one. </src><tgt><\|wait\|></tgt>` | 1759 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>And a little more </src><tgt>それぞれをカバーします。もう少し</tgt>` | 944 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>detail, </src><tgt><\|wait\|></tgt>` | 344 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 783 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알고 있나요? </src><tgt>知っていますか？</tgt>` | 1367 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1453 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>ここに異邦人として</tgt>` | 1590 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1034 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>言葉を失う</tgt>` | 1210 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그리는 그대로 </src><tgt><\|wait\|></tgt>` | 1701 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>끌려 갔느라 </src><tgt>ままに連れて行かれ、</tgt>` | 1700 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그럼 </src><tgt><\|wait\|></tgt>` | 1636 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그럼으로 내가 </src><tgt>その結果、</tgt>` | 900 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1423 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리노니 </src><tgt>あなたたちに</tgt>` | 1818 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영으로 </src><tgt><\|wait\|></tgt>` | 1599 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>神の霊で語る者は</tgt>` | 616 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 823 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 884 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个餐饮可以说是</src><tgt>餐饮に関しては、</tgt>` | 1085 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1386 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分</src><tgt>かなり良いと言えますが、</tgt>` | 1128 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1476 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>以及在事业方面的</src><tgt>事業的な側面や</tgt>` | 1507 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长的红利</src><tgt><\|wait\|></tgt>` | 1866 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>以及收入的提升</src><tgt>業績増加の恩恵、収入の増加、</tgt>` | 1678 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 1618 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>在投资理财方面</src><tgt>投資や資産運用に関しては、</tgt>` | 1945 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 474 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>今月も良いですが、</tgt>` | 1783 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说就</src><tgt><\|wait\|></tgt>` | 1655 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>稍微弱了</src><tgt>少し弱まったと言っても</tgt>` | 1077 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一点点。</src><tgt><\|wait\|></tgt>` | 775 |

---

### Test Example 41 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 775 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt>哦，</tgt>` | 1021 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Hiemel이라고 하는 </src><tgt><\|wait\|></tgt>` | 1438 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터도 </src><tgt>Hiemel</tgt>` | 987 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있고 </src><tgt><\|wait\|></tgt>` | 1626 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람도 </src><tgt>也能理解，</tgt>` | 1384 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있는 </src><tgt><\|wait\|></tgt>` | 1866 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터의 언어에 </src><tgt>也能理解计算机的语言，</tgt>` | 1716 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1705 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법이 맞게 </src><tgt>语法正确，</tgt>` | 1904 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>우리가 이제 그것들을 </src><tgt><\|wait\|></tgt>` | 506 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>我们现在需要编写这些，</tgt>` | 1798 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그것들을 </src><tgt><\|wait\|></tgt>` | 1659 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1081 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt>需要编写程序来编写它们。</tgt>` | 893 |

---

### Test Example 42 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1145 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>세인바라 </src><tgt>目を閉じて、</tgt>` | 1004 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌고야 </src><tgt><\|wait\|></tgt>` | 1154 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>이제 내 소름이 </src><tgt>今、</tgt>` | 1237 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 차리도 돋은 </src><tgt><\|wait\|></tgt>` | 1700 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>내 기미엄이야 </src><tgt>背筋がぞくぞくするような、</tgt>` | 1818 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들어서 </src><tgt><\|wait\|></tgt>` | 2012 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうっていうんだ。</tgt>` | 1207 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1664 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>엄밀히 </src><tgt>気心は</tgt>` | 1900 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>풀릴 거고 </src><tgt><\|wait\|></tgt>` | 580 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>이젠 엄밀히 안 지켜줄 거고 </src><tgt>完全に解けるし、もう厳密には守ってくれないんだ。</tgt>` | 2203 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1193 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 마음 에. </src><tgt>だから、心置きなく。</tgt>` | 1129 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 803 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational </src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>containment. How far </src><tgt>교육적 격리. 얼마나 멀리</tgt>` | 1160 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1225 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt>진짜로</tgt>` | 1038 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1560 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt>교육을 받았나요? 고등학교를 졸업했나요?</tgt>` | 1685 |
| 7 | `<src><\|wait\|></src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 2023 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>containment. Did you </src><tgt>그게 한 단계의 격리입니다. </tgt>` | 1568 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>go to college, </src><tgt><\|wait\|></tgt>` | 1675 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and so did you graduate </src><tgt>대학까지 갔나요? 그리고</tgt>` | 1996 |
| 11 | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>that's another level of </src><tgt><\|wait\|></tgt>` | 1842 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>containment. </src><tgt>그게 또 다른 단계의 격리입니다.</tgt>` | 1673 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for now. </src><tgt>지금까지는 여기까지입니다.</tgt>` | 711 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 775 |
| 15 | `<src>online. </src><tgt>오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 829 |

---

### Test Example 44 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 996 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和关于</src><tgt>伝聞によると、</tgt>` | 1107 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>针对对手的感情</src><tgt><\|wait\|></tgt>` | 1384 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真实意图的。</src><tgt>相手の感情や真意に関するものがあります。</tgt>` | 1298 |
| 5 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1326 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くは</tgt>` | 1286 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1540 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说，</src><tgt>人々がそう言うのを</tgt>` | 1770 |
| 9 | `<src>这样说：“</src><tgt>よく耳にするのが</tgt>` | `<src>啊。</src><tgt><\|wait\|></tgt>` | 1191 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看。</src><tgt>よく聞きますね。</tgt>` | 1119 |
| 11 | `<src>这个人</src><tgt>「ほら、</tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1777 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>躲黄了。</src><tgt>この人はまた逃げているようです。</tgt>` | 1918 |
| 13 | `<src>他的眼睛</src><tgt>また嘘をついている。目が</tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1212 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt>目は全てを物語っています。</tgt>` | 851 |
| 15 | `<src><\|wait\|></src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1001 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 718 |
| 17 | `<src><\|wait\|></src><tgt>つまり…</tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 620 |

---

### Test Example 45 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>濡らせてやれ</src><tgt>그렇다면 그냥 젖게 해버려.</tgt>` | 1761 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1079 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>は</src><tgt>나는</tgt>` | 928 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>火事を見ている</src><tgt><\|wait\|></tgt>` | 1341 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>불을 보고 있는 거야.</tgt>` | 1481 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1641 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超に超えてる</src><tgt>한계가 이미</tgt>` | 1602 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不滅の奇跡よ。</src><tgt><\|wait\|></tgt>` | 1698 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>초월했어. 불멸의 기적이라고.</tgt>` | 904 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1555 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>のぶなデイコを</src><tgt>오랫동안</tgt>` | 1893 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってる</src><tgt><\|wait\|></tgt>` | 1702 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt>노부나 데이코를 하고 있는데, 나는 이렇게</tgt>` | 1136 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい快族線を見た</src><tgt><\|wait\|></tgt>` | 818 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt>대단한 쾌속선을 본 적이 없어.</tgt>` | 823 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 924 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인증 상승 하는 </src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인다면 </src><tgt>If the stock index is rising,</tgt>` | 1698 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주도 </src><tgt><\|wait\|></tgt>` | 1697 |
| 5 | `<src>큰 폭의 </src><tgt>these large- cap stocks</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1024 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 상승 을 하겠지만 </src><tgt>large-cap stocks will also see a significant rise,</tgt>` | 2008 |
| 7 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1646 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 1014 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1665 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt>but first, the most volatile stocks</tgt>` | 1997 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1916 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1449 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시총이 </src><tgt>move the market first, so the market cap</tgt>` | 874 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 온종목 을 </src><tgt><\|wait\|></tgt>` | 815 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 같습니다. </src><tgt>is something to keep an eye on.</tgt>` | 977 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 486 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 928 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>then </src><tgt><\|wait\|></tgt>` | 1020 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self defining </src><tgt>アクティビティ、次に自己定義</tgt>` | 1601 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>what we think the standard is because you're </src><tgt><\|wait\|></tgt>` | 1046 |
| 5 | `<src>absolutely correct, </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>absolutely correct </src><tgt>の基準を考えているんです。なぜなら、</tgt>` | 1909 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1074 |
| 7 | `<src>is is that </src><tgt>しかし現実には、</tgt>` | `<src>is that </src><tgt>現実には、</tgt>` | 1712 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid </src><tgt><\|wait\|></tgt>` | 1662 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the block </src><tgt>ブロックの新しい子だから、</tgt>` | 1790 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed </src><tgt><\|wait\|></tgt>` | 1923 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>from </src><tgt>基準が変わったから、</tgt>` | 1523 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt><\|wait\|></tgt>` | 665 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt>20年前から、</tgt>` | 1729 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard because </src><tgt><\|wait\|></tgt>` | 1019 |
| 15 | `<src>everything at this point is being </src><tgt>より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>everything at this point </src><tgt>今の基準に縛られているんです。なぜなら、</tgt>` | 998 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to our standard </src><tgt><\|wait\|></tgt>` | 771 |

---

### Test Example 48 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 790 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>the sorts </src><tgt>모든 종류의</tgt>` | 1005 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>that are </src><tgt><\|wait\|></tgt>` | 1107 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>not </src><tgt>그것들은</tgt>` | 1075 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>among us </src><tgt><\|wait\|></tgt>` | 1061 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>in the sense of </src><tgt>우리 중</tgt>` | 1055 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>love. </src><tgt><\|wait\|></tgt>` | 1193 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src>We also </src><tgt>사랑이라는 관점에서</tgt>` | 1569 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>can also </src><tgt><\|wait\|></tgt>` | 1479 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>enter into </src><tgt>들어갈 수 있습니다.</tgt>` | 992 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the state of </src><tgt><\|wait\|></tgt>` | 1382 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>being in love. </src><tgt>사랑에 빠진 상태도요.</tgt>` | 1957 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It's all </src><tgt><\|wait\|></tgt>` | 1790 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>come to be </src><tgt>모든 것이</tgt>` | 1251 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that sort of </src><tgt><\|wait\|></tgt>` | 813 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>the whole thing. </src><tgt>그렇게 되는 겁니다.</tgt>` | 1055 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt><\|wait\|></tgt>` | 838 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>to evolve. </src><tgt>계속 진화하고 있죠.</tgt>` | 764 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 1021 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>And this is the visual development environment</tgt>` | 1438 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうだけじゃなくて</src><tgt><\|wait\|></tgt>` | 1144 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt>not just that. Visual Python</tgt>` | 879 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1555 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt>development environment.</tgt>` | 1343 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアル</src><tgt><\|wait\|></tgt>` | 1313 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>の書いてあとそれは</src><tgt>Also, you can write flow graphs in Visual Graph, and that's</tgt>` | 2329 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードなんそっから生成される</src><tgt><\|wait\|></tgt>` | 1873 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつやそれが実行</src><tgt>Python code that gets generated from there, or that runs.</tgt>` | 2151 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>することで信号処理</src><tgt><\|wait\|></tgt>` | 1767 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>That's how signal processing is done.</tgt>` | 1806 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>いうことになっているから</src><tgt><\|wait\|></tgt>` | 1067 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt>That's why it's set up that way.</tgt>` | 906 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 650 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ</src><tgt>Okay.</tgt>` | 430 |

---

### Test Example 50 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1132 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 해매 니다. </src><tgt>进去的时候，我非常困惑。</tgt>` | 1734 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>이 운전 을 </src><tgt><\|wait\|></tgt>` | 1162 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt>因为我之前开车</tgt>` | 1504 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1147 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있으면 그 강북 </src><tgt>走走来来，</tgt>` | 1170 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>으로 가면 </src><tgt><\|wait\|></tgt>` | 1748 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 </src><tgt>如果去江南区，</tgt>` | 1530 |
| 9 | `<src><\|wait\|></src><tgt>就不用说了，去外国</tgt>` | `<src>외국 엑이 나가면 또 장려 리요. </src><tgt><\|wait\|></tgt>` | 2019 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt>外国人去那儿，那也是鼓励。我</tgt>` | 2058 |
| 11 | `<src>좀 창피 하네요. </src><tgt>就更惨了。真有点丢人。</tgt>` | `<src>진짜 아니요. </src><tgt><\|wait\|></tgt>` | 1814 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt>真的不是。不如</tgt>` | 1704 |
| 13 | `<src>이제 </src><tgt>不过，</tgt>` | `<src>이제 열심히 </src><tgt><\|wait\|></tgt>` | 1028 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>노가요. </src><tgt>现在努力工作吧。</tgt>` | 813 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 아닌 거 같아요. </src><tgt><\|wait\|></tgt>` | 684 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>예. </src><tgt>我觉得不是。对。</tgt>` | 557 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 750 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람들이 </src><tgt>そして、多くの人が</tgt>` | 973 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1596 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 </src><tgt>分析をしています。ここで</tgt>` | 857 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자입을 분석을 보시면 </src><tgt><\|wait\|></tgt>` | 1971 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ロクジャイを分析すると、ソニーが</tgt>` | 1700 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이오렉트의 </src><tgt><\|wait\|></tgt>` | 1782 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FPP 파이프를 </src><tgt>I-O-RECTのFPPパイプを</tgt>` | 1479 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1607 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>낮추어서 로포인다. </src><tgt>128ビットに下げてローフォインダ。</tgt>` | 2131 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 1765 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt>Xboxにもない</tgt>` | 1685 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1078 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>S2가 </src><tgt>Infinity Cache S2が</tgt>` | 813 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>여기도 없다. </src><tgt><\|wait\|></tgt>` | 665 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>ここにもありません。</tgt>` | 554 |

---

### Test Example 52 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>だから、もちろん</tgt>` | 1114 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1745 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>こういうケースもあります。Aという人と</tgt>` | 1916 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 1267 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 컨택 에요. </src><tgt>Bという人がコンタクトを取るんです。</tgt>` | 1602 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>B가 컨설턴트 </src><tgt><\|wait\|></tgt>` | 1948 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>여 가지고 A라는 </src><tgt>Bがコンサルタントで、Aという</tgt>` | 1721 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 674 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>人が悪性コードを</tgt>` | 2015 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>저었을 때 </src><tgt><\|wait\|></tgt>` | 1841 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt>書いたとき、Bという人が</tgt>` | 1770 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1028 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크로사이트 스크립트에서 </src><tgt>実際、Cross-Site Scriptで</tgt>` | 840 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>XSP까지 </src><tgt><\|wait\|></tgt>` | 651 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까? </src><tgt>感染する可能性があるか？</tgt>` | 599 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 967 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>also, you will not </src><tgt>另外，</tgt>` | 1135 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1334 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>media objects </src><tgt>您将无法移动媒体对象，</tgt>` | 1003 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1504 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt>在资源之间</tgt>` | 1368 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>either, if </src><tgt><\|wait\|></tgt>` | 1266 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into the </src><tgt>或者</tgt>` | 1706 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation where you </src><tgt><\|wait\|></tgt>` | 913 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt>您发现</tgt>` | 1752 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1856 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular </src><tgt>将错误的媒体文件添加到了某个特定</tgt>` | 1963 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource. Now, </src><tgt><\|wait\|></tgt>` | 1500 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt>资源中。现在，</tgt>` | 672 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>giving those media files </src><tgt><\|wait\|></tgt>` | 895 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>and then making sure </src><tgt>我们来看看这些媒体文件，然后确保</tgt>` | 908 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 639 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>它们被正确备份。</tgt>` | 436 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 841 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼は</tgt>` | 1159 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a hungry </src><tgt><\|wait\|></tgt>` | 1208 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>and he knows that he's </src><tgt>イエスが飢えていることを知っている。そして、</tgt>` | 1650 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>is not that </src><tgt><\|wait\|></tgt>` | 1048 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>food in the wilderness </src><tgt>荒野で食料がないことを知っている。</tgt>` | 1624 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>today, is that he's hungry, </src><tgt><\|wait\|></tgt>` | 2409 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>and so he says to </src><tgt>そして彼は</tgt>` | 1027 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, "If </src><tgt><\|wait\|></tgt>` | 1732 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>the Son of God </src><tgt>イエスよ、</tgt>` | 1894 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>proved it, turn </src><tgt><\|wait\|></tgt>` | 1781 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>these stones to bread, </src><tgt>この石をパンに変えなさい。この石を</tgt>` | 1655 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>how did Jesus </src><tgt><\|wait\|></tgt>` | 513 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>deal with that </src><tgt>どうやって</tgt>` | 999 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation?" </src><tgt><\|wait\|></tgt>` | 842 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>Man, </src><tgt>その誘惑に対処したのか、と尋ねたんだ。</tgt>` | 847 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>genuinely </src><tgt><\|wait\|></tgt>` | 354 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>by prayer alone. </src><tgt>本当に祈りだけで。</tgt>` | 413 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1244 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1024 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>最初のセクションで少し間違っていました。</tgt>` | 1721 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1305 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1219 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt>AHRフィールドの重要性について</tgt>` | 1388 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance versus </src><tgt><\|wait\|></tgt>` | 1759 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>some </src><tgt>ある</tgt>` | 1162 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 1039 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt>バリアントデータベースが</tgt>` | 1363 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1943 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt>私の好きなものの一つです。つまり、</tgt>` | 1906 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>if we don't agree </src><tgt><\|wait\|></tgt>` | 1721 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1018 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt>これらのフィールドについて合意しないと、</tgt>` | 906 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 699 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>that we can draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 521 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt>これらのデータソースから情報を引き出すことができませんよね？</tgt>` | 613 |
| 19 | `<src><\|wait\|></src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 345 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1124 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src><\|wait\|></src><tgt>有意义的</tgt>` | 828 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1126 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>个人权利，</tgt>` | 990 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I I I don't I don't </src><tgt>而最高法院最后才加入，不是领导者。我我我</tgt>` | 2253 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>have the courts want to be </src><tgt><\|wait\|></tgt>` | 1946 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt>不希望法院</tgt>` | 1341 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of social change </src><tgt><\|wait\|></tgt>` | 1703 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>成为社会变革的先锋。</tgt>` | 714 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 1756 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt>但他们</tgt>` | 1733 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1309 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 733 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt>反映的是已经</tgt>` | 1045 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged </src><tgt><\|wait\|></tgt>` | 839 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>soom. </src><tgt>形成的共识。</tgt>` | 719 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 375 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt>你有一些联邦法官</tgt>` | 467 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 402 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 319 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 950 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>一下</src><tgt>그럼</tgt>` | 985 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 1256 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分</src><tgt>그림 부분을 한번 볼게요.</tgt>` | 1147 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个</src><tgt><\|wait\|></tgt>` | 1554 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>是客亭的部分，</src><tgt>객정 부분도 보이고,</tgt>` | 1477 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>而客亭一般</src><tgt><\|wait\|></tgt>` | 1667 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>就是属于</src><tgt>객정은 보통</tgt>` | 1547 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1039 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>在休息的地方</src><tgt>휴식하는 곳에</tgt>` | 1339 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>啊，所以呢，</src><tgt><\|wait\|></tgt>` | 1858 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分</src><tgt>있습니다. 그래서</tgt>` | 1845 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1431 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>我们需要</src><tgt>몸의 부분은</tgt>` | 622 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>给自己一点时间</src><tgt><\|wait\|></tgt>` | 989 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>好好地</src><tgt>잠시 시간을 내서</tgt>` | 783 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt><\|wait\|></tgt>` | 622 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们看到</src><tgt>쉬고 쉬는 게 필요하다는 뜻입니다. 그리고</tgt>` | 600 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是包含五一人的嘛。</src><tgt><\|wait\|></tgt>` | 480 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt>여기에는 51명이 포함되어 있습니다.</tgt>` | 426 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以也是说</src><tgt><\|wait\|></tgt>` | 347 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 817 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>この人々は全く珍しい</tgt>` | 1327 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up to </src><tgt>ことが多く、</tgt>` | 935 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize </src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>the world. </src><tgt>世界を完全に変革します。</tgt>` | 1439 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>personality is </src><tgt>その個性は</tgt>` | 1617 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 920 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾したものです。</tgt>` | 1572 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1874 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的である一方で、</tgt>` | 1958 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1254 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 814 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 1003 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>it gets straight to the </src><tgt>そして</tgt>` | 854 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt>本題に入ります。</tgt>` | 737 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 412 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt>彼らはまた</tgt>` | 493 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 377 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt>逆説を唱え、</tgt>` | 400 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate </src><tgt><\|wait\|></tgt>` | 327 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>議論から逃げません。</tgt>` | 334 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in and CP stands </src><tgt><\|wait\|></tgt>` | 364 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>for. </src><tgt>CPを支持しています。</tgt>` | 358 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이전 </src><tgt><\|wait\|></tgt>` | 890 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>성공 을 경험 을 </src><tgt><\|wait\|></tgt>` | 1189 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>한 명분 이 후부 를 </src><tgt>The previous successful person</tgt>` | 1572 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1333 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후부의 당수를 </src><tgt><\|wait\|></tgt>` | 1263 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 하면서 </src><tgt>while also pursuing the position of the second- in-line</tgt>` | 1807 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색 까지 </src><tgt><\|wait\|></tgt>` | 1682 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제는 </src><tgt>and even made a show of it, but now</tgt>` | 1337 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤성률 후보 가 </src><tgt><\|wait\|></tgt>` | 1722 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정일 을 </src><tgt><\|wait\|></tgt>` | 1929 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제관 순간 </src><tgt>candidate Yoon Sung-ryul</tgt>` | 1812 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석 은 들으 내놓고 </src><tgt><\|wait\|></tgt>` | 1533 |
| 13 | `<src><\|wait\|></src><tgt>Lee Jun -seok</tgt>` | `<src>윤성률 후보 </src><tgt><\|wait\|></tgt>` | 560 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt>is putting Yoon Sung-ryul out of the running</tgt>` | 1377 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼 를 품은 </src><tgt><\|wait\|></tgt>` | 541 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 682 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt>with a hatchet in his hand, showing an aggressive stance</tgt>` | 651 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 317 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt>that he's determined to do.</tgt>` | 384 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가 신발 </src><tgt><\|wait\|></tgt>` | 283 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 성상 납권 </src><tgt><\|wait\|></tgt>` | 387 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>가. </src><tgt>The shoe-shaped seal of former President Lee Jun-seok.</tgt>` | 371 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 339 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 에 얼마나 </src><tgt><\|wait\|></tgt>` | 355 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재입니까? </src><tgt>How big of a boon is this for the Democratic Party's attack?</tgt>` | 406 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1022 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt>Well, right now after dinner,</tgt>` | 1051 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt><\|wait\|></tgt>` | 1323 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt>I want to make something for it.</tgt>` | 1096 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1521 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ゴルフスローンホテルも</src><tgt>So, this Golf Sloan Hotel,</tgt>` | 1608 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる</src><tgt><\|wait\|></tgt>` | 1897 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>場所になってる</src><tgt>is a place where you can have breakfast,</tgt>` | 1623 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってる</src><tgt><\|wait\|></tgt>` | 1694 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>ので今後ね</src><tgt>so I'm planning to go there later.</tgt>` | 1927 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルフスローンホテル</src><tgt><\|wait\|></tgt>` | 1724 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>I'd like to stay at the Golf Sloan Hotel</tgt>` | 895 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt><\|wait\|></tgt>` | 1341 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt>if you're considering it,</tgt>` | 1089 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>thinking about staying here in the future,</tgt>` | `<src>見てみて、まあいいんじゃない</src><tgt><\|wait\|></tgt>` | 822 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt>and think it's a good idea,</tgt>` | 802 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>はい思います。</src><tgt><\|wait\|></tgt>` | 394 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt>I think so. From this hotel,</tgt>` | 524 |
| 19 | `<src>駅ももう</src><tgt>From this hotel,</tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 358 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>you can walk to Busan Station,</tgt>` | 400 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 348 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんな </src><tgt>it only takes a minute,</tgt>` | 342 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>かそんなレベルのね</src><tgt><\|wait\|></tgt>` | 379 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいねまあホテル</src><tgt>you know, the location is pretty good,</tgt>` | 404 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 258 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>so if you're interested,</tgt>` | 222 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 201 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それなら</src><tgt>please consider it. If that's the case,</tgt>` | 251 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt><\|wait\|></tgt>` | 200 |
