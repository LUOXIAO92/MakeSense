# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9833
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.2384
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.9048
  - TGT_RELEASE_TOTAL: 63
  - TGT_WAIT_ACCURACY: 0.9963
  - TGT_WAIT_TOTAL: 806
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1311.9590
  - PROCESS_TIME_MS_P50: 1261.9270
  - PROCESS_TIME_MS_P95: 2327.7390
  - PROCESS_TIME_MS_MAX: 3519.5190

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1217 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>在身上这一点？</src><tgt><\|wait\|></tgt>` | 789 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个要因</src><tgt><\|wait\|></tgt>` | 495 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>很大。然后</src><tgt><\|wait\|></tgt>` | 1144 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那</src><tgt><\|wait\|></tgt>` | 1272 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在面对</src><tgt><\|wait\|></tgt>` | 1283 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和他这个人，</src><tgt><\|wait\|></tgt>` | 888 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>这个</src><tgt><\|wait\|></tgt>` | 1573 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这样的</src><tgt><\|wait\|></tgt>` | 1647 |
| 11 | `<src>仁儿。</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels— this kind of walnut kernels.</tgt>` | `<src>和他。</src><tgt>Why is this so important? That factor is huge. And then, when I face him, this kind of him.</tgt>` | 1022 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要做</src><tgt><\|wait\|></tgt>` | 1210 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>的是，</src><tgt><\|wait\|></tgt>` | 973 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 994 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>身身的那爱交</src><tgt><\|wait\|></tgt>` | 1240 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt><\|wait\|></tgt>` | 703 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>十飞，</src><tgt><\|wait\|></tgt>` | 1408 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>可以做</src><tgt><\|wait\|></tgt>` | 1618 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心里影响，</src><tgt><\|wait\|></tgt>` | 1556 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>你耐心</src><tgt><\|wait\|></tgt>` | 685 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>等他</src><tgt><\|wait\|></tgt>` | 1584 |
| 11 | `<src>慢慢长大。</src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for them to grow slowly.</tgt>` | `<src>慢慢长大。</src><tgt>Parents need to use the love in their hearts to guide their children. Be patient and let them grow up slowly.</tgt>` | 2831 |

---

### Test Example 3 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 951 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Apple, </src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축복 받히고 </src><tgt><\|wait\|></tgt>` | 1023 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1114 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 722 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>범을 죽인 </src><tgt><\|wait\|></tgt>` | 1497 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1705 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1710 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1781 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt><\|wait\|></tgt>` | 1234 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents. They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt>I am Apple, blessed and the same generation as the people who killed Herona Park Han- sang.</tgt>` | 2436 |

---

### Test Example 4 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 1016 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용신이 </src><tgt><\|wait\|></tgt>` | 917 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>칼 </src><tgt><\|wait\|></tgt>` | 628 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>용신이 </src><tgt><\|wait\|></tgt>` | 887 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설프 용신이 가 </src><tgt><\|wait\|></tgt>` | 1486 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>섞여 </src><tgt><\|wait\|></tgt>` | 1372 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1732 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1554 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 734 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행운 으로 </src><tgt><\|wait\|></tgt>` | 1621 |
| 11 | `<src>진짜. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover, for real.</tgt>` | `<src>조금 쥐기 맞는 것 </src><tgt>Ah, I have a Wood element and a Metal element, and they're mixed up. Wow, this really feels like a lucky sign.</tgt>` | 3342 |

---

### Test Example 5 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1230 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>があの</src><tgt><\|wait\|></tgt>` | 976 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt><\|wait\|></tgt>` | 1205 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ようなものも</src><tgt><\|wait\|></tgt>` | 1194 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1028 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 938 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1620 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1518 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、</src><tgt><\|wait\|></tgt>` | 698 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>また</src><tgt><\|wait\|></tgt>` | 1534 |
| 11 | `<src>ランチの案内がありますので</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements, and we have some info about lunch,</tgt>` | `<src>私のアナウンスがあります</src><tgt>We have T- shirts and other items available, so please feel free to join us. That concludes my announcement.</tgt>` | 2871 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ので少々お待ちください。</src><tgt><\|wait\|></tgt>` | 795 |

---

### Test Example 6 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气鼠，</src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的。</src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 1238 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个</src><tgt><\|wait\|></tgt>` | 1286 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导，</src><tgt><\|wait\|></tgt>` | 1287 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如</src><tgt><\|wait\|></tgt>` | 705 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>初于中年，</src><tgt><\|wait\|></tgt>` | 1641 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1568 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1735 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 707 |
| 11 | `<src>一个师父。</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは師匠になる必要があるのです。</tgt>` | `<src>师傅，</src><tgt>「気鼠」は簡単です。しかし、師匠の指導が一つしかないのです。初めから中年まで、だからこそ反省が必要です。師匠になるためには、</tgt>` | 3456 |

---

### Test Example 7 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 917 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 926 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into your body </src><tgt><\|wait\|></tgt>` | 1306 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>where does </src><tgt><\|wait\|></tgt>` | 1290 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1272 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1230 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 1127 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tension in your chest? </src><tgt><\|wait\|></tgt>` | 1643 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it </src><tgt><\|wait\|></tgt>` | 1683 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a lump in your </src><tgt><\|wait\|></tgt>` | 1332 |
| 11 | `<src>language are you using? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，你在用什么语言？</tgt>` | `<src>using? </src><tgt>你的身体在做什么？进入你的身体，紧张感从哪里开始？是什么？是头痛吗？是胸部有紧张吗？还是你使用的东西里有东西？</tgt>` | 2874 |

---

### Test Example 8 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后</src><tgt><\|wait\|></tgt>` | 1227 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的冶炼轻</src><tgt><\|wait\|></tgt>` | 1275 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | 1473 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后就</src><tgt><\|wait\|></tgt>` | 1403 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1441 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1335 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 924 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>运行状态。</src><tgt><\|wait\|></tgt>` | 1689 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1341 |
| 11 | `<src>抑郁状态。</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。これが、いわゆる抑うつ状態です。</tgt>` | `<src>低于状态。</src><tgt>精錬を終えると、内部の冶錬軽エネルギーも衰弱し、相対的に低エネルギーな稼働状態に留まります。これがいわゆる「低エネルギー状態」です。</tgt>` | 2926 |

