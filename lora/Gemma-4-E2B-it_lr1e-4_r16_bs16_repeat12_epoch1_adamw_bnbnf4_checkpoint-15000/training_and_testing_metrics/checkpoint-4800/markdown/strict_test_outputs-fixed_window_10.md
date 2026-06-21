# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9164
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.6225
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.9524
  - TGT_RELEASE_TOTAL: 63
  - TGT_WAIT_ACCURACY: 0.9988
  - TGT_WAIT_TOTAL: 806
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1323.0170
  - PROCESS_TIME_MS_P50: 1281.1710
  - PROCESS_TIME_MS_P95: 2300.6710
  - PROCESS_TIME_MS_MAX: 3350.8930

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1353 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1282 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 975 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 956 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>深深的爱浇水，</src><tgt><\|wait\|></tgt>` | 1566 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 1363 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1493 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>培育孩子心灵营养，</src><tgt><\|wait\|></tgt>` | 1378 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1770 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>并耐心等待</src><tgt><\|wait\|></tgt>` | 1125 |
| 11 | `<src>慢慢长大。</src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for them to grow slowly.</tgt>` | `<src>孩子慢慢长大。</src><tgt>What parents need to do is pour deep love on them, nurture their inner growth, and patiently wait as they grow up.</tgt>` | 2146 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 812 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1177 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1316 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1293 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう未資格</src><tgt><\|wait\|></tgt>` | 1414 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1406 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1574 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>こう退ずしてあげると</src><tgt><\|wait\|></tgt>` | 1649 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 777 |
| 11 | `<src>大した。</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，十年后也不会有什么大……</tgt>` | `<src>大丈夫だ。</src><tgt>一开始，孩子还是一年级，对吧。在那时候剪掉未结实枝条，让它退去，十年后也行。</tgt>` | 2824 |

---

### Test Example 3 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자, </src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>저는 용심히 </src><tgt><\|wait\|></tgt>` | 941 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1150 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심히 </src><tgt><\|wait\|></tgt>` | 1210 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>새우 살 용심히가 </src><tgt><\|wait\|></tgt>` | 1345 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1396 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1463 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야, </src><tgt><\|wait\|></tgt>` | 1497 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1634 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해행으로도 </src><tgt><\|wait\|></tgt>` | 784 |
| 11 | `<src>진짜. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover, for real.</tgt>` | `<src>조금 죽임다인가? </src><tgt>So, I've got some swordfish and some shrimp mixed in. Wow, is this really a ' haeng ' dish?</tgt>` | 2894 |

---

### Test Example 4 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Aptrude, </src><tgt><\|wait\|></tgt>` | 989 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>쪽발시 뀌고 </src><tgt><\|wait\|></tgt>` | 1412 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1034 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1389 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt><\|wait\|></tgt>` | 1493 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>페르나, </src><tgt><\|wait\|></tgt>` | 1580 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1332 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1819 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1441 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents. They are the same generation as him.</tgt>` | `<src>됩니다. </src><tgt>I am Aptrude, a foot- fetishist. I am of the same generation as Perona, who killed his own parents, and Park Han- sang.</tgt>` | 2001 |

---

### Test Example 5 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1051 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 928 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1158 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1281 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1191 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 1145 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 917 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1862 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1175 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1668 |
| 11 | `<src>は、田舎の</src><tgt>大致是从这一带开始的，像梵高、高更、塞尚、雷诺阿他们的画，连乡下的</tgt>` | `<src>は、</src><tgt>大概从这之后开始画，比如高更、高安、塞尚、伦纳尔这些人的画，</tgt>` | 2526 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生</src><tgt><\|wait\|></tgt>` | 694 |

---

### Test Example 6 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1179 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>乖的监督者一点，</src><tgt><\|wait\|></tgt>` | 1158 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个游行</src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>也很大。</src><tgt><\|wait\|></tgt>` | 1107 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 1294 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在另一方面，</src><tgt><\|wait\|></tgt>` | 1423 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶渊明</src><tgt><\|wait\|></tgt>` | 1438 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1563 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>探讨一下，</src><tgt><\|wait\|></tgt>` | 1716 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 732 |
| 11 | `<src>仁儿。</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels— this kind of walnut kernels.</tgt>` | `<src>这种和陶渊明。</src><tgt>The supervisor is quite strict, and this protest is also quite large. And on the other hand, I've been discussing with Tao Yuanming— this discussion with Tao Yuanming.</tgt>` | 2980 |

---

### Test Example 7 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要器速是容易的，</src><tgt><\|wait\|></tgt>` | 1415 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有一个师傅</src><tgt><\|wait\|></tgt>` | 850 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>知道，</src><tgt><\|wait\|></tgt>` | 1331 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1368 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如何处于中间，</src><tgt><\|wait\|></tgt>` | 1473 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1458 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反</src><tgt><\|wait\|></tgt>` | 1442 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 821 |
| 11 | `<src>一个师父。</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅。</src><tgt>器速を上げるのは簡単です。しかし、師匠が一人しかいません。どうやってその間に立つか。だから、反転して、自分自身が師匠にならなければなりません。</tgt>` | 3163 |

---

### Test Example 8 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1257 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后呢，</src><tgt><\|wait\|></tgt>` | 1411 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的冶铁矿</src><tgt><\|wait\|></tgt>` | 1329 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了</src><tgt><\|wait\|></tgt>` | 625 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>了，然后</src><tgt><\|wait\|></tgt>` | 1355 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在</src><tgt><\|wait\|></tgt>` | 1379 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1558 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>一个相对的低能量的运行</src><tgt><\|wait\|></tgt>` | 1503 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态。</src><tgt><\|wait\|></tgt>` | 1642 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是</src><tgt><\|wait\|></tgt>` | 994 |
| 11 | `<src>抑郁状态。</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。これが、いわゆる抑うつ状態です。</tgt>` | `<src>所谓的蚁居状态。</src><tgt>砂漠を掘り終えると、内部の鉄鉱石のエネルギーも弱まります。そして、比較的低エネルギーの稼働状態にとどまります。これがいわゆる「蟻居状態」です。</tgt>` | 2651 |

