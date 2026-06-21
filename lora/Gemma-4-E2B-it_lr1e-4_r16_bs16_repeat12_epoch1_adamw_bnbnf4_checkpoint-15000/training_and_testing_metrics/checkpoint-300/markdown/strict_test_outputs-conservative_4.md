# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9554
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.1457
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 8
  - TARGET_METRICS_FILTERED_TURN_COUNT: 123
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 52
  - TGT_RELEASE_ACCURACY: 0.0000
  - TGT_RELEASE_TOTAL: 131
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 614
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1262.9290
  - PROCESS_TIME_MS_P50: 1226.3160
  - PROCESS_TIME_MS_P95: 2199.0390
  - PROCESS_TIME_MS_MAX: 11668.8850

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
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>的宿舍里，</src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个房间</src><tgt><\|wait\|></tgt>` | 1206 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>又很大，</src><tgt><\|wait\|></tgt>` | 1043 |
| 5 | `<src><\|wait\|></src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1063 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 847 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 1347 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>下课人。</src><tgt><\|wait\|></tgt>` | 1767 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>在宿舍里</src><tgt><\|wait\|></tgt>` | 1041 |
| 10 | `<src>这种核桃</src><tgt>Then, I'll add some walnut kernels— this kind of</tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1620 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 1213 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 872 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 988 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | 1154 |
| 5 | `<src>爱浇水、</src><tgt>What parents need to do is this:</tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 622 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 1424 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>去阻止孩子</src><tgt><\|wait\|></tgt>` | 1393 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心瘾</src><tgt><\|wait\|></tgt>` | 1797 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>影响</src><tgt><\|wait\|></tgt>` | 954 |
| 10 | `<src>并耐心等待孩子</src><tgt>water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for</tgt>` | `<src>你的孩子慢慢</src><tgt><\|wait\|></tgt>` | 1683 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>长大。</src><tgt><\|wait\|></tgt>` | 1276 |

---

### Test Example 3 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>明天这个情况</src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 699 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1276 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就是感谢的回复主管</src><tgt><\|wait\|></tgt>` | 1217 |
| 5 | `<src>或是通知对方，</src><tgt>In this situation, when we encounter a problem, we should</tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1188 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>要一下这个状况</src><tgt><\|wait\|></tgt>` | 899 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1234 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>怎么都把它</src><tgt><\|wait\|></tgt>` | 2278 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>扛下来，</src><tgt><\|wait\|></tgt>` | 1620 |
| 10 | `<src>整体而言，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall,</tgt>` | `<src>扛得住，</src><tgt><\|wait\|></tgt>` | 1003 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是</src><tgt><\|wait\|></tgt>` | 2018 |

---

### Test Example 4 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘纱完以后</src><tgt><\|wait\|></tgt>` | 1166 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 795 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>的液体检清</src><tgt><\|wait\|></tgt>` | 1248 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 1194 |
| 5 | `<src>然后</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、</tgt>` | `<src>刷了，然后就</src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>去填充在</src><tgt><\|wait\|></tgt>` | 1168 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 690 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态</src><tgt><\|wait\|></tgt>` | 2312 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态。</src><tgt><\|wait\|></tgt>` | 1677 |
| 10 | `<src>这就是所谓的</src><tgt>比較的低エネルギーの状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1154 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>的</src><tgt><\|wait\|></tgt>` | 1826 |

---

### Test Example 5 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要</src><tgt><\|wait\|></tgt>` | 946 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>气守</src><tgt><\|wait\|></tgt>` | 864 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>是容易的，但是</src><tgt><\|wait\|></tgt>` | 1362 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有</src><tgt><\|wait\|></tgt>` | 1145 |
| 5 | `<src><\|wait\|></src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1188 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>师父</src><tgt><\|wait\|></tgt>` | 861 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>只出</src><tgt><\|wait\|></tgt>` | 1139 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>于中天，</src><tgt><\|wait\|></tgt>` | 2385 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1597 |
| 10 | `<src>要成为</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>师父还</src><tgt><\|wait\|></tgt>` | 790 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师父。</src><tgt><\|wait\|></tgt>` | 2332 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 935 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 1218 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 </src><tgt><\|wait\|></tgt>` | 1129 |
| 5 | `<src>옹심이가 </src><tgt>I'm having the ongsimi and kal- ongsimi—</tgt>` | `<src>봉심이가 </src><tgt><\|wait\|></tgt>` | 1165 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>서커시 </src><tgt><\|wait\|></tgt>` | 928 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>근데 서커시 </src><tgt><\|wait\|></tgt>` | 1311 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>근데 </src><tgt><\|wait\|></tgt>` | 2245 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>아 진짜 이거 </src><tgt><\|wait\|></tgt>` | 1612 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover,</tgt>` | `<src>행으로 </src><tgt><\|wait\|></tgt>` | 1003 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽기 </src><tgt><\|wait\|></tgt>` | 2136 |

---

### Test Example 7 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 751 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの、特に</src><tgt><\|wait\|></tgt>` | 958 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>中まだ1年</src><tgt><\|wait\|></tgt>` | 1298 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>生ですからね。</src><tgt><\|wait\|></tgt>` | 1205 |
| 5 | `<src>この時点で</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>はい、その時点で</src><tgt><\|wait\|></tgt>` | 1450 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1316 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>四角線で</src><tgt><\|wait\|></tgt>` | 1343 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1328 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>対数してい</src><tgt><\|wait\|></tgt>` | 1598 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>上げる</src><tgt><\|wait\|></tgt>` | 831 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>と10年経っても</src><tgt><\|wait\|></tgt>` | 2375 |

---

### Test Example 8 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying</src><tgt><\|wait\|></tgt>` | 839 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research</src><tgt><\|wait\|></tgt>` | 827 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely happy</src><tgt><\|wait\|></tgt>` | 1267 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>people. This is</src><tgt><\|wait\|></tgt>` | 1046 |
| 5 | `<src>This is tip of the stem </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは</tgt>` | `<src>tip of the stem, </src><tgt><\|wait\|></tgt>` | 1308 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking </src><tgt><\|wait\|></tgt>` | 839 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>at 10% </src><tgt><\|wait\|></tgt>` | 1398 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 2262 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people out. </src><tgt><\|wait\|></tgt>` | 1742 |
| 10 | `<src>out there, </src><tgt>最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>People that </src><tgt><\|wait\|></tgt>` | 1234 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1875 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 814 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 872 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>apple, </src><tgt><\|wait\|></tgt>` | 1270 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>축 썰기 고. </src><tgt><\|wait\|></tgt>` | 1225 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1248 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>자신의 모로 조깅 </src><tgt><\|wait\|></tgt>` | 1043 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1022 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2299 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 1844 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대들이 </src><tgt><\|wait\|></tgt>` | 1436 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1585 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 864 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの、いただく</src><tgt><\|wait\|></tgt>` | 1070 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>というようなものも用意しております。</src><tgt><\|wait\|></tgt>` | 1195 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 1135 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 894 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1320 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります。</src><tgt><\|wait\|></tgt>` | 1976 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと、</src><tgt><\|wait\|></tgt>` | 757 |
| 10 | `<src><\|wait\|></src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src>連絡</src><tgt><\|wait\|></tgt>` | 1636 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>の連絡網がありますので、</src><tgt><\|wait\|></tgt>` | 1452 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1618 |

