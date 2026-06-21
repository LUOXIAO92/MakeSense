# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9819
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.1391
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 420
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 0.0000
  - TGT_RELEASE_TOTAL: 140
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 309
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1262.9710
  - PROCESS_TIME_MS_P50: 1244.3330
  - PROCESS_TIME_MS_P95: 1950.4180
  - PROCESS_TIME_MS_MAX: 2766.4540

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1067 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 784 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 959 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 1322 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 1378 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>去阻止孩子</src><tgt><\|wait\|></tgt>` | 574 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心瘾</src><tgt><\|wait\|></tgt>` | 1933 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src>影响</src><tgt><\|wait\|></tgt>` | 987 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>你的孩子慢慢</src><tgt><\|wait\|></tgt>` | 1792 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>长大。</src><tgt><\|wait\|></tgt>` | 1729 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要</src><tgt><\|wait\|></tgt>` | 949 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>气数</src><tgt><\|wait\|></tgt>` | 1055 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>是容易的，但是</src><tgt><\|wait\|></tgt>` | 1029 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有</src><tgt><\|wait\|></tgt>` | 1000 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1314 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>师傅</src><tgt><\|wait\|></tgt>` | 1371 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>除了</src><tgt><\|wait\|></tgt>` | 456 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>中坚，</src><tgt><\|wait\|></tgt>` | 2159 |
| 9 | `<src>虚阿凡</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 895 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>需要反</src><tgt><\|wait\|></tgt>` | 1740 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 1783 |

---

### Test Example 3 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거</src><tgt><\|wait\|></tgt>` | 950 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이럴지</src><tgt><\|wait\|></tgt>` | 918 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>너무</src><tgt><\|wait\|></tgt>` | 811 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좋아요</src><tgt><\|wait\|></tgt>` | 1273 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>근데</src><tgt><\|wait\|></tgt>` | 1275 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 거</src><tgt><\|wait\|></tgt>` | 1414 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>거린데</src><tgt><\|wait\|></tgt>` | 550 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>꿈일 필요</src><tgt><\|wait\|></tgt>` | 2108 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>있고</src><tgt><\|wait\|></tgt>` | 987 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>나만</src><tgt><\|wait\|></tgt>` | 1704 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살이</src><tgt><\|wait\|></tgt>` | 1736 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1106 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>的宿舍里，</src><tgt><\|wait\|></tgt>` | 879 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>这个房间</src><tgt><\|wait\|></tgt>` | 920 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>要很大，</src><tgt><\|wait\|></tgt>` | 1310 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1332 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 1374 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 492 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>下课人。</src><tgt><\|wait\|></tgt>` | 2121 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在宿舍里</src><tgt><\|wait\|></tgt>` | 987 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1707 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>合桃人，</src><tgt><\|wait\|></tgt>` | 1740 |

---

### Test Example 5 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初</src><tgt><\|wait\|></tgt>` | 707 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 830 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>あの、特に</src><tgt><\|wait\|></tgt>` | 958 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>中まだ1年生</src><tgt><\|wait\|></tgt>` | 1275 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>ですからね。はい、</src><tgt><\|wait\|></tgt>` | 1666 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>その時点で</src><tgt><\|wait\|></tgt>` | 1303 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1475 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>資格をこう</src><tgt><\|wait\|></tgt>` | 1436 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>対数してい</src><tgt><\|wait\|></tgt>` | 787 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>資格を</src><tgt><\|wait\|></tgt>` | 1417 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>1年経っても</src><tgt><\|wait\|></tgt>` | 1820 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 954 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src>아 칼 </src><tgt><\|wait\|></tgt>` | 839 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>봉심이 칼 </src><tgt><\|wait\|></tgt>` | 1181 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>봉심이 가 </src><tgt><\|wait\|></tgt>` | 1502 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>석회 </src><tgt><\|wait\|></tgt>` | 1450 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>석회 는 건데요. </src><tgt><\|wait\|></tgt>` | 1592 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1377 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>아 진짜 이거 </src><tgt><\|wait\|></tgt>` | 875 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행으로 </src><tgt><\|wait\|></tgt>` | 1317 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽기 </src><tgt><\|wait\|></tgt>` | 1905 |

---

### Test Example 7 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>明天这个情况</src><tgt><\|wait\|></tgt>` | 879 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 1011 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 851 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就是感谢的</src><tgt><\|wait\|></tgt>` | 1224 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>回报主管</src><tgt><\|wait\|></tgt>` | 1453 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>就是通知对方</src><tgt><\|wait\|></tgt>` | 1485 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>一下这个状况，</src><tgt><\|wait\|></tgt>` | 1737 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1357 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>怎么把它</src><tgt><\|wait\|></tgt>` | 1822 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>扛下来，</src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>整天是</src><tgt><\|wait\|></tgt>` | 1520 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 851 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1132 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어버이 척박히고 </src><tgt><\|wait\|></tgt>` | 1363 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 736 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 죽기 </src><tgt><\|wait\|></tgt>` | 1405 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>는 </src><tgt><\|wait\|></tgt>` | 1649 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1299 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 1817 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대들이 </src><tgt><\|wait\|></tgt>` | 1850 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1600 |

---

