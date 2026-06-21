# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9652
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3642
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 683
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 0.7614
  - TGT_RELEASE_TOTAL: 88
  - TGT_WAIT_ACCURACY: 0.8061
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1393.8610
  - PROCESS_TIME_MS_P50: 1316.7020
  - PROCESS_TIME_MS_P95: 2341.7920
  - PROCESS_TIME_MS_MAX: 3988.9620

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 847 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの</src><tgt>从一开始</tgt>` | 943 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>特に仲まだ</src><tgt><\|wait\|></tgt>` | 1193 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>就不是一年级学生。</tgt>` | 1330 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点</src><tgt><\|wait\|></tgt>` | 1553 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>でこう身近く</src><tgt>到了那个时候，</tgt>` | 1521 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選択を</src><tgt><\|wait\|></tgt>` | 1035 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう退ず</src><tgt><\|wait\|></tgt>` | 1529 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>してあげると</src><tgt>如果能让孩子选择退学，</tgt>` | 2418 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>受験立てても</src><tgt><\|wait\|></tgt>` | 1822 |
| 11 | `<src>大した。</src><tgt>十年后也不会有什么大……</tgt>` | `<src>退した。</src><tgt>就算考上了，也会退学。</tgt>` | 920 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1214 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 1040 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>是容易的，但是</src><tgt>気数を気にするのは簡単ですが、</tgt>` | 1372 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>只有一个</src><tgt><\|wait\|></tgt>` | 1301 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导</src><tgt>師匠の指導が</tgt>` | 1644 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1253 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>突破于中年。</src><tgt>中年の突破口になるんです。</tgt>` | 1262 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1199 |
| 9 | `<src>虚阿凡</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>だからこそ、反省が必要なんです。</tgt>` | 2415 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 1777 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师傅，</src><tgt>師匠になるためには、</tgt>` | 931 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1356 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是</src><tgt>What parents need to do is</tgt>` | 1482 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 780 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们身生的爱</src><tgt><\|wait\|></tgt>` | 1702 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>交水，</src><tgt>exchange love with our children,</tgt>` | 1820 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十分爱，</src><tgt><\|wait\|></tgt>` | 980 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>去育</src><tgt><\|wait\|></tgt>` | 1550 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心灵养养。</src><tgt>show them deep love, and nurture their spirits.</tgt>` | 943 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2241 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>你耐心等</src><tgt><\|wait\|></tgt>` | 2100 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢长大。</src><tgt>Be patient as your child grows up.</tgt>` | 1047 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1303 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>在宿舍里</src><tgt>Why</tgt>` | 883 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这样子？这个优生院很大，</src><tgt><\|wait\|></tgt>` | 1366 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src>然后</src><tgt>is it like this in the dorm? The Institute of Biology is huge,</tgt>` | 2119 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1328 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt>and then I'm on vacation</tgt>` | 1319 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人，</src><tgt><\|wait\|></tgt>` | 1799 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>with Tao Ren,</tgt>` | 900 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>可以吗？</src><tgt><\|wait\|></tgt>` | 1943 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt>can I?</tgt>` | 2225 |
| 11 | `<src>仁儿。</src><tgt>this kind of walnut kernels.</tgt>` | `<src>和陶人？</src><tgt><\|wait\|></tgt>` | 1572 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1249 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘撒完以后呢，</src><tgt>淘洗いが終わった後、</tgt>` | 1834 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的亚力检清</src><tgt><\|wait\|></tgt>` | 920 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也</src><tgt>内部の亜力も</tgt>` | 1200 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷除了，然后</src><tgt><\|wait\|></tgt>` | 1711 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>就停留在</src><tgt>刷り落とされて、</tgt>` | 1198 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1800 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 900 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>运行状态。</src><tgt>比較的低エネルギーの稼働状態に留まります。</tgt>` | 2005 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 2091 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>异域状态。</src><tgt>これがいわゆる異域状態です。</tgt>` | 1974 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 1117 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1107 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼봉심이 </src><tgt><\|wait\|></tgt>` | 1461 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>서울봉심이가 </src><tgt><\|wait\|></tgt>` | 1684 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1220 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>석연하는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1308 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1296 |
| 9 | `<src>진짜 이거 </src><tgt>Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 2243 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해행으로 </src><tgt><\|wait\|></tgt>` | 1166 |
| 11 | `<src>진짜. </src><tgt>seriously killer for a hangover, for real.</tgt>` | `<src>조금 죽입니다. </src><tgt>I'm actually a sword- enthusiast. Seoul Sword Enthusiast is quite open about it. Wow, I'm really going to kill this with a sword.</tgt>` | 3183 |

---

### Test Example 7 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1410 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스들은 </src><tgt>The Nics on the list</tgt>` | 1330 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 812 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1576 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1580 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1418 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스들이 </src><tgt><\|wait\|></tgt>` | 1476 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>있었기 때문 입니다. </src><tgt>were actually not highly intelligent. They were just randomly selected.</tgt>` | 1148 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2139 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 2159 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교사 들은 </src><tgt>The teachers who didn't know the truth</tgt>` | 2150 |

---

### Test Example 8 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1227 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>从这附近开始，</tgt>` | 1126 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まった</src><tgt><\|wait\|></tgt>` | 1025 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので</src><tgt>大概是从</tgt>` | 1190 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1557 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ご言やん</src><tgt>“ご法ご言やん”</tgt>` | 1741 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1137 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>生産の</src><tgt>的生产</tgt>` | 1335 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1981 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の</src><tgt><\|wait\|></tgt>` | 749 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵</src><tgt><\|wait\|></tgt>` | 2065 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1964 |

---

### Test Example 9 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 940 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 1154 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1122 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1284 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt>紧张感从哪里开始？</tgt>` | 1931 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>What is it? </src><tgt><\|wait\|></tgt>` | 1162 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt>是什么？是头？</tgt>` | 1911 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it a tension in your chest? </src><tgt><\|wait\|></tgt>` | 1076 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it a </src><tgt>还是胸口有紧张？</tgt>` | 1857 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>low language you use </src><tgt><\|wait\|></tgt>` | 2218 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>say. </src><tgt>还是你使用的语言太低级了？</tgt>` | 2028 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 1057 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>我们就是</src><tgt>In the face of this situation,</tgt>` | 1232 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 931 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的</src><tgt><\|wait\|></tgt>` | 1363 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>回报主管或是通知对方</src><tgt><\|wait\|></tgt>` | 1793 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们下了这个状况，</src><tgt>we just quickly report it to our supervisor or notify them that we've encountered this situation.</tgt>` | 1967 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1737 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't think you have to handle everything on your own.</tgt>` | 2468 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>努力承担。</src><tgt><\|wait\|></tgt>` | 1967 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>整体而言，</src><tgt>Overall,</tgt>` | 689 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是给做Solution。</src><tgt><\|wait\|></tgt>` | 1891 |

