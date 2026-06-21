# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9582
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.4437
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 683
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 0.9310
  - TGT_RELEASE_TOTAL: 87
  - TGT_WAIT_ACCURACY: 0.9388
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1362.6620
  - PROCESS_TIME_MS_P50: 1348.1630
  - PROCESS_TIME_MS_P95: 2223.8870
  - PROCESS_TIME_MS_MAX: 9323.0080

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 888 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 956 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1279 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1399 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설스 용심이가 </src><tgt><\|wait\|></tgt>` | 1310 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 667 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt>Well, there's a mix of righteous intent and wicked intent in me. Wow,</tgt>` | 2373 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 993 |
| 9 | `<src>진짜 이거 </src><tgt>Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1871 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해형으로 </src><tgt><\|wait\|></tgt>` | 1996 |
| 11 | `<src>진짜. </src><tgt>seriously killer for a hangover, for real.</tgt>` | `<src>조금 쥐기 맞는 것 </src><tgt><\|wait\|></tgt>` | 474 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 905 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气鼠是容易的，</src><tgt>「気鼠」は簡単です。</tgt>` | 1808 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 1317 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>只有一个师傅</src><tgt>でも、</tgt>` | 978 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>指导道，</src><tgt><\|wait\|></tgt>` | 1092 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如波出于</src><tgt>師匠が一人しかいません。</tgt>` | 1643 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>终天，</src><tgt><\|wait\|></tgt>` | 1572 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt>波は終天に</tgt>` | 917 |
| 9 | `<src>虚阿凡</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1517 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt>出たので、反するのです。</tgt>` | 2135 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师傅，</src><tgt><\|wait\|></tgt>` | 483 |

---

### Test Example 3 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 716 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 1130 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into your body. </src><tgt><\|wait\|></tgt>` | 1543 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does </src><tgt>进入你的身体。你</tgt>` | 1064 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1363 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>的紧张感从哪里开始？是什么？</tgt>` | 1744 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1682 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？胸口紧吗？</tgt>` | 2100 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it </src><tgt><\|wait\|></tgt>` | 1742 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>a lump in your </src><tgt>还是</tgt>` | 672 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>using? </src><tgt><\|wait\|></tgt>` | 1811 |

---

### Test Example 4 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 915 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>淘砂が終わった後、</tgt>` | 1420 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的冶炼轻呢</src><tgt><\|wait\|></tgt>` | 1556 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了。</src><tgt>内部の冶錬軽のエネルギーも衰弱します。</tgt>` | 1687 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 681 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>就停留在</src><tgt>そして、</tgt>` | 1362 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1630 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 835 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>运行状态，</src><tgt>比較的低エネルギーな稼働状態に留まります。</tgt>` | 1974 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1925 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>蚁居状态。</src><tgt>これがいわゆる「蟻居状態」です。</tgt>` | 2091 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1134 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>怪在嵩子寺里边，</src><tgt>It's all in the Songzi Temple.</tgt>` | 1814 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个游行也很大，</src><tgt><\|wait\|></tgt>` | 1488 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src><\|wait\|></src><tgt>The procession is huge too.</tgt>` | 1459 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 655 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt>And I'm on vacation</tgt>` | 1513 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶渊，</src><tgt><\|wait\|></tgt>` | 1641 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>with Tao Yuan,</tgt>` | 1636 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在那个</src><tgt><\|wait\|></tgt>` | 746 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2069 |
| 11 | `<src>仁儿。</src><tgt>this kind of walnut kernels.</tgt>` | `<src>这种和陶渊。</src><tgt>in that kind of... with Tao Yuan.</tgt>` | 2109 |

---

### Test Example 6 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 752 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1121 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>重复。学会重复。重复。</tgt>` | 1671 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1417 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>找到你擅长的地方，多做一些。</tgt>` | 1422 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And what you're not good </src><tgt><\|wait\|></tgt>` | 1406 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>at, get to people </src><tgt>你不太擅长的，</tgt>` | 1061 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 2004 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>找身边的人帮忙，</tgt>` | 2238 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and and tell the next time </src><tgt><\|wait\|></tgt>` | 2110 |

---

### Test Example 7 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>The people in the auspicious spots</tgt>` | 1124 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1400 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1435 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1709 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt>They are people who were selected randomly.</tgt>` | 1660 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 926 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1981 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교수 아들은 </src><tgt>The professor son who didn't know the truth</tgt>` | 2162 |

---

### Test Example 8 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is</tgt>` | 1584 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1226 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱</src><tgt><\|wait\|></tgt>` | 1147 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>浇水，</src><tgt>water them with our deep love,</tgt>` | 1222 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 1505 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>培育</src><tgt>fertilize them,</tgt>` | 1552 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心灵营养，</src><tgt><\|wait\|></tgt>` | 881 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>nurture their spiritual nourishment,</tgt>` | 1806 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>冷心等他</src><tgt><\|wait\|></tgt>` | 2107 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt>and wait patiently for them to grow up.</tgt>` | 2224 |

---

### Test Example 9 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 694 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 938 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1261 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>孩子还是小学一年级呢。</tgt>` | 1557 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1360 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう身近く</src><tgt>就在那个时候，</tgt>` | 1438 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>算定を</src><tgt><\|wait\|></tgt>` | 1348 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対図して</src><tgt><\|wait\|></tgt>` | 990 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>やってあげると</src><tgt>如果能提前算好身处，</tgt>` | 2050 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 2085 |
| 11 | `<src>大した。</src><tgt>十年后也不会有什么大……</tgt>` | `<src>大した。</src><tgt>十年后还是挺不错的。</tgt>` | 2295 |

---

### Test Example 10 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 789 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Abbotrol, </src><tgt>I'm Abbotrol,</tgt>` | 1180 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축발시키고 </src><tgt><\|wait\|></tgt>` | 1432 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1158 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1384 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt><\|wait\|></tgt>` | 1444 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>페르나아. </src><tgt>and I'm the one who cast him out and killed his own father, Fernan.</tgt>` | 2208 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1829 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 1314 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt>The same generation as Park Chan</tgt>` | 1319 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 2215 |

---

