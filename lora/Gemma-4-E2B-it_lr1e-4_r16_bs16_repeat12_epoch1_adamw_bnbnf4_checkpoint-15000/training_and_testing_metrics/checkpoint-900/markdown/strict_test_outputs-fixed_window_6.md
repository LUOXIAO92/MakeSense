# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9638
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3709
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 3
  - TARGET_METRICS_FILTERED_TURN_COUNT: 38
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 57
  - TGT_RELEASE_ACCURACY: 0.8462
  - TGT_RELEASE_TOTAL: 91
  - TGT_WAIT_ACCURACY: 0.9743
  - TGT_WAIT_TOTAL: 740
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1310.2930
  - PROCESS_TIME_MS_P50: 1325.8620
  - PROCESS_TIME_MS_P95: 1990.1840
  - PROCESS_TIME_MS_MAX: 3027.4760

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1080 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>在宿舍里，</src><tgt><\|wait\|></tgt>` | 1031 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个优惠</src><tgt><\|wait\|></tgt>` | 1222 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>也很大，然后</src><tgt><\|wait\|></tgt>` | 1121 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 666 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 1485 |
| 7 | `<src>儿核桃</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add</tgt>` | `<src>放假</src><tgt>Why is the discount so big in the dorms? And then, when I go on vacation,</tgt>` | 1654 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>和旅游，</src><tgt><\|wait\|></tgt>` | 1181 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>感觉</src><tgt><\|wait\|></tgt>` | 1867 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>在这些</src><tgt><\|wait\|></tgt>` | 1103 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和旅游。</src><tgt><\|wait\|></tgt>` | 1241 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 851 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 826 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲までまだ</src><tgt><\|wait\|></tgt>` | 1273 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1081 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 642 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1488 |
| 7 | `<src>剪定を</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段</tgt>` | `<src>四角線で</src><tgt>从一开始，特别是仲まで还是一年级，所以</tgt>` | 1582 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数していって</src><tgt><\|wait\|></tgt>` | 1337 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>上げる</src><tgt><\|wait\|></tgt>` | 1798 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>と10年経っても</src><tgt><\|wait\|></tgt>` | 1705 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>対数だ。</src><tgt><\|wait\|></tgt>` | 734 |

---

### Test Example 3 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 796 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1030 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 1339 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 688 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. </src><tgt><\|wait\|></tgt>` | 1503 |
| 7 | `<src>looking at the ten percent </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。</tgt>` | `<src>Looking at 10% </src><tgt>非常に幸せな人に関する重要な研究を調べたことがありますか？これは研究の入り口です。10%</tgt>` | 2245 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 818 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1638 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People with </src><tgt><\|wait\|></tgt>` | 1788 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>what we can learn from </src><tgt><\|wait\|></tgt>` | 1313 |

---

### Test Example 4 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=6)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 </src><tgt><\|wait\|></tgt>` | 1246 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>있는 식성 들은 </src><tgt><\|wait\|></tgt>` | 922 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1283 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1176 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 699 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1741 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>식성 들이었기 </src><tgt>The people on the list actually weren't highly intelligent; they were just randomly selected.</tgt>` | 1761 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | 754 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1747 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 1834 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>모을 랐던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1733 |

---

### Test Example 5 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1231 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气数是容易的，</src><tgt><\|wait\|></tgt>` | 981 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1200 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 1310 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅值得</src><tgt><\|wait\|></tgt>` | 1415 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1274 |
| 7 | `<src>处于中间，</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>留出余时间。</src><tgt>気数をつけるのは簡単ですが、師匠に時間を残しておくのは、</tgt>` | 1513 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 599 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反</src><tgt><\|wait\|></tgt>` | 1706 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1928 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师傅。</src><tgt><\|wait\|></tgt>` | 1830 |

---

### Test Example 6 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个</src><tgt><\|wait\|></tgt>` | 833 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>情况，我们就是</src><tgt><\|wait\|></tgt>` | 1020 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1337 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就更改了</src><tgt><\|wait\|></tgt>` | 1188 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>汇报主管或是通知对方</src><tgt><\|wait\|></tgt>` | 839 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我笑这个状况，</src><tgt><\|wait\|></tgt>` | 1570 |
| 7 | `<src>不要想自己</src><tgt>In this situation, when we encounter a problem, we should</tgt>` | `<src>不要想自己</src><tgt>When facing this situation, we just have to change our reporting supervisor or notify the other party. I'm laughing at this situation. Don't think</tgt>` | 2236 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1418 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>苦力偿单，</src><tgt><\|wait\|></tgt>` | 981 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>责任</src><tgt><\|wait\|></tgt>` | 1777 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>也使得</src><tgt><\|wait\|></tgt>` | 1720 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1030 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 967 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので、</src><tgt><\|wait\|></tgt>` | 1272 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1068 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 662 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>五減</src><tgt><\|wait\|></tgt>` | 1541 |
| 7 | `<src><\|wait\|></src><tgt>大致是从这一带开始的，</tgt>` | `<src><\|wait\|></src><tgt>大概是从这附近开始的，</tgt>` | 1470 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>細山</src><tgt><\|wait\|></tgt>` | 1270 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 1366 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>などのという人の</src><tgt><\|wait\|></tgt>` | 884 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵、</src><tgt><\|wait\|></tgt>` | 1836 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1885 |

---

### Test Example 8 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1144 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1060 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1281 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オーシャラとか</src><tgt><\|wait\|></tgt>` | 1175 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>だね、やっぱりですね、</src><tgt><\|wait\|></tgt>` | 976 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>海遊したい方って</src><tgt><\|wait\|></tgt>` | 1468 |
| 7 | `<src>すごい</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人</tgt>` | `<src>すぐに行こう</src><tgt>Adwanさん，感觉有点距离感，像Oceanara那样，</tgt>` | 1192 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>して다가 </src><tgt><\|wait\|></tgt>` | 1123 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>次で</src><tgt><\|wait\|></tgt>` | 1785 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>見て、と本的に</src><tgt><\|wait\|></tgt>` | 646 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>おとを聴くことが強ので、</src><tgt><\|wait\|></tgt>` | 1966 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1680 |

---

