# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9596
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.4238
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.7733
  - TGT_RELEASE_TOTAL: 494
  - TGT_WAIT_ACCURACY: 0.7086
  - TGT_WAIT_TOTAL: 374
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1363.3110
  - PROCESS_TIME_MS_P50: 1361.0520
  - PROCESS_TIME_MS_P95: 2113.8280
  - PROCESS_TIME_MS_MAX: 12802.0630

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt>从一开始</tgt>` | 770 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1030 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1314 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>孩子还是小学一年级的时候。</tgt>` | 1264 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>あの時点で</src><tgt>那时候</tgt>` | 485 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう身近く</src><tgt><\|wait\|></tgt>` | 1620 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選択を</src><tgt><\|wait\|></tgt>` | 1411 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう退ずして</src><tgt><\|wait\|></tgt>` | 1642 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>あげると</src><tgt>如果能早点做出选择，</tgt>` | 1731 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>十年経っても</src><tgt>十年后</tgt>` | 559 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>大した。</src><tgt>还是挺不错的。</tgt>` | 1779 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1145 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is</tgt>` | 1103 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1293 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱</src><tgt><\|wait\|></tgt>` | 1256 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>浇水，</src><tgt>water them with our deep love,</tgt>` | 636 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>fertilize them,</tgt>` | 1486 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1386 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>培育孩子心灵营养，</src><tgt>nurture their spiritual and emotional nourishment,</tgt>` | 1872 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1831 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>冷心等等，</src><tgt>and so on.</tgt>` | 1637 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>让孩子慢慢长大。</src><tgt>Let them grow up slowly.</tgt>` | 1753 |

---

### Test Example 3 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1259 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1062 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复一下。</tgt>` | 1240 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>学会“洗去再重复”。</tgt>` | 1361 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>Find what you're good at </src><tgt>找到你擅长的地方，</tgt>` | 712 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>多做一些。</tgt>` | 1456 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And what you're not good </src><tgt>你</tgt>` | 1365 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>good at, </src><tgt>不擅长的，</tgt>` | 1591 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>get the people around you to help you with </src><tgt>请身边的人帮忙</tgt>` | 2013 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1621 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>it, and then tell the next time </src><tgt>，下次</tgt>` | 1985 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1108 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气鼠是容易的，</src><tgt>「気鼠」は簡単です。</tgt>` | 2013 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src>但是</src><tgt>しかし、</tgt>` | 646 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师傅</src><tgt>師匠が</tgt>` | 1261 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>指导到</src><tgt><\|wait\|></tgt>` | 1504 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>卢波</src><tgt><\|wait\|></tgt>` | 1385 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>处于中年，</src><tgt>中年になってから</tgt>` | 1576 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>指導した</tgt>` | 659 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>需要反</src><tgt>ので、</tgt>` | 1728 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 1766 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师傅，</src><tgt>師匠になるには、</tgt>` | 2021 |

---

### Test Example 5 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>자 저는 </src><tgt>Well,</tgt>` | 1009 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 839 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1433 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1125 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설스 용심이가 </src><tgt><\|wait\|></tgt>` | 759 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt>it's a mix of righteous intent and murderous intent. Wow,</tgt>` | 2175 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1196 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1873 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>해형으로 </src><tgt><\|wait\|></tgt>` | 1853 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 쥐기 맞는 것 </src><tgt><\|wait\|></tgt>` | 2489 |

---

### Test Example 6 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>淘沙が終わった後、</tgt>` | 1931 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>内部的冶力减轻，</src><tgt>内部の冶力は弱まり、</tgt>` | 1309 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了。</src><tgt>エネルギーも衰えます。</tgt>` | 799 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>然后</src><tgt>それから</tgt>` | 1439 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在</src><tgt><\|wait\|></tgt>` | 1503 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1691 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 1125 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>运行状态，</src><tgt>比較的低エネルギーな稼働状態に留まります。</tgt>` | 1193 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これが</tgt>` | 1612 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>蚁居状态。</src><tgt>いわゆる「蟻居状態」です。</tgt>` | 2651 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大抵</src><tgt>通常</tgt>` | 1088 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>从这个阶段开始，</tgt>` | 933 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1331 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>我才开始做这个。</tgt>` | 1122 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴゴ号、</src><tgt>ゴゴ号、</tgt>` | 743 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt>高冈、</tgt>` | 1567 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1434 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt>塞尚、</tgt>` | 1702 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1725 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 565 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>は、</src><tgt>这些人的画，</tgt>` | 1785 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt>就算是在乡下</tgt>` | 2567 |

---

### Test Example 8 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` | 853 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` | 1110 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop into your body. </src><tgt>进入你的身体。</tgt>` | 1370 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1305 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1508 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么？</tgt>` | 1575 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | 1727 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是胸闷吗？</tgt>` | 1655 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>Or is it </src><tgt>还是</tgt>` | 670 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a block </src><tgt><\|wait\|></tgt>` | 1802 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>in what you're using? </src><tgt>你用的东西卡住了吗？</tgt>` | 2806 |

---

### Test Example 9 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1338 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>怪在嵩子寺附近，</src><tgt>It's near Songzi Temple,</tgt>` | 1961 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个游行也很大，</src><tgt>and the parade is huge.</tgt>` | 942 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1006 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt>And then,</tgt>` | 1503 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt><\|wait\|></tgt>` | 1357 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>解脱团，</src><tgt>I'm on vacation and I'm releasing the ' Jie Tuo ' group.</tgt>` | 1928 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1514 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>这里是</src><tgt><\|wait\|></tgt>` | 630 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1773 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>这种解脱团。</src><tgt>This is what a ' Jie Tuo ' group looks like.</tgt>` | 3005 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 977 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 1006 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt><\|wait\|></tgt>` | 1200 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>extremely happy people. This is </src><tgt>非常に幸せな人々の研究を様々な角度から行いました。</tgt>` | 1593 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1512 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>これは研究の序章です。</tgt>` | 1428 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 1594 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 736 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1677 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people that </src><tgt>最も幸せな人々の10%を分析したところ、</tgt>` | 2831 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>そこから学べる点があります。</tgt>` | 2009 |