### Test Example 11 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个</src><tgt><\|wait\|></tgt>` | 804 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>情况，我们就是</src><tgt>Facing this situation,</tgt>` | 1058 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1317 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>we just quickly report it to our supervisor.</tgt>` | 1727 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1108 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们学校这个状况，</src><tgt>Or we notify the school about the situation.</tgt>` | 1833 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1554 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't think you have to handle everything yourself.</tgt>` | 2090 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>抗不起了，</src><tgt><\|wait\|></tgt>` | 1933 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>不离成本，</src><tgt>You can't carry it all alone, and it's not free.</tgt>` | 752 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>资金就是</src><tgt><\|wait\|></tgt>` | 2313 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 815 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt>重要な研究を</tgt>` | 904 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt><\|wait\|></tgt>` | 1247 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>extremely happy people. This is </src><tgt>極度に幸せな人々について行いました。</tgt>` | 1680 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1323 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>これは先端的な研究です。</tgt>` | 1709 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 1685 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt>最も幸せな</tgt>` | 1949 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 795 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people that </src><tgt>人々を10%見ると、</tgt>` | 1914 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 2447 |

---

### Test Example 13 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 965 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这附近开始，</tgt>` | 1075 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1204 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>我才开始的，</tgt>` | 1450 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴゴ号、</src><tgt><\|wait\|></tgt>` | 1443 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt>比如“ゴゴ号”、“ゴー根”</tgt>` | 1638 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1573 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザム、</src><tgt>和“セザム”，</tgt>` | 1098 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1491 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt>还有</tgt>` | 2042 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1191 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt>田里中学生</tgt>` | 1565 |

---

### Test Example 14 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1046 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 942 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただこうもらう</src><tgt><\|wait\|></tgt>` | 1415 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt>We also have items like T- shirts available for you to take home.</tgt>` | 2243 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 617 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt>So please come and join us.</tgt>` | 1710 |
| 7 | `<src>ご連絡としては</src><tgt>so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt>That's all for the contact information.</tgt>` | 1654 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>て、</src><tgt><\|wait\|></tgt>` | 822 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt>Um,</tgt>` | 2030 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>ランチの案内があります</src><tgt><\|wait\|></tgt>` | 863 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ので、少々お待ちください。</src><tgt>we have a lunch announcement, so please wait a moment.</tgt>` | 2048 |

---

### Test Example 15 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>またまたちょっと</src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>距離が離れてくる</src><tgt>又又，</tgt>` | 1010 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1264 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>大将が</src><tgt>大将好像有点疏远了，</tgt>` | 1536 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>ある方多いですね。</src><tgt><\|wait\|></tgt>` | 1396 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>海老したい方って</src><tgt>好像很多人想去海老。</tgt>` | 1712 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行きに行き出したが</src><tgt><\|wait\|></tgt>` | 1711 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>いや</src><tgt>但</tgt>` | 1505 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ジュレで見て</src><tgt><\|wait\|></tgt>` | 928 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>ととこに</src><tgt>我刚想去，</tgt>` | 2060 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>おととしゃぐこれが強いので</src><tgt><\|wait\|></tgt>` | 2061 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt>结果在路边看到一个很强壮的家伙，</tgt>` | 1042 |

---

### Test Example 16 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 854 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 를 </src><tgt><\|wait\|></tgt>` | 997 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주겨 달라 해가지고 내가 </src><tgt>They asked me to give them another party,</tgt>` | 2137 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>주길 수 있도록 </src><tgt><\|wait\|></tgt>` | 1167 |
| 5 | `<src>다른 잔찜에 </src><tgt>came in here to do it.</tgt>` | `<src>하도노아스다. 다른 잔치 </src><tgt>so I could give it to them. It's</tgt>` | 1517 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>해주길 </src><tgt><\|wait\|></tgt>` | 970 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>때려야 되나? 내가 </src><tgt>like, should I give them another party? I</tgt>` | 2014 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 2014 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주자 는야. </src><tgt>don't hear any noise, you know.</tgt>` | 2280 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2293 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 944 |

---

### Test Example 17 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 767 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If you're a female high school student</tgt>` | 1771 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1508 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间有着某种</src><tgt><\|wait\|></tgt>` | 1415 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>联系，</src><tgt>and you have some kind of connection with someone who's a bit weird,</tgt>` | 1591 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 896 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>could it be</tgt>` | 1358 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天涯里开始的？</src><tgt><\|wait\|></tgt>` | 2005 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>something that started from the edge of the world?</tgt>` | 1592 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 940 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt>Yangzi's thoughts</tgt>` | 2219 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇，</src><tgt><\|wait\|></tgt>` | 1042 |

---

### Test Example 18 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 788 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAアンデスに</src><tgt><\|wait\|></tgt>` | 1199 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>それならば</src><tgt><\|wait\|></tgt>` | 1181 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>メインで生息過どうかっていうの</src><tgt><\|wait\|></tgt>` | 1505 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに</src><tgt><\|wait\|></tgt>` | 1298 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAAの乱交を</src><tgt><\|wait\|></tgt>` | 1512 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1496 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息過どうかっていうの</src><tgt><\|wait\|></tgt>` | 1048 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>調査する</src><tgt><\|wait\|></tgt>` | 1611 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>生息調査のことを保証する</src><tgt><\|wait\|></tgt>` | 2159 |
| 11 | `<src>といったような</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1187 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt>So, when you're looking into AA Andes, you can use it to check the main distribution and then use it to check the distribution— that's what it's used for.</tgt>` | 2968 |

---

### Test Example 19 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 800 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼 늘어난</tgt>` | 1480 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 1094 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy. And when those </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | 1902 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 821 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 결합이 끊어지면,</tgt>` | 1703 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1492 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>그 위치 에너지는</tgt>` | 1792 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 812 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>열이나 빛 같은 다른 에너지로 바뀌게 됩니다.</tgt>` | 2103 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 2246 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1696 |

---

