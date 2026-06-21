# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9735
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.2252
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
  - PROCESS_TIME_MS_AVG: 1316.3300
  - PROCESS_TIME_MS_P50: 1232.0190
  - PROCESS_TIME_MS_P95: 2146.6470
  - PROCESS_TIME_MS_MAX: 2905.7840

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
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1146 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>在身上这一点？</src><tgt>Why is it on the body?</tgt>` | 1110 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个优势</src><tgt><\|wait\|></tgt>` | 1158 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src>很大，然后</src><tgt>This is a big advantage.</tgt>` | 1243 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那</src><tgt><\|wait\|></tgt>` | 1216 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在面对</src><tgt>So when I face</tgt>` | 601 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>其他人才，</src><tgt><\|wait\|></tgt>` | 1637 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>other people,</tgt>` | 1621 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>感觉</src><tgt><\|wait\|></tgt>` | 652 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 1558 |
| 11 | `<src>仁儿。</src><tgt>this kind of walnut kernels.</tgt>` | `<src>其他人才。</src><tgt>I feel like these other people.</tgt>` | 1469 |

---

### Test Example 2 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后</src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>呢，</src><tgt>砂を掘り終わった後、</tgt>` | 1268 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压紧呢</src><tgt><\|wait\|></tgt>` | 1046 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了，</src><tgt>内部の圧密エネルギーも弱まり、</tgt>` | 1699 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后就</src><tgt><\|wait\|></tgt>` | 833 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>停留在</src><tgt>そのまま</tgt>` | 1505 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1077 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>低能量的运行</src><tgt>比較的低いエネルギーの</tgt>` | 1382 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态。</src><tgt><\|wait\|></tgt>` | 1699 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>運行状態に留まってしまいます。これが、いわゆる</tgt>` | 1315 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>异于状态。</src><tgt><\|wait\|></tgt>` | 1803 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气鼠，</src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>是容易的。</src><tgt>「気鼠」は簡単です。</tgt>` | 1288 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 895 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>只有一个</src><tgt>しかし、</tgt>` | 1156 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导，</src><tgt><\|wait\|></tgt>` | 1380 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如</src><tgt>師匠の指導が一つあるだけです。</tgt>` | 1548 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>除于中天，</src><tgt><\|wait\|></tgt>` | 1247 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt>中天を除けば、</tgt>` | 1240 |
| 9 | `<src>虚阿凡</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1774 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt>反転させる必要があります。</tgt>` | 1381 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>师傅，</src><tgt><\|wait\|></tgt>` | 1689 |

---

### Test Example 4 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 832 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Apple, </src><tgt>I am Apple,</tgt>` | 1074 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축복 받히고 </src><tgt><\|wait\|></tgt>` | 1173 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 744 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모호 로 죽인 </src><tgt><\|wait\|></tgt>` | 1024 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헬레나 </src><tgt><\|wait\|></tgt>` | 1846 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1515 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 673 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들인 </src><tgt><\|wait\|></tgt>` | 1822 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>것입니다. </src><tgt>and the same generation as Helena Park Han, who was killed by her own ambiguous death.</tgt>` | 2856 |

---

### Test Example 5 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 815 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt>様々な研究を</tgt>` | 861 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1143 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people? This is </src><tgt>行いましたか？極度に幸せな人たちを対象に。これは</tgt>` | 1472 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip the stem </src><tgt><\|wait\|></tgt>` | 1365 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>「先端研究」です。</tgt>` | 1372 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 844 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt>最も幸せな</tgt>` | 1697 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1742 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. </src><tgt>人々の10%を対象にしています。</tgt>` | 934 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>People that we can learn from. </src><tgt><\|wait\|></tgt>` | 2389 |

---

### Test Example 6 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要做</src><tgt><\|wait\|></tgt>` | 1180 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>的是，</src><tgt>Parents need to do:</tgt>` | 1050 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1155 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>深深的爱交</src><tgt>show their deep love</tgt>` | 1306 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt><\|wait\|></tgt>` | 1315 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>所以</src><tgt>by pouring our love into the water.</tgt>` | 1699 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>可以</src><tgt><\|wait\|></tgt>` | 901 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>对孩子心里影响，</src><tgt>This will have a positive impact on the child's heart,</tgt>` | 1542 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>以耐心</src><tgt><\|wait\|></tgt>` | 1723 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>等他</src><tgt>and help them</tgt>` | 1550 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1501 |

---

### Test Example 7 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 756 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 1049 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>村中まだ</src><tgt><\|wait\|></tgt>` | 1206 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>他还是村里一年级。</tgt>` | 1323 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1313 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう密告</src><tgt>就在那个时候，</tgt>` | 1902 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>前提を</src><tgt><\|wait\|></tgt>` | 1459 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう体図して</src><tgt>他已经把密告的前提</tgt>` | 792 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>やってあげると</src><tgt><\|wait\|></tgt>` | 1698 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt>设好了，就算过了十年，</tgt>` | 2254 |
| 11 | `<src>大した。</src><tgt>十年后也不会有什么大……</tgt>` | `<src>大した</src><tgt><\|wait\|></tgt>` | 931 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1210 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>식성들은 </src><tgt>Those with a favorable disposition are</tgt>` | 1215 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1017 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>actually not highly intelligent,</tgt>` | 1312 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1303 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt>but were randomly selected</tgt>` | 1585 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>식성들이 </src><tgt><\|wait\|></tgt>` | 1142 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>있었습니다. </src><tgt>and were</tgt>` | 1197 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1817 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1335 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교사 들은 </src><tgt>teachers who didn't know the facts</tgt>` | 2005 |

---

### Test Example 9 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1025 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这里开始，</tgt>` | 1159 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めたもので</src><tgt><\|wait\|></tgt>` | 1159 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt>我才开始的。</tgt>` | 1195 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法を</src><tgt><\|wait\|></tgt>` | 1414 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ごうぎゃん</src><tgt>我</tgt>` | 1599 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1147 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>生産の</src><tgt>生产了</tgt>` | 1116 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1846 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の絵</src><tgt>像Lunal这样的</tgt>` | 1345 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1763 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>は田舎の中学生でも</src><tgt>人，</tgt>` | 1876 |

---