---

### Test Example 9 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1162 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt><\|wait\|></tgt>` | 924 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>extremely happy people. This is </src><tgt><\|wait\|></tgt>` | 1268 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>Tip of the stem, </src><tgt><\|wait\|></tgt>` | 1476 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking at </src><tgt><\|wait\|></tgt>` | 1457 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1496 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1287 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1655 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people that </src><tgt><\|wait\|></tgt>` | 854 |
| 11 | `<src>people that we can learn from. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>非常に幸せな人たちに関する重要な研究を行いました。これは「Tip of the Stem」という研究です。最も幸せな人々の10%を見ています。私たちが学べる人たちです。</tgt>` | 3009 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツ</src><tgt><\|wait\|></tgt>` | 1227 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>などが</src><tgt><\|wait\|></tgt>` | 861 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あのいただもらえる</src><tgt><\|wait\|></tgt>` | 1220 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1220 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 1464 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1353 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりますし、</src><tgt><\|wait\|></tgt>` | 1507 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1742 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ご不明な点が</src><tgt><\|wait\|></tgt>` | 901 |
| 11 | `<src>ランチの案内がありますので</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements, and we have some info about lunch,</tgt>` | `<src>ありましたら内窓が</src><tgt>We also have items like T- shirts available, so please feel free to join us. That's all for the contact information.</tgt>` | 2609 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ありますのでご参照ください。</src><tgt><\|wait\|></tgt>` | 1004 |

---

### Test Example 11 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 1113 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 773 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1048 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 1212 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 1332 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1443 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1711 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 1559 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | 1770 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>language are you </src><tgt><\|wait\|></tgt>` | 1958 |
| 11 | `<src>language are you using? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，你在用什么语言？</tgt>` | `<src>using? </src><tgt>你的身体在做什么？进入你的身体。紧张感从哪里开始？是什么？是头痛吗？是胸闷吗？我问他们，你用的是什么语言？</tgt>` | 2466 |

---

### Test Example 12 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1003 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到我</src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活的一个轨道，</src><tgt><\|wait\|></tgt>` | 1250 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 954 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1301 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>好自在的</src><tgt><\|wait\|></tgt>` | 1404 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>时候在做热汤</src><tgt><\|wait\|></tgt>` | 1483 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热饭一样的，所以这个</src><tgt><\|wait\|></tgt>` | 1619 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>热汤</src><tgt><\|wait\|></tgt>` | 1722 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>我当时背动的这字，</src><tgt><\|wait\|></tgt>` | 1488 |
| 11 | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>是一个小小的愿望</src><tgt>제 삶의 궤도로 돌아가게 해주고, 편안하게 뜨거운 국물이나 밥을 먹을 수 있게 해주는 그런 느낌이에요. 그래서 제가 그때 외운 이 글자는 작은 소망이었어요.</tgt>` | 2626 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 589 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1276 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then </src><tgt><\|wait\|></tgt>` | 802 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1281 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1200 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1288 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1424 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1532 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1420 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. So </src><tgt><\|wait\|></tgt>` | 886 |
| 11 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们要使用这些值。也就是</tgt>` | `<src><\|wait\|></src><tgt>好的，在这些例子之后，说明指令是实际要使用这些值。所以</tgt>` | 2227 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | 991 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1125 |

---

### Test Example 14 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1031 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kiran Patel. </src><tgt><\|wait\|></tgt>` | 1045 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1248 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in </src><tgt><\|wait\|></tgt>` | 1010 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>business and finance </src><tgt><\|wait\|></tgt>` | 1310 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bachelor of psychology. </src><tgt><\|wait\|></tgt>` | 1457 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 1513 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1703 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | 1292 |
| 11 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src><\|wait\|></src><tgt>제 이름은 키란 파텔입니다. 현재 경영학과 재무학을 전공하고 있고, 심리학 학사 학위를 받았습니다. 여기 예일에서 공부하고 있습니다. 그리고 앞으로는</tgt>` | 2489 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>corporate consulting. </src><tgt><\|wait\|></tgt>` | 1046 |

---

### Test Example 15 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 846 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是能源物资</src><tgt><\|wait\|></tgt>` | 915 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二级以上</src><tgt><\|wait\|></tgt>` | 1229 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>并服务在</src><tgt><\|wait\|></tgt>` | 1297 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>一级一线</src><tgt><\|wait\|></tgt>` | 1176 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | 1330 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 649 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1611 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>在做未经封锁房屋时，</src><tgt><\|wait\|></tgt>` | 1343 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你可以发现</src><tgt><\|wait\|></tgt>` | 1638 |
| 11 | `<src>给微信公众号评分</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>给未经封锁房屋</src><tgt>2つ目は、エネルギー物資のレベル2以上で、レベル1の最前線で活動している大牛たちです。例えば、封鎖されていない家を調査していると、</tgt>` | 3139 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>平分的“新房”房</src><tgt><\|wait\|></tgt>` | 700 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 827 |

---

### Test Example 16 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1239 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 878 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1112 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1384 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1417 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1568 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1685 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>어떤 분입니까? </src><tgt><\|wait\|></tgt>` | 1264 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1775 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1952 |
| 11 | `<src>교사 들은. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random. The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교사 들은. </src><tgt>The students in the auspicious position were not actually intelligent, and the students who were randomly selected— what kind of people were they? The teachers who didn't know the truth...</tgt>` | 2662 |