---

### Test Example 9 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 927 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 942 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>村中まだ</src><tgt><\|wait\|></tgt>` | 1312 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1403 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1430 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう密告、</src><tgt><\|wait\|></tgt>` | 1521 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1254 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数していった</src><tgt><\|wait\|></tgt>` | 935 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>がけると</src><tgt><\|wait\|></tgt>` | 1749 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>10年経っても</src><tgt><\|wait\|></tgt>` | 1565 |
| 11 | `<src>大した。</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，十年后也不会有什么大……</tgt>` | `<src>対数だ。</src><tgt>从一开始，特别是村里，他还是个一年级。那个时候，他把密告和选举都用对数表示了，就算过了十年，还是对数。</tgt>` | 2643 |

---

### Test Example 10 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1336 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>식성들은 </src><tgt><\|wait\|></tgt>` | 957 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1196 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1449 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1441 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1393 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>식성들이 </src><tgt><\|wait\|></tgt>` | 871 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>있었습니다. </src><tgt><\|wait\|></tgt>` | 1486 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1776 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1354 |
| 11 | `<src>교사 들은. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random. The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교사 들은 </src><tgt>The students in the auspicious seats actually didn't have high intelligence. The students who were randomly selected were the ones in question. The teachers who didn't know the truth</tgt>` | 2850 |

---

### Test Example 11 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1232 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 985 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1239 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned and then repeat. </src><tgt><\|wait\|></tgt>` | 1409 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find out what you're good at. </src><tgt><\|wait\|></tgt>` | 1531 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>And do more of it. </src><tgt><\|wait\|></tgt>` | 1479 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And will you not </src><tgt><\|wait\|></tgt>` | 1407 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>get to people </src><tgt><\|wait\|></tgt>` | 928 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1873 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it? </src><tgt><\|wait\|></tgt>` | 2270 |
| 11 | `<src>And until next time. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。下次再见。</tgt>` | `<src>And in telling next time, </src><tgt>最后，重复。学习，然后重复。找出你擅长什么。然后多做一些。你会不会得到身边人的帮助？下次告诉别人，</tgt>` | 1835 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1123 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1014 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めたもので</src><tgt><\|wait\|></tgt>` | 1221 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>ご</src><tgt><\|wait\|></tgt>` | 1099 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>法</src><tgt><\|wait\|></tgt>` | 626 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>五言</src><tgt><\|wait\|></tgt>` | 1386 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1664 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>五音の</src><tgt><\|wait\|></tgt>` | 1731 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 749 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ルナールなどという人の絵</src><tgt><\|wait\|></tgt>` | 1504 |
| 11 | `<src>は、田舎の</src><tgt>大致是从这一带开始的，像梵高、高更、塞尚、雷诺阿他们的画，连乡下的</tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 2268 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt>大概是从那开始画的，比如五言五音的“ルナール”之类的。即使是乡下初中生，</tgt>` | 1887 |

---

### Test Example 13 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 779 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 994 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活的一个</src><tgt><\|wait\|></tgt>` | 914 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>轨道哈，</src><tgt><\|wait\|></tgt>` | 593 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够好好的</src><tgt><\|wait\|></tgt>` | 1320 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>扎根的时候，</src><tgt><\|wait\|></tgt>` | 1528 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日谈</src><tgt><\|wait\|></tgt>` | 1718 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>日愿解，</src><tgt><\|wait\|></tgt>` | 1745 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以说，</src><tgt><\|wait\|></tgt>` | 1736 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>我当时背到这四目</src><tgt><\|wait\|></tgt>` | 785 |
| 11 | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的小小</src><tgt>제 삶의 궤도로 돌아가서 뿌리내릴 수 있도록 해 주세요. 그래서 제가 그날 ' 일담일원해 ' 를 외웠는데,</tgt>` | 3316 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>愿望哈。</src><tgt><\|wait\|></tgt>` | 571 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 1005 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 920 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1246 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 1544 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1516 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking at </src><tgt><\|wait\|></tgt>` | 1677 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1720 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 749 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1370 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people that </src><tgt><\|wait\|></tgt>` | 2313 |
| 11 | `<src>people that we can learn from. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>極めて幸せな人たちを対象にした研究をしてみたんです。これは研究の入り口です。最も幸せな人々の10%を見て、そこから学んでいこうと思います。</tgt>` | 2220 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 981 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>산줄에 죽여달라 </src><tgt><\|wait\|></tgt>` | 1113 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>제가 죽고 내가 </src><tgt><\|wait\|></tgt>` | 1273 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔어도 </src><tgt><\|wait\|></tgt>` | 1495 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜이 </src><tgt><\|wait\|></tgt>` | 1482 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여달라 해야지 </src><tgt><\|wait\|></tgt>` | 1786 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>안 되냐 내가 </src><tgt><\|wait\|></tgt>` | 1751 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt><\|wait\|></tgt>` | 1727 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>안 듣고 있는 줄 알았느냐 </src><tgt><\|wait\|></tgt>` | 1582 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아 </src><tgt><\|wait\|></tgt>` | 1317 |
| 11 | `<src>내가 가. </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh? I'm going.</tgt>` | `<src>내가 </src><tgt>You want me to be killed by someone else? Even if I came here to kill you, you should have asked for it. Did you think I wouldn't hear that? Ah, I'm</tgt>` | 2235 |

---