### Test Example 10 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1134 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1057 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1170 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learned and to repeat, </src><tgt>重复一下。学到了，重复一下。</tgt>` | 1448 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out you're good at </src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>发现自己擅长的地方，多做一些。</tgt>` | 2095 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And will you not </src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>get to people </src><tgt>你会不会</tgt>` | 1760 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1363 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src>and </src><tgt>遇到身边的人来帮助你，</tgt>` | 1870 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and tell next time </src><tgt><\|wait\|></tgt>` | 1916 |

---

### Test Example 11 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 961 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>용신이 </src><tgt>Ah, I'm a Yong-shin</tgt>` | 1369 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>칼 </src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>용신이에요. </src><tgt>and a Kai- shin.</tgt>` | 1285 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>그래서 용신이 가 </src><tgt><\|wait\|></tgt>` | 1336 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>섞여 </src><tgt>So, when the Yong- shin mixes with</tgt>` | 1996 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1731 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>the other one, it's like— wow,</tgt>` | 2049 |
| 9 | `<src>진짜 이거 </src><tgt>Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1397 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행운 으로 </src><tgt>this is really</tgt>` | 1703 |
| 11 | `<src>진짜. </src><tgt>seriously killer for a hangover, for real.</tgt>` | `<src>조금 쥐기 맞는 것 </src><tgt><\|wait\|></tgt>` | 1986 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 839 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 1090 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into your body. </src><tgt><\|wait\|></tgt>` | 1188 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does </src><tgt>进入你的身体。</tgt>` | 1121 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么？</tgt>` | 2023 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 1741 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it a tension in your chest? </src><tgt>是头部的？还是胸部的紧张？</tgt>` | 2120 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I have </src><tgt><\|wait\|></tgt>` | 1769 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>a lot of </src><tgt>我</tgt>` | 1362 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>things I use. </src><tgt><\|wait\|></tgt>` | 1908 |

---

### Test Example 13 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果在女高中</src><tgt><\|wait\|></tgt>` | 860 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>生与长相</src><tgt>If a girl is born with</tgt>` | 1274 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>不怪的人之间，</src><tgt><\|wait\|></tgt>` | 1054 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有着某种</src><tgt>a certain</tgt>` | 1122 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>典型性，</src><tgt><\|wait\|></tgt>` | 1393 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>typicality, would it be</tgt>` | 1941 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1434 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天颞叶</src><tgt>from the temporal lobe</tgt>` | 766 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1719 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>to begin?</tgt>` | 1687 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1442 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>学习篇，</src><tgt>The Yang Zisi Study Guide,</tgt>` | 2017 |

---

### Test Example 14 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 </src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>너무 이 저열여야 </src><tgt>これ、</tgt>` | 1152 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>내일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1096 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>진짜 보살 도요 </src><tgt>本当に</tgt>` | 1231 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 고생 </src><tgt><\|wait\|></tgt>` | 1414 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>인데 꿈일 프로 </src><tgt>菩薩でもない。自分の苦労を</tgt>` | 2018 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보고 있고 </src><tgt><\|wait\|></tgt>` | 1615 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 이 보살 로 </src><tgt>見てるんだ。私だけが</tgt>` | 2049 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 프로 보이 색 우주 바지 </src><tgt><\|wait\|></tgt>` | 1753 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>다원 디 보살이든 </src><tgt>この菩薩に見られる、宇宙の全てを</tgt>` | 1683 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1874 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 899 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>산줄에 죽여달라 </src><tgt>I want to be killed by the other mountain clans.</tgt>` | 1447 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>제가 죽고 내가 </src><tgt><\|wait\|></tgt>` | 984 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔어도 </src><tgt>Even if I came here to die and let them kill me,</tgt>` | 2134 |
| 5 | `<src>다른 잔찜에 </src><tgt>came in here to do it.</tgt>` | `<src>다른 잔찜이 </src><tgt><\|wait\|></tgt>` | 588 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여달라 </src><tgt>I'd still want to be killed by the other clans.</tgt>` | 2146 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>하자는 거야 내가 </src><tgt><\|wait\|></tgt>` | 1618 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt>I'm not even hearing the big noise,</tgt>` | 2129 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주인 들이야 </src><tgt><\|wait\|></tgt>` | 2625 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아 </src><tgt>you masters,</tgt>` | 1223 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1145 |

---

### Test Example 16 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 948 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>我们就是</src><tgt>Faced with this situation,</tgt>` | 1101 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题就</src><tgt><\|wait\|></tgt>` | 1138 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>赶紧的回报主管，</src><tgt>we just quickly report it to our supervisor.</tgt>` | 1425 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1268 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们下了这个状况，</src><tgt>Or we let them know about the situation.</tgt>` | 2026 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1687 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't think you have to handle everything yourself.</tgt>` | 2191 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>工具理性承担，</src><tgt><\|wait\|></tgt>` | 2086 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>责任而已，</src><tgt>Just take responsibility for your part.</tgt>` | 1044 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>所以就属行，</src><tgt><\|wait\|></tgt>` | 1977 |

---

### Test Example 17 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1194 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>And then, </src><tgt>好的。然后，</tgt>` | 1106 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1196 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src>the instructor </src><tgt>在这些例子之后，</tgt>` | 1158 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>will </src><tgt><\|wait\|></tgt>` | 1351 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>allow us to use </src><tgt>讲师会让我们</tgt>` | 1459 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 865 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际使用</tgt>` | 1500 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1778 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>这些值。</tgt>` | 647 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 2513 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>game dot sort array. </src><tgt>所以，这个game.sort数组。</tgt>` | 952 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1514 |

---

### Test Example 18 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1104 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 891 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1130 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>緩むと</src><tgt>기어가 느슨해지면</tgt>` | 1202 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えなくなって</src><tgt><\|wait\|></tgt>` | 1037 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>しまうので、</src><tgt>신호가 꺼지게 되니까</tgt>` | 917 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1799 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>逆ネジの</src><tgt>기어 앞쪽에</tgt>` | 1734 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1817 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>ついているっていうこと</src><tgt>역나사 너트가</tgt>` | 874 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 2246 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>있다는 거죠. 네,</tgt>` | 991 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 1470 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 697 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt>제가</tgt>` | 860 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活的一个</src><tgt><\|wait\|></tgt>` | 1133 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt>제 삶의 궤도로 돌아가게 해 주세요.</tgt>` | 1239 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够哈</src><tgt><\|wait\|></tgt>` | 688 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在它下面的时候，</src><tgt>그 아래에 있을 때,</tgt>` | 1196 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日谈</src><tgt><\|wait\|></tgt>` | 1838 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>日愿解，所以</src><tgt>매일의 다짐을 해보세요. 그래서</tgt>` | 2045 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我们当时</src><tgt><\|wait\|></tgt>` | 1721 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>背动的时候，</src><tgt>그때 저희가</tgt>` | 1461 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>是一个小小的愿望哈，</src><tgt><\|wait\|></tgt>` | 1770 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src><\|wait\|></src><tgt>작은 소망을 품고 있었어요.</tgt>` | 2173 |

