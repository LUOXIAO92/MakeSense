# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9977
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9791
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.2467
  - SRC_WAIT_TOTAL: 150
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 418
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 140
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 309
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1366.9390
  - PROCESS_TIME_MS_P50: 1363.6070
  - PROCESS_TIME_MS_P95: 2169.8210
  - PROCESS_TIME_MS_MAX: 12958.8460

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1168 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>在宿舍里</src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>这个优生院很大？</src><tgt>Why is the dormitory so big?</tgt>` | 1113 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1474 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那</src><tgt><\|wait\|></tgt>` | 1253 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt>Then I'm on vacation,</tgt>` | 1257 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人，</src><tgt><\|wait\|></tgt>` | 643 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1741 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>感觉</src><tgt>and I'm with Tao Ren,</tgt>` | 1637 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 1486 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和陶人。</src><tgt><\|wait\|></tgt>` | 860 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 784 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 834 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>村中まだ</src><tgt>从一开始，村里</tgt>` | 1247 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1414 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1448 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>こう密告、</src><tgt>还有一年级，所以当时就</tgt>` | 1395 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1430 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数していった</src><tgt><\|wait\|></tgt>` | 1655 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>から</src><tgt>密告、选举，</tgt>` | 1578 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>10年経っても</src><tgt><\|wait\|></tgt>` | 915 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>対数だ。</src><tgt><\|wait\|></tgt>` | 1875 |

---

### Test Example 3 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 828 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Apple, </src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축복 받히고 </src><tgt>I am blessed by Apple,</tgt>` | 1064 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1536 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1271 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보호 육인 </src><tgt>a protector of my own,</tgt>` | 1330 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르노아 </src><tgt><\|wait\|></tgt>` | 610 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1668 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한성 과 </src><tgt>Herno Park and Park Han- seong,</tgt>` | 2143 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들인 </src><tgt><\|wait\|></tgt>` | 1445 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1904 |

---

### Test Example 4 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要做</src><tgt><\|wait\|></tgt>` | 1249 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>的是，</src><tgt><\|wait\|></tgt>` | 786 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src>用我们身身</src><tgt>Parents need to do their part by</tgt>` | 1501 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1123 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>的那爱交水，</src><tgt><\|wait\|></tgt>` | 1579 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十分</src><tgt>sharing our love and water,</tgt>` | 1315 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>可以做</src><tgt><\|wait\|></tgt>` | 1521 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心里影响，</src><tgt><\|wait\|></tgt>` | 1678 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src>给内心</src><tgt>and influencing our children's hearts.</tgt>` | 1713 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>等他</src><tgt><\|wait\|></tgt>` | 782 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 1842 |

---

### Test Example 5 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气鼠，</src><tgt><\|wait\|></tgt>` | 1124 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的。</src><tgt><\|wait\|></tgt>` | 847 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>但是</src><tgt>「気鼠」は簡単です。しかし、</tgt>` | 1747 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个</src><tgt><\|wait\|></tgt>` | 904 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导，</src><tgt><\|wait\|></tgt>` | 1439 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如</src><tgt>師匠の指導が一つあるだけです。</tgt>` | 1418 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>除于中天，</src><tgt><\|wait\|></tgt>` | 1951 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1359 |
| 9 | `<src>虚阿凡</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>中天以外は反転させる必要があります。</tgt>` | 1989 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 1025 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>师傅，</src><tgt><\|wait\|></tgt>` | 1359 |

---

### Test Example 6 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后</src><tgt><\|wait\|></tgt>` | 1153 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 787 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>内部的冶炼轻</src><tgt>砂を洗った後、内部の冶錬軽</tgt>` | 2127 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | 767 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后就</src><tgt><\|wait\|></tgt>` | 1300 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>停留在</src><tgt>エネルギーも衰弱して、</tgt>` | 1338 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1627 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 1682 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>运行状态。</src><tgt>比較的低エネルギーな稼働状態に留まってしまうのです。</tgt>` | 2150 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1715 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>逆流状态。</src><tgt><\|wait\|></tgt>` | 610 |

---

### Test Example 7 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1393 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>식성들은 </src><tgt><\|wait\|></tgt>` | 748 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt>Those with the right disposition in the auspicious positions</tgt>` | 1753 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1034 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1337 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt>actually weren't highly intelligent. They were</tgt>` | 1718 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>식성들이 </src><tgt><\|wait\|></tgt>` | 1853 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>있었기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 1678 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt>just randomly selected.</tgt>` | 1479 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1766 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐 던 교사 들은 </src><tgt><\|wait\|></tgt>` | 818 |

---

### Test Example 8 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 870 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>산줄에 죽여달라 </src><tgt><\|wait\|></tgt>` | 1037 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>제가 죽고 내가 </src><tgt>I'd rather be killed by another mountain range.</tgt>` | 2077 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔어도 </src><tgt><\|wait\|></tgt>` | 799 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜이 </src><tgt><\|wait\|></tgt>` | 1290 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>죽여달라 </src><tgt>Even if I came here to kill you,</tgt>` | 1613 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>계자 아니야 내가 </src><tgt><\|wait\|></tgt>` | 2070 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt><\|wait\|></tgt>` | 1267 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>안 듣고 있는 줄 알았느냐 </src><tgt>you wouldn't have listened to that kind of talk,</tgt>` | 2117 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아 </src><tgt><\|wait\|></tgt>` | 1738 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1285 |

---

### Test Example 9 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 881 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 842 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>重要な研究を</tgt>` | 1099 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 1566 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1504 |
| 6 | `<src>research, </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>行いましたか？これは研究の始まりに過ぎません。</tgt>` | 1647 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 1999 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1389 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt>最も幸せな人々の10%を</tgt>` | 1836 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people that </src><tgt><\|wait\|></tgt>` | 2038 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1519 |

---

### Test Example 10 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1279 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 824 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>is repeat. </src><tgt>最后，重复一下。</tgt>` | 1255 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned and to repeat, </src><tgt><\|wait\|></tgt>` | 1326 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out you're good at </src><tgt><\|wait\|></tgt>` | 1587 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>学到了，重复一下，发现自己擅长的地方，然后多做一些。</tgt>` | 2434 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And will you not </src><tgt><\|wait\|></tgt>` | 1499 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>get to people </src><tgt><\|wait\|></tgt>` | 1276 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>around you to help you with </src><tgt>你会不会遇到身边的人，</tgt>` | 1602 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and and tell </src><tgt><\|wait\|></tgt>` | 2014 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>me next time, </src><tgt><\|wait\|></tgt>` | 1551 |

