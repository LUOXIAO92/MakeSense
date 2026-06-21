# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9942
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9327
  - SRC_RELEASE_TOTAL: 713
  - SRC_WAIT_ACCURACY: 0.5563
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.7120
  - TGT_RELEASE_TOTAL: 493
  - TGT_WAIT_ACCURACY: 0.7493
  - TGT_WAIT_TOTAL: 371
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1344.7330
  - PROCESS_TIME_MS_P50: 1316.4690
  - PROCESS_TIME_MS_P95: 2250.6390
  - PROCESS_TIME_MS_MAX: 11234.9860

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1159 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>砂を洗い流した後は、</tgt>` | 1311 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>内部的压力</src><tgt>内部の圧力が</tgt>` | 903 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也稍弱了。</src><tgt>少し弱まります。</tgt>` | 1277 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1384 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在</src><tgt><\|wait\|></tgt>` | 1673 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1433 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 472 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>运行状态。</src><tgt>そして、比較的低エネルギーな稼働状態に留まります。</tgt>` | 2116 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これが</tgt>` | 1274 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>抑郁状态。</src><tgt>いわゆる抑うつ状態です。</tgt>` | 2359 |

---

### Test Example 2 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1230 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>The people in the auspicious spots</tgt>` | 982 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1064 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1363 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1461 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1733 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1430 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt>They are people who were selected randomly.</tgt>` | 816 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1390 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1639 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교수 하들은 </src><tgt>The professors who didn't know the truth</tgt>` | 2376 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 824 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 922 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>特に今まだ</src><tgt><\|wait\|></tgt>` | 1072 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>1年生ですからね。</src><tgt>从一开始，特别是现在还是大一新生。</tgt>` | 1618 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>この時点で</src><tgt>在这个阶段，</tgt>` | 1413 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう密告</src><tgt><\|wait\|></tgt>` | 1574 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>前提を</src><tgt><\|wait\|></tgt>` | 1389 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 518 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>暗ずして待ってあげると</src><tgt>如果先设定好密告的前提，</tgt>` | 2146 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>1年経っても</src><tgt>即使过了一年，</tgt>` | 1504 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>待ちは</src><tgt><\|wait\|></tgt>` | 2223 |

---

### Test Example 4 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1016 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔을 </src><tgt><\|wait\|></tgt>` | 961 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주게 달라 이거 주고 내가 </src><tgt><\|wait\|></tgt>` | 1306 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>주길 넣고 들어와 서도 </src><tgt><\|wait\|></tgt>` | 1338 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔 쯤에 </src><tgt><\|wait\|></tgt>` | 1677 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>주게 달라 </src><tgt><\|wait\|></tgt>` | 1399 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>해줘야 되나 내가 </src><tgt><\|wait\|></tgt>` | 1560 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1731 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 중이라 는 거야 </src><tgt><\|wait\|></tgt>` | 1792 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아 </src><tgt><\|wait\|></tgt>` | 973 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1897 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1276 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>乖的宠仔点，</src><tgt>Be a good, spoiled kid,</tgt>` | 1092 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个友谊很大，</src><tgt>this friendship is great.</tgt>` | 1366 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt>And then,</tgt>` | 1416 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt><\|wait\|></tgt>` | 1700 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>跟陶儿</src><tgt><\|wait\|></tgt>` | 1375 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 537 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在一起待了一段时间，</src><tgt>I spent some time with Tao'er during my vacation,</tgt>` | 2159 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1389 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>这种和陶儿。</src><tgt>this friendship with Tao'er...</tgt>` | 2604 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>아 저는 </src><tgt>Ah, I'm</tgt>` | 1131 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용신 이 </src><tgt><\|wait\|></tgt>` | 909 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1112 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>아 칼 용신이 </src><tgt><\|wait\|></tgt>` | 1391 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt>a Fire element, so</tgt>` | 1482 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>용신 이가 </src><tgt><\|wait\|></tgt>` | 1673 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데요. </src><tgt>it's mixed with a Metal element.</tgt>` | 1703 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1577 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1690 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>해행으로도 </src><tgt><\|wait\|></tgt>` | 760 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 주기 만 한 </src><tgt><\|wait\|></tgt>` | 2344 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大抵</src><tgt>通常</tgt>` | 945 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>从这里开始，</tgt>` | 851 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1039 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>始めたもので、</src><tgt>我才开始的。</tgt>` | 1211 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴホ</src><tgt><\|wait\|></tgt>` | 849 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴギョアン</src><tgt><\|wait\|></tgt>` | 1682 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1312 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>制圧の</src><tgt><\|wait\|></tgt>` | 1481 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1652 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどのという人の絵</src><tgt><\|wait\|></tgt>` | 1747 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>は田舎の中学生でも</src><tgt>即使是乡村中学生</tgt>` | 2253 |

---

### Test Example 8 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1210 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 911 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复。</tgt>` | 1022 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>学会重复。重复练习。</tgt>` | 1379 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1293 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>找到你擅长的地方，多做一些。</tgt>` | 2068 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1510 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>And what you're not good at, </src><tgt>你不太擅长的，</tgt>` | 1669 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>get the people around you to help you with. </src><tgt>让身边的人来帮你。</tgt>` | 1805 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 925 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>And until next time, </src><tgt>我们下次再见，</tgt>` | 2172 |

---