---

### Test Example 20 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1128 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>があの</src><tgt>T- shirts and such</tgt>` | 1154 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ようなものも</src><tgt>are also available</tgt>` | 1228 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt>for you to wear. Please feel free to join us.</tgt>` | 1982 |
| 7 | `<src>ご連絡としては</src><tgt>so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1457 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt>That's all for the contact information.</tgt>` | 735 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>て、</src><tgt><\|wait\|></tgt>` | 1701 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt>Um,</tgt>` | 1324 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>連絡の案内があります</src><tgt><\|wait\|></tgt>` | 1740 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ので、もう少々お待ちください。</src><tgt>there is a contact guide, so please wait a moment.</tgt>` | 2356 |

---

### Test Example 21 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1134 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>なんとちょっと距離が離れてくる</src><tgt>嗯，距离</tgt>` | 1106 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じを</src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>超おしゃれな</src><tgt>会稍微拉开一点，那种感觉，</tgt>` | 1372 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>パパゴイですね</src><tgt><\|wait\|></tgt>` | 1392 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>会話していただく</src><tgt>会很酷，</tgt>` | 1867 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>ってすぐ行き来して다가</src><tgt><\|wait\|></tgt>` | 1662 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>し</src><tgt>我们俩会来来去去聊，</tgt>` | 778 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ジュネズミと</src><tgt><\|wait\|></tgt>` | 1594 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>トモンツミオンと</src><tgt>还有ジュ内子和トモンツミ翁，</tgt>` | 2800 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>シャグが強いので</src><tgt><\|wait\|></tgt>` | 1790 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt>因为他们俩的Shagu很强，所以</tgt>` | 865 |

---

### Test Example 22 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 995 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Frenkel, </src><tgt>제 이름은 프렌켈입니다.</tgt>` | 1398 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>and I am currently studying </src><tgt><\|wait\|></tgt>` | 931 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src>in a PhD </src><tgt>현재</tgt>` | 1070 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in finance </src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a B.S. in psychology. </src><tgt>금융 분야 박사 과정과 심리학 학사 학위를 받고 있습니다.</tgt>` | 2167 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 1617 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here today </src><tgt>오늘 여기에서</tgt>` | 1686 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 682 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go </src><tgt>그리고 앞으로도</tgt>` | 2683 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>into corporate </src><tgt><\|wait\|></tgt>` | 1485 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt>기업 컨설팅 분야로 나아가고 싶습니다.</tgt>` | 1166 |

---

### Test Example 23 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this, </src><tgt><\|wait\|></tgt>` | 923 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで </src><tgt>그래서 이 점을 가지고</tgt>` | 1096 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 1126 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>という設定を</src><tgt>이 설정을</tgt>` | 1218 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>しましたね。</src><tgt><\|wait\|></tgt>` | 1358 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>で、</src><tgt>했습니다. 그리고</tgt>` | 1269 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 855 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>派生利用種の仕組み</src><tgt>파생 이용 방식의</tgt>` | 1892 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1761 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>元、</src><tgt>구조는</tgt>` | 1071 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>setubijiが</src><tgt><\|wait\|></tgt>` | 2037 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src><\|wait\|></src><tgt>원래 setubiji가</tgt>` | 1833 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>動きます。</src><tgt><\|wait\|></tgt>` | 840 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 818 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>A、Aアンデスに</src><tgt>Um, A, A Andes</tgt>` | 1124 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いるな場面で</src><tgt><\|wait\|></tgt>` | 1217 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>A制服かどうかっていうの</src><tgt>in that situation, whether they're in A uniforms or not,</tgt>` | 2205 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときにまあ</src><tgt><\|wait\|></tgt>` | 601 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>Aのランクを</src><tgt>when you're checking the A rank,</tgt>` | 1984 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べることであの</src><tgt><\|wait\|></tgt>` | 1672 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その制服かどうかっていうの</src><tgt>you know,</tgt>` | 1999 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を証明する制服で</src><tgt><\|wait\|></tgt>` | 2128 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt>you're guaranteed to be able to prove whether they're in A uniforms.</tgt>` | 1390 |
| 11 | `<src>といったような</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>といったら使い方を</src><tgt><\|wait\|></tgt>` | 1804 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されます。</src><tgt>That's how you use it.</tgt>` | 1255 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 856 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼 늘어나면서</tgt>` | 1259 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1088 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. And when those </src><tgt>화학 결합도 에너지를 저장합니다. 그리고</tgt>` | 1972 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 711 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 결합이 끊어지면, 그 잠재 에너지는</tgt>` | 2212 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1485 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>다른 종류의 에너지로 변환됩니다.</tgt>` | 2129 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 2185 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>예를 들어 열이나 빛 같은 에너지로요. 아니면</tgt>` | 1082 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 1816 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt>다른 결합을 만드는 데 사용되기도 합니다.</tgt>` | 1499 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 872 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>进入到二classList</src><tgt>2つ目は、</tgt>` | 1109 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 1168 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>还服务在一级</src><tgt>二つのクラスに</tgt>` | 1228 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1392 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>一线平安的大牛们。</src><tgt>サービスを提供している第一線のベテランたちです。</tgt>` | 2001 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1616 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做维信</src><tgt>例えば、</tgt>` | 659 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好事几点，</src><tgt><\|wait\|></tgt>` | 1767 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>「維信」のコミュニケーションを始める時間を見つけると、</tgt>` | 2743 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维信好平分</src><tgt><\|wait\|></tgt>` | 1536 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的星棒，</src><tgt>維信の星棒を</tgt>` | 1003 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1402 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1072 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt>あるいは、</tgt>` | 945 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1171 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何かを書きたい、テキストを書く必要がある場合、</tgt>` | 1485 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1260 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>そもそも</tgt>` | 1867 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1626 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. It's like oh, </src><tgt>スペルが全くわからないことに気づく。まるで「ああ、</tgt>` | 1818 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 683 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>started with </src><tgt>この単語は</tgt>` | 2564 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a double P, </src><tgt><\|wait\|></tgt>` | 595 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double L. I don't know </src><tgt>PPで始まる、LLで始まる、なんてことだ。</tgt>` | 2326 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1209 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1212 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt>19세기</tgt>` | 1198 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment </src><tgt><\|wait\|></tgt>` | 1007 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt>수정안의 의미와</tgt>` | 1323 |
| 5 | `<src>history as a guide </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1379 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt>역사를 살펴보고, 이것이</tgt>` | 1930 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 1645 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt>정치적 변화가 어떻게 일어날 수 있는지</tgt>` | 1778 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>United States. </src><tgt><\|wait\|></tgt>` | 748 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침이 될 수 있습니다.</tgt>` | 2906 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1927 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of course I </src><tgt>물론</tgt>` | 1096 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>married. </src><tgt><\|wait\|></tgt>` | 1062 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>砸到了一个</src><tgt><\|wait\|></tgt>` | 812 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>钱包，</src><tgt>財布にぶつかって、</tgt>` | 1142 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1091 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>拿到了钱包之后，</src><tgt>もし財布を落としてしまったら、</tgt>` | 1437 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1277 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>就要先</src><tgt>必ず</tgt>` | 1589 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt><\|wait\|></tgt>` | 1113 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想着哎，那我</src><tgt>守ってください。そうしないと、</tgt>` | 1291 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>再去操作</src><tgt><\|wait\|></tgt>` | 1739 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦，</src><tgt>後で操作しようと思っても、</tgt>` | 1918 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1259 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそんなことを言うのかというと、</tgt>` | 2152 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1172 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt>それは</tgt>` | 853 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>已经正常</src><tgt>I was already</tgt>` | 1056 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>喉咙扁桃炎，</src><tgt><\|wait\|></tgt>` | 1227 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src>所以</src><tgt>suffering from a normal sore throat,</tgt>` | 1305 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1391 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>提前大概有</src><tgt>so I insisted on not having surgery and had</tgt>` | 2025 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>十二三岁医生来</src><tgt><\|wait\|></tgt>` | 1722 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>诊断，</src><tgt>a doctor between twelve and thirteen years old to diagnose me.</tgt>` | 2181 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 2475 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下剃腿，</src><tgt>I had my legs cut off, shaved, and</tgt>` | 741 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1822 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>no problem at all.</tgt>` | 1165 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>以后的一刻的离开。</src><tgt><\|wait\|></tgt>` | 1038 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 921 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이루 어떨 때는 </src><tgt>Sometimes, when it's made of vanadium,</tgt>` | 1633 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 100일인가 </src><tgt><\|wait\|></tgt>` | 784 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 600잔 </src><tgt>it's about 100, or maybe 600</tgt>` | 2170 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>킬로그램 이상 </src><tgt><\|wait\|></tgt>` | 635 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>중요 하게 굉장히 </src><tgt>kilograms or more,</tgt>` | 1728 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1627 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄이다 </src><tgt>it's definitely a mineral.</tgt>` | 2107 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이기 때문에 </src><tgt><\|wait\|></tgt>` | 1909 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>굉장히 </src><tgt>So it's</tgt>` | 1283 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그렇 던 거죠 </src><tgt><\|wait\|></tgt>` | 1970 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>이제 그 후에다가 </src><tgt>definitely like that. And then, after that,</tgt>` | 1460 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아멘. </src><tgt><\|wait\|></tgt>` | 841 |