---

### Test Example 11 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1335 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>The people in the auspicious spots</tgt>` | 1581 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 937 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1565 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1550 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1687 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt>They are people who were selected randomly.</tgt>` | 1751 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 554 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1810 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교수 아들은 </src><tgt>The professor son, who didn't know the truth,</tgt>` | 2833 |

---

### Test Example 12 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 963 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Abbotrol, </src><tgt>I'm Abbotrol,</tgt>` | 1509 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축발시키고 </src><tgt><\|wait\|></tgt>` | 1067 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1323 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1570 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt><\|wait\|></tgt>` | 1557 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>페르나아. </src><tgt>Fernao, who killed his own father.</tgt>` | 1894 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1866 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 1829 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt>The same generation as Park Chan</tgt>` | 2362 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt>are here.</tgt>` | 899 |

---

### Test Example 13 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个</src><tgt><\|wait\|></tgt>` | 973 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>情况，我们就是</src><tgt>Facing this situation,</tgt>` | 1305 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1197 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>we should quickly report it to our supervisor.</tgt>` | 1542 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1639 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们学校这个状况，</src><tgt>Or we should notify the school about this situation.</tgt>` | 1666 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想</src><tgt><\|wait\|></tgt>` | 1437 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>自己什么都把它扛下来，</src><tgt>Don't try to handle everything yourself.</tgt>` | 2147 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>不理承担。</src><tgt>Don't ignore the responsibility.</tgt>` | 1874 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>整体而言，</src><tgt>Overall,</tgt>` | 1599 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>是应该诉讼。</src><tgt>it's better to sue.</tgt>` | 1500 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right. </src><tgt>好的。</tgt>` | 1207 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>And then, </src><tgt>然后，</tgt>` | 888 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | 1413 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1080 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 648 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1670 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1476 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1621 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1563 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>实际上要用这些值。</tgt>` | 717 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt>所以</tgt>` | 1541 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>game dot sort array. </src><tgt>这个game.sort数组。</tgt>` | 2225 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1157 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1096 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 를 </src><tgt><\|wait\|></tgt>` | 1350 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주게 달래 자가 주고 내가 </src><tgt><\|wait\|></tgt>` | 1241 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>죽이려고 들어왔으러서다. </src><tgt>I came to kill him because he was trying to get me to give him other feasts.</tgt>` | 2118 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 925 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 를 주게 달래 자 </src><tgt><\|wait\|></tgt>` | 1631 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>안 되나? 내가 </src><tgt>He was trying to get me to give him other feasts, but I said, ' You can't give me other feasts? '</tgt>` | 2983 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 696 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주자 는 거야. </src><tgt>He was the one who wasn't listening to me.</tgt>` | 2627 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1619 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 669 |

---

### Test Example 16 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1254 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1000 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただモノという</src><tgt><\|wait\|></tgt>` | 1302 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt>We also have items like T- shirts available.</tgt>` | 1493 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 705 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ぜひご参考ください。</src><tgt>Please do take a look.</tgt>` | 1331 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1348 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>That's all for the contact information.</tgt>` | 1755 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、</src><tgt><\|wait\|></tgt>` | 1858 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ご不明な点が</src><tgt><\|wait\|></tgt>` | 1820 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>ありましたら</src><tgt>If you have any questions,</tgt>` | 2125 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>お申し出ください。</src><tgt>please let us know.</tgt>` | 1187 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>そうですよ。</src><tgt>맞아요.</tgt>` | 949 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこで</src><tgt>거기서</tgt>` | 1023 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天国という</src><tgt><\|wait\|></tgt>` | 1284 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>施設被害が</src><tgt>천국 시설 피해가</tgt>` | 1261 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | 540 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt>그런데</tgt>` | 1473 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1504 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井英雄氏の仕組み</src><tgt>나가이 히데오 씨의</tgt>` | 1894 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>시스템은</tgt>` | 1795 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>冒険</src><tgt><\|wait\|></tgt>` | 1523 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 894 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>施設被害</src><tgt>모험 시설 피해</tgt>` | 2106 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>ゴビです。</src><tgt>고비예요.</tgt>` | 682 |

---

### Test Example 18 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1180 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 938 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが</src><tgt>기어가</tgt>` | 1327 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>遊ぶと、</src><tgt>돌면</tgt>` | 975 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>シンガアギアが</src><tgt>싱가 휠이</tgt>` | 898 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>작동이 안 되니까</tgt>` | 1774 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 앞쪽에</tgt>` | 1361 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>ヤクネジの</src><tgt><\|wait\|></tgt>` | 1696 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1862 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 683 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>나사 머리가 붙어 있는 거죠.</tgt>` | 1526 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2186 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>ハイブンブレーキを。</src><tgt>하이 브레이크를...</tgt>` | 865 |

---

### Test Example 19 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 914 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAアンデスにですね、</src><tgt>In the A A Andes,</tgt>` | 1463 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>遺伝性かどうか</src><tgt><\|wait\|></tgt>` | 1320 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>メディアでいう時に</src><tgt><\|wait\|></tgt>` | 1560 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>AAの乱交を</src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1527 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その遺伝性かどうか</src><tgt><\|wait\|></tgt>` | 773 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を調べる</src><tgt><\|wait\|></tgt>` | 1653 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>手続きを保証する</src><tgt><\|wait\|></tgt>` | 1617 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1735 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt>they use it to investigate whether something is hereditary in various situations. They guarantee the procedure for checking its hereditary status.</tgt>` | 1915 |

---

