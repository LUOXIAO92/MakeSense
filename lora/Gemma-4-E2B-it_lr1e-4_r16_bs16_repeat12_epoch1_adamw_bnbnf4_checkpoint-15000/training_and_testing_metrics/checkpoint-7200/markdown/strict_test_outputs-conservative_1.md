# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9554
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.6954
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 682
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 0.8523
  - TGT_RELEASE_TOTAL: 88
  - TGT_WAIT_ACCURACY: 0.8878
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1346.9830
  - PROCESS_TIME_MS_P50: 1310.9870
  - PROCESS_TIME_MS_P95: 2129.2460
  - PROCESS_TIME_MS_MAX: 3330.4920

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>快在哪里</src><tgt><\|wait\|></tgt>` | 1153 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>这边？</src><tgt>Where is it?</tgt>` | 947 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个油箱也很大，</src><tgt><\|wait\|></tgt>` | 1224 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src>然后</src><tgt>The fuel tank is also quite large,</tgt>` | 1236 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1313 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在排个队啊，</src><tgt>and I'm waiting in line,</tgt>` | 1994 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人，</src><tgt><\|wait\|></tgt>` | 1402 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>and Tao- ren,</tgt>` | 1694 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>感觉在，</src><tgt><\|wait\|></tgt>` | 1645 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I feel like I'm</tgt>` | 1758 |
| 11 | `<src>仁儿。</src><tgt>this kind of walnut kernels.</tgt>` | `<src>这种喝陶人，</src><tgt><\|wait\|></tgt>` | 953 |

---

### Test Example 2 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 980 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>抛洒完以后呢，</src><tgt>撒き終えたら、</tgt>` | 1270 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | 1328 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了，</src><tgt>内部の圧力が下がり、エネルギーも衰えます。</tgt>` | 1728 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 531 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>就停留在一个</src><tgt>そして、</tgt>` | 1741 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>相对的低</src><tgt><\|wait\|></tgt>` | 1453 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>能量的运行</src><tgt>比較的低いエネルギーレベルで</tgt>` | 1778 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态。</src><tgt><\|wait\|></tgt>` | 1602 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>運行状態に留まります。これが、いわゆる</tgt>` | 1786 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | 947 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 957 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气熟是容易的，</src><tgt>火をつけるのは簡単です。</tgt>` | 1311 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 836 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>只有一个师傅</src><tgt>でも、</tgt>` | 1185 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>知道，</src><tgt><\|wait\|></tgt>` | 1334 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>師匠が一人だけ知っているんです。</tgt>` | 1444 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>如何处于中间，</src><tgt><\|wait\|></tgt>` | 1868 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt>どうやってその間に立つか。だから</tgt>` | 1813 |
| 9 | `<src>虚阿凡</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>虚也反，</src><tgt><\|wait\|></tgt>` | 1659 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt>虚が反る。そして、</tgt>` | 1766 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师傅。</src><tgt><\|wait\|></tgt>` | 939 |

---

### Test Example 4 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1055 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是</src><tgt>What parents need to do is</tgt>` | 1122 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1172 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1151 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱交洗</src><tgt><\|wait\|></tgt>` | 1293 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十倍</src><tgt><\|wait\|></tgt>` | 1380 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1808 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心理营养，</src><tgt>pour ten times our deep love into our children's psychological nutrition,</tgt>` | 1927 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>并耐心</src><tgt><\|wait\|></tgt>` | 1617 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1773 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>等孩子慢慢长大。</src><tgt>and patiently wait for them to grow up.</tgt>` | 1241 |

---

### Test Example 5 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 727 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 974 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 1139 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>毕竟这还是一年级。</tgt>` | 1331 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1282 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう短く</src><tgt>在这个阶段，</tgt>` | 1514 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1748 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1776 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>こうタイズしてってあげると</src><tgt>如果剪得短一点，收紧一点，</tgt>` | 1848 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1872 |
| 11 | `<src>大した。</src><tgt>十年后也不会有什么大……</tgt>` | `<src>大した。</src><tgt>十年后还是挺好的。</tgt>` | 1084 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 744 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 1062 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1059 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>your body. </src><tgt>进入你的身体。</tgt>` | 1211 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 1353 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么？</tgt>` | 2375 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1209 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸闷？</tgt>` | 1706 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src><\|wait\|></src><tgt>我问他们</tgt>` | 1854 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | 1564 |

---

### Test Example 7 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1164 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>The people in the auspicious spots</tgt>` | 1123 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1093 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1174 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1362 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 2048 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1249 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>었기 때문 입니다. </src><tgt>They were just random people who were selected.</tgt>` | 1819 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1693 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1812 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교사 들은. </src><tgt>The teachers who didn't know the truth...</tgt>` | 1820 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 863 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>面对这个情况，我们就是</src><tgt>In the face of this situation,</tgt>` | 1257 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 997 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>when we run into a problem, we should immediately report it to our supervisor.</tgt>` | 2074 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 626 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们学校这个状况，</src><tgt>Or we should inform the school about the situation.</tgt>` | 2737 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 861 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't think of it as something you have to handle all on your own.</tgt>` | 1809 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>不理成担，</src><tgt><\|wait\|></tgt>` | 1499 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>整体而言，</src><tgt>Overall,</tgt>` | 1744 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业属凶。</src><tgt><\|wait\|></tgt>` | 1725 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 853 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | 1121 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | 1360 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 931 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1298 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1459 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 녀르나 </src><tgt><\|wait\|></tgt>` | 2000 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1658 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1678 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1858 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>같은 세대 들입니다. </src><tgt>They are the same generation that triggered I'm Apple, the one that killed their own parents, Park Han- sang.</tgt>` | 2240 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 814 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1049 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. This is </src><tgt>非常に幸せな人々に関する重要な研究を行いました。</tgt>` | 1753 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 921 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research, </src><tgt>これはまだ序の口に過ぎません。</tgt>` | 2396 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | 1128 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1493 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>最も幸せな10％の人々を</tgt>` | 1949 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, </src><tgt><\|wait\|></tgt>` | 1859 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>people that we can learn from. </src><tgt>観察するものです。そこから私たちは学びを得ることができます。</tgt>` | 1958 |