---

### Test Example 11 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Chunato Teru. </src><tgt>제 이름은 테루 츄나토입니다.</tgt>` | 1914 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 692 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1299 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in actuarial finance </src><tgt><\|wait\|></tgt>` | 1579 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of </src><tgt><\|wait\|></tgt>` | 1304 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>psychology. </src><tgt>현재 보험 계리 및 심리학 학사 학위를 공부하고 있습니다.</tgt>` | 1998 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 1570 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt>여기 예일에서</tgt>` | 1243 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 2076 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt>배우고 있습니다. 앞으로는</tgt>` | 1043 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1475 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 877 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1222 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people? This is </src><tgt>極度に幸せな人たちを対象にした研究は行いましたか？</tgt>` | 2188 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1568 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. </src><tgt>これは先端的な研究です。</tgt>` | 1084 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at 10% </src><tgt><\|wait\|></tgt>` | 1907 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>10%の</tgt>` | 1733 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1034 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People who </src><tgt>最も幸せな人たちを見ています。彼らは</tgt>` | 2627 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1963 |

---

### Test Example 13 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 </src><tgt><\|wait\|></tgt>` | 1324 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>너무 </src><tgt><\|wait\|></tgt>` | 850 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>이 절여야 될 수 있지만 </src><tgt>これは、あまりにも</tgt>` | 1336 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1745 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt>崇めるべきものではないかもしれませんが、本当に菩薩様でなければ、</tgt>` | 2309 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt><\|wait\|></tgt>` | 1125 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 보이 고 </src><tgt>夢かと思えるくらい、</tgt>` | 1718 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 2123 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보이 려고 </src><tgt>私だけが菩薩様に見えようとして</tgt>` | 813 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>보이 세 우주가 </src><tgt><\|wait\|></tgt>` | 1966 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>진다 한 때 보살 이란 </src><tgt>宇宙が崩壊する</tgt>` | 2101 |

---

### Test Example 14 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1305 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 947 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1163 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learned and to repeat </src><tgt><\|wait\|></tgt>` | 1225 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out if you're good at </src><tgt><\|wait\|></tgt>` | 2093 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>重复一下。学习一下，看看自己是否擅长，然后多做一些。</tgt>` | 1906 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good </src><tgt><\|wait\|></tgt>` | 1951 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>at it. </src><tgt>嗯，如果你不擅长的话，</tgt>` | 2310 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>Get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 2116 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>就让身边的人来帮你</tgt>` | 1075 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and and tell them next time </src><tgt><\|wait\|></tgt>` | 1571 |

---

### Test Example 15 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1092 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 로 슉빠르 시키고 </src><tgt><\|wait\|></tgt>` | 1471 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1429 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1564 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>머리 를 </src><tgt><\|wait\|></tgt>` | 1260 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>조깅 해려나 </src><tgt><\|wait\|></tgt>` | 1523 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1031 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 2256 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들인 </src><tgt><\|wait\|></tgt>` | 2472 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>가입니다. </src><tgt>I'm a fast- learner, and I'm from the same generation as Park Han- sang.</tgt>` | 2412 |

---

### Test Example 16 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 산줄에 </src><tgt><\|wait\|></tgt>` | 1077 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1332 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이기로 하도루아 수도 </src><tgt><\|wait\|></tgt>` | 1993 |
| 5 | `<src>다른 잔찜에 </src><tgt>came in here to do it.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1459 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔줄에 죽여달라고 </src><tgt><\|wait\|></tgt>` | 1321 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>해자나. 내가 </src><tgt><\|wait\|></tgt>` | 1951 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt><\|wait\|></tgt>` | 2198 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>안 듣고 있는 줄 알아내냐? </src><tgt><\|wait\|></tgt>` | 535 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>어? </src><tgt>You want me to kill someone on another mountain, so I'm going to kill them. You want me to kill someone on another mountain? You think I don't hear that? Huh?</tgt>` | 3989 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 773 |

---

### Test Example 17 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1362 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 963 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あのいただくもらえる</src><tgt><\|wait\|></tgt>` | 1182 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1365 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので、ぜひ</src><tgt>We also have things like T-shirts available for you to receive,</tgt>` | 2552 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 941 |
| 7 | `<src>ご連絡としては</src><tgt>so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt>so please join us. For contact,</tgt>` | 2031 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>はいジョイになります</src><tgt><\|wait\|></tgt>` | 1992 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>で、えっと</src><tgt>we'll be using the Joy system.</tgt>` | 756 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ね、</src><tgt><\|wait\|></tgt>` | 2178 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>人数が</src><tgt>Um,</tgt>` | 1824 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ありますので少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1036 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 942 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>그렇습니다. 그래서</tgt>` | 1037 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天気</src><tgt><\|wait\|></tgt>` | 1138 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>を</src><tgt><\|wait\|></tgt>` | 1072 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>チェックしましたね。</src><tgt>날씨를 확인했죠.</tgt>` | 1609 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1663 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>그리고</tgt>` | 745 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井清氏の</src><tgt><\|wait\|></tgt>` | 1931 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>仕組みは</src><tgt>나가이 세이치 씨의 시스템은</tgt>` | 2473 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>五個</src><tgt><\|wait\|></tgt>` | 1844 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>チェック</src><tgt><\|wait\|></tgt>` | 725 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>五個</src><tgt><\|wait\|></tgt>` | 1807 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt>5가지입니다.</tgt>` | 1026 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 891 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt>제가</tgt>` | 884 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我的生活</src><tgt><\|wait\|></tgt>` | 1162 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>在一个轨道，让我</src><tgt>제 삶의 궤도 안으로 돌아가게 해 주세요.</tgt>` | 1806 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>能够好好的</src><tgt><\|wait\|></tgt>` | 1511 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在它下面的时候，</src><tgt>그 아래에서 잘 지낼 수 있도록,</tgt>` | 1563 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日航</src><tgt><\|wait\|></tgt>` | 1818 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>日航的</src><tgt><\|wait\|></tgt>` | 1460 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>时候，我当时</src><tgt>당시 ' 니혼카이 ' 를 할 때,</tgt>` | 1521 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>背到</src><tgt><\|wait\|></tgt>` | 2141 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>做作业小小的愿望</src><tgt>숙제를 하던 작은 소망이</tgt>` | 2022 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>好。</src><tgt><\|wait\|></tgt>` | 1073 |