### Test Example 16 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1104 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Frenkel, </src><tgt><\|wait\|></tgt>` | 975 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>and I am currently studying </src><tgt><\|wait\|></tgt>` | 1371 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a PhD </src><tgt><\|wait\|></tgt>` | 1305 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in finance </src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a B.S. in psychology. </src><tgt><\|wait\|></tgt>` | 1446 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 1097 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>here today </src><tgt><\|wait\|></tgt>` | 1139 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1734 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go </src><tgt><\|wait\|></tgt>` | 1456 |
| 11 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>into corporate </src><tgt>제 이름은 프렌켈입니다. 현재 금융 분야에서 박사 과정을 밟고 있고 심리학 학사 학위도 가지고 있습니다. 오늘 여기서, 그리고 앞으로 기업</tgt>` | 2741 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1043 |

---

### Test Example 17 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 1067 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 947 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1264 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1481 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1403 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们下了这个状况，</src><tgt><\|wait\|></tgt>` | 1622 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1310 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1148 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>你無理承担，</src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言</src><tgt><\|wait\|></tgt>` | 2261 |
| 11 | `<src>事业运就属凶。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall, your career prospects are quite poor.</tgt>` | `<src>是应该做的事情。</src><tgt>When you face a situation like this, you should immediately report it to your supervisor or inform the other party. Don't try to handle everything yourself or take on the whole burden. Overall, that's what you should do.</tgt>` | 2746 |

---

### Test Example 18 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1286 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 979 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1246 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1342 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1278 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1176 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1183 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1547 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1797 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 1313 |
| 11 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们要使用这些值。也就是</tgt>` | `<src><\|wait\|></src><tgt>好的。接下来，根据这些例子，指令告诉我们，实际上要使用这些值。</tgt>` | 2225 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>So this game.board </src><tgt><\|wait\|></tgt>` | 756 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>array. </src><tgt><\|wait\|></tgt>` | 1215 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果在女高中</src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>生与长相</src><tgt><\|wait\|></tgt>` | 1001 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>不怪的人之间，</src><tgt><\|wait\|></tgt>` | 1374 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有着某种</src><tgt><\|wait\|></tgt>` | 1240 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>典型性，</src><tgt><\|wait\|></tgt>` | 1480 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1535 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1345 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天体实验</src><tgt><\|wait\|></tgt>` | 1041 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1650 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1793 |
| 11 | `<src>杨子思绪</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night? Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt>If it's between a girl in high school and someone who doesn't mind her looks, there's a certain typicality to it. Could it really have started with the ' Celestial Experiment '?</tgt>` | 2381 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>历年篇？</src><tgt><\|wait\|></tgt>` | 1352 |

---

### Test Example 20 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>なんとちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 922 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 737 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 778 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>あるこうだったかな</src><tgt><\|wait\|></tgt>` | 1396 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>と思いますね海老したい方って</src><tgt><\|wait\|></tgt>` | 1595 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行きに行き出したが</src><tgt><\|wait\|></tgt>` | 1861 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>し</src><tgt><\|wait\|></tgt>` | 1646 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ジュレゼミトトモンチ</src><tgt><\|wait\|></tgt>` | 1994 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>に言おうとしよう</src><tgt><\|wait\|></tgt>` | 2320 |
| 11 | `<src>傾向が強いので、</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且倾向于自己全部投资，</tgt>` | `<src>けどすごいので</src><tgt>大将好像说要稍微拉开一点距离，所以想去海老的话就立刻出发了。但因为要说ジュレゼミトトモンチ，所以</tgt>` | 2013 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1102 |

---

### Test Example 21 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1175 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 792 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 495 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと信号が</src><tgt><\|wait\|></tgt>` | 1246 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>消えなくなってしまう</src><tgt><\|wait\|></tgt>` | 1341 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1418 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1599 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1283 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 940 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついているっていうこと</src><tgt><\|wait\|></tgt>` | 1791 |
| 11 | `<src>ね。</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가 꺼지지 않게 되니까, 기어 끝에 역나사산 너트가 붙어 있는 거죠.</tgt>` | 3520 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい</src><tgt><\|wait\|></tgt>` | 685 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文型完了。</src><tgt><\|wait\|></tgt>` | 1258 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this, </src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで、</src><tgt><\|wait\|></tgt>` | 964 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 1202 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>to do a setup </src><tgt><\|wait\|></tgt>` | 1388 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>gigabit. はい、</src><tgt><\|wait\|></tgt>` | 1379 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 777 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1418 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>ハイシーの仕組み</src><tgt><\|wait\|></tgt>` | 1670 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1829 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>5G、</src><tgt><\|wait\|></tgt>` | 1679 |
| 11 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠. 파생 형용사의 구조는</tgt>` | `<src>6G、</src><tgt>그래서 이어서 기가비트 설정을 해보려고 합니다. 네, 하이시의 구조는 5G, 6G,</tgt>` | 2221 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>7G、</src><tgt><\|wait\|></tgt>` | 581 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>8Gです。</src><tgt><\|wait\|></tgt>` | 1185 |

---