---

### Test Example 11 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>从这里开始，</tgt>` | 994 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1062 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>我才做的，</tgt>` | 1298 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1334 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 1398 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1839 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1511 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 684 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1686 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 1989 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>中学生でも。</src><tgt>就连乡村初中生，</tgt>` | 1877 |

---

### Test Example 12 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아, 저는 </src><tgt><\|wait\|></tgt>` | 964 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>너무 심이 </src><tgt>Ah, I'm</tgt>` | 1133 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1141 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 웅심이 </src><tgt><\|wait\|></tgt>` | 1170 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어우, 웅심이가 </src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1774 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞이 는 건데요. 야, </src><tgt>so nervous, so nervous. Oh, the nervousness is mixing in. Wow,</tgt>` | 2776 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 618 |
| 9 | `<src>진짜 이거 </src><tgt>Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1718 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행운 으로 조금 죽입니다. </src><tgt>I'm actually killing it with a little bit of luck.</tgt>` | 2368 |
| 11 | `<src>진짜. </src><tgt>seriously killer for a hangover, for real.</tgt>` | `<src>제가 </src><tgt><\|wait\|></tgt>` | 1587 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1039 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1224 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>就是重复。学会重复。重复</tgt>` | 1490 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1105 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>你擅长的，多做一些。</tgt>` | 2367 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1051 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>And what you're not good at, </src><tgt>而你不擅长的，</tgt>` | 1708 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | 1938 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>就请身边的人帮忙。</tgt>` | 1920 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | 1829 |

---

### Test Example 14 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1188 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>距離が</src><tgt>嗯，</tgt>` | 885 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | 1088 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>オシャレる方がやで、</src><tgt>感觉距离在慢慢拉开，像是在说，时尚的人</tgt>` | 1887 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | 899 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>開業してたり</src><tgt>确实比较多。</tgt>` | 1433 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい</src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>自己意識高い</src><tgt><\|wait\|></tgt>` | 1498 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>っていうのもとなると</src><tgt>开业的人，</tgt>` | 691 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>そういった分野を</src><tgt><\|wait\|></tgt>` | 1639 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>取ることが強ので、</src><tgt>因为他们自我意识很强，所以会选择这些领域，</tgt>` | 2332 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので。</src><tgt><\|wait\|></tgt>` | 1607 |

---

### Test Example 15 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1121 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>and then </src><tgt>好的，</tgt>` | 897 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1016 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt>这些例子之后，</tgt>` | 1221 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1165 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | 696 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1869 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际上</tgt>` | 1145 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1765 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>要使用这些值。所以</tgt>` | 1749 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>this </src><tgt><\|wait\|></tgt>` | 1765 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>game.record array. </src><tgt>这个game.record数组。</tgt>` | 1013 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1480 |

---

### Test Example 16 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1119 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえるといったような</src><tgt><\|wait\|></tgt>` | 1091 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ものも用意しております</src><tgt><\|wait\|></tgt>` | 1317 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>ので、ぜひ</src><tgt>We have items like T- shirts available, so please feel free to</tgt>` | 1527 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1591 |
| 7 | `<src>ご連絡としては</src><tgt>so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt>join us. For contact,</tgt>` | 1545 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | 1787 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>えっと人数から</src><tgt>that's all. Um,</tgt>` | 1761 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>いう</src><tgt><\|wait\|></tgt>` | 1780 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>内訳がありますので、</src><tgt>we have the breakdown by number,</tgt>` | 1231 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ご参照もて下さい。</src><tgt><\|wait\|></tgt>` | 1263 |

---

### Test Example 17 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 805 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If a female high school student</tgt>` | 1204 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1454 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 802 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>has some kind of connection with someone with a strange appearance,</tgt>` | 1603 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1758 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>could it be</tgt>` | 1247 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | 1773 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>that started that night?</tgt>` | 1742 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1910 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子</src><tgt><\|wait\|></tgt>` | 1173 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>思绪连篇：</src><tgt>Yang Zi's thoughts flowed:</tgt>` | 1204 |

---

### Test Example 18 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 813 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>映画でですね、</src><tgt>In the movie,</tgt>` | 895 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに、</src><tgt>when they were checking whether the movie was alive in various scenes,</tgt>` | 1512 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | 1506 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことで、あの</src><tgt>by examining the movie's eggs,</tgt>` | 1871 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1817 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | 1838 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | 1906 |
| 11 | `<src>といったような</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1516 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt>they would guarantee that it was indeed alive.</tgt>` | 778 |

---

### Test Example 19 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | 1169 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>해가지고 내가 </src><tgt>He asked me to let him kill me with another knife,</tgt>` | 1873 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1447 |
| 5 | `<src>다른 잔찜에 </src><tgt>came in here to do it.</tgt>` | `<src>다른 잔찜에 </src><tgt>so I came in to kill him.</tgt>` | 1291 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 1193 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>해지 않았느냐? 내가 </src><tgt>Didn't I ask him to let him kill me?</tgt>` | 2166 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 786 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I didn't hear that,</tgt>` | 1884 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | 2168 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 가. </src><tgt>did you think I wasn't here? Huh? I'm going.</tgt>` | 1935 |

---