---

### Test Example 11 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>lastly, </src><tgt><\|wait\|></tgt>` | 884 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat, </src><tgt><\|wait\|></tgt>` | 1069 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>learners to repeat </src><tgt><\|wait\|></tgt>` | 1195 |
| 5 | `<src>Find what you're good at </src><tgt>最后，要重复。学会不断重复。找到你的长处，</tgt>` | `<src>find out you're good at </src><tgt><\|wait\|></tgt>` | 1456 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1049 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good </src><tgt><\|wait\|></tgt>` | 1259 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>yet, get to people </src><tgt><\|wait\|></tgt>` | 2175 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1766 |
| 10 | `<src><\|wait\|></src><tgt>多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1302 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>in tell next time, </src><tgt><\|wait\|></tgt>` | 1830 |

---

### Test Example 12 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단에 있는 </src><tgt><\|wait\|></tgt>` | 1304 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스들은 </src><tgt><\|wait\|></tgt>` | 812 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1227 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능이 높지 </src><tgt><\|wait\|></tgt>` | 1351 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1451 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1518 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스들이 </src><tgt><\|wait\|></tgt>` | 2148 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>있었기 때문입니다. </src><tgt><\|wait\|></tgt>` | 730 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1609 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 2505 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>모을 랐던 </src><tgt><\|wait\|></tgt>` | 567 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1199 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 970 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1171 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オーサーロカタが</src><tgt><\|wait\|></tgt>` | 1325 |
| 5 | `<src>多いですね。</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。</tgt>` | `<src>やっぱり多いですね。</src><tgt><\|wait\|></tgt>` | 1396 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | 1375 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ引っ越したい方</src><tgt><\|wait\|></tgt>` | 1549 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 1168 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>いいですね。</src><tgt><\|wait\|></tgt>` | 1589 |
| 10 | `<src>全部ちょっと次の投資</src><tgt>想创业的人自我意识都很强，而且</tgt>` | `<src>でもっと本音で</src><tgt><\|wait\|></tgt>` | 1002 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>本音で</src><tgt><\|wait\|></tgt>` | 2067 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なるので</src><tgt><\|wait\|></tgt>` | 1201 |

---

### Test Example 14 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 698 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>saying, "Drop pin your body </src><tgt><\|wait\|></tgt>` | 1416 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>where does </src><tgt><\|wait\|></tgt>` | 1120 |
| 5 | `<src>Where does the tension </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里</tgt>` | `<src>attention start? </src><tgt><\|wait\|></tgt>` | 1401 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1375 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>What is it is a day, </src><tgt><\|wait\|></tgt>` | 1787 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>cause it's time </src><tgt><\|wait\|></tgt>` | 1120 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>in your chest. </src><tgt><\|wait\|></tgt>` | 1839 |
| 10 | `<src><\|wait\|></src><tgt>开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I have a sob, </src><tgt><\|wait\|></tgt>` | 2630 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>ling which are you using? </src><tgt><\|wait\|></tgt>` | 1283 |

---