### Test Example 20 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>またまたちょっと</src><tgt>又又</tgt>` | 1267 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1339 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>みたいな感じで</src><tgt>有点像距离在拉开，</tgt>` | 1286 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>大将が</src><tgt>大将</tgt>` | 1280 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>ある方多いですね。</src><tgt>好像确实挺多的人。</tgt>` | 1557 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>海老したい方って</src><tgt>想海老的话，</tgt>` | 1523 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行き帰行きたが</src><tgt>马上就想去</tgt>` | 1714 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>いし</src><tgt>回去</tgt>` | 640 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ジュレで</src><tgt>吃寿司，</tgt>` | 1543 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>もとんつみやと</src><tgt><\|wait\|></tgt>` | 1977 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>してガコが強いので。</src><tgt>而且他们对“元つみ”和“ガコ”很上心。</tgt>` | 3010 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なので</src><tgt>所以</tgt>` | 1153 |

---

### Test Example 21 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 934 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If you're a female high school student</tgt>` | 1950 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 787 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间有着某种</src><tgt><\|wait\|></tgt>` | 1124 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>联系，</src><tgt>and you have some kind of connection with someone who's a bit weird,</tgt>` | 2261 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>could it be</tgt>` | 1004 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1592 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天涯里开始的？</src><tgt>something that started back in Tianya?</tgt>` | 2068 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1752 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1802 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 1453 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>连篇，</src><tgt>Yangzi's thoughts were flowing,</tgt>` | 1408 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 858 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt><\|wait\|></tgt>` | 1114 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活的一个</src><tgt><\|wait\|></tgt>` | 1327 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt>제 삶의 궤도로 돌아가게 해줘요.</tgt>` | 1436 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够哈</src><tgt><\|wait\|></tgt>` | 1539 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>在它下面的时候，</src><tgt>그 아래에 있을 때,</tgt>` | 1623 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1696 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭给人家吃，</src><tgt>사람들에게 뜨거운 국과 밥을 대접하고,</tgt>` | 2175 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就那么</src><tgt><\|wait\|></tgt>` | 1657 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>备好这些</src><tgt><\|wait\|></tgt>` | 1929 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的愿望哈，</src><tgt>그 작은 소망을 준비하는 거예요.</tgt>` | 1420 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1334 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 979 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼</tgt>` | 1344 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt>화학 결합은</tgt>` | 1161 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy. And when those </src><tgt>에너지를 저장합니다.</tgt>` | 1458 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>bonds are broken, </src><tgt>결합이 끊어지면</tgt>` | 1808 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 잠재 에너지가</tgt>` | 1409 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted </src><tgt><\|wait\|></tgt>` | 1545 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>to other types of energy, </src><tgt>다른 형태의 에너지로</tgt>` | 1988 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>변환됩니다. 예를 들어 열이나 빛 같은 거죠.</tgt>` | 2069 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>아니면</tgt>` | 1897 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 1121 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>다른 결합을 만드는 데 사용되기도 합니다.</tgt>` | 1498 |

---

### Test Example 24 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1080 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>我当时已很正常，</src><tgt>I was already quite normal at the time.</tgt>` | 1967 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>很快很乱跳，</src><tgt>But I started jumping around quickly.</tgt>` | 943 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1002 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>所以坚持不回答。</src><tgt>So I just kept saying no.</tgt>` | 1749 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间大概</src><tgt><\|wait\|></tgt>` | 1363 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1663 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>来筛选段，</src><tgt>There were about twelve screening rounds,</tgt>` | 1573 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 717 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下踢腿，</src><tgt>and the legs were kicking and kicking,</tgt>` | 2164 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>and it was all fine.</tgt>` | 2221 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 567 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>疑惑的离开。</src><tgt>They all left looking confused.</tgt>` | 1494 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个</src><tgt>2つ目は</tgt>` | 963 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是问子二</src><tgt>「子二」</tgt>` | 1339 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>事情，</src><tgt>の件です。</tgt>` | 1208 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>还服务</src><tgt><\|wait\|></tgt>` | 1299 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一级一线</src><tgt>第一線で</tgt>` | 1257 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>戦っている大牛たちを支援するものです。</tgt>` | 1492 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说</src><tgt>例えば、</tgt>` | 560 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做维向</src><tgt><\|wait\|></tgt>` | 1686 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>运动好事几点，</src><tgt>「維向運動」の好事几点</tgt>` | 2131 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt>を</tgt>` | 1601 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维向运动平分</src><tgt>分ける</tgt>` | 2020 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>的星棒，</src><tgt>星棒を</tgt>` | 1334 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>反而活了。</src><tgt>配ると、逆に活力が湧いてくるんです。</tgt>` | 1547 |

---

### Test Example 26 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1224 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 1106 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment, </src><tgt>19차 수정안의 의미는</tgt>` | 1518 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore its </src><tgt>그리고</tgt>` | 1289 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>그 역사를 살펴보는 것입니다.</tgt>` | 1608 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1468 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1514 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt>정치적 변화가 어떻게 일어날 수 있는지</tgt>` | 1247 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 그 가이드라인을 통해.</tgt>` | 1308 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1810 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1917 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>물론</tgt>` | 1188 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>I'm Miriam. </src><tgt>저는 미리아입니다.</tgt>` | 1606 |

---

### Test Example 27 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Shiranami Tsuruta. </src><tgt>제 이름은 시라나미 츠루타입니다.</tgt>` | 2114 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently studying </src><tgt>현재</tgt>` | 1059 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 695 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>a business and finance </src><tgt><\|wait\|></tgt>` | 1607 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a doctorate of </src><tgt><\|wait\|></tgt>` | 1533 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>psychology. </src><tgt>경영학과 심리학 박사 과정을 밟고 있습니다.</tgt>` | 1970 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yale, </src><tgt>여기 예일 대학교에서는</tgt>` | 1900 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1861 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>앞으로</tgt>` | 2449 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 683 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1828 |

---