### Test Example 20 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src><\|wait\|></src><tgt>次は</tgt>` | 890 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>选择二级以上</src><tgt><\|wait\|></tgt>` | 976 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>付费，</src><tgt>2階以上で有料の</tgt>` | 1260 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1168 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>「大牛」たちです。1階や1線で激突するんです。</tgt>` | 1695 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1606 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做维信</src><tgt>例えば、</tgt>` | 815 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好事几年前，</src><tgt><\|wait\|></tgt>` | 1510 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>数年前のWeChatの話題を</tgt>` | 1822 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维信沟通好平行</src><tgt><\|wait\|></tgt>` | 2055 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的新榜反而</src><tgt>聞いていたのに、</tgt>` | 1766 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>活了。</src><tgt><\|wait\|></tgt>` | 439 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 740 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到我</src><tgt><\|wait\|></tgt>` | 1079 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活的一个轨道，</src><tgt>제 삶의 궤도로 돌아가게 해줘요.</tgt>` | 1941 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1075 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 687 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>照它上面的时候，</src><tgt>그것을 따라가면서</tgt>` | 2541 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1010 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭给别人吃，</src><tgt>다른 사람들에게 뜨거운 국이나 밥을 만들어 주는 것,</tgt>` | 1720 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就这么认为</src><tgt><\|wait\|></tgt>` | 1640 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我的生活是</src><tgt>그렇게 생각해요. 제 삶은</tgt>` | 2094 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>这么一个小小的小愿望</src><tgt><\|wait\|></tgt>` | 1836 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>哈。</src><tgt>이 작은 소망 하나로요.</tgt>` | 1641 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 837 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>그렇습니다. 거기서</tgt>` | 978 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1096 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>テキという設備寺が</src><tgt>테키라는 설비가</tgt>` | 1445 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 1247 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>で、</src><tgt>있었죠. 그래서</tgt>` | 1500 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1747 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt>나가이 케이이치 씨의</tgt>` | 1888 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1645 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>五コン</src><tgt>구조는</tgt>` | 1816 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 934 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設備寺組</src><tgt>고콘 설비지</tgt>` | 1542 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 1490 |

---

### Test Example 23 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Vanadium and these things are</tgt>` | 1646 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 994 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 804 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1331 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 굉장히 </src><tgt>almost as effective as insulin.</tgt>` | 2396 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>바로 </src><tgt><\|wait\|></tgt>` | 951 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt>They are called ' diabetes minerals '.</tgt>` | 1752 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1974 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt>That's what I mean.</tgt>` | 1597 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 701 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt>And then, zinc.</tgt>` | 1712 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1106 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src><\|wait\|></src><tgt>이게</tgt>` | 949 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>です。ギアが</src><tgt><\|wait\|></tgt>` | 1003 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>緩むと芯が</src><tgt>기어입니다. 기어가 풀리면 심이</tgt>` | 1456 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなってしまう</src><tgt><\|wait\|></tgt>` | 1402 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>ので、</src><tgt>위아래로 움직이지 않게 되니까,</tgt>` | 2184 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1189 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src><\|wait\|></src><tgt>기어 앞쪽에</tgt>` | 1677 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>逆ネジのナットが</src><tgt><\|wait\|></tgt>` | 1774 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>付いているっていうこと</src><tgt>역나사 너트가</tgt>` | 2090 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1772 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>붙어 있는 거죠.</tgt>` | 507 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>はい分解完了。</src><tgt><\|wait\|></tgt>` | 1602 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 889 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then.</tgt>` | 1010 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1294 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src><\|wait\|></src><tgt>I was full of energy,</tgt>` | 1168 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>可以坚持不回答。</src><tgt><\|wait\|></tgt>` | 1373 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>期间大概有</src><tgt>and I could hold out without answering.</tgt>` | 2413 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>十名医生来</src><tgt><\|wait\|></tgt>` | 1088 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>诊断，</src><tgt>About ten doctors came to diagnose me,</tgt>` | 1585 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下条退</src><tgt><\|wait\|></tgt>` | 1701 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以上提，</src><tgt>and they said," Back, back,"</tgt>` | 2106 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1753 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>no problem at all.</tgt>` | 484 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1650 |

---

### Test Example 26 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 937 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src><\|wait\|></src><tgt>これ、</tgt>` | 922 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1127 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src><\|wait\|></src><tgt>あまりにも地味なことかもしれません。</tgt>` | 1371 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>でも、本当に菩薩ですよ。いや、自分は菩薩なのに、飾る必要が</tgt>` | 3330 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있고. </src><tgt><\|wait\|></tgt>` | 1663 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>あるんです。南韓で菩薩に見える必要が</tgt>` | 2154 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | 2003 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>지금 도안 때 보살 이라면. </src><tgt>あるんです。宇宙が今、道案で菩薩なら。</tgt>` | 1997 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1609 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 841 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>Like a stretched rubber band, </src><tgt>늘어난 고무줄처럼</tgt>` | 1280 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 961 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | 1636 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>and when those bonds </src><tgt><\|wait\|></tgt>` | 934 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>are broken, that potential energy </src><tgt>이 결합이 끊어지면,</tgt>` | 2739 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 824 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>그 잠재 에너지는 다른 형태의 에너지로</tgt>` | 1700 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | 1756 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>전환됩니다. 예를 들어 열이나 빛,</tgt>` | 2121 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | 1780 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1921 |

---