---

### Test Example 11 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 960 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src>칼 </src><tgt>Ah, I'm a</tgt>` | 1105 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 1519 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>서울 봉심이 가 </src><tgt><\|wait\|></tgt>` | 1547 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src><\|wait\|></src><tgt>Sword Saint, a Seoul Sword Saint,</tgt>` | 1420 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 2228 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1365 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>and I'm mixed with a Sword Saint. Wow, this is really</tgt>` | 2022 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행운 으로 </src><tgt><\|wait\|></tgt>` | 1899 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽입니다, 야. </src><tgt><\|wait\|></tgt>` | 1702 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 737 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>Drop into your body </src><tgt>你的身体在做什么？</tgt>` | 1687 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>where does </src><tgt><\|wait\|></tgt>` | 898 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1494 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>进入你的身体，紧张感从哪里开始？是什么？</tgt>` | 1783 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 2133 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tension in your chest? </src><tgt><\|wait\|></tgt>` | 1850 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>Or is it </src><tgt>是头部的？胸部有紧张吗？还是</tgt>` | 1308 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a lower place where you use </src><tgt><\|wait\|></tgt>` | 2035 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>thing? </src><tgt><\|wait\|></tgt>` | 1714 |

---

### Test Example 13 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this, </src><tgt><\|wait\|></tgt>` | 940 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで、</src><tgt><\|wait\|></tgt>` | 829 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src>think</src><tgt>그래서, 여기서</tgt>` | 1001 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>to use 7.8 </src><tgt><\|wait\|></tgt>` | 1606 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>gigabytes. </src><tgt><\|wait\|></tgt>` | 1318 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>で、</src><tgt>7.8기가바이트를 사용하려고 생각합니다. 그리고</tgt>` | 1478 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 582 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>ハイシーの仕組み</src><tgt><\|wait\|></tgt>` | 2099 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt>하이시의 구조는</tgt>` | 1406 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>五個、</src><tgt><\|wait\|></tgt>` | 1483 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7.8 </src><tgt><\|wait\|></tgt>` | 1738 |
| 12 | `<src>設備寺、五比</src><tgt>파생 형용사의 구조는 어근, 접미사, 어미로</tgt>` | `<src>gigabytes、</src><tgt>5개, 7.8기가바이트,</tgt>` | 841 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>で。</src><tgt><\|wait\|></tgt>` | 1933 |

---

### Test Example 14 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 1017 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 785 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>遇到问题就</src><tgt>When faced with this situation, we just</tgt>` | 1732 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 991 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1461 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>我们下了这个状况，</src><tgt>quickly report it to our supervisor, or let them know we've encountered this situation.</tgt>` | 2350 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1509 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1707 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>你無理承担，</src><tgt>Don't try to handle everything yourself or take on an unreasonable burden.</tgt>` | 1608 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>责任而已，</src><tgt><\|wait\|></tgt>` | 1867 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>所以就属下属</src><tgt><\|wait\|></tgt>` | 2210 |

---

### Test Example 15 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 너무 </src><tgt><\|wait\|></tgt>` | 1307 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인 저희 가 </src><tgt><\|wait\|></tgt>` | 677 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>해열 할 수 있지만 </src><tgt>これ、これぐらいなら私たちで熱を下げられるんですけど、</tgt>` | 2198 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1091 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 고생 </src><tgt><\|wait\|></tgt>` | 848 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>하는데 꿈일 프로 </src><tgt>本当に菩薩様も、いや、ご苦労されているのに夢のプロ</tgt>` | 2110 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보이 고 </src><tgt><\|wait\|></tgt>` | 1698 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1234 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보살 로 보이 고 있어요 </src><tgt>に見えてるんです。私だけ菩薩様に見えてるんです。</tgt>` | 2013 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>우주 가 진다 한 때 </src><tgt><\|wait\|></tgt>` | 1941 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이러는 게. </src><tgt><\|wait\|></tgt>` | 2200 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1306 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 849 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>好的。接下来，</tgt>` | 1349 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1214 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1440 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>这些例子告诉我们，</tgt>` | 1404 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1447 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1575 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>实际上</tgt>` | 1408 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 1111 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 1725 |
| 12 | `<src>this game dot scored array. </src><tgt>要使用这些值。也就是这个game.scored数组。</tgt>` | `<src>game.sort array. </src><tgt>要使用这些值。所以，这个game.sort数组。</tgt>` | 1015 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2133 |

---

### Test Example 17 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1034 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 906 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src>始めたもので</src><tgt>大概是从这里开始的，</tgt>` | 1141 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1467 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法、</src><tgt><\|wait\|></tgt>` | 1491 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src>ゴーギャン、</src><tgt>比如“五法”、“五颜”……</tgt>` | 1441 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1591 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1762 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt>还有“塞尚”、“卢纳尔”……</tgt>` | 2126 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1897 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 625 |
| 12 | `<src>中学生でも。</src><tgt>像梵高、高更、塞尚、雷诺阿他们的画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt>这些人的画，即使是乡村中学生也能</tgt>` | 2512 |

---

### Test Example 18 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1272 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>があの</src><tgt><\|wait\|></tgt>` | 780 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt>You can get T- shirts and other items.</tgt>` | 1728 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ようなものも</src><tgt><\|wait\|></tgt>` | 905 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1482 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ぜひご参加ください。</src><tgt>We have those available, so please join us.</tgt>` | 1547 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1537 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1610 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>て、</src><tgt>That's all for the contact information.</tgt>` | 1768 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>また</src><tgt><\|wait\|></tgt>` | 714 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>内側がありますので</src><tgt><\|wait\|></tgt>` | 1910 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>ご紹介お待ちください。</src><tgt>We'll be sharing more details soon, so please stay tuned.</tgt>` | 2802 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 892 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>已经正常</src><tgt><\|wait\|></tgt>` | 882 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>喉咙扁桃跳，</src><tgt>I had a normal sore throat at that time,</tgt>` | 1153 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1477 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开了当，</src><tgt><\|wait\|></tgt>` | 1246 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>提前大概有</src><tgt>so I didn't go to work. I had</tgt>` | 1505 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>三围医生来</src><tgt><\|wait\|></tgt>` | 626 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>诊断，</src><tgt><\|wait\|></tgt>` | 1866 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>以下药腿</src><tgt>a doctor come to diagnose me. I took the following medicine</tgt>` | 2474 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下剃腿，</src><tgt><\|wait\|></tgt>` | 780 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1922 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>当然都很</src><tgt>to treat my legs, and everything was fine. Of course, they were all</tgt>` | 1605 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一手打开。</src><tgt><\|wait\|></tgt>` | 1537 |

---

### Test Example 20 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1160 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>なんとちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1053 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>みたいな感じで</src><tgt>嗯，感觉距离好像有点拉开了，</tgt>` | 1811 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オーシャラーとかタタガネ</src><tgt><\|wait\|></tgt>` | 938 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>パオイですね</src><tgt><\|wait\|></tgt>` | 1359 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>海遊したい方って</src><tgt>想去海游的话，像Oceaner或者Tatamigane</tgt>` | 1790 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行き来していかが</src><tgt><\|wait\|></tgt>` | 2155 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>し</src><tgt><\|wait\|></tgt>` | 1009 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>でねで</src><tgt>这种，可以随时来来去去，</tgt>` | 1851 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>ドモンチニオとか</src><tgt><\|wait\|></tgt>` | 2009 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>セコが強いので</src><tgt><\|wait\|></tgt>` | 1398 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので</src><tgt>因为Donquignio和Sekko都很强，所以</tgt>` | 1926 |

---

### Test Example 21 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 869 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 893 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>chemical bonds also store </src><tgt>고무줄처럼 화학 결합도</tgt>` | 1728 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 995 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1492 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>에너지를 저장합니다. 그 결합이 끊어지면, 그 잠재 에너지는</tgt>` | 2432 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1384 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1520 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>열이나 빛 같은 다른 에너지 형태로 변환됩니다.</tgt>` | 1648 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 1846 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 1534 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1865 |