---

### Test Example 17 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1044 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 </src><tgt><\|wait\|></tgt>` | 1147 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>주겨 달라 이거 주고 내가 </src><tgt><\|wait\|></tgt>` | 1513 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>주질 못하 도록 후수주도라도 </src><tgt><\|wait\|></tgt>` | 966 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1289 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 주겨 달라 </src><tgt><\|wait\|></tgt>` | 1821 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았느냐 내가 </src><tgt><\|wait\|></tgt>` | 1711 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>이런 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1324 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 줄 알느냐 </src><tgt><\|wait\|></tgt>` | 1520 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아 </src><tgt><\|wait\|></tgt>` | 1882 |
| 11 | `<src>내가 가. </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh? I'm going.</tgt>` | `<src><\|wait\|></src><tgt>You asked for another dose of medicine, and I couldn't give it to you. You said, ' You asked for another dose of medicine, didn't you? ' You think I don't hear this?</tgt>` | 2771 |

---

### Test Example 18 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1242 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 918 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1151 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to dance, so repeat. </src><tgt><\|wait\|></tgt>` | 1336 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1673 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1642 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And when you're not good </src><tgt><\|wait\|></tgt>` | 1770 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1037 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>at it, get the people around you to help you with it. </src><tgt><\|wait\|></tgt>` | 1878 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1887 |
| 11 | `<src>And until next time. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。下次再见。</tgt>` | `<src>And and tell next time, </src><tgt>最后一点，就是重复。学会跳舞，所以要重复。找到自己擅长的地方，多做一些。当你不太擅长的时候，请身边的人帮忙。然后告诉他们，下次</tgt>` | 2689 |

---

### Test Example 19 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 1288 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 983 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1132 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | 1448 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现有的这个状况。</src><tgt><\|wait\|></tgt>` | 1578 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1721 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1332 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>不理成担，</src><tgt><\|wait\|></tgt>` | 1706 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>责任而已，</src><tgt><\|wait\|></tgt>` | 1884 |
| 11 | `<src>事业运就属凶。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall, your career prospects are quite poor.</tgt>` | `<src>是一个justsolution。</src><tgt>When facing this situation, we just need to report it to our supervisor or let them know about the current situation. Don't think of it as something you have to handle all by yourself. It's just a responsibility, a just solution.</tgt>` | 2998 |

---

### Test Example 20 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 816 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | 976 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1177 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1384 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | 1421 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあ映画の乱交を</src><tgt><\|wait\|></tgt>` | 1561 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べることで、あの</src><tgt><\|wait\|></tgt>` | 1802 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1297 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | 1816 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | 1916 |
| 11 | `<src>といったような</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>といったような</src><tgt>In movies, when you're checking if a creature is actually living in a certain environment, you can use film ecology to confirm that it is.</tgt>` | 2107 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | 1023 |

---

### Test Example 21 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 943 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1137 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1505 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 751 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | 1516 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1416 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>难道会是童年</src><tgt><\|wait\|></tgt>` | 1816 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1110 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>夜里开始的？</src><tgt><\|wait\|></tgt>` | 1850 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1917 |
| 11 | `<src>杨子思绪</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night? Yang Zi's thoughts</tgt>` | `<src>杨子</src><tgt>If there is some connection between high school girls and people with strange appearances, could it be that it starts at night in childhood? Yangzi</tgt>` | 2209 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>思绪连篇，</src><tgt><\|wait\|></tgt>` | 1128 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 840 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 886 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>テキオーセツビ寺が</src><tgt><\|wait\|></tgt>` | 1370 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたが、</src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1370 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1426 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井青氏の仕組み</src><tgt><\|wait\|></tgt>` | 1615 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1769 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>は五本、</src><tgt><\|wait\|></tgt>` | 885 |
| 11 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠. 파생 형용사의 구조는</tgt>` | `<src><\|wait\|></src><tgt>그렇습니다. 거기서 테키오세츠비지가 있었는데, 나카이 아오 씨의 체계는 다섯 본,</tgt>` | 2543 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>セツビ寺五本。</src><tgt><\|wait\|></tgt>` | 1044 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 1030 |

---