---

### Test Example 32 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒</src><tgt><\|wait\|></tgt>` | 1002 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1099 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>在这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1229 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>このローマは一日にしてできたものではなく、</tgt>` | 1584 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1089 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>ですから、今</tgt>` | 1619 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>说明你的一些</src><tgt><\|wait\|></tgt>` | 1113 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>网页啊，</src><tgt>あなたが説明しているウェブページや</tgt>` | 1197 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟粉丝</src><tgt><\|wait\|></tgt>` | 1782 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是你</src><tgt>フォロワーとの関係も、</tgt>` | 1635 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>瞬间就</src><tgt><\|wait\|></tgt>` | 1463 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的。</src><tgt>一瞬で変化するものではないんです。</tgt>` | 1950 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此，</src><tgt><\|wait\|></tgt>` | 1069 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>会建议属鸡的朋友呢，</src><tgt>ですから、鶏年生まれの皆さんには、</tgt>` | 1449 |

---

### Test Example 33 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>getting going </src><tgt>始めたばかりの</tgt>` | 1081 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt>人には、</tgt>` | 1202 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1382 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt>本当に重要な</tgt>` | 959 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1155 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>to </src><tgt>10個の</tgt>` | 1670 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 1931 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I have about one </src><tgt>ものがあります。それについて、</tgt>` | 1081 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 2035 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>about this video. </src><tgt>この動画について1分ほどの動画を撮ります。</tgt>` | 1872 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage </src><tgt><\|wait\|></tgt>` | 830 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>each one </src><tgt>各動画は</tgt>` | 1292 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 994 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 873 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>我们看到的是</src><tgt>이 사진의 일부는</tgt>` | 1141 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1075 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>戴雪的人，但是</src><tgt>눈을 덮은 사람을 보여줍니다. 하지만</tgt>` | 1610 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1168 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src>这通场</src><tgt>이것은 역방향입니다.</tgt>` | 1966 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>好像这样一个状况</src><tgt><\|wait\|></tgt>` | 1679 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>会受到</src><tgt>이런 상황이</tgt>` | 1817 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>去特别注意的是</src><tgt><\|wait\|></tgt>` | 887 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>它能不能</src><tgt>특별히 주목할 점은</tgt>` | 2306 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到与</src><tgt><\|wait\|></tgt>` | 1664 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>他掉不到</src><tgt>그가</tgt>` | 694 |
| 13 | `<src><\|wait\|></src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>与一个易事</src><tgt><\|wait\|></tgt>` | 1436 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt>어떤 일에 엮이지 않느냐는 것입니다.</tgt>` | 1199 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 844 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150개 가 증호 모드에서 </src><tgt>そのうち150個は、防御モードで</tgt>` | 1925 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>100미만 으로 </src><tgt><\|wait\|></tgt>` | 1167 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>100未満の非常に小さな企業が</tgt>` | 1461 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 587 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くありました。一般的には、</tgt>` | 1853 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1810 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>혹은 해외 에 </src><tgt>中小企業は成長するか、あるいは海外に</tgt>` | 2025 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>익스폴드되는데 </src><tgt><\|wait\|></tgt>` | 2655 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>進出しますが、これは</tgt>` | 766 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성기 없던 것은 </src><tgt><\|wait\|></tgt>` | 1760 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않은 </src><tgt>成長も廃業もしていない</tgt>` | 1624 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 998 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 858 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>而HTML</src><tgt>而HTML</tgt>` | 991 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1206 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터 도 </src><tgt>这个</tgt>` | 1184 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1441 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt>计算机也能理解，人也能理解。</tgt>` | 1810 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1354 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt>计算机语言</tgt>` | 830 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1810 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt>的语法，我们现在</tgt>` | 1614 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1488 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>需要编写代码，</tgt>` | 1928 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 976 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>编写这些代码的程序</tgt>` | 1309 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 970 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 957 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src>There </src><tgt>没什么新鲜事。</tgt>` | 1031 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1161 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>was such interests before. </src><tgt>以前也有过这样的兴趣。</tgt>` | 1249 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>Next future TC. </src><tgt>接下来是TC。</tgt>` | 1447 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, </src><tgt><\|wait\|></tgt>` | 804 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>so this is just </src><tgt>嗯，</tgt>` | 1668 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place. </src><tgt><\|wait\|></tgt>` | 1857 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>Look at </src><tgt>这只是另一个地方。</tgt>` | 1070 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2034 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>what </src><tgt><\|wait\|></tgt>` | 1835 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 939 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>would like to bug report should be </src><tgt>看看开发者或工程师想提交的Bug报告</tgt>` | 1612 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>available. </src><tgt><\|wait\|></tgt>` | 931 |

---

### Test Example 38 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1074 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어제 보면 </src><tgt>昨天</tgt>` | 863 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1194 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt>和20岁的人一起</tgt>` | 1165 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 820 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt>一起的弟弟，</tgt>` | 1071 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1862 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt>也是家人一样。所以</tgt>` | 1672 |
| 9 | `<src><\|wait\|></src><tgt>所以</tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1141 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생 한 거다는 </src><tgt>我播放的视频</tgt>` | 1165 |
| 11 | `<src>조금 </src><tgt>比起责任感，</tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 2653 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>有点</tgt>` | 527 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1777 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt>自己想多了，</tgt>` | 1099 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 1098 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>생각 했습니다. </src><tgt>我有点想多了。</tgt>` | 976 |

---

### Test Example 39 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>絶望、</src><tgt><\|wait\|></tgt>` | 1028 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一、二、三、とか</src><tgt>绝望、一、二、三，</tgt>` | 1776 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>です。恐らく</src><tgt><\|wait\|></tgt>` | 614 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt>十秒内</tgt>` | 1136 |
| 5 | `<src>まあ</src><tgt>差不多十秒。</tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1310 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt>一秒内，</tgt>` | 1444 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 877 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt>大概一秒左右吧。</tgt>` | 1703 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1777 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1293 |
| 11 | `<src>おそらく</src><tgt>然后</tgt>` | `<src>恐ろしく</src><tgt><\|wait\|></tgt>` | 1764 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一、</src><tgt>突然</tgt>` | 1462 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>二、三、</src><tgt><\|wait\|></tgt>` | 905 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>であの</src><tgt>十、十一、二、三，</tgt>` | 1372 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮内馬とかが</src><tgt><\|wait\|></tgt>` | 934 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>还有宫内马，</tgt>` | 758 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 843 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니와 </src><tgt>あなたたちも知っているでしょう。</tgt>` | 1255 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 </src><tgt><\|wait\|></tgt>` | 1019 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인 으로 있을 때에 </src><tgt>異邦人としてここにいる時、</tgt>` | 1605 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1086 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>言葉を失った偶像に</tgt>` | 1934 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1616 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>そのまま引きずられて行ったのです。</tgt>` | 1446 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 895 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>ですから、私が</tgt>` | 2116 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 955 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>あなたたちに知らせるように、</tgt>` | 2147 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1326 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>神の霊によって語る者は、</tgt>` | 1147 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 757 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>새 머라 </src><tgt>目を閉じて、</tgt>` | 1086 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1167 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>옛날 서름이 </src><tgt>新しい自分になるんだ。</tgt>` | 1232 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋던 그 차리 돋던 </src><tgt><\|wait\|></tgt>` | 1407 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>그 느낌 이 너무 </src><tgt>昔の自分、あの自信に満ちた感じが</tgt>` | 1951 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1459 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>揺れ動くから、一緒に遊ぼうってこと。</tgt>` | 1142 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 너무 </src><tgt><\|wait\|></tgt>` | 1480 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>불릴 거고 </src><tgt>鬼が呼びに来るから、</tgt>` | 2645 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>새 머리 돋던 </src><tgt><\|wait\|></tgt>` | 605 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>그 짓 쳐줄라고 </src><tgt>新しい自分になるための準備をして、</tgt>` | 2120 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>이제 늙어주려니까 </src><tgt><\|wait\|></tgt>` | 1541 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 마음 에 </src><tgt>もう年を取る準備をするから、心に</tgt>` | 1190 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 725 |

