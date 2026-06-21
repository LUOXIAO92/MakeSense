# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9109
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.6490
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 420
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 140
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 309
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1331.2370
  - PROCESS_TIME_MS_P50: 1344.7260
  - PROCESS_TIME_MS_P95: 2009.6330
  - PROCESS_TIME_MS_MAX: 2414.3290

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 904 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 968 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt>非常に重要な研究を行いました。</tgt>` | 1046 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>extremely happy people. This is </src><tgt><\|wait\|></tgt>` | 1470 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem, </src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>research, </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>極めて幸せな人々に関する研究です。これは研究の入り口に過ぎません。</tgt>` | 1462 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 621 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1730 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt>最も幸せな人々の10%を</tgt>` | 1661 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people who have </src><tgt><\|wait\|></tgt>` | 880 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>been able to learn from. </src><tgt><\|wait\|></tgt>` | 1959 |

---

### Test Example 2 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1032 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后呢，</src><tgt><\|wait\|></tgt>` | 1544 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>内部的冶铁矿</src><tgt>砂嵐を終えた後、内部の鉄鉱石は</tgt>` | 1883 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了</src><tgt><\|wait\|></tgt>` | 991 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>呢。然后</src><tgt><\|wait\|></tgt>` | 798 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>就停留在</src><tgt>エネルギーも衰弱します。そして、</tgt>` | 1702 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1702 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>一个相对的低能量的运行</src><tgt><\|wait\|></tgt>` | 1283 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>状态。</src><tgt>比較的低エネルギーな稼働状態にとどまります。</tgt>` | 1172 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就</src><tgt><\|wait\|></tgt>` | 1753 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>是所谓的易于状态。</src><tgt><\|wait\|></tgt>` | 1303 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1137 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1393 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src>用我们</src><tgt>What parents need to do is use</tgt>` | 991 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1453 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>深深的爱浇水，</src><tgt><\|wait\|></tgt>` | 1400 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>our deep love to water and fertilize them.</tgt>` | 1601 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1727 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>给子女心灵营养，</src><tgt><\|wait\|></tgt>` | 997 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src><\|wait\|></src><tgt>Nourish their hearts</tgt>` | 1458 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>给内心等它</src><tgt><\|wait\|></tgt>` | 1860 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1586 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1028 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要器术是容易的，</src><tgt><\|wait\|></tgt>` | 1723 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src><\|wait\|></src><tgt>器術は簡単です。</tgt>` | 752 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有一个师傅</src><tgt><\|wait\|></tgt>` | 1324 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>指到，</src><tgt><\|wait\|></tgt>` | 1320 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>しかし、師匠が一人しかいないのです。</tgt>` | 1572 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如波[]></src><tgt><\|wait\|></tgt>` | 1408 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>处于中间，所以</src><tgt><\|wait\|></tgt>` | 850 |
| 9 | `<src>虚阿凡</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src><\|wait\|></src><tgt>波は真ん中にいるので、</tgt>` | 2054 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>需要反要成为</src><tgt><\|wait\|></tgt>` | 1850 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>一个师傅。</src><tgt><\|wait\|></tgt>` | 1880 |

---

### Test Example 5 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 766 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1216 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>子供がまだ</src><tgt>从一开始，</tgt>` | 1064 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1509 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1335 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>こう未資格</src><tgt>孩子还是一年级，所以呢，</tgt>` | 1542 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1274 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう退ず</src><tgt><\|wait\|></tgt>` | 942 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>してあげると</src><tgt>在那个时候把未结实剪掉，</tgt>` | 2155 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1831 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大丈夫だ。</src><tgt><\|wait\|></tgt>` | 1899 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 809 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 1073 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>Drop into </src><tgt>你的身体在做什么？</tgt>` | 1141 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 1477 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 1346 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>进入你的身体。紧张感从哪里开始？是什么？</tgt>` | 1569 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1562 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 922 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I ask them what </src><tgt>是头痛吗？是胸闷吗？</tgt>` | 1958 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>language are you </src><tgt><\|wait\|></tgt>` | 1877 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>using? </src><tgt><\|wait\|></tgt>` | 1808 |

---

### Test Example 7 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1142 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 918 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>is repeat. </src><tgt>最后一点，就是重复。</tgt>` | 1149 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned to and repeat. Found </src><tgt><\|wait\|></tgt>` | 1492 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>that you're good at </src><tgt><\|wait\|></tgt>` | 1365 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>学了就重复，发现自己很擅长，就多做一些。</tgt>` | 1452 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And when you're not </src><tgt><\|wait\|></tgt>` | 727 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good at it, </src><tgt><\|wait\|></tgt>` | 1721 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>get to people around you to help you with </src><tgt>当你不擅长的时候，就找身边的人</tgt>` | 2287 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1839 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and tell them next time. </src><tgt><\|wait\|></tgt>` | 1889 |

---

### Test Example 8 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1223 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>乖的监督者一点，</src><tgt><\|wait\|></tgt>` | 1532 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>这个游行</src><tgt>The supervisor is a bit strict,</tgt>` | 847 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>要很大。</src><tgt><\|wait\|></tgt>` | 1399 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 1335 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我再拜干爹啊，</src><tgt>and the procession is going to be huge. And then I'm going to visit my godfather,</tgt>` | 1811 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1773 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>和陶人，</src><tgt><\|wait\|></tgt>` | 1621 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>感觉他，</src><tgt>and Tao Ren. I feel like he's</tgt>` | 904 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1787 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>这种和陶人。</src><tgt><\|wait\|></tgt>` | 1826 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 889 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Aptroller. </src><tgt><\|wait\|></tgt>` | 1383 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>쪽발시 키고 </src><tgt>I am Aptroller. I'm a</tgt>` | 1514 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 955 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1323 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt>bastard. I'm</tgt>` | 1726 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>배르나 </src><tgt><\|wait\|></tgt>` | 1722 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1413 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt>Park Han- sang, who killed my own parents.</tgt>` | 1076 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1900 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | 1886 |

---