### Test Example 15 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 723 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 894 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间</src><tgt><\|wait\|></tgt>` | 1437 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有这种</src><tgt><\|wait\|></tgt>` | 1206 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>宝贝心系</src><tgt><\|wait\|></tgt>` | 1437 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>的那些</src><tgt><\|wait\|></tgt>` | 1337 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>同事</src><tgt><\|wait\|></tgt>` | 1542 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天</src><tgt><\|wait\|></tgt>` | 1179 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的。</src><tgt><\|wait\|></tgt>` | 1649 |
| 10 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1172 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1881 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>说了两遍，</src><tgt><\|wait\|></tgt>` | 1268 |

---

### Test Example 16 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>待って、</src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>この辺りから</src><tgt><\|wait\|></tgt>` | 955 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので</src><tgt><\|wait\|></tgt>` | 1210 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>ご</src><tgt><\|wait\|></tgt>` | 1210 |
| 5 | `<src>ゴッホ、</src><tgt>大致是从这一带开始的，</tgt>` | `<src>方法</src><tgt><\|wait\|></tgt>` | 1427 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン。</src><tgt><\|wait\|></tgt>` | 1360 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1030 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ。</src><tgt><\|wait\|></tgt>` | 1771 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 1659 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ナルトという</src><tgt><\|wait\|></tgt>` | 1216 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>人の絵は</src><tgt><\|wait\|></tgt>` | 1874 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の</src><tgt><\|wait\|></tgt>` | 1265 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 869 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>먼지레 죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1001 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>해 가지고 내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 1449 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 1224 |
| 5 | `<src>다른 잔찜에 </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>아스다. 다른 </src><tgt><\|wait\|></tgt>` | 1508 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>잔 때문에 </src><tgt><\|wait\|></tgt>` | 1366 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>달래 자라. 내가 </src><tgt><\|wait\|></tgt>` | 2404 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>죽은 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1712 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>잔은 야. </src><tgt><\|wait\|></tgt>` | 1164 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1900 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>아. 내가 </src><tgt><\|wait\|></tgt>` | 1308 |

---

### Test Example 18 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 802 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A E E が</src><tgt><\|wait\|></tgt>` | 988 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>あんてですね。いる</src><tgt><\|wait\|></tgt>` | 1310 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>な場面で</src><tgt><\|wait\|></tgt>` | 1236 |
| 5 | `<src>調べるときに、</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area,</tgt>` | `<src>清掃活動</src><tgt><\|wait\|></tgt>` | 1440 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>行う時に</src><tgt><\|wait\|></tgt>` | 1328 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>A E の</src><tgt><\|wait\|></tgt>` | 1597 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>欄を調べたことで</src><tgt><\|wait\|></tgt>` | 1143 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>清掃活動</src><tgt><\|wait\|></tgt>` | 1629 |
| 10 | `<src>ことを保証する</src><tgt>you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>を清掃で</src><tgt><\|wait\|></tgt>` | 1230 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>保証されていった</src><tgt><\|wait\|></tgt>` | 1862 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方を</src><tgt><\|wait\|></tgt>` | 1384 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 689 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我的</src><tgt><\|wait\|></tgt>` | 845 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活，带一个</src><tgt><\|wait\|></tgt>` | 1065 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>鬼道号，让我</src><tgt><\|wait\|></tgt>` | 1189 |
| 5 | `<src>让我能够哈，</src><tgt>제 삶의 궤도로 돌아가고 싶어요.</tgt>` | `<src>能帮我</src><tgt><\|wait\|></tgt>` | 1267 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>在它下山的时候，</src><tgt><\|wait\|></tgt>` | 901 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在座日</src><tgt><\|wait\|></tgt>` | 1399 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>唐人街</src><tgt><\|wait\|></tgt>` | 2268 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那人街，我当时</src><tgt><\|wait\|></tgt>` | 1664 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>被掏出</src><tgt><\|wait\|></tgt>` | 1123 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的愿望</src><tgt><\|wait\|></tgt>` | 2046 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1490 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 910 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>以为</src><tgt><\|wait\|></tgt>` | 814 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 968 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>我</src><tgt><\|wait\|></tgt>` | 661 |
| 5 | `<src>坚持不开刀。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery.</tgt>` | `<src>可以坚持</src><tgt><\|wait\|></tgt>` | 1119 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>打开，期限大概</src><tgt><\|wait\|></tgt>` | 1486 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1359 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来选择段，</src><tgt><\|wait\|></tgt>` | 1793 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下</src><tgt><\|wait\|></tgt>` | 952 |
| 10 | `<src>一下提腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>挑腿，</src><tgt><\|wait\|></tgt>` | 1700 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>不没有问题，</src><tgt><\|wait\|></tgt>` | 1648 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>当然都很</src><tgt><\|wait\|></tgt>` | 1408 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一会打开。</src><tgt><\|wait\|></tgt>` | 1576 |

---

### Test Example 21 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 너무 </src><tgt><\|wait\|></tgt>` | 1405 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>심치 </src><tgt><\|wait\|></tgt>` | 516 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저하를 </src><tgt><\|wait\|></tgt>` | 1272 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이룰 수 있지만 </src><tgt><\|wait\|></tgt>` | 1294 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、</tgt>` | `<src>진짜 보살도 </src><tgt><\|wait\|></tgt>` | 1494 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기가 보살인데 </src><tgt><\|wait\|></tgt>` | 1622 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>꿈을 꿀 필요 </src><tgt><\|wait\|></tgt>` | 2315 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>있고 나만 보살로 </src><tgt><\|wait\|></tgt>` | 1709 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 필요 </src><tgt><\|wait\|></tgt>` | 1268 |
| 10 | `<src>지금 나한테 </src><tgt>自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に</tgt>` | `<src>있어요. 우주가 </src><tgt><\|wait\|></tgt>` | 1913 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>다원테 보살이 </src><tgt><\|wait\|></tgt>` | 1736 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1124 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。ギア</src><tgt><\|wait\|></tgt>` | 866 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1359 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src><\|wait\|></src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이</tgt>` | `<src>消えなくなってしまう</src><tgt><\|wait\|></tgt>` | 1395 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>のでギア</src><tgt><\|wait\|></tgt>` | 960 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>の先に</src><tgt><\|wait\|></tgt>` | 901 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 2232 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが付いて</src><tgt><\|wait\|></tgt>` | 1447 |
| 10 | `<src>ついているっていうことです</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>いるっていうこと</src><tgt><\|wait\|></tgt>` | 688 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 2478 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 507 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイ分解能</src><tgt><\|wait\|></tgt>` | 2197 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chun-Hwa Park, </src><tgt><\|wait\|></tgt>` | 797 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I'm currently studying </src><tgt><\|wait\|></tgt>` | 1267 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a BA in </src><tgt><\|wait\|></tgt>` | 1224 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>Business Finance and a </src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>major of psychology. </src><tgt><\|wait\|></tgt>` | 1422 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1979 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at </src><tgt><\|wait\|></tgt>` | 737 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Yenju, </src><tgt><\|wait\|></tgt>` | 1773 |
| 10 | `<src>and in the future, I want to go into </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>and uh in the future, I want to go </src><tgt><\|wait\|></tgt>` | 2587 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>into corporate </src><tgt><\|wait\|></tgt>` | 550 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 2139 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber</src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 723 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>band, chemical bonds also store</src><tgt><\|wait\|></tgt>` | 1344 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those</src><tgt><\|wait\|></tgt>` | 1293 |
| 5 | `<src>and when those bonds are broken, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면</tgt>` | `<src>bonds are broken,</src><tgt><\|wait\|></tgt>` | 1502 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy gets</src><tgt><\|wait\|></tgt>` | 1430 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to other</src><tgt><\|wait\|></tgt>` | 2339 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>types of energy, like</src><tgt><\|wait\|></tgt>` | 931 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>heat or light.</src><tgt><\|wait\|></tgt>` | 1204 |
| 10 | `<src><\|wait\|></src><tgt>잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>Or gets you</src><tgt><\|wait\|></tgt>` | 2546 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds</src><tgt><\|wait\|></tgt>` | 901 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1780 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1159 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the nineteenth amendment </src><tgt><\|wait\|></tgt>` | 833 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1278 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore </src><tgt><\|wait\|></tgt>` | 1044 |
| 5 | `<src>history as a guide </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1308 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help political </src><tgt><\|wait\|></tgt>` | 793 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 1268 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt><\|wait\|></tgt>` | 2378 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>United States. </src><tgt><\|wait\|></tgt>` | 1617 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 896 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 2195 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendment, </src><tgt><\|wait\|></tgt>` | 1277 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>of course, I'm </src><tgt><\|wait\|></tgt>` | 1471 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 901 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 832 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二期时，</src><tgt><\|wait\|></tgt>` | 1325 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>还服</src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>在一级一线</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で</tgt>` | `<src>在第一期</src><tgt><\|wait\|></tgt>` | 1418 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼大的牛们。</src><tgt><\|wait\|></tgt>` | 1415 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1076 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt><\|wait\|></tgt>` | 1659 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好几十年，</src><tgt><\|wait\|></tgt>` | 1837 |
| 10 | `<src>发现</src><tgt>戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1353 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信</src><tgt><\|wait\|></tgt>` | 1667 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>好平均分的</src><tgt><\|wait\|></tgt>` | 1575 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>心膀</src><tgt><\|wait\|></tgt>` | 1271 |

---

### Test Example 27 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1203 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>and then after these examples, </src><tgt><\|wait\|></tgt>` | 1328 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1226 |
| 5 | `<src>the instruction </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1398 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tell us to use </src><tgt><\|wait\|></tgt>` | 1371 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1733 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1070 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>this </src><tgt><\|wait\|></tgt>` | 1608 |
| 10 | `<src>these values. So </src><tgt>说明告诉我们要使用这些值。也就是</tgt>` | `<src>the values. So </src><tgt><\|wait\|></tgt>` | 1279 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>game.dot </src><tgt><\|wait\|></tgt>` | 1828 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>array. </src><tgt><\|wait\|></tgt>` | 1486 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1373 |

---

### Test Example 28 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 896 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 930 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>so here, you have to </src><tgt><\|wait\|></tgt>` | 1359 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>do 7.2 GB </src><tgt><\|wait\|></tgt>` | 1316 |
| 5 | `<src>ありましたね。</src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>already, right? </src><tgt><\|wait\|></tgt>` | 1483 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1333 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1852 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>fastest </src><tgt><\|wait\|></tgt>` | 842 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the </src><tgt><\|wait\|></tgt>` | 1676 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>Hokun </src><tgt><\|wait\|></tgt>` | 1417 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7.2 GB </src><tgt><\|wait\|></tgt>` | 1644 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>GB. </src><tgt><\|wait\|></tgt>` | 1719 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1150 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在</src><tgt><\|wait\|></tgt>` | 833 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>这个罗马呢</src><tgt><\|wait\|></tgt>` | 1068 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是</src><tgt><\|wait\|></tgt>` | 1104 |
| 5 | `<src>所以呢，</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、</tgt>` | `<src>年前造成的</src><tgt><\|wait\|></tgt>` | 635 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1428 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>现在</src><tgt><\|wait\|></tgt>` | 1290 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>除了你的一些</src><tgt><\|wait\|></tgt>` | 1761 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>鸡鸭跟凤</src><tgt><\|wait\|></tgt>` | 1070 |
| 10 | `<src>一夕之间就</src><tgt>今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>鸡也不可能是</src><tgt><\|wait\|></tgt>` | 1710 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间就</src><tgt><\|wait\|></tgt>` | 1510 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 1516 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>了，因此</src><tgt><\|wait\|></tgt>` | 1873 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>会建议</src><tgt><\|wait\|></tgt>` | 982 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라더니</src><tgt><\|wait\|></tgt>` | 1172 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>일거투는</src><tgt><\|wait\|></tgt>` | 645 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진</src><tgt><\|wait\|></tgt>` | 1206 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>유니술링과</src><tgt><\|wait\|></tgt>` | 1357 |
| 5 | `<src>유사 한 작용 이 </src><tgt>Things like vanadium</tgt>` | `<src>이거는</src><tgt><\|wait\|></tgt>` | 1435 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>거진 일반적인</src><tgt><\|wait\|></tgt>` | 1400 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>상태고 굉장히</src><tgt><\|wait\|></tgt>` | 1911 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>아주 당연히</src><tgt><\|wait\|></tgt>` | 875 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>비네랄이다</src><tgt><\|wait\|></tgt>` | 1747 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>길게</src><tgt><\|wait\|></tgt>` | 1943 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>길게</src><tgt><\|wait\|></tgt>` | 1012 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그런거죠. 이제</src><tgt><\|wait\|></tgt>` | 1718 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>그거에다가</src><tgt><\|wait\|></tgt>` | 1161 |

---

### Test Example 31 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 904 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>if you have to produce </src><tgt><\|wait\|></tgt>` | 991 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1218 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1299 |
| 5 | `<src>you realize that </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1441 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1925 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>which is like, </src><tgt><\|wait\|></tgt>` | 864 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>oh, is this word </src><tgt><\|wait\|></tgt>` | 1841 |
| 10 | `<src>spelled with a double </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2538 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>start with a double P, </src><tgt><\|wait\|></tgt>` | 936 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double M. I don't know </src><tgt><\|wait\|></tgt>` | 1890 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>what </src><tgt><\|wait\|></tgt>` | 888 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 895 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150원 계기가 </src><tgt><\|wait\|></tgt>` | 845 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중앙에서 </src><tgt><\|wait\|></tgt>` | 1194 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>100명 미만으로 </src><tgt><\|wait\|></tgt>` | 1386 |
| 5 | `<src>많았습니다. </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。</tgt>` | `<src>아주 작은 기업들이 </src><tgt><\|wait\|></tgt>` | 1557 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>있었습니다. </src><tgt><\|wait\|></tgt>` | 1399 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>일반적으로는 </src><tgt><\|wait\|></tgt>` | 2354 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 </src><tgt><\|wait\|></tgt>` | 1629 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 회계에 </src><tgt><\|wait\|></tgt>` | 799 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は</tgt>` | `<src>거의 적게 되는데 </src><tgt><\|wait\|></tgt>` | 2417 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>해외 송기 없으면 </src><tgt><\|wait\|></tgt>` | 1345 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>성장도 </src><tgt><\|wait\|></tgt>` | 1333 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>폐업 하지 않는 현상들이 </src><tgt><\|wait\|></tgt>` | 1076 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>帝王的</src><tgt><\|wait\|></tgt>` | 812 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>部分我们</src><tgt><\|wait\|></tgt>` | 817 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>看到了的是</src><tgt><\|wait\|></tgt>` | 1275 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>个戴庙的人，但是</src><tgt><\|wait\|></tgt>` | 1279 |
| 5 | `<src>它是属于逆向的，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요.</tgt>` | `<src>他是属于</src><tgt><\|wait\|></tgt>` | 1419 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这一通场</src><tgt><\|wait\|></tgt>` | 1423 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>场怎么样</src><tgt><\|wait\|></tgt>` | 1456 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>这样一个状况</src><tgt><\|wait\|></tgt>` | 1287 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>就特别注意是</src><tgt><\|wait\|></tgt>` | 1811 |
| 10 | `<src>是它能不能够</src><tgt>그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1286 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到与他</src><tgt><\|wait\|></tgt>` | 1733 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>掉不到与他</src><tgt><\|wait\|></tgt>` | 1500 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的意事</src><tgt><\|wait\|></tgt>` | 1345 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 859 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 894 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 818 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>钱头，那如果你</src><tgt><\|wait\|></tgt>` | 1340 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了钱头之后</src><tgt><\|wait\|></tgt>` | 1251 |
| 5 | `<src>请你务必就要</src><tgt>うまくいったなと思ったらね。その時は必ず利益を</tgt>` | `<src>亲你乌比</src><tgt><\|wait\|></tgt>` | 1464 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就要先手</src><tgt><\|wait\|></tgt>` | 1419 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>组，</src><tgt><\|wait\|></tgt>` | 1972 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想，</src><tgt><\|wait\|></tgt>` | 745 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在去操作一下</src><tgt><\|wait\|></tgt>` | 1821 |
| 10 | `<src>继续操作下去哦。</src><tgt>確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>去哦。</src><tgt><\|wait\|></tgt>` | 2184 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 736 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1704 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢</src><tgt><\|wait\|></tgt>` | 1063 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>呢</src><tgt><\|wait\|></tgt>` | 887 |