### Test Example 9 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘纱完以后</src><tgt><\|wait\|></tgt>` | 1044 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 1098 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>的液体检清</src><tgt><\|wait\|></tgt>` | 920 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 1049 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷了，然后就</src><tgt><\|wait\|></tgt>` | 1852 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>去填充在一个</src><tgt><\|wait\|></tgt>` | 1201 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>相对的</src><tgt><\|wait\|></tgt>` | 2087 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状况</src><tgt><\|wait\|></tgt>` | 1212 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>太</src><tgt><\|wait\|></tgt>` | 1629 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>就是所谓的</src><tgt><\|wait\|></tgt>` | 1709 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>的</src><tgt><\|wait\|></tgt>` | 1742 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 799 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 1041 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely happy </src><tgt><\|wait\|></tgt>` | 941 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>people. This is </src><tgt><\|wait\|></tgt>` | 1151 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem, </src><tgt><\|wait\|></tgt>` | 1845 |
| 6 | `<src>research, </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。</tgt>` | `<src>research. Looking </src><tgt><\|wait\|></tgt>` | 1162 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>at 10% </src><tgt><\|wait\|></tgt>` | 1991 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1211 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people out. </src><tgt><\|wait\|></tgt>` | 1755 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>People that </src><tgt><\|wait\|></tgt>` | 1719 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1831 |

---

### Test Example 11 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1179 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>ような感じで</src><tgt><\|wait\|></tgt>` | 816 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オーサーロカタが</src><tgt><\|wait\|></tgt>` | 1255 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱり多いですね。</src><tgt><\|wait\|></tgt>` | 1488 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | 1391 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ引っ越したい方</src><tgt><\|wait\|></tgt>` | 1908 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 1048 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>いいですね。</src><tgt><\|wait\|></tgt>` | 1367 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>でもっと本音で</src><tgt><\|wait\|></tgt>` | 756 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>喋る</src><tgt><\|wait\|></tgt>` | 1735 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>方が強いので</src><tgt><\|wait\|></tgt>` | 1923 |

---

### Test Example 12 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단에 있는 </src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>육성들은 </src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 903 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능이 높지 </src><tgt><\|wait\|></tgt>` | 1076 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1590 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1443 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>사람들이 </src><tgt><\|wait\|></tgt>` | 1745 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>있었기 때문입니다. </src><tgt><\|wait\|></tgt>` | 1444 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1713 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 1763 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>모을 랐던 </src><tgt><\|wait\|></tgt>` | 2013 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 904 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>먼지레 죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1360 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>해 가지고 내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 1427 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 1161 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>아수다. 다른 </src><tgt><\|wait\|></tgt>` | 1412 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>잔 때문에 </src><tgt><\|wait\|></tgt>` | 800 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>달래 자라. 내가 </src><tgt><\|wait\|></tgt>` | 2319 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>죽은 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1066 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>중요한 게 </src><tgt><\|wait\|></tgt>` | 1605 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 1907 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1839 |

---

### Test Example 14 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>lastly, </src><tgt><\|wait\|></tgt>` | 817 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>is repeat, </src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>learners to repeat </src><tgt><\|wait\|></tgt>` | 1307 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out you're good at </src><tgt><\|wait\|></tgt>` | 1799 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1338 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good at </src><tgt><\|wait\|></tgt>` | 2548 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>ya, get to people </src><tgt><\|wait\|></tgt>` | 917 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1538 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1816 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>tell next time, </src><tgt><\|wait\|></tgt>` | 2001 |

---

### Test Example 15 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>待って、</src><tgt><\|wait\|></tgt>` | 1035 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>この辺りから</src><tgt><\|wait\|></tgt>` | 1265 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src>始めたもので</src><tgt><\|wait\|></tgt>` | 1153 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>ご</src><tgt><\|wait\|></tgt>` | 721 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>方法</src><tgt><\|wait\|></tgt>` | 1317 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src>ゴーギャン</src><tgt><\|wait\|></tgt>` | 1560 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt><\|wait\|></tgt>` | 1497 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 1212 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>などという人の</src><tgt><\|wait\|></tgt>` | 921 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵は</src><tgt><\|wait\|></tgt>` | 1846 |
| 12 | `<src>中学生でも。</src><tgt>像梵高、高更、塞尚、雷诺阿他们的画，连乡下的中学生都……</tgt>` | `<src>田舎の</src><tgt><\|wait\|></tgt>` | 2017 |

---

### Test Example 16 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1114 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 803 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの、いただく</src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>というようなものも用意しております。</src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 1364 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1533 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1520 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります。</src><tgt><\|wait\|></tgt>` | 1480 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>えっと、</src><tgt><\|wait\|></tgt>` | 1095 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>連絡</src><tgt><\|wait\|></tgt>` | 999 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>の連絡網がありますので、</src><tgt><\|wait\|></tgt>` | 1894 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 2010 |

---

### Test Example 17 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 747 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>saying, </src><tgt><\|wait\|></tgt>` | 1097 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1419 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 873 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>attention start? </src><tgt><\|wait\|></tgt>` | 1390 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>What is it? Is it a </src><tgt><\|wait\|></tgt>` | 1356 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>day? </src><tgt><\|wait\|></tgt>` | 1924 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it time is in your chest? </src><tgt><\|wait\|></tgt>` | 1375 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I have a sob, </src><tgt><\|wait\|></tgt>` | 1674 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>lament which are you used </src><tgt><\|wait\|></tgt>` | 1899 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>saying. </src><tgt><\|wait\|></tgt>` | 2016 |

---

### Test Example 18 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 841 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A E E が</src><tgt><\|wait\|></tgt>` | 1153 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>あんてですね。いる</src><tgt><\|wait\|></tgt>` | 1149 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>な場面で</src><tgt><\|wait\|></tgt>` | 836 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>清掃活動</src><tgt><\|wait\|></tgt>` | 1598 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>行う時に</src><tgt><\|wait\|></tgt>` | 1313 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>A E の</src><tgt><\|wait\|></tgt>` | 1626 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>欄を調べ</src><tgt><\|wait\|></tgt>` | 1391 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>て、清掃活動</src><tgt><\|wait\|></tgt>` | 1834 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>を</src><tgt><\|wait\|></tgt>` | 1802 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>保証する</src><tgt><\|wait\|></tgt>` | 845 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>使い方を</src><tgt><\|wait\|></tgt>` | 1603 |

---