---

### Test Example 20 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1364 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>And then, </src><tgt>好的。然后，</tgt>` | 1113 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1162 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1587 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1318 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1102 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1381 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1939 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>这些例子之后，指令告诉我们实际使用这些值。所以</tgt>` | 849 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2234 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>this game dot word array </src><tgt><\|wait\|></tgt>` | 1997 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1307 |

---

### Test Example 21 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 915 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAがですね</src><tgt>As for AA,</tgt>` | 1036 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1187 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>いい制服かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1651 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>を考えるときに、</src><tgt>when we consider whether it's a good uniform in various situations,</tgt>` | 2440 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAAの</src><tgt><\|wait\|></tgt>` | 841 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ランキング調べで</src><tgt>in our AA ranking survey,</tgt>` | 1887 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あの制服かどうか</src><tgt><\|wait\|></tgt>` | 1981 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>の調査する制服で</src><tgt><\|wait\|></tgt>` | 889 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt><\|wait\|></tgt>` | 2266 |
| 11 | `<src>といったような</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1861 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt>they've made sure to use it for surveys on whether it's a uniform.</tgt>` | 1466 |

---

### Test Example 22 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>就是</src><tgt>2つ目は</tgt>` | 871 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>进入二吉星</src><tgt><\|wait\|></tgt>` | 1312 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>会福，</src><tgt>二吉星に入ります。</tgt>` | 1226 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一吉一线</src><tgt><\|wait\|></tgt>` | 1574 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>平安的大牛们。</src><tgt>平安な牛たちです。</tgt>` | 1604 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1013 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做</src><tgt>例えば、</tgt>` | 1564 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>维兴运动好事几年，</src><tgt><\|wait\|></tgt>` | 2131 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>維興運動を数年間続けていると、</tgt>` | 640 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维兴运动好平分</src><tgt><\|wait\|></tgt>` | 2347 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的星膀</src><tgt>維興運動の星膀が</tgt>` | 2050 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1417 |

---

### Test Example 23 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>あとなんか</src><tgt><\|wait\|></tgt>` | 1369 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>ちょっと距離が</src><tgt>还有，</tgt>` | 955 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じで</src><tgt><\|wait\|></tgt>` | 1265 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>オーシャラーとかで</src><tgt>感觉距离有点远，</tgt>` | 1810 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>パパおいでですね。</src><tgt><\|wait\|></tgt>` | 1815 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>海遊したい方って</src><tgt>像在海洋馆里看海豚一样。想去海洋馆的人</tgt>` | 1740 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐに行こう意識が</src><tgt><\|wait\|></tgt>` | 1618 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>来しい。</src><tgt>会很快就意识到要去。</tgt>` | 2235 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>でジュネズミと</src><tgt><\|wait\|></tgt>` | 613 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>トモンチンネオトボトシャ</src><tgt>然后</tgt>` | 2187 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>が強くて</src><tgt><\|wait\|></tgt>` | 1850 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt>因为ジュネズミ和トモンチンネオトボト强，所以</tgt>` | 1723 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1259 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 1036 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1168 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>緩むと</src><tgt>기어가 헐거워지면</tgt>` | 1285 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えなくなって</src><tgt><\|wait\|></tgt>` | 1963 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>しまうので、</src><tgt>신호가 꺼지게 되니까</tgt>` | 1491 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1818 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>逆ネジの</src><tgt>기어 끝에</tgt>` | 640 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 2258 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>ついてるっていうこと</src><tgt>역나사 너트가</tgt>` | 2367 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1881 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>붙어 있다는 거죠.</tgt>` | 827 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 1396 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1301 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt>あるいは、</tgt>` | 855 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1132 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何かを書く必要がある場合、</tgt>` | 1707 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1570 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>テキストを書くとき、</tgt>` | 1446 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1757 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. It's like oh, </src><tgt>単語のスペルが全くわからないことに気づく。まるで「あ、</tgt>` | 1475 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1411 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>started with a double </src><tgt>この単語は</tgt>` | 2093 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 855 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>P, double L, I don't know </src><tgt>PPで始まってる？LLで始まってる？わからない</tgt>` | 2220 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1356 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 945 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼</tgt>` | 1184 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1094 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. And when those </src><tgt>화학 결합도 에너지를 저장합니다. 그리고</tgt>` | 2503 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1696 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>결합이 끊어지면</tgt>` | 1185 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1481 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>그 잠재 에너지는 다른 형태의 에너지로</tgt>` | 2485 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 2041 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>변환됩니다. 예를 들어 열이나 빛 같은 것들이죠. 아니면</tgt>` | 1812 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make different bonds. </src><tgt><\|wait\|></tgt>` | 826 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>다른 결합을 만드는 데 사용되기도 합니다.</tgt>` | 1812 |

---

### Test Example 27 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 908 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1177 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不够的人之间，</src><tgt>If you're in a female high school and you're with someone who's not very attractive,</tgt>` | 2138 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>又这么重要</src><tgt><\|wait\|></tgt>` | 1513 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>的人系，</src><tgt>and you're still so focused on that person,</tgt>` | 1849 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1219 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1393 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天际野里开始的</src><tgt><\|wait\|></tgt>` | 2325 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2107 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1264 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1251 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>与年篇。</src><tgt>would it really be a relationship that starts with Yang Zisi and Nianpian?</tgt>` | 1914 |

---