### Test Example 28 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>最长的部分呢？</src><tgt>가장 긴 부분은요?</tgt>` | 1763 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是一个</src><tgt>우리가 보는 건</tgt>` | 820 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>戴雪的人，但是他是</src><tgt>눈을 덮은 사람인데,</tgt>` | 1391 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>属于逆向的，</src><tgt>역방향이에요.</tgt>` | 1691 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src>所以</src><tgt>그래서</tgt>` | 1243 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>通场吗这样的一个状况</src><tgt>통장처럼</tgt>` | 1738 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>的需要去</src><tgt>특별히</tgt>` | 1687 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意的是</src><tgt>주의할 점이</tgt>` | 603 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 2078 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>与他吊不到</src><tgt><\|wait\|></tgt>` | 1044 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与他的意识</src><tgt><\|wait\|></tgt>` | 1342 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>哦。</src><tgt>그의 의식을</tgt>` | 935 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 898 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>砸到了一个铁头，</src><tgt>鉄の塊にぶつかって、</tgt>` | 1937 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt>もし</tgt>` | 631 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>打到了铁头之后，</src><tgt>鉄の塊に当たったら、</tgt>` | 1409 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1542 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>抓前</src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>手阻，</src><tgt>必ず前手をガードしてください。</tgt>` | 1761 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说哎，</src><tgt>「あ、</tgt>` | 1932 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我再继续操作</src><tgt>また操作を</tgt>` | 1606 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦，</src><tgt>続けよう」なんて思わないでください。</tgt>` | 1817 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1651 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそんなことを言うのか？</tgt>` | 1170 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 709 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>因为呢。</src><tgt>なぜなら……</tgt>` | 1100 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt><\|wait\|></tgt>` | 1875 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 인슐린과 </src><tgt><\|wait\|></tgt>` | 786 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 유사 한 </src><tgt><\|wait\|></tgt>` | 1212 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>작용 이 </src><tgt><\|wait\|></tgt>` | 1495 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 굉장히 </src><tgt><\|wait\|></tgt>` | 1527 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1498 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 836 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1498 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1728 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt>It's like a mineral that acts almost as insulin— it's a mineral that's so similar to insulin that you could really call it a diabetes mineral. So, it's like that.</tgt>` | 3576 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1600 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아연. </src><tgt>And then, zinc.</tgt>` | 1129 |

---

### Test Example 31 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Or or if you have </src><tgt>あるいは、</tgt>` | 1126 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1118 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何かを書き出す必要がある場合、</tgt>` | 1397 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>テキストを</tgt>` | 1324 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt>書く際に、</tgt>` | 1530 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1528 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1699 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. It's like, oh, is </src><tgt>単語のスペルが全く分からないことに気づくかもしれません。「ああ、</tgt>` | 2145 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>this word </src><tgt>この単語は</tgt>` | 1808 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 2139 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1154 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double l, I don't know </src><tgt>pp、llで書くんだっけ？</tgt>` | 1965 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src>it. </src><tgt><\|wait\|></tgt>` | 992 |

---

### Test Example 32 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1280 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>啊，</src><tgt>えー、</tgt>` | 1043 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>このローマでは、</tgt>` | 1371 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>一日のうちに</tgt>` | 1352 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>所以呢，</src><tgt>できるわけじゃないんです。だから、</tgt>` | 1637 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt>今</tgt>` | 1332 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1558 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>遗迹啊</src><tgt>直面している遺産や</tgt>` | 862 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>跟风景，</src><tgt>風景は、</tgt>` | 1552 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也不可能是你</src><tgt>一瞬で</tgt>` | 1800 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一夜之间就眼见</src><tgt>変わるわけじゃないんです。</tgt>` | 2486 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>出来的。</src><tgt>一晩で目にするわけじゃない。</tgt>` | 838 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>你只会见一袖</src><tgt>一瞬で</tgt>` | 1629 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>几的朋友呢。</src><tgt>数人の友人に会うだけですよ。</tgt>` | 1358 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 803 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>백오십만 개가 중고 번호 </src><tgt>150万個が中古番号</tgt>` | 2202 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>1천 미만 으로 </src><tgt>1000未満で</tgt>` | 1412 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>4주장 원기업 들이 </src><tgt>4000万ウォン以下の企業が</tgt>` | 1193 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>多くありました。</tgt>` | 917 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | 1480 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 </src><tgt>中小企業は</tgt>` | 1702 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>成長するか、あるいは</tgt>` | 1947 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>폐업 해 길게 되는데 </src><tgt>廃業して長引くことが多いですが、</tgt>` | 2632 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>これは</tgt>` | 1536 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>소기업 들은 </src><tgt>中小企業は</tgt>` | 952 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>成長も廃業もしない</tgt>` | 1666 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>현상 들을 보이 게 된 거죠. </src><tgt>現象として現れました。</tgt>` | 1552 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new, </src><tgt>没什么新鲜事，</tgt>` | 1118 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1221 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there were </src><tgt><\|wait\|></tgt>` | 1213 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such instances before </src><tgt>以前也有过这样的情况，</tgt>` | 1407 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1519 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>netFilterTC, </src><tgt>netFilterTC，</tgt>` | 1376 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>and so </src><tgt>所以</tgt>` | 1183 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 914 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>this is just one another place </src><tgt>这只是</tgt>` | 1933 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>where we put </src><tgt>我们</tgt>` | 1572 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1725 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>dev </src><tgt><\|wait\|></tgt>` | 1550 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>operators or engineers </src><tgt><\|wait\|></tgt>` | 405 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>work on. It's a place </src><tgt>把开发人员或工程师放在的地方。这是一个</tgt>` | 2069 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>where of that. </src><tgt>工作场所。</tgt>` | 1092 |

---

### Test Example 35 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1170 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어디 를 보면 </src><tgt>你看，</tgt>` | 924 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1391 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 이런 </src><tgt><\|wait\|></tgt>` | 1163 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>존생이 자, 그래도 </src><tgt>那些和20岁一起长大的朋友，</tgt>` | 850 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>가족 같은 </src><tgt><\|wait\|></tgt>` | 1452 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>就像家人一样。</tgt>` | 1486 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt>所以</tgt>` | 1535 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1699 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생 감보 단은 </src><tgt>再生感宝</tgt>` | 705 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1725 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 2137 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 920 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 1429 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>잘해놓고 </src><tgt>自己做得很好，</tgt>` | 1247 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt>希望你也能幸福。</tgt>` | 876 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 913 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃，HTML</src><tgt>呃，</tgt>` | 1130 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1223 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터 도 </src><tgt><\|wait\|></tgt>` | 1116 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt>HTML这种计算机也能理解，</tgt>` | 670 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1412 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1576 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1737 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1835 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1660 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1709 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>我们得按照计算机语言的语法来写代码，</tgt>` | 1838 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1385 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1232 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>所以需要一个程序来写这些代码。</tgt>` | 952 |