### Test Example 23 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 932 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1591 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 852 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | 1657 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>자기 가 보살 인데 꿈일 프로 </src><tgt><\|wait\|></tgt>` | 2033 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>아무 이거, </src><tgt><\|wait\|></tgt>` | 1300 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1068 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보일 프로 요. </src><tgt><\|wait\|></tgt>` | 1858 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>우주 가 지금 나한테 </src><tgt><\|wait\|></tgt>` | 2014 |
| 11 | `<src>보살 이라는데. </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に菩薩だと言ってるんだから。</tgt>` | `<src>보살 이라는 게. </src><tgt>これ、あまりにも低俗なことかもしれないけど、本当に菩薩だよ。いや、自分が菩薩なのに夢の中の出来事だなんて、そんなことあるわけないよ。私だけが菩薩に見えるって。宇宙が今、私に菩薩だなんて。</tgt>` | 3351 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 931 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアです。ギアが</src><tgt><\|wait\|></tgt>` | 1300 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | 1284 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなってしまう</src><tgt><\|wait\|></tgt>` | 1464 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1348 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1362 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ヤクネ字のナットが</src><tgt><\|wait\|></tgt>` | 1748 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いている</src><tgt><\|wait\|></tgt>` | 775 |
| 11 | `<src>ね。</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거죠.</tgt>` | `<src>っていうことですね。</src><tgt>이게 기어입니다. 기어가 헐거워지면 심이 위아래로 움직이지 않게 되니까, 기어 끝에 쇠붙이 너트가 달려 있는 거죠.</tgt>` | 2957 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1085 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンハイ完了。</src><tgt><\|wait\|></tgt>` | 1154 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 1413 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 973 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>also store energy. </src><tgt><\|wait\|></tgt>` | 976 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>And when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1611 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1343 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1588 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1288 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 1874 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1920 |
| 11 | `<src>or gets used to make </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다. 또는</tgt>` | `<src>Or gets used to make </src><tgt>늘어난 고무줄처럼, 화학 결합도 에너지를 저장합니다. 그리고 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 에너지 형태로 변환됩니다. 아니면</tgt>` | 2677 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1168 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 1315 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 893 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1130 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1068 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1359 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | 1622 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1458 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 1508 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1713 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a </src><tgt><\|wait\|></tgt>` | 1955 |
| 11 | `<src><\|wait\|></src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>double p, </src><tgt>あるいは、何か文章を書く必要がある場合、文字を書く必要がある場合、言葉の綴りが全くわからないことに気づくかもしれません。「あ、この単語はpが二つ</tgt>` | 1830 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double lam. I don't </src><tgt><\|wait\|></tgt>` | 1018 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 1131 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1234 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 879 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | 1528 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 960 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1416 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1420 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1458 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 1361 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1741 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 781 |
| 11 | `<src>The meanings </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>The meanings of </src><tgt>제19조 수정헌법의 의미와 그 역사를 탐구하며, 이것이 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 되는 방식을 살펴봅니다.</tgt>` | 3000 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>the amendment, of course, are </src><tgt><\|wait\|></tgt>` | 1279 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 1273 |

---

### Test Example 28 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1535 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 780 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | 1495 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>おしゃれルカダがね、</src><tgt><\|wait\|></tgt>` | 971 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | 1353 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>海遊したい方って</src><tgt><\|wait\|></tgt>` | 1584 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい行き来おきいて</src><tgt><\|wait\|></tgt>` | 1909 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>ください。</src><tgt><\|wait\|></tgt>` | 1094 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>一日で見て</src><tgt><\|wait\|></tgt>` | 1680 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>とトンチモンの灯を</src><tgt><\|wait\|></tgt>` | 2043 |
| 11 | `<src>傾向が強いので、</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且倾向于自己全部投资，</tgt>` | `<src>見方が強いので、</src><tgt>嗯，感觉距离在慢慢拉远，像おしゃれLuca那样，很多人喜欢去海游。想去海游的朋友，一定要多来来往。一天下来看过了很多灯，所以看灯的眼光很强，</tgt>` | 2994 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1036 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 992 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1782 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 1317 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 477 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1507 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1513 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1652 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1274 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1525 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1940 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium, they're almost as insulin. They're so similar that you could call them diabetes minerals. That's how it is. Now,</tgt>` | 2224 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1025 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1188 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1059 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>我当时一切正常，</src><tgt><\|wait\|></tgt>` | 1298 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1365 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 750 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀。</src><tgt><\|wait\|></tgt>` | 1443 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间</src><tgt><\|wait\|></tgt>` | 1270 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>大概有十位医生来</src><tgt><\|wait\|></tgt>` | 1790 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1196 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>判断。以下条轨迹：</src><tgt><\|wait\|></tgt>` | 1863 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一旦打跌，</src><tgt><\|wait\|></tgt>` | 1978 |
| 11 | `<src>都没有问题。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>都没有问题。</src><tgt>I was perfectly fine back then, living my life to the fullest, so I insisted on not having surgery. During that time, about ten doctors came to assess me. The following is the trajectory: once I had a fall, everything was fine.</tgt>` | 2301 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1046 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>他们都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1267 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1389 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个</src><tgt><\|wait\|></tgt>` | 682 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，</src><tgt><\|wait\|></tgt>` | 1152 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>造成了，所以呢，</src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1383 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>你现在所面临的一些</src><tgt><\|wait\|></tgt>` | 1463 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>遗迹啊、</src><tgt><\|wait\|></tgt>` | 1522 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景，</src><tgt><\|wait\|></tgt>` | 1654 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 757 |
| 11 | `<src><\|wait\|></src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>期间就</src><tgt>皆さんにお伝えしたいのは、このローマという場所が、何かを招いたわけではないということです。ですから、今あなたが直面している遺跡や風景が、</tgt>` | 2895 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | 1031 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此，会建议</src><tgt><\|wait\|></tgt>` | 1219 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | 1250 |

---