### Test Example 23 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 너무 </src><tgt><\|wait\|></tgt>` | 1174 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인 저희 가 </src><tgt><\|wait\|></tgt>` | 950 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>해열 할 수 있지만 </src><tgt><\|wait\|></tgt>` | 1393 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1457 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 고생 </src><tgt><\|wait\|></tgt>` | 1487 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>하는데 꿈일 프로 </src><tgt><\|wait\|></tgt>` | 1706 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>보고 있고 </src><tgt><\|wait\|></tgt>` | 1660 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1751 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보이 려고 </src><tgt><\|wait\|></tgt>` | 861 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>보여 주지 못하 는데 </src><tgt><\|wait\|></tgt>` | 2383 |
| 11 | `<src>보살 이라는데. </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に菩薩だと言ってるんだから。</tgt>` | `<src>보살 이러는 게 </src><tgt>これ、私たちには熱を上げられるかもしれませんが、本当に菩薩ですか？いや、自分の苦労を理解して、夢を見ているだけじゃないですか？私だけ菩薩に見せようとしないのに、菩薩って言うのは、</tgt>` | 2696 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 920 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A、Aアンデスに</src><tgt><\|wait\|></tgt>` | 1108 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いるな場面で</src><tgt><\|wait\|></tgt>` | 1379 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>A制服かどうか</src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>メディアでいるときに</src><tgt><\|wait\|></tgt>` | 1427 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあAの</src><tgt><\|wait\|></tgt>` | 1594 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>乱攻調べことであの</src><tgt><\|wait\|></tgt>` | 1324 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>そのA制服かどうか</src><tgt><\|wait\|></tgt>` | 1145 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>の調査する制服で</src><tgt><\|wait\|></tgt>` | 1670 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうこと保証する</src><tgt><\|wait\|></tgt>` | 2341 |
| 11 | `<src>といったような</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>といってあの使い方を定めました。</src><tgt>We've set the rules for how to use the A uniform when A is in the A Andes. This is to ensure that the uniform used for the A uniform investigation is indeed the A uniform.</tgt>` | 2607 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 710 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到二classList</src><tgt><\|wait\|></tgt>` | 1031 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 1203 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>还服务在一级</src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1282 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>一线平安的大牛们。</src><tgt><\|wait\|></tgt>` | 1054 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1195 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做维信</src><tgt><\|wait\|></tgt>` | 1753 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好事几点，</src><tgt><\|wait\|></tgt>` | 1845 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1379 |
| 11 | `<src>给微信公众号评分</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>给维信好平分</src><tgt>2つ目は、二つのクラスに移行します。そして、第一線の平安大牛たちをサポートします。例えば、維信のコミュニケーションを良い形で分けるとき、</tgt>` | 2775 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>的星棒反而</src><tgt><\|wait\|></tgt>` | 1296 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>活了。</src><tgt><\|wait\|></tgt>` | 1018 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 996 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 974 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1403 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1385 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1513 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1736 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1675 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1888 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 1527 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 1528 |
| 11 | `<src>or gets used to make </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다. 또는</tgt>` | `<src>to make </src><tgt>늘어난 고무줄처럼 화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 형태의 에너지로 변환됩니다. 또는</tgt>` | 2320 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1190 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1147 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 928 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1243 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1357 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1325 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1169 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1058 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like oh, </src><tgt><\|wait\|></tgt>` | 1717 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1806 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>started with </src><tgt><\|wait\|></tgt>` | 1372 |
| 11 | `<src><\|wait\|></src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>a double P, </src><tgt>あるいは、何かを書いて、文章を書こうとしたとき、言葉の綴りすら知らないことに気づく。まるで「あ、この単語はダブルPで始まるんだ」</tgt>` | 2747 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double L. I don't know </src><tgt><\|wait\|></tgt>` | 1433 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>it. </src><tgt><\|wait\|></tgt>` | 1177 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1055 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>已经正常</src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>喉咙扁桃炎，</src><tgt><\|wait\|></tgt>` | 1257 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1243 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1238 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>提前大概有</src><tgt><\|wait\|></tgt>` | 681 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>十二星</src><tgt><\|wait\|></tgt>` | 1625 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>医生来诊断，</src><tgt><\|wait\|></tgt>` | 1846 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下药腿</src><tgt><\|wait\|></tgt>` | 1850 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下剃腿，</src><tgt><\|wait\|></tgt>` | 1492 |
| 11 | `<src>都没有问题。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>都没有问题。</src><tgt>I already had a normal tonsillitis at the time, so I insisted on not having surgery. I got a diagnosis from a doctor about twelve days in advance. The medication I took, the leg- shaving, everything was fine.</tgt>` | 2818 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>当然都很</src><tgt><\|wait\|></tgt>` | 1170 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一手打的离开。</src><tgt><\|wait\|></tgt>` | 1262 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1206 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这</src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1032 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1202 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 710 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1390 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>说明你的一些</src><tgt><\|wait\|></tgt>` | 1720 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>婚礼啊</src><tgt><\|wait\|></tgt>` | 1707 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟婚礼</src><tgt><\|wait\|></tgt>` | 1597 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你细之间就</src><tgt><\|wait\|></tgt>` | 638 |
| 11 | `<src><\|wait\|></src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src><\|wait\|></src><tgt>皆さんにお伝えしたいのは、この「ローマ」は一日にしてできたものではないということです。ですから、今あなたが結婚式や</tgt>` | 3326 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 612 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因际会建议</src><tgt><\|wait\|></tgt>` | 1374 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>属鸡的朋友呢，</src><tgt><\|wait\|></tgt>` | 1341 |

---

### Test Example 30 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1254 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 1065 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>Amendment </src><tgt><\|wait\|></tgt>` | 1210 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1415 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1503 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1627 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 1299 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt><\|wait\|></tgt>` | 1049 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>United States. </src><tgt><\|wait\|></tgt>` | 1633 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 2065 |
| 11 | `<src>The meanings </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>of the amendment </src><tgt>19차 수정안의 의미와 그 역사를 탐구하며, 이것이 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 될 수 있도록 하겠습니다. 이 수정안의 의미는</tgt>` | 2181 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of course I </src><tgt><\|wait\|></tgt>` | 1218 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>married. </src><tgt><\|wait\|></tgt>` | 1461 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>砸到了一个</src><tgt><\|wait\|></tgt>` | 933 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>钱包，</src><tgt><\|wait\|></tgt>` | 940 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1206 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>拿到了钱包之后，</src><tgt><\|wait\|></tgt>` | 1404 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1477 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就要先</src><tgt><\|wait\|></tgt>` | 1118 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt><\|wait\|></tgt>` | 957 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着哎，那我</src><tgt><\|wait\|></tgt>` | 1694 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>再去操作</src><tgt><\|wait\|></tgt>` | 1707 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦，</src><tgt><\|wait\|></tgt>` | 1360 |
| 11 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src><\|wait\|></src><tgt>財布にぶつけてしまったら、まずしっかり守るようにしてください。そうして、また操作しようとか考えないでください。</tgt>` | 2419 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 809 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1185 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1392 |

---

### Test Example 32 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 1049 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이루 어떨 때는 </src><tgt><\|wait\|></tgt>` | 1001 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 100일 중에 </src><tgt><\|wait\|></tgt>` | 1421 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>거진 60산 </src><tgt><\|wait\|></tgt>` | 1383 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>중간 에 </src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>나올 정도 고 굉장히 </src><tgt><\|wait\|></tgt>` | 1766 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1681 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1788 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이기적이야 </src><tgt><\|wait\|></tgt>` | 1276 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>정도로 이게 </src><tgt><\|wait\|></tgt>` | 1665 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>그런 거죠 </src><tgt>Sometimes, vanadium is so abundant that it's about 60% of the total 100%— that's just a mineral, really.</tgt>` | 1635 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>이제 그 후에다가 </src><tgt><\|wait\|></tgt>` | 1251 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아멘. </src><tgt><\|wait\|></tgt>` | 1385 |

---