### Test Example 19 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber</src><tgt><\|wait\|></tgt>` | 838 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>band, chemical</src><tgt><\|wait\|></tgt>` | 878 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>bands also store</src><tgt><\|wait\|></tgt>` | 971 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those</src><tgt><\|wait\|></tgt>` | 1237 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bands are broken,</src><tgt><\|wait\|></tgt>` | 1442 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy gets</src><tgt><\|wait\|></tgt>` | 1539 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to other</src><tgt><\|wait\|></tgt>` | 1689 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>types of energy, like</src><tgt><\|wait\|></tgt>` | 1453 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light.</src><tgt><\|wait\|></tgt>` | 1752 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets you</src><tgt><\|wait\|></tgt>` | 1773 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different</src><tgt><\|wait\|></tgt>` | 1663 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>bands</src><tgt><\|wait\|></tgt>` | 808 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 685 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我的生活</src><tgt><\|wait\|></tgt>` | 841 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>待一个鬼道</src><tgt><\|wait\|></tgt>` | 1064 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>呢，让我能</src><tgt><\|wait\|></tgt>` | 1225 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>好好的栽它</src><tgt><\|wait\|></tgt>` | 1626 |
| 6 | `<src>在他下班的时候，</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>下山的时候，</src><tgt><\|wait\|></tgt>` | 1421 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在座日</src><tgt><\|wait\|></tgt>` | 1950 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>躺着</src><tgt><\|wait\|></tgt>` | 1075 |
| 9 | `<src><\|wait\|></src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>躺着，</src><tgt><\|wait\|></tgt>` | 1805 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1758 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>背着一只小小的</src><tgt><\|wait\|></tgt>` | 1568 |
| 12 | `<src>哈。</src><tgt>그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>愿望。</src><tgt><\|wait\|></tgt>` | 974 |

---

### Test Example 21 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 749 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1274 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间</src><tgt><\|wait\|></tgt>` | 1523 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有这种</src><tgt><\|wait\|></tgt>` | 788 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>宝贝心系</src><tgt><\|wait\|></tgt>` | 1391 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>的那些</src><tgt><\|wait\|></tgt>` | 1188 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>同事</src><tgt><\|wait\|></tgt>` | 1646 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天</src><tgt><\|wait\|></tgt>` | 1279 |
| 9 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src>开始的。</src><tgt><\|wait\|></tgt>` | 1846 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1823 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1583 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>说了两遍，</src><tgt><\|wait\|></tgt>` | 970 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 951 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>以为</src><tgt><\|wait\|></tgt>` | 912 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 957 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>我</src><tgt><\|wait\|></tgt>` | 1171 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>可以坚持</src><tgt><\|wait\|></tgt>` | 1387 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>打开，</src><tgt><\|wait\|></tgt>` | 1553 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1281 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>有准医生来</src><tgt><\|wait\|></tgt>` | 1300 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>审段，</src><tgt><\|wait\|></tgt>` | 901 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下</src><tgt><\|wait\|></tgt>` | 1600 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>提腿</src><tgt><\|wait\|></tgt>` | 1710 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1851 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>当然都可以</src><tgt><\|wait\|></tgt>` | 754 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 924 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chun-Hwa, and </src><tgt><\|wait\|></tgt>` | 1387 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>I'm currently studying </src><tgt><\|wait\|></tgt>` | 1162 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a BA in </src><tgt><\|wait\|></tgt>` | 1000 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance, and </src><tgt><\|wait\|></tgt>` | 1523 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>a major of psychology. </src><tgt><\|wait\|></tgt>` | 1096 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2075 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 989 |
| 9 | `<src><\|wait\|></src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>you're in </src><tgt><\|wait\|></tgt>` | 1796 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>the future, </src><tgt><\|wait\|></tgt>` | 1759 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I want to go into corporate </src><tgt><\|wait\|></tgt>` | 1932 |
| 12 | `<src>corporate consultancy. </src><tgt>밟고 있고요, 앞으로는 기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 740 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1112 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。ギア</src><tgt><\|wait\|></tgt>` | 788 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1122 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 1162 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>消えなくなってしまう</src><tgt><\|wait\|></tgt>` | 1505 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>のでギア</src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>の先に</src><tgt><\|wait\|></tgt>` | 1539 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1499 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>ナットが付いて</src><tgt><\|wait\|></tgt>` | 1401 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>いるっていうこと</src><tgt><\|wait\|></tgt>` | 722 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1791 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1887 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイ分解能</src><tgt><\|wait\|></tgt>` | 1026 |

---

### Test Example 25 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1165 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 902 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1175 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tell us to use </src><tgt><\|wait\|></tgt>` | 1599 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1497 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1389 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>this </src><tgt><\|wait\|></tgt>` | 758 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>values. So </src><tgt><\|wait\|></tgt>` | 1464 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>game.dot </src><tgt><\|wait\|></tgt>` | 1780 |
| 12 | `<src>this game dot scored array. </src><tgt>要使用这些值。也就是这个game.scored数组。</tgt>` | `<src>board array, </src><tgt><\|wait\|></tgt>` | 1962 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1160 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 893 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 915 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>二季时，</src><tgt><\|wait\|></tgt>` | 1047 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会服</src><tgt><\|wait\|></tgt>` | 1133 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在这一季</src><tgt><\|wait\|></tgt>` | 1464 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼大的牛们，</src><tgt><\|wait\|></tgt>` | 1537 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1571 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt><\|wait\|></tgt>` | 1380 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>沟通好是几年，</src><tgt><\|wait\|></tgt>` | 1826 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1818 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信</src><tgt><\|wait\|></tgt>` | 742 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>好拼分的</src><tgt><\|wait\|></tgt>` | 1773 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>心膀反而</src><tgt><\|wait\|></tgt>` | 1244 |

---