---

### Test Example 37 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて</tgt>` | 1272 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>색인 보라 </src><tgt>色を</tgt>` | 1051 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>選んでください。</tgt>` | 1303 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 </src><tgt>昔の</tgt>` | 1171 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>돋든 자리 돋든 </src><tgt>模様や、</tgt>` | 664 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>느낌 이 오면 </src><tgt>模様が浮かんでくるような感覚があれば、</tgt>` | 2038 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 흔들 어서 </src><tgt>それを振って</tgt>` | 1082 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうってことです。</tgt>` | 1758 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>귀신 이 </src><tgt>お化けが</tgt>` | 1807 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>너무 많이 올릴 거고 </src><tgt>たくさん出てくるので、</tgt>` | 1807 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>시눈 이 오면 </src><tgt>目が見えなくなったら</tgt>` | 2352 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>「守って」って</tgt>` | 997 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>이제 찔러 주라고 그러니까 </src><tgt>刺してって言われるから、</tgt>` | 1540 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>リラックスして</tgt>` | 1222 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>目を閉じてください。</tgt>` | 780 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 960 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알거니와, </src><tgt>知っているでしょう。</tgt>` | 1462 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>너희 가 </src><tgt><\|wait\|></tgt>` | 1050 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인으로 있을 때에 </src><tgt>異邦人として</tgt>` | 1459 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1572 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>말 못 하는 우선에게로 </src><tgt>言葉を</tgt>` | 1509 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>그대로 </src><tgt>話せない優先のところへ、そのまま</tgt>` | 1801 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>그려 갔느니라. </src><tgt>描いて行ったのです。</tgt>` | 1941 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1769 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>ですから、私が</tgt>` | 2046 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちに</tgt>` | 1210 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>知らせるのです。</tgt>` | 1377 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님 의 </src><tgt>神の</tgt>` | 990 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>영으로 </src><tgt>霊によって</tgt>` | 940 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt>語る者は。</tgt>` | 688 |

---

### Test Example 39 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十連リネテとか</src><tgt><\|wait\|></tgt>` | 1630 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですかですか？</src><tgt>是十连リネテ吗？</tgt>` | 1078 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>恐らく十秒で</src><tgt>大概十秒</tgt>` | 1219 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1473 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1367 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1346 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt>的时间吧，大概一秒钟左右。</tgt>` | 929 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1764 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1560 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1734 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十連リネテ</src><tgt><\|wait\|></tgt>` | 1712 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt>大概是十连リネテ，</tgt>` | 1421 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 876 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt>宫马之类的</tgt>` | 1130 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>吧。</tgt>` | 651 |

---

### Test Example 40 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어 가면 </src><tgt>进去的话，</tgt>` | 1247 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>会非常迷路。</tgt>` | 1225 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1328 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하려고 은 </src><tgt><\|wait\|></tgt>` | 1301 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 걸어 다니 고 </src><tgt>想开车的话，</tgt>` | 1444 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>이건 에 뭐 </src><tgt><\|wait\|></tgt>` | 1048 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>강북 으로 가면 </src><tgt>走走停停，</tgt>` | 961 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt>去江北那儿更是</tgt>` | 1756 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 장렬이에요. </src><tgt>简直是灾难。</tgt>` | 1962 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1624 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>신기 하네요. </src><tgt>挺神奇的。</tgt>` | 1954 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>대신 에 이제 </src><tgt>不如</tgt>` | 1264 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1244 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>모여 봐요. 그거 는 </src><tgt>努力聚拢一下吧。那</tgt>` | 1006 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>다인 것 같아요. </src><tgt>好像是多人的聚会。</tgt>` | 1214 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 894 |

---

### Test Example 41 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1298 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1217 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1239 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and, </src><tgt>今まさに動き出そうとしている人には、</tgt>` | 1391 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>like ten of them </src><tgt>10人くらい</tgt>` | 1665 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that you're really </src><tgt><\|wait\|></tgt>` | 1577 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>important. </src><tgt>本当に大事な人たちがいます。</tgt>` | 1730 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1842 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1699 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one </src><tgt><\|wait\|></tgt>` | 1851 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 1502 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>この動画の続きとして、1分ほどの動画を</tgt>` | 1528 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one </src><tgt>作ります。それぞれ</tgt>` | 1252 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>and a little more </src><tgt>詳しく</tgt>` | 781 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, </src><tgt>解説します。</tgt>` | 1103 |

---

### Test Example 42 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt>So, this is</tgt>` | 1241 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1437 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうやつでやって、</src><tgt>a visual development environment.</tgt>` | 1129 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルパイソン</src><tgt><\|wait\|></tgt>` | 1277 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt>It's a Visual Python development environment.</tgt>` | 1812 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt>The reason</tgt>` | 1337 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルに書いて</src><tgt><\|wait\|></tgt>` | 1793 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>あとそれは</src><tgt><\|wait\|></tgt>` | 1850 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>パイソンコードがそっから生成される</src><tgt>is that you write it in Visual FlowGraph,</tgt>` | 1626 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>っていうそれが</src><tgt><\|wait\|></tgt>` | 1607 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt>and Python code is generated from it. When it runs,</tgt>` | 1852 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われる</src><tgt><\|wait\|></tgt>` | 1257 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>っていうところに</src><tgt><\|wait\|></tgt>` | 640 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているからです。</src><tgt>signal processing happens.</tgt>` | 1056 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 759 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay, so</tgt>` | 1036 |

---