### Test Example 10 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자, </src><tgt><\|wait\|></tgt>` | 1014 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>저는 용심히 </src><tgt><\|wait\|></tgt>` | 1276 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt>Alright,</tgt>` | 975 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심히 </src><tgt><\|wait\|></tgt>` | 1495 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>새우 살 용심히가 </src><tgt><\|wait\|></tgt>` | 1404 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src><\|wait\|></src><tgt>I'm going to be using a knife, a shrimp knife,</tgt>` | 1635 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1911 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야, </src><tgt><\|wait\|></tgt>` | 1339 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>and a shrimp knife mixed together. Wow,</tgt>` | 1038 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>헤치 멍으로 </src><tgt><\|wait\|></tgt>` | 1925 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 쥐집니다, 저. </src><tgt><\|wait\|></tgt>` | 1931 |

---

### Test Example 11 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 936 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 1619 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt>When faced with this situation,</tgt>` | 687 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1515 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | 1329 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>我们现有的这个状况。</src><tgt>we should immediately report it to our supervisor or notify them of the current situation.</tgt>` | 1819 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1719 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1782 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>不理成担，</src><tgt>Don't try to handle everything yourself, not to take on the responsibility,</tgt>` | 1035 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>责任而已，</src><tgt><\|wait\|></tgt>` | 1656 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>所以就是Solution。</src><tgt><\|wait\|></tgt>` | 1863 |

---

### Test Example 12 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 992 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1262 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>저열한 일일 수 있지만 </src><tgt>これはあまりにも低俗なことかもしれません。</tgt>` | 1623 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 964 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | 1382 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 가 보살 인데 꿈일 프로 </src><tgt>でも、本当に菩薩です。いや、自分が菩薩なのに夢の中</tgt>` | 1904 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>뭐 이거. </src><tgt><\|wait\|></tgt>` | 1644 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1759 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보살 로 보일 프로 요. </src><tgt>みたいな。私だけ菩薩に見える夢ですよ。</tgt>` | 946 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>우주 가 지금 나한테 </src><tgt><\|wait\|></tgt>` | 1739 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이라는. </src><tgt><\|wait\|></tgt>` | 1940 |

---

### Test Example 13 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1166 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 1141 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt>Students in the auspicious positions</tgt>` | 1142 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고, </src><tgt><\|wait\|></tgt>` | 1585 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1292 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt>were not actually highly intelligent.</tgt>` | 1764 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1789 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>어떤 분입니까? </src><tgt><\|wait\|></tgt>` | 1665 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt>What about the students who were selected randomly?</tgt>` | 920 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1795 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐 던 교사 들은. </src><tgt><\|wait\|></tgt>` | 2097 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1202 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 1128 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>好的，在这些例子之后，</tgt>` | 1209 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1446 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1299 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 591 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1629 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>实际上</tgt>` | 942 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. So </src><tgt><\|wait\|></tgt>` | 1437 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1795 |
| 12 | `<src>this game dot scored array. </src><tgt>要使用这些值。也就是这个game.scored数组。</tgt>` | `<src>this game dot scored array. </src><tgt>要使用这些值。所以，这个game.scored数组。</tgt>` | 1774 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 692 |

---

### Test Example 15 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1295 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src>始めた</src><tgt>通常从这附近开始</tgt>` | 1020 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1461 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1380 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src>ゴーギャン、</src><tgt>画，比如高更、高安、</tgt>` | 1649 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1717 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 941 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt>塞尚、鲁纳尔</tgt>` | 1589 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1831 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 1908 |
| 12 | `<src>中学生でも。</src><tgt>像梵高、高更、塞尚、雷诺阿他们的画，连乡下的中学生都……</tgt>` | `<src>中学生</src><tgt>这些人的画，</tgt>` | 876 |

---

### Test Example 16 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 870 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | 849 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>いろんな場面で</src><tgt>In movies,</tgt>` | 1105 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1166 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに</src><tgt><\|wait\|></tgt>` | 793 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあ映画の乱交を</src><tgt>when you're checking if a movie is alive in various situations,</tgt>` | 1624 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べることで、あの</src><tgt><\|wait\|></tgt>` | 1327 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1948 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>示すする</src><tgt>you can show whether it's alive by checking its habitat.</tgt>` | 2235 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>生息であることが保証する</src><tgt><\|wait\|></tgt>` | 1966 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1810 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>使い方をされます。</src><tgt>That's how it's used.</tgt>` | 1113 |

---

### Test Example 17 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1257 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 1052 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离在慢慢拉开，</tgt>` | 1403 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>おしゃれルカダがね、</src><tgt><\|wait\|></tgt>` | 1376 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | 1256 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>海遊したい方って</src><tgt>おしゃれ的Luca的人确实挺多的。想去海游的人</tgt>` | 1759 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい行き来おきいのが</src><tgt><\|wait\|></tgt>` | 1881 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 1592 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>一日で見て</src><tgt>真的会来回往。</tgt>` | 847 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>多分一日で</src><tgt><\|wait\|></tgt>` | 1788 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>と思うから強いので、</src><tgt><\|wait\|></tgt>` | 1861 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので。</src><tgt>因为大概一天就能看完了，所以……</tgt>` | 1213 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 835 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1372 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt>If a high school girl</tgt>` | 1201 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1244 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src><\|wait\|></src><tgt>has some kind of connection with someone with a strange appearance,</tgt>` | 1595 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>难道会是童年</src><tgt><\|wait\|></tgt>` | 1717 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 843 |
| 9 | `<src><\|wait\|></src><tgt>Could it have started that night?</tgt>` | `<src>夜里开始的？</src><tgt>could it be that it started in the night of her childhood?</tgt>` | 1778 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1863 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子</src><tgt><\|wait\|></tgt>` | 1851 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>思绪连篇，</src><tgt>Yangzi's thoughts were racing,</tgt>` | 1244 |

---

### Test Example 19 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツ</src><tgt><\|wait\|></tgt>` | 1129 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>などが</src><tgt><\|wait\|></tgt>` | 1147 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あのいただもらえる</src><tgt>You can get things like T- shirts,</tgt>` | 1375 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt><\|wait\|></tgt>` | 1362 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>ので、ぜひ</src><tgt><\|wait\|></tgt>` | 1327 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ご参加ください。</src><tgt>and other items. So please do join us.</tgt>` | 1785 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1642 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりますし、</src><tgt><\|wait\|></tgt>` | 1413 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>えっと</src><tgt>That's all for the contact information,</tgt>` | 1008 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ご不明な点が</src><tgt><\|wait\|></tgt>` | 1891 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>ありましたら内窓がありますので、</src><tgt><\|wait\|></tgt>` | 1898 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>お越しお待ちください。</src><tgt>and if you have any questions, we have an indoor window, so please come by.</tgt>` | 1549 |

