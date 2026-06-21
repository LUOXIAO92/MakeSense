# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9513
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4106
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 683
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 0.6932
  - TGT_RELEASE_TOTAL: 88
  - TGT_WAIT_ACCURACY: 0.8163
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1316.5330
  - PROCESS_TIME_MS_P50: 1303.0430
  - PROCESS_TIME_MS_P95: 2132.6730
  - PROCESS_TIME_MS_MAX: 3795.0380

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
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 745 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 776 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲まだ一年生</src><tgt><\|wait\|></tgt>` | 1126 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>ですからね。</src><tgt>因为仲还在一年级。</tgt>` | 1325 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1218 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう密告</src><tgt>在那时候，</tgt>` | 1337 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1394 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう退ずして</src><tgt>我们把选举退出来，</tgt>` | 1770 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>あげると</src><tgt><\|wait\|></tgt>` | 1673 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt>十年后</tgt>` | 1538 |
| 11 | `<src>大した。</src><tgt>十年后也不会有什么大……</tgt>` | `<src>退した。</src><tgt><\|wait\|></tgt>` | 1008 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1137 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气数是容易的，</src><tgt>気数をつけるのは簡単です。</tgt>` | 1516 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 473 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>但是只有</src><tgt>ただ、</tgt>` | 1199 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导到</src><tgt><\|wait\|></tgt>` | 1193 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1572 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>如初于中坚。</src><tgt>師匠の指導がなければ、中堅にまで到達するのは難しいでしょう。</tgt>` | 2219 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt>ですから、</tgt>` | 744 |
| 9 | `<src>虚阿凡</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1616 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>反省が必要です。</tgt>` | 1791 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅，</src><tgt><\|wait\|></tgt>` | 1823 |

---

### Test Example 3 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1013 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘撒完以后呢，</src><tgt>淘を終えたら、</tgt>` | 1442 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的弹性</src><tgt><\|wait\|></tgt>` | 599 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也稍微</src><tgt>内部の弾力性も</tgt>` | 1839 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>弱了，然后就</src><tgt><\|wait\|></tgt>` | 972 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>停留在</src><tgt>少し弱くなり、</tgt>` | 1566 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1601 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>低能量的运行状态</src><tgt>比較的低いエネルギーの動作状態に留まり、</tgt>` | 1275 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>态。</src><tgt><\|wait\|></tgt>` | 1415 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これがいわゆる</tgt>` | 1860 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>低于状态。</src><tgt><\|wait\|></tgt>` | 1836 |

---

### Test Example 4 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1190 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>外在声音这一点，</src><tgt>Regarding the external sound,</tgt>` | 1140 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个优势很大。</src><tgt><\|wait\|></tgt>` | 797 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src><\|wait\|></src><tgt>this is a big advantage.</tgt>` | 1629 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 1049 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在面对</src><tgt><\|wait\|></tgt>` | 1484 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人</src><tgt><\|wait\|></tgt>` | 1211 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1580 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>这个特点，</src><tgt>And when I face this characteristic,</tgt>` | 1744 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1777 |
| 11 | `<src>仁儿。</src><tgt>this kind of walnut kernels.</tgt>` | `<src>这种和陶人。</src><tgt>this kind of interaction with Tao people.</tgt>` | 2133 |

---

### Test Example 5 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这儿开始，</tgt>` | 1037 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>初めての</src><tgt><\|wait\|></tgt>` | 866 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1118 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1368 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ごうぎゃん</src><tgt><\|wait\|></tgt>` | 1333 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>生産の</src><tgt><\|wait\|></tgt>` | 1412 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 687 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の</src><tgt><\|wait\|></tgt>` | 1671 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵</src><tgt><\|wait\|></tgt>` | 1959 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1722 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 939 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 842 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 1091 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1154 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설 용심이 가 </src><tgt><\|wait\|></tgt>` | 1470 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1416 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1723 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1290 |
| 9 | `<src>진짜 이거 </src><tgt>Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1697 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>헤엄으로도 조금 죽입니다. </src><tgt>I have a mix of sword and dragon heart. Wow, this really kills you, even in swimming.</tgt>` | 3085 |
| 11 | `<src>진짜. </src><tgt>seriously killer for a hangover, for real.</tgt>` | `<src>진짜 </src><tgt><\|wait\|></tgt>` | 882 |

---

### Test Example 7 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做什么？</src><tgt>What do parents need to do?</tgt>` | 1106 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 897 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们身生的爱</src><tgt><\|wait\|></tgt>` | 1513 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>交出来，</src><tgt>You need to give us your love,</tgt>` | 1296 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1357 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给</src><tgt><\|wait\|></tgt>` | 1107 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>出孩子心灵</src><tgt><\|wait\|></tgt>` | 1690 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>营养，</src><tgt><\|wait\|></tgt>` | 1728 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>给耐心的孩子</src><tgt><\|wait\|></tgt>` | 1773 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt>so that your child's heart is nourished and grows up with patience.</tgt>` | 2204 |

---

### Test Example 8 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1119 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 786 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1091 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learned as a repeat. </src><tgt>重复。重复学习。</tgt>` | 1465 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Finally, you're good at </src><tgt><\|wait\|></tgt>` | 1353 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>最后，你做得很好，多做一些。</tgt>` | 2245 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good </src><tgt><\|wait\|></tgt>` | 1498 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>at it. </src><tgt>嗯，你做得还不错，但不是很好。</tgt>` | 1539 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>People around you to help you with </src><tgt><\|wait\|></tgt>` | 910 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2166 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and and tell the next time </src><tgt><\|wait\|></tgt>` | 1564 |

---

### Test Example 9 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 956 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>saying? </src><tgt>你的身体在说什么？</tgt>` | 907 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 899 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does the </src><tgt><\|wait\|></tgt>` | 1519 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>tension start? </src><tgt>紧张感从哪里开始？</tgt>` | 1193 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>What is it? </src><tgt><\|wait\|></tgt>` | 1654 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head, is it a </src><tgt>是什么？是头？</tgt>` | 2029 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>tension in your chest? </src><tgt><\|wait\|></tgt>` | 853 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it a </src><tgt>还是胸部？</tgt>` | 1591 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>lengthen which are you </src><tgt><\|wait\|></tgt>` | 2298 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>using? </src><tgt>还是你正在使用的拉伸？</tgt>` | 1445 |