---

### Test Example 35 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 913 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>说实话</src><tgt><\|wait\|></tgt>` | 819 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错，但是</src><tgt><\|wait\|></tgt>` | 1273 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较</src><tgt><\|wait\|></tgt>` | 968 |
| 5 | `<src>也就是</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり</tgt>` | `<src>正财的部分</src><tgt><\|wait\|></tgt>` | 1259 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 697 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | 1472 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>业绩收入的</src><tgt><\|wait\|></tgt>` | 2257 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升，</src><tgt><\|wait\|></tgt>` | 485 |
| 10 | `<src>投资理财方面呢，</src><tgt>仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>如果是在投资领域</src><tgt><\|wait\|></tgt>` | 1761 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这一方面</src><tgt><\|wait\|></tgt>` | 2540 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>这个月也是不错，</src><tgt><\|wait\|></tgt>` | 929 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对来说</src><tgt><\|wait\|></tgt>` | 1758 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>说实话，</src><tgt><\|wait\|></tgt>` | 1021 |
| 15 | `<src><\|wait\|></src><tgt>悪くはないんですが、本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微</src><tgt><\|wait\|></tgt>` | 1067 |

---

### Test Example 36 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 929 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there's such </src><tgt><\|wait\|></tgt>` | 1299 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>instances before </src><tgt><\|wait\|></tgt>` | 1203 |
| 5 | `<src><\|wait\|></src><tgt>没什么新鲜的。以前就有过这样的接口，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1421 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>Netflix</src><tgt><\|wait\|></tgt>` | 1360 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>TC. </src><tgt><\|wait\|></tgt>` | 1617 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so this is just </src><tgt><\|wait\|></tgt>` | 1148 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1703 |
| 10 | `<src>to look at. </src><tgt>比如netfilter和 TC。所以这只是另一个需要关注的地方。</tgt>` | `<src>look at. </src><tgt><\|wait\|></tgt>` | 1263 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1777 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1350 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developer's </src><tgt><\|wait\|></tgt>` | 1426 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>engineering background should be </src><tgt><\|wait\|></tgt>` | 776 |
| 15 | `<src>should be aware of that. </src><tgt>但开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>there of that. </src><tgt><\|wait\|></tgt>` | 1166 |