---

### Test Example 20 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 971 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 </src><tgt><\|wait\|></tgt>` | 1372 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주겨 달라 이거 주고 내가 </src><tgt>He asked for another massage, gave it to me,</tgt>` | 1702 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>주질 못하 므로 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1616 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 516 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>다른 잔찜을 주겨 달라 </src><tgt>and I couldn't give it to him, so I came in.</tgt>` | 1997 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았느냐. 내가 </src><tgt><\|wait\|></tgt>` | 1750 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 2012 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>있는 줄 알느냐? </src><tgt>Didn't he ask for another massage? Did he think I wasn't listening?</tgt>` | 2348 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1307 |

---

### Test Example 21 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 896 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1874 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>인슐린과 </src><tgt>Vanadium and these things are almost like insulin</tgt>` | 1331 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 742 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1282 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 </src><tgt>in terms of action.</tgt>` | 1600 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1722 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1079 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt>They are called ' diabetes minerals '.</tgt>` | 1354 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1872 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1888 |
| 12 | `<src>그거 에다가 </src><tgt>you could call them diabetes minerals. And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt>That's what I mean. And then,</tgt>` | 1103 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1122 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 1168 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src><\|wait\|></src><tgt>그렇습니다. 그래서</tgt>` | 1153 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>テキという施設を</src><tgt><\|wait\|></tgt>` | 1534 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>集めましたね。</src><tgt><\|wait\|></tgt>` | 1331 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>で、</src><tgt>테키라는 시설을 모았죠. 그리고</tgt>` | 1677 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1728 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | 1214 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>나가이 케이요시 씨의</tgt>` | 1305 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>は冒険、</src><tgt><\|wait\|></tgt>` | 1930 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1880 |
| 12 | `<src>設備寺、五比</src><tgt>파생 형용사의 구조는 어근, 접미사, 어미로</tgt>` | `<src>施設集ごび</src><tgt>구조는 모험, 시설 집</tgt>` | 1310 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 841 |

---

### Test Example 23 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 805 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到我</src><tgt><\|wait\|></tgt>` | 1228 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活的一个轨道，</src><tgt>제 삶의 궤도로 돌아가게 해줘요.</tgt>` | 1724 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 882 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1289 |
| 6 | `<src>在他下班的时候，</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>好在他下班的时候，</src><tgt>퇴근하고</tgt>` | 1497 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1120 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>在工作和锻炼的时候，所以</src><tgt><\|wait\|></tgt>` | 1248 |
| 9 | `<src><\|wait\|></src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src><\|wait\|></src><tgt>일하고 운동할 수 있게 해줘요. 그래서</tgt>` | 2060 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>们我当时背对穿着</src><tgt><\|wait\|></tgt>` | 2092 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的幽梦哈，</src><tgt><\|wait\|></tgt>` | 2011 |
| 12 | `<src>哈。</src><tgt>그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src><\|wait\|></src><tgt>그때는 등 돌린 채 작은 꿈을 꾸고 있었어요.</tgt>` | 1860 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 892 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 1621 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼, 화학 결합은</tgt>` | 1668 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>also store energy. </src><tgt><\|wait\|></tgt>` | 844 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>And when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1247 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>에너지도 저장합니다. 그리고 그 결합이 끊어지면, 그 잠재 에너지가</tgt>` | 2252 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1213 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 2078 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>열이나 빛 같은 다른 에너지 형태로 변환됩니다.</tgt>` | 1910 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It gets </src><tgt><\|wait\|></tgt>` | 1366 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>used to make </src><tgt><\|wait\|></tgt>` | 1015 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>이 에너지는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1880 |

---

### Test Example 25 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1164 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1231 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアです。ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | 1591 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | 1068 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなってしまう</src><tgt><\|wait\|></tgt>` | 1356 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>ので、</src><tgt>느슨해지면 심이 위아래로 움직이지 않게 되니까,</tgt>` | 1774 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1729 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1702 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>ヤクネ字のナットが</src><tgt>기어 끝에 쇠붙이 너트가</tgt>` | 1046 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いている</src><tgt><\|wait\|></tgt>` | 1700 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>っていうことですね。</src><tgt><\|wait\|></tgt>` | 1818 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>달려 있다는 뜻이죠.</tgt>` | 1266 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>歯一番力</src><tgt><\|wait\|></tgt>` | 910 |

---

### Test Example 26 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1138 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment, </src><tgt>제19조 수정헌법의 의미는</tgt>` | 1761 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 977 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1315 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to how political </src><tgt>어떻게</tgt>` | 1605 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1694 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 862 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 일어날 수 있는지에 대한 역사적 안내서입니다.</tgt>` | 1974 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1765 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1849 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>수정헌법의 의미는 물론</tgt>` | 1530 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>are Miriam. </src><tgt><\|wait\|></tgt>` | 774 |

---

### Test Example 27 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kiran Patel. </src><tgt><\|wait\|></tgt>` | 1361 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>I am currently studying </src><tgt>제 이름은 키란 파텔입니다. 현재</tgt>` | 1514 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in </src><tgt><\|wait\|></tgt>` | 932 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>business and finance </src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of psychology. </src><tgt>경영 및 금융학을 전공하고 있으며, 심리학 학사 학위를 받았습니다.</tgt>` | 1947 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1636 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 1844 |
| 9 | `<src><\|wait\|></src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src><\|wait\|></src><tgt>여기 예일에서</tgt>` | 666 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | 2044 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1842 |
| 12 | `<src>corporate consultancy. </src><tgt>밟고 있고요, 앞으로는 기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consulting. </src><tgt>배우고 있습니다. 그리고 장래에는 기업 컨설팅 분야로 가고 싶습니다.</tgt>` | 2066 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 1016 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 1065 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>あるいは、何かを文書で作成しなければならない場合、</tgt>` | 1391 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1351 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1300 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know how </src><tgt>文章を書く、</tgt>` | 1583 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1645 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like, oh, </src><tgt><\|wait\|></tgt>` | 1005 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt>単語の綴りさえわからないことに気づく。まるで「あ、この単語は</tgt>` | 1904 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a </src><tgt><\|wait\|></tgt>` | 1888 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>double p, </src><tgt><\|wait\|></tgt>` | 1805 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double lam? I don't </src><tgt>pが二つ、lが二つで綴られているの？」</tgt>` | 1738 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 823 |