---

### Test Example 22 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 819 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A、Aアンデスに</src><tgt><\|wait\|></tgt>` | 975 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>いるな場面で</src><tgt>In a situation where A is in the Andes,</tgt>` | 1805 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>A制服かどうかっていうのは</src><tgt><\|wait\|></tgt>` | 1097 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>やる時に</src><tgt><\|wait\|></tgt>` | 1286 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAの</src><tgt>when you're deciding whether A should wear a uniform,</tgt>` | 1584 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ランクを調べたことであの</src><tgt><\|wait\|></tgt>` | 2139 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その制服かどうかっていうのは</src><tgt><\|wait\|></tgt>` | 1831 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>表すする制服で</src><tgt>you'd use the uniform that reflects A's rank.</tgt>` | 1620 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうこと保証する</src><tgt><\|wait\|></tgt>` | 1881 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったら使い方を</src><tgt><\|wait\|></tgt>` | 1570 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>定めました。</src><tgt>That's how we defined how to use it.</tgt>` | 1715 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 954 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Frenkel, </src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>and I am currently studying </src><tgt>제 이름은 프렌켈입니다. 현재</tgt>` | 2067 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a PhD path </src><tgt><\|wait\|></tgt>` | 662 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in finance </src><tgt><\|wait\|></tgt>` | 1386 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a B.S. in psychology. </src><tgt>금융 분야 박사 과정과 심리학 학사 학위를 전공하고 있습니다.</tgt>` | 2349 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 1381 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>you at Yale, </src><tgt><\|wait\|></tgt>` | 1373 |
| 9 | `<src><\|wait\|></src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>and in the </src><tgt>Yale에서 뵙고,</tgt>` | 1704 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 2263 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy </src><tgt><\|wait\|></tgt>` | 1671 |
| 12 | `<src>corporate consultancy. </src><tgt>밟고 있고요, 앞으로는 기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src><\|wait\|></src><tgt>앞으로 기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1869 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1131 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 894 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアが</src><tgt>이게 기어입니다. 기어가</tgt>` | 1363 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと信号が</src><tgt><\|wait\|></tgt>` | 1320 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>消えなくなってしまう</src><tgt><\|wait\|></tgt>` | 1550 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>ので、</src><tgt>풀리면 신호가 꺼지지 않기 때문에,</tgt>` | 1601 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1753 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1460 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | 1991 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついているっていうこと</src><tgt><\|wait\|></tgt>` | 1977 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1068 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>달려 있다는 거죠. 네,</tgt>` | 2000 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 850 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1277 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 916 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment </src><tgt>19차 수정헌법의 의미는</tgt>` | 1682 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 914 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1471 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to how political </src><tgt>어떻게</tgt>` | 1336 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 1629 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt><\|wait\|></tgt>` | 1730 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>United States. </src><tgt>미국에서 정치적 변화가 일어날 수 있는 길잡이로서 그 역사를 탐구하는 것입니다.</tgt>` | 2515 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1668 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1430 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of course I </src><tgt>물론</tgt>` | 1537 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>married. </src><tgt><\|wait\|></tgt>` | 922 |

---