---

### Test Example 10 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1284 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt>Students on the list</tgt>` | 903 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 867 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>actually didn't have high intelligence,</tgt>` | 2163 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 772 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1721 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1520 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt>and are people who were selected randomly.</tgt>` | 1268 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1412 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1920 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교사 들은 </src><tgt>The teachers who didn't know the facts</tgt>` | 1978 |

---

### Test Example 11 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 791 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 849 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 슉빠시끼고 </src><tgt><\|wait\|></tgt>` | 1257 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1524 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1059 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모럴 조깅 </src><tgt><\|wait\|></tgt>` | 1693 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1449 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1168 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 1710 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1814 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt>I'm Apple, and I'm in the same generation as Herona Park and others.</tgt>` | 2237 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 832 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 736 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1124 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 1259 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem. </src><tgt>非常に幸せな人々の研究をしましたか？これはまさにその入り口です。</tgt>` | 2218 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>Research looking at </src><tgt><\|wait\|></tgt>` | 1126 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1608 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 955 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1665 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People that </src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>最も幸せな人々の10%を研究するものです。そこから私たちは学ぶことができます。</tgt>` | 2278 |

---

### Test Example 13 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>我们就是</src><tgt>When faced with this situation,</tgt>` | 905 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 868 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的</src><tgt><\|wait\|></tgt>` | 1313 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>汇报主管，或是通知对方</src><tgt><\|wait\|></tgt>` | 1352 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们一下这个状况，</src><tgt>we quickly report it to our supervisor or notify them about the situation.</tgt>` | 2552 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1427 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't think you have to handle everything yourself.</tgt>` | 1732 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>扛得起多大</src><tgt><\|wait\|></tgt>` | 613 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>的承担？真的而已，</src><tgt>How much can you really handle? It's just a matter of time.</tgt>` | 3142 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>所以就属上。</src><tgt><\|wait\|></tgt>` | 739 |

---

### Test Example 14 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1046 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt>T-shirts and</tgt>` | 787 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あのいただろうといった</src><tgt><\|wait\|></tgt>` | 1139 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ようなものも用意しております</src><tgt>other items like that are also available.</tgt>` | 1212 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 1341 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt>So please come and join us.</tgt>` | 1372 |
| 7 | `<src>ご連絡としては</src><tgt>so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt>For contact, that's all.</tgt>` | 1720 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>けど</src><tgt><\|wait\|></tgt>` | 1670 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>何しろ</src><tgt>But</tgt>` | 1169 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>人数が</src><tgt><\|wait\|></tgt>` | 1401 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>あまりがありませんので少々お待ちください。</src><tgt>since there aren't many people, please wait a moment.</tgt>` | 1620 |

---

### Test Example 15 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>あとなんか</src><tgt><\|wait\|></tgt>` | 1306 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>ちょっと距離が離れてくる</src><tgt>还有，</tgt>` | 1002 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 780 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>大将が</src><tgt>大将好像有点想</tgt>` | 1315 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱりこうですね</src><tgt><\|wait\|></tgt>` | 1221 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>会話したい方って</src><tgt>聊聊</tgt>` | 1328 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行き来しきただい</src><tgt><\|wait\|></tgt>` | 1757 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>し。</src><tgt>的话，会一直来来回来。</tgt>` | 1424 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>でね</src><tgt><\|wait\|></tgt>` | 1705 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と多分その人にとっては</src><tgt>而且，</tgt>` | 1778 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>すごく強いので。</src><tgt><\|wait\|></tgt>` | 1740 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt>因为那个人对他来说非常强烈，所以</tgt>` | 714 |

---

### Test Example 16 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 775 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAがですね</src><tgt>As for AA,</tgt>` | 818 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1129 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>正則かどうか</src><tgt><\|wait\|></tgt>` | 1133 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>っていう場合時に</src><tgt><\|wait\|></tgt>` | 1391 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAAの乱交を</src><tgt><\|wait\|></tgt>` | 1364 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べてということで</src><tgt><\|wait\|></tgt>` | 1421 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あの正則かどうか</src><tgt><\|wait\|></tgt>` | 1735 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を調べる正則かどうか</src><tgt><\|wait\|></tgt>` | 1792 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>を保証する</src><tgt><\|wait\|></tgt>` | 1871 |
| 11 | `<src>といったような</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1655 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されます。</src><tgt>it's used to check if AA is regular in various situations, and to guarantee that it is regular.</tgt>` | 1194 |

---

### Test Example 17 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 831 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>그래서 여기서</tgt>` | 763 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 1077 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>to set up </src><tgt><\|wait\|></tgt>` | 828 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>7GBが</src><tgt>7GB를</tgt>` | 1055 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>ありましたが、</src><tgt><\|wait\|></tgt>` | 958 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>설정하려고 했는데,</tgt>` | 1702 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>ハセキーヨシの仕組み</src><tgt><\|wait\|></tgt>` | 1786 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>하세키요시의 메커니즘은</tgt>` | 1368 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>もうコン</src><tgt><\|wait\|></tgt>` | 1283 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7GB</src><tgt><\|wait\|></tgt>` | 2008 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1777 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビです。</src><tgt>이미 7GB입니다.</tgt>` | 1360 |

---