### Test Example 9 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1127 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要切鼠是容易的，</src><tgt>ネズミを捕まえるのは簡単です。</tgt>` | 1624 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1181 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只要一个师傅</src><tgt>でも、</tgt>` | 789 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>指道，</src><tgt>師匠が指し示せば、</tgt>` | 2129 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1150 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>如波出于终间，</src><tgt>終末から波が立ち上がるように、</tgt>` | 1572 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>ですから</tgt>` | 1552 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>反転させる必要があります。</tgt>` | 1731 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1044 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅，</src><tgt>師匠になるには、</tgt>` | 1946 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1248 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 863 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただいている</src><tgt><\|wait\|></tgt>` | 1022 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>ものも用意しておりますので</src><tgt>We also have items like T- shirts available,</tgt>` | 1306 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ぜひご参加ください。</src><tgt>so please feel free to join us.</tgt>` | 1912 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1226 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>That's all for the contact information.</tgt>` | 780 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1701 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>またのご来場</src><tgt><\|wait\|></tgt>` | 1797 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>を心より</src><tgt><\|wait\|></tgt>` | 1946 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>お待ちしております。</src><tgt>We look forward to seeing you again.</tgt>` | 951 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt>非常に重要な</tgt>` | 908 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1089 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. This is </src><tgt>極めて幸せな人々に関する研究を行いました。</tgt>` | 1838 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>tip of the stem </src><tgt>これは</tgt>` | 1383 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>この研究の序章です。</tgt>` | 1576 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1418 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1627 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>最も幸せな人々の10%を</tgt>` | 1864 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people who live </src><tgt>見ると、</tgt>` | 1882 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>私たちが学ぶべき人々です。</tgt>` | 1196 |

---

### Test Example 12 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Aptitude </src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축발시키고 </src><tgt><\|wait\|></tgt>` | 1187 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1265 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1260 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt><\|wait\|></tgt>` | 1821 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1323 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 549 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1794 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1820 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt>I am a member of the same generation as Herona Park Han- sang, who killed her own parents.</tgt>` | 2882 |

---

### Test Example 13 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1255 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is</tgt>` | 1064 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1014 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1327 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水，</src><tgt>water them with our deep love.</tgt>` | 1963 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>Fertilize them,</tgt>` | 1304 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1481 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>培育孩子心里的营养，</src><tgt>nurture the nourishment in their hearts,</tgt>` | 2028 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1652 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>并耐心等待</src><tgt>and patiently wait</tgt>` | 2245 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>孩子慢慢长大。</src><tgt>as their child slowly grows up.</tgt>` | 790 |

---

### Test Example 14 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` | 868 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` | 899 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop into your body </src><tgt><\|wait\|></tgt>` | 1101 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1303 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>where does the tension </src><tgt><\|wait\|></tgt>` | 1299 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>进入你的身体，紧张感从哪里开始？是什么？</tgt>` | 2191 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | 1482 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>胸口紧绷吗？</tgt>` | 2088 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>Or is the body </src><tgt>还是</tgt>` | 1545 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>landing? </src><tgt>身体在沉降？</tgt>` | 2393 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>Which way are you using? </src><tgt>你是在哪个方向使用？</tgt>` | 775 |

---

### Test Example 15 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 884 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAアンデスに</src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>世論の場面で</src><tgt><\|wait\|></tgt>` | 1088 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>AA制服かどうか</src><tgt><\|wait\|></tgt>` | 1375 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>によっては</src><tgt><\|wait\|></tgt>` | 1105 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>AAの乱抗を</src><tgt><\|wait\|></tgt>` | 1612 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1297 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その制服かどうか</src><tgt><\|wait\|></tgt>` | 980 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を検証する</src><tgt><\|wait\|></tgt>` | 1673 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>制服であることを保証する</src><tgt><\|wait\|></tgt>` | 1794 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1735 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt>They have been using it to verify whether it is an AA uniform by examining the AA anti-fan situation in public opinion settings.</tgt>` | 1636 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right. </src><tgt>好的。</tgt>` | 1178 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>And then, </src><tgt>然后，</tgt>` | 734 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | 1062 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1128 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 838 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1863 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1230 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1392 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1551 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So, </src><tgt>实际上要使用这些值。所以，</tgt>` | 1300 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1082 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>this game dot sort array </src><tgt><\|wait\|></tgt>` | 2488 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1483 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>そう</src><tgt><\|wait\|></tgt>` | 919 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>です。そこで</src><tgt>그렇습니다. 거기서</tgt>` | 1008 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天国という</src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>設定が</src><tgt>천국 설정이</tgt>` | 1271 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>ありましたが、</src><tgt>있었는데,</tgt>` | 1097 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1360 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1368 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井青氏の仕組み</src><tgt>나가이 아오 씨의</tgt>` | 1251 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>구조는</tgt>` | 1626 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>ウォコン</src><tgt><\|wait\|></tgt>` | 1662 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1056 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設定が</src><tgt>워콘 설정이</tgt>` | 1978 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>ゴビです。</src><tgt>고비입니다.</tgt>` | 1585 |

---

### Test Example 18 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これが</src><tgt>이것이</tgt>` | 1153 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>ギアです。</src><tgt>기어입니다.</tgt>` | 742 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが</src><tgt>기어가</tgt>` | 1011 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>緩むと、</src><tgt>느슨해지면</tgt>` | 1273 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消え</src><tgt>신호가</tgt>` | 960 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>꺼지게 되기 때문에</tgt>` | 1931 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 앞쪽에</tgt>` | 1410 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1063 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | 1770 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt>달려 있다는</tgt>` | 1793 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>뜻입니다.</tgt>` | 1689 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1174 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>ハイ分解完了。</src><tgt>하이 분해 완료.</tgt>` | 1578 |

---