### Test Example 28 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 1044 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>아일 겉은 </src><tgt><\|wait\|></tgt>` | 1338 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 융수리늄과 </src><tgt><\|wait\|></tgt>` | 1078 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1423 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산탄중인기나를 </src><tgt><\|wait\|></tgt>` | 2048 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>중요 하게 </src><tgt><\|wait\|></tgt>` | 1042 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아들 </src><tgt><\|wait\|></tgt>` | 1739 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1087 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이리 </src><tgt><\|wait\|></tgt>` | 1737 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>굉장히 잘 가져왔고 </src><tgt><\|wait\|></tgt>` | 2526 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1855 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 943 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아현. </src><tgt><\|wait\|></tgt>` | 1310 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1333 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>of the 19th Amendment </src><tgt>19차 수정헌법의</tgt>` | 1883 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 591 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore its </src><tgt>의미와</tgt>` | 1434 |
| 5 | `<src>history as a guide </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1700 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt>역사를 살펴보고, 그것이</tgt>` | 1322 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 1766 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen </src><tgt>정치적 변화가 어떻게 일어날 수 있는지</tgt>` | 1060 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1841 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt>미국에서</tgt>` | 2294 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1886 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the </src><tgt>일어날 수 있는지에 대한 지침입니다. 수정헌법의 의미는</tgt>` | 1333 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Amendment of </src><tgt><\|wait\|></tgt>` | 1264 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1012 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then.</tgt>` | 1156 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>红不렁跳，</src><tgt><\|wait\|></tgt>` | 1251 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src>所以</src><tgt>The red lines were all over the place,</tgt>` | 1705 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1712 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>期限大概</src><tgt>so we didn't go for surgery. The deadline was</tgt>` | 1376 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二星</src><tgt><\|wait\|></tgt>` | 1858 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>来选择，</src><tgt>about twelve days,</tgt>` | 1981 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 871 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>and then we had to cut it down to just a few days.</tgt>` | 2538 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1731 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他能</src><tgt>It was fine.</tgt>` | 1240 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很愉快地离开。</src><tgt><\|wait\|></tgt>` | 1338 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1261 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>啊，</src><tgt>皆さん、</tgt>` | 959 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1179 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>このローマは一日にしてできたものではありません。</tgt>` | 2183 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1455 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>ですから、</tgt>` | 893 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所见的一些</src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>世界气啊</src><tgt>今あなたが</tgt>` | 1022 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景</src><tgt><\|wait\|></tgt>` | 2217 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是</src><tgt>見ている世界や風景が、</tgt>` | 1187 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | 1556 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的。</src><tgt>一晩で変化したものではないということを覚えておいてください。</tgt>` | 2202 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会</src><tgt><\|wait\|></tgt>` | 1466 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>建议属鸡的朋友呢，</src><tgt>そのため、酉年生まれの皆さんは、</tgt>` | 1371 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 926 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150인가 </src><tgt>その中で150</tgt>` | 1349 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중호보에서 100미만 으로 </src><tgt><\|wait\|></tgt>` | 1172 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업 들만 </src><tgt>の企業だけが、中小型企業から</tgt>` | 2210 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>남았습니다. </src><tgt><\|wait\|></tgt>` | 1660 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>残りました。一般的には</tgt>` | 1063 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 기업 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1782 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>혹은 </src><tgt>中小企業は成長するか、あるいは</tgt>` | 2225 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>해화법이 이렇게 되는데 </src><tgt><\|wait\|></tgt>` | 2113 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>이번 에 </src><tgt>海運法がこうなりましたが、今回は</tgt>` | 1087 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업 들은 성장 도 </src><tgt><\|wait\|></tgt>` | 1589 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>폐업도 하지 않은 </src><tgt>中小企業は成長も倒産もしていない</tgt>` | 1812 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1215 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 907 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>我们看到的是</src><tgt>이 사진의 일부는</tgt>` | 1189 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1029 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>一个戴旧的人，但是他是</src><tgt>낡은 안경을 쓴 사람입니다. 하지만</tgt>` | 2558 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的</src><tgt><\|wait\|></tgt>` | 1692 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src><\|wait\|></src><tgt>역행하는</tgt>` | 949 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这种反潮流</src><tgt><\|wait\|></tgt>` | 1654 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>像一个状况，</src><tgt>상황을 보여줍니다.</tgt>` | 2026 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>需要去特别注意</src><tgt><\|wait\|></tgt>` | 749 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能</src><tgt>특별히 주의할 점은,</tgt>` | 2350 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 1816 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他掉不到</src><tgt>그가</tgt>` | 1279 |
| 13 | `<src><\|wait\|></src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1227 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>了。</src><tgt>당신의 의식에 닿지 않는지 여부입니다.</tgt>` | 1039 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 925 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到了一个天头，</src><tgt>天頂に達した</tgt>` | 1588 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 662 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了天头之后，</src><tgt>なら、天頂に達した後は</tgt>` | 2121 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1558 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>就要先</src><tgt>必ず</tgt>` | 938 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt><\|wait\|></tgt>` | 1758 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想着</src><tgt>守り抜いてください。そして、</tgt>` | 938 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>哎，</src><tgt><\|wait\|></tgt>` | 1874 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>闹我再继续操作下去哦。</src><tgt>「いや、もうこれ以上操作は続けられないよ」って言われたら、</tgt>` | 2924 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1709 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそんなこと言うのか？</tgt>` | 1566 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1105 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt>だって、</tgt>` | 911 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new </src><tgt><\|wait\|></tgt>` | 1005 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1092 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there was </src><tgt><\|wait\|></tgt>` | 1110 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such interests before, </src><tgt>以前就没有过这样的兴趣，</tgt>` | 1317 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1712 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>net future TC </src><tgt><\|wait\|></tgt>` | 1332 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1016 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>and so this is just </src><tgt><\|wait\|></tgt>` | 1675 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 2233 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>to look at </src><tgt><\|wait\|></tgt>` | 516 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2169 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>but </src><tgt><\|wait\|></tgt>` | 1846 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1207 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>would like to </src><tgt><\|wait\|></tgt>` | 1275 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>have a pair of them. </src><tgt>但开发者或工程师们想看一眼，这只是另一个地方，但他们需要一对。</tgt>` | 1422 |

---

### Test Example 36 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 847 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>이거 알고 있나요? </src><tgt>これ、知ってますか？</tgt>` | 1268 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 </src><tgt><\|wait\|></tgt>` | 982 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인으로 </src><tgt>ここは</tgt>` | 1209 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>있을 때 </src><tgt><\|wait\|></tgt>` | 1794 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>말 못하는 우상에게로 </src><tgt>異邦人として、言葉を話せない偶像に向かって</tgt>` | 1899 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그때 로 </src><tgt><\|wait\|></tgt>` | 1753 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>걸려 갔느라 </src><tgt>連れて行かれて、</tgt>` | 2007 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그럼 </src><tgt><\|wait\|></tgt>` | 793 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>으로 내가 </src><tgt>その結果、</tgt>` | 2220 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1864 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 는 것이 </src><tgt>あなたたちに知らせる</tgt>` | 666 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>아니 며 </src><tgt><\|wait\|></tgt>` | 1647 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>영으로 말하는 </src><tgt>のは、</tgt>` | 1035 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>자는. </src><tgt><\|wait\|></tgt>` | 912 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1332 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>is just getting going </src><tgt>「</tgt>` | 993 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1097 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1283 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I got ten of them </src><tgt>やる気はあるけど、まだ動き出す必要がある人、</tgt>` | 2602 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 1022 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1910 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>um </src><tgt>そのうち10人くらいは本当に重要です。</tgt>` | 2231 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 638 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I have about </src><tgt>私は</tgt>` | 2088 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1900 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at follow this video </src><tgt>この動画の後に1分間の動画を</tgt>` | 1106 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1537 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>And a little more </src><tgt>撮って、それぞれをカバーしていきます。あと、</tgt>` | 1061 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>detail. </src><tgt><\|wait\|></tgt>` | 742 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1239 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一手とか</src><tgt><\|wait\|></tgt>` | 1119 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですか？</src><tgt>十一手之类的吗？</tgt>` | 1139 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく十秒で</src><tgt><\|wait\|></tgt>` | 1581 |
| 5 | `<src>まあ</src><tgt>差不多十秒。</tgt>` | `<src>まあ</src><tgt>大概十秒内，</tgt>` | 1579 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒以内に</src><tgt><\|wait\|></tgt>` | 1254 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一秒ぐらいの</src><tgt>一秒内</tgt>` | 1175 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>せっかんですかね。</src><tgt><\|wait\|></tgt>` | 1379 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src><\|wait\|></src><tgt>左右的急促吗？</tgt>` | 2282 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 2357 |
| 11 | `<src>おそらく</src><tgt>然后</tgt>` | `<src>おそらく</src><tgt>大概</tgt>` | 1802 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一手</src><tgt><\|wait\|></tgt>` | 560 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt>十一手</tgt>` | 1366 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1099 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt>和马之类的</tgt>` | 917 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 612 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1277 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>濡らせてやる。</src><tgt>그럼 흠뻑 젖게 해줄게.</tgt>` | 1901 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 620 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>今</src><tgt>나는 지금</tgt>` | 1054 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き締めを見ている。</src><tgt><\|wait\|></tgt>` | 1747 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>힘을 줄이고 있어.</tgt>` | 1312 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1053 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超に</src><tgt>한계가</tgt>` | 1428 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>超えているふ重き勢だ。</src><tgt><\|wait\|></tgt>` | 2313 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>아주 많이 넘었어.</tgt>` | 945 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1707 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなデイを</src><tgt>오랫동안</tgt>` | 1934 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 1197 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt>이런 데서</tgt>` | 1363 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい階則線を</src><tgt><\|wait\|></tgt>` | 777 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt>엄청난 계급선을 본 적이 없어.</tgt>` | 1054 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1326 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어, 어차피 보면 </src><tgt>嗯，反正</tgt>` | 1274 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1117 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1524 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1822 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 1110 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>他就是和我一起经历过二十岁的弟弟，也是家人一样。</tgt>` | 2103 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1747 |
| 9 | `<src><\|wait\|></src><tgt>所以</tgt>` | `<src>어 </src><tgt>所以</tgt>` | 797 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생감 못하 는 </src><tgt><\|wait\|></tgt>` | 1966 |
| 11 | `<src>조금 </src><tgt>比起责任感，</tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 734 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로. </src><tgt>我有点自卑，</tgt>` | 1949 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1278 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1153 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 내려놓고 </src><tgt>放下很多东西，</tgt>` | 823 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠 다. </src><tgt><\|wait\|></tgt>` | 1007 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1167 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>財運についてですが、今月は</tgt>` | 1792 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 693 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分。</src><tgt>悪くないと言えるでしょう。ただ、正の収入に偏っている感じです。</tgt>` | 2410 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 1431 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>在事业方面</src><tgt>事業面では</tgt>` | 938 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩相对所载的</src><tgt><\|wait\|></tgt>` | 1805 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>红利以及收入的</src><tgt>期待通りの利益や収入が</tgt>` | 2414 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果</src><tgt><\|wait\|></tgt>` | 2113 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>在投资理财方面</src><tgt>上がらないかもしれません。投資や資産運用面では、</tgt>` | 2059 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 662 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>今月も悪くないですが、</tgt>` | 1754 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对整体来说</src><tgt><\|wait\|></tgt>` | 975 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>就算</src><tgt>全体的に見ても、</tgt>` | 953 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>弱了那么一点。</src><tgt><\|wait\|></tgt>` | 656 |