### Test Example 33 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1194 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 985 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1214 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1179 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>like ten of them </src><tgt><\|wait\|></tgt>` | 1132 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 820 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1737 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to </src><tgt><\|wait\|></tgt>` | 1651 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 1762 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one </src><tgt><\|wait\|></tgt>` | 598 |
| 11 | `<src>one minute videos </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>minute videos </src><tgt>これから始める人には、本当に重要なことが10個くらいあります。1分程度の動画を</tgt>` | 2871 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video. </src><tgt><\|wait\|></tgt>` | 874 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage </src><tgt><\|wait\|></tgt>` | 1192 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>each one </src><tgt><\|wait\|></tgt>` | 1104 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 972 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 974 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1216 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>带吊耳的人，但是</src><tgt><\|wait\|></tgt>` | 1511 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1560 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这通场</src><tgt><\|wait\|></tgt>` | 1688 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>有没有这样的一个状况</src><tgt><\|wait\|></tgt>` | 1711 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>需要去特别</src><tgt><\|wait\|></tgt>` | 1782 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>注意的是</src><tgt><\|wait\|></tgt>` | 1093 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1749 |
| 11 | `<src>钓到鱼，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt>이 부분은 귀걸이를 한 사람을 보여주는데, 이건 역방향이에요. 이런 상황에서 특별히 주의할 점은 그 사람이</tgt>` | 1648 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>于他吊不到</src><tgt><\|wait\|></tgt>` | 1276 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>于你的意识</src><tgt><\|wait\|></tgt>` | 1432 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt><\|wait\|></tgt>` | 458 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1127 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There </src><tgt><\|wait\|></tgt>` | 894 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1223 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>was such interests before. </src><tgt><\|wait\|></tgt>` | 1354 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1273 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>Net future TC </src><tgt><\|wait\|></tgt>` | 648 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>is so </src><tgt><\|wait\|></tgt>` | 1608 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1757 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>this just one another place </src><tgt><\|wait\|></tgt>` | 1904 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 2126 |
| 11 | `<src>But </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt>没什么新鲜事。以前也有这样的兴趣。NetFutureTC就是另一个地方，用来看看。但</tgt>` | 1350 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers, engineers, </src><tgt><\|wait\|></tgt>` | 1255 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>developers should be </src><tgt><\|wait\|></tgt>` | 1387 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 616 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 970 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>而HTML</src><tgt><\|wait\|></tgt>` | 949 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 도 </src><tgt><\|wait\|></tgt>` | 1365 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1483 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1219 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 931 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1622 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1832 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1931 |
| 11 | `<src>코드 를 작성 해야 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1049 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt>HTML，也就是计算机语言，也是计算机和人都能理解的。所以我们现在需要根据它的语法来编写代码，</tgt>` | 1791 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 876 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1474 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1092 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10</src><tgt><\|wait\|></tgt>` | 1032 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt><\|wait\|></tgt>` | 943 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>ですとね、</src><tgt><\|wait\|></tgt>` | 972 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく10秒で</src><tgt><\|wait\|></tgt>` | 695 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1167 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>1秒に</src><tgt><\|wait\|></tgt>` | 1491 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1789 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>スピンとかね、</src><tgt><\|wait\|></tgt>` | 1761 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 595 |
| 11 | `<src>おそらく</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。然后</tgt>` | `<src>おそらく</src><tgt>10到12手的话，大概10秒钟，嗯，1秒左右的旋转，然后</tgt>` | 3134 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11手</src><tgt><\|wait\|></tgt>` | 703 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1144 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 665 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | 1319 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 1013 |

---

### Test Example 38 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1111 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1084 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 1262 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较稳定</src><tgt><\|wait\|></tgt>` | 1247 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>的部分，因为</src><tgt><\|wait\|></tgt>` | 1475 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面</src><tgt><\|wait\|></tgt>` | 1647 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长所带来的</src><tgt><\|wait\|></tgt>` | 1466 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>流动收益的</src><tgt><\|wait\|></tgt>` | 896 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升，</src><tgt><\|wait\|></tgt>` | 1626 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果设置利在方面</src><tgt><\|wait\|></tgt>` | 2331 |
| 11 | `<src>这个月</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>这个月</src><tgt>金運については、今月は悪くないと言えるでしょう。ただ、安定しているというよりは、</tgt>` | 1648 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错的，只是</src><tgt><\|wait\|></tgt>` | 1142 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对整体来说</src><tgt><\|wait\|></tgt>` | 838 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了</src><tgt><\|wait\|></tgt>` | 1206 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一点。</src><tgt><\|wait\|></tgt>` | 1028 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1116 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らしてやる。</src><tgt><\|wait\|></tgt>` | 946 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 829 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt><\|wait\|></tgt>` | 619 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き絞みている。</src><tgt><\|wait\|></tgt>` | 1387 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1490 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1439 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えている</src><tgt><\|wait\|></tgt>` | 1422 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈火勢気を</src><tgt><\|wait\|></tgt>` | 1048 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1657 |
| 11 | `<src>長年</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>長年</src><tgt>그럼 젖게 해줄게. 지금 끌어당기고 있어. 한계는 이미 한참을 넘어선 불멸의 화염 기세가</tgt>` | 3117 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>の大国を</src><tgt><\|wait\|></tgt>` | 937 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 1151 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 860 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい海賊船を見た</src><tgt><\|wait\|></tgt>` | 1168 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 1062 |

---

### Test Example 40 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 930 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개 가 중화 버섯 </src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>열매 미만 으로 </src><tgt><\|wait\|></tgt>` | 1245 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>4조 4000 기업 들이 </src><tgt><\|wait\|></tgt>` | 1560 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>몰락 했습니다. </src><tgt><\|wait\|></tgt>` | 1347 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1755 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1792 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 법인 </src><tgt><\|wait\|></tgt>` | 1823 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>의 고객 대가 되는데 </src><tgt><\|wait\|></tgt>` | 1570 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>일본 에 상기 없던 </src><tgt><\|wait\|></tgt>` | 1504 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は成長も廃業も</tgt>` | `<src>성장 도 </src><tgt>そのうち150個未満の中国の木綿の果実を前に、4兆4000社の企業が倒産しました。一般的に、中小企業は成長するか、あるいは海外法人の顧客になるのですが、日本にはない成長も</tgt>` | 2728 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>표해 도 하지 않을 현상 들을 </src><tgt><\|wait\|></tgt>` | 1460 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1247 |

---

### Test Example 41 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1195 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어제 보면 </src><tgt><\|wait\|></tgt>` | 1013 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 </src><tgt><\|wait\|></tgt>` | 999 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>20대를 함께 한 </src><tgt><\|wait\|></tgt>` | 1240 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 795 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 1394 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1798 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1661 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1717 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생 한 거다는 </src><tgt><\|wait\|></tgt>` | 1510 |
| 11 | `<src>조금 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>조금 자기 스스로 </src><tgt>昨天，他就是那个和我们一起度过二十岁的弟弟，也是像家人一样的弟弟。所以，</tgt>` | 2247 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>어. </src><tgt><\|wait\|></tgt>` | 645 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>정말 </src><tgt><\|wait\|></tgt>` | 1168 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 1125 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 817 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>생각 했습니다. </src><tgt><\|wait\|></tgt>` | 1349 |