### Test Example 19 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 973 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt>これ、</tgt>` | 797 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>좋아요 라는 의미 룰 있지만 </src><tgt>「いいね」って意味合いはありますが、</tgt>` | 1254 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt>本当に菩薩様です。</tgt>` | 1437 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 자기 의 </src><tgt>いや、</tgt>` | 1467 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>自分の菩薩様なんですが、</tgt>` | 1983 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>피라고 보이 고 </src><tgt>夢だとわかって、</tgt>` | 1492 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1687 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>보살 로 보이 려고 보이 색 우주 가 </src><tgt>自分だけ菩薩様に見せようとして、宇宙が</tgt>` | 2316 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>진짜 </src><tgt><\|wait\|></tgt>` | 2293 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>보살이 라는데. </src><tgt>本当に菩薩様だと言っているんです。</tgt>` | 1723 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 869 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt><\|wait\|></tgt>` | 906 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活的一个</src><tgt>제 삶의</tgt>` | 1108 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt>궤도로 돌아가게 해줘요.</tgt>` | 1537 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1407 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>好自在的他下面的时候，</src><tgt>편안하게, 제 아래에서</tgt>` | 1909 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1397 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭给人家吃，</src><tgt>뜨거운 국이나 밥을 만들어 사람들에게 대접할 수 있게 해줘요.</tgt>` | 2831 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就这么个</src><tgt><\|wait\|></tgt>` | 967 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我待在这样的</src><tgt><\|wait\|></tgt>` | 2352 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的愿望哈。</src><tgt>그게 제가 가진 작은 소망이에요.</tgt>` | 722 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1181 |

---

### Test Example 21 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1018 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>面对这个情况，</src><tgt>Facing this situation,</tgt>` | 933 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>我们就遇到问题</src><tgt>we run into</tgt>` | 1074 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就各自的回报主管，</src><tgt>the problem of each person's own performance manager.</tgt>` | 1716 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt>Or, we notify the other party</tgt>` | 2004 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们下了这个状况，</src><tgt>that we've encountered this situation.</tgt>` | 1954 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 621 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>不要想自己什么</src><tgt>Don't think</tgt>` | 1743 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>都把它扛下来，</src><tgt>you have to handle everything yourself.</tgt>` | 1944 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>不离成本，整体而言</src><tgt>Don't think of it as a cost.</tgt>` | 2708 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>是一定是属实。</src><tgt>Overall, it's definitely true.</tgt>` | 1632 |

---

### Test Example 22 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 948 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If you're a high school girl</tgt>` | 1296 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1093 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1007 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>and you have some kind of connection with someone who looks a bit strange,</tgt>` | 2499 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>could it be</tgt>` | 1285 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1084 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里</src><tgt><\|wait\|></tgt>` | 1817 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>something that started that night?</tgt>` | 1753 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2171 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 787 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>连篇，</src><tgt>Yangzi's thoughts raced on,</tgt>` | 1525 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt>제 이름은</tgt>` | 1074 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Kiran Patel, </src><tgt>키란 파텔입니다.</tgt>` | 1005 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently studying </src><tgt>현재</tgt>` | 1040 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a business background </src><tgt><\|wait\|></tgt>` | 1358 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>and finance </src><tgt>비즈니스 및 금융 분야를 공부하고 있습니다.</tgt>` | 2194 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of psychology </src><tgt>또한</tgt>` | 1164 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1437 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at Wayne </src><tgt><\|wait\|></tgt>` | 1636 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1690 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>and in the future I want to go </src><tgt>웨인 대학에서 심리학 학사 학위를 받았습니다. 앞으로</tgt>` | 1634 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1518 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>into corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1729 |

---

### Test Example 24 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt><\|wait\|></tgt>` | 1183 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 인슐린과 </src><tgt><\|wait\|></tgt>` | 1212 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1013 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산 잔 층인 </src><tgt><\|wait\|></tgt>` | 1806 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일정 도 굉장히 </src><tgt><\|wait\|></tgt>` | 1457 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1448 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1693 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1265 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1025 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 2475 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1543 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 426 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>Like a stretched rubber band, </src><tgt>늘어난 고무줄처럼,</tgt>` | 1313 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt>화학 결합은</tgt>` | 903 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy. And when those </src><tgt>에너지를 저장합니다. 그리고</tgt>` | 1478 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>bonds are broken, </src><tgt>그 결합이 끊어지면,</tgt>` | 2165 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 잠재 에너지는</tgt>` | 1698 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 731 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt><\|wait\|></tgt>` | 1881 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light. </src><tgt>열이나 빛 같은 다른 에너지 형태로 변환됩니다.</tgt>` | 1989 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2399 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>Or gets used to make </src><tgt>또는</tgt>` | 1454 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>다른 결합을 만드는 데 사용됩니다.</tgt>` | 641 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个</src><tgt>2つ目は</tgt>` | 922 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 794 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>就是进入二级市场，</src><tgt>二级市場への参入です。</tgt>` | 1142 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1268 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一级一级线</src><tgt>一级市場の</tgt>` | 960 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们</src><tgt>大牛たちが</tgt>` | 1569 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说</src><tgt>一斉に殺し合う</tgt>` | 1209 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1386 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>微信公众号几点，你会</src><tgt>例として、微信の公式アカウントが</tgt>` | 2069 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1643 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>发件给微信公众号拼分的</src><tgt>投稿する時間帯に、</tgt>` | 2673 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1589 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>新棒反之惑了。</src><tgt>新棒と反之惑が</tgt>` | 857 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Or, or if you have </src><tgt>あるいは、</tgt>` | 1169 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 816 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何かを書き起こす必要がある場合、</tgt>` | 1400 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>テキストを書く、</tgt>` | 1156 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1434 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1780 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1451 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. Like, oh, is </src><tgt>単語のスペルが全くわからないことに気づくかもしれません。「ああ、</tgt>` | 1729 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>this word </src><tgt>この単語は</tgt>` | 1740 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 1065 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1980 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam. I don't know. </src><tgt>doublep、doublel、わからない」</tgt>` | 1776 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1510 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1226 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 950 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment </src><tgt>19차 수정헌법의</tgt>` | 1612 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore its </src><tgt>의미와</tgt>` | 980 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>역사를 탐구하며</tgt>` | 1881 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1298 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change </src><tgt>정치적 변화가</tgt>` | 1527 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>어떻게 일어날 수 있는지</tgt>` | 1830 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침을 살펴봅니다.</tgt>` | 2279 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2287 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1449 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>물론</tgt>` | 506 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>I'm Mary. </src><tgt>저는 메리입니다.</tgt>` | 1443 |

---