---

### Test Example 42 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 946 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃</src><tgt><\|wait\|></tgt>` | 975 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HJM이라고 하는 </src><tgt><\|wait\|></tgt>` | 1192 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1460 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1752 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1206 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1261 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1423 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2228 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 이 맞게 </src><tgt><\|wait\|></tgt>` | 2255 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1786 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>조어 들을 작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 836 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 조어 들을 </src><tgt><\|wait\|></tgt>` | 1667 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1099 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt>呃，HJM这种计算机语言是人也能理解的，我们也要能理解。我们现在需要编写程序来编写这些程序，</tgt>` | 1706 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1278 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. How far </src><tgt>학력 수준. 얼마나</tgt>` | 1492 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 781 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1350 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>go in your education? </src><tgt>교육을 받았는지 확인해 보세요.</tgt>` | 2161 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 1232 |
| 7 | `<src><\|wait\|></src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>That's one level of </src><tgt>고등학교를 졸업했나요?</tgt>` | 2000 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1914 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>그게 한 단계의 학력 수준입니다. 대학에 갔나요?</tgt>` | 880 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, </src><tgt><\|wait\|></tgt>` | 2237 |
| 11 | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>만약 그렇다면, 졸업했나요?</tgt>` | 2155 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt><\|wait\|></tgt>` | 1663 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for now. </src><tgt>그게 또 다른 학력 수준입니다. 지금은 여기까지입니다.</tgt>` | 1630 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 790 |
| 15 | `<src>online. </src><tgt>오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 783 |

---