### Test Example 26 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이루 어떨 때는 </src><tgt><\|wait\|></tgt>` | 898 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>거진 100일 중에 </src><tgt>Sometimes, vanadium is</tgt>` | 1893 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>거진 60% </src><tgt><\|wait\|></tgt>` | 831 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>이상 70일 정도 </src><tgt><\|wait\|></tgt>` | 1393 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>보긴장이 </src><tgt>about 60% to 70% of the time.</tgt>` | 1697 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1826 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1909 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이기적이야 </src><tgt>It's obviously a mineral.</tgt>` | 1362 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>절도 왜 </src><tgt><\|wait\|></tgt>` | 1867 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠 이제 </src><tgt><\|wait\|></tgt>` | 1112 |
| 12 | `<src>그거 에다가 </src><tgt>you could call them diabetes minerals. And on top of that,</tgt>` | `<src>그 후에다가 </src><tgt>But why is it that way?</tgt>` | 2005 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아멘. </src><tgt><\|wait\|></tgt>` | 938 |

---

### Test Example 27 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 870 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到二classList</src><tgt><\|wait\|></tgt>` | 910 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>啊，</src><tgt>2つ目は、二つのクラスに</tgt>` | 1244 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>还服务在一级</src><tgt><\|wait\|></tgt>` | 1411 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1503 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>一线平安的大牛们。</src><tgt>サービスを提供している、第一線の平安の牛たちです。</tgt>` | 1668 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1749 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做维信</src><tgt><\|wait\|></tgt>` | 1607 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>沟通好事期间，</src><tgt>例えば、維信のコミュニケーションを始めた時期に、</tgt>` | 1905 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1786 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维信好平分</src><tgt><\|wait\|></tgt>` | 684 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的辛膀，</src><tgt>維信の辛膀を平らにするようなことが、</tgt>` | 2584 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1180 |

---

### Test Example 28 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1259 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这</src><tgt><\|wait\|></tgt>` | 635 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>这个罗马呢，</src><tgt>皆さんにお伝えしたいのは、このローマでは、</tgt>` | 1557 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 1110 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>造成了所以呢，</src><tgt><\|wait\|></tgt>` | 1548 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>それが原因で、今</tgt>` | 1357 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1613 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt><\|wait\|></tgt>` | 1674 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>跟风险</src><tgt>直面している危機やリスクは、</tgt>` | 1735 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 810 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>事业就</src><tgt><\|wait\|></tgt>` | 1713 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src>眼变出来</src><tgt>あなたのキャリアが</tgt>` | 1364 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因此会建议</src><tgt><\|wait\|></tgt>` | 1671 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢，</src><tgt><\|wait\|></tgt>` | 1270 |

---

### Test Example 29 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果在女高中</src><tgt><\|wait\|></tgt>` | 933 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>生与长相</src><tgt><\|wait\|></tgt>` | 889 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>古怪的人之间，</src><tgt>If you're in a female high school and you're with someone who's a bit eccentric,</tgt>` | 2516 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有着某种</src><tgt><\|wait\|></tgt>` | 1509 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>典型性，</src><tgt><\|wait\|></tgt>` | 1358 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>难道会是</src><tgt>there's a certain type of person you'd expect. Could it be</tgt>` | 2671 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1274 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天颞叶</src><tgt><\|wait\|></tgt>` | 1549 |
| 9 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src>开始的？</src><tgt>the kind that starts in the temporal lobe?</tgt>` | 2244 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1525 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1518 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>喜欢甜，</src><tgt>Yang Zisi likes sweets,</tgt>` | 1310 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>砸到了一个</src><tgt><\|wait\|></tgt>` | 893 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>钱包，</src><tgt><\|wait\|></tgt>` | 786 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>那如果你</src><tgt>財布にぶつけてしまったら、</tgt>` | 1500 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>拿到了钱包之后，</src><tgt><\|wait\|></tgt>` | 1135 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1527 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src>就要先</src><tgt>必ず</tgt>` | 1306 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt><\|wait\|></tgt>` | 1457 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着哎，那我</src><tgt><\|wait\|></tgt>` | 1665 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src>再去操作</src><tgt>しっかり守ってください。そうして「あ、</tgt>` | 1851 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦，</src><tgt><\|wait\|></tgt>` | 844 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1771 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>それから操作しよう」なんて考えないでください。なぜそんなことを言うのかというと、</tgt>` | 2166 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1176 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1218 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 852 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 879 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src>一个</src><tgt>이 부분은</tgt>` | 999 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>带吊耳的人，但是</src><tgt><\|wait\|></tgt>` | 1608 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1588 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src>这通场</src><tgt>귀걸이가 달린 사람을 보여주는데, 이건 역방향이에요.</tgt>` | 1867 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>有没有这样的一个状况</src><tgt><\|wait\|></tgt>` | 2087 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>需要去特别</src><tgt><\|wait\|></tgt>` | 1283 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>注意的是</src><tgt>이런 상황을 특별히 주의해야 할까요?</tgt>` | 1589 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>它能不能</src><tgt><\|wait\|></tgt>` | 1751 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到于它</src><tgt><\|wait\|></tgt>` | 655 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>吊不到于</src><tgt>그것이</tgt>` | 2012 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>于一个易事</src><tgt><\|wait\|></tgt>` | 1087 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt><\|wait\|></tgt>` | 1092 |

---

### Test Example 32 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There </src><tgt><\|wait\|></tgt>` | 733 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事。</tgt>` | 1015 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>was such interests before. </src><tgt><\|wait\|></tgt>` | 1598 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1436 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>Net future TC. </src><tgt>以前也有这样的兴趣。NetfutureTC。</tgt>` | 1306 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, </src><tgt><\|wait\|></tgt>` | 558 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>so this is just </src><tgt><\|wait\|></tgt>` | 1906 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>one another place. </src><tgt>嗯，所以这只是另一个地方。</tgt>` | 1916 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>Look at </src><tgt><\|wait\|></tgt>` | 1287 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1736 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src>what </src><tgt>看看</tgt>` | 594 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1837 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>would like to bug report should be </src><tgt><\|wait\|></tgt>` | 1431 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>available. </src><tgt>开发者或工程师想提交Bug报告的地方。</tgt>` | 1214 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1179 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 746 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>あるいは、何かを書きたい場合、</tgt>` | 1748 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 920 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1445 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know </src><tgt>テキストを書くとき、</tgt>` | 1607 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1757 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like, oh, </src><tgt><\|wait\|></tgt>` | 2207 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt>単語のスペルが全くわからないことに気づくんです。「あ、この単語は</tgt>` | 2010 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with </src><tgt><\|wait\|></tgt>` | 1474 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a double P, </src><tgt><\|wait\|></tgt>` | 2096 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double L. I don't know </src><tgt>PPで始まる、LLで始まる…」ってなるわけです。でも、</tgt>` | 1899 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 713 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 907 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개 가 증호 모드에서 </src><tgt><\|wait\|></tgt>` | 1098 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>100m로 </src><tgt>そのうち150個は、防御モードで100mに</tgt>` | 2226 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>4주자 관계 업들이 </src><tgt><\|wait\|></tgt>` | 1526 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1398 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くありました。一般的には、</tgt>` | 1574 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작업 팩들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1808 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해업을 </src><tgt><\|wait\|></tgt>` | 1859 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>끼어 곱게 되는데 </src><tgt>作業パックは成長したり、あるいはハーブを組み合わせて増やすものもありますが、</tgt>` | 2121 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>이거 는 </src><tgt><\|wait\|></tgt>` | 683 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성기 없던 것은 성장 도 </src><tgt><\|wait\|></tgt>` | 2479 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>패업도 하지 않을 현상 들을 </src><tgt>これらは、成長も増殖もしない現象を</tgt>` | 1533 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1042 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 832 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>而HTML</src><tgt><\|wait\|></tgt>` | 840 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src>이라고 하는 </src><tgt>而HTML</tgt>` | 1026 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 도 </src><tgt><\|wait\|></tgt>` | 1579 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1500 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>사람 도 </src><tgt>这个计算机也是可以理解的，</tgt>` | 1394 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1520 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1783 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>문법 에 </src><tgt>人类也是可以理解的，</tgt>` | 1706 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1049 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1728 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>就像语言的语法一样，我们现在需要编写代码，</tgt>` | 2074 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1159 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1184 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要一个程序来编写这些代码。</tgt>` | 1040 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1328 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 750 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>needs to get </src><tgt>これから始める人たちは、</tgt>` | 1436 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1107 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>like ten of them </src><tgt><\|wait\|></tgt>` | 1556 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt>本当に重要な</tgt>` | 1363 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1629 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to </src><tgt><\|wait\|></tgt>` | 1644 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>10個の</tgt>` | 1902 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one </src><tgt><\|wait\|></tgt>` | 930 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 1636 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video. </src><tgt>動画があります。この動画の後に、1分程度の動画を1本作ります。</tgt>` | 2810 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage </src><tgt><\|wait\|></tgt>` | 971 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>each one </src><tgt><\|wait\|></tgt>` | 789 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, </src><tgt>それぞれの動画では、もう少し詳しく</tgt>` | 1131 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1154 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 830 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>还不错的，但是</src><tgt>金運については、今月はかなり良いと言えるでしょう。ただ、</tgt>` | 2213 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较稳定</src><tgt><\|wait\|></tgt>` | 679 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>的部分，也就是</src><tgt><\|wait\|></tgt>` | 1175 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>在事业方面</src><tgt>安定している部分もあります。つまり、仕事面では</tgt>` | 1647 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长所带来的</src><tgt><\|wait\|></tgt>` | 2040 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>流动收益的</src><tgt><\|wait\|></tgt>` | 1255 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>提升。如果</src><tgt>業績向上による収入の増加です。もし</tgt>` | 1855 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>在投资理财方面，</src><tgt><\|wait\|></tgt>` | 1957 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1049 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>投資・資産運用面では、今月も悪くないですが、</tgt>` | 2255 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对整体来说</src><tgt><\|wait\|></tgt>` | 1295 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了</src><tgt><\|wait\|></tgt>` | 1017 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>一点。</src><tgt>全体的に見ると少し弱めです。</tgt>` | 646 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10</src><tgt><\|wait\|></tgt>` | 967 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt><\|wait\|></tgt>` | 907 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですとね、</src><tgt>比如10手、12手的话，</tgt>` | 1461 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく10秒で</src><tgt><\|wait\|></tgt>` | 1224 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>1秒に</src><tgt>大概10秒内，</tgt>` | 1416 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1787 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>スピンとかね、</src><tgt><\|wait\|></tgt>` | 1668 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>ね。</src><tgt>1秒左右的旋转，对吧？</tgt>` | 1926 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1752 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 625 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src>12手</src><tgt>然后大概</tgt>` | 1702 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1352 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1219 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮川とかが</src><tgt>12手的话，宫川</tgt>` | 1058 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 820 |