### Test Example 43 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt>だから</tgt>` | 1103 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>もちろん、</tgt>` | 825 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt>こういうケースもあります。</tgt>` | 1499 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>Aさんと</tgt>` | 1080 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람 이 </src><tgt>Bさんが</tgt>` | 755 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 콘텐츠 예요. </src><tgt>お互いにコンテンツを共有するケースです。</tgt>` | 2263 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 콘텐츠 예요 </src><tgt>コンテンツを共有するケースです。</tgt>` | 1012 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>이렇게 되고 </src><tgt>そして、</tgt>` | 1481 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | 1937 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪意のあるコードを</tgt>` | 1807 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>주었을 때 </src><tgt>送った時、</tgt>` | 2029 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비라는 사람 이 </src><tgt>Bさんが</tgt>` | 1329 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt>実際に</tgt>` | 1441 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로스 사이트 크리티에서 </src><tgt>クロスサイトクリティで</tgt>` | 1414 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>JSP까지 </src><tgt>JSPまで</tgt>` | 750 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>感染してしまうかどうか。</tgt>` | 1098 |

---

### Test Example 44 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1177 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1335 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1219 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is, because you're </src><tgt>自分たちで「基準」って何だと思うかを定義するんです。</tgt>` | 1609 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>absolutely correct, </src><tgt>完全に正しいんです。</tgt>` | 1437 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src>but the reality </src><tgt>でも、</tgt>` | 1411 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt>現実には、</tgt>` | 1628 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat and </src><tgt>私たちが新しい猫で、</tgt>` | 2008 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, and because </src><tgt>ブロックで、</tgt>` | 1663 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>基準が</tgt>` | 1716 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1587 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前から変わってしまって、</tgt>` | 427 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1657 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard </src><tgt>より高い基準を</tgt>` | 1128 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>求められているんです。</tgt>` | 622 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is being held to </src><tgt><\|wait\|></tgt>` | 1079 |

---

### Test Example 45 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>金運についてですが、</tgt>` | 1164 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | 1596 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>还不错的，但是</src><tgt>かなり良い方だと思います。</tgt>` | 909 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较稳定</src><tgt>安定していて、</tgt>` | 1254 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src>的部分。也就是说，</src><tgt>安定しているという感じです。つまり、</tgt>` | 1903 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>在事业方面</src><tgt>仕事面では</tgt>` | 1384 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>的业绩增长</src><tgt>業績の伸びは</tgt>` | 1715 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>是稳定的，</src><tgt>安定しています。</tgt>` | 1866 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>收入的提升。如果</src><tgt>収入も上がります。</tgt>` | 2027 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>在投资理财方面，</src><tgt>投資や資産運用については、</tgt>` | 2693 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 481 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错的，</src><tgt>良い方です。</tgt>` | 1501 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>只是相对占财来说，</src><tgt>ただ、お金を稼ぐという点から見ると、</tgt>` | 1718 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>就稍微落了那么一点</src><tgt>少し</tgt>` | 702 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>点。</src><tgt>落ちた感じです。</tgt>` | 707 |

---

### Test Example 46 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1177 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1177 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1370 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1314 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? </src><tgt>실제로 학업을 얼마나 마쳤나요?</tgt>` | 1674 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>고등학교를 졸업했나요?</tgt>` | 1712 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt>그게</tgt>` | 1654 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>attainment. </src><tgt>한 단계의 학력 수준입니다.</tgt>` | 1925 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>대학에 갔나요?</tgt>` | 2006 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>And if so, </src><tgt>만약 그렇다면,</tgt>` | 2295 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>졸업했나요?</tgt>` | 839 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt>또 다른 단계의 학력 수준입니다.</tgt>` | 1674 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>그게</tgt>` | 1148 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>지금까지입니다. 곧</tgt>` | 854 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 984 |

---

### Test Example 47 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1127 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう蒸らせてやる。</src><tgt>그렇다면 물을 끓여서 쪄버리겠다.</tgt>` | 1846 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt>나는</tgt>` | 809 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt>지금</tgt>` | 1258 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>ひっそり見てる。</src><tgt>조용히 지켜보고 있어.</tgt>` | 1567 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1377 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>이제</tgt>` | 700 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えている</src><tgt><\|wait\|></tgt>` | 1466 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不烈火勢気よ。</src><tgt>불멸의 화염처럼, 정말 한계가 넘어서 버렸어.</tgt>` | 2196 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1708 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 2155 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船内で</src><tgt><\|wait\|></tgt>` | 924 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>クーヤやってる</src><tgt><\|wait\|></tgt>` | 1431 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1137 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい海賊船を</src><tgt><\|wait\|></tgt>` | 836 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>나는 배 안에서 오랜 세월 동안 쿠야를 해왔는데, 이렇게 대단한 해적선을 본 적이 없어.</tgt>` | 1613 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1237 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感觉</src><tgt><\|wait\|></tgt>` | 1344 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt>相手の感情を</tgt>` | 1162 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>或真性的意图的，</src><tgt>推し量ったり、本心を見抜いたり、</tgt>` | 1599 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1504 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>そういうことが</tgt>` | 1356 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1668 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>后经场会提到</src><tgt>後世の場では</tgt>` | 1769 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>人们这样说：“</src><tgt>よく</tgt>` | 532 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 1819 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt>この人は</tgt>` | 1844 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了。”</src><tgt>また嘘をついているよ」って言われるんです。</tgt>` | 1378 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>彼の目は</tgt>` | 1424 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>すべてを物語っているんです。</tgt>` | 1209 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 745 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 1054 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说：“</src><tgt><\|wait\|></tgt>` | 621 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そして、これについて</tgt>` | 882 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>多くの人が</tgt>` | 1219 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석 을 해놨습니다. </src><tgt>分析をしています。</tgt>` | 1330 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt>ここで</tgt>` | 1225 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>이 로쿠 자의 연설 을 보시면 </src><tgt>このロクジャの演説を見ると、</tgt>` | 1985 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니가 </src><tgt>ソニーが</tgt>` | 1330 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>이력 칩에 </src><tgt>イオレットチップに</tgt>` | 1771 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>FDP 파이 프를 </src><tgt>FDPパイプを</tgt>` | 1994 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>128ビットに</tgt>` | 1916 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>나충가서 로 보인 다. </src><tgt>落とし込んでいるようです。</tgt>` | 2800 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 430 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈, </src><tgt>Xboxシリーズ、</tgt>` | 1649 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에 서도 없는 </src><tgt>Xboxにはない</tgt>` | 1223 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt>インフィニットキャッシュ、</tgt>` | 690 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L2가 여기 도 없다. </src><tgt>L2もありません。</tgt>` | 1080 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 505 |