### Test Example 9 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 693 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 956 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1013 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>鬼岛哈，让我</src><tgt><\|wait\|></tgt>` | 1192 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>能够好在它</src><tgt><\|wait\|></tgt>` | 688 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>下山的时候，</src><tgt><\|wait\|></tgt>` | 1343 |
| 7 | `<src>在做热汤</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在座日</src><tgt>저를 귀섬으로 데려가 주세요. 제가 그곳에서</tgt>` | 1835 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>躺在</src><tgt><\|wait\|></tgt>` | 1253 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那样的</src><tgt><\|wait\|></tgt>` | 1701 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>时候，</src><tgt><\|wait\|></tgt>` | 641 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>我当时被掏出</src><tgt><\|wait\|></tgt>` | 1863 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>一个小小欲望哈。</src><tgt><\|wait\|></tgt>` | 2133 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1227 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 877 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1152 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただくというようなものも</src><tgt><\|wait\|></tgt>` | 1139 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 729 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1553 |
| 7 | `<src>ご連絡としては</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt>We also have T-shirts and similar items available, so please feel free to join us.</tgt>` | 1692 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 987 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1885 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>何しろ</src><tgt><\|wait\|></tgt>` | 998 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>何しろ</src><tgt><\|wait\|></tgt>` | 1338 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>何々のような内が</src><tgt><\|wait\|></tgt>` | 2235 |

---

### Test Example 11 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1099 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용신이 </src><tgt><\|wait\|></tgt>` | 893 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1347 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용신이 </src><tgt><\|wait\|></tgt>` | 1418 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설 용신이 가 </src><tgt><\|wait\|></tgt>` | 1702 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1377 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi.</tgt>` | `<src>석연 하는 건데요. </src><tgt>So, I'm a sword- element person, and the sword element is a bit awkward.</tgt>` | 1597 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1714 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1480 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>혜경으로도 </src><tgt><\|wait\|></tgt>` | 816 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽임이 되는 사람. </src><tgt><\|wait\|></tgt>` | 2328 |

---

### Test Example 12 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1222 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是</src><tgt><\|wait\|></tgt>` | 938 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1345 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱交</src><tgt><\|wait\|></tgt>` | 1420 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1657 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src>给足</src><tgt>What parents need to do is this: water and fertilize with our deep love,</tgt>` | `<src>祈求孩子</src><tgt>Parents need to use our deep love to pray for their children</tgt>` | 1495 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心灵</src><tgt><\|wait\|></tgt>` | 1822 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>营养、</src><tgt><\|wait\|></tgt>` | 1699 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>心耐性，</src><tgt><\|wait\|></tgt>` | 839 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>等孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 2066 |

---

### Test Example 13 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1253 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后呢，</src><tgt><\|wait\|></tgt>` | 966 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的液体</src><tgt><\|wait\|></tgt>` | 1222 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>减轻，能量也</src><tgt><\|wait\|></tgt>` | 1373 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>稍弱了，然后就</src><tgt><\|wait\|></tgt>` | 1769 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1326 |
| 7 | `<src>相对的低</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的</tgt>` | `<src>一个相对的</src><tgt>淘撒が終わると、内部の液体が軽くなり、エネルギーも少し弱まります。そして、</tgt>` | 1747 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态</src><tgt><\|wait\|></tgt>` | 1768 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>态。</src><tgt><\|wait\|></tgt>` | 1758 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1663 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>低语状态。</src><tgt><\|wait\|></tgt>` | 1502 |

---

### Test Example 14 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1065 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 984 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 958 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと</src><tgt><\|wait\|></tgt>` | 727 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えが</src><tgt><\|wait\|></tgt>` | 1233 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>できなくなってしまうので、</src><tgt><\|wait\|></tgt>` | 1598 |
| 7 | `<src>ギアの先に</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가 꺼져서</tgt>` | 1837 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 998 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1650 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついてるっていうこと</src><tgt><\|wait\|></tgt>` | 676 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1739 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1740 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 1282 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 881 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt><\|wait\|></tgt>` | 1023 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1453 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수도 다. </src><tgt><\|wait\|></tgt>` | 1388 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 쯤에 </src><tgt><\|wait\|></tgt>` | 1884 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1236 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room?</tgt>` | `<src>해차는 거야. 내가 </src><tgt>They might have come to kill me because someone on the advanced side wanted me to. It's like a feast, and they're asking for a death. I</tgt>` | 3027 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt><\|wait\|></tgt>` | 614 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>안 듣고 있는 줄은 아는 거야. </src><tgt><\|wait\|></tgt>` | 2059 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 1811 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 988 |

---

### Test Example 16 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=6)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 970 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 912 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 젭팔 젭팔 젭팔 젭팔 </src><tgt><\|wait\|></tgt>` | 2255 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 650 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1639 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 젭팔 젭팔 젭팔 젭팔 </src><tgt>I am Apple, Apple, Apple, Apple, and</tgt>` | 2374 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>조깅. </src><tgt><\|wait\|></tgt>` | 612 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1700 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>헤르나. 박한성 과 </src><tgt><\|wait\|></tgt>` | 2064 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1863 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1302 |

---

### Test Example 17 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 857 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是指</src><tgt><\|wait\|></tgt>` | 953 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二classList，</src><tgt><\|wait\|></tgt>` | 1105 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>它属于</src><tgt><\|wait\|></tgt>` | 1003 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 763 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们。</src><tgt><\|wait\|></tgt>` | 1376 |
| 7 | `<src>比如说，呃，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、</tgt>` | `<src>比如说，</src><tgt>2つ目は、二クラスです。これは一級一線で戦う大牛たちに属します。例えば、</tgt>` | 2297 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 767 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>维生运动</src><tgt><\|wait\|></tgt>` | 1343 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>好事几年，你会发现</src><tgt><\|wait\|></tgt>` | 999 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>维生运动</src><tgt><\|wait\|></tgt>` | 1764 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>平分的星棒</src><tgt><\|wait\|></tgt>` | 1839 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1321 |

---

### Test Example 18 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 964 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>body saying? </src><tgt><\|wait\|></tgt>` | 812 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1384 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1323 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt><\|wait\|></tgt>` | 1724 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>What is it? Is it </src><tgt><\|wait\|></tgt>` | 1436 |
| 7 | `<src>Is it a headache? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？</tgt>` | `<src>a day? </src><tgt>你的身体在说什么？把图钉钉在你的身体上。紧张感从哪里开始？是什么？是</tgt>` | 1874 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Because it's a time in your chest. </src><tgt><\|wait\|></tgt>` | 1800 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is the body </src><tgt><\|wait\|></tgt>` | 1865 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>lacking what you use </src><tgt><\|wait\|></tgt>` | 2100 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>saying? </src><tgt><\|wait\|></tgt>` | 1034 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1040 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 884 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无波澜，</src><tgt><\|wait\|></tgt>` | 1333 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不懈的</src><tgt><\|wait\|></tgt>` | 691 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>开到七千八百</src><tgt><\|wait\|></tgt>` | 1722 |
| 7 | `<src>大概有十位医生</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors</tgt>` | `<src>万位一生</src><tgt>Everything was normal back then. There was no ripple, so I kept going, and it took</tgt>` | 1761 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来审断，</src><tgt><\|wait\|></tgt>` | 789 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 1762 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下打腿，</src><tgt><\|wait\|></tgt>` | 1836 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1191 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1294 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1067 |