---

### Test Example 39 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1111 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어제 보면 </src><tgt><\|wait\|></tgt>` | 904 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>가장 20대를 </src><tgt>昨天看，</tgt>` | 1097 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1508 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1497 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt>和最年轻的20岁同龄的弟弟，</tgt>` | 1727 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1995 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1346 |
| 9 | `<src><\|wait\|></src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>어 </src><tgt>也是家人一样的弟弟。所以，</tgt>` | 1688 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생 한 거다는 </src><tgt><\|wait\|></tgt>` | 1180 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1258 |
| 12 | `<src>자기 스스로 </src><tgt>比起责任感，</tgt>` | `<src>어. </src><tgt>我录制的时候，嗯，有点……</tgt>` | 1799 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>정말 </src><tgt><\|wait\|></tgt>` | 1336 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 1217 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>真的放了很多东西，</tgt>` | 1014 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>생각 했습니다. </src><tgt><\|wait\|></tgt>` | 827 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 859 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 </src><tgt><\|wait\|></tgt>` | 948 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>너희가 이방인으로 </src><tgt>あなたたちも知っているでしょう。あなたたちが異邦人として</tgt>` | 2303 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 922 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 940 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>ある偶像について語れない時、</tgt>` | 1521 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1565 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>그녀와 갔느니라. </src><tgt><\|wait\|></tgt>` | 1855 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src><\|wait\|></src><tgt>その偶像にそれそのまま行ってしまったのです。</tgt>` | 1842 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1950 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1308 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>ですから、私があなたたちに知らせるのです。</tgt>` | 2010 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1336 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 994 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | 940 |

---

### Test Example 41 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1265 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 841 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうのが出ていまして、</src><tgt>This is a visual development environment that has appeared.</tgt>` | 2086 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 803 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1191 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのも</src><tgt>It's a Visual Python development environment.</tgt>` | 1514 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルン</src><tgt><\|wait\|></tgt>` | 1908 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとそれとは</src><tgt><\|wait\|></tgt>` | 1478 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコアさんそっから生成される</src><tgt>It's because it generates from a FlowGraph Visual</tgt>` | 2069 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつそれが</src><tgt><\|wait\|></tgt>` | 1844 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1451 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>that is executed, which performs signal processing.</tgt>` | 1775 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことをしている</src><tgt><\|wait\|></tgt>` | 1252 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>からですね。</src><tgt><\|wait\|></tgt>` | 900 |
| 15 | `<src>はい。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>はい。</src><tgt>So, yes.</tgt>` | 458 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 872 |

---

### Test Example 42 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1144 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らしてやる。</src><tgt><\|wait\|></tgt>` | 937 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>俺は</src><tgt>그럼 젖게 해줄게. 나는</tgt>` | 1749 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt><\|wait\|></tgt>` | 825 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き絞みている。</src><tgt><\|wait\|></tgt>` | 1531 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>지금 꽉 쥐고 있어.</tgt>` | 1520 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1746 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えている</src><tgt><\|wait\|></tgt>` | 1559 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不烈酒、</src><tgt>이미 한계는 아득히 넘어선 불량주,</tgt>` | 2059 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1924 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1306 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船大工やってる</src><tgt>오랫동안 배를 만들던</tgt>` | 1949 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>な。</src><tgt><\|wait\|></tgt>` | 1045 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 702 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>すごい海賊船を見た</src><tgt>선장이야. 나는 이렇게 대단한 해적선을</tgt>` | 1213 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 721 |