### Test Example 20 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 805 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>就是问子二</src><tgt>2つ目は、</tgt>` | 865 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>师堂，</src><tgt><\|wait\|></tgt>` | 1195 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>还服务</src><tgt>子二師堂です。また、</tgt>` | 1363 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1338 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>一級一线で戦う大牛たちも支援しています。</tgt>` | 1586 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 896 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做维信</src><tgt>例えば、</tgt>` | 1357 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好事几点，</src><tgt><\|wait\|></tgt>` | 1754 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>維信コミュニケーションの好事几点をする時、</tgt>` | 1000 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维信做和平分的</src><tgt><\|wait\|></tgt>` | 1802 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>新棒，</src><tgt>維信の平和分立新棒が</tgt>` | 2552 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1734 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうですよ。</src><tgt><\|wait\|></tgt>` | 842 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>맞아요. 거기서</tgt>` | 1026 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天国</src><tgt><\|wait\|></tgt>` | 1322 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>という施設</src><tgt>천국이라는 시설이</tgt>` | 1378 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>がありましたね。</src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>で、</src><tgt>있었죠. 그런데</tgt>` | 1482 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1395 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井英雄氏の仕組み</src><tgt>나가이 히데오 씨의</tgt>` | 1272 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1520 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>冒険</src><tgt>시스템은</tgt>` | 2160 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 959 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>施設、</src><tgt>모험 시설,</tgt>` | 1738 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビース。</src><tgt><\|wait\|></tgt>` | 1861 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 700 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt><\|wait\|></tgt>` | 969 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活的一个</src><tgt><\|wait\|></tgt>` | 1266 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt>제 삶의 궤도로 돌아가게 해줘요.</tgt>` | 1839 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够哈</src><tgt><\|wait\|></tgt>` | 1098 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在它下面的时候，</src><tgt>그 아래에 있을 때,</tgt>` | 1698 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1621 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭给人家吃，</src><tgt>사람들에게 뜨거운 국과 밥을 대접하고,</tgt>` | 2080 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就那么</src><tgt><\|wait\|></tgt>` | 1059 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>备好这些</src><tgt>그렇게 준비해 두면</tgt>` | 1503 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的愿望哈，</src><tgt><\|wait\|></tgt>` | 2437 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src><\|wait\|></src><tgt>작은 소망 하나를 이루는 거죠.</tgt>` | 1949 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 848 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Shiranatori Go. </src><tgt>제 이름은 시라나토리 고입니다.</tgt>` | 1801 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1487 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src><\|wait\|></src><tgt>현재</tgt>` | 1218 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>a business background finance </src><tgt><\|wait\|></tgt>` | 825 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of psychology </src><tgt>경영학 전공과 심리학 학사 학위를</tgt>` | 2314 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 972 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at Yuen. </src><tgt>여기 유엔에서 공부하고 있습니다.</tgt>` | 2013 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And in the </src><tgt><\|wait\|></tgt>` | 1445 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>앞으로는</tgt>` | 1182 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2314 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1978 |

---