### Test Example 18 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1169 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>And then, </src><tgt>好的。然后，</tgt>` | 931 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 977 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1321 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1208 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1444 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1383 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1408 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 567 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>这些例子之后，指令告诉我们实际要使用这些值。所以</tgt>` | 1687 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2258 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>this game.board array </src><tgt>这个game.board数组</tgt>` | 1446 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 671 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 860 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个</src><tgt><\|wait\|></tgt>` | 1107 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道，让我</src><tgt>제 삶의 궤도로 돌아가게 해 주세요.</tgt>` | 2066 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>能够好自在</src><tgt><\|wait\|></tgt>` | 835 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>他下班的时候，</src><tgt>퇴근할 때 편안하게</tgt>` | 1920 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在工作</src><tgt><\|wait\|></tgt>` | 1379 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>和朋友聊天，</src><tgt>친구들과 수다 떨고</tgt>` | 1251 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就这么</src><tgt><\|wait\|></tgt>` | 1411 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>而不是被他</src><tgt>싶어요. 그저</tgt>` | 2416 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>做一些小小的愿望</src><tgt><\|wait\|></tgt>` | 1436 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>哦。</src><tgt>작은 소원 같은 걸 빌어주는 게 아니에요.</tgt>` | 1768 |

---

### Test Example 20 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 922 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 층을 </src><tgt><\|wait\|></tgt>` | 936 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여 달라고 주고 내가 </src><tgt><\|wait\|></tgt>` | 1087 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수도다. </src><tgt>I might have come here to kill someone on another floor.</tgt>` | 2386 |
| 5 | `<src>다른 잔찜에 </src><tgt>came in here to do it.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1315 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔팀이 죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1586 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>하자나? 내가 </src><tgt>The other team is asking for a kill, right? I</tgt>` | 1715 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1755 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>줄은 아니야. </src><tgt>am not one of those people who don't hear that.</tgt>` | 3187 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 780 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1700 |

---

### Test Example 21 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴 찌 너무 </src><tgt><\|wait\|></tgt>` | 1416 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 588 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>이 저열하려 했지만 </src><tgt>これ、あまりにも低く抑えようとしていましたが、</tgt>` | 1459 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1476 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt>本当に菩薩です。いや、自分の</tgt>` | 1358 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 피로 고 </src><tgt><\|wait\|></tgt>` | 1598 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보이 고 </src><tgt>菩薩で夢にうつるような方で、</tgt>` | 1952 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 이 보살 로 </src><tgt><\|wait\|></tgt>` | 1706 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 피로 고 보이 세 우주 까지 </src><tgt>私だけが菩薩に見えるように、宇宙まで</tgt>` | 1968 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>다왔는데 이 보살 이란 </src><tgt><\|wait\|></tgt>` | 2042 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>그냥 </src><tgt>来て、この菩薩はただの</tgt>` | 1886 |

---

### Test Example 22 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1130 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 788 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1153 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1403 |
| 5 | `<src>history as a guide </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1190 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change can </src><tgt><\|wait\|></tgt>` | 1465 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1471 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>happen in the United States. </src><tgt><\|wait\|></tgt>` | 1754 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1738 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meaning of the amendment </src><tgt><\|wait\|></tgt>` | 1730 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, I'm </src><tgt><\|wait\|></tgt>` | 857 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Maryed. </src><tgt><\|wait\|></tgt>` | 1742 |

---

### Test Example 23 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 724 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生与</src><tgt><\|wait\|></tgt>` | 882 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>长相不怪的人之间，</src><tgt>If you're in a relationship with a guy who's not too striking,</tgt>` | 1996 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>又这么重要，</src><tgt><\|wait\|></tgt>` | 1062 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>你</src><tgt><\|wait\|></tgt>` | 748 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1576 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1242 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天而异</src><tgt><\|wait\|></tgt>` | 1475 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>you're going to be as important as this? Are you going to be as important as this as you were when you first started dating?</tgt>` | 2188 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2122 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1381 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>学历年偏。</src><tgt>Yang Zisi's academic background is quite high.</tgt>` | 2134 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 952 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼</tgt>` | 908 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 891 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. And when those </src><tgt>화학 결합도 에너지를 저장합니다. 그리고</tgt>` | 2372 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1040 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy gets </src><tgt>결합이 끊어지면</tgt>` | 1468 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to </src><tgt><\|wait\|></tgt>` | 1291 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt>그 잠재 에너지는 다른 형태의 에너지로 변환됩니다. 예를 들어</tgt>` | 2362 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light. </src><tgt><\|wait\|></tgt>` | 464 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>열이나 빛으로 변환됩니다. 또는</tgt>` | 3032 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make different bonds. </src><tgt><\|wait\|></tgt>` | 801 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>다른 결합을 만드는 데 사용됩니다.</tgt>` | 2108 |

---

### Test Example 25 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 915 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Chunhatteru. </src><tgt>제 이름은 춘하터입니다.</tgt>` | 1630 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 513 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src>in a BA in </src><tgt><\|wait\|></tgt>` | 1517 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance </src><tgt><\|wait\|></tgt>` | 911 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a B.A. in Psychology. </src><tgt>현재 경영 금융학 학사 학위와 심리학 학사 학위를 전공하고 있습니다.</tgt>` | 2964 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1387 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yale, </src><tgt>여기 예일 대학교에서는</tgt>` | 1768 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1870 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>앞으로</tgt>` | 2000 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1673 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1158 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1069 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 865 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1136 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>信号が</src><tgt>기어가 헐거워지면</tgt>` | 1745 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>出せなくなって</src><tgt><\|wait\|></tgt>` | 1028 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>しまうので、</src><tgt>신호가 안 나가서</tgt>` | 1773 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1604 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 950 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1635 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 2037 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt>기어 끝에 역나사 너트가 붙어 있는 거죠.</tgt>` | 1949 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい</src><tgt><\|wait\|></tgt>` | 1658 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文型完了を</src><tgt><\|wait\|></tgt>` | 1165 |

---