---

### Test Example 43 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1238 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>상승 하는 </src><tgt><\|wait\|></tgt>` | 672 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인 다면 </src><tgt>If the stock index is showing an upward trend,</tgt>` | 2177 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1117 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | 826 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will also rise sharply,</tgt>` | 1620 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1695 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 </src><tgt><\|wait\|></tgt>` | 1636 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>들이 </src><tgt>but first, these light- cap stocks</tgt>` | 1821 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 2041 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 1666 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt>move first to lead the market,</tgt>` | 1561 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>역시 총이 </src><tgt><\|wait\|></tgt>` | 1252 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 866 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 </src><tgt>so you should always keep an eye on the light- cap stocks.</tgt>` | 810 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 740 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>did you </src><tgt>학력 수준. 얼마나</tgt>` | 1406 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go in your </src><tgt><\|wait\|></tgt>` | 1131 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1537 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>실제로 학업을 얼마나 마쳤나요? 고등학교를 졸업했나요?</tgt>` | 2368 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1833 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1311 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>그건 학력 수준의 한 단계입니다. 대학에 갔나요?</tgt>` | 1727 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, </src><tgt><\|wait\|></tgt>` | 1795 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>did you graduate? </src><tgt><\|wait\|></tgt>` | 1519 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of attainment. </src><tgt>그래서 졸업했나요? 그건 또 다른 학력 수준입니다.</tgt>` | 2120 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1054 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt><\|wait\|></tgt>` | 1098 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>지금까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 979 |

---