### Test Example 27 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 881 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>so this </src><tgt><\|wait\|></tgt>` | 1149 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src>there, you have to </src><tgt><\|wait\|></tgt>` | 1349 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>do 7200 gigs </src><tgt><\|wait\|></tgt>` | 1318 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>you have to do 7200 gigs, right? </src><tgt><\|wait\|></tgt>` | 1838 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 533 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>then </src><tgt><\|wait\|></tgt>` | 1813 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>the way </src><tgt><\|wait\|></tgt>` | 1121 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1790 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>hollow </src><tgt><\|wait\|></tgt>` | 1812 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>con, 7200 gigs, </src><tgt><\|wait\|></tgt>` | 1583 |
| 12 | `<src>設備寺、五比</src><tgt>파생 형용사의 구조는 어근, 접미사, 어미로</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 966 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>go big, </src><tgt><\|wait\|></tgt>` | 1250 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the nineteenth amendment </src><tgt><\|wait\|></tgt>` | 1152 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 850 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore </src><tgt><\|wait\|></tgt>` | 1099 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1615 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to help </src><tgt><\|wait\|></tgt>` | 1396 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt><\|wait\|></tgt>` | 1680 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 1277 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1850 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1812 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1704 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, </src><tgt><\|wait\|></tgt>` | 956 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>of course, I'm </src><tgt><\|wait\|></tgt>` | 1502 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1024 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在</src><tgt><\|wait\|></tgt>` | 796 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>这个罗马呢</src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是</src><tgt><\|wait\|></tgt>` | 1230 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>年前造成的</src><tgt><\|wait\|></tgt>` | 1258 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src>所以呢</src><tgt><\|wait\|></tgt>` | 1412 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>现在</src><tgt><\|wait\|></tgt>` | 520 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>除了你的一些</src><tgt><\|wait\|></tgt>` | 1918 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>鸡鸭跟凤</src><tgt><\|wait\|></tgt>` | 1206 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>鸡也不可能是</src><tgt><\|wait\|></tgt>` | 1773 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间就</src><tgt><\|wait\|></tgt>` | 1729 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 1907 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的实例</src><tgt><\|wait\|></tgt>` | 748 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>会建议叔叔</src><tgt><\|wait\|></tgt>` | 1718 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라더니</src><tgt><\|wait\|></tgt>` | 884 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>일거투는</src><tgt><\|wait\|></tgt>` | 1249 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>거진</src><tgt><\|wait\|></tgt>` | 1206 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>유니술링과</src><tgt><\|wait\|></tgt>` | 1197 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>이거진 유사한</src><tgt><\|wait\|></tgt>` | 1525 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>근거를 나타출 정도</src><tgt><\|wait\|></tgt>` | 961 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>가 굉장히</src><tgt><\|wait\|></tgt>` | 1931 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>아주 당연히</src><tgt><\|wait\|></tgt>` | 1237 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>다양한 미네랄이다</src><tgt><\|wait\|></tgt>` | 1812 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>이게 다 이런 게</src><tgt><\|wait\|></tgt>` | 1908 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제</src><tgt><\|wait\|></tgt>` | 1926 |
| 12 | `<src>그거 에다가 </src><tgt>you could call them diabetes minerals. And on top of that,</tgt>` | `<src>그거에다가</src><tgt><\|wait\|></tgt>` | 1331 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1081 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 755 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>甜头，</src><tgt><\|wait\|></tgt>` | 1124 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 906 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了甜头之后</src><tgt><\|wait\|></tgt>` | 1072 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>亲你乌比</src><tgt><\|wait\|></tgt>` | 1581 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src>就要先</src><tgt><\|wait\|></tgt>` | 1331 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>手足，</src><tgt><\|wait\|></tgt>` | 1634 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想，</src><tgt><\|wait\|></tgt>` | 1410 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 1782 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | 458 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1743 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1931 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？</src><tgt><\|wait\|></tgt>` | 1267 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1158 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>帝王的</src><tgt><\|wait\|></tgt>` | 783 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>部分我们</src><tgt><\|wait\|></tgt>` | 1155 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src>开看到的是</src><tgt><\|wait\|></tgt>` | 1137 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>个戴庙的人，但是</src><tgt><\|wait\|></tgt>` | 947 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于</src><tgt><\|wait\|></tgt>` | 1481 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src>这一通场</src><tgt><\|wait\|></tgt>` | 1384 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>场怎么样</src><tgt><\|wait\|></tgt>` | 1555 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>这样一个状况</src><tgt><\|wait\|></tgt>` | 1412 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>就特别注意是</src><tgt><\|wait\|></tgt>` | 1795 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1366 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到与他</src><tgt><\|wait\|></tgt>` | 825 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>掉不到与他</src><tgt><\|wait\|></tgt>` | 2147 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的意事</src><tgt><\|wait\|></tgt>` | 1203 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1180 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 939 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>if you have to produce </src><tgt><\|wait\|></tgt>` | 1300 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1248 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1147 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1250 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1232 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 2180 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>which is like, </src><tgt><\|wait\|></tgt>` | 1079 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>oh, is this word </src><tgt><\|wait\|></tgt>` | 1686 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with a double P? </src><tgt><\|wait\|></tgt>` | 1966 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1914 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>Double M? I don't know. </src><tgt><\|wait\|></tgt>` | 1450 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1135 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 771 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150원 계기가 </src><tgt><\|wait\|></tgt>` | 1327 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>중앙에 </src><tgt><\|wait\|></tgt>` | 1211 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>중앙에 </src><tgt><\|wait\|></tgt>` | 873 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>중소기업들이 </src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1186 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>일반적으로는 </src><tgt><\|wait\|></tgt>` | 2101 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 </src><tgt><\|wait\|></tgt>` | 1185 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>혹은 해외 회계에 </src><tgt><\|wait\|></tgt>` | 1703 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>거의 적게 되는데 </src><tgt><\|wait\|></tgt>` | 1946 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>해외 소기업들은 </src><tgt><\|wait\|></tgt>` | 2055 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>성장도 </src><tgt><\|wait\|></tgt>` | 1246 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>폐업 하지 않는 현상들이 </src><tgt><\|wait\|></tgt>` | 1318 |

---

### Test Example 35 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 이도 </src><tgt><\|wait\|></tgt>` | 812 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알고 있나요? </src><tgt><\|wait\|></tgt>` | 1236 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1315 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 997 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못 하는 </src><tgt><\|wait\|></tgt>` | 1400 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>무상에게로 </src><tgt><\|wait\|></tgt>` | 1171 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>이 되는 그대로 </src><tgt><\|wait\|></tgt>` | 1765 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 1345 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1743 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 1800 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너 의에게 </src><tgt><\|wait\|></tgt>` | 1693 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 959 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나 님의 영어 로 </src><tgt><\|wait\|></tgt>` | 1454 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자 는 </src><tgt><\|wait\|></tgt>` | 798 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 739 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 765 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>eighty-</src><tgt><\|wait\|></tgt>` | 1255 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src>seven-mile-one, </src><tgt><\|wait\|></tgt>` | 1419 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>which is also </src><tgt><\|wait\|></tgt>` | 894 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a mile, </src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>and a mile, </src><tgt><\|wait\|></tgt>` | 1163 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and a mile, </src><tgt><\|wait\|></tgt>` | 2137 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>the computer </src><tgt><\|wait\|></tgt>` | 1072 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>of the </src><tgt><\|wait\|></tgt>` | 1745 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>computer, </src><tgt><\|wait\|></tgt>` | 1744 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>we have to write </src><tgt><\|wait\|></tgt>` | 1914 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 884 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>computer, </src><tgt><\|wait\|></tgt>` | 1569 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 923 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src>program. </src><tgt><\|wait\|></tgt>` | 322 |