---

### Test Example 37 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational</src><tgt><\|wait\|></tgt>` | 979 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>engagement. How far</src><tgt><\|wait\|></tgt>` | 903 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually</src><tgt><\|wait\|></tgt>` | 1333 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your</src><tgt><\|wait\|></tgt>` | 1235 |
| 5 | `<src>actually go in your education? Did you </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>education? Did you graduate</src><tgt><\|wait\|></tgt>` | 1585 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>from high school?</src><tgt><\|wait\|></tgt>` | 1336 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of</src><tgt><\|wait\|></tgt>` | 1860 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>engagement. Did you</src><tgt><\|wait\|></tgt>` | 979 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>go to college, and</src><tgt><\|wait\|></tgt>` | 1773 |
| 10 | `<src>and if so, did you graduate? </src><tgt>고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>so did you graduate?</src><tgt><\|wait\|></tgt>` | 2129 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level of</src><tgt><\|wait\|></tgt>` | 867 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>engagement.</src><tgt><\|wait\|></tgt>` | 1961 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now.</src><tgt><\|wait\|></tgt>` | 1101 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you</src><tgt><\|wait\|></tgt>` | 889 |
| 15 | `<src>online. </src><tgt>그게 또 다른 단계입니다. 그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online.</src><tgt><\|wait\|></tgt>` | 664 |

---

### Test Example 38 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 792 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 948 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>eighty-seven, </src><tgt><\|wait\|></tgt>` | 1300 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>which is </src><tgt><\|wait\|></tgt>` | 1183 |
| 5 | `<src><\|wait\|></src><tgt>HTML是一种</tgt>` | `<src>also </src><tgt><\|wait\|></tgt>` | 1359 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>a thing that can be understood, </src><tgt><\|wait\|></tgt>` | 1430 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and also </src><tgt><\|wait\|></tgt>` | 1072 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>the computer </src><tgt><\|wait\|></tgt>` | 1629 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>of the </src><tgt><\|wait\|></tgt>` | 1760 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>language, </src><tgt><\|wait\|></tgt>` | 1155 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>we have to write </src><tgt><\|wait\|></tgt>` | 1972 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>it, but </src><tgt><\|wait\|></tgt>` | 1480 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>we have to write </src><tgt><\|wait\|></tgt>` | 1395 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>the programs. </src><tgt><\|wait\|></tgt>` | 907 |
| 15 | `<src>필요 합니다. </src><tgt>我们需要按照它的语法来编写代码，而编写代码就需要专门的程序。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 999 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 이도 </src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알고 있나요? </src><tgt><\|wait\|></tgt>` | 831 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1378 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src>말 못하 는 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない</tgt>` | `<src>말 못 하는 </src><tgt><\|wait\|></tgt>` | 1467 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>무상에게로 </src><tgt><\|wait\|></tgt>` | 1474 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>이 되는 그대로 </src><tgt><\|wait\|></tgt>` | 2031 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 764 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1611 |
| 10 | `<src>그러므로 내가 </src><tgt>偶像に引かれるままに連れて行かれました。ですから、</tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 2057 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너 의에게 </src><tgt><\|wait\|></tgt>` | 940 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1629 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나 님의 영어 로 </src><tgt><\|wait\|></tgt>` | 1248 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자 는 </src><tgt><\|wait\|></tgt>` | 1032 |
| 15 | `<src><\|wait\|></src><tgt>あなたがたに教えます。神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 859 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 1111 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 864 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1289 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1174 |
| 5 | `<src>함께 한 동생 이자 </src><tgt>怎么说呢，</tgt>` | `<src>20대들을 </src><tgt><\|wait\|></tgt>` | 1210 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 880 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>이 동생이잖아. </src><tgt><\|wait\|></tgt>` | 1355 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 2199 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1624 |
| 10 | `<src>책임감 보다는 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>제인 거 보다는 </src><tgt><\|wait\|></tgt>` | 1061 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1989 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1118 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1487 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거. </src><tgt><\|wait\|></tgt>` | 1000 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>넣고. </src><tgt><\|wait\|></tgt>` | 1041 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 </src><tgt><\|wait\|></tgt>` | 853 |

---

### Test Example 41 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is</src><tgt><\|wait\|></tgt>` | 1246 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going needs</src><tgt><\|wait\|></tgt>` | 816 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>to get</src><tgt><\|wait\|></tgt>` | 1200 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1229 |
| 5 | `<src>and I have ten of them </src><tgt>それは始めたばかりの人が手に入れるべきもので、</tgt>` | `<src>and a ten of them that</src><tgt><\|wait\|></tgt>` | 1617 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>you're really important</src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2145 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to</src><tgt><\|wait\|></tgt>` | 515 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>um, I'm going to go and do</src><tgt><\|wait\|></tgt>` | 1961 |
| 10 | `<src>I have about </src><tgt>私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I have about one</src><tgt><\|wait\|></tgt>` | 2496 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>video, it's</src><tgt><\|wait\|></tgt>` | 1280 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>all this video</src><tgt><\|wait\|></tgt>` | 1356 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one, </src><tgt><\|wait\|></tgt>` | 1020 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>and a little more</src><tgt><\|wait\|></tgt>` | 1108 |
| 15 | `<src>in a little more detail, but. </src><tgt>この動画の後に、それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, but</src><tgt><\|wait\|></tgt>` | 835 |

---

### Test Example 42 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>村せてやる</src><tgt><\|wait\|></tgt>` | 877 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>あれ</src><tgt><\|wait\|></tgt>` | 1061 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1151 |
| 5 | `<src>今奇跡を見てる。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어.</tgt>` | `<src>ひき手を見ている</src><tgt><\|wait\|></tgt>` | 1383 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 702 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1386 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 2251 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不れる不気味な</src><tgt><\|wait\|></tgt>` | 635 |
| 10 | `<src><\|wait\|></src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不気味な</src><tgt><\|wait\|></tgt>` | 1613 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年に</src><tgt><\|wait\|></tgt>` | 2542 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>分のデイコールやってる</src><tgt><\|wait\|></tgt>` | 1180 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>な</src><tgt><\|wait\|></tgt>` | 1493 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1034 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>すごい快族線を見た</src><tgt><\|wait\|></tgt>` | 1193 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 770 |

---