---

### Test Example 20 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 928 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1319 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned to repeat </src><tgt><\|wait\|></tgt>` | 1411 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>by finding a good app </src><tgt><\|wait\|></tgt>` | 1704 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it </src><tgt><\|wait\|></tgt>` | 1436 |
| 7 | `<src><\|wait\|></src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>and when you're not </src><tgt>最后，就是重复。我通过找一个好的App，多做几次，</tgt>` | 1728 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good at it, </src><tgt><\|wait\|></tgt>` | 1770 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 2057 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1878 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and in telling next time </src><tgt><\|wait\|></tgt>` | 1383 |

---

### Test Example 21 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이걸지 너무 </src><tgt><\|wait\|></tgt>` | 928 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>이 저희 할 일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1390 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 들요 </src><tgt><\|wait\|></tgt>` | 1379 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt><\|wait\|></tgt>` | 1746 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 </src><tgt><\|wait\|></tgt>` | 1379 |
| 7 | `<src>뭐 있고 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？</tgt>` | `<src>피라고 하고 있고 </src><tgt>これは、私たちがやるべきことでもありますが、本当に菩薩です。いや、自分の菩薩で夢だと</tgt>` | 1908 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1552 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보일 피라고 하고 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | 2169 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>지나 다오한테 </src><tgt><\|wait\|></tgt>` | 2121 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이란 </src><tgt><\|wait\|></tgt>` | 1035 |

---

### Test Example 22 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1285 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 883 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 1313 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1202 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 669 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1601 |
| 7 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们</tgt>` | `<src><\|wait\|></src><tgt>好的，那么在这些例子之后，</tgt>` | 1258 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually. </src><tgt><\|wait\|></tgt>` | 1192 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>These </src><tgt><\|wait\|></tgt>` | 1459 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>values. So these </src><tgt><\|wait\|></tgt>` | 864 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1810 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>game.board array </src><tgt><\|wait\|></tgt>` | 1953 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>实际上，它告诉我们使用这些值。所以，</tgt>` | 1546 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1149 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunah Terug. I </src><tgt><\|wait\|></tgt>` | 997 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>am currently studying </src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1354 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in a background in finance </src><tgt><\|wait\|></tgt>` | 1798 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a background in </src><tgt><\|wait\|></tgt>` | 1337 |
| 7 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src><\|wait\|></src><tgt>제 이름은 츄나 테루입니다. 저는 현재 금융 분야와 심리학 분야를 전공하고 있습니다.</tgt>` | 1813 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>psychology. </src><tgt><\|wait\|></tgt>` | 1596 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And in the </src><tgt><\|wait\|></tgt>` | 1848 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 1959 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1200 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1317 |

---

### Test Example 24 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this, </src><tgt><\|wait\|></tgt>` | 1131 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこ</src><tgt><\|wait\|></tgt>` | 755 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1309 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>think to set up 7.8 GB </src><tgt><\|wait\|></tgt>` | 1452 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>가 </src><tgt><\|wait\|></tgt>` | 1467 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>되셨다네. </src><tgt><\|wait\|></tgt>` | 1508 |
| 7 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src><\|wait\|></src><tgt>그래서, 거기서 7.8GB를 설정하면 되죠.</tgt>` | 1201 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>파생 에이오시의 </src><tgt><\|wait\|></tgt>` | 771 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>식음이 </src><tgt><\|wait\|></tgt>` | 1618 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>뭐건 </src><tgt><\|wait\|></tgt>` | 1836 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1655 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>세트 수비지 </src><tgt><\|wait\|></tgt>` | 1501 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>고비스. </src><tgt><\|wait\|></tgt>` | 1378 |

---

### Test Example 25 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1037 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 754 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>在女高中生与长相不够的人之间</src><tgt><\|wait\|></tgt>` | 1458 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1303 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>有种矛盾心理，</src><tgt><\|wait\|></tgt>` | 1807 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1340 |
| 7 | `<src><\|wait\|></src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src><\|wait\|></src><tgt>If a female high school student has a contradictory feeling between being with someone who is physically attractive and someone who isn't,</tgt>` | 1882 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天起</src><tgt><\|wait\|></tgt>` | 1621 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1874 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1730 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1372 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>留言篇。</src><tgt><\|wait\|></tgt>` | 1354 |

---