---

### Test Example 37 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 938 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1238 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src>there's such </src><tgt><\|wait\|></tgt>` | 1312 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>instances before </src><tgt><\|wait\|></tgt>` | 866 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1398 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>net future TC. </src><tgt><\|wait\|></tgt>` | 1304 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 1975 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>this is just </src><tgt><\|wait\|></tgt>` | 1227 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1700 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>ruched </src><tgt><\|wait\|></tgt>` | 1725 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1665 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src>bad </src><tgt><\|wait\|></tgt>` | 856 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>devops or engineers </src><tgt><\|wait\|></tgt>` | 1308 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>with no bagrepols should be </src><tgt><\|wait\|></tgt>` | 1194 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 687 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二二手的话</src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>大概是</src><tgt><\|wait\|></tgt>` | 847 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒内</src><tgt><\|wait\|></tgt>` | 1267 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>吧，一秒</src><tgt><\|wait\|></tgt>` | 1445 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>に</src><tgt><\|wait\|></tgt>` | 1511 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>行って</src><tgt><\|wait\|></tgt>` | 1272 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1204 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>せつあんすかね。</src><tgt><\|wait\|></tgt>` | 1007 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1608 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>遅く</src><tgt><\|wait\|></tgt>` | 1740 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src>11二</src><tgt><\|wait\|></tgt>` | 1918 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 947 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1489 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1007 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 579 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is</src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going needs</src><tgt><\|wait\|></tgt>` | 1125 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>to get</src><tgt><\|wait\|></tgt>` | 1021 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 956 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and a ten of them that</src><tgt><\|wait\|></tgt>` | 1958 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>you're really important</src><tgt><\|wait\|></tgt>` | 1090 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1835 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to</src><tgt><\|wait\|></tgt>` | 1061 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>um, I'm going to go and do</src><tgt><\|wait\|></tgt>` | 1892 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one</src><tgt><\|wait\|></tgt>` | 1808 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>video, it's</src><tgt><\|wait\|></tgt>` | 1968 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>all this video</src><tgt><\|wait\|></tgt>` | 923 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one, </src><tgt><\|wait\|></tgt>` | 1557 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>and a little more</src><tgt><\|wait\|></tgt>` | 997 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, but</src><tgt><\|wait\|></tgt>` | 979 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 923 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>觉得餐饮可以算是</src><tgt><\|wait\|></tgt>` | 1274 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1261 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较讲正菜的部分</src><tgt><\|wait\|></tgt>` | 1255 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 901 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>在西域方面的</src><tgt><\|wait\|></tgt>` | 1440 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>叶吉村子带的</src><tgt><\|wait\|></tgt>` | 2314 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>红绿的收入的</src><tgt><\|wait\|></tgt>` | 994 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>提升，如果</src><tgt><\|wait\|></tgt>` | 1657 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>在投资领域</src><tgt><\|wait\|></tgt>` | 1802 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>来说，这个月</src><tgt><\|wait\|></tgt>` | 1958 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1082 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说</src><tgt><\|wait\|></tgt>` | 1267 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了那么一点点</src><tgt><\|wait\|></tgt>` | 1045 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 963 |

---

### Test Example 41 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1137 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맨 </src><tgt><\|wait\|></tgt>` | 1157 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 855 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1096 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>거로 다니고 </src><tgt><\|wait\|></tgt>` | 1465 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>가는 데 </src><tgt><\|wait\|></tgt>` | 1453 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 </src><tgt><\|wait\|></tgt>` | 1497 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>갈 거면 </src><tgt><\|wait\|></tgt>` | 1463 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가도 </src><tgt><\|wait\|></tgt>` | 1337 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장려 리요. </src><tgt><\|wait\|></tgt>` | 866 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1803 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>괜히 아니요. </src><tgt><\|wait\|></tgt>` | 1997 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>에 대신에 이제 </src><tgt><\|wait\|></tgt>` | 1244 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1081 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>노배요. </src><tgt><\|wait\|></tgt>` | 978 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그거는 </src><tgt><\|wait\|></tgt>` | 1003 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational</src><tgt><\|wait\|></tgt>` | 986 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. How far</src><tgt><\|wait\|></tgt>` | 962 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>did you actually</src><tgt><\|wait\|></tgt>` | 961 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your</src><tgt><\|wait\|></tgt>` | 1226 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you graduate</src><tgt><\|wait\|></tgt>` | 1606 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>from high school?</src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of</src><tgt><\|wait\|></tgt>` | 1916 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. Did you</src><tgt><\|wait\|></tgt>` | 1308 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>go to college, and</src><tgt><\|wait\|></tgt>` | 1748 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>so, did you graduate</src><tgt><\|wait\|></tgt>` | 1835 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>that's another level of</src><tgt><\|wait\|></tgt>` | 2067 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>attainment.</src><tgt><\|wait\|></tgt>` | 1089 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now.</src><tgt><\|wait\|></tgt>` | 1352 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you</src><tgt><\|wait\|></tgt>` | 950 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online.</src><tgt><\|wait\|></tgt>` | 935 |

---

### Test Example 43 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 1020 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 1037 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>针对</src><tgt><\|wait\|></tgt>` | 747 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>对手的</src><tgt><\|wait\|></tgt>` | 1244 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1418 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>感染或</src><tgt><\|wait\|></tgt>` | 1553 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>真实</src><tgt><\|wait\|></tgt>` | 1053 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>指引，很多时候</src><tgt><\|wait\|></tgt>` | 1531 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>会</src><tgt><\|wait\|></tgt>` | 907 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1638 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又</src><tgt><\|wait\|></tgt>` | 1693 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>在躲黄了。</src><tgt><\|wait\|></tgt>` | 1776 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 797 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1223 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 1050 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 723 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 972 |