---

### Test Example 29 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 909 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是能源物资</src><tgt><\|wait\|></tgt>` | 1297 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>二级以上</src><tgt>2つ目は、エネルギー物資の2級以上</tgt>` | 1520 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>并服务</src><tgt><\|wait\|></tgt>` | 1040 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1312 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>で、1級の最前線で戦っている大牛たちを支援することです。</tgt>` | 2071 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 1503 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1651 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>在做未静运动抗击疫情期间，你会</src><tgt>例えば、未静運動でパンデミックと戦っている間、</tgt>` | 1283 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1546 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>发现给未静运动</src><tgt><\|wait\|></tgt>` | 1985 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>公平的新榜</src><tgt>未静運動に公平な新しい</tgt>` | 1521 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反之效果了。</src><tgt><\|wait\|></tgt>` | 917 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 933 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 1171 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src><\|wait\|></src><tgt>이 부분은</tgt>` | 1025 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>一个在跳舞的人，但是</src><tgt><\|wait\|></tgt>` | 1551 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于逆向的</src><tgt><\|wait\|></tgt>` | 1369 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src><\|wait\|></src><tgt>춤추는 사람을 보여주는데, 역방향으로</tgt>` | 1775 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这种采用这样的一个状况的</src><tgt><\|wait\|></tgt>` | 1817 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>摄像就要去</src><tgt><\|wait\|></tgt>` | 1694 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>特别注意的是，</src><tgt>촬영할 때는 특별히 주의해야 합니다.</tgt>` | 828 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能够</src><tgt><\|wait\|></tgt>` | 1845 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到于他</src><tgt><\|wait\|></tgt>` | 1817 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>吊不到</src><tgt>그가</tgt>` | 1168 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>于你的意识</src><tgt><\|wait\|></tgt>` | 938 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt><\|wait\|></tgt>` | 1239 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1047 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>要提醒大家呢，</src><tgt><\|wait\|></tgt>` | 1530 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>皆さんに注意していただきたいのですが、このローマでは、</tgt>` | 1690 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 667 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>最终呢，</src><tgt><\|wait\|></tgt>` | 1305 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src>你现在所</src><tgt>今、</tgt>` | 1521 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1594 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>面临的一些遗迹啊、</src><tgt><\|wait\|></tgt>` | 836 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>跟风景</src><tgt>あなたが直面している遺跡や風景が、最終的に</tgt>` | 1919 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你市之间</src><tgt><\|wait\|></tgt>` | 1936 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1860 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src>就演变出来</src><tgt>あなたの街と</tgt>` | 1091 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因此会建议</src><tgt><\|wait\|></tgt>` | 1139 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>这对的朋友呢。</src><tgt><\|wait\|></tgt>` | 1260 |

---

### Test Example 32 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>我当时一切正常，</src><tgt><\|wait\|></tgt>` | 1363 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>活蹦乱跳，</src><tgt>I was doing great back then— everything was normal, I was full of energy,</tgt>` | 2124 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1201 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀。</src><tgt><\|wait\|></tgt>` | 532 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>期间</src><tgt>so I insisted on not having the surgery. During that time,</tgt>` | 1657 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>大概由村卫医生来</src><tgt><\|wait\|></tgt>` | 1895 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>判断，</src><tgt><\|wait\|></tgt>` | 1791 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>以下腰腿</src><tgt>it was the village doctor who made the call. The doctor said</tgt>` | 803 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>已达到阈值，</src><tgt><\|wait\|></tgt>` | 1831 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1903 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>that my hips and legs had reached the threshold, so there was no problem at all. They were all</tgt>` | 2120 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>愉快地离开。</src><tgt><\|wait\|></tgt>` | 1162 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 812 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | 1623 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>如果你</src><tgt>良い兆しが訪れたら、</tgt>` | 846 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1349 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src><\|wait\|></src><tgt>その兆しを得た後は、必ず</tgt>` | 1483 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1514 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | 919 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src><\|wait\|></src><tgt>守り抜いてください。そうして「あ、</tgt>` | 1958 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>继续操作下去哦，</src><tgt><\|wait\|></tgt>` | 1979 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1853 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>じゃあ、操作を続けよう」なんて考えないでください。なぜそう言うのかというと、</tgt>` | 1799 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 895 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 888 |

---

### Test Example 34 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一、</src><tgt><\|wait\|></tgt>` | 1116 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>二手にとかでした。おそらく</src><tgt>应该是十一、二手之类的。</tgt>` | 1233 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 1446 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1308 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>一秒に</src><tgt>大概十秒，嗯，</tgt>` | 1292 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 603 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間が</src><tgt><\|wait\|></tgt>` | 1701 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>あるんですね。</src><tgt>有一秒左右的时间。</tgt>` | 1434 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 844 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1758 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src>十一、</src><tgt>然后大概</tgt>` | 624 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>二手にで</src><tgt><\|wait\|></tgt>` | 1888 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1430 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>宮内馬とかが</src><tgt>十一、二手，那个宫内马之类的</tgt>` | 1122 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>あるから。</src><tgt><\|wait\|></tgt>` | 737 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 840 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150미가 종업었을 </src><tgt><\|wait\|></tgt>` | 1795 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>연령 미만 으로 </src><tgt>その中で150ミリが</tgt>` | 1155 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1047 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1178 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>創業から150ミリ未満の、非常に小さな企業が多くありました。一般的には、</tgt>` | 2011 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1666 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 혹은 </src><tgt><\|wait\|></tgt>` | 2067 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>폐업해 있기도 한데 </src><tgt>小さな企業は成長したり、あるいは廃業したりすることもありますが、</tgt>` | 2241 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>일본 회선 </src><tgt><\|wait\|></tgt>` | 1837 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업들은 </src><tgt><\|wait\|></tgt>` | 1257 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>日本の小企業は成長も廃業もせず、</tgt>` | 1282 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들이 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1015 |