### Test Example 43 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 1012 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 824 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>针对</src><tgt><\|wait\|></tgt>` | 899 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>对手的</src><tgt><\|wait\|></tgt>` | 670 |
| 5 | `<src><\|wait\|></src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1186 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>攻击</src><tgt><\|wait\|></tgt>` | 1335 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>很多时候</src><tgt><\|wait\|></tgt>` | 1352 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>经常会</src><tgt><\|wait\|></tgt>` | 1278 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>对人们</src><tgt><\|wait\|></tgt>` | 1419 |
| 10 | `<src>你们看，</src><tgt>するとき、よく耳にするのが「ほら、</tgt>` | `<src>这样说吧，你们看。</src><tgt><\|wait\|></tgt>` | 1688 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又</src><tgt><\|wait\|></tgt>` | 1171 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>在躲黄了。</src><tgt><\|wait\|></tgt>` | 1945 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1448 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 1332 |
| 15 | `<src><\|wait\|></src><tgt>また嘘をついている。目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 778 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 1156 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 810 |

---

### Test Example 44 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 929 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手的话</src><tgt><\|wait\|></tgt>` | 904 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>大概率</src><tgt><\|wait\|></tgt>` | 1075 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒内</src><tgt><\|wait\|></tgt>` | 1159 |
| 5 | `<src>まあ</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>吧，</src><tgt><\|wait\|></tgt>` | 1171 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒内</src><tgt><\|wait\|></tgt>` | 896 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒内</src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>约一秒钟</src><tgt><\|wait\|></tgt>` | 2317 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>的</src><tgt><\|wait\|></tgt>` | 1747 |
| 10 | `<src>でなんか</src><tgt>一秒一手多一点这样算。然后</tgt>` | `<src>感觉</src><tgt><\|wait\|></tgt>` | 1248 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 1761 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 1192 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>一二二</src><tgt><\|wait\|></tgt>` | 1419 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>二二</src><tgt><\|wait\|></tgt>` | 960 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>的二二</src><tgt><\|wait\|></tgt>` | 1174 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>会遇到</src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>で、これはですね、</src><tgt><\|wait\|></tgt>` | 1273 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 750 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていう開発環境</src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、ビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1385 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>なんです。で、</src><tgt><\|wait\|></tgt>` | 1470 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1344 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフでビジュアルを</src><tgt><\|wait\|></tgt>` | 2157 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとは</src><tgt><\|wait\|></tgt>` | 645 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコード</src><tgt><\|wait\|></tgt>` | 1695 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>を生成する。それが</src><tgt><\|wait\|></tgt>` | 1780 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1233 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理を</src><tgt><\|wait\|></tgt>` | 1634 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>行うという</src><tgt><\|wait\|></tgt>` | 1149 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ところになっているから</src><tgt><\|wait\|></tgt>` | 885 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1048 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はい。じゃあ</src><tgt><\|wait\|></tgt>` | 825 |

---