### Test Example 24 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>And then, </src><tgt>好的。然后，</tgt>` | 995 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1374 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | 1395 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1358 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1451 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1348 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 934 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1831 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>实际上要用这些值。</tgt>` | 1974 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 570 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>game dot sort array. </src><tgt>所以这个game.sort数组。</tgt>` | 2511 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1843 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 1019 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment, </src><tgt>19차 수정안의 의미는</tgt>` | 1790 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 992 |
| 5 | `<src>history as a guide </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>19차 수정안의 역사와</tgt>` | 1496 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1463 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>정치적 변화를</tgt>` | 1682 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 1212 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>이해하는 데 도움이 됩니다.</tgt>` | 1480 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1897 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1702 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>물론</tgt>` | 978 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Miriam. </src><tgt><\|wait\|></tgt>` | 1858 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1058 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 953 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1261 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>ゆるむと</src><tgt>기어가 맞물리면</tgt>` | 1523 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えて</src><tgt><\|wait\|></tgt>` | 1444 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>신호가 꺼져서</tgt>` | 1570 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1637 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>ヤクネジの</src><tgt>안 되니까, 기어 앞쪽에</tgt>` | 1230 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1355 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>付いている</src><tgt>나사 머리가</tgt>` | 2106 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>っていうことですね。</src><tgt><\|wait\|></tgt>` | 2142 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>달려 있는 거예요.</tgt>` | 798 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンブレーキを</src><tgt><\|wait\|></tgt>` | 1698 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 919 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt>あるいは、</tgt>` | 899 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1310 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何かを書きたい、テキストを書きたい、</tgt>` | 1738 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1164 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>その時に、</tgt>` | 1557 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1604 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. It's like, oh, </src><tgt>言葉の綴りすら分からないことに気づく。まるで「あ、</tgt>` | 1998 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 732 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>spelled with a double </src><tgt>この単語、</tgt>` | 2050 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2123 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double l, I don't know. </src><tgt>doublep、doublel、なんて綴りだか分からない感じ。</tgt>` | 1920 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 887 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>我当时已很正常，</src><tgt>I was already quite normal at the time.</tgt>` | 1802 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>很快乱跳，</src><tgt><\|wait\|></tgt>` | 1478 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src><\|wait\|></src><tgt>But I quickly started jumping around,</tgt>` | 1494 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀，</src><tgt><\|wait\|></tgt>` | 796 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>切肩大概</src><tgt>so I couldn't keep it open.</tgt>` | 1486 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1518 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>来选择，</src><tgt>I had to choose between twelve options.</tgt>` | 1958 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 924 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>I had to choose between kicking and lifting my legs.</tgt>` | 1812 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 2318 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他能都很</src><tgt>Both were fine.</tgt>` | 1707 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 867 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 766 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>最长的部分呢？</src><tgt>가장 긴 부분은요?</tgt>` | 1489 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是一个</src><tgt><\|wait\|></tgt>` | 1326 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>戴雪的人，但是他是</src><tgt>우리가 보는 건 戴雪(다이쉐) 인데, 그는</tgt>` | 1989 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的，</src><tgt><\|wait\|></tgt>` | 802 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src>所以</src><tgt>역방향에 속하니까</tgt>` | 1310 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通场吗这样的一个状况</src><tgt><\|wait\|></tgt>` | 1751 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>的需要去</src><tgt>통장(통장)이</tgt>` | 1924 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别的注意</src><tgt><\|wait\|></tgt>` | 1196 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能</src><tgt>특별히 주의해야 할 점은, 그가</tgt>` | 1475 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>能够得到</src><tgt><\|wait\|></tgt>` | 2184 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他吊不到</src><tgt>그에게</tgt>` | 1017 |
| 13 | `<src><\|wait\|></src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1203 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt>당신의 의식을</tgt>` | 1017 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 815 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt>Vanadium and these things</tgt>` | 1786 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 1000일인가 </src><tgt><\|wait\|></tgt>` | 1582 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1293 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>거진 6000일인가 </src><tgt><\|wait\|></tgt>` | 897 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>중대 로는 굉장히 </src><tgt>are around 1,000 or 6,000, I think. For the heavy elements,</tgt>` | 2595 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 794 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연 업 미네랄이다 </src><tgt>they're definitely minerals.</tgt>` | 2082 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1985 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 2151 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>제 그런 거죠. 이제 </src><tgt>That's why we talk about them. Now,</tgt>` | 1185 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1352 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt>add in zinc.</tgt>` | 985 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 934 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在这个</src><tgt>皆さんにお伝えしたいのですが、</tgt>` | 1055 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，</src><tgt><\|wait\|></tgt>` | 1326 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>このローマは一日にしてできたものではなく、</tgt>` | 1831 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1006 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>ですから、</tgt>` | 1425 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1441 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>遗迹啊</src><tgt>今あなたが直面している遺産や</tgt>` | 1124 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景，</src><tgt><\|wait\|></tgt>` | 1632 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是你</src><tgt>風景も、</tgt>` | 2176 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一夜之间就</src><tgt><\|wait\|></tgt>` | 1392 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的。</src><tgt>一夜にして変化したものではないんです。</tgt>` | 1374 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此，</src><tgt><\|wait\|></tgt>` | 1818 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>会见习属期的朋友呢，</src><tgt>ですから、見習属の皆さんには、</tgt>` | 1210 |

---

### Test Example 32 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 865 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事，</tgt>` | 987 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there were </src><tgt><\|wait\|></tgt>` | 1215 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such instances before </src><tgt>以前也有过</tgt>` | 1295 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1275 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>net filter TC, </src><tgt>网络过滤器TC，</tgt>` | 779 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>and so </src><tgt><\|wait\|></tgt>` | 1230 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src><\|wait\|></src><tgt>所以</tgt>` | 1541 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>this is just one another place </src><tgt><\|wait\|></tgt>` | 1070 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>where we put </src><tgt>我们只是</tgt>` | 1443 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2152 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>dev </src><tgt><\|wait\|></tgt>` | 1195 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>operators or engineers </src><tgt><\|wait\|></tgt>` | 1511 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>work on a codebase </src><tgt><\|wait\|></tgt>` | 1883 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt>把开发人员或工程师在代码库上工作的人放在这里，他们应该知道这一点。</tgt>` | 1410 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 733 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>砸到了一个铁头，</src><tgt>鉄の塊にぶつかって、</tgt>` | 1772 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1381 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>打到了铁头之后，</src><tgt>もし鉄の塊にぶつかったら、</tgt>` | 1640 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 744 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>抓前</src><tgt>必ず</tgt>` | 1106 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>手阻，</src><tgt><\|wait\|></tgt>` | 1592 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想说哎，</src><tgt>前手をガードしてください。そうすると、</tgt>` | 1116 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我再去操作</src><tgt><\|wait\|></tgt>` | 1553 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>「あ、また操作しなきゃ」なんて思わないようにしてください。</tgt>` | 2321 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2419 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのかというと、</tgt>` | 1927 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1068 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>因为呢。</src><tgt>……</tgt>` | 1106 |

---

### Test Example 34 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 767 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃，XJML</src><tgt>呃，</tgt>` | 997 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1214 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피트도 </src><tgt>XJML</tgt>` | 1450 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1481 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt>这个Compit</tgt>` | 1440 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1443 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴피트 언어 의 </src><tgt>语言，</tgt>` | 1008 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1751 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 과 같게 우리 가 이제 </src><tgt>就像我们理解的语法一样，</tgt>` | 2303 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 2155 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>我们需要编写代码，</tgt>` | 1046 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1365 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>编写这些代码的程序</tgt>` | 1051 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1182 |

---

### Test Example 35 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>ちょうど今動き出した</tgt>` | 999 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1267 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt>人、</tgt>` | 1239 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really </src><tgt>本当に</tgt>` | 592 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1258 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt>大事なことなんです。10個あります。</tgt>` | 1973 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1982 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src><\|wait\|></src><tgt>今から</tgt>` | 1833 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>I have about one minute videos </src><tgt><\|wait\|></tgt>` | 725 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>この動画の続きになるような1分程度の動画を</tgt>` | 2560 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1819 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>You know, </src><tgt>いくつか紹介します。そうですね、</tgt>` | 1121 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>a little more detail, </src><tgt><\|wait\|></tgt>` | 1217 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 942 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十日、</src><tgt>十日，</tgt>` | 1040 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>二日手とかですか。</src><tgt><\|wait\|></tgt>` | 1546 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく十秒で</src><tgt>二日手吗？大概十秒</tgt>` | 1501 |
| 5 | `<src>まあ</src><tgt>差不多十秒。</tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1057 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt>一秒</tgt>` | 1422 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1375 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt>左右的时间吧。</tgt>` | 984 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>そうですね。</src><tgt><\|wait\|></tgt>` | 1796 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt>是啊。然后</tgt>` | 1883 |
| 11 | `<src>おそらく</src><tgt>然后</tgt>` | `<src>おそらくする</src><tgt><\|wait\|></tgt>` | 635 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一日に</src><tgt>大概十一日</tgt>` | 2327 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1569 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>的时候，</tgt>` | 872 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | 890 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>宫马什么的。</tgt>` | 1072 |

---