### Test Example 29 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 847 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150배가 종업원 수가 </src><tgt>150倍の従業員数が</tgt>` | 1476 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>1000명 미만 으로 </src><tgt>1000人未満に</tgt>` | 1434 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>なるような、非常に小さな企業が</tgt>` | 1490 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>多くありました。</tgt>` | 1376 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的に、</tgt>` | 1370 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 </src><tgt>中小企業は</tgt>` | 1202 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>成長するか、あるいは</tgt>` | 2000 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>폐업 했을 때도 있는데 </src><tgt>廃業することもありますが、</tgt>` | 1861 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>これは</tgt>` | 2166 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>소기업 들은 </src><tgt>中小企業は</tgt>` | 568 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>成長も廃業もしない</tgt>` | 1536 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>현상 으로 보이 게 된 거죠. </src><tgt>現象と見なされたのです。</tgt>` | 1663 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>我当时已婚正常，</src><tgt>I was already married at the time,</tgt>` | 1312 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>毫无妨乱跳。</src><tgt>so it didn't bother me at all.</tgt>` | 1489 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 831 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>所以坚持不开道，</src><tgt>So I insisted on not opening the Dao,</tgt>` | 2150 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间大概</src><tgt><\|wait\|></tgt>` | 1305 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>有一名医生</src><tgt><\|wait\|></tgt>` | 1185 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>来审断，</src><tgt>and a doctor came to examine me.</tgt>` | 1986 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下挑腿，</src><tgt>He said:</tgt>` | 1655 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>If you lift your leg up,</tgt>` | 2623 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>it's fine. If you lift it down, it's also fine.</tgt>` | 1672 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1135 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>疑不欲的离开。</src><tgt>They were very suspicious and left.</tgt>` | 786 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1113 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1068 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>このローマでは、</tgt>` | 1395 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>一日のうちに</tgt>` | 1044 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>所以呢，</src><tgt>できるわけではないということです。</tgt>` | 1645 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1460 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>你现在所面临的一些</src><tgt>今直面している</tgt>` | 1572 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt>危機や</tgt>` | 1643 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>跟风险，</src><tgt>リスクは、</tgt>` | 1325 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 955 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一时间就显现出来。</src><tgt>一瞬で現れるものではないということです。</tgt>` | 2653 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1549 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>的因此会建议</src><tgt>そのため、</tgt>` | 1288 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>属鸡的粉丝呢。</src><tgt>酉年生まれの皆さんには、</tgt>` | 663 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 898 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到了一个甜头，</src><tgt>良い兆しが訪れました。</tgt>` | 1189 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt>もし</tgt>` | 802 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了甜头之后，</src><tgt>この兆しを得た後、</tgt>` | 1559 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你务必就要</src><tgt>必ず</tgt>` | 1538 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1467 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>先守住，</src><tgt>守り抜いてください。</tgt>` | 1627 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说：“哎，</src><tgt>「ああ、</tgt>` | 1799 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我再继续操作</src><tgt>もう一度</tgt>` | 1784 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。”</src><tgt>操作を続けよう」なんて考えないでください。</tgt>` | 2251 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 779 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのか？</tgt>` | 1525 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1531 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>因为呢。</src><tgt>なぜなら……</tgt>` | 1102 |

---

### Test Example 33 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>嗯，</tgt>` | 727 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>HTML </src><tgt><\|wait\|></tgt>` | 777 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1035 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터 도 </src><tgt><\|wait\|></tgt>` | 1188 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt>计算机</tgt>` | 839 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1456 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1578 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1543 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 </src><tgt><\|wait\|></tgt>` | 1636 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>말끼 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1707 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 741 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 2356 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1538 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 948 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>计算机语言，也就是HTML，也是人能理解的。计算机语言的语法，我们现在需要编写代码，所以需要一个程序来编写这些代码。</tgt>` | 1867 |

---

### Test Example 34 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1167 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 918 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1067 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1284 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and I have ten of them </src><tgt>今まさに動き出している人たち、その10人</tgt>` | 1675 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that you really </src><tgt><\|wait\|></tgt>` | 1655 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>might want to </src><tgt><\|wait\|></tgt>` | 1385 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 513 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>um I'm going to go </src><tgt><\|wait\|></tgt>` | 1926 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>and do I have about one </src><tgt><\|wait\|></tgt>` | 1724 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 2223 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at the end of this video </src><tgt>について、</tgt>` | 622 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt>この動画の最後に1分程度の動画を1つずつ紹介します。</tgt>` | 1620 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>And a little more </src><tgt><\|wait\|></tgt>` | 1437 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, </src><tgt>もう少し詳しく、</tgt>` | 1126 |

---

### Test Example 35 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>金運についてですが、</tgt>` | 1153 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个月财运</src><tgt>今月の金運は</tgt>` | 945 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>可以说是属于不好的，</src><tgt>あまり良くないと言えます。</tgt>` | 1473 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>但是比较稳定</src><tgt>でも、</tgt>` | 893 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src>的部分，</src><tgt>安定している部分もあります。</tgt>` | 1472 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>也就是在事业方面的</src><tgt>つまり、</tgt>` | 1664 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩增长</src><tgt>仕事の業績向上</tgt>` | 1382 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>带来的红利</src><tgt>による恩恵</tgt>` | 523 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>和收入的提升。</src><tgt>や収入の増加です。</tgt>` | 1865 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>如果涉及到投资理财方面，</src><tgt>投資や資産運用に関しては、</tgt>` | 1881 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 2352 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不落，</src><tgt>あまり良くない</tgt>` | 1504 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>只是相对整体来说，</src><tgt>わけではありません。ただ、全体的に見ると、</tgt>` | 617 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>少し弱気な</tgt>` | 1362 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点点。</src><tgt>程度です。</tgt>` | 1201 |

---