### Test Example 28 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 922 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Kerenath Duru. </src><tgt>제 이름은 케레나스 두루입니다.</tgt>` | 1569 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently </src><tgt><\|wait\|></tgt>` | 901 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src><\|wait\|></src><tgt>현재</tgt>` | 889 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Bachelor of Psychology </src><tgt>경영학 학사 과정과</tgt>` | 2656 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 891 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at the ANU, </src><tgt>ANU에서 심리학 학사 과정을</tgt>` | 1586 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1714 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>and in the future, I want to go into </src><tgt>수강하고 있습니다. 앞으로는</tgt>` | 2342 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1678 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 2006 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>have to produce </src><tgt>あるいは、</tgt>` | 924 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1131 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何かを書き起こす必要がある場合、</tgt>` | 1431 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1251 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt>テキストを書く必要がある場合、</tgt>` | 2846 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 765 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. Like, oh, </src><tgt>そもそも単語の綴りがわからないことに気づくかもしれません。「ああ、</tgt>` | 1826 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1572 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>spelled with a double </src><tgt>この単語は</tgt>` | 2010 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1799 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam? I don't </src><tgt>ダブルp？ダブルl？</tgt>` | 1484 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 663 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1007 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1115 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1251 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>このローマは一日にしてできたものではなく、</tgt>` | 1524 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 884 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>今</tgt>` | 1307 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1836 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>危机啊，</src><tgt>直面している危機や</tgt>` | 1652 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风险</src><tgt><\|wait\|></tgt>` | 527 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是你事先</src><tgt>リスクは、事前に</tgt>` | 1723 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1889 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>逐渐显现出来的，</src><tgt>徐々に現れるものではないんです。</tgt>` | 1918 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1492 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>属鸡的朋友呢。</src><tgt>ですから、酉年生まれの方には、</tgt>` | 892 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 848 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>我们可以看到的是</src><tgt>이 부분에서 볼 수 있는 것은</tgt>` | 1111 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 1321 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>的人，但是</src><tgt>낚시를 하는 사람인데,</tgt>` | 1053 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于逆向的</src><tgt><\|wait\|></tgt>` | 1302 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src><\|wait\|></src><tgt>역방향으로</tgt>` | 1750 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这种场吗这样的一个状况</src><tgt><\|wait\|></tgt>` | 1579 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>的教学，就要去</src><tgt>배워야 하는 상황입니다. 이런 상황을</tgt>` | 1763 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意的是，</src><tgt><\|wait\|></tgt>` | 1709 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能够</src><tgt>특별히 주의할 점은 그 사람이</tgt>` | 2129 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | 1779 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>他钓不到</src><tgt>물고기를 잡을 수 있는지, 잡지 못하는지</tgt>` | 1091 |
| 13 | `<src><\|wait\|></src><tgt>물고기를 잡지 못한다는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 945 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>鱼的意识哦。</src><tgt>그 의식입니다.</tgt>` | 1180 |

---

### Test Example 32 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1112 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 938 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment, </src><tgt>제19조 수정헌법의 의미는</tgt>` | 1968 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 720 |
| 5 | `<src>history as a guide </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>그리고</tgt>` | 1175 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1902 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1336 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt>정치적 변화가</tgt>` | 1786 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1772 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>미국에서 어떻게 일어날 수 있는지 보여주는 지침서입니다.</tgt>` | 2394 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 1673 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, are </src><tgt>물론 수정헌법의 의미는</tgt>` | 2023 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 1277 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 799 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万人が</tgt>` | 1649 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | 1211 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>従業員10人未満の非常に小さな企業で、</tgt>` | 1585 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 736 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くありました。一般的に</tgt>` | 2115 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1340 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>혹은 폐업 할 길을 </src><tgt>中小企業は成長するか、あるいは廃業する</tgt>` | 1408 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | 1738 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>일본 의 소기업 들은 </src><tgt>道を選びますが、日本の小企業は</tgt>` | 2246 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | 1731 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | 1894 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1316 |

---

### Test Example 34 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就</src><tgt><\|wait\|></tgt>` | 960 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一手に</src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>解けたとか言った、おそらく</src><tgt>就说解了一手，</tgt>` | 1175 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 1304 |
| 5 | `<src>まあ</src><tgt>差不多十秒。</tgt>` | `<src>まあ</src><tgt>或者说十秒内，</tgt>` | 1358 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1469 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一定くらいの</src><tgt><\|wait\|></tgt>` | 1749 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>速度なんですか</src><tgt><\|wait\|></tgt>` | 1492 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>ね。</src><tgt>大概每秒有一点这种速度吧。</tgt>` | 660 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1640 |
| 11 | `<src>おそらく</src><tgt>然后</tgt>` | `<src>おそらく</src><tgt>然后</tgt>` | 1699 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一手に</src><tgt><\|wait\|></tgt>` | 867 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt>大概十一手，</tgt>` | 1476 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1519 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt>宫马之类的</tgt>` | 809 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>あるから。</src><tgt><\|wait\|></tgt>` | 925 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 919 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src>There were </src><tgt>没什么新鲜事。</tgt>` | 1029 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1236 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such interfaces before, </src><tgt>以前就有这样的接口，</tgt>` | 1215 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1311 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>netfilter, TC. </src><tgt>netfilter、TC。</tgt>` | 2176 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 1202 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>this is just </src><tgt>对，所以这只是</tgt>` | 1668 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1656 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src><\|wait\|></src><tgt>另一个地方，</tgt>` | 1765 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 987 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt>用来看看。</tgt>` | 1522 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>But developers, </src><tgt><\|wait\|></tgt>` | 1634 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>originators were going to have </src><tgt>但开发者和发起方</tgt>` | 917 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>a pair of them. </src><tgt><\|wait\|></tgt>` | 825 |

---