### Test Example 26 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 829 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>Aが</src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>あるんですね。いろんな場面で</src><tgt><\|wait\|></tgt>` | 1401 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうかっていう</src><tgt><\|wait\|></tgt>` | 1426 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>場合でいう時に、</src><tgt><\|wait\|></tgt>` | 1952 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>Aの欄を</src><tgt><\|wait\|></tgt>` | 1240 |
| 7 | `<src>ことで、あの</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>調べて、あの</src><tgt>So, A exists. In various situations, when we're deciding whether to eat it raw or cooked, we check the A column, and then</tgt>` | 2408 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうかっていう</src><tgt><\|wait\|></tgt>` | 1216 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>表示される生食で</src><tgt><\|wait\|></tgt>` | 1907 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt><\|wait\|></tgt>` | 1990 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1076 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt><\|wait\|></tgt>` | 1470 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 941 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 922 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1390 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1348 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1684 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy gets </src><tgt><\|wait\|></tgt>` | 1410 |
| 7 | `<src>gets converted to </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>converted to </src><tgt>고무줄처럼 늘어나면 화학 결합도 에너지를 저장해요. 그 결합이 끊어지면, 그 잠재 에너지는</tgt>` | 2110 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1517 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 1867 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 1818 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds, </src><tgt><\|wait\|></tgt>` | 1346 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1492 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1240 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of the </src><tgt><\|wait\|></tgt>` | 930 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>nineteenth amendment, </src><tgt><\|wait\|></tgt>` | 1344 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore </src><tgt><\|wait\|></tgt>` | 1371 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>its history as a guide </src><tgt><\|wait\|></tgt>` | 1398 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help </src><tgt><\|wait\|></tgt>` | 1238 |
| 7 | `<src><\|wait\|></src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>political change </src><tgt>19번째 수정헌법의 의미와 그 역사를 탐구하고, 정치적 변화를 위한 지침으로</tgt>` | 1820 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 1142 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1203 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1766 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1806 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of course I'm </src><tgt><\|wait\|></tgt>` | 1413 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Maryed. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지 살펴볼 것입니다. 물론 저는 메리드입니다.</tgt>` | 1883 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1261 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在</src><tgt><\|wait\|></tgt>` | 763 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1359 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一定要</src><tgt><\|wait\|></tgt>` | 1322 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>存在的，所以呢，</src><tgt><\|wait\|></tgt>` | 1267 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1194 |
| 7 | `<src>所面临的一些</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している</tgt>` | `<src>所见的一些</src><tgt>皆さんにお伝えしたいのは、このローマは必ずしも存在するわけではないということです。ですから、今あなたが</tgt>` | 1556 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>网页、</src><tgt><\|wait\|></tgt>` | 752 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟粉丝也不可能</src><tgt><\|wait\|></tgt>` | 1791 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>是即时之间</src><tgt><\|wait\|></tgt>` | 1883 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就演变出来。</src><tgt><\|wait\|></tgt>` | 1668 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1511 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1283 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>危機やリスクも、一朝一夕で生まれたわけじゃありません。そこで、酉年生まれの皆さんには…</tgt>` | `<src>我的朋友呢，</src><tgt>ウェブサイトやファンがリアルタイムで変化していくわけではないので、私の友人たちに</tgt>` | 1330 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1259 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 706 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1352 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1415 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1474 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1594 |
| 7 | `<src>to spell </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>how to spell </src><tgt>あるいは、何か書く、テキストを書く、という作業をする際に、スペルが全くわからないと気づいた場合、</tgt>` | 1929 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like, oh, </src><tgt><\|wait\|></tgt>` | 1789 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1744 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with a </src><tgt><\|wait\|></tgt>` | 1732 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>double P, </src><tgt><\|wait\|></tgt>` | 1319 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double L, I don't know </src><tgt><\|wait\|></tgt>` | 1649 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>「え、この単語は『ダブルP』、『ダブルL』、わからない、</tgt>` | 1465 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 1087 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이런 것들은 </src><tgt><\|wait\|></tgt>` | 881 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유전 실링과 </src><tgt><\|wait\|></tgt>` | 1334 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 거진 </src><tgt><\|wait\|></tgt>` | 1331 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산 한 적인 </src><tgt><\|wait\|></tgt>` | 1909 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>물질 들은 굉장히 </src><tgt><\|wait\|></tgt>` | 1282 |
| 7 | `<src>굉장히 아주 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where</tgt>` | `<src>아주 </src><tgt>These things, like vanadium, are very, very</tgt>` | 1379 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다. </src><tgt><\|wait\|></tgt>` | 2042 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1877 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 잘 가져가고 </src><tgt><\|wait\|></tgt>` | 1904 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1366 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1514 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt>definitely minerals. They take these very well. And now, with that, ah,</tgt>` | 1530 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 1019 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150만 개가 </src><tgt><\|wait\|></tgt>` | 952 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중요 본서 1000만으로 </src><tgt><\|wait\|></tgt>` | 1380 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>4000000 기업 들 </src><tgt><\|wait\|></tgt>` | 1347 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>이 많았습니다. </src><tgt><\|wait\|></tgt>` | 1773 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1283 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか</tgt>` | `<src>자건 업계 들은 </src><tgt>そのうち150万件が重要本書1000万件、4000万件の企業でした。一般的に、財政業は</tgt>` | 3002 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 혹은 </src><tgt><\|wait\|></tgt>` | 686 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>해화법이 그껴도 되는데 </src><tgt><\|wait\|></tgt>` | 1979 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>이번 에 </src><tgt><\|wait\|></tgt>` | 1903 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성기 없던 는 </src><tgt><\|wait\|></tgt>` | 1169 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 폐업도 하지 않는 </src><tgt><\|wait\|></tgt>` | 1402 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들도 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1467 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1176 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>there </src><tgt><\|wait\|></tgt>` | 747 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1320 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>was such interfaces before, </src><tgt><\|wait\|></tgt>` | 1367 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1247 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>net future TC, </src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src>Yeah, so </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以</tgt>` | `<src>and so </src><tgt>没什么新意，以前也有这样的接口，比如netfutureTC，所以</tgt>` | 1436 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>this is just </src><tgt><\|wait\|></tgt>` | 805 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1708 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 1905 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1707 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1411 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1275 |
| 14 | `<src>working on BugRepo </src><tgt>这只是另一个需要关注的地方。但开发人员或在BugRepo工作的工程师</tgt>` | `<src>working on bug reports </src><tgt>这只是另一个地方来看。但开发人员或工程师</tgt>` | 1046 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 1117 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>欠钱头，</src><tgt><\|wait\|></tgt>` | 871 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1285 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了欠钱头之后，</src><tgt><\|wait\|></tgt>` | 1410 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1667 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就要先</src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src>先守住，</src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。</tgt>` | `<src>守住，</src><tgt>彼は借金頭に追いついた。もし借金頭になったら、必ず守り、</tgt>` | 1765 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着</src><tgt><\|wait\|></tgt>` | 1632 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呃，那我在去操作</src><tgt><\|wait\|></tgt>` | 2036 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 1715 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1373 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1253 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？因为呢，</src><tgt><\|wait\|></tgt>` | 796 |
| 14 | `<src>因为呢。</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、それはですね。</tgt>` | `<src><\|wait\|></src><tgt>操作に行こうと思わないでくれ。なぜそんなことを言うのか？だって、</tgt>` | 1489 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 908 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>这章的部分我们看到的是</src><tgt><\|wait\|></tgt>` | 1007 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1206 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>戴庙的人，但是</src><tgt><\|wait\|></tgt>` | 1434 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于逆向的。</src><tgt><\|wait\|></tgt>` | 1819 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这通场</src><tgt><\|wait\|></tgt>` | 1333 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을</tgt>` | `<src>好像嘛，</src><tgt>이 장의 부분은 묘지에서 템플을 쓴 사람을 보여줍니다. 하지만 그는 역방향에 속합니다. 이 통장처럼</tgt>` | 2660 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>这样一个状况</src><tgt><\|wait\|></tgt>` | 851 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>需要去特别注意</src><tgt><\|wait\|></tgt>` | 1900 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能</src><tgt><\|wait\|></tgt>` | 1813 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 1202 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他掉不到</src><tgt><\|wait\|></tgt>` | 1302 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的</src><tgt><\|wait\|></tgt>` | 646 |
| 14 | `<src>的意思哦。</src><tgt>만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는 뜻이거든요.</tgt>` | `<src>意识。</src><tgt>이런 상황은 특별히 주의해야 합니다. 그가 당신의 의식에 닿지 않을 수 있습니다.</tgt>` | 1853 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1197 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>is just getting going </src><tgt><\|wait\|></tgt>` | 925 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1314 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1328 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1350 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really </src><tgt><\|wait\|></tgt>` | 1300 |
| 7 | `<src>really important. </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。</tgt>` | `<src>important. </src><tgt>これから始める人が、本当に重要な10のポイントがあるんです。</tgt>` | 1405 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 812 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 1880 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1864 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1719 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video. </src><tgt><\|wait\|></tgt>` | 1436 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage of </src><tgt>この動画の後に、1分程度の動画を1本作るつもりです。その動画で</tgt>` | 1798 |
| 14 | `<src>that cover each one </src><tgt>それについてお話ししていきます。この動画の後に、それぞれを</tgt>` | `<src>each one </src><tgt><\|wait\|></tgt>` | 1213 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 804 |

---

### Test Example 37 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1296 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세모라 </src><tgt><\|wait\|></tgt>` | 873 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1331 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이게 </src><tgt><\|wait\|></tgt>` | 1159 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>소름이 돋는 차리 돋는 </src><tgt><\|wait\|></tgt>` | 1431 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 온이야. </src><tgt><\|wait\|></tgt>` | 1418 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。</tgt>` | `<src>이걸 </src><tgt>目を閉じて、セモラを振るんだ。これが鳥肌が立つ、鳥肌が立つような感覚なんだ。これを</tgt>` | 1928 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>흔들어서 같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1867 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1006 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>오밀리 </src><tgt><\|wait\|></tgt>` | 1353 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>할 거고, 신이 오밀리 </src><tgt><\|wait\|></tgt>` | 2421 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>안 </src><tgt><\|wait\|></tgt>` | 699 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1469 |
| 14 | `<src>편안 한 마음 에 </src><tgt>一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら守ってくれるように突いてくれるから、安心して</tgt>` | `<src>인자니까 편안 마음 에 </src><tgt>振って一緒に遊ぶんだ。鬼神が</tgt>` | 1554 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 897 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1132 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt><\|wait\|></tgt>` | 923 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>かですと、</src><tgt><\|wait\|></tgt>` | 1377 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく10秒で</src><tgt><\|wait\|></tgt>` | 1379 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ1秒に</src><tgt><\|wait\|></tgt>` | 1489 |
| 7 | `<src>一定強ぐらいの</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点</tgt>` | `<src>1秒ぐらいの</src><tgt>比如12手，大概10秒，</tgt>` | 1121 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>せつなんですかね。</src><tgt><\|wait\|></tgt>` | 880 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1620 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1860 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1660 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>12手</src><tgt><\|wait\|></tgt>` | 1503 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1261 |
| 14 | `<src>あの</src><tgt>这样算。然后十一二手的时候，</tgt>` | `<src>あの</src><tgt>大概1秒，是吗？然后，大概12手，</tgt>` | 1081 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1049 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 846 |

---

### Test Example 39 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1302 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 909 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1262 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt><\|wait\|></tgt>` | 1325 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1387 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1289 |
| 7 | `<src><\|wait\|></src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>That's one level of </src><tgt>학력 수준. 실제로 교육을 얼마나 받았나요? 고등학교를 졸업했나요? 그건</tgt>` | 1796 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1240 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1116 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, did you graduate </src><tgt><\|wait\|></tgt>` | 1874 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>that's another level of </src><tgt><\|wait\|></tgt>` | 2343 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment? </src><tgt><\|wait\|></tgt>` | 929 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt>한 단계의 학력입니다. 대학에 갔나요? 그렇다면 또 한 단계의 학력입니다. 이제 그게 전부입니다.</tgt>` | 2201 |
| 14 | `<src>now. I'll see you </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다. 그럼 오늘은 여기까지 하겠습니다.</tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 814 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 909 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1330 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个财运可以说是</src><tgt><\|wait\|></tgt>` | 769 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很难的，但是</src><tgt><\|wait\|></tgt>` | 1217 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏正财的部分</src><tgt><\|wait\|></tgt>` | 1373 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也是</src><tgt><\|wait\|></tgt>` | 1443 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | 1301 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長による</tgt>` | `<src>业绩增长所带来的</src><tgt>財運についてですが、これは難しいと言えます。ただ、偏正財の部分は、事業の業績向上による</tgt>` | 1802 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>红利，</src><tgt><\|wait\|></tgt>` | 1819 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>收益的提升，</src><tgt><\|wait\|></tgt>` | 1582 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果是在投资理财方面</src><tgt><\|wait\|></tgt>` | 842 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1750 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1263 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对而言来说，</src><tgt><\|wait\|></tgt>` | 1473 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>ボーナスや昇給の運気が強めです。投資や資産運用についても、悪くはないんですが、本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>利益や収益の向上があれば、投資や資産運用に関しては今月も良いでしょう。ただ、それよりも、</tgt>` | 1917 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt><\|wait\|></tgt>` | 673 |