### Test Example 36 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new, </src><tgt>没什么新鲜事，</tgt>` | 1098 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there are </src><tgt><\|wait\|></tgt>` | 1091 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such instances before </src><tgt>以前就有过这样的例子，</tgt>` | 1487 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1471 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>netfilterTC, </src><tgt>在netfilterTC中，</tgt>` | 1775 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>and so </src><tgt>所以</tgt>` | 1337 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 379 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>this is just one </src><tgt>这只是</tgt>` | 1744 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>another place where </src><tgt>另一个地方，</tgt>` | 1637 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2194 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>what the developer </src><tgt><\|wait\|></tgt>` | 768 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1479 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>or engineer's work in the bug reports </src><tgt>开发者或工程师在bug报告中</tgt>` | 1675 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>应该注意到的。</tgt>` | 1280 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10</src><tgt><\|wait\|></tgt>` | 1024 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>見てとか</src><tgt><\|wait\|></tgt>` | 972 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですかとか恐らく</src><tgt><\|wait\|></tgt>` | 1082 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>10秒</src><tgt><\|wait\|></tgt>` | 1294 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>でまあ</src><tgt><\|wait\|></tgt>` | 1124 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>1秒に</src><tgt><\|wait\|></tgt>` | 1475 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>言って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね</src><tgt><\|wait\|></tgt>` | 967 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>と</src><tgt><\|wait\|></tgt>` | 1680 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1790 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1505 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11</src><tgt><\|wait\|></tgt>` | 1402 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>見てで</src><tgt><\|wait\|></tgt>` | 1520 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 772 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1076 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>から。</src><tgt><\|wait\|></tgt>` | 1197 |

---

### Test Example 38 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src>这一张的部分呢，</src><tgt>이 부분은</tgt>` | 1023 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 840 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1095 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>一个戴雪的人，但是</src><tgt>눈을 덮은 사람을 보여줍니다. 하지만</tgt>` | 1929 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>它是属于逆向的，</src><tgt>이것은 역방향입니다.</tgt>` | 1912 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1334 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>这通场法嘛，</src><tgt>이 통장법은</tgt>` | 1148 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>这样的一个状况</src><tgt>이런 상황이</tgt>` | 1859 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>需要去特别注意的是</src><tgt>특별히 주의해야 할 점입니다.</tgt>` | 1894 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 2108 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>能够得到</src><tgt><\|wait\|></tgt>` | 655 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>于他去掉</src><tgt><\|wait\|></tgt>` | 1450 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>于你的意识</src><tgt><\|wait\|></tgt>` | 1565 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>哦。</src><tgt>그가 당신의 의식을 잃게 하는 것을 막을 수 있는지 여부입니다.</tgt>` | 1455 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 962 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알거니화. </src><tgt>知っているでしょう。</tgt>` | 977 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>너희가 </src><tgt><\|wait\|></tgt>` | 1078 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인 으로 있을 때에 </src><tgt>異邦人として</tgt>` | 1507 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1543 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>말 못하 는 우선 에게로 </src><tgt>話せない者たちに</tgt>` | 1762 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1360 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>그대로 흘려 </src><tgt><\|wait\|></tgt>` | 1636 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>갔느니라. </src><tgt>そのまま流されたのです。</tgt>` | 1768 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 </src><tgt>ですから、</tgt>` | 1031 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>내가 너희 에게 </src><tgt>私があなたたちに</tgt>` | 2018 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>知らせるのです。</tgt>` | 1589 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | 1564 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>語る者は、</tgt>` | 1154 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 746 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt>그렇다면</tgt>` | 1103 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう寝かせている。</src><tgt>이미 잠들게 두는 거지.</tgt>` | 1063 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt>나는</tgt>` | 992 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt><\|wait\|></tgt>` | 1270 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>血記事を見ている。</src><tgt>지금 혈기( 血記事) 를 보고 있어.</tgt>` | 1422 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1646 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>이제</tgt>` | 1060 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えている</src><tgt><\|wait\|></tgt>` | 956 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不烈の気性よ。</src><tgt>한계가 넘어서지 않았어, 부렬의 기세야.</tgt>` | 2597 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1197 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 2124 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船団を</src><tgt><\|wait\|></tgt>` | 663 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってるだろう。</src><tgt>오랫동안 선단을 운영해왔을 텐데.</tgt>` | 1569 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt>나는 이렇게 대단한</tgt>` | 1542 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>海賊船を見た</src><tgt>해적선을</tgt>` | 1204 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>ことがない。</src><tgt>본 적이 없어.</tgt>` | 783 |

---

### Test Example 41 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어떻게 보면 </src><tgt>嗯，怎么说呢，</tgt>` | 1040 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1090 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1252 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 </src><tgt><\|wait\|></tgt>` | 1626 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>같은 동생 이잖아. </src><tgt>他就是那个和我们一起经历过二十岁的弟弟，也是家人一样的弟弟。</tgt>` | 2016 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt>所以</tgt>` | 1607 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>嗯，</tgt>` | 896 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생 한 거라 는 </src><tgt><\|wait\|></tgt>` | 1492 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 2150 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 542 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1459 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 1590 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>잘 넣고 </src><tgt><\|wait\|></tgt>` | 1134 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>생각 했습니다. </src><tgt>我试着自己想了些东西，</tgt>` | 991 |

---