### Test Example 27 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150개 가 </src><tgt>そのうち150個は</tgt>` | 1398 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중화 벌써 100만으로 </src><tgt><\|wait\|></tgt>` | 875 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな企業が</tgt>` | 1564 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 831 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くありました。一般的には</tgt>` | 1765 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 기업 들은 </src><tgt><\|wait\|></tgt>` | 1705 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>小さな企業は成長するか、あるいは</tgt>` | 1464 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>해화법에 의해 거대 해가 된데 </src><tgt><\|wait\|></tgt>` | 1179 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>이번 에 </src><tgt>今回の</tgt>` | 1760 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성기 없던 성장 도 </src><tgt><\|wait\|></tgt>` | 1901 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>폐업도 하지 않은 </src><tgt>成長も廃業もしていない</tgt>` | 1680 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들들이 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1208 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 843 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>就是说</src><tgt>2つ目は、</tgt>` | 839 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二吉时，</src><tgt><\|wait\|></tgt>` | 1116 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>会福在一期</src><tgt>二吉時、</tgt>` | 1438 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1158 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>线平安的大牛们。</src><tgt>平安な大牛たちが一期一線に福を招きます。</tgt>` | 2229 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1386 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 963 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>维信运动好事期间，</src><tgt>例えば、維信運動の好事期間に</tgt>` | 1827 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1868 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维信运动</src><tgt><\|wait\|></tgt>` | 1797 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>平分的星棒，</src><tgt>維信運動の星棒が均等に配られるのを見かけるでしょう。</tgt>` | 1994 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1084 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 972 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이런 것들은 </src><tgt>These things, like vanadium,</tgt>` | 1115 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유용 실은 </src><tgt><\|wait\|></tgt>` | 806 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>뭐 거의 </src><tgt><\|wait\|></tgt>` | 1401 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 그런 기능 이랄 </src><tgt><\|wait\|></tgt>` | 1297 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>정도 고 굉장히 </src><tgt><\|wait\|></tgt>` | 1568 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1224 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다. </src><tgt>are very useful. They have functions that are almost similar to those of</tgt>` | 1744 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이거 굉장히 </src><tgt><\|wait\|></tgt>` | 1489 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1985 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt>minerals. They are very, very much like that. Now,</tgt>` | 1994 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1902 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아니면 </src><tgt><\|wait\|></tgt>` | 1082 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1175 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在这个</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 898 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，不是</src><tgt><\|wait\|></tgt>` | 974 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>以前造成的，</src><tgt>このローマは以前から</tgt>` | 1649 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 950 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>作られたものではありません。ですから、</tgt>` | 1783 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>有什么</src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>一些遗迹啊，</src><tgt>今ある遺跡や</tgt>` | 1081 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景</src><tgt><\|wait\|></tgt>` | 1655 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是</src><tgt>風景は、</tgt>` | 1752 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一致</src><tgt><\|wait\|></tgt>` | 1633 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>改变出来的。</src><tgt>一様に変わったものではありません。</tgt>` | 735 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此，</src><tgt><\|wait\|></tgt>` | 1742 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>会建议各位的朋友呢，</src><tgt>ですから、皆さんには</tgt>` | 1223 |

---

### Test Example 31 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 887 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then,</tgt>` | 884 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无反弹，</src><tgt><\|wait\|></tgt>` | 1093 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src>所以</src><tgt>with no rebound,</tgt>` | 1164 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1361 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1303 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>来整段，</src><tgt><\|wait\|></tgt>` | 1725 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 1725 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 1765 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>so we stuck with it. The deadline was about twelve days. We just kept pushing, and it was all fine.</tgt>` | 2306 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>当然都很</src><tgt><\|wait\|></tgt>` | 1796 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一火的离开。</src><tgt>Of course, they all left in a blaze of fire.</tgt>` | 1305 |

---

### Test Example 32 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1282 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt>あるいは、</tgt>` | 466 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1072 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何か書く必要がある場合、テキストを書く場合、</tgt>` | 2104 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 861 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>そもそも</tgt>` | 1572 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1682 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>and it's like oh, </src><tgt>スペルがわからない、なんてことになって、</tgt>` | 2005 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 807 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>start with a double </src><tgt><\|wait\|></tgt>` | 2276 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>p, double </src><tgt><\|wait\|></tgt>` | 1414 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>l, I don't know </src><tgt>「この単語は『pp』で始まる、</tgt>` | 2136 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1163 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 937 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>这章的部分我们看到的是</src><tgt>이 장의 부분은</tgt>` | 1297 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 573 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>带调的人，但是他是</src><tgt>조절하는 사람입니다. 하지만</tgt>` | 2056 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的</src><tgt><\|wait\|></tgt>` | 822 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1503 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这种场那种</src><tgt><\|wait\|></tgt>` | 1618 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>这样一个状况，需要去特别</src><tgt><\|wait\|></tgt>` | 1020 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>注意的是</src><tgt><\|wait\|></tgt>` | 1613 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1737 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 1594 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他调不到</src><tgt><\|wait\|></tgt>` | 788 |
| 13 | `<src><\|wait\|></src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1817 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>了。</src><tgt>역방향적인 이런 상황에서 특별히 주의할 점은 그가 당신의 의식과 조화를 이룰 수 있는지 여부입니다.</tgt>` | 1863 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 895 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到一个天头，</src><tgt>天頭に達した</tgt>` | 1188 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 684 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了天头之后，</src><tgt>天頭に達した後は、</tgt>` | 1960 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 870 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>就要先</src><tgt><\|wait\|></tgt>` | 1542 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt>必ず守り、</tgt>` | 1683 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想着哎，那我</src><tgt><\|wait\|></tgt>` | 998 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>再去操作</src><tgt>「よし、</tgt>` | 1600 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 1801 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>操作しよう」なんて考えないでください。</tgt>` | 2102 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1693 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt>なぜそう言うのかというと、</tgt>` | 1093 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1248 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1082 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事。</tgt>` | 788 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>There was such </src><tgt><\|wait\|></tgt>` | 969 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>interest before, </src><tgt>之前</tgt>` | 1126 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1369 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>net future TC. </src><tgt>NetFutureTC</tgt>` | 1338 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1432 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>And so this is just </src><tgt>就是这样，</tgt>` | 1744 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1671 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>to look at. </src><tgt>另一个地方可以看看。</tgt>` | 629 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2006 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1350 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1334 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>working on Bug Repos should be </src><tgt><\|wait\|></tgt>` | 960 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt>但那些在BugRepos上工作的开发者或工程师应该知道这一点。</tgt>` | 1755 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十二手とか</src><tgt><\|wait\|></tgt>` | 933 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>言った。おそらく</src><tgt>他说十二手。大概</tgt>` | 1095 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 1528 |
| 5 | `<src>まあ</src><tgt>差不多十秒。</tgt>` | `<src>まあ</src><tgt>十秒内</tgt>` | 948 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1417 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一秒ぐらいの</src><tgt>一秒左右</tgt>` | 1389 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>せつなんつか</src><tgt><\|wait\|></tgt>` | 1624 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>ね。</src><tgt>的节奏。</tgt>` | 1647 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 903 |
| 11 | `<src>おそらく</src><tgt>然后</tgt>` | `<src>おそらく</src><tgt>大概</tgt>` | 1278 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十二手</src><tgt><\|wait\|></tgt>` | 1780 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt>十二手，</tgt>` | 1473 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 653 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt>宫马之类的</tgt>` | 1130 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 853 |