---

### Test Example 41 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 1044 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알 거니 뭐? </src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1290 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1331 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1385 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1381 |
| 7 | `<src>끄는 그대로 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに</tgt>` | `<src>그는 그대로 </src><tgt>あなたたちも知っているでしょう？ここで異邦人として、言葉を話せない偶像に</tgt>` | 1633 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 </src><tgt><\|wait\|></tgt>` | 1057 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>갔느니라. </src><tgt><\|wait\|></tgt>` | 1330 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 1909 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1979 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1134 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영으로 </src><tgt><\|wait\|></tgt>` | 1466 |
| 14 | `<src>말하는 자는. </src><tgt>連れて行かれました。ですから、あなたがたに教えます。神の霊によって語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>連れて行かれた。それゆえ、私はあなたたちに告げます。神の霊によって</tgt>` | 1682 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 929 |

---

### Test Example 42 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1028 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>呃，</src><tgt><\|wait\|></tgt>` | 787 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HJM이라고 하는 </src><tgt><\|wait\|></tgt>` | 1375 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1387 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1912 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1214 |
| 7 | `<src><\|wait\|></src><tgt>HTML是一种</tgt>` | `<src>이해 할 수 있는 </src><tgt>呃，计算机也能理解HJM，</tgt>` | 1418 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1910 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1836 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 말께 우리가 이제 </src><tgt><\|wait\|></tgt>` | 1662 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1488 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 1320 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 686 |
| 14 | `<src>프로그램 이 </src><tgt>计算机语言，计算机能理解，人类也能理解。我们需要按照它的语法来编写代码，而编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>人也能理解计算机语言的语法。我们现在需要编写代码，</tgt>` | 1590 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 832 |