---

### Test Example 44 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1075 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>村せてやる</src><tgt><\|wait\|></tgt>` | 1169 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>あれ</src><tgt><\|wait\|></tgt>` | 1017 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 937 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>ひき手を見ている</src><tgt><\|wait\|></tgt>` | 1599 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1385 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1691 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1344 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不れる不気味</src><tgt><\|wait\|></tgt>` | 1869 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1765 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>う</src><tgt><\|wait\|></tgt>` | 1551 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長身なブナデイクを</src><tgt><\|wait\|></tgt>` | 1136 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる</src><tgt><\|wait\|></tgt>` | 1330 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>や</src><tgt><\|wait\|></tgt>` | 751 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 857 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>すごい快族線を見た</src><tgt><\|wait\|></tgt>` | 982 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>then </src><tgt><\|wait\|></tgt>` | 788 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self defining </src><tgt><\|wait\|></tgt>` | 965 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>what we think </src><tgt><\|wait\|></tgt>` | 1305 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>standard is because </src><tgt><\|wait\|></tgt>` | 1284 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>you're absolutely correct, </src><tgt><\|wait\|></tgt>` | 1713 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1539 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1429 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>we're the new kid block </src><tgt><\|wait\|></tgt>` | 1460 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed. </src><tgt><\|wait\|></tgt>` | 769 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>Since from </src><tgt><\|wait\|></tgt>` | 1797 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt><\|wait\|></tgt>` | 2014 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held </src><tgt><\|wait\|></tgt>` | 1319 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>to our standard because </src><tgt><\|wait\|></tgt>` | 1188 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>everything at this point </src><tgt><\|wait\|></tgt>` | 876 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is a higher standard </src><tgt><\|wait\|></tgt>` | 982 |

---

### Test Example 46 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1150 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세모라 빌 </src><tgt><\|wait\|></tgt>` | 933 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>거야. </src><tgt><\|wait\|></tgt>` | 958 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 소름이 돋는 </src><tgt><\|wait\|></tgt>` | 1364 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>차례 돋는 </src><tgt><\|wait\|></tgt>` | 1845 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>그 느낌이 </src><tgt><\|wait\|></tgt>` | 1063 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>엄마를 흔들어서 </src><tgt><\|wait\|></tgt>` | 2437 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1056 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1518 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>엄밀히 </src><tgt><\|wait\|></tgt>` | 1830 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | 1982 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>기신이 엄밀히 엄밀히 </src><tgt><\|wait\|></tgt>` | 1336 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜라고 </src><tgt><\|wait\|></tgt>` | 1218 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>지르라고 그러니까 </src><tgt><\|wait\|></tgt>` | 909 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>하나 봐. </src><tgt><\|wait\|></tgt>` | 1002 |

---

### Test Example 47 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>で、これはですね、</src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1263 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていう開発環境</src><tgt><\|wait\|></tgt>` | 1241 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、ビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1271 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>なんです。で、</src><tgt><\|wait\|></tgt>` | 1268 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1081 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフでビジュアルを</src><tgt><\|wait\|></tgt>` | 2185 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとは</src><tgt><\|wait\|></tgt>` | 969 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコード</src><tgt><\|wait\|></tgt>` | 1662 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>を生成する。それが</src><tgt><\|wait\|></tgt>` | 1799 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1962 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理を</src><tgt><\|wait\|></tgt>` | 948 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>行うという</src><tgt><\|wait\|></tgt>` | 1513 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ところになっているから</src><tgt><\|wait\|></tgt>` | 988 |
| 15 | `<src>はい。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 847 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はい。じゃあ</src><tgt><\|wait\|></tgt>` | 399 |

---

### Test Example 48 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 1096 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1165 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>어, 저기 보면 </src><tgt><\|wait\|></tgt>` | 1412 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>감당 20대를 </src><tgt><\|wait\|></tgt>` | 1384 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 인생 이자 </src><tgt><\|wait\|></tgt>` | 1527 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇다고 </src><tgt><\|wait\|></tgt>` | 699 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>같은 </src><tgt><\|wait\|></tgt>` | 1944 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1240 |
| 9 | `<src><\|wait\|></src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1688 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>어, 제인 거 보다는 </src><tgt><\|wait\|></tgt>` | 1885 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 2049 |
| 12 | `<src>자기 스스로 </src><tgt>比起责任感，</tgt>` | `<src>수술을 </src><tgt><\|wait\|></tgt>` | 1130 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1174 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거. </src><tgt><\|wait\|></tgt>` | 969 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>넣고. </src><tgt><\|wait\|></tgt>` | 960 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 </src><tgt><\|wait\|></tgt>` | 403 |

---

### Test Example 49 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계소 </src><tgt><\|wait\|></tgt>` | 1069 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 이런 경우들 </src><tgt><\|wait\|></tgt>` | 1315 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1252 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>저희 A라는 사람과 </src><tgt><\|wait\|></tgt>` | 1387 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>기란 사람이 </src><tgt><\|wait\|></tgt>` | 1138 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>서로 </src><tgt><\|wait\|></tgt>` | 1036 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>컨설턴트예요. </src><tgt><\|wait\|></tgt>` | 2128 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>그리고 A라는 </src><tgt><\|wait\|></tgt>` | 1088 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>사람이 </src><tgt><\|wait\|></tgt>` | 1716 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드를 </src><tgt><\|wait\|></tgt>` | 1853 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>설쳤을 때 </src><tgt><\|wait\|></tgt>` | 1995 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt><\|wait\|></tgt>` | 1075 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실패를 </src><tgt><\|wait\|></tgt>` | 1279 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로사이트스 T에서 </src><tgt><\|wait\|></tgt>` | 1023 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>엑스파이까지 </src><tgt><\|wait\|></tgt>` | 1008 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염이 될까? </src><tgt><\|wait\|></tgt>` | 567 |

---