---

### Test Example 42 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1089 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>金運については、今月は</tgt>` | 1524 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 705 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏正财的部分</src><tgt>かなり良いと言えるでしょう。ただ、正財の</tgt>` | 1940 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>又都在</src><tgt><\|wait\|></tgt>` | 649 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>事业方面</src><tgt>部分が、仕事面でも</tgt>` | 1876 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩相当的</src><tgt><\|wait\|></tgt>` | 1684 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>丰厚，收入的</src><tgt>業績がかなり好調で、収入も</tgt>` | 1823 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果</src><tgt><\|wait\|></tgt>` | 698 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>在投资理财方面，</src><tgt>上がっています。投資や資産運用に関しては、</tgt>` | 2837 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1867 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>今月も悪くないですが、</tgt>` | 1309 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对整体来说，</src><tgt><\|wait\|></tgt>` | 1010 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>全体的に見ると少し弱く、</tgt>` | 1042 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一点。</src><tgt><\|wait\|></tgt>` | 641 |

---

### Test Example 43 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1065 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>濡らしてやる。</src><tgt>그럼 젖게 해줄게.</tgt>` | 1379 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 968 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>今</src><tgt>나는 지금</tgt>` | 1112 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き絞みている。</src><tgt><\|wait\|></tgt>` | 1237 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>끌고 있어.</tgt>` | 601 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1664 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超に超えている</src><tgt>한계는 이미</tgt>` | 1794 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>ふれふれきせきを</src><tgt><\|wait\|></tgt>` | 2026 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>아득히 넘었어.</tgt>` | 1790 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1391 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船内で</src><tgt>오랫동안 배 안에서</tgt>` | 2026 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>漕ぐをやっている。</src><tgt><\|wait\|></tgt>` | 1205 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt>노를 젓고 있었지. 나는 이렇게</tgt>` | 1302 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい海賊船を見た。</src><tgt><\|wait\|></tgt>` | 865 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>だが</src><tgt>대단한 해적선을 본 적이 없었어.</tgt>` | 657 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1118 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. How far </src><tgt>학력 수준. 얼마나</tgt>` | 1282 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you </src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go in your </src><tgt>실제로</tgt>` | 1206 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1393 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt>교육을 얼마나 받았나요? 고등학교를 졸업했나요?</tgt>` | 2027 |
| 7 | `<src><\|wait\|></src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1803 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt>그것이 한 단계의 학력 수준입니다.</tgt>` | 2139 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 2276 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, </src><tgt>대학에 갔나요? 그래서</tgt>` | 879 |
| 11 | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt><\|wait\|></tgt>` | 1974 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt>졸업했나요? 그것이 또 다른 단계의 학력 수준입니다.</tgt>` | 1916 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 819 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt>지금까지입니다. 다음에</tgt>` | 812 |
| 15 | `<src>online. </src><tgt>오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 536 |

---

### Test Example 45 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1177 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 해매입니다. </src><tgt>进去之后，会非常迷茫。</tgt>` | 1403 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 961 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>할 거고 </src><tgt>会开车，</tgt>` | 1141 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 </src><tgt><\|wait\|></tgt>` | 1380 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고는 뭐 </src><tgt>走路，</tgt>` | 1594 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1225 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt>去江南区的话，更是无话可说，</tgt>` | 1296 |
| 9 | `<src><\|wait\|></src><tgt>就不用说了，去外国</tgt>` | `<src>외국 에 나가 면 또 장려 리요. </src><tgt><\|wait\|></tgt>` | 1991 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt>去国外的话，更是鼓励。</tgt>` | 2598 |
| 11 | `<src>좀 창피 하네요. </src><tgt>就更惨了。真有点丢人。</tgt>` | `<src>신기 해네요. </src><tgt><\|wait\|></tgt>` | 897 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt>挺神奇的。相反，现在</tgt>` | 1688 |
| 13 | `<src>이제 </src><tgt>不过，</tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1314 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모여 봐요. </src><tgt>努力聚集吧。</tgt>` | 961 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | 946 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>我觉得那都是多余的。</tgt>` | 758 |

---

### Test Example 46 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1118 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉对手的</src><tgt>相手の</tgt>` | 1132 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>感情或真实</src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>意图的，</src><tgt>感情や本心、意図を察したり感じ取ったりすること、</tgt>` | 2138 |
| 5 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 567 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1793 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1433 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt>よく</tgt>` | 759 |
| 9 | `<src>这样说：“</src><tgt>よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1755 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt>聞くでしょう。「見て、</tgt>` | 1906 |
| 11 | `<src>这个人</src><tgt>「ほら、</tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1269 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>说谎了。</src><tgt>この人は嘘をついているよ」とか、</tgt>` | 2149 |
| 13 | `<src>他的眼睛</src><tgt>また嘘をついている。目が</tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1279 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt>彼の目はすべてを物語っている。</tgt>` | 943 |
| 15 | `<src><\|wait\|></src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 777 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 676 |
| 17 | `<src><\|wait\|></src><tgt>つまり…</tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 639 |