### Test Example 46 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1210 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 838 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>세모라 빌 뻔 했어요. </src><tgt><\|wait\|></tgt>` | 1461 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1216 |
| 5 | `<src>닭살이 돋든 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり</tgt>` | `<src>이제 소름이 돋은 </src><tgt><\|wait\|></tgt>` | 1603 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>그 차리 돋은 느낌 </src><tgt><\|wait\|></tgt>` | 1593 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>을 흔들어서 </src><tgt><\|wait\|></tgt>` | 2255 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1840 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1446 |
| 10 | `<src>물릴 거고 </src><tgt>何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、</tgt>` | `<src>기신이 오면 </src><tgt><\|wait\|></tgt>` | 1643 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | 1696 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>기신이 오면 너 지켜주고 </src><tgt><\|wait\|></tgt>` | 1408 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>지켜주라니까 </src><tgt><\|wait\|></tgt>` | 865 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에. </src><tgt><\|wait\|></tgt>` | 888 |
| 15 | `<src>눈 감아. </src><tgt>神様が来たら守ってくれるように突いてくれるから、安心して目を閉じて。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 673 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>축가 절수가 </src><tgt><\|wait\|></tgt>` | 1102 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승하는 </src><tgt><\|wait\|></tgt>` | 717 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>그름을 보인 다음에 </src><tgt><\|wait\|></tgt>` | 1321 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러한 </src><tgt><\|wait\|></tgt>` | 1209 |
| 5 | `<src>큰 폭의 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src>대형주도 </src><tgt><\|wait\|></tgt>` | 1501 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭으로 상승을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1534 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>어 먼저 </src><tgt><\|wait\|></tgt>` | 2131 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 </src><tgt><\|wait\|></tgt>` | 730 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>들이 </src><tgt><\|wait\|></tgt>` | 1488 |
| 10 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>이 먼저 시장을 </src><tgt><\|wait\|></tgt>` | 1692 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도하면서 움직이기 때문에 </src><tgt><\|wait\|></tgt>` | 1352 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1613 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동이 가벼운 </src><tgt><\|wait\|></tgt>` | 1289 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>종목을 </src><tgt><\|wait\|></tgt>` | 921 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>어 눈으로 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 1177 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 527 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>드러가면 </src><tgt><\|wait\|></tgt>` | 1134 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맨니다. </src><tgt><\|wait\|></tgt>` | 1005 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>아예 운전 을 </src><tgt><\|wait\|></tgt>` | 1301 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>거로 </src><tgt><\|wait\|></tgt>` | 1221 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>一进去就会晕头转向。不管是开车还是走路，</tgt>` | `<src>거로 다니고 </src><tgt><\|wait\|></tgt>` | 1493 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>가는 에 뭐 </src><tgt><\|wait\|></tgt>` | 1345 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북으로 가면 </src><tgt><\|wait\|></tgt>` | 1770 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말 할 것 또 </src><tgt><\|wait\|></tgt>` | 1046 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가도 </src><tgt><\|wait\|></tgt>` | 1773 |
| 10 | `<src>또 장렬이에요. </src><tgt>去江北就不用说了，去外国就更惨了。</tgt>` | `<src>장려 리요. </src><tgt><\|wait\|></tgt>` | 2332 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 615 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>괜히 에요. </src><tgt><\|wait\|></tgt>` | 2326 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1019 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 987 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>真有点丢人。不过，我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>노발요. </src><tgt><\|wait\|></tgt>` | 898 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그거는 </src><tgt><\|wait\|></tgt>` | 435 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 922 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 867 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>then self-defining what we think </src><tgt><\|wait\|></tgt>` | 1451 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>standard is because </src><tgt><\|wait\|></tgt>` | 1216 |
| 5 | `<src>absolutely correct, </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1427 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1844 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid </src><tgt><\|wait\|></tgt>` | 1001 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because </src><tgt><\|wait\|></tgt>` | 1699 |
| 10 | `<src>standards have </src><tgt>しかし現実には、</tgt>` | `<src>the standards have changed </src><tgt><\|wait\|></tgt>` | 2499 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>since 20 </src><tgt><\|wait\|></tgt>` | 507 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt><\|wait\|></tgt>` | 2200 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held </src><tgt><\|wait\|></tgt>` | 1029 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>to our standard because </src><tgt><\|wait\|></tgt>` | 1103 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>everything at this point </src><tgt><\|wait\|></tgt>` | 809 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is a higher standard </src><tgt><\|wait\|></tgt>` | 452 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계소 </src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 이런 </src><tgt><\|wait\|></tgt>` | 882 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>경우 들도 있습니다. </src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>저희가 A라는 사람과 </src><tgt><\|wait\|></tgt>` | 1353 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに</tgt>` | `<src>기란 사람이 </src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 </src><tgt><\|wait\|></tgt>` | 1355 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>컨설턴트예요. </src><tgt><\|wait\|></tgt>` | 2157 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>그리고 A라는 </src><tgt><\|wait\|></tgt>` | 685 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람이 </src><tgt><\|wait\|></tgt>` | 1689 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드를 </src><tgt><\|wait\|></tgt>` | 2548 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>설쳤을 때 </src><tgt><\|wait\|></tgt>` | 530 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비라는 사람이 </src><tgt><\|wait\|></tgt>` | 2198 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실패를 </src><tgt><\|wait\|></tgt>` | 1009 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로사이트스 T에서 </src><tgt><\|wait\|></tgt>` | 1129 |
| 15 | `<src>EX 파일 까지 </src><tgt>配布したとします。その場合、Bさんは実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>엑스파이까지 </src><tgt><\|wait\|></tgt>` | 901 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염이 될까? </src><tgt><\|wait\|></tgt>` | 422 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 913 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 678 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>subtlety, you can </src><tgt><\|wait\|></tgt>` | 1336 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but we </src><tgt><\|wait\|></tgt>` | 1168 |
| 5 | `<src><\|wait\|></src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>must </src><tgt><\|wait\|></tgt>` | 1132 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>always be </src><tgt><\|wait\|></tgt>` | 795 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>in the eyes of </src><tgt><\|wait\|></tgt>` | 1390 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>love, </src><tgt><\|wait\|></tgt>` | 2227 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>you can enter the </src><tgt><\|wait\|></tgt>` | 1443 |
| 10 | `<src><\|wait\|></src><tgt>사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>hunt, </src><tgt><\|wait\|></tgt>` | 677 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>in the hunt, </src><tgt><\|wait\|></tgt>` | 2506 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>you have to be </src><tgt><\|wait\|></tgt>` | 657 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>the one who has to be </src><tgt><\|wait\|></tgt>` | 2082 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>the one who becomes </src><tgt><\|wait\|></tgt>` | 1030 |
| 15 | `<src><\|wait\|></src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다.</tgt>` | `<src>the hunt </src><tgt><\|wait\|></tgt>` | 1192 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 830 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that hunt </src><tgt><\|wait\|></tgt>` | 311 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>continues to </src><tgt><\|wait\|></tgt>` | 458 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 1005 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1286 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1144 |
| 5 | `<src><\|wait\|></src><tgt>另外，你没法</tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1414 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1044 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though if </src><tgt><\|wait\|></tgt>` | 790 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into a situation </src><tgt><\|wait\|></tgt>` | 2303 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>where you </src><tgt><\|wait\|></tgt>` | 1586 |
| 10 | `<src>where you realize </src><tgt>在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1035 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 2123 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>to a particular resource </src><tgt><\|wait\|></tgt>` | 1215 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>to put in the list. Now, </src><tgt><\|wait\|></tgt>` | 1627 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 939 |
| 15 | `<src><\|wait\|></src><tgt>给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>giving those media files </src><tgt><\|wait\|></tgt>` | 1125 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 831 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>to get backed up properly. </src><tgt><\|wait\|></tgt>` | 572 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>Wait. </src><tgt><\|wait\|></tgt>` | 465 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point </src><tgt><\|wait\|></tgt>` | 989 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>knows Jesus </src><tgt><\|wait\|></tgt>` | 717 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1232 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1200 |
| 5 | `<src>he's been without food, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに</tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1402 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>he's been in the wilderness </src><tgt><\|wait\|></tgt>` | 1383 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for a whole year, </src><tgt><\|wait\|></tgt>` | 1336 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>is hungry. And so he says, </src><tgt><\|wait\|></tgt>` | 1485 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, </src><tgt><\|wait\|></tgt>` | 1763 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the son of God, </src><tgt><\|wait\|></tgt>` | 1715 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt><\|wait\|></tgt>` | 1419 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones </src><tgt><\|wait\|></tgt>` | 1864 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to bread. </src><tgt><\|wait\|></tgt>` | 987 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>How did Jesus deal with that? </src><tgt><\|wait\|></tgt>` | 1128 |
| 15 | `<src>temptation? </src><tgt>この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>The temptation. </src><tgt><\|wait\|></tgt>` | 786 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 761 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>genuinely </src><tgt><\|wait\|></tgt>` | 599 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>led by Peter alone. </src><tgt><\|wait\|></tgt>` | 571 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1460 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in here for a mile on the first </src><tgt><\|wait\|></tgt>` | 818 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>section about </src><tgt><\|wait\|></tgt>` | 1133 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1208 |
| 5 | `<src>about the EHR fields </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの</tgt>` | `<src>the HR field </src><tgt><\|wait\|></tgt>` | 1415 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1345 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 763 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>important versus </src><tgt><\|wait\|></tgt>` | 2038 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the variant database </src><tgt><\|wait\|></tgt>` | 1610 |
| 10 | `<src>databases, </src><tgt>決定的な重要性と、</tgt>` | `<src>is which is obviously </src><tgt><\|wait\|></tgt>` | 1129 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 2053 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1520 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1395 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 844 |
| 15 | `<src>to be in these </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、</tgt>` | `<src>that need to be in these data </src><tgt><\|wait\|></tgt>` | 1264 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>sources that we can </src><tgt><\|wait\|></tgt>` | 690 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 640 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 593 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 338 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1150 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 879 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, and </src><tgt><\|wait\|></tgt>` | 1065 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>Supreme Court </src><tgt><\|wait\|></tgt>` | 1167 |
| 5 | `<src>came along </src><tgt>有意义的个人权利，而最高法院</tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1182 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And </src><tgt><\|wait\|></tgt>` | 897 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>I thought the courts </src><tgt><\|wait\|></tgt>` | 1396 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>want to be the </src><tgt><\|wait\|></tgt>` | 2342 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>vanard of social change. </src><tgt><\|wait\|></tgt>` | 1679 |
| 10 | `<src>change </src><tgt>是最后才介入的，不是引领者。我不认为</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 923 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>Ah, these days, </src><tgt><\|wait\|></tgt>` | 2230 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but they rather </src><tgt><\|wait\|></tgt>` | 1248 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect the </src><tgt><\|wait\|></tgt>` | 1376 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>consensus </src><tgt><\|wait\|></tgt>` | 931 |
| 15 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，它们更倾向于</tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1128 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 790 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 371 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>you have </src><tgt><\|wait\|></tgt>` | 498 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 542 |
| 20 | `<src><\|wait\|></src><tgt>反映已经形成的共识。所以，有些联邦法官……</tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 367 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 386 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1106 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 800 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，</src><tgt><\|wait\|></tgt>` | 1268 |
| 5 | `<src>的一个是客厅</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면</tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1472 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>客听的部分，</src><tgt><\|wait\|></tgt>` | 1343 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>客听一般</src><tgt><\|wait\|></tgt>` | 1782 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是属于</src><tgt><\|wait\|></tgt>` | 1078 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们再</src><tgt><\|wait\|></tgt>` | 1623 |
| 10 | `<src>在休息的地方，</src><tgt>거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt><\|wait\|></tgt>` | 1281 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1790 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分。</src><tgt><\|wait\|></tgt>` | 1585 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它会反映的是</src><tgt><\|wait\|></tgt>` | 1293 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>需要给</src><tgt><\|wait\|></tgt>` | 860 |
| 15 | `<src>一点时间，</src><tgt>그래서 이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 1046 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地做。</src><tgt><\|wait\|></tgt>` | 826 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>下来休息，</src><tgt><\|wait\|></tgt>` | 621 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们看到这边是</src><tgt><\|wait\|></tgt>` | 608 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>双人吗？</src><tgt><\|wait\|></tgt>` | 392 |
| 20 | `<src>啊，</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는 아무도 없네요.</tgt>` | `<src>好，所以</src><tgt><\|wait\|></tgt>` | 355 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>是说，</src><tgt><\|wait\|></tgt>` | 364 |

---

### Test Example 57 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 876 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>말하는 사람들이 </src><tgt><\|wait\|></tgt>` | 807 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1399 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 </src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src>분석 을 보시면 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、</tgt>` | `<src>의 예시 를 보시면 </src><tgt><\|wait\|></tgt>` | 1563 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>손이 가 </src><tgt><\|wait\|></tgt>` | 1383 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>유리 룩 튜 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에` | 11669 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FFP 파이프 를 </src><tgt><\|wait\|></tgt>` | 943 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128 비트 로 </src><tgt><\|wait\|></tgt>` | 489 |
| 10 | `<src>것으로 보인다. </src><tgt>ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>나 줘 로 보인다. </src><tgt><\|wait\|></tgt>` | 503 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 582 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 362 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 392 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>에 S2 </src><tgt><\|wait\|></tgt>` | 327 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 343 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 382 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 937 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 818 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>completely rare, and they often </src><tgt><\|wait\|></tgt>` | 1347 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1234 |
| 5 | `<src><\|wait\|></src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>completely revolutionize </src><tgt><\|wait\|></tgt>` | 1392 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>the world. </src><tgt><\|wait\|></tgt>` | 1365 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1761 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>The personality is </src><tgt><\|wait\|></tgt>` | 1072 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1781 |
| 10 | `<src>contradiction. </src><tgt>世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 1736 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>they're extroverted, </src><tgt><\|wait\|></tgt>` | 1273 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>they also </src><tgt><\|wait\|></tgt>` | 1953 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 876 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 946 |
| 15 | `<src>and like to </src><tgt>外交的である一方、無意味な会話は嫌います。そして、</tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 837 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it gets straight to the </src><tgt><\|wait\|></tgt>` | 883 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 587 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 546 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 415 |
| 20 | `<src>the devil's advocate, and they </src><tgt>要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 392 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 361 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 352 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Ean </src><tgt><\|wait\|></tgt>` | 320 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>TP stands </src><tgt><\|wait\|></tgt>` | 262 |
| 25 | `<src>ENTP stands for </src><tgt>議論を避けることはありません。ENTPとは</tgt>` | `<src>for </src><tgt><\|wait\|></tgt>` | 208 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=4)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전의 이준석은</src><tgt><\|wait\|></tgt>` | 1375 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 438 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>정무를 거부한 명분</src><tgt><\|wait\|></tgt>` | 1415 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>이 후보를 위해서</src><tgt><\|wait\|></tgt>` | 1159 |
| 5 | `<src>후보 의 당선 을 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>하면서 후보의 당선을 위해서</src><tgt><\|wait\|></tgt>` | 1573 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>하면서</src><tgt><\|wait\|></tgt>` | 1303 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색까지 냈지만</src><tgt><\|wait\|></tgt>` | 2443 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>이제는</src><tgt><\|wait\|></tgt>` | 744 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보가</src><tgt><\|wait\|></tgt>` | 1468 |
| 10 | `<src>김종인 을 </src><tgt>for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>김경배를 재관순간</src><tgt><\|wait\|></tgt>` | 2648 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>이준석은</src><tgt><\|wait\|></tgt>` | 1522 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>들어내 놓고</src><tgt><\|wait\|></tgt>` | 1340 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보</src><tgt><\|wait\|></tgt>` | 907 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는</src><tgt><\|wait\|></tgt>` | 1153 |
| 15 | `<src><\|wait\|></src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>도끼를 품은</src><tgt><\|wait\|></tgt>` | 790 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격성을</src><tgt><\|wait\|></tgt>` | 605 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이기로</src><tgt><\|wait\|></tgt>` | 531 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것</src><tgt><\|wait\|></tgt>` | 399 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다.</src><tgt><\|wait\|></tgt>` | 382 |
| 20 | `<src><\|wait\|></src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's</tgt>` | `<src>김세발</src><tgt><\|wait\|></tgt>` | 366 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 청상납금</src><tgt><\|wait\|></tgt>` | 389 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 360 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이</src><tgt><\|wait\|></tgt>` | 347 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격에 얼마나</src><tgt><\|wait\|></tgt>` | 303 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute— what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재입니까?</src><tgt><\|wait\|></tgt>` | 316 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 4 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1039 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt><\|wait\|></tgt>` | 864 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってみたいです。</src><tgt><\|wait\|></tgt>` | 1421 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1137 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ホテル</src><tgt><\|wait\|></tgt>` | 689 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>の朝食が</src><tgt><\|wait\|></tgt>` | 1253 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所になってる</src><tgt><\|wait\|></tgt>` | 2340 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってる</src><tgt><\|wait\|></tgt>` | 1644 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 1166 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1908 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>このドストンホテル</src><tgt><\|wait\|></tgt>` | 1335 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい方</src><tgt><\|wait\|></tgt>` | 1488 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>はですね、</src><tgt><\|wait\|></tgt>` | 886 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>この夏</src><tgt><\|wait\|></tgt>` | 1058 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>いいじゃないかと</src><tgt><\|wait\|></tgt>` | 862 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 265 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>このホテルからですね</src><tgt><\|wait\|></tgt>` | 471 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 575 |
| 20 | `<src><\|wait\|></src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>もう</src><tgt><\|wait\|></tgt>` | 366 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt><\|wait\|></tgt>` | 378 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>1分かかるか</src><tgt><\|wait\|></tgt>` | 387 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>わからないか</src><tgt><\|wait\|></tgt>` | 309 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>そんなね、</src><tgt><\|wait\|></tgt>` | 392 |
| 25 | `<src>ホテルになってますので</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>まあホテルになってますので</src><tgt><\|wait\|></tgt>` | 351 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 318 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 320 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。</src><tgt><\|wait\|></tgt>` | 184 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それでは</src><tgt><\|wait\|></tgt>` | 175 |