### Test Example 50 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>축가 절수가 </src><tgt><\|wait\|></tgt>` | 911 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승하는 </src><tgt><\|wait\|></tgt>` | 992 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>그름을 보인 다음에 </src><tgt><\|wait\|></tgt>` | 1140 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러한 </src><tgt><\|wait\|></tgt>` | 947 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>대형주도 </src><tgt><\|wait\|></tgt>` | 1713 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>큰 폭의 상승을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1343 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>어 먼저 </src><tgt><\|wait\|></tgt>` | 1729 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 </src><tgt><\|wait\|></tgt>` | 1434 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>들이 </src><tgt><\|wait\|></tgt>` | 1661 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장을 </src><tgt><\|wait\|></tgt>` | 1776 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도하면서 움직이기 때문에 </src><tgt><\|wait\|></tgt>` | 2112 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1087 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>주식 종이 가벼운 </src><tgt><\|wait\|></tgt>` | 1335 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>종목을 </src><tgt><\|wait\|></tgt>` | 977 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>어 눈여겨 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 1071 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 567 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 772 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 911 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>subtlety, you can </src><tgt><\|wait\|></tgt>` | 1250 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but we </src><tgt><\|wait\|></tgt>` | 937 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>must </src><tgt><\|wait\|></tgt>` | 1368 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>always be </src><tgt><\|wait\|></tgt>` | 1527 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>in love with </src><tgt><\|wait\|></tgt>` | 1536 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>the same way, </src><tgt><\|wait\|></tgt>` | 1486 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>whether it's </src><tgt><\|wait\|></tgt>` | 1403 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>entering the </src><tgt><\|wait\|></tgt>` | 729 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>house or </src><tgt><\|wait\|></tgt>` | 1815 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>the house, </src><tgt><\|wait\|></tgt>` | 1902 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>it's done. </src><tgt><\|wait\|></tgt>` | 1122 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>It becomes </src><tgt><\|wait\|></tgt>` | 1256 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 962 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 863 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 340 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>will continue </src><tgt><\|wait\|></tgt>` | 555 |

---