---

### Test Example 37 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 742 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니 뭐니 </src><tgt>知っていること、知らないこと、</tgt>` | 1306 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 805 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>異邦人としてここにいるとき、</tgt>` | 2131 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 713 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>우상 에게로 </src><tgt>言葉を失う偶像に</tgt>` | 1839 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1363 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>끌려 갔느라 </src><tgt>そのまま連れて行かれ、</tgt>` | 1395 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1265 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그럼 으로 내가 </src><tgt>その結果、</tgt>` | 2005 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1776 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리노니 </src><tgt>あなたたちに</tgt>` | 771 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 </src><tgt><\|wait\|></tgt>` | 1437 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>영으로 말하는 자는 </src><tgt>神の霊で語る者は</tgt>` | 1396 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 850 |

---

### Test Example 38 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 910 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃，</src><tgt>呃，</tgt>` | 655 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>H텔멜이라고 하는 </src><tgt><\|wait\|></tgt>` | 1149 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피터도 </src><tgt>H텔멜</tgt>` | 1408 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1234 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 </src><tgt>这个计算机也能理解，</tgt>` | 1882 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1646 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>있는 컴퓨터 어노에 </src><tgt>还有</tgt>` | 1017 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 </src><tgt><\|wait\|></tgt>` | 1570 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>말 같게 우리 가 이제 </src><tgt>像语法一样，</tgt>` | 1861 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1745 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>我们得写代码，</tgt>` | 502 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1873 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1229 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt>需要一个程序来写这些代码。</tgt>` | 1105 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1222 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>getting going </src><tgt>これから</tgt>` | 594 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1123 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1070 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt>やるべきことがたくさんある人、</tgt>` | 1510 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 1349 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1470 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 1063 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I have about one </src><tgt><\|wait\|></tgt>` | 1149 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 2150 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at the fall this video. </src><tgt>この動画で1分くらいの動画を1つ作ります。それから、</tgt>` | 1753 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage of each one </src><tgt><\|wait\|></tgt>` | 1998 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1456 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt>それぞれの動画をもう少し詳しく解説します。</tgt>` | 928 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1140 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个财运可以说是</src><tgt>財運についてですが、</tgt>` | 1106 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 696 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较欠账的部分</src><tgt>かなり良い方ですが、</tgt>` | 1738 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 801 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>在事业方面的业绩</src><tgt>事業の業績が</tgt>` | 1811 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>相对所代表的红利</src><tgt><\|wait\|></tgt>` | 1715 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>以及收入的提升</src><tgt>それに見合う利益や収入の増加が</tgt>` | 1510 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1147 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>如果是在投资理财方面</src><tgt>投資や資産運用に関しては、</tgt>` | 2833 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月也是</src><tgt><\|wait\|></tgt>` | 1025 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>不错，只是</src><tgt>今月も悪くないですが、</tgt>` | 1724 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对财运来说，</src><tgt><\|wait\|></tgt>` | 1144 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>就算</src><tgt>財運としては、</tgt>` | 1155 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>入了那么一点。</src><tgt><\|wait\|></tgt>` | 816 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1123 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>세인보라 </src><tgt><\|wait\|></tgt>` | 851 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt>目を閉じて、戦えばいいんだ。</tgt>` | 1230 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>이제 서름이 </src><tgt><\|wait\|></tgt>` | 1539 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 차리 돋은 </src><tgt><\|wait\|></tgt>` | 1246 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1389 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>한들어서 </src><tgt><\|wait\|></tgt>` | 1247 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>もう目も覚めて、体も覚めて、一緒に遊ぼうってこと。</tgt>` | 1721 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1541 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>어물일 거고 </src><tgt><\|wait\|></tgt>` | 1786 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 어물이야. </src><tgt>敵は厄介なやつだ。敵は厄介なやつだ。</tgt>` | 2252 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1916 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>인찔러 주다니까 </src><tgt>守ってくれって言ったら、</tgt>` | 1267 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 마음 에. </src><tgt><\|wait\|></tgt>` | 1053 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감음. </src><tgt>心は安らか。目を閉じる。</tgt>` | 1017 |

---