---

### Test Example 36 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1117 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src>there were </src><tgt>没什么新鲜事，</tgt>` | 1129 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such interfaces before. </src><tgt><\|wait\|></tgt>` | 1510 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>Netfilter, TC, </src><tgt>以前就有这样的接口。Netfilter、TC、</tgt>` | 1752 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1721 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>and so this is </src><tgt><\|wait\|></tgt>` | 1280 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>just one another place </src><tgt>还有</tgt>` | 1071 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 1788 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 751 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt>一个地方来看。这就是</tgt>` | 1772 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>But developers or engineers would </src><tgt><\|wait\|></tgt>` | 1572 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>expect the kernel modules </src><tgt><\|wait\|></tgt>` | 1007 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>to be available of that. </src><tgt>开发者或工程师会期待内核模块能提供这些东西。</tgt>` | 974 |

---

### Test Example 37 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 868 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1514 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>이방인으로 </src><tgt>あなたたちも知っているだろう。あなたたちが異邦人として</tgt>` | 1687 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 823 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1171 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>いたとき、言葉を持たない偶像に</tgt>` | 1529 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1722 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 973 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src><\|wait\|></src><tgt>引き寄せられていったのだ。</tgt>` | 1570 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1816 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 1080 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>だから、私があなたたちに知らせる。そして、</tgt>` | 1689 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1459 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 1287 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>神の霊によって語る者は……</tgt>` | 968 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1168 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1092 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>needs to get </src><tgt>これから始める人たちは、</tgt>` | 1153 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1481 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1395 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really </src><tgt>本当に</tgt>` | 1532 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1637 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 702 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go into </src><tgt>大事なことなんです。10個あります。</tgt>` | 2058 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1887 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>a about one minute videos </src><tgt><\|wait\|></tgt>` | 1831 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at the fall this video </src><tgt>この動画で1分程度の動画をいくつか見て、</tgt>` | 1388 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | 1027 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1173 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, </src><tgt>それぞれ詳しく解説します。</tgt>` | 1147 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 990 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1470 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>很不错的，但是</src><tgt>金運については、今月はかなり良いと言えます。ただ、</tgt>` | 1798 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 710 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正财的部分，也就是</src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>在事业方面的</src><tgt>正財、つまり仕事面では、</tgt>` | 1563 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长所带来的红利，</src><tgt><\|wait\|></tgt>` | 1898 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>与收入的</src><tgt><\|wait\|></tgt>` | 2061 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>提升，</src><tgt>業績向上による恩恵や収入の増加といった面が</tgt>` | 1610 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果涉及到投资理财方面呢，</src><tgt><\|wait\|></tgt>` | 783 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1800 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>強いですが、投資や資産運用に関しては、今月も良いでしょう。ただ、</tgt>` | 1849 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对正财来说，</src><tgt><\|wait\|></tgt>` | 1345 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | 690 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src><\|wait\|></src><tgt>正財に比べると少し弱めです。</tgt>` | 785 |

---

### Test Example 40 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 827 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>어 Htielmei, </src><tgt><\|wait\|></tgt>` | 1383 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt>呃，</tgt>` | 902 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 컴피트어도 </src><tgt><\|wait\|></tgt>` | 1553 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1322 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src><\|wait\|></src><tgt>像Htielmei这样的竞争者也是可以理解的，</tgt>` | 1622 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1914 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴피트의 언어 에 </src><tgt><\|wait\|></tgt>` | 1725 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src><\|wait\|></src><tgt>也是人们能理解的竞争语言，</tgt>` | 891 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 을 알기에 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1923 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1840 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>조건 을 작성 해야 되는데 </src><tgt>因为我们了解其语法，所以需要设定条件，</tgt>` | 1680 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 895 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>그 조건 을 작성 하는 </src><tgt><\|wait\|></tgt>` | 922 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src>프로그램 이 필요 합니다. </src><tgt>所以需要一个程序来设定这些条件。</tgt>` | 1221 |

---

### Test Example 41 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어 어찌 보면 </src><tgt><\|wait\|></tgt>` | 1219 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>가장 20대를 </src><tgt>嗯，怎么说呢，</tgt>` | 1370 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1244 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1400 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt>他就是和我们一起走过二十岁的那个弟弟，也是</tgt>` | 1775 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>같은 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1806 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1742 |
| 9 | `<src><\|wait\|></src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src><\|wait\|></src><tgt>家人，毕竟是亲弟弟。所以</tgt>` | 784 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | 1880 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1836 |
| 12 | `<src>자기 스스로 </src><tgt>比起责任感，</tgt>` | `<src>자기 스스로 </src><tgt>比起责任感，</tgt>` | 1311 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 802 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것 </src><tgt><\|wait\|></tgt>` | 1231 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>他更倾向于靠自己，</tgt>` | 1053 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 566 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1258 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>How far did you </src><tgt>학력 수준. 당신은</tgt>` | 1103 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1412 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 1368 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>실제로 학업을 얼마나 마쳤나요? 고등학교를 졸업했나요?</tgt>` | 2113 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt><\|wait\|></tgt>` | 1614 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>of attainment. </src><tgt><\|wait\|></tgt>` | 2048 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>그것이 한 단계의 학력 수준입니다. 대학에 다녔나요?</tgt>` | 1817 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And did you graduate? </src><tgt><\|wait\|></tgt>` | 805 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level </src><tgt><\|wait\|></tgt>` | 1718 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>of attainment. </src><tgt>그리고 졸업했나요? 그것이 또 다른 단계의 학력 수준입니다.</tgt>` | 2031 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1150 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. </src><tgt><\|wait\|></tgt>` | 930 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>I'll see you online. </src><tgt>자, 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 840 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1192 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 846 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>색인 모를 때가 </src><tgt>目を閉じて、色を認識できない時が</tgt>` | 1426 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1370 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>소름 이 돋는 카타르 도뿐 때, </src><tgt><\|wait\|></tgt>` | 1473 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 오면 </src><tgt>ある、その時、鳥肌が立つような感覚が来る時、その感覚が</tgt>` | 1642 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1747 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 900 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src><\|wait\|></src><tgt>来る時、それを揺らして一緒に遊ぼうっていうことなんだ。</tgt>` | 1743 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 물릴 거고 </src><tgt><\|wait\|></tgt>` | 2087 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>시눈 이 오면 </src><tgt><\|wait\|></tgt>` | 2024 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>너 찢겨 들어 고 </src><tgt>鬼が来たら噛みつき、目が見たら引き裂いて、</tgt>` | 2064 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주려 하니까 </src><tgt><\|wait\|></tgt>` | 1160 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 1132 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>刺そうとするから、リラックスして目を閉じて。</tgt>` | 894 |