### Test Example 45 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1328 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새 머라 </src><tgt><\|wait\|></tgt>` | 848 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>目を閉じて、新しい自分になるんだ。</tgt>` | 1755 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 </src><tgt><\|wait\|></tgt>` | 919 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋던 자태 돋던 </src><tgt><\|wait\|></tgt>` | 1511 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>내 기미 움이야. </src><tgt>昔の自分、昔の姿が芽生えているんだ。</tgt>` | 1750 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 2275 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1478 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>기신이 움이야. </src><tgt>それを揺らして、一緒に遊ぼうってこと。新しい自分、新しい姿が芽生えているんだ。</tgt>` | 2709 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | 807 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 움이야. </src><tgt><\|wait\|></tgt>` | 2292 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>新しい自分、新しい姿が芽生えているんだ。それを守ってくれ、</tgt>` | 1591 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>이제 늙어 주라니까 </src><tgt><\|wait\|></tgt>` | 936 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에 </src><tgt><\|wait\|></tgt>` | 878 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>もう年を取るんだって、心に余裕を持って目を閉じて。</tgt>` | 1087 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 으면 </src><tgt><\|wait\|></tgt>` | 1410 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매입니다. </src><tgt><\|wait\|></tgt>` | 887 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>운전 을 </src><tgt>进入的话，会非常迷茫。</tgt>` | 1605 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 927 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1442 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>있고 </src><tgt>因为之前开车，现在走路，</tgt>` | 1493 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1983 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1464 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가 면 또 장려 리요. </src><tgt>去江南区的话，更是无话可说，去国外的话，更是鼓励。</tgt>` | 2638 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1502 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>신기 하네요. </src><tgt><\|wait\|></tgt>` | 1589 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>这真让人觉得不可思议。不如</tgt>` | 1783 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1070 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모여 봐요. </src><tgt><\|wait\|></tgt>` | 1001 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 다인 것 같아요. </src><tgt>努力聚集起来吧，我觉得那样更好。</tgt>` | 1049 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 366 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1187 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉对手的</src><tgt><\|wait\|></tgt>` | 926 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>感情或真实</src><tgt>相手の感情や本心、</tgt>` | 1668 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>意图的，</src><tgt><\|wait\|></tgt>` | 920 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1457 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>很多是</src><tgt>意図を察知したり感じ取ったりすることが多いです。</tgt>` | 1725 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1853 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1660 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt>よく耳にする言葉があります。</tgt>` | 1553 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1980 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1105 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>说谎了。</src><tgt>見てください、この人は嘘をついています。</tgt>` | 2037 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1264 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 594 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>彼の目はすべてを物語っています。</tgt>` | 1025 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 916 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 593 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 880 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 874 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>분석 을 해 놓았습니다. </src><tgt>これについて多くの人が分析してあります。</tgt>` | 2091 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 552 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자 에 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1576 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ここで「ロクジャ」の分析を見ると、ソニーが</tgt>` | 1681 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이오 628F </src><tgt><\|wait\|></tgt>` | 2491 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>파이 프를 </src><tgt><\|wait\|></tgt>` | 1759 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>EOS628Fファームウェアを128ビットに</tgt>` | 1500 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나충하 고서 로 포인트 한다. </src><tgt><\|wait\|></tgt>` | 1550 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 </src><tgt><\|wait\|></tgt>` | 1933 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>시리즈, </src><tgt>最適化していることがポイントです。Xboxシリーズ、</tgt>` | 1525 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1022 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt><\|wait\|></tgt>` | 1034 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L시가 여기 도 없다. </src><tgt>XboxにはないInfinityCacheやL1キャッシュもありません。</tgt>` | 1155 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 632 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 911 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt>活動、そして</tgt>` | 1136 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1475 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1608 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>自分自身で「基準」を定義することです。なぜなら、あなたは完全に正しいからです。</tgt>` | 2170 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is that </src><tgt><\|wait\|></tgt>` | 1928 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat and </src><tgt><\|wait\|></tgt>` | 1839 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, </src><tgt>しかし、現実には、私たちが新しい猫であり、ブロックである以上、</tgt>` | 1290 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have </src><tgt><\|wait\|></tgt>` | 1852 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1662 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>changed from twenty years ago, </src><tgt>基準は20年前に変わってから、</tgt>` | 1868 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1058 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our own standard </src><tgt><\|wait\|></tgt>` | 914 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>私たちは自分自身の基準に照らされています。なぜなら、今のところ、</tgt>` | 1213 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 669 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 894 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt>ですから、もちろんこのようなケースもあります。私たちは</tgt>` | 1687 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1016 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1483 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>서로 컨설턴트예요. </src><tgt>AさんとBさんがお互いにコンサルタントです。</tgt>` | 1876 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이게 컨설턴트여야 </src><tgt><\|wait\|></tgt>` | 2491 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>되고 A라는 </src><tgt><\|wait\|></tgt>` | 1488 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>사람 이 </src><tgt>コンサルタントでなければなりません。Aさんは</tgt>` | 1168 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 2121 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 2030 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>B라는 사람 이 </src><tgt>悪意のあるコードを渡したとき、Bさんは</tgt>` | 1539 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 934 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스 사이트 스큐티에서 </src><tgt><\|wait\|></tgt>` | 1115 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>이 엑스파일까지 </src><tgt>実際にクロスサイトスクリプティングでこのXMLファイルまで</tgt>` | 1109 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까 </src><tgt><\|wait\|></tgt>` | 676 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 1031 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 942 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src>be able to move </src><tgt>嗯，你也不会</tgt>` | 1351 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1202 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1395 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt>在资源之间移动媒体对象，</tgt>` | 1193 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>so if </src><tgt><\|wait\|></tgt>` | 474 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the </src><tgt><\|wait\|></tgt>` | 1875 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>situation where you </src><tgt>因为</tgt>` | 1393 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1882 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 936 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular </src><tgt>你发现把错误的媒体文件</tgt>` | 1534 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, you can </src><tgt><\|wait\|></tgt>` | 1560 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>let us know, and we can see about </src><tgt><\|wait\|></tgt>` | 1736 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>moving those </src><tgt>放到了某个资源上，可以告诉我们，我们会</tgt>` | 1356 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>media files and then making sure </src><tgt><\|wait\|></tgt>` | 1029 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>you get back up </src><tgt><\|wait\|></tgt>` | 948 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt>把那些媒体文件移动回来，确保它们能正常工作。</tgt>` | 768 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all of the </src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>short-lived </src><tgt><\|wait\|></tgt>` | 738 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>decisions, </src><tgt>모든 단기적인 결정에 대해서는,</tgt>` | 1760 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but among </src><tgt><\|wait\|></tgt>` | 917 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1436 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>us, we are</src><tgt>우리 중에는</tgt>` | 1361 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>the most loving. </src><tgt><\|wait\|></tgt>` | 1640 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>We also </src><tgt><\|wait\|></tgt>` | 1657 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>tend to enter </src><tgt>가장 사랑하는 경향이 있습니다.</tgt>` | 1944 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 868 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>hidden in the midst of the storm </src><tgt><\|wait\|></tgt>` | 1663 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>of love. </src><tgt>우리는 사랑의 폭풍 속으로 숨어들기도 합니다.</tgt>` | 2143 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>Dào了晚上. </src><tgt><\|wait\|></tgt>` | 1139 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 1140 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>很那个</src><tgt>밤이 되면 그것은</tgt>` | 971 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>重白。</src><tgt><\|wait\|></tgt>` | 857 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt><\|wait\|></tgt>` | 499 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>一动。</src><tgt>매우 하얀색이 됩니다. 계속 움직입니다.</tgt>` | 715 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1113 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 669 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>is hungry, </src><tgt>ある時、彼はイエスが飢えていることを知っていました。</tgt>` | 2143 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 802 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1193 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>be in the wilderness </src><tgt>そして、</tgt>` | 1333 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days </src><tgt><\|wait\|></tgt>` | 1746 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>that he's hungry. And so he says to </src><tgt><\|wait\|></tgt>` | 2239 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus, </src><tgt>彼は40日間荒野で飢えることになることを知っていました。だからイエスに言いました。</tgt>` | 2082 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>If you're the Son of God, prove it </src><tgt><\|wait\|></tgt>` | 1667 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>by turning </src><tgt><\|wait\|></tgt>` | 1502 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>these stones to bread. </src><tgt>もしあなたが神の御子なら、この石をパンに変えてみせなさい。</tgt>` | 2249 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 844 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that </src><tgt><\|wait\|></tgt>` | 990 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>彼はその試練にどう対処したのでしょうか？</tgt>` | 1070 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 599 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan led by </src><tgt><\|wait\|></tgt>` | 385 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>right alone. </src><tgt>いやはや、ヨナタンは一人で進んだのです。</tgt>` | 553 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1461 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 789 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>最初のセクションで少し間違った場所に入ってしまって、</tgt>` | 2184 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt><\|wait\|></tgt>` | 647 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1277 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src>being of </src><tgt>AHRフィールドの</tgt>` | 1310 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>critical importance </src><tgt><\|wait\|></tgt>` | 1570 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1671 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src>variant data </src><tgt>重要性について、</tgt>` | 1682 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>bases, which is obviously </src><tgt><\|wait\|></tgt>` | 964 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>not my loves. </src><tgt><\|wait\|></tgt>` | 1821 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt>バリアントデータベースは明らかに私の好みではありません。では、</tgt>` | 1862 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1440 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1175 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>to be in these </src><tgt>これらの</tgt>` | 919 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 931 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 602 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt>データソースに含めるべきフィールドについて合意できなければ、それからデータを取得することはできませんよね？</tgt>` | 875 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 473 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1156 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 891 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>right, and </src><tgt>有意义的个人权利，</tgt>` | 1047 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>the Supreme Court </src><tgt><\|wait\|></tgt>` | 1572 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1274 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't know </src><tgt>最高法院是最后出现的，而不是引领者。我不知道</tgt>` | 1661 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1621 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the the Van </src><tgt><\|wait\|></tgt>` | 1733 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>Guard of </src><tgt>法院是否想成为</tgt>` | 1664 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>Social Change, </src><tgt><\|wait\|></tgt>` | 869 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 1919 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>But they rather </src><tgt>社会变革的“范德堡守卫者”。但他们更倾向于</tgt>` | 2802 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect the </src><tgt><\|wait\|></tgt>` | 943 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>consensus </src><tgt><\|wait\|></tgt>` | 779 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>that's already </src><tgt>反映已经达成的共识，</tgt>` | 1070 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 839 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 370 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src>You have </src><tgt>而这个共识已经浮现出来。</tgt>` | 661 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 442 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 393 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who. </src><tgt>你有一些联邦法官，他们……</tgt>` | 497 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 935 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>图片</src><tgt>그럼 사진을 한번 볼게요. 사진은</tgt>` | 1681 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>的背后呢，</src><tgt><\|wait\|></tgt>` | 982 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1474 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>客订的部分。</src><tgt>뒷면을 보면 ' 고객 주문 ' 이라고 적혀 있어요.</tgt>` | 1746 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客订一般</src><tgt><\|wait\|></tgt>` | 2100 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1248 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src>我们</src><tgt>보통 ' 고객 주문 ' 은</tgt>` | 1698 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在修习的地方，</src><tgt><\|wait\|></tgt>` | 1921 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1062 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src>这是身体的部分。</src><tgt>수련하는 곳에 해당하니까, 이건 신체 부분이에요.</tgt>` | 2248 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它反映的是</src><tgt><\|wait\|></tgt>` | 1257 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 526 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>自己一点时间</src><tgt>이건</tgt>` | 874 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地做</src><tgt><\|wait\|></tgt>` | 923 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>下来休息，</src><tgt><\|wait\|></tgt>` | 412 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们可以看到</src><tgt>잠시 시간을 내서 잘 쉬어야 한다는 뜻이에요. 그리고</tgt>` | 603 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是双五一人的嘛。</src><tgt><\|wait\|></tgt>` | 494 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 261 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>여기 ' 쌍오일인 ' 이라고 되어 있죠. 자, 그래서</tgt>` | 545 |