### Test Example 42 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1188 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>锤模和感知的</src><tgt><\|wait\|></tgt>` | 990 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>目标感火真实</src><tgt><\|wait\|></tgt>` | 868 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>图片的</src><tgt><\|wait\|></tgt>` | 1114 |
| 5 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1313 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1308 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1438 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1736 |
| 9 | `<src>这样说：“</src><tgt>よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1760 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1832 |
| 11 | `<src>这个人</src><tgt>「ほら、</tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1722 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>说谎了。</src><tgt><\|wait\|></tgt>` | 560 |
| 13 | `<src>他的眼睛</src><tgt>また嘘をついている。目が</tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1870 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 1159 |
| 15 | `<src><\|wait\|></src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 995 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说</src><tgt><\|wait\|></tgt>` | 953 |
| 17 | `<src><\|wait\|></src><tgt>つまり…</tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 613 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1176 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. How far </src><tgt>학력 수준. 얼마나</tgt>` | 1209 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 691 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1536 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>go in your education? </src><tgt>실제로 교육을 얼마나 받았나요?</tgt>` | 1379 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 1779 |
| 7 | `<src><\|wait\|></src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>That's one level of </src><tgt>고등학교를 졸업했나요? 그건</tgt>` | 2174 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1707 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>한 단계의 학력입니다. 대학에 갔나요?</tgt>` | 1866 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, did you graduate? </src><tgt><\|wait\|></tgt>` | 2085 |
| 11 | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of </src><tgt>그래서 졸업했나요? 또 다른 단계의</tgt>` | 1737 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1020 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for now. </src><tgt>학력입니다. 지금은 여기까지입니다.</tgt>` | 1383 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 949 |
| 15 | `<src>online. </src><tgt>오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 761 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>드러가면 </src><tgt><\|wait\|></tgt>` | 1291 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 해명 입니다. </src><tgt>这简直是天大的辩解。</tgt>` | 1404 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 512 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1618 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>거로 다니 고 </src><tgt><\|wait\|></tgt>` | 1018 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그러면 뭐 </src><tgt><\|wait\|></tgt>` | 1633 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1649 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1026 |
| 9 | `<src><\|wait\|></src><tgt>就不用说了，去外国</tgt>` | `<src>외국 에게 나가 는 것도 당연 이요. </src><tgt>既然是开车来的，那去江南区当然没得说，去国外也理所当然。</tgt>` | 2108 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1936 |
| 11 | `<src>좀 창피 하네요. </src><tgt>就更惨了。真有点丢人。</tgt>` | `<src>신기 하네요. </src><tgt>挺神奇的。</tgt>` | 1549 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1705 |
| 13 | `<src>이제 </src><tgt>不过，</tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1021 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>노발 요. 그거 는 </src><tgt>不如努力工作吧。那</tgt>` | 1358 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>나인 것 같아요. </src><tgt><\|wait\|></tgt>` | 1111 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>我觉得更靠谱。</tgt>` | 644 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 967 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 832 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt>基準を自分たちで定義することです。</tgt>` | 1975 |
| 5 | `<src>absolutely correct, </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 969 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt>全くその通りですが、</tgt>` | 1623 |
| 7 | `<src>is is that </src><tgt>しかし現実には、</tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1499 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat and </src><tgt>現実として、私たちは</tgt>` | 1063 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, and because </src><tgt><\|wait\|></tgt>` | 1634 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>新しい猫とブロックであり、</tgt>` | 2414 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1404 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>20 years ago, we </src><tgt>20年前に比べて基準が変わってしまったので、</tgt>` | 1862 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>are being held to </src><tgt><\|wait\|></tgt>` | 1107 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard </src><tgt>私たちは</tgt>` | 1055 |
| 15 | `<src>everything at this point is being </src><tgt>より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 879 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher standard </src><tgt>この時点ではより高い基準を</tgt>` | 969 |

---

### Test Example 46 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 996 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>濡らせてやる。</src><tgt>그럼 젖게 해줄게.</tgt>` | 1133 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 868 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1217 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>ひどい女見てる。</src><tgt>나는 끔찍한 여자를 보고 있어.</tgt>` | 1732 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1559 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1656 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 962 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>ふれをキセキう。</src><tgt>이제 한계는 아득히 넘어섰어. 이 접촉은 기적이야.</tgt>` | 2000 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2196 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1368 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなデイコを</src><tgt><\|wait\|></tgt>` | 1755 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってる。</src><tgt>오랫동안 부나 데이코를 해왔어.</tgt>` | 1389 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 950 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい解毒線を</src><tgt><\|wait\|></tgt>` | 828 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt>나는 이렇게 대단한 해독선을 본 적이 없어.</tgt>` | 959 |

---