---

### Test Example 42 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 1003 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 </src><tgt><\|wait\|></tgt>` | 989 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>너희가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1392 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1366 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1489 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1715 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 978 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1328 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 2278 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。ですから、あなたがたに</tgt>` | `<src>너희에게 </src><tgt>あなたたちも知っているでしょう。異邦人としているとき、言葉を話せない偶像にそのまま引きずられて行ったのです。ですから、私があなたたちに</tgt>` | 1944 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1261 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1458 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 1078 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 752 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1304 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새 머라 </src><tgt><\|wait\|></tgt>` | 1041 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1222 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 </src><tgt><\|wait\|></tgt>` | 1418 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋던 자태 돋던 </src><tgt><\|wait\|></tgt>` | 1522 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>그 느낌 이 너무 </src><tgt><\|wait\|></tgt>` | 1603 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1321 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1136 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 너무 </src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>불릴 거고 </src><tgt><\|wait\|></tgt>` | 2267 |
| 11 | `<src>신이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら</tgt>` | `<src>귀신 이 너무 </src><tgt>目を閉じて、新しい自分になろう。昔の自分、あの姿、あの感じを揺らして、一緒に遊ぼうってこと。お化けが怖くてたまらないし、お化けが怖くてたまらない、</tgt>` | 2794 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>지켜 주라고 </src><tgt><\|wait\|></tgt>` | 940 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>이제 늙어 주니까 </src><tgt><\|wait\|></tgt>` | 1137 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에 </src><tgt><\|wait\|></tgt>` | 1182 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 553 |

---

### Test Example 44 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1102 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 838 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1046 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 669 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1311 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨트롤 텐트예요. </src><tgt><\|wait\|></tgt>` | 1635 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이 컨트롤 텐트가 </src><tgt><\|wait\|></tgt>` | 1858 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>여기 고 </src><tgt><\|wait\|></tgt>` | 1601 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1844 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 2162 |
| 11 | `<src>뿌렸 을 때 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、</tgt>` | `<src>들여 쓸 때 </src><tgt>ですから、もちろんこのようなケースもあります。AさんとBさんがお互いにコントロールテントです。このコントロールテントがここにあるとします。Aさんが悪意のあるコードを仕込むと、</tgt>` | 2036 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1291 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스 사이트 크래킹을 </src><tgt><\|wait\|></tgt>` | 1543 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>해서 </src><tgt><\|wait\|></tgt>` | 446 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>API까지 </src><tgt><\|wait\|></tgt>` | 1210 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>가능 이 될까? </src><tgt><\|wait\|></tgt>` | 518 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1159 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 1060 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you </src><tgt><\|wait\|></tgt>` | 1242 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go in your </src><tgt><\|wait\|></tgt>` | 1380 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1506 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1833 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1821 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1747 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1497 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, did you graduate? </src><tgt><\|wait\|></tgt>` | 1693 |
| 11 | `<src>That's another level of </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of </src><tgt>학력 수준. 실제로 학업을 얼마나 마쳤나요? 고등학교를 졸업했나요? 그건 한 단계의 학력입니다. 대학에 갔나요? 그래서 졸업했나요? 그건 또 다른 단계의 학력입니다.</tgt>` | 2735 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1321 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | 1061 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | 797 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 751 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1222 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 992 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうのが出ていればいいです。</src><tgt><\|wait\|></tgt>` | 1392 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1324 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1423 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt><\|wait\|></tgt>` | 1490 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルン</src><tgt><\|wait\|></tgt>` | 1398 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとそれとは</src><tgt><\|wait\|></tgt>` | 1030 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードなんそっから生成される</src><tgt><\|wait\|></tgt>` | 1833 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつそれが</src><tgt><\|wait\|></tgt>` | 2252 |
| 11 | `<src>実行されることで</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>実行されることで信号処理</src><tgt>So, you just need to have a visual development environment. It's a Visual Python development environment. This is because you write a flow graph, and then Python code is generated from that. When that runs, it performs signal processing.</tgt>` | 2752 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 940 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことに</src><tgt><\|wait\|></tgt>` | 1055 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているからです。</src><tgt><\|wait\|></tgt>` | 1164 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 583 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 755 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1155 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉对手的</src><tgt><\|wait\|></tgt>` | 1098 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>感情或真实</src><tgt><\|wait\|></tgt>` | 1244 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>意图的，</src><tgt><\|wait\|></tgt>` | 1397 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1454 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1619 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1310 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1096 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1621 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 2327 |
| 11 | `<src>这个人</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが「ほら、</tgt>` | `<src>这个人又在</src><tgt>相手の感情や本心、意図を察したり感じ取ったりすることは、よく聞くことなんです。見てください、この人は</tgt>` | 1797 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>躲黄了，</src><tgt><\|wait\|></tgt>` | 1303 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1185 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 623 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1170 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 501 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 728 |

---