### Test Example 32 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 934 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there were </src><tgt><\|wait\|></tgt>` | 1088 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such instances before </src><tgt><\|wait\|></tgt>` | 1260 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1300 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>that future TC </src><tgt><\|wait\|></tgt>` | 1406 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1390 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>is just </src><tgt><\|wait\|></tgt>` | 1560 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1272 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to loot it, </src><tgt><\|wait\|></tgt>` | 1067 |
| 11 | `<src>But </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事，以前也发生过这种情况，所以未来TC只是另一个可以掠夺的地方，</tgt>` | 2352 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but devotional. </src><tgt><\|wait\|></tgt>` | 768 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>Software engineers would </src><tgt><\|wait\|></tgt>` | 1130 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>not know about repositories </src><tgt><\|wait\|></tgt>` | 1142 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 1288 |

---

### Test Example 33 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1450 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 882 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1019 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>like ten of them </src><tgt><\|wait\|></tgt>` | 1343 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that you really </src><tgt><\|wait\|></tgt>` | 1420 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1433 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1511 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1683 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 740 |
| 11 | `<src>one minute videos </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>a about one minute videos </src><tgt>これから始める人には、本当に重要な10個のポイントがあります。1分程度の動画で</tgt>` | 2663 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | 578 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1072 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1196 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>You know, in a little more detail, </src><tgt><\|wait\|></tgt>` | 1575 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1019 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | 1414 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt><\|wait\|></tgt>` | 846 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1024 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1520 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1395 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1704 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | 1328 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1703 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | 1925 |
| 11 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src><\|wait\|></src><tgt>好調子な状態になれば、その調子を絶対に守り抜いてください。そうして「あ、もっと操作を続けよう」なんて考えないでください。</tgt>` | 2289 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1118 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1082 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 1030 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 1197 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 881 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1139 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>一个在跳舞的人，但是</src><tgt><\|wait\|></tgt>` | 1143 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于逆向的</src><tgt><\|wait\|></tgt>` | 1503 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1351 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>。这种场景模仿这样的一个状况</src><tgt><\|wait\|></tgt>` | 1974 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>的摄像机摄像机</src><tgt><\|wait\|></tgt>` | 1285 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>去特别注意的是</src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能够</src><tgt><\|wait\|></tgt>` | 1894 |
| 11 | `<src>钓到鱼，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到与他</src><tgt>이 부분에서는 춤추는 사람이 보이는데, 그는 역방향으로 움직이고 있습니다. 이런 상황을 카메라가 촬영할 때, 특히 주목할 점은 그가</tgt>` | 2413 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>调不到</src><tgt><\|wait\|></tgt>` | 1173 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1196 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 36 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150미가 종업었을 </src><tgt><\|wait\|></tgt>` | 1643 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>연령 및 인원 으로 </src><tgt><\|wait\|></tgt>` | 1348 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 702 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1094 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1508 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 2016 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 </src><tgt><\|wait\|></tgt>` | 1045 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>회업의 길을 걷게 되는데 </src><tgt><\|wait\|></tgt>` | 1871 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>회업은 </src><tgt><\|wait\|></tgt>` | 1936 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は成長も廃業も</tgt>` | `<src>소기업들은 성장 도 </src><tgt>その中で150人規模の企業が多かったんです。年齢や人数でいうと、とても小さな企業が多かったですね。一般的に、小さな企業は成長するか、あるいはネットワークビジネスの道に進むことになります。ネットワークビジネスは、小企業は成長も</tgt>` | 3262 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>표해도 하지 않을 현상 들을 </src><tgt><\|wait\|></tgt>` | 1308 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1089 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1250 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一・二日とか</src><tgt><\|wait\|></tgt>` | 1285 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>でした。おそらく</src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 839 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1290 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1408 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1486 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間が</src><tgt><\|wait\|></tgt>` | 1438 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>あるんですね。</src><tgt><\|wait\|></tgt>` | 1717 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 744 |
| 11 | `<src>おそらく</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。然后</tgt>` | `<src>おそらく</src><tgt>大概是十一号、二号吧。大概十秒，嗯，一秒左右的时间。然后，大概</tgt>` | 2658 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一・二日</src><tgt><\|wait\|></tgt>` | 619 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 951 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>であの</src><tgt><\|wait\|></tgt>` | 1164 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮内馬とかが</src><tgt><\|wait\|></tgt>` | 1243 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>あるから。</src><tgt><\|wait\|></tgt>` | 887 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 963 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1399 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 1239 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 773 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1499 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1413 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | 1570 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1393 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1963 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。ですから、あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちも知っているだろう。あなたたちが異邦人であった時、言葉を持たない偶像へと引きずられていった。だから、私があなたたちに</tgt>` | 1652 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1070 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1204 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 1254 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 39 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1048 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>어 Htielmei, </src><tgt><\|wait\|></tgt>` | 1418 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1110 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 컴피트어도 </src><tgt><\|wait\|></tgt>` | 841 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1528 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1405 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1937 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴피트어도 어느 에 </src><tgt><\|wait\|></tgt>` | 1262 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1635 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1954 |
| 11 | `<src>코드 를 작성 해야 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>코드 를 작성 해야 </src><tgt>嗯，像Htielmei这样的竞争对手，我们也能理解，而且人们也能理解。所以，</tgt>` | 1998 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 857 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1204 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 </src><tgt><\|wait\|></tgt>` | 1001 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>프로그램 이 필요 합니다. </src><tgt><\|wait\|></tgt>` | 802 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1013 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう寝かせている。</src><tgt><\|wait\|></tgt>` | 994 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1159 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1287 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>今一日を見てる。</src><tgt><\|wait\|></tgt>` | 1174 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 934 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1145 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1643 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>遠くに越えている船を汚しきす。</src><tgt><\|wait\|></tgt>` | 1530 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1576 |
| 11 | `<src>長年</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>그럼 이미 잠들게 해두지. 나는 지금 하루를 보고 있어. 더 이상 한계는 멀리 지나쳐버린 배를 더럽히고 있어.</tgt>` | 3094 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長年にわだいこを</src><tgt><\|wait\|></tgt>` | 1245 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 1108 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt><\|wait\|></tgt>` | 1265 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>海賊船を見た</src><tgt><\|wait\|></tgt>` | 986 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 767 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1288 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1156 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1238 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 765 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正财的部分，也就是</src><tgt><\|wait\|></tgt>` | 1706 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | 1302 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长所带来的红利</src><tgt><\|wait\|></tgt>` | 1939 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>与收入的</src><tgt><\|wait\|></tgt>` | 1181 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | 1653 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | 2034 |
| 11 | `<src>这个月</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>这个月</src><tgt>金運については、今月はかなり良いと言えます。ただ、正財、つまり仕事の業績向上による恩恵や収入アップに偏っています。投資や資産運用に関しては、今月</tgt>` | 2586 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1227 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对整体来说，</src><tgt><\|wait\|></tgt>` | 1120 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了</src><tgt><\|wait\|></tgt>` | 853 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt><\|wait\|></tgt>` | 956 |