---

### Test Example 44 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1116 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう寝かせている。</src><tgt><\|wait\|></tgt>` | 1230 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>俺は</src><tgt>그럼 이미 재우고 있어. 나는</tgt>` | 1287 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1324 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>今一日を</src><tgt><\|wait\|></tgt>` | 1320 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>오늘 하루를</tgt>` | 1571 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1547 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 721 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>遠くに越えているふれば、潔き。</src><tgt>이미 한계는 멀리 지나갔어. 그렇다면, 깔끔하게.</tgt>` | 2347 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1867 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1849 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>流れのぶなでいくを</src><tgt>흐름에 몸을 맡기는 걸</tgt>` | 1648 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 805 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt><\|wait\|></tgt>` | 1004 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>오랫동안 배를 만들어왔지만, 이렇게 대단한 해적선은</tgt>` | `<src>海賊船を見た</src><tgt>하고 있어. 나는 이렇게 대단한 해적선을</tgt>` | 1205 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 787 |

---

### Test Example 45 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1184 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1156 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 해맨입니다. </src><tgt>进入的话，非常难。</tgt>` | 1227 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이 운전 을 할 거는 </src><tgt><\|wait\|></tgt>` | 1487 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1305 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>거러 거로 다니 고는. 뭐 </src><tgt>开车的话，还是开这个。</tgt>` | 1892 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1736 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1797 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가 면 또 </src><tgt>去江南的话，更是难说，出国的话，</tgt>` | 880 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. </src><tgt><\|wait\|></tgt>` | 1735 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 시간 이 </src><tgt><\|wait\|></tgt>` | 1884 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>也是很艰难。时间的话，</tgt>` | 1560 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 761 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>무뤄봐요. 그거 는 </src><tgt><\|wait\|></tgt>` | 1099 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>잘한 것 같아요. </src><tgt>不如现在努力工作吧。我觉得那部分做得不错。</tgt>` | 1204 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 896 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1175 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index is showing an upward trend,</tgt>` | 1823 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 개형주도 </src><tgt><\|wait\|></tgt>` | 1068 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1044 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt>these small- cap stocks will also rise sharply,</tgt>` | 1798 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1711 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1613 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt>but first, these lighter stocks</tgt>` | 967 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1781 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 2152 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src><\|wait\|></src><tgt>move the market first,</tgt>` | 1469 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 역시 초기 </src><tgt><\|wait\|></tgt>` | 847 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목을 </src><tgt><\|wait\|></tgt>` | 978 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨봐야 될 것 </src><tgt>so you should always keep an eye on the initial lighter stocks.</tgt>` | 1338 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | 831 |

---