### Test Example 42 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt>だから</tgt>` | 984 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>もちろん、</tgt>` | 827 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>이런 경우 들이 있습니다. 저희 가 </src><tgt>こういうケースもあります。</tgt>` | 1219 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>Aさんと</tgt>` | 1167 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람 이 </src><tgt>Bさんが</tgt>` | 877 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 콘텐츠 예요. </src><tgt>お互いにコンテンツを共有している場合です。</tgt>` | 2178 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 </src><tgt>そういった</tgt>` | 1072 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>콘텐츠 예요. 그리고 </src><tgt>コンテンツがある場合です。そして、</tgt>` | 1309 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | 1756 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪意のあるコードを</tgt>` | 1903 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>주었을 때 </src><tgt>送ったときに、</tgt>` | 2470 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비라는 사람 이 </src><tgt>Bさんが</tgt>` | 831 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 934 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로스 사이트 크리티 에서 </src><tgt>クロスサイトクリティカル（XSS）で</tgt>` | 1789 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>JSP까지 </src><tgt>JSPまで</tgt>` | 1225 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>가능 이 될까. </src><tgt>到達できるか、</tgt>` | 836 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて</tgt>` | 1318 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>색인 번호 를 </src><tgt>色番号を</tgt>` | 928 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>選んでください。</tgt>` | 1070 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 서름이 돋든 </src><tgt>今、</tgt>` | 1402 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>가짜 이 돋든 </src><tgt>本物でも偽物でも、</tgt>` | 1977 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>느낌 이 </src><tgt><\|wait\|></tgt>` | 1302 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>오면 이걸 흔들 어서 </src><tgt>感じたら、それを振って</tgt>` | 1628 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぶってこと。</tgt>` | 1957 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>귀신 이 오면 </src><tgt>お化けが来たら</tgt>` | 1853 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>噛まれるし、</tgt>` | 2462 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>새니 이 오면 </src><tgt>刺されるし、</tgt>` | 1598 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>お前を守るために</tgt>` | 1352 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>찔러 주잖아. 그러니까 </src><tgt>刺してくれてるんだ。だから</tgt>` | 716 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>リラックスして</tgt>` | 1168 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | 756 |

---