---

### Test Example 43 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=6)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1281 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 915 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうのが</src><tgt><\|wait\|></tgt>` | 1247 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>出じゃなくて、ビジュアル</src><tgt><\|wait\|></tgt>` | 1392 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>Python開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1478 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1264 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>フローグラフビジュアル</src><tgt>So, this is actually not a visual development environment, but a Visual Python development environment.</tgt>` | 1621 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとは</src><tgt><\|wait\|></tgt>` | 1068 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードが</src><tgt><\|wait\|></tgt>` | 1230 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成されて、それが</src><tgt><\|wait\|></tgt>` | 2009 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 2102 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1070 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことをしている</src><tgt>It's a flow graph visual. You write the Python code, and it gets generated from there. When it runs, it performs signal processing.</tgt>` | 2013 |
| 14 | `<src><\|wait\|></src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 878 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 708 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | 581 |

---

### Test Example 44 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1221 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らせてやれ、</src><tgt><\|wait\|></tgt>` | 1035 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1238 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1344 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>ひどいよ見てる。</src><tgt><\|wait\|></tgt>` | 1416 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>그럼 그냥 젖게 해. 나는 끔찍하게 보고 있어.</tgt>` | 1833 |
| 7 | `<src>もう限界なんか</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미</tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1269 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に</src><tgt><\|wait\|></tgt>` | 1875 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>超えてる不練不器勢。</src><tgt><\|wait\|></tgt>` | 1738 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 711 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1872 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船出を</src><tgt>한계는 이미 넘어서 버린 불련불기세. 오랜 세월</tgt>` | 2074 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 602 |
| 14 | `<src>俺は</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야. 오랫동안 배를 만들어왔지만,</tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1266 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい海賊船を</src><tgt><\|wait\|></tgt>` | 853 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | 651 |

---

### Test Example 45 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1235 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어, 어찌 보면 </src><tgt><\|wait\|></tgt>` | 1005 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1324 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1312 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1950 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt><\|wait\|></tgt>` | 1241 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>嗯，怎么说呢，他就是我们20岁同龄的弟弟，</tgt>` | 1777 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1611 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1752 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재능 이 못다는 </src><tgt><\|wait\|></tgt>` | 1669 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1532 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1255 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>所以，嗯，他天赋不太好，</tgt>` | 878 |
| 14 | `<src>좀 많은 것을 </src><tgt>所以比起责任感，</tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 1171 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 813 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 659 |

---

### Test Example 46 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知</src><tgt><\|wait\|></tgt>` | 922 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1265 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真实意图的。</src><tgt><\|wait\|></tgt>` | 1356 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1551 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1212 |
| 7 | `<src>很多时候经常</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、</tgt>` | `<src>好经常会</src><tgt>相手の感情や真意を察知したり、感知したりすることです。よく</tgt>` | 1617 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说，</src><tgt><\|wait\|></tgt>` | 712 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1551 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看。</src><tgt><\|wait\|></tgt>` | 1870 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1770 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>躲黄了。</src><tgt><\|wait\|></tgt>` | 1342 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1382 |
| 14 | `<src>已经说明了一切。”</src><tgt>よく耳にするのが「ほら、また嘘をついている。目がすべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>よく聞く言葉があります。「見てください。この人はまた逃げました。彼の目はすべてを物語っています」と。この人は</tgt>` | 1499 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 707 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 653 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 714 |

---