### Test Example 48 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 1060 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 1038 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1249 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1278 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1091 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 685 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>so if </src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the </src><tgt><\|wait\|></tgt>` | 1303 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation where you </src><tgt><\|wait\|></tgt>` | 1020 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1774 |
| 11 | `<src>you've added the wrong media </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>the wrong media </src><tgt>另外，你将无法在资源之间移动媒体对象。所以，如果你发现添加了错误的媒体文件，</tgt>` | 2952 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular </src><tgt><\|wait\|></tgt>` | 941 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, </src><tgt><\|wait\|></tgt>` | 1135 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 874 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those </src><tgt><\|wait\|></tgt>` | 1137 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>media files and then making sure </src><tgt><\|wait\|></tgt>` | 1100 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>you get back up </src><tgt><\|wait\|></tgt>` | 680 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 753 |

---

### Test Example 49 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 으면 </src><tgt><\|wait\|></tgt>` | 1373 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매입니다. </src><tgt><\|wait\|></tgt>` | 1000 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1211 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1374 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1506 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있고 </src><tgt><\|wait\|></tgt>` | 1615 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1583 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 832 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 장려 리요. </src><tgt><\|wait\|></tgt>` | 1720 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 2267 |
| 11 | `<src>좀 창피 하네요. </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国就更惨了。真有点丢人。</tgt>` | `<src>신기 하네요. </src><tgt>如果进去的话，会非常迷茫。因为我之前是开车来的，现在是走路的。而且，如果要去江南区，那更是不用说了，如果出国的话，那更是鼓励。挺神奇的。</tgt>` | 2699 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 805 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1195 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모여 봐요. </src><tgt><\|wait\|></tgt>` | 1063 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | 775 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 745 |

---