### Test Example 44 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1171 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉</src><tgt><\|wait\|></tgt>` | 929 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt>相手の感情を</tgt>` | 1088 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>或真实意图的，</src><tgt>推し量ったり感じ取ったりする。</tgt>` | 1641 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1584 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1334 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1509 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>好经常会听到</src><tgt><\|wait\|></tgt>` | 435 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>人们这样说：“</src><tgt>人々はよく</tgt>` | 1754 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>こう言う。「見て、</tgt>` | 1716 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt>この人は</tgt>` | 2128 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在作谎了。”</src><tgt>また嘘をついているよ」って。</tgt>` | 907 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>その目は</tgt>` | 1272 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>すべてを物語っている。</tgt>` | 1627 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1102 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 706 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt>言っているんだ。</tgt>` | 453 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1139 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational entertainment. </src><tgt>교육적인 엔터테인먼트.</tgt>` | 1039 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1099 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? </src><tgt>당신은 교육을 얼마나 받았나요?</tgt>` | 1567 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>고등학교를 졸업했나요?</tgt>` | 1985 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt>그것은</tgt>` | 1424 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>of entertainment. </src><tgt>엔터테인먼트의 한 단계일 뿐입니다.</tgt>` | 2272 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>대학에 갔나요?</tgt>` | 1597 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>And if so, </src><tgt>만약 그렇다면,</tgt>` | 2443 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>졸업했나요?</tgt>` | 1582 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of entertainment. </src><tgt>그것은 또 다른 단계의 엔터테인먼트입니다.</tgt>` | 1353 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>그래서</tgt>` | 504 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>여기까지입니다. 다음에</tgt>` | 1397 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 771 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1131 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 828 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인 다면 </src><tgt>If the stock index is on an upward trend,</tgt>` | 2007 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이러 면 대형 주도 </src><tgt>then</tgt>` | 1010 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 1163 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1567 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 </src><tgt>large- cap stocks will also rise sharply.</tgt>` | 1570 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 가벼운 </src><tgt><\|wait\|></tgt>` | 1787 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt>But first,</tgt>` | 1793 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 2057 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이 기 </src><tgt><\|wait\|></tgt>` | 887 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>때문 에 </src><tgt>because lighter stocks lead the market,</tgt>` | 1550 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 리 초의 </src><tgt><\|wait\|></tgt>` | 1591 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1148 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 907 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>we should keep an eye on those lighter stocks.</tgt>` | 697 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1072 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then self </src><tgt>活動、</tgt>` | 953 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>defining what we think </src><tgt><\|wait\|></tgt>` | 1107 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is, </src><tgt>そして自分自身で、自分たちが考える基準を定義します。</tgt>` | 1705 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>because you're absolutely correct </src><tgt>なぜなら、</tgt>` | 1948 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1139 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>but the reality is that </src><tgt>その考えは完全に正しいのですが、現実は</tgt>` | 1540 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on </src><tgt>私たちが</tgt>` | 1954 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, and because this </src><tgt>新しいブロックの住人だからです。そして、</tgt>` | 1973 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>基準が</tgt>` | 2274 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1450 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前に変わってから、</tgt>` | 651 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1382 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard </src><tgt>私たちはより高い基準を</tgt>` | 1240 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>求められています。なぜなら、今の状況では</tgt>` | 862 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 662 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1301 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 914 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맵니다. </src><tgt>进入的时候，会非常迷茫。</tgt>` | 1695 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전 을 할 건 </src><tgt><\|wait\|></tgt>` | 947 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1543 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>거로 거로 다니 고는 </src><tgt><\|wait\|></tgt>` | 1660 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1466 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1683 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 는 것도 </src><tgt><\|wait\|></tgt>` | 1808 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>장렬 이요. </src><tgt>开车的话，如果开到果罗果罗，说不定还要去江北，更不用说出国，都是很惨烈。</tgt>` | 2973 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>좀 챙기 야 </src><tgt>得好好照顾</tgt>` | 1568 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>네요. 대신 에 이제 </src><tgt>一下了。不过，</tgt>` | 1564 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 868 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>무뤄요. 그거 는 </src><tgt>我会努力的。那个</tgt>` | 789 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>내일 있는 것 같아요. </src><tgt>好像是明天的事。</tgt>` | 773 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 591 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt>So, this is</tgt>` | 1195 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 961 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>という出じゃなくて、</src><tgt>not a visual development environment,</tgt>` | 1533 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 944 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>but a Visual Python development environment.</tgt>` | 2269 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも、</src><tgt>That's because</tgt>` | 1472 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルの書いて</src><tgt><\|wait\|></tgt>` | 1119 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>後、それは</src><tgt>you write the flow graph visually,</tgt>` | 1975 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコード、</src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成される、それが</src><tgt>and then it generates Python code from that,</tgt>` | 2751 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt>which is then executed,</tgt>` | 1609 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われる</src><tgt><\|wait\|></tgt>` | 1538 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>っていうところに</src><tgt><\|wait\|></tgt>` | 701 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているから</src><tgt>and that's where the signal processing happens.</tgt>` | 966 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 728 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はい。じゃあ、</src><tgt>Okay, so,</tgt>` | 632 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そして、これについて</tgt>` | 893 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>多くの人が</tgt>` | 897 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석 을 해놓았습니다. </src><tgt>分析をしています。</tgt>` | 1483 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 910 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>로쿠자 내부 냄새 를 보시면 </src><tgt>ロクジャの内部の匂いを</tgt>` | 1913 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니가 </src><tgt>見ると、ソニーが</tgt>` | 1545 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>이력 칩에 </src><tgt>イエロジックチップに</tgt>` | 1545 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>FP 파이 를 </src><tgt>FPファームを</tgt>` | 1789 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>128ビットに</tgt>` | 1873 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>나중 가서 로프인들. </src><tgt>落とし、後でローピンしている。</tgt>` | 2725 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1543 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈 엑스에서도 없는 </src><tgt>XboxシリーズのXboxでもない</tgt>` | 1595 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 983 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュ</tgt>` | 670 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>S가 여기 도 없다. </src><tgt>Sもここにはない。</tgt>` | 807 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 549 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So </src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>also, you will not </src><tgt>另外，</tgt>` | 815 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>be able to move </src><tgt>你将无法</tgt>` | 1035 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>me-media objects </src><tgt><\|wait\|></tgt>` | 1191 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 867 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt><\|wait\|></tgt>` | 1668 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>so, </src><tgt>在资源之间移动me-media对象，所以</tgt>` | 1595 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 1293 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where you </src><tgt>如果你遇到</tgt>` | 1886 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt>发现</tgt>` | 1683 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 2146 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource </src><tgt><\|wait\|></tgt>` | 798 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>in the URL as now. </src><tgt>将错误的媒体文件添加到了URL中的特定资源中，</tgt>` | 1639 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>And we can see about </src><tgt>我们就可以</tgt>` | 1505 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those media </src><tgt><\|wait\|></tgt>` | 1117 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>files and then making sure </src><tgt>尝试移动这些媒体文件，并确保</tgt>` | 1062 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 593 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>它们能正确备份。</tgt>` | 413 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 918 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>フロア1の所得</src><tgt>1층의</tgt>` | 973 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>決直到的額向</src><tgt>소득 결정액은</tgt>` | 1421 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>美当我们在储于</src><tgt><\|wait\|></tgt>` | 1486 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>爱之中的</src><tgt>우리가 사랑하는</tgt>` | 1681 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>所谓的爱</src><tgt>그 소위 사랑에</tgt>` | 1559 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1651 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>我们何时进入</src><tgt>언제</tgt>` | 1316 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 966 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>恨，在掌上的时候，</src><tgt>분노에 빠져서 손에 쥐고 있을 때</tgt>` | 2732 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>它是爱。</src><tgt>그것은 사랑입니다.</tgt>` | 1502 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | 1372 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>它就变成</src><tgt>그것은</tgt>` | 416 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1242 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>恨那个种百，</src><tgt>그 ' 100번 분노' 로 변합니다.</tgt>` | 880 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 618 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>继续在移动。</src><tgt>계속 움직입니다.</tgt>` | 438 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1364 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 890 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section of </src><tgt><\|wait\|></tgt>` | 1141 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>the AHR field </src><tgt><\|wait\|></tgt>` | 1268 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1644 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1414 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 568 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1675 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, which is obviously </src><tgt><\|wait\|></tgt>` | 1845 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>not of my loves. </src><tgt><\|wait\|></tgt>` | 1974 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 958 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1576 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1388 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these </src><tgt><\|wait\|></tgt>` | 432 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 1281 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 836 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 657 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 442 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point </src><tgt>ある時点では、</tgt>` | 980 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>in Noah's Genesis </src><tgt>ノア記の</tgt>` | 935 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>3:13, </src><tgt>3章13節に、</tgt>` | 1682 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that he's going </src><tgt><\|wait\|></tgt>` | 992 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>to the flood </src><tgt>彼は洪水に</tgt>` | 1682 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in the wilderness forty days </src><tgt>40日間、</tgt>` | 1438 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>or more, that he's hungry </src><tgt>あるいはそれ以上、</tgt>` | 1508 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>and so he says to </src><tgt>飢えを</tgt>` | 1847 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>Jesus, hey, if you're </src><tgt>感じていた。だから彼はイエスに言った。「おい、</tgt>` | 2252 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>the Son of God, prove it." </src><tgt>神の子なら証明してみろ」と。</tgt>` | 2370 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1481 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えろ」と。</tgt>` | 1634 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1102 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>How did Jesus deal with that </src><tgt>イエスはどう対処したのか、</tgt>` | 944 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>imitation? </src><tgt>その模倣にどう対処したのか。</tgt>` | 704 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 446 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Man Jonathan led by </src><tgt>男のヨナタンは</tgt>` | 405 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>brae alone. </src><tgt>一人でブラエを率いて行った。</tgt>` | 455 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1208 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful, </src><tgt><\|wait\|></tgt>` | 747 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1025 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 794 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. And I don't know </src><tgt>有意义的、个人的权利，最高法院最后才做出裁决，而不是主导。我不知道</tgt>` | 3234 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>if the courts want to be </src><tgt>法院是否想</tgt>` | 1432 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1674 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1734 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>成为社会变革的先锋。</tgt>` | 1336 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>如今，</tgt>` | 1607 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1537 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src>but they rather reflect </src><tgt>但它们更多地反映了</tgt>` | 899 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 926 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the consensus that's already </src><tgt>已经形成的共识，</tgt>` | 1299 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>即</tgt>` | 699 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt>已经浮现出来的共识。</tgt>` | 593 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>you have </src><tgt>所以，</tgt>` | 460 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt>你有一些联邦法官</tgt>` | 404 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 417 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>……</tgt>` | 267 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>그럼</tgt>` | 984 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片呢，</src><tgt>그림을 한번 볼까요?</tgt>` | 989 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1062 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的不分呢，</src><tgt>그림의 분할은</tgt>` | 1494 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1447 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>的一个食吞的部分。</src><tgt>식도 부분으로 볼 수 있습니다.</tgt>` | 1874 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1455 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>那克吞一般都是</src><tgt>식도 분할은 보통</tgt>` | 1907 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>属于我们在</src><tgt><\|wait\|></tgt>` | 1726 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2248 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>吸收的地方，所以呢，</src><tgt>우리가 흡수하는 부분에 해당합니다. 그래서</tgt>` | 1170 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分</src><tgt>이것이</tgt>` | 1068 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>呢，会反映的是</src><tgt>신체의 부분은</tgt>` | 1562 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1096 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 712 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 516 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>可以好好的坐下来休息</src><tgt><\|wait\|></tgt>` | 651 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>可不？我们可以看到</src><tgt>잠시 앉아서 쉴 수 있는 시간을 갖는 것이 필요하다는 것을 반영합니다. 괜찮으신가요? 그림을 보면</tgt>` | 765 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>这边是恐武一人的吗？</src><tgt>여기에 ' 공무일인' 이 한 명만 있는 것 같네요.</tgt>` | 514 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt>좋습니다.</tgt>` | 331 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>说一</src><tgt><\|wait\|></tgt>` | 322 |