---

### Test Example 57 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 963 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 828 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>And they often </src><tgt>これらの人々は完全に稀です。そして、彼らはしばしば</tgt>` | 2185 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 657 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1307 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>世界を完全に革命しようと現れます。</tgt>` | 1582 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1630 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>is something </src><tgt><\|wait\|></tgt>` | 1464 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>that have a contradiction. </src><tgt>その性格は矛盾を抱えています。</tgt>` | 2040 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1666 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 696 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的である一方で、</tgt>` | 2047 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1068 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 1211 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src>And like to </src><tgt>無意味な会話を嫌います。そして、</tgt>` | 1112 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt><\|wait\|></tgt>` | 901 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 451 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>要点をまっすぐ言うのが好きです。また、</tgt>` | 698 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 405 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>the devil's advocate, </src><tgt><\|wait\|></tgt>` | 413 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and never shy away </src><tgt>悪魔の代弁者になるのも好きです。そして、</tgt>` | 537 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 308 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 276 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src>E and C P </src><tgt>議論を避けることは決してありません。</tgt>` | 356 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for. </src><tgt><\|wait\|></tgt>` | 282 |

---

### Test Example 58 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 693 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 870 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活的一个</src><tgt>제 삶의</tgt>` | 969 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>轨道哈，</src><tgt><\|wait\|></tgt>` | 1359 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够好好的</src><tgt><\|wait\|></tgt>` | 940 |
| 6 | `<src>在他下班的时候，</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>扎根的时候，</src><tgt>궤도로 돌아가서 뿌리내릴 수 있도록, 그럴 때</tgt>` | 1856 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日谈</src><tgt><\|wait\|></tgt>` | 636 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单` | 12959 |
| 9 | `<src><\|wait\|></src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>的这单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单单` | 4452 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>我暂时背动这个</src><tgt>제가 이 단계를</tgt>` | 349 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>小小的愿望哈，</src><tgt><\|wait\|></tgt>` | 288 |
| 12 | `<src>哈。</src><tgt>그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 310 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 893 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt>I'd like to make something after a meal.</tgt>` | 1156 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1473 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのねフォールボス</src><tgt><\|wait\|></tgt>` | 1275 |
| 6 | `<src>も</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ホテルも朝食が</src><tgt>So, the breakfast at this Four Boss Hotel</tgt>` | 1496 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 614 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になっている</src><tgt><\|wait\|></tgt>` | 1618 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>is supposed to be a place where you can eat breakfast,</tgt>` | 2356 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1077 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここ五つフォールボス</src><tgt><\|wait\|></tgt>` | 1901 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>ホテル泊まってみたい</src><tgt>so I'd like to stay at this Four Boss Hotel in the future.</tgt>` | 1623 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>な方はですね</src><tgt><\|wait\|></tgt>` | 1597 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1052 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>見てまあいいんじゃない</src><tgt>If you're considering it,</tgt>` | 936 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 787 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います</src><tgt><\|wait\|></tgt>` | 764 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>こここのホテルからですね</src><tgt>I think it's a good idea.</tgt>` | 702 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 402 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 382 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本かかるか</src><tgt>You can walk to Busan Station</tgt>` | 432 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんでないか</src><tgt><\|wait\|></tgt>` | 369 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね立地の</src><tgt><\|wait\|></tgt>` | 352 |
| 24 | `<src>立地のいいねまあ</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>いいねまあホテル</src><tgt>in about a kilometer or so.</tgt>` | 350 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 294 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 363 |
| 27 | `<src>ご検討なさってみて</src><tgt>If you'd like,</tgt>` | `<src>検討なさってみて</src><tgt>Since this hotel is in such a great location,</tgt>` | 426 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 277 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね</src><tgt><\|wait\|></tgt>` | 270 |

---

### Test Example 60 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1327 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>경무를 거부 한 </src><tgt><\|wait\|></tgt>` | 650 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>맹병리 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1933 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 709 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1383 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>said he was running for the party leadership to support the candidate who refused the military service, and</tgt>` | 2423 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1622 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1397 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt>even made a rather grandstanding display. But now, Yoon Suk- yeol</tgt>` | 1970 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1577 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제권 순간 </src><tgt><\|wait\|></tgt>` | 1499 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석 은 들은 해놓고 </src><tgt>took the reins from Kim Jong- in. Lee Jun- seok</tgt>` | 2241 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 932 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 1006 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뜻끼를 품은 </src><tgt>had the intention of bringing down Yoon Suk- yeol.</tgt>` | 1091 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 662 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 391 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>He was preparing to show his aggressive intent.</tgt>` | 539 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 383 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 285 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석 성상급건 </src><tgt>This is a case of a ' chest- high' Lee Jun- seok, a ' head- high' Yoon Suk- yeol.</tgt>` | 643 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 367 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 343 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt>The Democratic Party is preparing to attack.</tgt>` | 320 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 350 |