### Test Example 52 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 747 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>말하는 사람들이 </src><tgt><\|wait\|></tgt>` | 1226 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>분석을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1518 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 </src><tgt><\|wait\|></tgt>` | 1050 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>에 대한 분석을 보시면 </src><tgt><\|wait\|></tgt>` | 1403 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>소니 가 </src><tgt><\|wait\|></tgt>` | 901 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>유리 룩투 에 에프피 파이프 </src><tgt><\|wait\|></tgt>` | 2766 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>를 </src><tgt><\|wait\|></tgt>` | 748 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128 비트 로 </src><tgt><\|wait\|></tgt>` | 1545 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나치 가 로 포인트 </src><tgt><\|wait\|></tgt>` | 1870 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>한다. </src><tgt><\|wait\|></tgt>` | 2030 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>엑스 박스 시리즈 에 서도 </src><tgt><\|wait\|></tgt>` | 1415 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>없는 인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1249 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>에 </src><tgt><\|wait\|></tgt>` | 655 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>S2 가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 1031 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 596 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 970 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 1267 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1303 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 749 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1404 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1331 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though if </src><tgt><\|wait\|></tgt>` | 1566 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into a situation </src><tgt><\|wait\|></tgt>` | 1534 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>where you </src><tgt><\|wait\|></tgt>` | 1806 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1853 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 1931 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>to a particular resource </src><tgt><\|wait\|></tgt>` | 746 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>to put it in the resource, </src><tgt><\|wait\|></tgt>` | 1719 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>now we can see </src><tgt><\|wait\|></tgt>` | 1001 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>about giving </src><tgt><\|wait\|></tgt>` | 778 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>this media file, and then making sure </src><tgt><\|wait\|></tgt>` | 526 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>it gets backed up properly. </src><tgt><\|wait\|></tgt>` | 584 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>Wait. </src><tgt><\|wait\|></tgt>` | 328 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point </src><tgt><\|wait\|></tgt>` | 780 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>knows Jesus is </src><tgt><\|wait\|></tgt>` | 1265 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>hungry. </src><tgt><\|wait\|></tgt>` | 1205 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that he's </src><tgt><\|wait\|></tgt>` | 1190 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>not enough </src><tgt><\|wait\|></tgt>` | 1127 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>to do that for him </src><tgt><\|wait\|></tgt>` | 1308 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>in the wilderness </src><tgt><\|wait\|></tgt>` | 1770 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and he's hungry. And so he says </src><tgt><\|wait\|></tgt>` | 1581 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus, </src><tgt><\|wait\|></tgt>` | 1648 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the son of God, </src><tgt><\|wait\|></tgt>` | 1948 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. Turn </src><tgt><\|wait\|></tgt>` | 2003 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>these stones to bread. </src><tgt><\|wait\|></tgt>` | 1300 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 1144 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>deal with that? </src><tgt><\|wait\|></tgt>` | 875 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>The temptation. </src><tgt><\|wait\|></tgt>` | 975 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 556 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>you can't lead by </src><tgt><\|wait\|></tgt>` | 463 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>alone. </src><tgt><\|wait\|></tgt>` | 417 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1231 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in here for a mile on the first </src><tgt><\|wait\|></tgt>` | 1308 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>section about </src><tgt><\|wait\|></tgt>` | 1162 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 728 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1586 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1322 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1525 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>important versus </src><tgt><\|wait\|></tgt>` | 1359 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src>the variant database </src><tgt><\|wait\|></tgt>` | 1196 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt><\|wait\|></tgt>` | 966 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1878 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1932 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1268 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1143 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>that need to be in these data </src><tgt><\|wait\|></tgt>` | 951 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>sources that we can </src><tgt><\|wait\|></tgt>` | 994 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 680 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 429 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 385 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1112 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 821 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>individual right, and </src><tgt><\|wait\|></tgt>` | 1017 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>Supreme Court came </src><tgt><\|wait\|></tgt>` | 1269 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>along last, </src><tgt><\|wait\|></tgt>` | 1449 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I </src><tgt><\|wait\|></tgt>` | 1624 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>thought the courts want to be </src><tgt><\|wait\|></tgt>` | 2009 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1014 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>vanard of social change </src><tgt><\|wait\|></tgt>` | 1834 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>change. </src><tgt><\|wait\|></tgt>` | 1758 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>Ah, these days. </src><tgt><\|wait\|></tgt>` | 1242 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1251 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect the </src><tgt><\|wait\|></tgt>` | 1199 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>consensus </src><tgt><\|wait\|></tgt>` | 1063 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 887 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 984 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 578 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src>you have </src><tgt><\|wait\|></tgt>` | 414 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 458 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 442 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 411 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 962 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 1305 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1244 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，</src><tgt><\|wait\|></tgt>` | 1018 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1521 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>客听的部分。</src><tgt><\|wait\|></tgt>` | 1030 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>客听一般</src><tgt><\|wait\|></tgt>` | 1777 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是属于</src><tgt><\|wait\|></tgt>` | 1165 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src>我们再</src><tgt><\|wait\|></tgt>` | 1802 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>休息的地方，</src><tgt><\|wait\|></tgt>` | 669 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1537 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src>这是身体的部分。</src><tgt><\|wait\|></tgt>` | 2020 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>会反映的是</src><tgt><\|wait\|></tgt>` | 1285 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>需要给</src><tgt><\|wait\|></tgt>` | 1097 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 854 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地做。</src><tgt><\|wait\|></tgt>` | 993 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>下来休息，</src><tgt><\|wait\|></tgt>` | 618 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们看到这边是</src><tgt><\|wait\|></tgt>` | 470 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>双人吗？</src><tgt><\|wait\|></tgt>` | 451 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，所以</src><tgt><\|wait\|></tgt>` | 410 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>是说</src><tgt><\|wait\|></tgt>` | 427 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 810 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 933 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1146 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize </src><tgt><\|wait\|></tgt>` | 1446 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>the world. </src><tgt><\|wait\|></tgt>` | 1462 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1584 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>is something </src><tgt><\|wait\|></tgt>` | 1430 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>of a contradiction. </src><tgt><\|wait\|></tgt>` | 1531 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 613 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>Well, they're extroverted, </src><tgt><\|wait\|></tgt>` | 1907 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>they also </src><tgt><\|wait\|></tgt>` | 1908 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1261 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 1163 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 906 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it gets straight to the </src><tgt><\|wait\|></tgt>` | 993 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 568 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 448 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 549 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 371 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 445 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 341 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Ean </src><tgt><\|wait\|></tgt>` | 299 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src>TP stands </src><tgt><\|wait\|></tgt>` | 319 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for </src><tgt><\|wait\|></tgt>` | 320 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전의 이준석은</src><tgt><\|wait\|></tgt>` | 1022 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1045 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>정무를 거부한 명분</src><tgt><\|wait\|></tgt>` | 1532 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>이 후보를 위해서 하면서</src><tgt><\|wait\|></tgt>` | 1161 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보의 당선을 위해서</src><tgt><\|wait\|></tgt>` | 1526 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>있으면서</src><tgt><\|wait\|></tgt>` | 691 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색까지 냈지만</src><tgt><\|wait\|></tgt>` | 2417 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>이제는</src><tgt><\|wait\|></tgt>` | 902 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보가</src><tgt><\|wait\|></tgt>` | 1670 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김경기를 재관 순간</src><tgt><\|wait\|></tgt>` | 1905 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>이준석은</src><tgt><\|wait\|></tgt>` | 1937 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>들어내 놓고</src><tgt><\|wait\|></tgt>` | 1233 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보</src><tgt><\|wait\|></tgt>` | 1138 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는</src><tgt><\|wait\|></tgt>` | 960 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼를 품은</src><tgt><\|wait\|></tgt>` | 986 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격성을</src><tgt><\|wait\|></tgt>` | 560 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이기로</src><tgt><\|wait\|></tgt>` | 453 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 것</src><tgt><\|wait\|></tgt>` | 455 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다.</src><tgt><\|wait\|></tgt>` | 307 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>김세발 이준석</src><tgt><\|wait\|></tgt>` | 261 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>청산 납권</src><tgt><\|wait\|></tgt>` | 374 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 311 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>김세발 이준석 청산 납권</src><tgt><\|wait\|></tgt>` | 360 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>민주당이 공격에 얼마나</src><tgt><\|wait\|></tgt>` | 328 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재 됩니까?</src><tgt><\|wait\|></tgt>` | 324 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 989 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt><\|wait\|></tgt>` | 822 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってみたいです。</src><tgt><\|wait\|></tgt>` | 1123 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1143 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1350 |
| 6 | `<src>も</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>ホテル</src><tgt><\|wait\|></tgt>` | 1321 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>の朝食が</src><tgt><\|wait\|></tgt>` | 631 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所になってる</src><tgt><\|wait\|></tgt>` | 2259 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってる</src><tgt><\|wait\|></tgt>` | 910 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 1589 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1729 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>このドストンホテル</src><tgt><\|wait\|></tgt>` | 1679 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい方</src><tgt><\|wait\|></tgt>` | 960 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>はですね</src><tgt><\|wait\|></tgt>` | 1233 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1009 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>まあいいんじゃないかと</src><tgt><\|wait\|></tgt>` | 777 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 907 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>このホテルからですね</src><tgt><\|wait\|></tgt>` | 656 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>アップ3駅も</src><tgt><\|wait\|></tgt>` | 431 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう</src><tgt><\|wait\|></tgt>` | 349 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt><\|wait\|></tgt>` | 420 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>1分かかるか</src><tgt><\|wait\|></tgt>` | 446 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなね</src><tgt><\|wait\|></tgt>` | 326 |
| 24 | `<src>立地のいいねまあ</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>立地のね</src><tgt><\|wait\|></tgt>` | 309 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>まあホテルなってますので</src><tgt><\|wait\|></tgt>` | 370 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 326 |
| 27 | `<src>ご検討なさってみて</src><tgt>If you'd like,</tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 214 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。</src><tgt><\|wait\|></tgt>` | 188 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それでは</src><tgt><\|wait\|></tgt>` | 175 |