---

### Test Example 57 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>これらの人々は</tgt>` | 960 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>非常に稀で、</tgt>` | 917 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1088 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>and they often show up </src><tgt>よく</tgt>` | 1341 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1362 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するような形で現れます。</tgt>` | 2051 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1439 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その性格は</tgt>` | 1642 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾をはらんでいます。</tgt>` | 1757 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1058 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 1969 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ですが、</tgt>` | 1619 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1181 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations, </src><tgt>無意味な会話も嫌います。</tgt>` | 738 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1162 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to </src><tgt><\|wait\|></tgt>` | 834 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>the point. </src><tgt>そして、要点をまっすぐ言うのが好きです。</tgt>` | 712 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love to </src><tgt>彼らは</tgt>` | 439 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 408 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>play the devil's advocate, </src><tgt>悪魔の代弁者も好みます。</tgt>` | 434 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 345 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>and never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 433 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 399 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. stands for </src><tgt>E.T.P.は</tgt>` | 450 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>for. </src><tgt>forの略です。</tgt>` | 297 |

---

### Test Example 58 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 991 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1313 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1303 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 894 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1860 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1365 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1497 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>had made quite a show of himself, claiming he had rejected the government for the sake of the candidate's victory. But now,</tgt>` | 3306 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 877 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 2212 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1578 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석은 들은 해 놓고 </src><tgt>the moment Yoon Suk- yeol removed Kim Jong- in,</tgt>` | 1659 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1129 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 927 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기 를 </src><tgt><\|wait\|></tgt>` | 428 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>뿜은 공격 성을 </src><tgt><\|wait\|></tgt>` | 513 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 448 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 406 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>것입니다. </src><tgt>Lee Jun- seok was determined to attack Yoon Suk- yeol, showing his venom to bring him down.</tgt>` | 572 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 270 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석의 성상급언 </src><tgt><\|wait\|></tgt>` | 401 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 398 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 375 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 353 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt>How much of a boon is this for the Democratic Party's attack on Lee Jun- seok?</tgt>` | 539 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1084 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後ね今</src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので</src><tgt>I'd like to make something after a meal now.</tgt>` | 1558 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>ここで</src><tgt><\|wait\|></tgt>` | 904 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>このゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | 1247 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1354 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1641 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 717 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>I'm planning to have breakfast at the Goldstone Hotel here.</tgt>` | 2300 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1363 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | 2273 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 660 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt>If you're thinking of staying at the Goldstone Hotel in the future,</tgt>` | 1670 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさ</src><tgt><\|wait\|></tgt>` | 1390 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>てもってみてもまあいいんじゃない</src><tgt>I think it's a good place to consider.</tgt>` | 1457 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt>Yes.</tgt>` | 751 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt>I think so.</tgt>` | 548 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>ここホテルからですね</src><tgt>From here, from the hotel,</tgt>` | 459 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 350 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 420 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 285 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんないか</src><tgt><\|wait\|></tgt>` | 377 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 359 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>リッチのねまあホテル</src><tgt><\|wait\|></tgt>` | 420 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt>you can walk to Busan Station in about a minute or so. So, the hotel is</tgt>` | 594 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>翌ったらですね</src><tgt>really close.</tgt>` | 281 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 267 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それでは</src><tgt>Please consider staying there.</tgt>` | 272 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>ね今回は</src><tgt>That's it for this time.</tgt>` | 278 |

---

### Test Example 60 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>まあ</src><tgt>嗯，</tgt>` | 1065 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>だんだんちょっと距離が</src><tgt><\|wait\|></tgt>` | 908 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じで</src><tgt>感觉距离在慢慢拉开，</tgt>` | 1157 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>大将が</src><tgt>大将</tgt>` | 1151 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>タタタタポイですね。</src><tgt>好像在说“哒哒哒哒波伊”。</tgt>` | 1587 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>海遊して</src><tgt><\|wait\|></tgt>` | 1590 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>いか型ってすぐイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイ` | 11235 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>イイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイ` | 5364 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>イイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイ` | 2558 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>イイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイ` | 1516 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>イイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイイ` | 1530 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なので</src><tgt>所以</tgt>` | 150 |