### Test Example 37 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>进去之后会非常迷路。</tgt>` | 936 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1260 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하려고 은 </src><tgt><\|wait\|></tgt>` | 1164 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 걸어다니 고 </src><tgt><\|wait\|></tgt>` | 1533 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있으면 </src><tgt>如果你想走路去，</tgt>` | 756 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>막굴 가면 </src><tgt><\|wait\|></tgt>` | 1206 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt>那更是天方夜谭，</tgt>` | 1854 |
| 9 | `<src><\|wait\|></src><tgt>就不用说了，去外国</tgt>` | `<src>외국 에 나가 는 것도 </src><tgt><\|wait\|></tgt>` | 1906 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. </src><tgt>更别说出国了，简直是惨烈。</tgt>` | 1917 |
| 11 | `<src>좀 창피 하네요. </src><tgt>就更惨了。真有点丢人。</tgt>` | `<src>좀 챙겨야 해요. </src><tgt><\|wait\|></tgt>` | 725 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt>得好好照顾一下。</tgt>` | 2353 |
| 13 | `<src>이제 </src><tgt>不过，</tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1582 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>무뤄봐요. 그거 는 </src><tgt>不如现在努力做研究吧。那</tgt>` | 1424 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>내일 있는 것 같아요. </src><tgt><\|wait\|></tgt>` | 965 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>好像是明天有。</tgt>` | 489 |

---

### Test Example 38 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 733 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>백오십만 개가 중고 번에서 </src><tgt>そのうち150万個は中古販売で</tgt>` | 2057 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>1천 미만 으로 </src><tgt><\|wait\|></tgt>` | 1260 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>4, 500여 개 기업 들이 </src><tgt>1000個未満の企業が450～500個</tgt>` | 2082 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1372 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>ありました。</tgt>` | 1620 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1136 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>一般的に、中小企業は成長するか、あるいは</tgt>` | 1836 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>폐업 해 길게 되는데 </src><tgt><\|wait\|></tgt>` | 1777 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>廃業して長引くことが多いのですが、これは</tgt>` | 2534 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업 들은 </src><tgt><\|wait\|></tgt>` | 1883 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>中小企業は成長も廃業もしない</tgt>` | 1334 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1162 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 798 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니와, </src><tgt>あなたたちも知っているでしょう。</tgt>` | 1584 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>너희 가 </src><tgt><\|wait\|></tgt>` | 1212 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인으로 있을 때에 </src><tgt>異邦人としている時に、</tgt>` | 1623 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 771 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>말 못 하는 우선에게로 </src><tgt>言葉を</tgt>` | 1610 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1575 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>그대로 흘려 </src><tgt><\|wait\|></tgt>` | 971 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>갔느니라. </src><tgt>言えぬ先へとそのまま流れていったのです。</tgt>` | 1944 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 </src><tgt><\|wait\|></tgt>` | 1735 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>내가 너희 에게 </src><tgt>だからこそ、私があなたたちに</tgt>` | 2474 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1625 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 </src><tgt>知らせるのです。神の</tgt>` | 1096 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>영으로 말하는 자는 </src><tgt><\|wait\|></tgt>` | 730 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>御霊で語る者は、</tgt>` | 1091 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 978 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう蒸らせてやるよ。</src><tgt>그럼 그냥 쪄 죽여버리겠어.</tgt>` | 1219 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>今</src><tgt>나는 지금</tgt>` | 1137 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き地を見ている。</src><tgt><\|wait\|></tgt>` | 1283 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>그 지도를 보고 있어.</tgt>` | 789 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1266 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超に超えている</src><tgt>한계가</tgt>` | 1627 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈火勢力よ。</src><tgt><\|wait\|></tgt>` | 1657 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>아주, 아주, 아주 넘어서 버린 불멸의 세력이야.</tgt>` | 1349 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1609 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船団大攻を</src><tgt>오랜 세월 동안</tgt>` | 2199 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってるだろ。</src><tgt><\|wait\|></tgt>` | 869 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt>선단 대공을 해왔잖아.</tgt>` | 1747 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい海賊船を</src><tgt><\|wait\|></tgt>` | 918 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt>나는 이렇게 대단한 해적선을 본 적이 없어.</tgt>` | 1291 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 917 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>金運についてですが、今月は</tgt>` | 1727 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 1489 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财</src><tgt>悪くないですね。ただ、</tgt>` | 1585 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>的部分。也就是说，</src><tgt><\|wait\|></tgt>` | 759 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>在事业方面</src><tgt>正月の運気は少し弱めです。つまり、仕事運は</tgt>` | 2165 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长</src><tgt><\|wait\|></tgt>` | 931 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>带来的红利</src><tgt>業績アップによる恩恵が</tgt>` | 1957 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>与收入的提升，</src><tgt><\|wait\|></tgt>` | 1974 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>如果涉及到投资理财方面，</src><tgt>収入アップにつながります。投資や資産運用に関しては、</tgt>` | 709 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 2216 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错的，</src><tgt>今月も悪くありません。</tgt>` | 1940 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对正财来说，</src><tgt><\|wait\|></tgt>` | 1092 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>ただ、正月の運気と比べると少し</tgt>` | 1270 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt><\|wait\|></tgt>` | 588 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1033 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어디 를 보면 </src><tgt>呃，</tgt>` | 1072 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1672 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt>看，</tgt>` | 1045 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>통생 의자, 그리고 </src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>가족 같은 </src><tgt>那些和20岁一起长大的同龄人，还有</tgt>` | 2098 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>통생 의자나 </src><tgt><\|wait\|></tgt>` | 1379 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt>像家人一样的同龄人，所以</tgt>` | 1938 |
| 9 | `<src><\|wait\|></src><tgt>所以</tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1315 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생 감 보다는 </src><tgt>比起再生，</tgt>` | 1224 |
| 11 | `<src>조금 </src><tgt>比起责任感，</tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 2375 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>쓰는 </src><tgt>还是多用</tgt>` | 1575 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 844 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것 </src><tgt>自己写的东西</tgt>` | 844 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | 1157 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt>吧，希望大家能幸福。</tgt>` | 990 |

---