---

### Test Example 50 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1119 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1279 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인 다면 </src><tgt>If the stock index is rising,</tgt>` | 1388 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이러 면 대형 주도 </src><tgt><\|wait\|></tgt>` | 1239 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1503 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>어 큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1642 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 먼저 </src><tgt>it will likely see a large- cap lead. But first,</tgt>` | 1917 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1716 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt>these smaller stocks</tgt>` | 1993 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1918 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt>will lead the market first,</tgt>` | 1214 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 </src><tgt>so</tgt>` | 1345 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1229 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 862 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 1121 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>we should always keep an eye on the small- cap stocks.</tgt>` | 854 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 992 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>you will not be able to </src><tgt>你将无法</tgt>` | 1533 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media </src><tgt><\|wait\|></tgt>` | 1313 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>objects between </src><tgt><\|wait\|></tgt>` | 1365 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>the resources </src><tgt><\|wait\|></tgt>` | 724 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>if, if </src><tgt>在资源之间移动媒体对象，如果</tgt>` | 1380 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 1542 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where you </src><tgt>出现这种情况：</tgt>` | 1899 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt>你发现</tgt>` | 1679 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1825 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource. </src><tgt>把错误的媒体文件添加到了某个资源中。</tgt>` | 1690 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>To put it as we'll </src><tgt>我们</tgt>` | 1363 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>now, and we can see about </src><tgt>现在来看看</tgt>` | 1198 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those </src><tgt><\|wait\|></tgt>` | 781 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>media files and then making sure </src><tgt>移动这些媒体文件，并确保</tgt>` | 1163 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt>它们能</tgt>` | 604 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>正确备份。</tgt>` | 478 |

---

### Test Example 52 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이거 이 저 </src><tgt><\|wait\|></tgt>` | 1289 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>얘를 쓸 수 있지만 </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ` | 12802 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요. </src><tgt>本当に菩薩です。</tgt>` | 1763 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 자기 의 </src><tgt>いや、自分の</tgt>` | 1369 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>菩薩なんですけど、夢</tgt>` | 1167 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>풀어가고 있고 </src><tgt>を解いているんです。</tgt>` | 887 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>私だけ</tgt>` | 796 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>보살 로 보일 필요 가 </src><tgt>菩薩に見える必要が</tgt>` | 835 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>없어요. 우주 가 지지 않아. </src><tgt>ありません。宇宙がそうしないんです。</tgt>` | 592 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>이 보살 이라는 게. </src><tgt>この菩薩っていうのは。</tgt>` | 575 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point, </src><tgt>ある時、</tgt>` | 925 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>彼は</tgt>` | 967 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is a son of Henry, </src><tgt>ヘンリーの息子であることを知っていました。</tgt>` | 1587 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1268 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he's supposed to be </src><tgt><\|wait\|></tgt>` | 1634 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in the wilderness </src><tgt><\|wait\|></tgt>` | 1431 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>forty days, that he's hungry, </src><tgt>彼は40日間荒野で飢え、</tgt>` | 2120 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>and so he sends </src><tgt>飢えているはずだと知っていました。だから彼は</tgt>` | 1891 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>to Jesus. Hey, if you're </src><tgt>イエスに送ったのです。「おい、</tgt>` | 2746 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>the son of God, prove it." </src><tgt>神の息子なら証明してみろ」と。</tgt>` | 2075 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn these </src><tgt><\|wait\|></tgt>` | 348 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>stones to bread. </src><tgt>この石をパンに変えろ」と。</tgt>` | 1821 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1164 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>just deal with that </src><tgt><\|wait\|></tgt>` | 424 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>彼はその誘惑にどう対処したのでしょうか？</tgt>` | 1243 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt>いやはや、</tgt>` | 416 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Jonathan lead by bread. </src><tgt>ジョナタンはパンで導いたのです。</tgt>` | 593 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>一人で。</tgt>` | 343 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1429 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 1091 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section </src><tgt><\|wait\|></tgt>` | 1365 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1320 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1533 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1376 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 814 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1222 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1783 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 442 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously not my love. </src><tgt>AHR分野の重要性に関する最初のセクションで、変異データベースと重要性の比較について少し混乱していました。もちろん、それは私の好みではありません。</tgt>` | 4225 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt>もし</tgt>` | 665 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1366 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1067 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 947 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 959 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>that we can draw from, </src><tgt>私たちが利用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | 808 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right? </src><tgt>利用できるものはありませんよね？</tgt>` | 656 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 455 |

---