### Test Example 36 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 769 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到了一个甜头，那</src><tgt>いい兆しが訪れたので、</tgt>` | 1280 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt><\|wait\|></tgt>` | 849 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了甜头之后，</src><tgt>もしいい兆しを得た後、</tgt>` | 1420 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1241 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src><\|wait\|></src><tgt>必ず</tgt>` | 1630 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1546 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想说，哎，那我再</src><tgt>守り抜いてください。そうして</tgt>` | 1937 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1717 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>继续操作下去哦。</src><tgt>「あ、もうちょっと操作を続けよう」なんて考えないでください。</tgt>` | 2420 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1703 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのか？</tgt>` | 1822 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1176 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>因为呢。</src><tgt>それはですね……</tgt>` | 993 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1090 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>getting going </src><tgt>始めたばかりの人が</tgt>` | 999 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to </src><tgt><\|wait\|></tgt>` | 1068 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src>get. </src><tgt>必要なのは、</tgt>` | 1247 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>And like ten of them that </src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>are really </src><tgt>そうやってやるだけです。で、</tgt>` | 1731 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1530 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt>本当に重要な人が10人くらいいるんです。</tgt>` | 1836 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go </src><tgt><\|wait\|></tgt>` | 1785 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1875 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>into about one minute videos </src><tgt>1分程度の動画をいくつか見て、</tgt>` | 1756 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>about this video. </src><tgt><\|wait\|></tgt>` | 595 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>They cover each one, </src><tgt>その動画の内容を</tgt>` | 1788 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1194 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>and a little more detail, </src><tgt>詳しく解説します。</tgt>` | 1021 |

---

### Test Example 38 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 804 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>어 Htmetal </src><tgt>嗯，</tgt>` | 1000 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1066 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있고 </src><tgt>计算机</tgt>` | 1252 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1424 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1817 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1595 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 551 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1714 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1862 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>是HMetal，也是人能理解的计算机语言。根据这种语言的语法，我们现在需要编写代码，</tgt>` | 2246 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | 1729 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | 1193 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt>需要一个编写这些代码的程序。</tgt>` | 1044 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 826 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니와 너희 가 </src><tgt>あなたたちも知っているだろう。</tgt>` | 1244 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 1228 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>異邦人としていた時、</tgt>` | 1136 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1187 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>言葉を持たない偶像に</tgt>` | 1782 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1448 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src><\|wait\|></src><tgt>引き寄せられるままに</tgt>` | 1784 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1870 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>引きずり込まれた。だから私は</tgt>` | 2145 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 1804 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>あなたたちに告げます。</tgt>` | 1809 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 874 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는. </src><tgt>神の霊によって語る者は……</tgt>` | 1113 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 466 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 928 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>金運についてですが、今月は</tgt>` | 1266 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1180 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分，</src><tgt>とても良いと言えます。ただ、正の収入に偏っていて、</tgt>` | 1999 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 603 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>在事业方面的</src><tgt>仕事面での</tgt>` | 1750 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩成长所带来的</src><tgt><\|wait\|></tgt>` | 1318 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>红利与收入的</src><tgt>業績成長による恩恵や収入の</tgt>` | 1770 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | 1771 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>投资理财方面呢，</src><tgt>向上です。投資や資産運用に関しては、</tgt>` | 2257 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1675 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>今月も悪くありませんが、</tgt>` | 1639 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | 818 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>稍微弱了那么一点。</src><tgt>正の収入と比べると少し弱めです。</tgt>` | 1350 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 477 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1034 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう眠らせてやれ。</src><tgt>그럼 그냥 재워버려.</tgt>` | 1165 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1022 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src><\|wait\|></src><tgt>난</tgt>` | 1183 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>今基地を見ている。</src><tgt><\|wait\|></tgt>` | 1329 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>지금 기지를 보고 있어.</tgt>` | 1393 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1830 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>遠い越えている</src><tgt>더 이상 한계는</tgt>` | 1483 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>船の犠牲球。</src><tgt><\|wait\|></tgt>` | 636 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>넘어버린 배의 희생구.</tgt>` | 1914 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1797 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船大工をやってる</src><tgt>오래전부터 배를</tgt>` | 1940 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>が、</src><tgt><\|wait\|></tgt>` | 1583 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt>만들던 내가, 이렇게 대단한</tgt>` | 1039 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>海賊船を見た</src><tgt><\|wait\|></tgt>` | 837 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt>해적선을 본 적이 없어.</tgt>` | 838 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1087 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어떻게 보면 </src><tgt>嗯，怎么说呢，</tgt>` | 1180 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1519 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 796 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>동생 이자 </src><tgt><\|wait\|></tgt>` | 1304 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 1451 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>같은 동생 이잖아 </src><tgt>也是和我们一起经历二十岁的人，也是家人，</tgt>` | 2197 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1427 |
| 9 | `<src><\|wait\|></src><tgt>所以</tgt>` | `<src>어 책임 이 </src><tgt>所以</tgt>` | 1596 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>없는 거라는 </src><tgt><\|wait\|></tgt>` | 1752 |
| 11 | `<src>조금 </src><tgt>比起责任感，</tgt>` | `<src>조건 삭제 </src><tgt><\|wait\|></tgt>` | 856 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>쓰고 </src><tgt>把“没有责任”这个条件删掉，</tgt>` | 1818 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1536 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 걸 </src><tgt><\|wait\|></tgt>` | 703 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고. </src><tgt>再多放点东西进去。</tgt>` | 1203 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 653 |

---