### Test Example 43 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 967 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>ですから、もちろん</tgt>` | 772 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1353 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースはあります。Aさんと</tgt>` | 1524 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1230 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 콘텐츠 예요. </src><tgt>Bさんがお互いにコンテンツを共有している場合です。</tgt>` | 1516 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 콘텐츠 예요 </src><tgt><\|wait\|></tgt>` | 1192 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>이렇게 되고 </src><tgt>このようにコンテンツが流れていて、</tgt>` | 1183 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1894 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aさんが悪意のあるコードを</tgt>` | 2104 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 556 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람 이 </src><tgt>送ったとき、Bさんが</tgt>` | 2455 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1832 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크로스 사이트 크리티에서 </src><tgt>クロスサイトクリティカル</tgt>` | 1122 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>JSP까지 </src><tgt><\|wait\|></tgt>` | 1224 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>からJSPまで感染してしまうのか、という話です。</tgt>` | 1043 |

---

### Test Example 44 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1121 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>색인 보라 </src><tgt>目を閉じて、</tgt>` | 1051 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1314 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>옛날 서름이 </src><tgt>色を紫にしてください。昔の</tgt>` | 1627 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋든 단찰이 돋든 </src><tgt><\|wait\|></tgt>` | 1228 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 너무 </src><tgt>色あせや色褪せが</tgt>` | 1719 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1753 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀 자는 거야. </src><tgt>すごく気になるんです。それを揺らして、一緒に遊ぶんです。</tgt>` | 2259 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 2085 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>너무 굴릴 거고 </src><tgt>お化けもすごく踊って、</tgt>` | 2111 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>시눈 이 너무 </src><tgt><\|wait\|></tgt>` | 777 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>지켜 주라고 </src><tgt>お目もすごく守って、</tgt>` | 1884 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주다 보니까 </src><tgt><\|wait\|></tgt>` | 990 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>刺して、そんな感じで、気持ちよく</tgt>` | 1260 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감음. </src><tgt><\|wait\|></tgt>` | 901 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1037 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1675 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, because you're </src><tgt>自分たちで「標準」って何だと思うかを定義するんです。だって、</tgt>` | 2145 |
| 5 | `<src>absolutely correct, </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | 702 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt>その考えは完全に正しい。でも、</tgt>` | 1496 |
| 7 | `<src>is is that </src><tgt>しかし現実には、</tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1447 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>現実には、</tgt>` | 1807 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>on the block, and because </src><tgt><\|wait\|></tgt>` | 838 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>私たちが新しいカタカナの登場人物だから。そして、</tgt>` | 2066 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 2242 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前に変わった基準が</tgt>` | 1711 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1076 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our own standard </src><tgt>私たちの基準に</tgt>` | 634 |
| 15 | `<src>everything at this point is being </src><tgt>より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 1158 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher </src><tgt>より高い基準が</tgt>` | 965 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>So, this is</tgt>` | 1364 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうやつでやって、</src><tgt><\|wait\|></tgt>` | 1447 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルパイソン</src><tgt>a visual development environment. We use it to</tgt>` | 1506 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 881 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt>develop with Visual Python.</tgt>` | 1446 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルに書いて</src><tgt><\|wait\|></tgt>` | 1742 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>あとそれは</src><tgt>The reason is that</tgt>` | 1085 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードがそっから生成される</src><tgt><\|wait\|></tgt>` | 1666 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>っていうそれが</src><tgt>the Python code is generated from the flow graph.</tgt>` | 1998 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 2407 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われる</src><tgt>And when it runs, it performs signal processing.</tgt>` | 1956 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>っていう機能になっているから</src><tgt><\|wait\|></tgt>` | 1077 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt>That's why it has that feature.</tgt>` | 1071 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 452 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay, so</tgt>` | 886 |

---

### Test Example 47 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 991 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1039 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1421 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1226 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? </src><tgt>실제로 교육을 얼마나 받았나요?</tgt>` | 1510 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 1723 |
| 7 | `<src><\|wait\|></src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>That's one level of </src><tgt>고등학교를 졸업했나요?</tgt>` | 1809 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1881 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>그게 한 단계의 학력 수준입니다. 대학에 갔나요?</tgt>` | 2361 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, </src><tgt><\|wait\|></tgt>` | 1064 |
| 11 | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>만약 그렇다면, 졸업했나요?</tgt>` | 1757 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt><\|wait\|></tgt>` | 1977 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>그게 또 다른 단계의 학력 수준입니다. 그래서</tgt>` | 1211 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. </src><tgt><\|wait\|></tgt>` | 1046 |
| 15 | `<src>online. </src><tgt>오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>I'll see you online. </src><tgt>지금은 여기까지입니다. 온라인에서 뵙겠습니다.</tgt>` | 1205 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感觉</src><tgt>推し量る</tgt>` | 1287 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1198 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真挚意图的，</src><tgt>相手の感情や真意を察知する。</tgt>` | 1978 |
| 5 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 768 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1405 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1395 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>后经场会提到</src><tgt>後世の場では</tgt>` | 1121 |
| 9 | `<src>这样说：“</src><tgt>よく耳にするのが</tgt>` | `<src>人们这样说：“</src><tgt><\|wait\|></tgt>` | 1700 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 2137 |
| 11 | `<src>这个人</src><tgt>「ほら、</tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1166 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了。”</src><tgt>この人はまた嘘をついているよ」って言われる。</tgt>` | 1735 |
| 13 | `<src>他的眼睛</src><tgt>また嘘をついている。目が</tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1717 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt>彼の目はすべてを物語っている。</tgt>` | 1098 |
| 15 | `<src><\|wait\|></src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1222 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt>つまり、</tgt>` | 818 |
| 17 | `<src><\|wait\|></src><tgt>つまり…</tgt>` | `<src>说：“</src><tgt><\|wait\|></tgt>` | 536 |

---

### Test Example 49 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 999 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 866 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인 다면 </src><tgt>If the stock index is rising,</tgt>` | 2148 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러 면 대형 주도 </src><tgt><\|wait\|></tgt>` | 1412 |
| 5 | `<src>큰 폭의 </src><tgt>these large- cap stocks</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 729 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1601 |
| 7 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>하겠지만 먼저 </src><tgt><\|wait\|></tgt>` | 1590 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1477 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt><\|wait\|></tgt>` | 1163 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1890 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 2128 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 873 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1719 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1018 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 1163 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>you'll see a large- cap lead, but since these lighter stocks move the market first, you should always keep an eye on the market cap of these lighter stocks.</tgt>` | 1456 |