### Test Example 47 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1074 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매니다. </src><tgt><\|wait\|></tgt>` | 1089 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1316 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1249 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 784 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1216 |
| 7 | `<src>강북 을 가면 </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北</tgt>` | `<src>뭐 강북 으로 가면 </src><tgt>进去的时候，我真的非常迷茫。因为我刚从开车转为步行，所以</tgt>` | 2127 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 857 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 는 것도 </src><tgt><\|wait\|></tgt>` | 1877 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장려 리예요. </src><tgt><\|wait\|></tgt>` | 1910 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 챙겨 야 해요. </src><tgt><\|wait\|></tgt>` | 2225 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1068 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt>去江南，更不用说出国了，这都是鼓励的。得好好准备一下。反而</tgt>` | 1721 |
| 14 | `<src>열심히 물어봐요. </src><tgt>就不用说了，去外国就更惨了。真有点丢人。不过，我会努力去问路。</tgt>` | `<src>뭐 바요. </src><tgt><\|wait\|></tgt>` | 1239 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 다행인 것 같아요. </src><tgt><\|wait\|></tgt>` | 1068 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 752 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 1200 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인상 하는 </src><tgt><\|wait\|></tgt>` | 723 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1400 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러 배형주도 </src><tgt><\|wait\|></tgt>` | 1353 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1434 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1666 |
| 7 | `<src>먼저 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>먼저 </src><tgt>If the stock market index is showing an upward trend, this stock will likely see a large increase. However,</tgt>` | 1823 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 1699 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1886 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1817 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1470 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1421 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시총이 </src><tgt>the first to move are the variable- interest rate- sensitive stocks, which lead the market. Therefore,</tgt>` | 1374 |
| 14 | `<src>가벼운 종목 을 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>가변 온 종목 을 </src><tgt><\|wait\|></tgt>` | 842 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈줄을 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 733 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 555 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 920 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1398 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1682 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1421 |
| 7 | `<src>is is that </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>is that </src><tgt>活動、そして自分自身で基準を定義すること。なぜなら、あなたが完全に正しいからこそ、現実とは</tgt>` | 1836 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt><\|wait\|></tgt>` | 1847 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the box, </src><tgt><\|wait\|></tgt>` | 1800 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed. </src><tgt><\|wait\|></tgt>` | 2312 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>From twenty years ago, </src><tgt><\|wait\|></tgt>` | 1396 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1214 |
| 14 | `<src>a higher standard because </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、</tgt>` | `<src>our standard </src><tgt>「新しい箱の猫」だからです。そして基準が変わったからです。20年前に、私たちは</tgt>` | 1298 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 725 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 561 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>けそ</src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 963 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1483 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 </src><tgt><\|wait\|></tgt>` | 1649 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 퀀텀 텐트예요. </src><tgt><\|wait\|></tgt>` | 1578 |
| 7 | `<src><\|wait\|></src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに</tgt>` | `<src>이게 컨설턴트 </src><tgt>けそ、もちろんこういうケースもあります。Aという人とBという人が量子テントです。これがコンサルタント</tgt>` | 2003 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>이어가지고 </src><tgt><\|wait\|></tgt>` | 1430 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1891 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 2268 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>들었을 때 </src><tgt><\|wait\|></tgt>` | 1056 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람이 </src><tgt><\|wait\|></tgt>` | 1426 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1144 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、Bさんは実際のクロスサイトスクリプティングから</tgt>` | `<src>크로 사이트 스크립트에서 </src><tgt>を継承して、Aという人が悪性コードを感染させると、Bという人が実際にクロスサイトスクリプトで</tgt>` | 1473 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>XSS까지 </src><tgt><\|wait\|></tgt>` | 706 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>가능히 될까? </src><tgt><\|wait\|></tgt>` | 641 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 873 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1338 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 1309 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자 앱 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1797 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니 가 </src><tgt><\|wait\|></tgt>` | 1337 |
| 7 | `<src>26비트 FP </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビット</tgt>` | `<src>이력 60에 </src><tgt>そして、これについて多くの人が分析をしています。このRokuzアプリの分析を見ると、ソニーが</tgt>` | 1897 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPP 파이프를 </src><tgt><\|wait\|></tgt>` | 1711 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1973 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나충가서 로포인 다. </src><tgt><\|wait\|></tgt>` | 2549 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 760 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1319 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>60の履歴60にFPPパイプを128ビットで導入しています。Xboxシリーズにもない</tgt>` | 1911 |
| 14 | `<src>인피니트 캐시 </src><tgt>FPパイプを128ビットに下げたようです。</tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 686 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>S가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 827 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 506 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1235 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 915 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1264 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1663 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1117 |
| 7 | `<src>So, if </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果</tgt>` | `<src>though, </src><tgt>另外，虽然你不能在资源之间移动媒体对象，</tgt>` | 1228 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 810 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where you </src><tgt><\|wait\|></tgt>` | 1692 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1958 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1752 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular </src><tgt><\|wait\|></tgt>` | 1408 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, we'll let us know. </src><tgt><\|wait\|></tgt>` | 1658 |
| 14 | `<src>and we can see about </src><tgt>你发现自己给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>And we can see about </src><tgt>但如果你发现把错误的媒体文件添加到了某个资源中，我们会通知你。我们也可以</tgt>` | 1597 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those media files </src><tgt><\|wait\|></tgt>` | 1025 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 753 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>to get that up </src><tgt><\|wait\|></tgt>` | 599 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 522 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1530 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 796 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1300 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt><\|wait\|></tgt>` | 1262 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1263 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1373 |
| 7 | `<src>being of critical importance </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、</tgt>` | `<src>importance </src><tgt>最初のセクションで、AHR分野の重要性について少し間違った認識を持っていました。</tgt>` | 1523 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 708 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant </src><tgt><\|wait\|></tgt>` | 1640 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>databases, which is obviously </src><tgt><\|wait\|></tgt>` | 1822 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1260 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1426 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1146 |
| 14 | `<src>upon the fields that need </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、</tgt>` | `<src>the fields that </src><tgt>バリアントデータベースは、私が大好きで、明らかに重要です。つまり、</tgt>` | 1505 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>need to be in these </src><tgt><\|wait\|></tgt>` | 1285 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 1011 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from. </src><tgt><\|wait\|></tgt>` | 709 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>There's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 667 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 515 |

---

### Test Example 54 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1024 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>for all the sorts </src><tgt><\|wait\|></tgt>` | 863 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>that we've just discussed, </src><tgt><\|wait\|></tgt>` | 1336 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but we're </src><tgt><\|wait\|></tgt>` | 1326 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1555 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>in the heart of love, </src><tgt><\|wait\|></tgt>` | 1572 |
| 7 | `<src>所谓的爱，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위</tgt>` | `<src>so the love </src><tgt>우리가 방금 논의한 모든 종류의 상황에 대해, 우리는 사랑의 마음속에 있기 때문에</tgt>` | 1822 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1615 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>will also enter </src><tgt><\|wait\|></tgt>` | 1845 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1743 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the time of the cross, </src><tgt><\|wait\|></tgt>` | 1515 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>that we love. </src><tgt><\|wait\|></tgt>` | 1583 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It's the end. </src><tgt><\|wait\|></tgt>` | 1131 |
| 14 | `<src>它就变成恨。</src><tgt>사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다.</tgt>` | `<src>It becomes </src><tgt>사랑의 마음속에 사랑이 들어오고, 십자가의 시간에도 사랑이 들어옵니다. 그것이 끝입니다. 그것은</tgt>` | 1481 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 697 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>that whole world. </src><tgt><\|wait\|></tgt>` | 548 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 338 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>It continues to do. </src><tgt><\|wait\|></tgt>` | 366 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1192 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>He knows Jesus </src><tgt><\|wait\|></tgt>` | 688 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a hungry </src><tgt><\|wait\|></tgt>` | 1309 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>and knows that </src><tgt><\|wait\|></tgt>` | 1343 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's supposed to </src><tgt><\|wait\|></tgt>` | 1393 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1366 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>for forty days that he's hungry, </src><tgt>ある時、彼はイエスが飢えていることを知っていました。そして、40日間飢えを耐え忍ぶべきだと知っていました。</tgt>` | 2026 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 1784 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 1954 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the Son of God, </src><tgt><\|wait\|></tgt>` | 2400 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt><\|wait\|></tgt>` | 1010 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones to bread. </src><tgt><\|wait\|></tgt>` | 1393 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt>だから、イエスに言いました。「もしあなたが神の子なら、証明してください。この石をパンに変えなさい。イエスは</tgt>` | 2123 |
| 14 | `<src>How did Jesus deal with that </src><tgt>で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。イエスは</tgt>` | `<src>deal with that </src><tgt><\|wait\|></tgt>` | 495 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation?" </src><tgt><\|wait\|></tgt>` | 801 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 520 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 511 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>Jonathan led by the stone. </src><tgt><\|wait\|></tgt>` | 479 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1164 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 951 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1042 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1161 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 692 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I I don't know </src><tgt><\|wait\|></tgt>` | 1757 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为</tgt>` | `<src>if the courts want to be </src><tgt>有意义的个人权利，而最高法院是最后才加入的，而不是领导者。我不知道法院是否想</tgt>` | 2189 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 807 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1676 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1871 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 1638 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1521 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1266 |
| 14 | `<src>the consensus </src><tgt>法院现在想成为社会变革的先锋，它们更倾向于</tgt>` | `<src>reflect the consensus </src><tgt>成为社会变革的先锋。如今，但他们更反映的是</tgt>` | 977 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1121 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 989 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 787 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 560 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 523 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>已经形成的共识。</tgt>` | 416 |
| 21 | `<src>who. </src><tgt>反映已经形成的共识。所以，有些联邦法官……</tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 298 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我們看一下</src><tgt><\|wait\|></tgt>` | 1081 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>一下</src><tgt><\|wait\|></tgt>` | 807 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它的圖片哦，</src><tgt><\|wait\|></tgt>` | 1217 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>圖片的部分呢，</src><tgt><\|wait\|></tgt>` | 1120 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我們可以看到的一個是</src><tgt><\|wait\|></tgt>` | 708 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>克汀的部分，</src><tgt><\|wait\|></tgt>` | 1736 |
| 7 | `<src>那客厅一般</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통</tgt>` | `<src>而克汀一般</src><tgt>그럼 그림을 한번 볼게요. 그림 부분에는 크틴이 보이는데요, 크틴은 보통</tgt>` | 2001 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是屬於</src><tgt><\|wait\|></tgt>` | 765 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我們在</src><tgt><\|wait\|></tgt>` | 1720 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>修習期</src><tgt><\|wait\|></tgt>` | 1777 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的地方，所以呢，</src><tgt><\|wait\|></tgt>` | 1169 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>這是身體的部分</src><tgt><\|wait\|></tgt>` | 1541 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，會反應的是</src><tgt><\|wait\|></tgt>` | 1056 |
| 14 | `<src>你需要给自己</src><tgt>우리가 쉬는 곳이잖아요. 그래서 이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要</src><tgt>학습 기간에 나오는 부분이에요. 그래서 이건 신체 부분인데, 반응하는 건</tgt>` | 1599 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>给自己一點時間</src><tgt><\|wait\|></tgt>` | 1199 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 719 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做下來修習</src><tgt><\|wait\|></tgt>` | 719 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可由我們可以看到</src><tgt><\|wait\|></tgt>` | 550 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>這邊是包含五人的嘛。</src><tgt><\|wait\|></tgt>` | 546 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 482 |
| 21 | `<src>所以是说。</src><tgt>시간을 내서 편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는 아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以也是說。</src><tgt>시간을 좀 갖고 잘 연습해야 하는 부분이에요. 연습은 5명이 포함되어 있고요. 그래서</tgt>` | 661 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 1060 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 798 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1349 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1280 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1350 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1345 |
| 7 | `<src><\|wait\|></src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>The </src><tgt>彼らは全く珍しい人々です。そして、彼らは世界を完全に変革するために現れることがよくあります。彼らは</tgt>` | 1856 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>personality is </src><tgt><\|wait\|></tgt>` | 1883 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 931 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1401 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 2013 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, they also </src><tgt><\|wait\|></tgt>` | 1269 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>矛盾した性格を持っています。外向的である一方で、</tgt>` | 1452 |
| 14 | `<src>meaningless conversations </src><tgt>彼らの性格は矛盾しています。外交的である一方、無意味な会話は嫌います。</tgt>` | `<src>hate meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1313 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like to </src><tgt><\|wait\|></tgt>` | 749 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt><\|wait\|></tgt>` | 599 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 619 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 552 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 577 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and then </src><tgt>意味のない会話を嫌います。そして、要点をまっすぐ話すのが好きです。彼らはまた、</tgt>` | 642 |
| 21 | `<src><\|wait\|></src><tgt>そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 285 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 362 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 354 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E and CP </src><tgt><\|wait\|></tgt>` | 349 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stand for. </src><tgt><\|wait\|></tgt>` | 344 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 1383 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>정무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 690 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1207 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1342 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1928 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1278 |
| 7 | `<src>제법 생색까지 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>제법 생색까지 </src><tgt>Lee Jun-seok previously claimed he refused political duties to support his candidacy, and that he was running for the party's leadership.</tgt>` | 2364 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1148 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1872 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1959 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제권 순간 </src><tgt><\|wait\|></tgt>` | 1157 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석 은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1628 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt>He even made a show of it, but now Yoon Suk-yeol is the presidential candidate, and Kim Jong-in is the presidential candidate.</tgt>` | 2144 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt>and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 720 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독끼를 품은 </src><tgt><\|wait\|></tgt>` | 582 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 496 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 518 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 399 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt>He's now set on attacking Yoon Suk-yeol, who is seen as having a grudge against Kim Jong-in.</tgt>` | 567 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 329 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석 성상납금 </src><tgt><\|wait\|></tgt>` | 367 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 365 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 351 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt><\|wait\|></tgt>` | 291 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마 나 큰 호재 입니까? </src><tgt>How big of a boon is the Democratic Party's attack on Lee Jun-seok's alleged campaign finance?</tgt>` | 527 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 6.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 995 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので</src><tgt><\|wait\|></tgt>` | 1482 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1337 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1724 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスローンホテルも</src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src>朝食が食べれる場所</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>朝食が食べれる場所</src><tgt>Well, I want to make something after dinner now. So, this Golf Sloan Hotel</tgt>` | 1808 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1615 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1884 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1711 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルフスローンホテル</src><tgt><\|wait\|></tgt>` | 1466 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1391 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なという方はですね</src><tgt><\|wait\|></tgt>` | 558 |
| 14 | `<src>検討なさってみて</src><tgt>is also planning to have breakfast available. So, for anyone thinking about staying here in the future,</tgt>` | `<src>検討なさって</src><tgt>is a place where you can have breakfast after a golf course. So, if you're considering staying at the Golf Sloan Hotel</tgt>` | 1928 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみて、まあいいんじゃない</src><tgt><\|wait\|></tgt>` | 768 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 428 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 524 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 531 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 425 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 324 |
| 21 | `<src>歩いて一分</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>一分かかる</src><tgt>and think, " Hmm, that sounds good." From here, it's just a minute walk to Busan Station.</tgt>` | 465 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんな</src><tgt><\|wait\|></tgt>` | 210 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>かそんなレベルでのね</src><tgt><\|wait\|></tgt>` | 316 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 371 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 314 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 316 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさって</src><tgt><\|wait\|></tgt>` | 302 |
| 28 | `<src>ください</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good. If you'd like, please consider it.</tgt>` | `<src>みてください。それなら</src><tgt>It's a great location, so if you're considering it, please take a look. If that's the case,</tgt>` | 414 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ですね今回は</src><tgt><\|wait\|></tgt>` | 186 |