### Test Example 43 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1046 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>So, this is</tgt>` | 1123 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>というだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 1423 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>not just a visual development environment.</tgt>` | 992 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1280 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローリフを</src><tgt>It's a visual Python development environment.</tgt>` | 2775 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1294 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいではPythonコード</src><tgt>You write the flow chart visually, and then it</tgt>` | 1156 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>がそれから</src><tgt><\|wait\|></tgt>` | 1645 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>generates Python code, which</tgt>` | 2072 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1789 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 637 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているからです。</src><tgt>is then executed to perform signal processing.</tgt>` | 1464 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1150 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt>Yes,</tgt>` | 950 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | 788 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1030 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1091 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1278 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>actually go in your education? Did you </src><tgt>실제로 교육을 얼마나 받으셨나요?</tgt>` | 1620 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 2089 |
| 7 | `<src><\|wait\|></src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src><\|wait\|></src><tgt>고등학교 졸업하셨나요?</tgt>` | 1248 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | 1634 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>to college, </src><tgt>그건 한 단계의 학력 수준입니다. 대학에 가셨나요?</tgt>` | 2000 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | 2003 |
| 11 | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요?</tgt>` | 1891 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1580 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>그것도 또 다른 단계의 학력 수준입니다. 자, 이제</tgt>` | 1278 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt><\|wait\|></tgt>` | 1065 |
| 15 | `<src>online. </src><tgt>오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 854 |

---

### Test Example 45 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手</src><tgt>相手の</tgt>` | 982 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>的感情或</src><tgt><\|wait\|></tgt>` | 1135 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真性意图的，</src><tgt>感情や真意を察知したり感じ取ったりすること、</tgt>` | 2130 |
| 5 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 606 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くは</tgt>` | 1493 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常</src><tgt><\|wait\|></tgt>` | 1635 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>会听到人们这样说：</src><tgt>よく聞くでしょう。</tgt>` | 1780 |
| 9 | `<src>这样说：“</src><tgt>よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1640 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 824 |
| 11 | `<src>这个人</src><tgt>「ほら、</tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1494 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了，</src><tgt>この人また嘘をついてるよ」</tgt>` | 2017 |
| 13 | `<src>他的眼睛</src><tgt>また嘘をついている。目が</tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1553 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt>って。その人の目はすべてを物語ってるんだ」</tgt>` | 1178 |
| 15 | `<src><\|wait\|></src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 648 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说。</src><tgt>つまり、</tgt>` | 744 |
| 17 | `<src><\|wait\|></src><tgt>つまり…</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 851 |

---

### Test Example 46 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 간 것 </src><tgt><\|wait\|></tgt>` | 1140 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src><\|wait\|></src><tgt>目がかすんでいて、</tgt>` | 1061 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>생활 할 필요 가 </src><tgt><\|wait\|></tgt>` | 1232 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>이한테 서름이 돋은 </src><tgt>このせいで</tgt>` | 1266 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>바찰이 돋은 </src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 뭐냐면 </src><tgt>皮膚に</tgt>` | 1603 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1645 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>じゅもんが立ち上がったような感じなんです。だから、一緒に遊ぼうってことですね。</tgt>` | 2123 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | 1649 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>물릴 거고 </src><tgt>幽霊が来たら噛まれて、</tgt>` | 2119 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>시눈 이 오면 </src><tgt><\|wait\|></tgt>` | 1780 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>目が見えたら「守ってくれ」って</tgt>` | 1938 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | 1386 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>刺してくるから、安心して</tgt>` | 878 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 간다. </src><tgt><\|wait\|></tgt>` | 916 |

---

### Test Example 47 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계속 뭐 </src><tgt><\|wait\|></tgt>` | 1084 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>물론 이제 </src><tgt>もちろん、</tgt>` | 911 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1117 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースはあります。Aという人と</tgt>` | 1434 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 서로 </src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>컨턴트예요. </src><tgt>Bという人がコンテンツを交換している場合です。</tgt>` | 2797 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이런 컨턴트예요. </src><tgt><\|wait\|></tgt>` | 1302 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src><\|wait\|></src><tgt>そういったコンテンツです。</tgt>` | 969 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1757 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aという人が悪性コードを</tgt>` | 2190 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1818 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비란 사람 이 </src><tgt>渡したとき、Bという人が</tgt>` | 1796 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스사이트 </src><tgt><\|wait\|></tgt>` | 1112 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크리 에터에서 </src><tgt>実際にクロスサイトクリエーターから</tgt>` | 865 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>예스 파일 까지 </src><tgt><\|wait\|></tgt>` | 478 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까, </src><tgt>yesファイルまで感染してしまうかどうか、</tgt>` | 1018 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 924 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 983 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | 1989 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1258 |
| 5 | `<src>큰 폭의 </src><tgt>these large- cap stocks</tgt>` | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | 673 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 2137 |
| 7 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1070 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1631 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt><\|wait\|></tgt>` | 1859 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1817 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 1091 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 항상 </src><tgt>these large- cap stocks will likely rise sharply. But since these lighter stocks lead the market first,</tgt>` | 1589 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 1473 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1228 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1020 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt>you should always keep an eye on the market cap of those lighter stocks.</tgt>` | 1088 |

---

### Test Example 49 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1139 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>一旦进入，就会完全迷失方向。</tgt>` | 1259 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1117 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1006 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | 1445 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>고 있는데 </src><tgt>开车的话，只能走，只能爬，</tgt>` | 2136 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>막굴거면 말할 </src><tgt><\|wait\|></tgt>` | 1337 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>것도 없고요. 외국 에 </src><tgt>根本没法说。如果</tgt>` | 1612 |
| 9 | `<src><\|wait\|></src><tgt>就不用说了，去外国</tgt>` | `<src>나가 는 것도 </src><tgt><\|wait\|></tgt>` | 1700 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. </src><tgt>要往外走，那简直是天方夜谭。</tgt>` | 2267 |
| 11 | `<src>좀 창피 하네요. </src><tgt>就更惨了。真有点丢人。</tgt>` | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | 1896 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt>真有点尴尬。不如</tgt>` | 1759 |
| 13 | `<src>이제 </src><tgt>不过，</tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1188 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>물어요. 그거 는 </src><tgt>努力学习？</tgt>` | 1031 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>된 것 같아요. </src><tgt><\|wait\|></tgt>` | 818 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>好像是这样。</tgt>` | 578 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 765 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 분석 을 </src><tgt>そして、これについて多くの人が</tgt>` | 1225 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | 1319 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 로쿠자 의 </src><tgt>分析を挙げています。ここで</tgt>` | 1318 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 938 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ロクジャの分析を見ると、ソニーが</tgt>` | 2502 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | 1061 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>파이프 를 </src><tgt>26ビットFPパイプラインを</tgt>` | 1526 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | 1871 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | 2159 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1777 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>Xbox Series X에서도 없는 </src><tgt>XboxSeriesXにはない</tgt>` | 1799 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1188 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュ</tgt>` | 1041 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 858 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>L3もありません。</tgt>` | 613 |