---

### Test Example 47 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1161 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>This is, you know,</tgt>` | 1285 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>というやつがあって、</src><tgt><\|wait\|></tgt>` | 995 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルパイソン</src><tgt>a visual development environment. It's</tgt>` | 1484 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1122 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt>a visual Python development environment.</tgt>` | 1855 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルン</src><tgt><\|wait\|></tgt>` | 1665 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとそれは</src><tgt>The reason is that you write a flow graph in Visual, and then</tgt>` | 1646 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコード、そっから生成される</src><tgt><\|wait\|></tgt>` | 830 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつそれが</src><tgt>Python code is generated from it. That's what</tgt>` | 2812 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1954 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>is executed, which performs signal processing.</tgt>` | 1308 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことに</src><tgt><\|wait\|></tgt>` | 996 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているからですね。</src><tgt>That's why it's set up that way.</tgt>` | 1102 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 618 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay,</tgt>` | 633 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>상승 하는 </src><tgt>The stock index is now rising,</tgt>` | 1172 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1066 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt>so these large- cap stocks</tgt>` | 1484 |
| 5 | `<src>큰 폭의 </src><tgt>these large- cap stocks</tgt>` | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | 1088 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>상승 을 하겠지만 </src><tgt>will also see a significant increase,</tgt>` | 1955 |
| 7 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1612 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 </src><tgt>but first,</tgt>` | 974 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>들이 </src><tgt><\|wait\|></tgt>` | 1231 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt>these light- cap stocks will first</tgt>` | 2305 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 </src><tgt><\|wait\|></tgt>` | 891 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 </src><tgt>lead the market's movement.</tgt>` | 2150 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요식초기 </src><tgt><\|wait\|></tgt>` | 1455 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt>So, always keep an eye on light- cap stocks early on.</tgt>` | 1452 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 </src><tgt><\|wait\|></tgt>` | 744 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>You'll need to watch them with your own eyes.</tgt>` | 746 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 801 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>これについて、多くの人が</tgt>` | 1209 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1135 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 </src><tgt>分析をしています。ここで</tgt>` | 1184 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자 에 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1496 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>このロクジャの分析を見ると、ソニーが</tgt>` | 2061 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이오 6K </src><tgt><\|wait\|></tgt>` | 1716 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>to FPD 파이 프를 </src><tgt>EOS 6KtoFPDパイプを</tgt>` | 2134 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128bit로 </src><tgt><\|wait\|></tgt>` | 2648 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>나충업스 로 보인 다. </src><tgt>128bitに最適化しているようです。</tgt>` | 1952 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 </src><tgt><\|wait\|></tgt>` | 990 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>시리즈, </src><tgt>Xboxシリーズ、</tgt>` | 1210 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 792 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt>XboxにもないInfinityCache、</tgt>` | 968 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L시가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 690 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>LSiもありません。</tgt>` | 331 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1148 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1231 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt>自分自身で「基準」とは何かを定義することです。</tgt>` | 1812 |
| 5 | `<src>absolutely correct, </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 886 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>その通りです。</tgt>` | 1779 |
| 7 | `<src>is is that </src><tgt>しかし現実には、</tgt>` | `<src>But the reality is that </src><tgt><\|wait\|></tgt>` | 1721 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>しかし、現実には、私たちが</tgt>` | 1927 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>on the block, and because </src><tgt><\|wait\|></tgt>` | 886 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>新しい波に乗っているから、基準が</tgt>` | 2402 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1823 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前に変わってしまったため、</tgt>` | 1331 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1125 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our own standard </src><tgt>私たちは自分たちの基準に</tgt>` | 986 |
| 15 | `<src>everything at this point is being </src><tgt>より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 727 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher </src><tgt>応えなければならないのです。なぜなら、今の状況では、</tgt>` | 814 |

---

### Test Example 51 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1018 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>ですから、もちろん</tgt>` | 878 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1401 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースもあります。Aという人と</tgt>` | 1247 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1432 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 컨설턴트예요. </src><tgt>Bという人がお互いにコンサルタントです。</tgt>` | 2048 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이게 컨설턴트여야 </src><tgt><\|wait\|></tgt>` | 1891 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>되고 A라는 </src><tgt>コンサルタントでなければならないし、</tgt>` | 2041 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 1796 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aという人が悪意のあるコードを</tgt>` | 1411 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1929 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>B라는 사람 이 </src><tgt>与えたとき、Bという人が</tgt>` | 1411 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 791 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크로스 사이트 스키트에서 </src><tgt>実際にクロスサイトスクリプティングで</tgt>` | 1225 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>이 X 파일까지 </src><tgt><\|wait\|></tgt>` | 695 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까 </src><tgt>感染して、Xファイルまで感染してしまうのか、</tgt>` | 560 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all of the </src><tgt><\|wait\|></tgt>` | 893 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>short-lived </src><tgt>단명하는</tgt>` | 1044 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>decisions, </src><tgt><\|wait\|></tgt>` | 1144 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>but then </src><tgt>결정들은 모두</tgt>` | 1173 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>we should </src><tgt><\|wait\|></tgt>` | 1383 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>forgive each other </src><tgt>용서해야 합니다.</tgt>` | 1525 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>in love. </src><tgt><\|wait\|></tgt>` | 1123 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src>我们也</src><tgt>사랑 안에서 서로를 용서합시다.</tgt>` | 1463 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>同时</src><tgt><\|wait\|></tgt>` | 1680 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>进入恨，</src><tgt>동시에 증오도</tgt>` | 1453 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | 1708 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>他是在</src><tgt>들입니다. 아침에 그는</tgt>` | 2045 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上。</src><tgt><\|wait\|></tgt>` | 1100 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>他就变成恨。</src><tgt>밤이 되면 증오로 변합니다.</tgt>` | 1190 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那个</src><tgt><\|wait\|></tgt>` | 897 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>钟摆。</src><tgt>그 시계추가 바로 그것입니다.</tgt>` | 778 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt><\|wait\|></tgt>` | 644 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>一动。</src><tgt>계속 움직입니다.</tgt>` | 500 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>also, you will not </src><tgt>另外，</tgt>` | 1115 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1195 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>media objects </src><tgt>你将无法移动媒体对象，</tgt>` | 1271 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between </src><tgt><\|wait\|></tgt>` | 1291 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>the resources </src><tgt>在资源之间</tgt>` | 1420 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though, </src><tgt><\|wait\|></tgt>` | 845 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>if you get into the </src><tgt>移动，但如果你进入</tgt>` | 1718 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation where you </src><tgt><\|wait\|></tgt>` | 1773 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt>情况，发现你已经</tgt>` | 1455 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1684 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular </src><tgt>将错误的媒体文件</tgt>` | 1846 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, we'll do our best </src><tgt><\|wait\|></tgt>` | 1123 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>to let us know, </src><tgt>添加到了某个资源中，我们会尽力通知你们，</tgt>` | 1499 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but we can see about </src><tgt><\|wait\|></tgt>` | 899 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files </src><tgt>但我们能看到</tgt>` | 672 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure to get back up </src><tgt><\|wait\|></tgt>` | 745 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>移动这些媒体文件并确保它们能正常工作。</tgt>` | 591 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1347 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt>最初の数キロは</tgt>` | 1155 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1095 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt>少し間違っていました。</tgt>` | 1136 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of </src><tgt>AHRフィールドの</tgt>` | 1484 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>critical importance </src><tgt><\|wait\|></tgt>` | 1004 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt>重要性について、</tgt>` | 1365 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant </src><tgt><\|wait\|></tgt>` | 1768 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>databases, which is obviously </src><tgt>バリアントデータベースとの比較についてです。これは明らかに</tgt>` | 1152 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 2127 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt>私が好きな分野の一つです。</tgt>` | 1843 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1158 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt>もし、</tgt>` | 1211 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these </src><tgt><\|wait\|></tgt>` | 992 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>これらのデータソースに含めるべきフィールドについて合意できなければ、</tgt>` | 900 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 676 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt>そこから引き出すものはないですよね？</tgt>` | 579 |
| 19 | `<src><\|wait\|></src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 394 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1178 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 869 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt>有意义的个人权利，</tgt>` | 1185 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 978 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt>最高法院</tgt>` | 515 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. And I don't know </src><tgt><\|wait\|></tgt>` | 1572 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt>是最后出现的，而不是引领者。我不知道法院是否想</tgt>` | 2424 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1314 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt>成为</tgt>` | 1710 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 820 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt>社会变革的先锋。如今。</tgt>` | 2438 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1847 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt>但他们更倾向于</tgt>` | 1075 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1174 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt>反映已经形成的共识，</tgt>` | 934 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 599 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt>所以。</tgt>` | 569 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 502 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt>你有一些联邦法官</tgt>` | 565 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 449 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>……</tgt>` | 334 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 930 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼はイエスを</tgt>` | 1240 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry, </src><tgt><\|wait\|></tgt>` | 954 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>he knows that </src><tgt>飢えていることを知っている。そして、</tgt>` | 1317 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's been told </src><tgt><\|wait\|></tgt>` | 1334 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>before in the wilderness </src><tgt>彼は荒野で</tgt>` | 1858 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry, </src><tgt><\|wait\|></tgt>` | 1881 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>and so he says to </src><tgt>40日間飢えていたことを知っている。だから彼は</tgt>` | 2229 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 2581 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it </src><tgt>イエスに言ったのだ。もしあなたが神の子なら、それを証明してみせなさい。</tgt>` | 2021 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>by turn these </src><tgt><\|wait\|></tgt>` | 922 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>stones to bread, </src><tgt>これらの石をパンに変えてみせなさい。</tgt>` | 1563 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and how did he </src><tgt><\|wait\|></tgt>` | 957 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>just deal with that </src><tgt>彼はどうやって</tgt>` | 750 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 660 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>Man, </src><tgt>その誘惑にどう対処したのか？いや、</tgt>` | 531 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 424 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>ヨナタンはパンで導いた。一人で。</tgt>` | 443 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1024 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼게요.</tgt>` | 1289 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>图片</src><tgt><\|wait\|></tgt>` | 953 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>的部分呢，</src><tgt>사진 부분은</tgt>` | 1177 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1430 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>客厅的部分，</src><tgt>손님용 홀이 보입니다.</tgt>` | 1799 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1117 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>都是属于</src><tgt>보통 손님용 홀은</tgt>` | 1088 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1735 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>在休息的地方，</src><tgt>휴식 공간에</tgt>` | 1388 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1690 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分，</src><tgt>두 번째 부분은 신체 부분입니다.</tgt>` | 1908 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它反映的是</src><tgt><\|wait\|></tgt>` | 960 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给</src><tgt>이 부분은</tgt>` | 1219 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 826 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好好地做</src><tgt>스스로</tgt>` | 777 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>一下来休息，</src><tgt><\|wait\|></tgt>` | 674 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们可以看到</src><tgt>잠시 쉬면서</tgt>` | 430 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是双人的人的嘛。</src><tgt><\|wait\|></tgt>` | 579 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt>쉴 수 있는 공간을 보여줍니다. 자,</tgt>` | 536 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以也是说。</src><tgt><\|wait\|></tgt>` | 303 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 824 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare. </src><tgt>この人々は完全に稀です。</tgt>` | 1203 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1098 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up </src><tgt>そして、彼らはしばしば</tgt>` | 1278 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1325 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>世界を完全に革命するよう現れます。</tgt>` | 2027 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1615 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>is something </src><tgt>その個性は、</tgt>` | 1420 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>that have a contradiction. </src><tgt><\|wait\|></tgt>` | 934 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾を抱えています。</tgt>` | 2481 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 647 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的である一方で、</tgt>` | 2124 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1344 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 1053 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 764 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>it gets </src><tgt>そして、</tgt>` | 527 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>straight to the point. </src><tgt><\|wait\|></tgt>` | 658 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>要点はストレートです。彼らはまた、</tgt>` | 607 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 427 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, </src><tgt>悪魔の代弁者になるのも大好きです。</tgt>` | 500 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 290 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることは決してありません。</tgt>` | 369 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E. </src><tgt><\|wait\|></tgt>` | 320 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>N. </src><tgt>E.N.</tgt>` | 333 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>T. P. Standfor. </src><tgt><\|wait\|></tgt>` | 310 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1032 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>경무를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1512 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>맹병리 후보 를 </src><tgt><\|wait\|></tgt>` | 713 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt>said he was running for the Minister of National Defense</tgt>` | 1681 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 에 당술을 </src><tgt><\|wait\|></tgt>` | 967 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>to reject the appointment of the previous candidate, and to reject the appointment of the candidate</tgt>` | 2575 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1245 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>he was quite brazen about it, but now</tgt>` | 2019 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2121 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정은 을 </src><tgt>Yoon Suk- yeol is</tgt>` | 1027 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제간 순간 </src><tgt><\|wait\|></tgt>` | 1921 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석 은 들은 해놓고 </src><tgt>now openly criticizing Kim Jong- un.</tgt>` | 1527 |
| 13 | `<src><\|wait\|></src><tgt>Lee Jun -seok</tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 903 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 </src><tgt>He has already made his move, and he is</tgt>` | 970 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 떡기를 </src><tgt><\|wait\|></tgt>` | 842 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt>ready to attack Yoon Suk- yeol.</tgt>` | 471 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 401 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>He is determined to</tgt>` | 456 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 370 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt>take action.</tgt>` | 288 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 성상급건. </src><tgt><\|wait\|></tgt>` | 326 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt>Lee Jun- seok, a former presidential candidate.</tgt>` | 336 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 242 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 얼마나 </src><tgt>How much the Democratic Party</tgt>` | 375 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 342 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今作って</src><tgt>Well, I'm making this right after dinner.</tgt>` | 1193 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>みたいなの</src><tgt><\|wait\|></tgt>` | 1146 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>でここのね</src><tgt>So, this one here,</tgt>` | 1282 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>フォールボスノンホテル</src><tgt><\|wait\|></tgt>` | 1372 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>も朝食が</src><tgt>the breakfast at the Four Seasons Hotel</tgt>` | 1890 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1423 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt>is a place where you can have breakfast.</tgt>` | 820 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1722 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt>So, going forward,</tgt>` | 1678 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1459 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいな</src><tgt>I'd like to stay here at the Goldston Hotel.</tgt>` | 2244 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>っていう方はですね</src><tgt><\|wait\|></tgt>` | 1344 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt>If you're considering it,</tgt>` | 1051 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>thinking about staying here in the future,</tgt>` | `<src>見てまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 783 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt>just take a look and see if it's a good fit.</tgt>` | 957 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います</src><tgt><\|wait\|></tgt>` | 278 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt>I think it's a good option.</tgt>` | 553 |
| 19 | `<src>駅ももう</src><tgt>From this hotel,</tgt>` | `<src>新三駅も</src><tgt><\|wait\|></tgt>` | 439 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>You can walk to Shin- San Station</tgt>` | 444 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本かかるか</src><tgt><\|wait\|></tgt>` | 303 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんでないか</src><tgt>in about a minute or so.</tgt>` | 381 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 342 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地ねまあホテル</src><tgt>The location is pretty good,</tgt>` | 431 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 322 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>So if you're interested,</tgt>` | 212 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 190 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください</src><tgt>please give it some thought.</tgt>` | 185 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね</src><tgt><\|wait\|></tgt>` | 198 |