### Test Example 44 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>けさ</src><tgt><\|wait\|></tgt>` | 1261 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>今朝、もちろん</tgt>` | 1076 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1346 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースもあります。Aという方と</tgt>` | 2168 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 1414 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 콘텐츠예요. </src><tgt>Bという方がお互いにコンテンツを</tgt>` | 1263 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 </src><tgt><\|wait\|></tgt>` | 1716 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>콘텐츠 해가지고 </src><tgt>作り合っているんです。そうやってコンテンツを作って、</tgt>` | 2433 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람이 </src><tgt><\|wait\|></tgt>` | 520 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aという方が悪意のあるコードを</tgt>` | 2430 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 1739 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>B라는 사람이 </src><tgt>渡したとき、Bという方が</tgt>` | 1419 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1197 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크로 사이트 스크립트에서 </src><tgt>実際にクロスサイトスクリプトで</tgt>` | 1011 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>이엑스파일까지 </src><tgt><\|wait\|></tgt>` | 843 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까 </src><tgt>感染するのか、</tgt>` | 585 |

---

### Test Example 45 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1291 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉</src><tgt><\|wait\|></tgt>` | 1107 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1025 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真实意图的。</src><tgt>相手の感情や本心を見抜くこと。</tgt>` | 2371 |
| 5 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 995 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1783 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：“</src><tgt>「</tgt>` | 1372 |
| 9 | `<src>这样说：“</src><tgt>よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1377 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt>見ての通り、</tgt>` | 2271 |
| 11 | `<src>这个人</src><tgt>「ほら、</tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1677 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在躲黄了。”</src><tgt>この人はまた黄運に入っているよ」って言われる。</tgt>` | 1139 |
| 13 | `<src>他的眼睛</src><tgt>また嘘をついている。目が</tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1400 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt>彼の目はすべてを物語っている。</tgt>` | 1171 |
| 15 | `<src><\|wait\|></src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 979 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 620 |
| 17 | `<src><\|wait\|></src><tgt>つまり…</tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 492 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1322 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>This is</tgt>` | 1164 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 1050 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1450 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt>not just a visual development environment, but a visual Python development environment.</tgt>` | 2446 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt><\|wait\|></tgt>` | 826 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルの</src><tgt><\|wait\|></tgt>` | 2006 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとそれは</src><tgt>This is because it includes a flow graph visual editor, and that's</tgt>` | 2465 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードが</src><tgt><\|wait\|></tgt>` | 2365 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成されて、それが</src><tgt>Python code that gets generated from it,</tgt>` | 2052 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1004 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>and that's how signal processing is performed.</tgt>` | 1622 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているから</src><tgt><\|wait\|></tgt>` | 698 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt>That's why it's structured like this.</tgt>` | 1073 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 661 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ</src><tgt>Okay,</tgt>` | 276 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 절수가 </src><tgt><\|wait\|></tgt>` | 1073 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt>The stock price is now rising,</tgt>` | 1349 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 </src><tgt><\|wait\|></tgt>` | 877 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>보인 다음에 이런 대형 주도 </src><tgt>and then</tgt>` | 1867 |
| 5 | `<src>큰 폭의 </src><tgt>these large- cap stocks</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1460 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1255 |
| 7 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>하겠지만 먼저 </src><tgt><\|wait\|></tgt>` | 1817 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 </src><tgt><\|wait\|></tgt>` | 692 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 2210 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 2141 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 </src><tgt><\|wait\|></tgt>` | 1264 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>때문 에 </src><tgt><\|wait\|></tgt>` | 1272 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요식초기 </src><tgt><\|wait\|></tgt>` | 1573 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 종목 을 </src><tgt><\|wait\|></tgt>` | 1115 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 </src><tgt><\|wait\|></tgt>` | 842 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>I think we'll have to watch the variable stocks first, because they move the market in the early stages. So, we'll need to look at the variable stocks with our eyes.</tgt>` | 1522 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1249 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 </src><tgt><\|wait\|></tgt>` | 886 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>해매입니다. </src><tgt>进去的时候，非常冷。我</tgt>` | 1353 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전을 하고 </src><tgt><\|wait\|></tgt>` | 1221 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 다니 고 </src><tgt>开车、走路，</tgt>` | 1917 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있거나 </src><tgt><\|wait\|></tgt>` | 1224 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>뭐 강북 으로 가면 </src><tgt>或者去北郊，</tgt>` | 1197 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1509 |
| 9 | `<src><\|wait\|></src><tgt>就不用说了，去外国</tgt>` | `<src>외국 에게 나가 는 것도 </src><tgt>说得更别提了，</tgt>` | 2392 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장려 려요. </src><tgt><\|wait\|></tgt>` | 2483 |
| 11 | `<src>좀 창피 하네요. </src><tgt>就更惨了。真有点丢人。</tgt>` | `<src>좀 챙기 야 </src><tgt>去国外也需要鼓励。要多注意</tgt>` | 2173 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>내신에 </src><tgt><\|wait\|></tgt>` | 1497 |
| 13 | `<src>이제 </src><tgt>不过，</tgt>` | `<src>이제 열심히 </src><tgt>内申，</tgt>` | 1079 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>노려봐요. 그거 는 </src><tgt><\|wait\|></tgt>` | 1026 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>좋은 것 같아요. </src><tgt>现在努力一下吧。我觉得这挺好的。</tgt>` | 919 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 538 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 898 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>そして、これについて多くの人々が</tgt>` | 1599 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 828 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 </src><tgt>分析をしています。ここで</tgt>` | 1424 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자 의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 2042 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ロクジャの分析を見ると、ソニーが</tgt>` | 1308 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 칩에 </src><tgt><\|wait\|></tgt>` | 1835 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FPD 파이프를 </src><tgt>イエローチップにFPDパイプを</tgt>` | 2433 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트로 </src><tgt><\|wait\|></tgt>` | 2087 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>낮춘 것이 로포인이다. </src><tgt>128ビットに下げたことがローポインです。</tgt>` | 1691 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 </src><tgt><\|wait\|></tgt>` | 952 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>시리즈, </src><tgt>Xboxシリーズ、</tgt>` | 1351 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1193 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt>Xboxにはないインフィニットキャッシュ、</tgt>` | 1210 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>LSI가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 696 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>LSIもありません。</tgt>` | 599 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1232 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1120 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt>自分自身で「基準」を定義することです。基準とは、</tgt>` | 2409 |
| 5 | `<src>absolutely correct, </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1723 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>But the reality </src><tgt>その通りです。しかし、現実には</tgt>` | 1349 |
| 7 | `<src>is is that </src><tgt>しかし現実には、</tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1261 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on </src><tgt>私たちは</tgt>` | 2366 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, and because </src><tgt><\|wait\|></tgt>` | 2162 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>新しい世代だからです。そして基準は</tgt>` | 1140 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1321 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago. </src><tgt>20年前に変わってしまったんです。</tgt>` | 1565 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>We are being held to </src><tgt><\|wait\|></tgt>` | 1145 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>higher standards </src><tgt>私たちはより高い基準を</tgt>` | 944 |
| 15 | `<src>everything at this point is being </src><tgt>より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 834 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher standards. </src><tgt>守らなければならないんです。なぜなら、今のところすべてがより高い基準で評価されているからです。</tgt>` | 1120 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 932 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>フローイーの組織</src><tgt><\|wait\|></tgt>` | 1143 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>決直到了那个现象。</src><tgt>플로이의 조직은 그 현상을 정확히 꿰뚫어 봤습니다.</tgt>` | 1985 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>美当中</src><tgt><\|wait\|></tgt>` | 1265 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我们属于</src><tgt>우리 중</tgt>` | 1296 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>爱之中，</src><tgt><\|wait\|></tgt>` | 1054 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>属位的爱。</src><tgt>은혜 가운데 속한 사랑입니다.</tgt>` | 1902 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 724 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>也同时进入</src><tgt>우리는 동시에</tgt>` | 2089 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1836 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨在掌上的时候，</src><tgt>분노를 손에 쥐고 있을 때,</tgt>` | 1178 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>它才爱。</src><tgt><\|wait\|></tgt>` | 1682 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上。</src><tgt>비로소 사랑이 찾아옵니다. 밤이 되면요.</tgt>` | 1769 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 1020 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>恨，</src><tgt>분노로 변합니다.</tgt>` | 903 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆。</src><tgt><\|wait\|></tgt>` | 722 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt>그 시계추는 계속</tgt>` | 626 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>一动。</src><tgt><\|wait\|></tgt>` | 602 |