### Test Example 47 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어차피 보면 </src><tgt>反正</tgt>` | 780 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1195 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1209 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt>这个弟弟，他跟我们一起过了二十岁，</tgt>` | 1765 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 1597 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>也是像家人一样的弟弟。</tgt>` | 1838 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 793 |
| 9 | `<src><\|wait\|></src><tgt>所以</tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1554 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인감모다는 </src><tgt><\|wait\|></tgt>` | 2011 |
| 11 | `<src>조금 </src><tgt>比起责任感，</tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1872 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1773 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 1160 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내놓고 </src><tgt><\|wait\|></tgt>` | 844 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt>所以，希望他能多展现一些自己，多开心。</tgt>` | 1089 |

---

### Test Example 48 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 1170 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>This is</tgt>` | 902 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうやつで、</src><tgt><\|wait\|></tgt>` | 973 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1320 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt>a visual development environment. It's a visual Python development environment.</tgt>` | 1764 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1301 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルの書いてあと</src><tgt><\|wait\|></tgt>` | 1873 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>これやつはPython</src><tgt><\|wait\|></tgt>` | 971 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>コードなんそっから生成される</src><tgt><\|wait\|></tgt>` | 1648 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつはそれが</src><tgt><\|wait\|></tgt>` | 2305 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1431 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1677 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことに</src><tgt><\|wait\|></tgt>` | 1001 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているからですね。</src><tgt>It's a flow graph visual. You write the flow graph, and then the Python code is generated from it. When that code runs, it performs signal processing.</tgt>` | 2126 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 591 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ</src><tgt>Okay.</tgt>` | 546 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 861 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>そして、これについて多くの人々が</tgt>` | 1211 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 801 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 로쿠자 </src><tgt>分析をしています。ここで</tgt>` | 1736 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 928 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>Sonyの分析を見ると、</tgt>` | 1653 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 60초에 </src><tgt><\|wait\|></tgt>` | 1818 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FP 파이프를 </src><tgt>60秒でFPパイプを</tgt>` | 1609 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 991 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>낮춘 것을 로포인 다. </src><tgt>128ビットに下げていることがわかります。</tgt>` | 3116 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 782 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt>Xboxシリーズにはない</tgt>` | 2018 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1384 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>CS가 </src><tgt>InfinityCacheCSが</tgt>` | 803 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>여기도 없다. </src><tgt><\|wait\|></tgt>` | 983 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>ここにもありません。</tgt>` | 648 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>ですから、もちろん</tgt>` | 806 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1306 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースもあります。Aという方と</tgt>` | 2143 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 713 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 큰 텐트예요. </src><tgt>Bという方がお互いに大きなテントです。</tgt>` | 2270 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>왜 이렇게 큰 텐트 여야 </src><tgt><\|wait\|></tgt>` | 1787 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>하니까 </src><tgt>なぜこんなに大きなテントが必要なのか、</tgt>` | 1759 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람이 </src><tgt><\|wait\|></tgt>` | 1844 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aという方が</tgt>` | 1992 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1121 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt>悪意のあるコードを渡した時に、Bという方が</tgt>` | 1373 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로 사이트 </src><tgt><\|wait\|></tgt>` | 1380 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>스크립트에서 </src><tgt>実際のクロスサイトスクリプトで</tgt>` | 700 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>XSS까지 </src><tgt><\|wait\|></tgt>` | 795 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>가능히 될까? </src><tgt>XSSまで可能になるのか、</tgt>` | 738 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>for all </src><tgt><\|wait\|></tgt>` | 768 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>the source </src><tgt><\|wait\|></tgt>` | 742 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>that is recognized. </src><tgt>인정받은 모든 출처에 대해</tgt>` | 1297 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>But when we </src><tgt><\|wait\|></tgt>` | 1419 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1074 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>study it, </src><tgt>연구할 때</tgt>` | 1446 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>the source of the love </src><tgt><\|wait\|></tgt>` | 1466 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src>we also </src><tgt><\|wait\|></tgt>` | 1456 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>can also enter </src><tgt><\|wait\|></tgt>` | 1581 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 438 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the source of the love </src><tgt><\|wait\|></tgt>` | 2548 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>that is in the heart. </src><tgt>마음속에 있는 사랑의 근원도 알 수 있습니다.</tgt>` | 1316 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It comes to the end. </src><tgt><\|wait\|></tgt>` | 1978 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>It becomes </src><tgt>그것은 결국</tgt>` | 1067 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the love </src><tgt><\|wait\|></tgt>` | 995 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>that is the same. </src><tgt>같은 사랑이 됩니다.</tgt>` | 1145 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt><\|wait\|></tgt>` | 620 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>in one. </src><tgt>계속됩니다.</tgt>` | 479 |

---

### Test Example 52 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 절수가 </src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt>The stock price is now rising,</tgt>` | 1110 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 812 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1820 |
| 5 | `<src>큰 폭의 </src><tgt>these large- cap stocks</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 871 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1826 |
| 7 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 1085 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1590 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 2012 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직 이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1853 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1609 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요소 1초기 </src><tgt><\|wait\|></tgt>` | 987 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 온 종목 을 </src><tgt><\|wait\|></tgt>` | 1370 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 될 것 같습니다. </src><tgt>and while these large- cap stocks will likely see a big surge, it seems we'll need to watch the variable- cap stocks first, as they're the ones that lead the market. So, we'll need to watch the variable- cap stocks with our eyes.</tgt>` | 2144 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 404 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1129 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, you will not </src><tgt>另外，</tgt>` | 905 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 902 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>be able to move media objects </src><tgt><\|wait\|></tgt>` | 1725 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 960 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>你无法在资源之间移动媒体对象。</tgt>` | 1951 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So if </src><tgt><\|wait\|></tgt>` | 1524 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into the situation </src><tgt><\|wait\|></tgt>` | 1068 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1547 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize you've added </src><tgt><\|wait\|></tgt>` | 1837 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file, </src><tgt><\|wait\|></tgt>` | 1984 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>to a particular resource, </src><tgt><\|wait\|></tgt>` | 1130 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>we'll let us know. </src><tgt>如果你发现把媒体文件加到了错误的资源上，我们会通知你。</tgt>` | 1612 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>Now we can see about </src><tgt><\|wait\|></tgt>` | 1302 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those media files </src><tgt><\|wait\|></tgt>` | 867 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>and then making sure </src><tgt>然后我们再看看怎么移动这些媒体文件，并确保</tgt>` | 1005 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get back up </src><tgt><\|wait\|></tgt>` | 450 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>它们能正确恢复。</tgt>` | 377 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>and it warns Jesus </src><tgt>ある時、イエスは</tgt>` | 1004 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>of hunger. </src><tgt><\|wait\|></tgt>` | 676 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>He knows that </src><tgt>飢えについて警告します。彼は</tgt>` | 1966 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>is going to </src><tgt><\|wait\|></tgt>` | 822 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>be in the wilderness </src><tgt>荒野に</tgt>` | 1603 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry. </src><tgt><\|wait\|></tgt>` | 1921 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>And so he says to </src><tgt>40日間飢えに苦しむことになるだろうと知っています。そこで</tgt>` | 2119 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 475 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the son of God, prove it </src><tgt>イエスよ、もしあなたが神の子なら、</tgt>` | 3167 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 667 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>turn these stones to bread. </src><tgt>この石をパンに変えてみせなさい。</tgt>` | 2151 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 1364 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>deal with that </src><tgt>イエスは</tgt>` | 698 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 950 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src><\|wait\|></src><tgt>その誘惑にどう対処したのでしょうか？</tgt>` | 709 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 523 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>いや、ジョナタンはパンで導いた。一人で。</tgt>` | 570 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1189 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 744 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, and </src><tgt><\|wait\|></tgt>` | 1142 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>the Supreme Court </src><tgt><\|wait\|></tgt>` | 1154 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1411 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't I don't </src><tgt><\|wait\|></tgt>` | 1934 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>have the courts want to be </src><tgt><\|wait\|></tgt>` | 1713 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 954 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1641 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1755 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 1695 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 649 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1793 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1060 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1029 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 808 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 718 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 409 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 478 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 423 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 315 |

---