### Test Example 47 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1497 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>というだけではなくて、</src><tgt>And this is not just a visual development environment,</tgt>` | 1460 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 882 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのも</src><tgt>it's a visual Python development environment.</tgt>` | 1551 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルの</src><tgt><\|wait\|></tgt>` | 1804 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いたあと、それに対しては</src><tgt><\|wait\|></tgt>` | 1746 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードが</src><tgt>Because after writing a FlowGraph in Visual Graph,</tgt>` | 882 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成されて、それが</src><tgt><\|wait\|></tgt>` | 1898 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1945 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt>Python code is generated for it, and that code is executed to perform signal processing.</tgt>` | 2065 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 1180 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 946 |
| 15 | `<src>はい。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>はい。</src><tgt>That's the structure it's built on. Yes.</tgt>` | 697 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | 665 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계속 뭐 </src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>물론 이제 </src><tgt><\|wait\|></tgt>` | 788 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt>もちろん、こういうケースもあります。私たちが</tgt>` | 1488 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1496 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>서로 컨설턴트 예요. </src><tgt>AさんとBさんがコンサルタントで、お互いに</tgt>` | 1801 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 컨설턴트가 </src><tgt><\|wait\|></tgt>` | 1889 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>오고 </src><tgt><\|wait\|></tgt>` | 1615 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>コンサルタントとして来て、Aさんが</tgt>` | 916 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1904 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1892 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>비난 하는 사람 이 </src><tgt>悪性コードを与えたときに、それを非難する人が</tgt>` | 1777 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 956 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스사이트 CT에서 </src><tgt><\|wait\|></tgt>` | 733 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>EX 파일까지 </src><tgt>実際にクロスサイトCTでEXファイルまで</tgt>` | 1162 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 976 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1023 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1188 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt>活動、そして自分を定義すること。つまり、</tgt>` | 1776 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 900 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1473 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>自分にとっての基準とは何か、というものです。なぜなら、あなたは完全に正しいからです。</tgt>` | 1857 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is is that </src><tgt><\|wait\|></tgt>` | 1758 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 2059 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because </src><tgt>しかし、現実には、私たちは新しい子だからです。そして、</tgt>` | 2201 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt><\|wait\|></tgt>` | 1903 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1434 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>changed from twenty years ago, </src><tgt>基準は20年前に変わってしまったのです。</tgt>` | 966 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 959 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard </src><tgt><\|wait\|></tgt>` | 1055 |
| 15 | `<src>everything at this point is being </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything </src><tgt>すべてが</tgt>` | 600 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>at this point is being held to </src><tgt><\|wait\|></tgt>` | 633 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1087 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手的</src><tgt><\|wait\|></tgt>` | 1631 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>感情或</src><tgt>相手の感情や</tgt>` | 655 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | 1538 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1356 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt>真の意図を推し量ったり感じ取ったりすることです。</tgt>` | 1892 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>很多时候，</src><tgt><\|wait\|></tgt>` | 1703 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>经常会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 2162 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt>多くの場合、人々はよく次のように言います。</tgt>` | 1794 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你看，</src><tgt><\|wait\|></tgt>` | 614 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1758 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>又在说谎了。</src><tgt>「ほら、この人はまた嘘をついている」</tgt>` | 1783 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 959 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 702 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>彼の目はすべてを物語っている。</tgt>` | 1090 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | 791 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>你。</src><tgt><\|wait\|></tgt>` | 461 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 1503 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src>be able to </src><tgt>另外，你将无法</tgt>` | 849 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1411 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1336 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt>在资源之间移动媒体对象，</tgt>` | 1535 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1271 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 954 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>a situation </src><tgt>如果你遇到</tgt>` | 1735 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>where you realize </src><tgt><\|wait\|></tgt>` | 621 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | 1973 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource. </src><tgt>把错误的媒体文件添加到某个资源中。</tgt>` | 2167 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>In the last </src><tgt><\|wait\|></tgt>` | 1531 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 996 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src><\|wait\|></src><tgt>在上次的</tgt>` | 665 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure </src><tgt><\|wait\|></tgt>` | 1146 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 844 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>it gets backed up properly. </src><tgt>操作中，我们可以移动这些媒体文件，并确保它们能正确备份。</tgt>` | 636 |

---

### Test Example 52 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 776 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1381 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>분석 을 내놓았습니다. </src><tgt>そしてこれについて、多くの人が分析を提示しました。</tgt>` | 1827 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 658 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자 의 편집 설을 보시면 </src><tgt><\|wait\|></tgt>` | 1539 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ここで、このロクジャの編集説を見ると、ソニーが</tgt>` | 1674 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 60 뒤에 </src><tgt><\|wait\|></tgt>` | 1881 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPD 파이프를 </src><tgt><\|wait\|></tgt>` | 1998 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>2016年にFPDパイプを128ビットに</tgt>` | 2265 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮춘 것이 로프 인다. </src><tgt><\|wait\|></tgt>` | 2095 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1492 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>엑스 박스 시리즈, X에서도 없는 </src><tgt>下げたのがロフインです。Xboxシリーズ、Xでもない</tgt>` | 1592 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 923 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt><\|wait\|></tgt>` | 669 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>S2가 여기 도 없다. </src><tgt>インフィニットキャッシュ、S2もここにもない。</tgt>` | 946 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 409 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 845 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>佛陀一得</src><tgt><\|wait\|></tgt>` | 1352 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>阻止觉知到的那个现象，</src><tgt>부처님께서 깨달음을 막는 그 현상을</tgt>` | 2024 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 747 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>每当我们</src><tgt><\|wait\|></tgt>` | 1036 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>处于爱之中，</src><tgt>하나도 모를 때, 우리가 사랑 속에 있을 때,</tgt>` | 1798 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | 1737 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1630 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>我们也同时进入</src><tgt>소위 말하는 사랑도 동시에</tgt>` | 886 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1822 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨在场所的时候，</src><tgt><\|wait\|></tgt>` | 1970 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>它是不爱。</src><tgt>증오의 장소에 들어갑니다. 그때는 사랑이 아닙니다.</tgt>` | 1769 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 987 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，它就变成</src><tgt><\|wait\|></tgt>` | 794 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src><\|wait\|></src><tgt>밤이 되면, 그것은</tgt>` | 1070 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>恨那个钟摆，</src><tgt><\|wait\|></tgt>` | 847 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 455 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>继续在移动。</src><tgt>그 종을 증오하는 종이 되어 계속 움직입니다.</tgt>` | 511 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1299 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 1054 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section </src><tgt>第1セクションで少し混乱していました。</tgt>` | 1230 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1446 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the EHR </src><tgt><\|wait\|></tgt>` | 1345 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src>fields being of critical </src><tgt>EHRの項目が</tgt>` | 1522 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 825 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>importance versus, you know, </src><tgt><\|wait\|></tgt>` | 1501 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src><\|wait\|></src><tgt>重要性という話で、</tgt>` | 2010 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, which is obviously </src><tgt><\|wait\|></tgt>` | 1824 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1194 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src><\|wait\|></src><tgt>バリアントデータベース、つまり私が大好きで、もちろん</tgt>` | 1507 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | 1615 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1240 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>that need to be in these </src><tgt>好きなものの一つです。もし</tgt>` | 1179 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 677 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 523 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right？ </src><tgt>データソースに含めるべき項目について合意できなければ、そこから引き出すものはない、ですよね？</tgt>` | 845 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 307 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1220 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | 1148 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1449 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1084 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt>最高法院是最后才跟进的，而不是引领。</tgt>` | 915 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 1544 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1673 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>the the vanguard of </src><tgt>我不认为法院想成为</tgt>` | 1630 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 754 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days, </src><tgt><\|wait\|></tgt>` | 1820 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src><\|wait\|></src><tgt>社会变革的最前沿。如今，</tgt>` | 1927 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | 1006 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1117 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>the consensus </src><tgt>它们更多反映的是</tgt>` | 1019 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | 634 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 1009 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src><\|wait\|></src><tgt>已经形成的共识。</tgt>` | 809 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>you have some federal judges </src><tgt><\|wait\|></tgt>` | 527 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 392 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who. </src><tgt>所以，你有一些联邦法官，他们……</tgt>` | 560 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 843 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 1156 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>is a hungry, </src><tgt>ある時、彼はイエスが飢えていることを知っていました。</tgt>` | 1693 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows </src><tgt><\|wait\|></tgt>` | 945 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>that he's about to </src><tgt><\|wait\|></tgt>` | 1386 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>be in the wilderness </src><tgt>彼は、彼がまもなく</tgt>` | 1674 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days, that he's hungry, </src><tgt><\|wait\|></tgt>` | 1979 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he sends </src><tgt><\|wait\|></tgt>` | 2060 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>to Jesus. He said," </src><tgt>40日間荒野にいることを知っていました。彼は飢えていることを知っていました。だから、イエスに送ったのです。彼は言いました。</tgt>` | 2414 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>If you are the Son of God, </src><tgt><\|wait\|></tgt>` | 1989 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. Turn </src><tgt><\|wait\|></tgt>` | 1562 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>these stones to bread." </src><tgt>「もしあなたが神の御子なら、証明してみせろ。この石をパンに変えろ」と。</tgt>` | 1611 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1093 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>How did Jesus deal with </src><tgt><\|wait\|></tgt>` | 820 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>that temptation? </src><tgt>イエスは、その誘惑にどう対処したのでしょうか？</tgt>` | 597 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 353 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan </src><tgt><\|wait\|></tgt>` | 485 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>led by bread alone. </src><tgt>いやはや、ヨハネはパンだけで生きていました。</tgt>` | 517 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1366 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1122 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1358 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是</src><tgt><\|wait\|></tgt>` | 1291 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>客厅的部分，</src><tgt>사진 부분에는 거실이 보입니다.</tgt>` | 1763 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1784 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>它客厅一般都是</src><tgt><\|wait\|></tgt>` | 1722 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src><\|wait\|></src><tgt>거실은 보통</tgt>` | 798 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>属于我们在休息的</src><tgt><\|wait\|></tgt>` | 1864 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>地方，所以呢，</src><tgt><\|wait\|></tgt>` | 1945 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src><\|wait\|></src><tgt>우리가 쉬는 공간이라서,</tgt>` | 1436 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>是身体的部分呢，</src><tgt><\|wait\|></tgt>` | 825 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>反映的是你需要给自己</src><tgt><\|wait\|></tgt>` | 1142 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src><\|wait\|></src><tgt>몸의 부분은</tgt>` | 1017 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>一点时间可以</src><tgt><\|wait\|></tgt>` | 459 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>好好地坐下来休息，</src><tgt><\|wait\|></tgt>` | 855 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们可以看到这边是</src><tgt>잠시 앉아서 쉬면서 시간을 보내야 한다는 걸 보여줍니다. 그리고 여기는</tgt>` | 673 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的吗？</src><tgt><\|wait\|></tgt>` | 468 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 380 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>사람이 없는 곳이죠? 자, 그러니까...</tgt>` | 456 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 2.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 852 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1203 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>and they often </src><tgt>これらの人々は極めて稀で、</tgt>` | 1298 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1327 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1333 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>completely revolutionize the world </src><tgt>世界を完全に変革する</tgt>` | 1626 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1710 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>their personality is </src><tgt><\|wait\|></tgt>` | 879 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>something of a contradiction. </src><tgt>存在です。彼らの性格は矛盾に満ちています。</tgt>` | 1733 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1897 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1855 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的である一方で、</tgt>` | 1171 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1050 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | 1272 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src><\|wait\|></src><tgt>無意味な会話を嫌い、</tgt>` | 952 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to </src><tgt><\|wait\|></tgt>` | 641 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 798 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love to </src><tgt>要点を直接言いたいタイプです。また、</tgt>` | 582 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 404 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 327 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and they're never shy </src><tgt>悪魔の代弁者になるのも好きで、</tgt>` | 442 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>of a debate. </src><tgt><\|wait\|></tgt>` | 262 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 315 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src>ENTP </src><tgt>議論を避けることはありません。ENTPは</tgt>` | 394 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for. </src><tgt><\|wait\|></tgt>` | 282 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 886 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt><\|wait\|></tgt>` | 1636 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>거부 한 명령 이 후보 를 </src><tgt>Previously, Lee Jun- seok rejected the government's appointment of him as a candidate.</tgt>` | 1973 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1279 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 616 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>He said it was for the sake of the candidate's election,</tgt>` | 1596 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1758 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 2070 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt>and even put on quite a show for it. But now, Yoon Suk- yeol is</tgt>` | 1819 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 813 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1682 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석은 </src><tgt>removing Kim Jong- in,</tgt>` | 1567 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>더루내놓고 </src><tgt><\|wait\|></tgt>` | 982 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 768 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 뚜렷 이 </src><tgt>Lee Jun- seok is clearly determined to bring down Yoon Suk- yeol.</tgt>` | 1508 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>보겠다는 </src><tgt><\|wait\|></tgt>` | 660 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 성을 보이 기로 </src><tgt><\|wait\|></tgt>` | 472 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt>He is showing an aggressive stance</tgt>` | 416 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt><\|wait\|></tgt>` | 319 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 354 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석의 </src><tgt>and is set on doing so.</tgt>` | 436 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>성상 납건. </src><tgt><\|wait\|></tgt>` | 369 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 338 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 </src><tgt>Lee Jun- seok's image in the media. The opposition party's attack</tgt>` | 444 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 315 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 2.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1034 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂で</src><tgt><\|wait\|></tgt>` | 807 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってるみたいです。なので</src><tgt>Well, it looks like they're making it in the cafeteria right now. So,</tgt>` | 1592 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>ここで</src><tgt><\|wait\|></tgt>` | 1426 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>このロジェストンホテル</src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>も</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel</tgt>` | `<src>も</src><tgt>this Rogerstone Hotel</tgt>` | 1431 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 647 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1586 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になっているので、</src><tgt>is supposed to be a place where you can have breakfast, so</tgt>` | 2201 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 860 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>I'd like to stay at the Golden Stone Hotel here in the future.</tgt>` | 2074 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なっていう方はですね、</src><tgt><\|wait\|></tgt>` | 1364 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1259 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>まあいいんじゃないか</src><tgt>If you're considering it,</tgt>` | 939 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと、はい。</src><tgt><\|wait\|></tgt>` | 575 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>と思います。</src><tgt><\|wait\|></tgt>` | 797 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>ここのホテルからですね</src><tgt>I think it's a good option, so yes.</tgt>` | 522 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 323 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 387 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt>From this hotel, you can walk</tgt>` | 434 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 402 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんな辺りのね</src><tgt><\|wait\|></tgt>` | 376 |
| 24 | `<src>立地のいいねまあ</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good.</tgt>` | `<src>立地のいいねまあ</src><tgt>about a kilometer to Busan Station— it's a really convenient location.</tgt>` | 508 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>ホテルになってますので、</src><tgt><\|wait\|></tgt>` | 264 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 291 |
| 27 | `<src>ご検討なさってみて</src><tgt>If you'd like,</tgt>` | `<src>ご検討なさってみて</src><tgt>So if you're interested,</tgt>` | 216 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 196 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね、今回は。</src><tgt><\|wait\|></tgt>` | 185 |