### Test Example 55 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 926 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>ForallE的首制</src><tgt>ForallE의</tgt>` | 1561 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>截止到那个现象，</src><tgt>최초의</tgt>` | 1020 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1257 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>美登们处于</src><tgt>현상까지, 메이든들은</tgt>` | 1823 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1371 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>爱之中所位的爱，</src><tgt>사랑의 위치에 있습니다.</tgt>` | 1824 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1833 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>我们也同时进入</src><tgt>우리도 동시에</tgt>` | 1763 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1883 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>恨在掌上的时候，</src><tgt>손에 쥔 분노 속으로 들어갑니다.</tgt>` | 1643 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>他才爱。</src><tgt>그때서야 비로소 사랑할 수 있습니다.</tgt>` | 1852 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | 1043 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>他就变成</src><tgt>그는</tgt>` | 490 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1085 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>恨那个种白，</src><tgt>그 ' 种白 ' 이라는 분노로 변합니다.</tgt>` | 948 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 490 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>继续在移动。</src><tgt>계속해서 움직입니다.</tgt>` | 406 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>자, 그럼</tgt>` | 1086 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그림을 한번 볼까요?</tgt>` | 1636 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 950 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>그림 부분은</tgt>` | 1348 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt>보시다시피</tgt>` | 1610 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>客厅的部分，</src><tgt>객실 부분이에요.</tgt>` | 1561 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>那客厅一般</src><tgt>보통 객실은</tgt>` | 1676 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是</src><tgt><\|wait\|></tgt>` | 1626 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>属于我们要</src><tgt><\|wait\|></tgt>` | 600 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt>쉴 수 있는 공간이죠.</tgt>` | 1842 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt>그래서</tgt>` | 1818 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的</src><tgt>이건</tgt>` | 1199 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>部分的话，反映的是</src><tgt>몸의 부분이라서</tgt>` | 1418 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 1032 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 937 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地</src><tgt><\|wait\|></tgt>` | 854 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>坐下来休息，</src><tgt>편안하게 앉아서 쉬어야 하는 시간이에요.</tgt>` | 843 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>可由我们可以看到</src><tgt>그리고</tgt>` | 342 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>这边是放五椅人的嘛。</src><tgt>여기 다섯 개의 의자가 놓여 있는 걸 볼 수 있죠.</tgt>` | 705 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt>네,</tgt>` | 229 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>그러니까...</tgt>` | 337 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1336 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful, </src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1344 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1111 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 542 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. And I don't know </src><tgt>有意义的、个人的权利，最高法院最后才做出裁决，而不是引领。我不知道</tgt>` | 2905 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>if the courts want to be </src><tgt>法院是否想</tgt>` | 1735 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the the van </src><tgt><\|wait\|></tgt>` | 1428 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>ard of </src><tgt><\|wait\|></tgt>` | 717 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>成为社会变革的先锋。</tgt>` | 1800 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>如今，</tgt>` | 1770 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but they rather </src><tgt>但他们更倾向于</tgt>` | 1454 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 1342 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 866 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1110 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>反映已经形成的共识。</tgt>` | 585 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt>所以。</tgt>` | 812 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 596 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 455 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 494 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>你有一些联邦法官，他们……</tgt>` | 445 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>この人たちは</tgt>` | 971 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>全く珍しく、</tgt>` | 1329 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>and they often </src><tgt>よく</tgt>` | 1089 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1072 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 610 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するんです。</tgt>` | 1894 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1109 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その性格は</tgt>` | 1602 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾をはらんでるんです。</tgt>` | 1993 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1757 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 1879 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ですが、</tgt>` | 1477 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1591 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations </src><tgt>無意味な会話を</tgt>` | 1161 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 746 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to </src><tgt>嫌い。そして</tgt>` | 1159 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>the point. </src><tgt>要点をまっすぐ言うのが好きなんです。</tgt>` | 749 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love </src><tgt>彼らは</tgt>` | 421 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 462 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, </src><tgt>悪魔の代弁者になるのも大好きで、</tgt>` | 535 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never </src><tgt><\|wait\|></tgt>` | 305 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 369 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 324 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E and C P </src><tgt>EとCPは</tgt>` | 375 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stands for. </src><tgt>…の略です。</tgt>` | 385 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>で、まあ</src><tgt>So, well,</tgt>` | 1211 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 1282 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt>I'd like to try making something after a meal.</tgt>` | 1431 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なのでここのね</src><tgt>So, this one</tgt>` | 1218 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ホルモン温泉ホテル</src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1391 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>焼魚食べれる場所</src><tgt><\|wait\|></tgt>` | 1545 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 749 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので</src><tgt>is planned to be a place where you can eat grilled fish after a meal.</tgt>` | 1866 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1812 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 2526 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 605 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なっていう方はですね</src><tgt>If you're thinking of staying at the Goldston Hotel here in the future,</tgt>` | 2016 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1056 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみるとまあいいんじゃない</src><tgt>you should check it out.</tgt>` | 550 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>かなと。はい。</src><tgt>I think it'd be great.</tgt>` | 1082 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 461 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>ここのホテルからですね</src><tgt>From this hotel,</tgt>` | 507 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 502 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 398 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt><\|wait\|></tgt>` | 290 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 343 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 273 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | 279 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>ホテルになってますので</src><tgt>it's really well- located. You can walk to Busan Station in about a kilometer or so.</tgt>` | 513 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>So if you're interested,</tgt>` | 269 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 262 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それでは</src><tgt>please give it some thought.</tgt>` | 328 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>ね今回は</src><tgt>Well, that's it for this time.</tgt>` | 330 |

---

### Test Example 60 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 1005 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt><\|wait\|></tgt>` | 1560 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 멤버 이 </src><tgt><\|wait\|></tgt>` | 1021 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>후보 를 위해서 하며서 </src><tgt><\|wait\|></tgt>` | 1384 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1706 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1448 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색까지 </src><tgt><\|wait\|></tgt>` | 1731 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1894 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1795 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1954 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1316 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1478 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 1231 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 844 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기 를 품은 </src><tgt><\|wait\|></tgt>` | 1120 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 684 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 474 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 448 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>작정 한 것입니다. </src><tgt>Lee Jun- seok was a member who rejected the government, and he even showed his enthusiasm for the nomination. But now, the moment Yoon Suk- yeol removed Kim Jong- un, Lee Jun- seok has decided to show his aggressive side, saying he's going to knock Yoon Suk- yeol down.</tgt>` | 1213 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 324 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석의 성상납건 </src><tgt><\|wait\|></tgt>` | 406 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 370 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 261 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 얼마나 </src><tgt><\|wait\|></tgt>` | 355 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 입니까? </src><tgt>How big of a boon is the Democratic Party's attack on Lee Jun- seok's sexual scandal?</tgt>` | 439 |