---

### Test Example 51 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 943 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt>活動、</tgt>` | 934 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1107 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt>つまり自分自身で基準を定義することです。</tgt>` | 1504 |
| 5 | `<src>absolutely correct, </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1271 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct, </src><tgt>なぜなら、</tgt>` | 2032 |
| 7 | `<src>is is that </src><tgt>しかし現実には、</tgt>` | `<src>but the reality is </src><tgt><\|wait\|></tgt>` | 1329 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>that because we're the new kid on the </src><tgt>あなたは完全に正しい。しかし、現実には、</tgt>` | 1908 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt><\|wait\|></tgt>` | 1724 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>私たちが新しい世代だからです。そして、</tgt>` | 2160 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>standards have changed from 20 </src><tgt><\|wait\|></tgt>` | 1831 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt>20年前に基準が変わったので、</tgt>` | 1885 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1169 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard </src><tgt>より高い基準を</tgt>` | 994 |
| 15 | `<src>everything at this point is being </src><tgt>より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point is being </src><tgt><\|wait\|></tgt>` | 937 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>held to a higher standard. </src><tgt>求められているのです。なぜなら、今の時代はすべてがより高い基準で評価されているからです。</tgt>` | 689 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 787 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>为了以的首支</src><tgt>첫 번째</tgt>` | 1019 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>觉知到的那个现象，</src><tgt><\|wait\|></tgt>` | 1447 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src><\|wait\|></src><tgt>깨달음에 이르는 현상을 위해,</tgt>` | 1140 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>每当我们处于</src><tgt><\|wait\|></tgt>` | 1181 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1635 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>爱之中，所有的爱，</src><tgt>우리가 사랑 속에 있을 때, 모든 사랑은</tgt>` | 1980 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1434 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>我们也同时进入</src><tgt>동시에</tgt>` | 1683 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1869 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨。在早上的时候，</src><tgt>혐오로 들어갑니다. 아침에는</tgt>` | 1718 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | 660 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt>사랑이지만, 밤이 되면</tgt>` | 1812 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 1177 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>恨。</src><tgt>혐오로 변합니다.</tgt>` | 1008 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆。</src><tgt><\|wait\|></tgt>` | 809 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt>그 시계추는 계속해서</tgt>` | 638 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>一动，</src><tgt><\|wait\|></tgt>` | 375 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 926 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | 1326 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src><\|wait\|></src><tgt>您将无法</tgt>` | 1121 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1327 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | 1878 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 1411 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into this </src><tgt>所以，如果您</tgt>` | 1765 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1651 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>situation where you realize </src><tgt>遇到这种情况，发现</tgt>` | 1452 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | 1104 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>某个资源里放错了媒体文件，</tgt>` | 1927 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | 1771 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt>请务必告诉我们，我们</tgt>` | 1300 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 911 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files and then making sure they </src><tgt>会帮忙移动这些媒体文件，并确保它们</tgt>` | 1179 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 372 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>能正确备份。</tgt>` | 463 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1235 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 889 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>第1セクションで少し混乱してて、</tgt>` | 1854 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 753 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the EHR fields </src><tgt>EHRの項目について</tgt>` | 1308 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1479 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>being of critical importance </src><tgt>重要性が</tgt>` | 1654 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus variant </src><tgt><\|wait\|></tgt>` | 1600 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 511 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>databases, </src><tgt>バリアントデータベースと比べて、</tgt>` | 1769 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | 2101 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if you </src><tgt>それは私の大好きな分野の一つです。もし</tgt>` | 1903 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>don't agree </src><tgt><\|wait\|></tgt>` | 1673 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields that need </src><tgt>必要な項目について合意できなければ、</tgt>` | 1276 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these </src><tgt><\|wait\|></tgt>` | 1004 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>そのデータソースに</tgt>` | 823 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 570 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>there's nothing to draw from, right? </src><tgt>アクセスできなければ、参照できるものがないわけですよね？</tgt>` | 628 |
| 19 | `<src><\|wait\|></src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 437 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 804 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼はイエスを</tgt>` | 1104 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>He knows that </src><tgt>飢えていると知ります。</tgt>` | 1173 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | 1387 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src><\|wait\|></src><tgt>彼は、</tgt>` | 1347 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | 2139 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>And so he says </src><tgt>40日間荒野で食べ物も水もなかったことを知っています。だから彼はこう言いました。</tgt>` | 2050 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | 1499 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it." </src><tgt>「おい、お前が神の御子なら、証明してみろ」と。</tgt>` | 2829 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn these </src><tgt><\|wait\|></tgt>` | 1095 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>stones to bread." </src><tgt>「この石をパンに変えろ」と。</tgt>` | 1918 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1257 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>say deal with </src><tgt><\|wait\|></tgt>` | 894 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>that temptation? </src><tgt>彼はその誘惑にどう立ち向かったのでしょうか？</tgt>` | 1060 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 496 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>John utterly </src><tgt>いや、</tgt>` | 450 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>did better alone. </src><tgt><\|wait\|></tgt>` | 450 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 930 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1245 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1145 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분에서는</tgt>` | 1105 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | 1308 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>的部分。</src><tgt>거실 부분이 보입니다.</tgt>` | 1810 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>那客厅一般都是</src><tgt>거실은 보통</tgt>` | 1764 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>属于我们要</src><tgt><\|wait\|></tgt>` | 1611 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt>쉴 수 있는 공간이라</tgt>` | 1317 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 983 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>呢，这身体的部分</src><tgt>몸의</tgt>` | 1787 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>会反映的是</src><tgt><\|wait\|></tgt>` | 456 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt>부분은</tgt>` | 1495 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 1119 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 541 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt>잠시 앉아서 쉬면서</tgt>` | 854 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们可以看到这边是</src><tgt><\|wait\|></tgt>` | 928 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的嘛。</src><tgt>쉬어야 한다는 걸 보여줍니다. 여기는 지금 아무도 없는 모습이네요.</tgt>` | 755 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 286 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>啊，所以是说。</src><tgt>그러니까...</tgt>` | 411 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 911 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | 1016 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1221 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt>最高法院</tgt>` | 1125 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | 623 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt>是最后才跟进的，而不是引领。我不认为法院想</tgt>` | 3110 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1611 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt>成为</tgt>` | 508 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1628 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>社会变革的前沿阵线。如今，</tgt>` | 2117 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1806 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src>but they rather reflect </src><tgt>但它们更多地反映了</tgt>` | 1631 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 743 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1002 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>that's already emerged. </src><tgt>已经形成的共识。</tgt>` | 906 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 950 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>So you have </src><tgt>所以，</tgt>` | 516 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 484 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 436 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>你还有一些联邦法官，他们……</tgt>` | 385 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 827 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>彼らは極めて稀な存在で、</tgt>` | 1199 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1153 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up to </src><tgt>よく</tgt>` | 986 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1339 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>completely revolutionize the world. </src><tgt>世界を完全に変革するんです。</tgt>` | 1994 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1344 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>Their personality is </src><tgt>その</tgt>` | 1709 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1689 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src>While </src><tgt>性格は矛盾をはらんでいます。</tgt>` | 1758 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 950 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>they're extroverted, </src><tgt>外向的で、</tgt>` | 1737 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1641 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations, </src><tgt>無意味な会話や</tgt>` | 1222 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1002 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>and like to get straight to the </src><tgt>つまらない話は嫌い。そして、</tgt>` | 879 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 568 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love to </src><tgt>要点をすぐに言いたいタイプです。</tgt>` | 494 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 342 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and they </src><tgt>悪魔の肩を背負うのも好きで、</tgt>` | 354 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 296 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 340 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 300 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. </src><tgt>E.T.P.は</tgt>` | 394 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stands for </src><tgt><\|wait\|></tgt>` | 260 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂ね</src><tgt>Well,</tgt>` | 833 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | 934 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>みたいですなのでここのね</src><tgt>it looks like they're making it right now in the cafeteria. So,</tgt>` | 1636 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | 1338 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1363 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1924 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1757 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので</src><tgt>Goldstone Hotel is also planned to have breakfast.</tgt>` | 1628 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | 732 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | 1774 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1753 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なっていう方はですね</src><tgt>If you're thinking of staying at Goldstone Hotel in the future,</tgt>` | 2040 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1151 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>thinking about staying here in the future,</tgt>` | `<src>もまあいいんじゃないか</src><tgt>you might want to consider it.</tgt>` | 1078 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なとはい。</src><tgt><\|wait\|></tgt>` | 976 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思いますここ</src><tgt>I think it's a good idea.</tgt>` | 569 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>のホテルからですね</src><tgt><\|wait\|></tgt>` | 467 |
| 19 | `<src>駅ももう</src><tgt>From this hotel,</tgt>` | `<src>부산駅ももう</src><tgt>From this hotel,</tgt>` | 428 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt><\|wait\|></tgt>` | 327 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分</src><tgt><\|wait\|></tgt>` | 307 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | 387 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | 304 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | 297 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>ホテルになってますので</src><tgt>the location is so good that you can walk to Busan Station in about a minute or so.</tgt>` | 380 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 236 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt>So if you're interested,</tgt>` | 285 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 238 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね今回は。</src><tgt>please give it some thought. Well, that's it for this time.</tgt>` | 348 |

---

### Test Example 60 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 890 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>당무 를 거부 한 </src><tgt>Lee Jun- seok</tgt>` | 1173 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1354 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 850 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1399 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1756 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1497 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>previously gave the excuse that he was refusing to perform his official duties for the sake of the candidate and for the sake of the candidate's victory, even putting on quite a show. But now</tgt>` | 3318 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1204 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1220 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Jong- in,</tgt>` | 2052 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | 1715 |
| 13 | `<src><\|wait\|></src><tgt>Lee Jun -seok</tgt>` | `<src>드러내 놓고 윤석열 후보 를 </src><tgt>Lee Jun- seok revealed that he</tgt>` | 1366 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 933 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 971 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 535 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 497 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 419 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt>was determined to show his aggressive intent to bring down Yoon Suk- yeol.</tgt>` | 430 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 249 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상납 건 </src><tgt>Lee Jun- seok's alleged sex- for-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -` | 2469 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 225 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 183 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 얼마나 </src><tgt><\|wait\|></tgt>` | 192 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재입니까. </src><tgt>How huge of a boon is this for the opposition party's attack?</tgt>` | 267 |