---

### Test Example 50 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 866 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>이거 이 저 </src><tgt>これ、これ、これ、</tgt>` | 1530 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>일할 수 있지만 </src><tgt><\|wait\|></tgt>` | 1331 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>진짜 보살 도요 </src><tgt>これ、これ、これ、</tgt>` | 1457 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 가 </src><tgt><\|wait\|></tgt>` | 916 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>これ、これ、これ、</tgt>` | 1821 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>풀어가 고 있고 </src><tgt><\|wait\|></tgt>` | 1580 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>これ、これ、これ、</tgt>` | 1946 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 볼 필요 가 </src><tgt><\|wait\|></tgt>` | 1156 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>없어요 우주 가 지지 않아. </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ` | 9323 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 461 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 713 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>そして、これについて多くの人が</tgt>` | 1480 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1596 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 </src><tgt>分析をしています。ここで</tgt>` | 994 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠 자의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1217 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>このロクジャの分析を見ると、ソニーが</tgt>` | 1899 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>UHD에 </src><tgt><\|wait\|></tgt>` | 1366 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FP 파이프 를 </src><tgt>UHDFPファームを</tgt>` | 1991 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1368 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>낮춘 것을 </src><tgt>128ビットに下げたことを</tgt>` | 1304 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>눈치 못한다. </src><tgt><\|wait\|></tgt>` | 2422 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈 엑스에서도 없는 </src><tgt>見逃している。XboxシリーズのXboxにもない</tgt>` | 2289 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 830 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュ</tgt>` | 1205 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>S2가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 948 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>S2もここにはない。</tgt>` | 557 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 757 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>ForallE的首制</src><tgt>ForallE의</tgt>` | 1359 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>截止到那个现象，</src><tgt><\|wait\|></tgt>` | 1443 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src><\|wait\|></src><tgt>최초의</tgt>` | 942 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>美登们处于</src><tgt><\|wait\|></tgt>` | 1411 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>暧昧中，</src><tgt>현상까지, 메이딩들은 애매한 상황에 놓여 있습니다.</tgt>` | 2445 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>属位的爱，</src><tgt><\|wait\|></tgt>` | 1044 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src>我们也</src><tgt>소위의 사랑도</tgt>` | 1870 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>同时进入恨</src><tgt><\|wait\|></tgt>` | 912 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt>동시에</tgt>` | 1617 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>在掌上的时候，</src><tgt><\|wait\|></tgt>` | 2121 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>他才爱。</src><tgt>손에 쥐었을 때 비로소 사랑하는 것입니다.</tgt>` | 1278 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1202 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>他就变成</src><tgt>밤이 되면</tgt>` | 1016 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>恨，</src><tgt><\|wait\|></tgt>` | 1205 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆。</src><tgt>그것은 钟摆이 됩니다.</tgt>` | 843 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续</src><tgt><\|wait\|></tgt>` | 533 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>在移动。</src><tgt>계속 움직입니다.</tgt>` | 447 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 919 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, you will not </src><tgt>另外，</tgt>` | 1182 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1423 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>media objects </src><tgt>你将无法</tgt>` | 1139 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1403 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt>在资源之间移动媒体对象，</tgt>` | 1458 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>unless </src><tgt><\|wait\|></tgt>` | 1339 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into </src><tgt>除非</tgt>` | 946 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where you </src><tgt><\|wait\|></tgt>` | 1925 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt>你意识到</tgt>` | 1872 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 600 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource. </src><tgt>把错误的媒体文件添加到了某个资源中。</tgt>` | 2572 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>To put it as we'll </src><tgt><\|wait\|></tgt>` | 1918 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>now, and we can see about </src><tgt>现在我们来看一下，</tgt>` | 1132 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1095 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files and then making sure </src><tgt>移动这些媒体文件，并确保</tgt>` | 1042 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 462 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>它们能正确备份。</tgt>` | 347 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1188 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 879 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section </src><tgt>最初のセクションで少し混乱してしまって、</tgt>` | 2031 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 875 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the EHR </src><tgt><\|wait\|></tgt>` | 1331 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>field being of critical </src><tgt>EHRの重要性について</tgt>` | 1472 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 1333 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 915 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1854 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 1920 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously, for my loves, </src><tgt>変異データベースとの比較で、</tgt>` | 704 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>is that if </src><tgt><\|wait\|></tgt>` | 2304 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree </src><tgt>もちろん、私の愛する皆さん、</tgt>` | 1949 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1058 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt>これらの</tgt>` | 1072 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 392 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>that we can draw from. </src><tgt>データソースに含めるべき項目について合意できなければ、</tgt>` | 1162 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>There's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 555 |
| 19 | `<src><\|wait\|></src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src><\|wait\|></src><tgt>それから参照できるものもありませんよね？</tgt>` | 519 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful, </src><tgt>有意义的、</tgt>` | 986 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1267 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>个人权利，</tgt>` | 1449 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1404 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't know </src><tgt>最高法院最后才介入，而不是主导。我不知道</tgt>` | 1676 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1728 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src>the the van </src><tgt>法院是否想</tgt>` | 1375 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>ard of </src><tgt><\|wait\|></tgt>` | 1041 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>成为社会变革的先锋。</tgt>` | 2137 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 1828 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt>但现在，他们更倾向于</tgt>` | 877 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 1794 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1041 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 898 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | 589 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 857 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt>所以。</tgt>` | 409 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 455 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>你有一些联邦法官，</tgt>` | 416 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 342 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 884 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼게요.</tgt>` | 1522 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1210 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>사진 부분은</tgt>` | 1068 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1411 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>客厅的部分，</src><tgt>객실 부분이에요.</tgt>` | 1597 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1613 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>都是</src><tgt>보통 객실은</tgt>` | 977 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>属于我们要</src><tgt><\|wait\|></tgt>` | 1460 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt>쉴 수 있는 곳이죠.</tgt>` | 1833 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 593 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的</src><tgt>그러니까</tgt>` | 2270 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>部分的话，反映的是</src><tgt><\|wait\|></tgt>` | 1610 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt>몸의 부분은</tgt>` | 1009 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 689 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好好地</src><tgt>자기 자신에게</tgt>` | 1133 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt><\|wait\|></tgt>` | 831 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可如果我们看到</src><tgt>잠시 앉아서 쉴 시간을 주는 거예요. 그런데</tgt>` | 603 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是双椅人的嘛，</src><tgt><\|wait\|></tgt>` | 460 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt>여기 두 개의 의자가 보이네요. 네,</tgt>` | 504 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 354 |