---

### Test Example 42 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1168 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>색인 번호 읽어봐야 </src><tgt><\|wait\|></tgt>` | 1712 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 850 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>연세 서름이듯 </src><tgt><\|wait\|></tgt>` | 1491 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>눈 개미 며 </src><tgt><\|wait\|></tgt>` | 1488 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1905 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1230 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1633 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 오면 물릴 거고 </src><tgt><\|wait\|></tgt>` | 2052 |
| 11 | `<src>신이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら</tgt>` | `<src>시눈 이 오면 </src><tgt>目を閉じて番号を読んでみれば、年老いようなものだ。目をこすり合わせて、一緒に遊ぼうというんだ。鬼が来たら噛みつき、目つきが来たら</tgt>` | 2730 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 찢겨 들어갑 </src><tgt><\|wait\|></tgt>` | 1429 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>조르 니까 </src><tgt><\|wait\|></tgt>` | 1080 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 673 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 935 |

---

### Test Example 43 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1378 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어 어찌 보면 </src><tgt><\|wait\|></tgt>` | 1149 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1480 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 656 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1552 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 1363 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>같은 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1961 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1065 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1700 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | 2002 |
| 11 | `<src>조금 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>조금 </src><tgt>嗯，怎么说呢，他就是和我们一起走过最20岁的人，也是一个像家人一样的弟弟。所以，比起责任感，</tgt>` | 2240 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1068 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1096 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | 1036 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | 611 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 1026 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1260 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 869 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>엄청 해맨입니다. </src><tgt><\|wait\|></tgt>` | 1420 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이 운전 을 할 건 </src><tgt><\|wait\|></tgt>` | 1146 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1415 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>거러 거로 다니 고는 </src><tgt><\|wait\|></tgt>` | 1646 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1849 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1188 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 </src><tgt><\|wait\|></tgt>` | 1727 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. </src><tgt><\|wait\|></tgt>` | 1969 |
| 11 | `<src>좀 창피 하네요. </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国就更惨了。真有点丢人。</tgt>` | `<src>좀 객관 적으로 </src><tgt>进去的话非常危险。要开车的话，走国道的话，去江北更是难说，出国的话也是很危险。客观地说，</tgt>` | 2133 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1205 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1143 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>무뤄봐요. 그거 는 </src><tgt><\|wait\|></tgt>` | 981 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>잘한 것 같아요. </src><tgt><\|wait\|></tgt>` | 585 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1300 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1015 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1250 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 905 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 1464 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 1655 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt><\|wait\|></tgt>` | 1875 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>of attainment. </src><tgt><\|wait\|></tgt>` | 1135 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1835 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, </src><tgt><\|wait\|></tgt>` | 1959 |
| 11 | `<src>That's another level of </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>학력 수준. 실제로 교육은 어느 정도까지 마쳤나요? 고등학교를 졸업했나요? 그게 한 단계의 학력 수준입니다. 대학에 다녔나요? 그렇다면 졸업했나요?</tgt>` | 2713 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt><\|wait\|></tgt>` | 1489 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1126 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. </src><tgt><\|wait\|></tgt>` | 579 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>I'll see you online. </src><tgt><\|wait\|></tgt>` | 1037 |

---

### Test Example 46 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1029 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1488 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 884 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1679 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1349 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is, </src><tgt><\|wait\|></tgt>` | 1862 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>is that because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 1676 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because </src><tgt><\|wait\|></tgt>` | 1297 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt><\|wait\|></tgt>` | 1956 |
| 11 | `<src>changed from 20 </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>活動、そして自分自身で基準を定義することです。なぜなら、あなたが完全に正しいからです。しかし現実には、私たちは新しい子だからです。そして基準は</tgt>` | 2203 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>changed from twenty years ago, </src><tgt><\|wait\|></tgt>` | 1243 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1210 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard </src><tgt><\|wait\|></tgt>` | 959 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point is being </src><tgt><\|wait\|></tgt>` | 475 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | 862 |

---

### Test Example 47 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1406 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1150 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>というだけではなくて、</src><tgt><\|wait\|></tgt>` | 1360 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 655 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1658 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも、フローグラフは</src><tgt><\|wait\|></tgt>` | 1644 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1764 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それ自体はPythonコード</src><tgt><\|wait\|></tgt>` | 1132 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>なんそっから</src><tgt><\|wait\|></tgt>` | 1632 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | 1919 |
| 11 | `<src>実行されることで</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>実行されることで</src><tgt>So, this isn't just a visual development environment; it's a visual Python development environment. Because FlowGraph writes in visual format, it generates Python code from that, and when that code is executed,</tgt>` | 2670 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 1345 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 977 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 838 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 913 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ、</src><tgt><\|wait\|></tgt>` | 538 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1288 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手的</src><tgt><\|wait\|></tgt>` | 1408 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>感情或</src><tgt><\|wait\|></tgt>` | 979 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的。</src><tgt><\|wait\|></tgt>` | 893 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1409 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1403 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>很多时候，</src><tgt><\|wait\|></tgt>` | 1556 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>经常会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1519 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1775 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1951 |
| 11 | `<src>这个人</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが「ほら、</tgt>` | `<src>这个人</src><tgt>相手の感情や真の意図を推し量ったり感じ取ったりすることです。多くの場合、人々はよくこう言います。「見て、この人は</tgt>` | 2276 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | 1204 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1046 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1006 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 567 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | 901 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 784 |

---