### Test Example 50 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1085 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>상승 하는 </src><tgt><\|wait\|></tgt>` | 943 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1386 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1399 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | 1469 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1789 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1657 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 </src><tgt><\|wait\|></tgt>` | 1949 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>들이 </src><tgt><\|wait\|></tgt>` | 1464 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1575 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>주도 하면서 </src><tgt>If the stock index is showing an upward trend, these large- cap stocks will likely see a significant rise. However, smaller stocks will lead the market first.</tgt>` | 2141 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 731 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요식초기 </src><tgt><\|wait\|></tgt>` | 1342 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1127 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 676 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 767 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 903 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 978 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1389 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 1196 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자 에 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1563 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 1624 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 칩에 </src><tgt><\|wait\|></tgt>` | 1411 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPD 파이프 를 </src><tgt><\|wait\|></tgt>` | 1044 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1676 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나출 것으로 보입니다. </src><tgt><\|wait\|></tgt>` | 2328 |
| 11 | `<src><\|wait\|></src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>엑스 박스 </src><tgt>これについて多くの人が分析しています。このロクジャの分析を見ると、ソニーがイオレットチップにFPDパイプを128ビットで出力する見込みです。</tgt>` | 2431 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>시리즈 엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 808 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1434 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>계의 S2가 </src><tgt><\|wait\|></tgt>` | 1162 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>여기도 없다. </src><tgt><\|wait\|></tgt>` | 642 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 769 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all of the </src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>short-lived </src><tgt><\|wait\|></tgt>` | 968 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>decisions, </src><tgt><\|wait\|></tgt>` | 1211 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but then </src><tgt><\|wait\|></tgt>` | 1337 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>we should </src><tgt><\|wait\|></tgt>` | 1259 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>focus on </src><tgt><\|wait\|></tgt>` | 802 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>the right love. </src><tgt><\|wait\|></tgt>` | 1522 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>We may also </src><tgt><\|wait\|></tgt>` | 1664 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>tend to enter </src><tgt><\|wait\|></tgt>` | 1833 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1597 |
| 11 | `<src>在早上的时候，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는</tgt>` | `<src>a state of </src><tgt>모든 단기적인 결정들은 그렇지만, 우리는 올바른 사랑에 집중해야 합니다. 또한</tgt>` | 2048 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>action when we love. </src><tgt><\|wait\|></tgt>` | 777 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>Dào了晚上，</src><tgt><\|wait\|></tgt>` | 1270 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 1388 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>恨。</src><tgt><\|wait\|></tgt>` | 778 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个中百。</src><tgt><\|wait\|></tgt>` | 883 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt><\|wait\|></tgt>` | 468 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>一动。</src><tgt><\|wait\|></tgt>` | 640 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1175 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 962 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1373 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1580 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1685 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is that </src><tgt><\|wait\|></tgt>` | 1749 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat and </src><tgt><\|wait\|></tgt>` | 1910 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, </src><tgt><\|wait\|></tgt>` | 2129 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have </src><tgt><\|wait\|></tgt>` | 911 |
| 11 | `<src>changed from 20 </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>changed from </src><tgt>活動、そして自分自身で基準を定義すること。なぜなら、あなたは完全に正しいからです。しかし、現実は、私たちが新しい猫であり、ブロックであるからです。そして、基準は</tgt>` | 2221 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt><\|wait\|></tgt>` | 911 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1115 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our own standard </src><tgt><\|wait\|></tgt>` | 1192 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 550 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 814 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1426 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 955 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1249 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt><\|wait\|></tgt>` | 1303 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1267 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of </src><tgt><\|wait\|></tgt>` | 796 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>critical importance </src><tgt><\|wait\|></tgt>` | 1414 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1650 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 1494 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>systems, which is obviously </src><tgt><\|wait\|></tgt>` | 723 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt>最初のセクションで、AHRフィールドが変種データベースシステムよりも重要であるという点について、少しズレていました。変種データベースシステムは、もちろん大好きです。</tgt>` | 3469 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt><\|wait\|></tgt>` | 678 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>if we don't agree upon </src><tgt><\|wait\|></tgt>` | 1330 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields </src><tgt><\|wait\|></tgt>` | 1401 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1128 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 707 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 793 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 483 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 463 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 962 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 952 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry, </src><tgt><\|wait\|></tgt>` | 1279 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1356 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's been without food </src><tgt><\|wait\|></tgt>` | 1602 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in the wilderness </src><tgt><\|wait\|></tgt>` | 1637 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days, that he's hungry, </src><tgt><\|wait\|></tgt>` | 1808 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 1741 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, </src><tgt><\|wait\|></tgt>` | 543 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the Son of God, prove it </src><tgt><\|wait\|></tgt>` | 2755 |
| 11 | `<src><\|wait\|></src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>by turning these </src><tgt>ある時、彼はイエスが飢えていることを知っていました。40日間荒野で食べ物がないことを知っていました。だから彼はイエスに言いました。「もしあなたが神の御子なら、</tgt>` | 2426 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>stones to bread." </src><tgt><\|wait\|></tgt>` | 1229 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 657 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>say this? </src><tgt><\|wait\|></tgt>` | 1259 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>Deal with that temptation? </src><tgt><\|wait\|></tgt>` | 440 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 732 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 442 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>Alone. </src><tgt><\|wait\|></tgt>` | 462 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1310 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 991 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, and </src><tgt><\|wait\|></tgt>` | 1204 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>the Supreme Court </src><tgt><\|wait\|></tgt>` | 1203 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1215 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I don't know </src><tgt><\|wait\|></tgt>` | 828 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1823 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the the van </src><tgt><\|wait\|></tgt>` | 1615 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>ard of social </src><tgt><\|wait\|></tgt>` | 1773 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>change, </src><tgt><\|wait\|></tgt>` | 1355 |
| 11 | `<src>these days, </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为法院现在想成为社会变革的先锋，</tgt>` | `<src>these days. </src><tgt>有意义的个人权利，而最高法院是最后出现的，而不是引领者。我不知道法院是否想成为社会变革的先锋。</tgt>` | 2402 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 703 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 1095 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1082 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 804 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 1303 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 460 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 684 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 418 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 457 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 380 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>图片</src><tgt><\|wait\|></tgt>` | 1224 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1434 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是</src><tgt><\|wait\|></tgt>` | 1466 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>客订的部分，</src><tgt><\|wait\|></tgt>` | 1529 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>而客订一般</src><tgt><\|wait\|></tgt>` | 1385 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 939 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1621 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在修习的地方，</src><tgt><\|wait\|></tgt>` | 1533 |
| 11 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>所以呢，</src><tgt>그럼 사진을 한번 볼게요. 사진 부분에서 ' 고객 주문 ' 이라는 게 보이실 거예요. 보통 고객 주문은 우리가 수련하는 곳에서 나오는 거라, 그래서</tgt>` | 2663 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分</src><tgt><\|wait\|></tgt>` | 1177 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1004 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1025 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 1127 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地做</src><tgt><\|wait\|></tgt>` | 596 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>下来休息，</src><tgt><\|wait\|></tgt>` | 750 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可以看到这边是</src><tgt><\|wait\|></tgt>` | 408 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>空无一人的吗？</src><tgt><\|wait\|></tgt>` | 498 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 388 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 421 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 948 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1214 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1279 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1086 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>revolutionize the world. </src><tgt><\|wait\|></tgt>` | 800 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>is something </src><tgt><\|wait\|></tgt>` | 1663 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>that have a contradiction. </src><tgt><\|wait\|></tgt>` | 1780 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1251 |
| 11 | `<src>While they're </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>While they're </src><tgt>彼らは全く珍しい人々です。そして、彼らはしばしば世界を完全に革命しようと現れます。その性格は矛盾を抱えています。彼らは</tgt>` | 2887 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, they also </src><tgt><\|wait\|></tgt>` | 680 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate </src><tgt><\|wait\|></tgt>` | 936 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1470 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like to </src><tgt><\|wait\|></tgt>` | 723 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt><\|wait\|></tgt>` | 972 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 462 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 683 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 370 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>the devil's advocate, </src><tgt><\|wait\|></tgt>` | 500 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 385 |
| 22 | `<src>never shy away from a debate. </src><tgt>外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 415 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 362 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. stands for </src><tgt><\|wait\|></tgt>` | 380 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stand for. </src><tgt><\|wait\|></tgt>` | 319 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1059 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 793 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt><\|wait\|></tgt>` | 556 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1039 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのねフォールボス</src><tgt><\|wait\|></tgt>` | 1469 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>のホテルも朝食が</src><tgt><\|wait\|></tgt>` | 1572 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1617 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1302 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっているので</src><tgt><\|wait\|></tgt>` | 946 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1565 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>ここゴルドストンホテル</src><tgt>I'd like to make a meal after dinner. So, the breakfast at this Goldston Hotel is supposed to be available, so I'm looking forward to</tgt>` | 3342 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 724 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>な方はですね</src><tgt><\|wait\|></tgt>` | 1141 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討させて</src><tgt><\|wait\|></tgt>` | 811 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てもうまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 1207 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 995 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います</src><tgt><\|wait\|></tgt>` | 714 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 767 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 452 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 415 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本かかるか</src><tgt><\|wait\|></tgt>` | 325 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel, it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんでないか</src><tgt><\|wait\|></tgt>` | 271 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレデのね</src><tgt><\|wait\|></tgt>` | 370 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地ねまあホテル</src><tgt><\|wait\|></tgt>` | 372 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt><\|wait\|></tgt>` | 308 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 342 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 336 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください</src><tgt><\|wait\|></tgt>` | 314 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね</src><tgt><\|wait\|></tgt>` | 291 |

---

### Test Example 60 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1132 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>경무를 거부 한 </src><tgt><\|wait\|></tgt>` | 1000 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>맹병리 후보 를 </src><tgt><\|wait\|></tgt>` | 1264 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1372 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당술을 </src><tgt><\|wait\|></tgt>` | 1572 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1709 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1774 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1874 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2358 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 802 |
| 11 | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제권 순간 </src><tgt>Previously, Lee Jun- seok made it sound like he was running for the party's leadership to reject the party's leadership candidate, and even put on quite a show for the party's leadership. But now, as Yoon Suk- yeol's candidate Kim Jong- in takes the leadership, Lee Jun- seok</tgt>` | 3042 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1223 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1270 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 593 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼 를 품은 </src><tgt><\|wait\|></tgt>` | 589 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 346 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 459 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 391 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 412 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 351 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 성상급건. </src><tgt><\|wait\|></tgt>` | 394 |
| 22 | `<src><\|wait\|></src><tgt>Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 326 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 337 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt><\|wait\|></tgt>` | 322 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 318 |