---

### Test Example 57 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 777 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼は</tgt>` | 1101 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a son of Henry, </src><tgt><\|wait\|></tgt>` | 1658 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>he knows that </src><tgt>イエスがヘンリーの息子だと知っていました。</tgt>` | 1618 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's Jude Powell's </src><tgt><\|wait\|></tgt>` | 880 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>son of the wilderness </src><tgt>そして、彼はユダ・パウエルが</tgt>` | 1981 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>sermon today is that he's Henry. </src><tgt><\|wait\|></tgt>` | 1549 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>And so he says to </src><tgt>今日説教でヘンリーの息子だと述べていることを知っていました。だから彼は</tgt>` | 2585 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 1650 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're a son of God, </src><tgt>イエスに言ったのです。「もしあなたが神の息子なら、</tgt>` | 2652 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt><\|wait\|></tgt>` | 1839 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread. </src><tgt>証明してみせなさい。この石をパンに変えなさい。」</tgt>` | 1334 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1069 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | 915 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 451 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>Man, </src><tgt>その誘惑にどう対処したのでしょうか？いやはや、</tgt>` | 566 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by </src><tgt><\|wait\|></tgt>` | 429 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>barrel alone. </src><tgt>ジョナタンは樽を一人で運んだのです。</tgt>` | 497 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 793 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>これらの人々は非常に稀です。</tgt>` | 1355 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1200 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up </src><tgt>そして、</tgt>` | 1106 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1414 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するよう、しばしば現れます。</tgt>` | 1561 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1638 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その性格は</tgt>` | 883 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1732 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾をはらんでいます。</tgt>` | 2136 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 2067 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ではありますが、</tgt>` | 861 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1608 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations </src><tgt>無意味な会話を</tgt>` | 1077 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1241 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>and like to get straight to </src><tgt>嫌い、</tgt>` | 871 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 518 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>要点にすぐ入ることを好みます。また、</tgt>` | 600 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 422 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>to play the devil's advocate, </src><tgt>悪魔の代弁者になるのも好きです。</tgt>` | 539 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never </src><tgt><\|wait\|></tgt>` | 308 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 366 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 255 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E and C P </src><tgt>EとCPは</tgt>` | 262 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stands for. </src><tgt><\|wait\|></tgt>` | 288 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 813 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이준석은 정부 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1775 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 멤버 이 </src><tgt><\|wait\|></tgt>` | 1494 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>후보 를 위해서 하며서 </src><tgt>was a member who rejected the government's candidate status.</tgt>` | 1865 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1559 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>He said he was for the candidate's victory,</tgt>` | 2023 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색까지 </src><tgt><\|wait\|></tgt>` | 1928 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>even offering a ' Je-bo ' ( a term for a political donation or contribution) to show his support. But now</tgt>` | 2483 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2410 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1592 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Jong- in</tgt>` | 1444 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1081 |
| 13 | `<src><\|wait\|></src><tgt>Lee Jun -seok</tgt>` | `<src>윤석열 후보 를 </src><tgt>and then</tgt>` | 442 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 897 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt>held a grudge to bring down Yoon Suk- yeol.</tgt>` | 665 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 283 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt>He was showing a combative spirit.</tgt>` | 431 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 335 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt>He was determined to do it.</tgt>` | 333 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 295 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 </src><tgt><\|wait\|></tgt>` | 283 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>성창납건. </src><tgt>Lee Jun- seok's ' Seong- chang- nap-geon ' (a term for a political donation).</tgt>` | 595 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 261 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 </src><tgt>The opposition party's attack</tgt>` | 300 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 342 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>で、まあ</src><tgt><\|wait\|></tgt>` | 965 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt>So, after the meal,</tgt>` | 968 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので、</src><tgt><\|wait\|></tgt>` | 1655 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>でここのね</src><tgt>I want to make something now. So,</tgt>` | 1509 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ホルモン温泉ホテル</src><tgt><\|wait\|></tgt>` | 1104 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1412 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>焼魚食べれる場所</src><tgt><\|wait\|></tgt>` | 1450 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 875 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので</src><tgt>I'm planning to go to the Horumon Onsen Hotel to eat grilled fish.</tgt>` | 2470 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1661 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt>So, in the future,</tgt>` | 2120 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 804 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なっていう方はですね、</src><tgt>if you're thinking of staying at the Goldston Hotel,</tgt>` | 2109 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 784 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>thinking about staying here in the future,</tgt>` | `<src>見てみると、まあいいんじゃない</src><tgt>take a look at it,</tgt>` | 1200 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと、はい。</src><tgt><\|wait\|></tgt>` | 917 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt>I think it's a good idea.</tgt>` | 533 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここのホテルからですね。</src><tgt><\|wait\|></tgt>` | 317 |
| 19 | `<src>駅ももう</src><tgt>From this hotel,</tgt>` | `<src>부산駅も</src><tgt>From this hotel,</tgt>` | 459 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 375 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt><\|wait\|></tgt>` | 284 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 332 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 328 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいね、まあホテル</src><tgt><\|wait\|></tgt>` | 372 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので、</src><tgt>the location is really great— you can walk to Busan Station in about a kilometer or so.</tgt>` | 457 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>翌ったらですね、</src><tgt><\|wait\|></tgt>` | 306 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt>So, if you're considering it,</tgt>` | 362 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 201 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね、今回は。</src><tgt>please give it some thought. That's it for this time.</tgt>` | 246 |