### Test Example 49 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1376 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 775 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | 1728 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 637 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1425 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1679 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1540 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1057 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt><\|wait\|></tgt>` | 1990 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1883 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>시장 을 주도 하면서 움직이 기 때문 에 </src><tgt>If the stock index is showing an upward trend, these large- cap stocks will likely rise sharply as well. However, since these smaller stocks move first and lead the market,</tgt>` | 2723 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1128 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 역시 초기 </src><tgt><\|wait\|></tgt>` | 1224 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목을 </src><tgt><\|wait\|></tgt>` | 897 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1009 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | 761 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계속 뭐 </src><tgt><\|wait\|></tgt>` | 1337 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>물론 이제 </src><tgt><\|wait\|></tgt>` | 1001 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1829 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 532 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1739 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨설턴트예요. </src><tgt><\|wait\|></tgt>` | 1717 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1299 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>B가 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | 1421 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1605 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 2018 |
| 11 | `<src>뿌렸 을 때 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、</tgt>` | `<src>주었을 때 </src><tgt>もちろん、こういうケースも時々あります。AさんとBさんがコンサルタントで、Bさんがコンサルタントです。Bさんが悪意のあるコードをAさんに与えた場合、</tgt>` | 2591 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 </src><tgt><\|wait\|></tgt>` | 1307 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 977 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스사이트 스킷에서 </src><tgt><\|wait\|></tgt>` | 897 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>EX 파일까지 </src><tgt><\|wait\|></tgt>` | 933 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 854 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1156 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 내놓았습니다. </src><tgt><\|wait\|></tgt>` | 1579 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 539 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자 의 편집 설을 보시면 </src><tgt><\|wait\|></tgt>` | 1709 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 1300 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>26MP의 </src><tgt><\|wait\|></tgt>` | 1730 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FHD 파이프 를 </src><tgt><\|wait\|></tgt>` | 1332 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1762 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮춘 것을 보여 줍니다. </src><tgt><\|wait\|></tgt>` | 2045 |
| 11 | `<src><\|wait\|></src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src><\|wait\|></src><tgt>これについて多くの人が分析を挙げています。この6.2の編集設定を見ると、Sonyが26MPのFHDパイプラインを128ビットに下げたことがわかります。</tgt>` | 2561 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>X 박스 시리즈 X에서도 </src><tgt><\|wait\|></tgt>` | 1421 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>없는 </src><tgt><\|wait\|></tgt>` | 906 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 887 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>SD가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 1018 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 782 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1045 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>佛陀一得</src><tgt><\|wait\|></tgt>` | 1156 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>阻止觉知到的那个现象，</src><tgt><\|wait\|></tgt>` | 1586 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 558 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>美当我们</src><tgt><\|wait\|></tgt>` | 1334 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | 1425 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | 1459 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1358 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>我们也同时进入</src><tgt><\|wait\|></tgt>` | 1753 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 906 |
| 11 | `<src>在早上的时候，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는</tgt>` | `<src>恨在场所的时候，</src><tgt>부처님께서 깨달음을 막는 그 현상을, 우리가 사랑 속에 있을 때, 소위 사랑이면서도 동시에 증오를</tgt>` | 2670 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>它是不害，</src><tgt><\|wait\|></tgt>` | 1082 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1154 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 1237 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 917 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>恨那个钟摆，</src><tgt><\|wait\|></tgt>` | 550 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 873 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | 725 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1254 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 1279 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to </src><tgt><\|wait\|></tgt>` | 1099 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 839 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1421 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | 1443 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1545 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>So, if you get into </src><tgt><\|wait\|></tgt>` | 1434 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt><\|wait\|></tgt>` | 1723 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>where you realize </src><tgt><\|wait\|></tgt>` | 1349 |
| 11 | `<src>you've added the wrong media </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>you've added the wrong media </src><tgt>另外，你将无法在资源之间移动媒体对象。所以，如果你遇到这种情况，发现你添加了错误的媒体文件，</tgt>` | 2072 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | 1125 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know. </src><tgt><\|wait\|></tgt>` | 1265 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>Now, we can see about </src><tgt><\|wait\|></tgt>` | 1274 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 968 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files </src><tgt><\|wait\|></tgt>` | 969 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 734 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>they get backed up properly. </src><tgt><\|wait\|></tgt>` | 515 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1582 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 778 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>on the first section </src><tgt><\|wait\|></tgt>` | 1249 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the EHR </src><tgt><\|wait\|></tgt>` | 1335 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>fields being of critical </src><tgt><\|wait\|></tgt>` | 1410 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1381 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>importance versus, </src><tgt><\|wait\|></tgt>` | 1552 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1593 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, which is obviously </src><tgt><\|wait\|></tgt>` | 792 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt>EHRの各分野の重要性について、ある程度混乱していました。それと、バリアントデータベースの重要性についてです。もちろん、それは私の大好きな分野の一つです。</tgt>` | 3027 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt><\|wait\|></tgt>` | 1027 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>if we don't agree </src><tgt><\|wait\|></tgt>` | 1252 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1178 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1091 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 732 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 543 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 700 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 470 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1264 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 780 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a hungry, </src><tgt><\|wait\|></tgt>` | 1244 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 959 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's been out there </src><tgt><\|wait\|></tgt>` | 1575 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in the wilderness </src><tgt><\|wait\|></tgt>` | 1407 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days, that he's hungry, </src><tgt><\|wait\|></tgt>` | 2167 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he sends </src><tgt><\|wait\|></tgt>` | 1095 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>to Jesus. </src><tgt><\|wait\|></tgt>` | 1613 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>Hey, if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | 2153 |
| 11 | `<src><\|wait\|></src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src><\|wait\|></src><tgt>ある時、彼はイエスが飢えていることを知っていました。彼は40日間荒野に出ていたことを知っていました。そして、イエスに送ったのです。「おい、もしお前が神の御子なら、証明してみろ」</tgt>` | 2880 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones to bread. </src><tgt><\|wait\|></tgt>` | 1142 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 1025 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>deal with </src><tgt><\|wait\|></tgt>` | 605 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>that temptation? </src><tgt><\|wait\|></tgt>` | 986 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 763 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan </src><tgt><\|wait\|></tgt>` | 438 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>led by bad alone. </src><tgt><\|wait\|></tgt>` | 336 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1186 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1173 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1324 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | 1434 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 2118 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1141 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1775 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1909 |
| 11 | `<src>these days, </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>有意义的个人权利，最高法院是最后才跟进的，而不是引领。我不认为法院想成为社会变革的前沿。如今，</tgt>` | 1749 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 960 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | 1207 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1154 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 930 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | 956 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 570 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 390 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>you have some federal judges </src><tgt><\|wait\|></tgt>` | 451 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 330 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 222 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1122 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1138 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1128 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是</src><tgt><\|wait\|></tgt>` | 1362 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>客厅的部分，</src><tgt><\|wait\|></tgt>` | 1352 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1532 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1359 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1677 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>我们休息的地方，</src><tgt><\|wait\|></tgt>` | 768 |
| 11 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>所以呢，</src><tgt>그럼 사진을 한번 살펴볼게요. 사진 부분에는 거실이 하나 보이는데요, 거실은 보통 우리가 쉬는 공간이라서,</tgt>` | 2863 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 986 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分会反映的是</src><tgt><\|wait\|></tgt>` | 1198 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 1013 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1040 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>一点时间可以</src><tgt><\|wait\|></tgt>` | 566 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>好好地坐下来休息，</src><tgt><\|wait\|></tgt>` | 981 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们可以看到这边是</src><tgt><\|wait\|></tgt>` | 810 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的吗？</src><tgt><\|wait\|></tgt>` | 489 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>哦，</src><tgt><\|wait\|></tgt>` | 388 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 383 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 951 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 925 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1145 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1203 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1287 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize the world </src><tgt><\|wait\|></tgt>` | 1424 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1399 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>the personality is </src><tgt><\|wait\|></tgt>` | 1573 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction, </src><tgt><\|wait\|></tgt>` | 1576 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 745 |
| 11 | `<src>While they're </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>while they're </src><tgt>これらの人々は極めて稀で、世界を完全に変革することがよくあります。その性格は矛盾をはらんでいます。彼らは</tgt>` | 2908 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted. </src><tgt><\|wait\|></tgt>` | 603 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>They also hate </src><tgt><\|wait\|></tgt>` | 870 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1127 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1172 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like it gets </src><tgt><\|wait\|></tgt>` | 1018 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>straight to the point. </src><tgt><\|wait\|></tgt>` | 985 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love to </src><tgt><\|wait\|></tgt>` | 740 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 350 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 393 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 360 |
| 22 | `<src>never shy away from a debate. </src><tgt>外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 366 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 346 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>INTP </src><tgt><\|wait\|></tgt>` | 329 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for. </src><tgt><\|wait\|></tgt>` | 346 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt><\|wait\|></tgt>` | 1422 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 명령 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1549 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 527 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1538 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1464 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1875 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1174 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1727 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 2038 |
| 11 | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok had made it seem like he was rejecting the government and that he was running for candidacy. He even seemed to be putting on a show for his candidacy. But now, the moment Yoon Suk- yeol removed Kim Jong- in,</tgt>` | 3094 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해도 </src><tgt><\|wait\|></tgt>` | 1298 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 880 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 686 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뜻끼를 </src><tgt><\|wait\|></tgt>` | 875 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt><\|wait\|></tgt>` | 770 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 471 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 394 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt><\|wait\|></tgt>` | 389 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>강세 발 </src><tgt><\|wait\|></tgt>` | 339 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 </src><tgt><\|wait\|></tgt>` | 340 |
| 22 | `<src><\|wait\|></src><tgt>Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>성상 랍건. </src><tgt><\|wait\|></tgt>` | 354 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 307 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 305 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 296 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂で</src><tgt><\|wait\|></tgt>` | 863 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってるみたいです。なので</src><tgt><\|wait\|></tgt>` | 1437 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>ここで</src><tgt><\|wait\|></tgt>` | 1089 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>もうそれのホテル</src><tgt><\|wait\|></tgt>` | 1306 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1330 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1411 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1191 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっているので</src><tgt><\|wait\|></tgt>` | 1052 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1616 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>ここゴルドーストーンホテル</src><tgt>Well, it seems they're making it right now at the diner. So, it's planned to be a place where you can have breakfast at that hotel too. So, going forward,</tgt>` | 3206 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいな</src><tgt><\|wait\|></tgt>` | 1054 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>っていう方はですね</src><tgt><\|wait\|></tgt>` | 1077 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なせて</src><tgt><\|wait\|></tgt>` | 1110 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみるとまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 975 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt><\|wait\|></tgt>` | 612 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>と思います。</src><tgt><\|wait\|></tgt>` | 892 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここのホテルからですね</src><tgt><\|wait\|></tgt>` | 828 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 471 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 416 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt><\|wait\|></tgt>` | 343 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel, it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 385 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんな辺りのね</src><tgt><\|wait\|></tgt>` | 342 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | 348 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | 296 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt>if you're thinking of staying there, I think it's a good idea to consider it. And since the hotel is located near Busan Station, you can walk there in about an hour or so,</tgt>` | 616 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 196 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 187 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は。</src><tgt><\|wait\|></tgt>` | 187 |