### Test Example 56 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1441 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt>最初の数マイルは</tgt>` | 1009 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 776 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt><\|wait\|></tgt>` | 1204 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1226 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1316 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 1386 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1403 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant data </src><tgt><\|wait\|></tgt>` | 616 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>bases, which is obviously </src><tgt><\|wait\|></tgt>` | 1725 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>not of my loves. </src><tgt>AHRフィールドの重要性について、最初のセクションで少し間違った道を進んでしまいました。バリアントデータベースの重要性については、もちろん私の好みではありません。</tgt>` | 3795 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1806 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1156 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1028 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these data </src><tgt><\|wait\|></tgt>` | 828 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>sources that we can </src><tgt><\|wait\|></tgt>` | 886 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 523 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt>つまり、これらのデータソースに含めるべきフィールドについて合意できていない場合、そこから引き出すことはできませんよね？</tgt>` | 720 |
| 19 | `<src><\|wait\|></src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 297 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1104 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片呢，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1300 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 604 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분에서는</tgt>` | 1733 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>了一个是克汀，</src><tgt><\|wait\|></tgt>` | 1038 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>的部分，</src><tgt>크틴 부분,</tgt>` | 1512 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>克汀一般</src><tgt><\|wait\|></tgt>` | 1445 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>是属于</src><tgt>크틴은 보통</tgt>` | 1182 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1709 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>我们在修饰的地方。</src><tgt>우리가 꾸미는 부분에 속합니다.</tgt>` | 2214 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1711 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分。</src><tgt>그러니까 이건 신체 부분입니다.</tgt>` | 1662 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它会反映的是</src><tgt><\|wait\|></tgt>` | 918 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1119 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 706 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 924 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做一下来修饰，</src><tgt>꾸미는 데 시간이 좀 필요합니다.</tgt>` | 744 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可以看到</src><tgt><\|wait\|></tgt>` | 459 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是双耳人的嘛。</src><tgt>여기서 양쪽 귀를 보여요.</tgt>` | 562 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 271 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt>네, 그러니까</tgt>` | 335 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 930 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>彼らは全く珍しく、</tgt>` | 1113 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 782 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1537 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely </src><tgt><\|wait\|></tgt>` | 937 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>世界を完全に変革する。そして、</tgt>` | 1965 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>is something </src><tgt><\|wait\|></tgt>` | 980 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>of a contradiction. </src><tgt>その人格は矛盾に満ちている。</tgt>` | 1885 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2165 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're extroverted, </src><tgt>外向的ではあるが、</tgt>` | 1617 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>they also </src><tgt><\|wait\|></tgt>` | 1677 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate </src><tgt><\|wait\|></tgt>` | 1048 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations. </src><tgt>無意味な会話も嫌う。</tgt>` | 1307 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 985 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>it gets straight to the </src><tgt><\|wait\|></tgt>` | 734 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt>そしてすぐに本題に入る。</tgt>` | 478 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 376 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate, </src><tgt>彼らは議論の相手を演じるのも好きだ。</tgt>` | 511 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and they're </src><tgt><\|wait\|></tgt>` | 312 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy about </src><tgt>そして、</tgt>` | 270 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>a debate. </src><tgt><\|wait\|></tgt>` | 326 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>議論を避けることは決してない。</tgt>` | 371 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E. N. P. </src><tgt><\|wait\|></tgt>` | 347 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stands for. </src><tgt>E. N. P. は</tgt>` | 398 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 1291 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>정무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 886 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 706 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1519 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1180 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1641 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1693 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 984 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1651 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1840 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1737 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 700 |
| 13 | `<src><\|wait\|></src><tgt>Lee Jun -seok</tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1791 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 1324 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기 를 품은 </src><tgt><\|wait\|></tgt>` | 892 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 953 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 657 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 482 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt>Previously, Lee Jun- seok was acting as a candidate for the party, claiming to be against the party's political direction, and even showing off his candidacy. But now, as Yoon Suk- yeol has removed Kim Jong- un, Lee Jun- seok is plotting to attack Yoon Suk- yeol and has shown his aggressive intent.</tgt>` | 1300 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 315 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 청상 납권 </src><tgt><\|wait\|></tgt>` | 369 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 337 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 344 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 얼마나 </src><tgt><\|wait\|></tgt>` | 278 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 입니까? </src><tgt>How much of a boon is this for the Democratic Party?</tgt>` | 389 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今作って</src><tgt>Well, I'm making this now after dinner</tgt>` | 1526 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>みたいです。</src><tgt><\|wait\|></tgt>` | 593 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt>so</tgt>` | 1044 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのねゴルフスローンホテル</src><tgt><\|wait\|></tgt>` | 1498 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>も朝食が</src><tgt><\|wait\|></tgt>` | 1754 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1490 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1126 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1695 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1747 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1752 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まっていきたいな</src><tgt><\|wait\|></tgt>` | 735 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>っていう方はですね</src><tgt><\|wait\|></tgt>` | 1869 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討させて</src><tgt><\|wait\|></tgt>` | 1152 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>thinking about staying here in the future,</tgt>` | `<src>見てまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 1010 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 883 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt>I'm making this now after dinner. So, since the Golfstone Hotel here is a place where you can have breakfast, I'd like to consider staying there in the future. I think it's a good idea.</tgt>` | 1297 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 459 |
| 19 | `<src>駅ももう</src><tgt>From this hotel,</tgt>` | `<src>부산駅も</src><tgt>From here, you can also get to Busan Station</tgt>` | 388 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 335 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかるか</src><tgt><\|wait\|></tgt>` | 291 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんないか</src><tgt><\|wait\|></tgt>` | 302 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね立地の</src><tgt><\|wait\|></tgt>` | 260 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>いいねまあホテル</src><tgt><\|wait\|></tgt>` | 302 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt>and the location is great— you can walk to Busan Station in about a minute or so. Since it's a hotel,</tgt>` | 589 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 301 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討させて</src><tgt>I'd like to consider it if you're interested.</tgt>` | 257 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>くださいそれでは</src><tgt><\|wait\|></tgt>` | 191 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt>Well, this time,</tgt>` | 202 |