---

### Test Example 52 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1304 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>새로 </src><tgt>目を閉じて、</tgt>` | 1025 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>밝을 거야. </src><tgt><\|wait\|></tgt>` | 1189 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>이제 </src><tgt>新しい光が差し込むよ。</tgt>` | 1235 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>서름이 돋은 차리 돋은 </src><tgt><\|wait\|></tgt>` | 2472 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 너무 야. </src><tgt>今、</tgt>` | 1216 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 </src><tgt><\|wait\|></tgt>` | 1904 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>한들어서 같이 놀자는 거야. </src><tgt>このゾクゾクする感じ、すごくいい。だから一緒に遊ぼうっていうんだ。</tgt>` | 2661 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 2219 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>너무 울릴 거고 </src><tgt>お化けがすごく鳴るし、</tgt>` | 2033 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 너무 야. 너 </src><tgt><\|wait\|></tgt>` | 1032 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>지켜 주라고 </src><tgt>神様がすごく鳴る。神様がすごく鳴る。神様がすごく鳴る。神様がすごく鳴る。神様がすごく鳴る。</tgt>` | 2566 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>인찔러 주라고 하니까 </src><tgt><\|wait\|></tgt>` | 932 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 마음 에. </src><tgt>神様が守ってくれって言うから、気持ちが楽になるんだ。</tgt>` | 846 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 627 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1223 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, you will not </src><tgt>另外，</tgt>` | 1125 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1084 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1196 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between </src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>the resources </src><tgt><\|wait\|></tgt>` | 1552 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though, </src><tgt><\|wait\|></tgt>` | 888 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 1775 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where you </src><tgt><\|wait\|></tgt>` | 2286 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 531 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 2163 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular </src><tgt><\|wait\|></tgt>` | 1922 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, we'll tell us. </src><tgt>虽然你不能在资源之间移动媒体对象，但如果你发现把错误的媒体文件添加到了某个资源中，我们会告诉你。</tgt>` | 2235 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>Now, and we can see about </src><tgt><\|wait\|></tgt>` | 1078 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those </src><tgt><\|wait\|></tgt>` | 856 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>media files and then making sure </src><tgt>现在，我们可以看看移动这些媒体文件，然后确保</tgt>` | 1017 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get back up </src><tgt><\|wait\|></tgt>` | 640 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>它们能正确恢复。</tgt>` | 478 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1081 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼はイエスを</tgt>` | 1446 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a son of Henry, </src><tgt><\|wait\|></tgt>` | 818 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>he knows that </src><tgt>ヘンリーの息子だと知っていました。</tgt>` | 1958 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's a Jew </src><tgt><\|wait\|></tgt>` | 1613 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>in the wilderness </src><tgt>彼は、</tgt>` | 948 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>spurtied day. </src><tgt><\|wait\|></tgt>` | 1847 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>And so he says to </src><tgt>荒野の日にユダヤ人であることも知っていました。だから彼は</tgt>` | 2573 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, </src><tgt><\|wait\|></tgt>` | 1526 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're a son of God, prove it. </src><tgt>イエスに言いました。「もしあなたが神の息子なら、証明してみせろ」と。</tgt>` | 2360 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn </src><tgt><\|wait\|></tgt>` | 839 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>these stones to bread. </src><tgt>この石をパンに変えなさいと。</tgt>` | 1694 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1100 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>just deal with that </src><tgt>彼はどうやって</tgt>` | 859 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 811 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>Man, </src><tgt>その誘惑に対処したのか？いや、</tgt>` | 614 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan led by bread. </src><tgt><\|wait\|></tgt>` | 638 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>ジョナタンはパンで導いた。一人で。</tgt>` | 560 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1534 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt>最初の1マイルは</tgt>` | 1424 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 790 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1450 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1704 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1245 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 1159 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1223 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant data </src><tgt><\|wait\|></tgt>` | 1977 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>bases, which is obviously </src><tgt><\|wait\|></tgt>` | 742 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>not of my loves. </src><tgt>私の好みではなかった。最初のセクションでは、AHRフィールドの重要性が、バリアントデータベースの重要性よりも重要であるという話だったからね。</tgt>` | 3636 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt><\|wait\|></tgt>` | 720 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>if we don't agree upon </src><tgt>つまり、</tgt>` | 1464 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields </src><tgt><\|wait\|></tgt>` | 1098 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt>これらの</tgt>` | 963 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 697 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>that we can draw from. </src><tgt>データソースに含めるべきフィールドについて合意できなければ、</tgt>` | 832 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>There's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 713 |
| 19 | `<src><\|wait\|></src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src><\|wait\|></src><tgt>それから引き出すものがないわけだよね？</tgt>` | 512 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1193 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1588 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 671 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>사진 부분은</tgt>` | 1584 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1517 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>一个是克汀的部分，</src><tgt>크레틴 부분과</tgt>` | 1424 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>而克汀一般</src><tgt><\|wait\|></tgt>` | 1830 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>都是属于</src><tgt>크레틴은 보통</tgt>` | 757 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们在</src><tgt><\|wait\|></tgt>` | 2092 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>吸收的</src><tgt>우리가 흡수하는</tgt>` | 2437 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>地方，所以呢</src><tgt><\|wait\|></tgt>` | 1897 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>它是身体的部分</src><tgt>부분이거든요. 그래서</tgt>` | 1014 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢会反映的是</src><tgt><\|wait\|></tgt>` | 1411 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给</src><tgt>몸이 반응하는 건</tgt>` | 924 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 964 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好的</src><tgt>우리가</tgt>` | 715 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息</src><tgt><\|wait\|></tgt>` | 427 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可不那么可以看到</src><tgt>앉아서 쉴 시간이 필요하다는 걸 보여주는 거예요.</tgt>` | 753 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是仿佛一人的嘛。</src><tgt><\|wait\|></tgt>` | 385 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt>여기서 마치 혼자 있는 것 같죠? 자,</tgt>` | 363 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以也是说。</src><tgt><\|wait\|></tgt>` | 356 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1327 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 945 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1220 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1148 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1526 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't I don't </src><tgt><\|wait\|></tgt>` | 1916 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>believe the courts want to be </src><tgt><\|wait\|></tgt>` | 1267 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1339 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 2254 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1790 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 826 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1879 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1291 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1344 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 724 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 844 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt>有意义的个人权利，而最高法院是最后一个加入的，而不是引领者。我不认为法院想成为社会变革的前卫。如今，它们更多地反映的是已经形成的共识。</tgt>` | 1481 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 362 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt>所以，</tgt>` | 337 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 329 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>你有一些联邦法官，</tgt>` | 452 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 930 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare. </src><tgt>この人たちは本当に珍しい。</tgt>` | 1279 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 995 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up </src><tgt>そして、</tgt>` | 1193 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1546 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>世界を完全に変革するために現れることが多い。</tgt>` | 1764 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The person </src><tgt><\|wait\|></tgt>` | 1602 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>alive is </src><tgt>生きている人は</tgt>` | 809 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 2342 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾した存在だ。</tgt>` | 2179 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>Well, they're extroverted. </src><tgt><\|wait\|></tgt>` | 1450 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>They also </src><tgt>まあ、外向的だ。そして、</tgt>` | 1191 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate </src><tgt><\|wait\|></tgt>` | 1479 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations. </src><tgt>意味のない会話が大嫌いだ。</tgt>` | 1258 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 867 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>it gets straight to the </src><tgt>そして、</tgt>` | 662 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 570 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>すぐに本題に入る。彼らは</tgt>` | 676 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 538 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>to it. </src><tgt>議論の相手になるのも大好きだ。</tgt>` | 376 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And never shy away </src><tgt><\|wait\|></tgt>` | 414 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることは決してない。</tgt>` | 334 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 277 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. stands for </src><tgt>E.T.P.は</tgt>` | 444 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stand for. </src><tgt><\|wait\|></tgt>` | 336 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 1292 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>정무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1222 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 852 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1622 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1815 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1119 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1854 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1657 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1138 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정은을 </src><tgt><\|wait\|></tgt>` | 1904 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제간 순간 </src><tgt><\|wait\|></tgt>` | 755 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석을 들으 네놓고 </src><tgt><\|wait\|></tgt>` | 2083 |
| 13 | `<src><\|wait\|></src><tgt>Lee Jun -seok</tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1656 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 </src><tgt><\|wait\|></tgt>` | 979 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 떡기를 </src><tgt><\|wait\|></tgt>` | 1175 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 </src><tgt><\|wait\|></tgt>` | 618 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 성을 보이 기로 </src><tgt><\|wait\|></tgt>` | 544 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 553 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt>Lee Jun- seok previously claimed he was running for the candidate's victory, even showing off his support for the candidate's win. But now, Yoon Suk- yeol is determined to defeat him. He's made up his mind to attack.</tgt>` | 1178 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 292 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 청상납건 </src><tgt><\|wait\|></tgt>` | 343 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 250 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 276 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt><\|wait\|></tgt>` | 355 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt>How big of a boon is the Democratic Party's attack on Lee Jun- seok's case of accepting gifts?</tgt>` | 478 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1169 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 1103 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt>I'd like to try making this after a meal.</tgt>` | 1490 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1168 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1634 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ホテルも朝食が</src><tgt><\|wait\|></tgt>` | 1358 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1087 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1375 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>Since this hotel is supposed to have breakfast, I'm planning to</tgt>` | 2494 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1989 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここ五郎ドストンホテル</src><tgt><\|wait\|></tgt>` | 932 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1642 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt>stay at the Goro Dosto Hotel in the future.</tgt>` | 1779 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1021 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>thinking about staying here in the future,</tgt>` | `<src>みてもまあいいんじゃない</src><tgt>If you're considering it,</tgt>` | 1119 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 601 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います</src><tgt>I think it's a good idea.</tgt>` | 599 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>こここのホテルからですね</src><tgt><\|wait\|></tgt>` | 579 |
| 19 | `<src>駅ももう</src><tgt>From this hotel,</tgt>` | `<src>부산駅も</src><tgt>From this hotel,</tgt>` | 482 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 353 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 427 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんないか</src><tgt><\|wait\|></tgt>` | 335 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 302 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 414 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt>the location is really good— you can walk to Busan Station in just a minute.</tgt>` | 471 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 248 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさって</src><tgt>So if you're interested,</tgt>` | 236 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>みてください</src><tgt><\|wait\|></tgt>` | 188 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね</src><tgt>please take a look.</tgt>` | 219 |
